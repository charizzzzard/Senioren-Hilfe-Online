#!/usr/bin/env python3
"""Lesendes Cockpit für die Weiterentwicklung, kein Scheduler und keine Freigabe.

python tools/betrieb.py
python tools/betrieb.py --format json --pr-snapshot /privat/offene-prs.json
python tools/betrieb.py --validate

Kein Netzwerk, kein Build, keine Dateiänderung. Ausgabe nur nach stdout.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parent.parent
REPOSITORY = "charizzzzard/Senioren-Hilfe-Online"
STATES = {"proposed", "ready", "in_progress", "blocked", "in_review", "done", "cancelled"}
AREAS = {"operations", "quality", "product", "acquisition", "distribution", "community"}


class CockpitError(ValueError):
    pass


def mapping(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise CockpitError(f"{path}: YAML-Objekt erwartet")
    return value


def validate_registry(config: dict) -> list[str]:
    errors = []
    if config.get("schema_version") != 1 or config.get("mode") != "proposal":
        errors.append("schema_version: 1 und mode: proposal erwartet; keine automatische Aktivierung")
    for key in ("wip_limit", "pr_snapshot_max_age_hours"):
        if type(config.get(key)) is not int or config[key] < 1:
            errors.append(f"{key}: positive ganze Zahl erwartet")
    tasks = config.get("tasks")
    if not isinstance(tasks, list):
        return errors + ["tasks: Liste erwartet"]
    by_id = {}
    for task in tasks:
        if not isinstance(task, dict):
            errors.append("Aufgabe muss ein Objekt sein")
            continue
        ident = task.get("id")
        if not isinstance(ident, str) or not re.fullmatch(r"[A-Z]{2,5}-\d{3}", ident):
            errors.append(f"Ungültige Aufgabenkennung: {ident!r}")
            continue
        if ident in by_id:
            errors.append(f"Doppelte Kennung: {ident}")
        by_id[ident] = task
        for key in ("title", "owner", "metric"):
            if not isinstance(task.get(key), str) or not task[key].strip():
                errors.append(f"{ident}: {key} fehlt")
        if not isinstance(task.get("area"), str) or task["area"] not in AREAS or not isinstance(task.get("state"), str) or task["state"] not in STATES:
            errors.append(f"{ident}: unbekannter Bereich oder Zustand")
        if type(task.get("priority")) is not int or not 0 <= task["priority"] <= 3:
            errors.append(f"{ident}: priority muss 0 bis 3 sein")
        dependencies = task.get("depends_on")
        if not isinstance(dependencies, list) or any(not isinstance(x, str) for x in dependencies):
            errors.append(f"{ident}: depends_on muss eine Liste von Kennungen sein")
        criteria = task.get("acceptance")
        if not isinstance(criteria, list) or not criteria or any(not isinstance(x, str) or not x.strip() for x in criteria):
            errors.append(f"{ident}: mindestens ein konkretes Abnahmekriterium erforderlich")
        if task.get("state") == "blocked" and not task.get("blocker"):
            errors.append(f"{ident}: blockierte Aufgabe braucht blocker")
    graph = {}
    for ident, task in by_id.items():
        dependencies = task.get("depends_on")
        graph[ident] = dependencies if isinstance(dependencies, list) and all(isinstance(x, str) for x in dependencies) else []
        for dependency in graph[ident]:
            if dependency not in by_id:
                errors.append(f"{ident}: unbekannte Abhängigkeit {dependency}")
    visiting, visited = set(), set()

    def visit(ident):
        if ident in visiting:
            errors.append(f"Zyklische Abhängigkeit bei {ident}")
            return
        if ident in visited or ident not in graph:
            return
        visiting.add(ident)
        for dependency in graph[ident]:
            visit(dependency)
        visiting.remove(ident)
        visited.add(ident)

    for ident in graph:
        visit(ident)
    return errors


def date_value(value) -> dt.date | None:
    if isinstance(value, dt.datetime):
        return None
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value)
        except ValueError:
            pass
    return None


def content_inventory(root: Path, today: dt.date) -> dict:
    result = {"published": 0, "by_section": {}, "evidence_table_present": 0,
              "missing_evidence_tables": [], "source_review_overdue": [],
              "source_review_unknown": [], "device_test_claims": [],
              "evidence_note": "Dateipräsenz und Frontmatter sind keine bestätigte Fakten- oder Geräteprüfung."}
    for section in ("artikel", "lexikon"):
        result["by_section"][section] = 0
        folder = root / "content" / section
        if not folder.is_dir():
            raise CockpitError(f"Inhaltsverzeichnis fehlt: {folder}")
        for path in sorted(folder.glob("*.md")):
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", path.read_text(encoding="utf-8"), re.S)
            meta = yaml.safe_load(match.group(1)) if match else None
            if not isinstance(meta, dict):
                raise CockpitError(f"{path}: Frontmatter fehlt oder ist ungültig")
            published = date_value(meta.get("veroeffentlicht"))
            if not published:
                raise CockpitError(f"{path}: Veröffentlichungsdatum fehlt oder ist ungültig")
            if meta.get("entwurf") or published > today:
                continue
            ident = f"{section}/{path.stem}"
            result["published"] += 1
            result["by_section"][section] += 1
            evidence = root / "content" / "belege" / section / (path.stem + ".yaml")
            if evidence.is_file():
                result["evidence_table_present"] += 1
            else:
                result["missing_evidence_tables"].append(ident)
            reviewed = date_value(meta.get("geprueft"))
            if not reviewed or reviewed > today:
                result["source_review_unknown"].append(ident)
            elif (today - reviewed).days > 180:
                result["source_review_overdue"].append(ident)
            if meta.get("getestet"):
                result["device_test_claims"].append({"text": ident, "claim": str(meta["getestet"])})
    return result


def archive_status(root: Path, today: dt.date) -> dict:
    """Zeigt Originalwerte und Auswertbarkeit; ersetzt keine kennzahlen.py-Berechnung."""
    path = root / "kennzahlen" / "wochen.csv"
    if not path.is_file():
        return {"status": "unavailable", "comparison_ready": False, "reason": "Wochenarchiv fehlt"}
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    seen = set()
    for row in rows:
        week = row.get("woche", "")
        if week in seen:
            raise CockpitError(f"Doppelte Archivwoche: {week}")
        seen.add(week)
        try:
            year, number = map(int, week.split("-W"))
            monday = dt.date.fromisocalendar(year, number, 1)
            if monday > today:
                raise ValueError("Woche liegt in der Zukunft")
            if row["von"] != monday.isoformat() or row["bis"] != (monday + dt.timedelta(days=6)).isoformat():
                raise ValueError("abweichende ISO-Grenzen")
            if date_value(row.get("stand")) is None or date_value(row["stand"]) > today:
                raise ValueError("ungültiger oder zukünftiger Abrufstand")
            if row.get("daten") not in {"final", "vorlaeufig"}:
                raise ValueError("unbekannter Datenstatus")
            for field in ("klicks", "impressionen"):
                if int(row[field]) < 0:
                    raise ValueError("negative Summe")
            if row["daten"] == "final" and (date_value(row["stand"]) - date_value(row["bis"])).days < 4:
                raise ValueError("final vor Ablauf der Datenverzögerung")
        except (ValueError, TypeError, KeyError) as exc:
            raise CockpitError(f"Ungültige Archivwoche {week!r}: {exc}") from exc
    rows.sort(key=lambda row: row["von"])
    completed = [row for row in rows if date_value(row["bis"]) < today]
    recent = completed[-8:]
    consecutive = len(recent) == 8 and all(
        (date_value(b["von"]) - date_value(a["von"])).days == 7 for a, b in zip(recent, recent[1:]))
    ready = consecutive and all(row["daten"] == "final" for row in recent)
    latest_complete = today - dt.timedelta(days=today.weekday() + 1)
    delay = (latest_complete - date_value(completed[-1]["bis"])).days if completed else None
    if delay is not None and delay > 7:
        ready = False
    return {"status": "available" if rows else "empty", "weeks": len(rows),
            "latest": rows[-1] if rows else None, "comparison_ready": ready,
            "archive_delay_days": delay,
            "reason": "Acht aufeinanderfolgende finale Wochen erforderlich; Archiv darf höchstens eine Woche zurückliegen.",
            "analysis_command": "python tools/kennzahlen.py auswerten",
            "note": "Archivstand, kein neuer GSC-Abruf. Indexzahlen bleiben datierte Momentaufnahmen."}


def pipeline_status(snapshot: Path | None, now: dt.datetime, max_age_hours: int) -> dict:
    if snapshot is None:
        return {"status": "unavailable", "reason": "Kein PR-Snapshot; offene Arbeit ist unbekannt, nicht null."}
    data = json.loads(snapshot.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("repository") != REPOSITORY:
        raise CockpitError("PR-Snapshot: Version oder Repository ungültig")
    try:
        fetched = dt.datetime.fromisoformat(data["fetched_at"].replace("Z", "+00:00"))
        if fetched.tzinfo is None:
            raise ValueError("Zeitzone fehlt")
    except (KeyError, ValueError, TypeError, AttributeError) as exc:
        raise CockpitError("PR-Snapshot: fetched_at muss einen Zeitpunkt mit Zeitzone enthalten") from exc
    age = (now - fetched).total_seconds() / 3600
    if age < -0.1:
        raise CockpitError("PR-Snapshot liegt in der Zukunft")
    prs = data.get("pull_requests")
    if not isinstance(prs, list):
        raise CockpitError("PR-Snapshot: pull_requests muss eine Liste sein")
    numbers = set()
    counts = {"open": 0, "draft": 0, "awaiting_review": 0, "rework": 0, "objection": 0}
    for pr in prs:
        if not isinstance(pr, dict) or type(pr.get("number")) is not int or pr["number"] < 1:
            raise CockpitError("PR-Snapshot: ungültige PR-Nummer")
        if pr["number"] in numbers:
            raise CockpitError("PR-Snapshot enthält doppelte PRs")
        numbers.add(pr["number"])
        labels = pr.get("labels")
        if not isinstance(labels, list) or any(not isinstance(x, str) for x in labels) or type(pr.get("draft")) is not bool:
            raise CockpitError("PR-Snapshot: labels oder draft ungültig")
        if not isinstance(pr.get("head_sha"), str) or not re.fullmatch(r"[0-9a-f]{40}", pr["head_sha"]):
            raise CockpitError("PR-Snapshot: vollständige Head-SHA erforderlich")
        counts["open"] += 1
        if pr["draft"]:
            counts["draft"] += 1
            continue
        counts["awaiting_review"] += "pruefung-ausstehend" in labels
        counts["rework"] += "pruefung-nachbessern" in labels
        counts["objection"] += "einspruch" in labels
    status = "available"
    if data.get("complete") is not True:
        status = "partial"
    elif age > max_age_hours:
        status = "stale"
    return {"status": status, "fetched_at": fetched.isoformat(), "age_hours": round(age, 1),
            "counts": counts, "note": "Momentaufnahme; Labels sind keine bestätigte Mergefreigabe. Bei partial/stale nur bekannte Teilzahlen."}


def build_report(root: Path, config: dict, now: dt.datetime, snapshot: Path | None) -> dict:
    errors = validate_registry(config)
    if errors:
        raise CockpitError("; ".join(errors))
    active = [task for task in config["tasks"] if task["state"] in {"in_progress", "in_review"}]
    by_id = {task["id"]: task for task in config["tasks"]}
    candidates = [task for task in config["tasks"] if task["state"] in {"proposed", "ready"}
                  and all(by_id[dependency]["state"] == "done" for dependency in task["depends_on"])]
    candidates.sort(key=lambda task: (task["priority"], task["id"]))
    slots = max(0, config["wip_limit"] - len(active))
    return {"generated_at": now.isoformat(), "mode": "proposal", "release_authority": False,
            "content": content_inventory(root, now.date()), "search_archive": archive_status(root, now.date()),
            "pipeline": pipeline_status(snapshot, now, config["pr_snapshot_max_age_hours"]),
            "development": {"wip_limit": config["wip_limit"], "active": active,
                            "wip_exceeded": len(active) > config["wip_limit"],
                            "next_candidates": candidates[:slots]},
            "not_measured": ["Tatsächlicher Aufgabenabschluss älterer Leser", "Aktuelle Gerätebeweis-Abdeckung",
                             "Empfehlungen und Nutzung durch Einrichtungen", "Ausgaben und Serverzustand"],
            "policy_checks": "Nicht ausgeführt. Verbindlich bleiben check.py und docs/BETRIEB.md."}


def markdown_report(report: dict) -> str:
    content, archive, pipeline, development = (report[k] for k in ("content", "search_archive", "pipeline", "development"))
    lines = ["# Netzleicht: Betriebsübersicht", "", f"Stand: {report['generated_at']}. Lesender Vorschlag, keine Freigabe.", "",
             f"- Veröffentlichte Inhaltstexte: {content['published']} ({content['by_section']['artikel']} Artikel, {content['by_section']['lexikon']} Lexikon).",
             f"- Belegdatei vorhanden: {content['evidence_table_present']}; fehlend: {len(content['missing_evidence_tables'])}.",
             f"- Quellen-Prüfdatum älter als 180 Tage: {len(content['source_review_overdue'])}; unbekannt/ungültig: {len(content['source_review_unknown'])}.",
             f"- Texte mit Geräte-Testangabe: {len(content['device_test_claims'])}; Angaben wurden hier nicht verifiziert.",
             f"- Sucharchiv: {archive['status']}; zwei Vierwochenfenster auswertbar: {'ja' if archive['comparison_ready'] else 'nein'}.",
             f"- PR-Daten: {pipeline['status']}."]
    if archive.get("latest"):
        row = archive["latest"]
        lines.append(f"- Letzte Archivwoche {row['woche']}: {row['klicks']} Klicks, {row['impressionen']} Impressionen; {row['daten']}, Abruf {row['stand']}.")
    if pipeline.get("counts"):
        count = pipeline["counts"]
        lines.append(f"- Bekannte PRs: {count['open']}, davon Entwürfe {count['draft']}; Prüfung ausstehend {count['awaiting_review']}, Nachbesserung {count['rework']}, Einspruch {count['objection']}.")
    lines.extend(["", "## Weiterentwicklung", "", f"Aktive zusätzliche Vorhaben: {len(development['active'])}/{development['wip_limit']}."])
    if development["wip_exceeded"]:
        lines.append("WIP-Limit überschritten: begonnene Arbeit abschließen, weitere Vorhaben zurückstellen.")
    for task in development["active"]:
        lines.append(f"- {task['id']}: {task['title']} ({task['state']}).")
    for task in development["next_candidates"]:
        lines.append(f"- Nächster Vorschlag: {task['id']} – {task['title']}.")
    if not development["next_candidates"]:
        lines.append("Kein weiteres Vorhaben vorgeschlagen; laufende Arbeit oder Abhängigkeiten zuerst klären.")
    if content["missing_evidence_tables"]:
        lines.extend(["", "## Fehlende Belegdateien", ""] + [f"- {item}" for item in content["missing_evidence_tables"]])
    lines.extend(["", "## Grenzen", "", content["evidence_note"], archive.get("note", archive.get("reason", "")),
                  "Offene PRs können fehlende Dateien bereits bearbeiten: vor neuer Arbeit den aktuellen GitHub-Stand abgleichen.",
                  report["policy_checks"], "", "Nicht gemessen:", ""] + [f"- {item}" for item in report["not_measured"]])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=ROOT / "ops/betriebssystem.yaml")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--pr-snapshot", type=Path)
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()
    try:
        config = mapping(args.registry)
        errors = validate_registry(config)
        if errors:
            raise CockpitError("; ".join(errors))
        if args.validate:
            print("Aufgabenregister gültig. Keine Aktivierung oder Ausführung.")
            return 0
        report = build_report(ROOT, config, dt.datetime.now(ZoneInfo("Europe/Berlin")), args.pr_snapshot)
        print(json.dumps(report, ensure_ascii=False, indent=2) if args.format == "json" else markdown_report(report), end="\n" if args.format == "json" else "")
        return 0
    except (CockpitError, OSError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"Betriebsübersicht nicht verfügbar: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
