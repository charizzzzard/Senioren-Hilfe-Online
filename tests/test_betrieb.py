"""Betriebsinvarianten des lesenden Cockpits, ohne Netzwerk oder echte Konten."""
import copy
import csv
import datetime as dt
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("betrieb", Path(__file__).resolve().parents[1] / "tools/betrieb.py")
betrieb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(betrieb)


def registry():
    return {"schema_version": 1, "mode": "proposal", "wip_limit": 1, "pr_snapshot_max_age_hours": 48,
            "tasks": [{"id": "SYS-001", "title": "Prüfen", "area": "operations", "priority": 0,
                       "state": "proposed", "owner": "betrieb", "metric": "Befund", "depends_on": [],
                       "acceptance": ["Ergebnis unabhängig geprüft"]}]}


class RegistryTests(unittest.TestCase):
    def test_dependency_cycle_and_unknown_dependency_rejected(self):
        config = registry()
        config["tasks"][0]["depends_on"] = ["SYS-001", "SYS-999"]
        errors = " ".join(betrieb.validate_registry(config))
        self.assertIn("Zyklische", errors)
        self.assertIn("unbekannte Abhängigkeit", errors)

    def test_duplicate_ids_and_unexplained_blocker_rejected(self):
        config = registry()
        config["tasks"].append(copy.deepcopy(config["tasks"][0]))
        config["tasks"][1]["state"] = "blocked"
        errors = " ".join(betrieb.validate_registry(config))
        self.assertIn("Doppelte", errors)
        self.assertIn("blocker", errors)

    def test_no_automatic_promotion_to_active_mode(self):
        config = registry()
        config["mode"] = "active"
        self.assertTrue(betrieb.validate_registry(config))

    def test_invalid_types_produce_validation_errors(self):
        config = registry()
        config["wip_limit"] = True
        config["tasks"][0]["state"] = []
        config["tasks"][0]["depends_on"] = [123]
        self.assertTrue(betrieb.validate_registry(config))


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for section in ("artikel", "lexikon"):
            (self.root / "content" / section).mkdir(parents=True)

    def write_text(self, slug, extra="", date="2026-11-01"):
        path = self.root / "content/artikel" / (slug + ".md")
        path.write_text(f"---\nveroeffentlicht: {date}\ngeprueft: 2026-11-01\n{extra}---\nText\n", encoding="utf-8")

    def test_drafts_future_dates_and_noncontent_pages_excluded(self):
        self.write_text("live")
        self.write_text("draft", "entwurf: true\n")
        self.write_text("future", date="2026-12-01")
        (self.root / "content/seiten").mkdir()
        (self.root / "content/seiten/kontakt.md").write_text("Kontakt")
        result = betrieb.content_inventory(self.root, dt.date(2026, 11, 14))
        self.assertEqual(result["published"], 1)
        self.assertEqual(result["missing_evidence_tables"], ["artikel/live"])

    def test_presence_and_claim_are_not_verified_evidence(self):
        self.write_text("live", "getestet: Ein Geräteversprechen\n")
        folder = self.root / "content/belege/artikel"
        folder.mkdir(parents=True)
        (folder / "live.yaml").write_text("kein gültiger Nachweis")
        result = betrieb.content_inventory(self.root, dt.date(2026, 11, 14))
        self.assertEqual(result["evidence_table_present"], 1)
        self.assertEqual(len(result["device_test_claims"]), 1)
        self.assertIn("keine bestätigte", result["evidence_note"])
        self.assertNotIn("verified_device_tests", result)

    def test_invalid_publication_is_error_not_zero_work(self):
        self.write_text("bad", date="unbekannt")
        with self.assertRaises(betrieb.CockpitError):
            betrieb.content_inventory(self.root, dt.date(2026, 11, 14))


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "kennzahlen").mkdir()
        self.today = dt.date(2026, 11, 14)

    def write_weeks(self, starts, provisional=False):
        rows = []
        for start in starts:
            year, week, _ = start.isocalendar()
            rows.append({"woche": f"{year}-W{week:02d}", "von": start.isoformat(),
                         "bis": (start + dt.timedelta(days=6)).isoformat(), "klicks": "3", "impressionen": "40",
                         "daten": "vorlaeufig" if provisional else "final", "stand": "2026-11-14"})
        with (self.root / "kennzahlen/wochen.csv").open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    def test_eight_final_consecutive_weeks_are_ready(self):
        starts = [dt.date(2026, 9, 14) + dt.timedelta(weeks=i) for i in range(8)]
        self.write_weeks(starts)
        result = betrieb.archive_status(self.root, self.today)
        self.assertTrue(result["comparison_ready"])
        self.assertNotIn("growth_percent", result)

    def test_eight_rows_with_gap_or_provisional_are_not_ready(self):
        starts = [dt.date(2026, 9, 7) + dt.timedelta(weeks=i) for i in range(9)]
        starts.pop(3)
        self.write_weeks(starts)
        self.assertFalse(betrieb.archive_status(self.root, self.today)["comparison_ready"])
        self.write_weeks(starts, provisional=True)
        self.assertFalse(betrieb.archive_status(self.root, self.today)["comparison_ready"])

    def test_stale_eight_weeks_are_not_ready(self):
        starts = [dt.date(2026, 7, 6) + dt.timedelta(weeks=i) for i in range(8)]
        self.write_weeks(starts)
        self.assertFalse(betrieb.archive_status(self.root, self.today)["comparison_ready"])

    def test_duplicate_weeks_fail(self):
        self.write_weeks([dt.date(2026, 11, 2)] * 2)
        with self.assertRaises(betrieb.CockpitError):
            betrieb.archive_status(self.root, self.today)

    def test_final_data_too_early_fail(self):
        self.write_weeks([dt.date(2026, 11, 9)])
        with self.assertRaises(betrieb.CockpitError):
            betrieb.archive_status(self.root, self.today)

    def test_missing_archive_is_unknown(self):
        self.assertEqual(betrieb.archive_status(self.root, self.today)["status"], "unavailable")


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "prs.json"
        self.now = dt.datetime(2026, 11, 14, 23, tzinfo=dt.timezone.utc)
        self.data = {"schema_version": 1, "repository": betrieb.REPOSITORY,
                     "fetched_at": "2026-11-14T22:00:00Z", "complete": True,
                     "pull_requests": [{"number": 1, "draft": False, "head_sha": "a" * 40,
                                        "labels": ["pruefung-ausstehend", "klasse-c", "gelesen"]}]}

    def run_snapshot(self):
        self.path.write_text(json.dumps(self.data), encoding="utf-8")
        return betrieb.pipeline_status(self.path, self.now, 48)

    def test_absence_is_not_empty_queue(self):
        result = betrieb.pipeline_status(None, self.now, 48)
        self.assertEqual(result["status"], "unavailable")
        self.assertNotIn("counts", result)

    def test_draft_does_not_consume_review_queue(self):
        self.data["pull_requests"][0]["draft"] = True
        result = self.run_snapshot()
        self.assertEqual(result["counts"]["draft"], 1)
        self.assertEqual(result["counts"]["awaiting_review"], 0)

    def test_stale_partial_and_future_snapshots_distinct(self):
        self.data["fetched_at"] = "2026-11-10T22:00:00Z"
        self.assertEqual(self.run_snapshot()["status"], "stale")
        self.data["complete"] = False
        self.assertEqual(self.run_snapshot()["status"], "partial")
        self.data["fetched_at"] = "2026-11-15T22:00:00Z"
        with self.assertRaises(betrieb.CockpitError):
            self.run_snapshot()

    def test_duplicate_pr_and_invalid_sha_rejected(self):
        self.data["pull_requests"].append(copy.deepcopy(self.data["pull_requests"][0]))
        with self.assertRaises(betrieb.CockpitError):
            self.run_snapshot()
        self.data["pull_requests"].pop()
        self.data["pull_requests"][0]["head_sha"] = None
        with self.assertRaises(betrieb.CockpitError):
            self.run_snapshot()

    def test_label_is_not_an_approval(self):
        result = self.run_snapshot()
        self.assertNotIn("ready_to_merge", result)
        self.assertIn("keine bestätigte", result["note"])


class SchedulingAdviceTests(unittest.TestCase):
    def test_wip_and_dependencies_prevent_new_work(self):
        config = registry()
        config["tasks"][0]["state"] = "in_review"
        second = copy.deepcopy(config["tasks"][0])
        second.update(id="DEV-001", state="proposed", depends_on=["SYS-001"])
        config["tasks"].append(second)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for section in ("artikel", "lexikon"):
                (root / "content" / section).mkdir(parents=True)
            now = dt.datetime(2026, 11, 14, tzinfo=dt.timezone.utc)
            report = betrieb.build_report(root, config, now, None)
            self.assertEqual(report["development"]["next_candidates"], [])
            self.assertFalse(report["release_authority"])
            config["tasks"][0]["state"] = "done"
            report = betrieb.build_report(root, config, now, None)
            self.assertEqual(report["development"]["next_candidates"][0]["id"], "DEV-001")
            config["tasks"][0]["state"] = "cancelled"
            report = betrieb.build_report(root, config, now, None)
            self.assertEqual(report["development"]["next_candidates"], [])


if __name__ == "__main__":
    unittest.main()
