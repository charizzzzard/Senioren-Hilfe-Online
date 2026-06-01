#!/usr/bin/env python3
"""Validate SHO-OS content contracts without external dependencies.

The checks are intentionally dependency-free and text-based. They support the
current constrained YAML/frontmatter shapes in this repository, but they are not
a substitute for a real YAML parser or full publish-gate validator.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "README.md",
    "docs/00_PROJECT_SYSTEM_DEFINITION.md",
    "docs/content/MVP_CONTENT_BACKLOG.yaml",
    "docs/content/CONTENT_BRIEF_TEMPLATE.md",
    "docs/architecture/CAPABILITY_MAP.yaml",
    "docs/governance/TRUST_AND_MONETIZATION_POLICY.md",
    "docs/governance/SOURCE_AND_EVIDENCE_STANDARD.md",
    "docs/governance/CONTENT_REVIEW_GATE.md",
    "docs/governance/OPERATOR_ACCEPTANCE_POLICY.md",
    "external_review_packet/00_READ_ME_FIRST.md",
    "external_review_packet/HANDOFF_LATEST_CONTEXT.md",
]

REQUIRED_BACKLOG_FIELDS = {
    "title",
    "slug",
    "cluster",
    "priority",
    "risk_level",
    "monetization_allowed_initially",
    "status",
}

ALLOWED_RISK_LEVELS = {"low", "medium", "high"}
SECURITY_TERMS = ("betrug", "sicherheit", "blockieren", "app-berechtigungen")

EXPECTED_BRIEF_FILES = {
    "whatsapp-fuer-senioren-sicher-einrichten.md",
    "betrugsnachrichten-auf-whatsapp-erkennen.md",
    "smartphone-schriftgroesse-und-bedienhilfen-einstellen.md",
    "smartphone-fuer-senioren-einrichten.md",
}

REQUIRED_BRIEF_FIELDS = {
    "brief_id",
    "title",
    "slug",
    "cluster",
    "target_audience",
    "primary_user_problem",
    "search_intent",
    "differentiation_angle",
    "risk_level",
    "monetization_allowed_initially",
    "affiliate_allowed_initially",
    "review_status",
    "operator_acceptance_status",
    "content_status",
}


def parse_simple_list_items(text: str, item_start_key: str) -> list[dict[str, str]]:
    """Parse a constrained YAML list whose entries start with a known key."""
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    start_pattern = re.compile(rf"^\s*-\s+{re.escape(item_start_key)}:\s*(.*)$")

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        start_match = start_pattern.match(line)
        if start_match:
            if current is not None:
                items.append(current)
            current = {item_start_key: start_match.group(1).strip()}
            continue

        if current is None:
            continue

        match = re.match(r"^\s+([A-Za-z0-9_]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            current[key] = value.strip()

    if current is not None:
        items.append(current)

    return items


def parse_frontmatter_fields(text: str) -> dict[str, str]:
    """Parse top-level scalar/list keys from a Markdown frontmatter block."""
    fields: dict[str, str] = {}
    if not text.startswith("---"):
        return fields

    parts = text.split("---", 2)
    if len(parts) < 3:
        return fields

    for raw_line in parts[1].splitlines():
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", raw_line.rstrip())
        if match:
            key, value = match.groups()
            fields[key] = value.strip()

    return fields


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() == "true"


def normalized(value: str | None) -> str:
    return (value or "").strip().lower()


def has_security_context(fields: dict[str, str]) -> bool:
    searchable = " ".join(
        [
            fields.get("title", ""),
            fields.get("slug", ""),
            fields.get("cluster", ""),
            fields.get("primary_user_problem", ""),
        ]
    ).lower()
    return any(term in searchable for term in SECURITY_TERMS)


def validate_required_docs(failures: list[str]) -> None:
    for rel_path in REQUIRED_DOCS:
        if not (ROOT / rel_path).exists():
            failures.append(f"Missing required file: {rel_path}")


def validate_backlog(failures: list[str]) -> int:
    backlog_path = ROOT / "docs/content/MVP_CONTENT_BACKLOG.yaml"
    if not backlog_path.exists():
        failures.append("Missing backlog: docs/content/MVP_CONTENT_BACKLOG.yaml")
        return 0

    articles = parse_simple_list_items(backlog_path.read_text(encoding="utf-8"), "title")
    if len(articles) < 8:
        failures.append(f"Backlog must contain at least 8 article entries; found {len(articles)}")

    seen_slugs: set[str] = set()
    for index, article in enumerate(articles, start=1):
        missing = REQUIRED_BACKLOG_FIELDS - set(article)
        if missing:
            failures.append(
                f"Backlog entry {index} is missing required fields: {', '.join(sorted(missing))}"
            )

        slug = article.get("slug", "")
        if slug in seen_slugs:
            failures.append(f"Backlog slug must be unique: {slug}")
        if slug:
            seen_slugs.add(slug)

        risk_level = normalized(article.get("risk_level"))
        if risk_level and risk_level not in ALLOWED_RISK_LEVELS:
            failures.append(
                f"Backlog entry {index} has invalid risk_level '{article.get('risk_level')}'"
            )

        if has_security_context(article) and is_true(article.get("monetization_allowed_initially")):
            failures.append(
                "Security/fraud backlog entry must not allow initial monetization: "
                f"{article.get('title', f'entry {index}')}"
            )

    return len(articles)


def validate_brief_scaffolds(failures: list[str]) -> int:
    briefs_dir = ROOT / "docs/content/briefs"
    if not briefs_dir.exists():
        failures.append("Missing brief scaffold directory: docs/content/briefs")
        return 0

    found_files = {path.name for path in briefs_dir.glob("*.md")}
    missing_files = EXPECTED_BRIEF_FILES - found_files
    extra_files = found_files - EXPECTED_BRIEF_FILES

    for file_name in sorted(missing_files):
        failures.append(f"Missing expected brief scaffold: docs/content/briefs/{file_name}")
    for file_name in sorted(extra_files):
        failures.append(f"Unexpected brief scaffold in Batch 01: docs/content/briefs/{file_name}")

    for file_name in sorted(EXPECTED_BRIEF_FILES & found_files):
        path = briefs_dir / file_name
        fields = parse_frontmatter_fields(path.read_text(encoding="utf-8"))
        missing = REQUIRED_BRIEF_FIELDS - set(fields)
        if missing:
            failures.append(
                f"Brief {file_name} is missing required fields: {', '.join(sorted(missing))}"
            )

        if normalized(fields.get("content_status")) != "scaffold_only":
            failures.append(f"Brief {file_name} must have content_status: scaffold_only")
        if normalized(fields.get("review_status")) == "approved_for_publish":
            failures.append(f"Brief {file_name} must not be approved_for_publish")
        if normalized(fields.get("operator_acceptance_status")) == "accepted":
            failures.append(f"Brief {file_name} must not have accepted operator status")
        if has_security_context(fields) and is_true(fields.get("monetization_allowed_initially")):
            failures.append(
                f"Security/fraud brief must not allow initial monetization: {file_name}"
            )

    return len(found_files)


def main() -> int:
    failures: list[str] = []

    validate_required_docs(failures)
    backlog_count = validate_backlog(failures)
    brief_count = validate_brief_scaffolds(failures)

    if failures:
        print("FAIL: SHO-OS content contract validation failed")
        for failure in failures:
            print(f"- {failure}")
        print("- YAML/frontmatter parsing: dependency-free and text-based")
        return 1

    print("PASS: SHO-OS content contract validation passed")
    print(f"- Required documentation files present: {len(REQUIRED_DOCS)}")
    print(f"- MVP backlog article entries: {backlog_count}")
    print(f"- Batch 01 brief scaffold files: {brief_count}")
    print("- YAML/frontmatter parsing: dependency-free and text-based")
    return 0


if __name__ == "__main__":
    sys.exit(main())
