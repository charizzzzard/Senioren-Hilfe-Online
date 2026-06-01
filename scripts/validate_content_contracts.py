#!/usr/bin/env python3
"""Validate initial SHO-OS content contracts without external dependencies.

This script intentionally performs a small text-based YAML check instead of
using a full YAML parser. It is suitable for the current simple backlog shape,
but it must be replaced or expanded before validating arbitrary YAML.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "README.md",
    "docs/00_PROJECT_SYSTEM_DEFINITION.md",
    "docs/strategy/POSITIONING.md",
    "docs/strategy/MVP_SCOPE.md",
    "docs/strategy/MONETIZATION_THESIS.md",
    "docs/architecture/SYSTEM_MAP.md",
    "docs/architecture/CAPABILITY_MAP.yaml",
    "docs/architecture/CONTENT_PIPELINE.md",
    "docs/governance/TRUST_AND_MONETIZATION_POLICY.md",
    "docs/governance/SOURCE_AND_EVIDENCE_STANDARD.md",
    "docs/governance/CONTENT_REVIEW_GATE.md",
    "docs/governance/ACCESSIBILITY_AND_SENIOR_UX_STANDARD.md",
    "docs/governance/OPERATOR_ACCEPTANCE_POLICY.md",
    "docs/content/ARTICLE_TEMPLATE.md",
    "docs/content/CONTENT_BRIEF_TEMPLATE.md",
    "docs/content/MVP_CONTENT_BACKLOG.yaml",
    "docs/content/TOPIC_CLUSTER_MAP.md",
    "docs/operations/PUBLISHING_RUNBOOK.md",
    "docs/operations/REVIEW_RUNBOOK.md",
    "docs/operations/METRICS_AND_LEARNING_LOOP.md",
    "docs/operations/HANDOFF_STANDARD.md",
    "docs/engineering/ENGINEERING_PRINCIPLES.md",
    "docs/engineering/STATIC_SITE_REQUIREMENTS.md",
    "docs/engineering/VALIDATION_REQUIREMENTS.md",
    "external_review_packet/00_READ_ME_FIRST.md",
    "external_review_packet/HANDOFF_LATEST_CONTEXT.md",
]

REQUIRED_BACKLOG_FIELDS = {"title", "slug", "cluster", "priority", "status"}
SECURITY_TERMS = ("betrug", "sicherheit", "whatsapp kontakt blockieren", "app-berechtigungen")


def parse_simple_backlog(text: str) -> list[dict[str, str]]:
    """Parse the constrained backlog list shape used in this repository."""
    articles: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if re.match(r"^\s*-\s+title:\s*", line):
            if current is not None:
                articles.append(current)
            current = {}
            key, value = line.split(":", 1)
            current["title"] = value.strip()
            continue

        if current is None:
            continue

        match = re.match(r"^\s+([A-Za-z0-9_]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            current[key] = value.strip()

    if current is not None:
        articles.append(current)

    return articles


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() == "true"


def main() -> int:
    failures: list[str] = []

    for rel_path in REQUIRED_DOCS:
        path = ROOT / rel_path
        if not path.exists():
            failures.append(f"Missing required file: {rel_path}")

    backlog_path = ROOT / "docs/content/MVP_CONTENT_BACKLOG.yaml"
    articles: list[dict[str, str]] = []
    if backlog_path.exists():
        articles = parse_simple_backlog(backlog_path.read_text(encoding="utf-8"))
        if len(articles) < 8:
            failures.append(f"Backlog must contain at least 8 article entries; found {len(articles)}")

        for index, article in enumerate(articles, start=1):
            missing = REQUIRED_BACKLOG_FIELDS - set(article)
            if missing:
                failures.append(
                    f"Backlog entry {index} is missing required fields: {', '.join(sorted(missing))}"
                )

            searchable = " ".join(
                [article.get("title", ""), article.get("slug", ""), article.get("cluster", "")]
            ).lower()
            if any(term in searchable for term in SECURITY_TERMS) and is_true(
                article.get("monetization_allowed_initially")
            ):
                failures.append(
                    "Security/fraud backlog entry must not allow initial monetization: "
                    f"{article.get('title', f'entry {index}')}"
                )

    if failures:
        print("FAIL: SHO-OS content contract validation failed")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS: SHO-OS content contract validation passed")
    print(f"- Required documentation files present: {len(REQUIRED_DOCS)}")
    print(f"- MVP backlog article entries: {len(articles)}")
    print("- Text-based YAML check: limited to the current simple backlog structure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
