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
    "docs/content/research_inputs/README.md",
    "docs/content/source_packs/README.md",
    "docs/content/source_packs/SOURCE_PACK_TEMPLATE.md",
    "docs/content/source_packs/operator-research-source-pack-batch-01.md",
    "docs/content/claim_maps/README.md",
    "docs/content/claim_maps/CLAIM_MAP_TEMPLATE.md",
    "docs/content/claim_maps/source-to-claim-map-batch-01.md",
    "docs/content/source_reviews/README.md",
    "docs/content/source_reviews/whatsapp-source-manual-review-batch-01.md",
    "docs/content/evidence_captures/README.md",
    "docs/content/evidence_captures/EVIDENCE_CAPTURE_TEMPLATE.md",
    "docs/content/evidence_captures/whatsapp-line-evidence-capture-batch-01.md",
    "docs/content/serp_observations/README.md",
    "docs/content/serp_observations/SERP_OBSERVATION_TEMPLATE.md",
    "docs/content/serp_observations/serp-observation-batch-01.md",
    "docs/content/research_enrichments/README.md",
    "docs/content/research_enrichments/RESEARCH_ENRICHMENT_TEMPLATE.md",
    "docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md",
    "docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md",
    "docs/operations/CONTENT_RESEARCH_OPERATING_PROTOCOL.md",
    "docs/operations/RESEARCH_BATCH_STAGE_MODEL.md",
    "docs/operations/CODEX_EXECUTOR_BOUNDARY.md",
    "docs/content/BATCH_WORKFLOW_TEMPLATE.md",
    "docs/operations/NEXT_STAGE_DECISION_TREE.md",
    "docs/operations/STATUS_REGISTRY.yaml",
    "docs/content/batches/MVP_BATCH_01.yaml",
    "scripts/validate_stage_transitions.py",
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

EXPECTED_RESEARCH_FILES = {
    "whatsapp-fuer-senioren-sicher-einrichten.research.md": {
        "brief_file": "whatsapp-fuer-senioren-sicher-einrichten.md",
        "brief_id": "SHO-MVP-BRIEF-001",
        "research_id": "SHO-MVP-RESEARCH-001",
        "slug": "whatsapp-fuer-senioren-sicher-einrichten",
    },
    "betrugsnachrichten-auf-whatsapp-erkennen.research.md": {
        "brief_file": "betrugsnachrichten-auf-whatsapp-erkennen.md",
        "brief_id": "SHO-MVP-BRIEF-002",
        "research_id": "SHO-MVP-RESEARCH-002",
        "slug": "betrugsnachrichten-auf-whatsapp-erkennen",
    },
    "smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md": {
        "brief_file": "smartphone-schriftgroesse-und-bedienhilfen-einstellen.md",
        "brief_id": "SHO-MVP-BRIEF-003",
        "research_id": "SHO-MVP-RESEARCH-003",
        "slug": "smartphone-schriftgroesse-und-bedienhilfen-einstellen",
    },
    "smartphone-fuer-senioren-einrichten.research.md": {
        "brief_file": "smartphone-fuer-senioren-einrichten.md",
        "brief_id": "SHO-MVP-BRIEF-004",
        "research_id": "SHO-MVP-RESEARCH-004",
        "slug": "smartphone-fuer-senioren-einrichten",
    },
}

SOURCE_PACK_PATH = ROOT / "docs/content/source_packs/operator-research-source-pack-batch-01.md"
SOURCE_PACK_REL_PATH = "docs/content/source_packs/operator-research-source-pack-batch-01.md"
CLAIM_MAP_PATH = ROOT / "docs/content/claim_maps/source-to-claim-map-batch-01.md"
CLAIM_MAP_REL_PATH = "docs/content/claim_maps/source-to-claim-map-batch-01.md"
SOURCE_REVIEW_PATH = ROOT / "docs/content/source_reviews/whatsapp-source-manual-review-batch-01.md"
SOURCE_REVIEW_REL_PATH = "docs/content/source_reviews/whatsapp-source-manual-review-batch-01.md"
EVIDENCE_CAPTURE_PATH = ROOT / "docs/content/evidence_captures/whatsapp-line-evidence-capture-batch-01.md"
EVIDENCE_CAPTURE_REL_PATH = "docs/content/evidence_captures/whatsapp-line-evidence-capture-batch-01.md"
SERP_OBSERVATION_PATH = ROOT / "docs/content/serp_observations/serp-observation-batch-01.md"
SERP_OBSERVATION_REL_PATH = "docs/content/serp_observations/serp-observation-batch-01.md"
RESEARCH_ENRICHMENTS_DIR = ROOT / "docs/content/research_enrichments"
EXPECTED_RESEARCH_ENRICHMENTS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md": {
        "brief_id": "SHO-MVP-BRIEF-002",
        "research_input": "docs/content/research_inputs/betrugsnachrichten-auf-whatsapp-erkennen.research.md",
        "required_claims": ["SHO-CLAIM-004", "SHO-CLAIM-005", "SHO-CLAIM-006", "SHO-CLAIM-007"],
        "required_terms": ["excluded", "blocked"],
    },
    "smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md": {
        "brief_id": "SHO-MVP-BRIEF-003",
        "research_input": "docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md",
        "required_claims": ["SHO-CLAIM-008", "SHO-CLAIM-009", "SHO-CLAIM-010"],
        "required_terms": ["support_only"],
    },
}
WHATSAPP_MANUAL_REVIEW_SOURCE_IDS = {"SHO-SRC-001", "SHO-SRC-002", "SHO-SRC-003", "SHO-SRC-004"}
WHATSAPP_MANUAL_REVIEW_CLAIM_IDS = {"SHO-CLAIM-001", "SHO-CLAIM-002", "SHO-CLAIM-003", "SHO-CLAIM-007"}
ALLOWED_RESEARCH_STATUSES = {
    "not_researched",
    "source_candidates_added",
    "source_candidates_verified_partial",
}
ALLOWED_RESEARCH_SOURCE_STATUSES = {
    "missing",
    "candidate",
    "partial_verified",
    "verified_sources_available",
    "verified_sources_available_with_duplicate_rejected",
}
ALLOWED_SOURCE_PACK_STATUSES = {
    "source_pack_shell",
    "source_candidates_added",
    "source_candidates_verified_partial",
}
ALLOWED_SOURCE_ROW_STATUSES = {"candidate", "verified", "rejected"}
ALLOWED_VERIFICATION_STATUSES = {
    "needs_manual_review",
    "verified",
    "verified_limited",
    "duplicate_of",
}
ALLOWED_CLAIM_STATUSES = {
    "claim_slot_defined",
    "evidence_available",
    "evidence_limited",
    "needs_manual_review",
    "blocked_duplicate",
}
ALLOWED_CLAIM_USE = {
    "article_draft_candidate",
    "support_only",
    "needs_manual_review_before_draft",
    "not_allowed",
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
    "research_input_path",
    "research_status",
    "source_status",
    "serp_status",
    "content_status",
}

REQUIRED_RESEARCH_FIELDS = {
    "research_id",
    "linked_brief_id",
    "linked_brief_path",
    "slug",
    "research_status",
    "source_status",
    "serp_status",
    "serp_observation_path",
    "serp_observation_status",
    "serp_review_status",
    "source_pack_path",
    "source_pack_status",
    "claim_map_path",
    "claim_map_status",
    "operator_acceptance_status",
}

REQUIRED_SOURCE_PACK_FIELDS = {
    "source_pack_id",
    "batch_id",
    "linked_research_inputs",
    "source_pack_status",
    "created_by",
    "created_at",
    "operator_acceptance_status",
}

REQUIRED_CLAIM_MAP_FIELDS = {
    "claim_map_id",
    "batch_id",
    "linked_source_pack",
    "claim_map_status",
    "operator_acceptance_status",
}

PROTOCOL_REQUIRED_TERMS = {
    "docs/operations/CONTENT_RESEARCH_OPERATING_PROTOCOL.md": [
        "operator_defined_brief_scaffold",
        "research_input_shell",
        "source_pack_shell",
        "source_candidates_added",
        "source_candidates_verified_partial",
        "claim_slots_mapped",
        "operator_accepted",
    ],
    "docs/operations/CODEX_EXECUTOR_BOUNDARY.md": [
        "codex darf nicht",
        "operator acceptance",
        "keine quellen recherchieren",
        "keine claims formulieren",
    ],
    "docs/operations/RESEARCH_BATCH_STAGE_MODEL.md": [
        "verbotene spr",
        "review_required",
        "blocked",
    ],
    "docs/operations/STATUS_REGISTRY.yaml": [
        "forbidden_transitions",
        "forbidden_by_codex",
    ],
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


def validate_protocol_automation_files(failures: list[str]) -> None:
    for rel_path, required_terms in PROTOCOL_REQUIRED_TERMS.items():
        path = ROOT / rel_path
        if not path.exists():
            failures.append(f"Missing protocol automation file: {rel_path}")
            continue

        text = path.read_text(encoding="utf-8").lower()
        for term in required_terms:
            if term.lower() not in text:
                failures.append(f"{rel_path} must contain required marker: {term}")

    batch_manifest = ROOT / "docs/content/batches/MVP_BATCH_01.yaml"
    if batch_manifest.exists():
        text = batch_manifest.read_text(encoding="utf-8")
        required_fragments = [
            "batch_id: MVP_BATCH_01",
            "current_stage: claim_slots_mapped",
            "operator_acceptance_status: not_accepted",
            "claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md",
            f"- {SOURCE_REVIEW_REL_PATH}",
            f"- {EVIDENCE_CAPTURE_REL_PATH}",
            f"serp_observation: {SERP_OBSERVATION_REL_PATH}",
            "serp_status: observed",
            "serp_observation_status: operator_research_observed",
            "serp_review_status: needs_review",
            "current_stage: claim_slots_mapped",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Batch manifest must contain: {fragment}")
        forbidden_fragments = [
            "approved_for_publish",
            "operator_acceptance_status: accepted",
            "current_stage: research_enriched_brief_candidate",
            "publish_ready",
        ]
        for fragment in forbidden_fragments:
            if fragment in text:
                failures.append(f"Batch manifest must not contain: {fragment}")


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
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        missing = REQUIRED_BRIEF_FIELDS - set(fields)
        if missing:
            failures.append(
                f"Brief {file_name} is missing required fields: {', '.join(sorted(missing))}"
            )

        if "approved_for_publish" in text:
            failures.append(f"Brief {file_name} must not contain approved_for_publish")
        if normalized(fields.get("content_status")) != "scaffold_only":
            failures.append(f"Brief {file_name} must have content_status: scaffold_only")
        if normalized(fields.get("review_status")) == "approved_for_publish":
            failures.append(f"Brief {file_name} must not be approved_for_publish")
        if normalized(fields.get("operator_acceptance_status")) == "accepted":
            failures.append(f"Brief {file_name} must not have accepted operator status")
        if normalized(fields.get("research_status")) != "not_researched":
            failures.append(f"Brief {file_name} must have research_status: not_researched")
        if normalized(fields.get("source_status")) != "missing":
            failures.append(f"Brief {file_name} must have source_status: missing")
        if normalized(fields.get("serp_status")) != "not_researched":
            failures.append(f"Brief {file_name} must have serp_status: not_researched")

        expected_research_path = (
            f"docs/content/research_inputs/{fields.get('slug', '')}.research.md"
        )
        if fields.get("research_input_path") != expected_research_path:
            failures.append(
                f"Brief {file_name} must link to research_input_path: {expected_research_path}"
            )
        if has_security_context(fields) and is_true(fields.get("monetization_allowed_initially")):
            failures.append(
                f"Security/fraud brief must not allow initial monetization: {file_name}"
            )

    return len(found_files)


def validate_research_inputs(failures: list[str]) -> int:
    research_dir = ROOT / "docs/content/research_inputs"
    if not research_dir.exists():
        failures.append("Missing research input directory: docs/content/research_inputs")
        return 0

    readme_path = research_dir / "README.md"
    if not readme_path.exists():
        failures.append("Missing research input README: docs/content/research_inputs/README.md")

    found_files = {path.name for path in research_dir.glob("*.research.md")}
    expected_files = set(EXPECTED_RESEARCH_FILES)
    missing_files = expected_files - found_files
    extra_files = found_files - expected_files

    for file_name in sorted(missing_files):
        failures.append(f"Missing expected research input: docs/content/research_inputs/{file_name}")
    for file_name in sorted(extra_files):
        failures.append(f"Unexpected research input in Batch 01: docs/content/research_inputs/{file_name}")

    for file_name in sorted(expected_files & found_files):
        path = research_dir / file_name
        fields = parse_frontmatter_fields(path.read_text(encoding="utf-8"))
        expected = EXPECTED_RESEARCH_FILES[file_name]
        missing = REQUIRED_RESEARCH_FIELDS - set(fields)
        if missing:
            failures.append(
                f"Research input {file_name} is missing required fields: {', '.join(sorted(missing))}"
            )

        expected_brief_path = f"docs/content/briefs/{expected['brief_file']}"
        if fields.get("research_id") != expected["research_id"]:
            failures.append(f"Research input {file_name} has unexpected research_id")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Research input {file_name} has unexpected linked_brief_id")
        if fields.get("linked_brief_path") != expected_brief_path:
            failures.append(
                f"Research input {file_name} must link to brief path: {expected_brief_path}"
            )
        if fields.get("slug") != expected["slug"]:
            failures.append(f"Research input {file_name} has unexpected slug")
        if normalized(fields.get("research_status")) not in ALLOWED_RESEARCH_STATUSES:
            failures.append(
                f"Research input {file_name} has unsupported research_status: {fields.get('research_status')}"
            )
        if normalized(fields.get("source_status")) not in ALLOWED_RESEARCH_SOURCE_STATUSES:
            failures.append(
                f"Research input {file_name} has unsupported source_status: {fields.get('source_status')}"
            )
        if normalized(fields.get("serp_status")) != "observed":
            failures.append(f"Research input {file_name} must have serp_status: observed")
        if fields.get("serp_observation_path") != SERP_OBSERVATION_REL_PATH:
            failures.append(
                f"Research input {file_name} must link to serp_observation_path: {SERP_OBSERVATION_REL_PATH}"
            )
        if normalized(fields.get("serp_observation_status")) != "operator_research_observed":
            failures.append(
                f"Research input {file_name} must have serp_observation_status: operator_research_observed"
            )
        if normalized(fields.get("serp_review_status")) != "needs_review":
            failures.append(f"Research input {file_name} must have serp_review_status: needs_review")
        if fields.get("source_pack_path") != SOURCE_PACK_REL_PATH:
            failures.append(
                f"Research input {file_name} must link to source_pack_path: {SOURCE_PACK_REL_PATH}"
            )
        if normalized(fields.get("source_pack_status")) not in ALLOWED_SOURCE_PACK_STATUSES:
            failures.append(
                f"Research input {file_name} has unsupported source_pack_status: {fields.get('source_pack_status')}"
            )
        if fields.get("claim_map_path") != CLAIM_MAP_REL_PATH:
            failures.append(
                f"Research input {file_name} must link to claim_map_path: {CLAIM_MAP_REL_PATH}"
            )
        if normalized(fields.get("claim_map_status")) != "claim_slots_mapped":
            failures.append(f"Research input {file_name} must have claim_map_status: claim_slots_mapped")
        if file_name in {
            "whatsapp-fuer-senioren-sicher-einrichten.research.md",
            "betrugsnachrichten-auf-whatsapp-erkennen.research.md",
        } and fields.get("manual_source_review_path") != SOURCE_REVIEW_REL_PATH:
            failures.append(
                f"Research input {file_name} must link to manual_source_review_path: {SOURCE_REVIEW_REL_PATH}"
            )
        if file_name in {
            "whatsapp-fuer-senioren-sicher-einrichten.research.md",
            "betrugsnachrichten-auf-whatsapp-erkennen.research.md",
        }:
            if fields.get("evidence_capture_path") != EVIDENCE_CAPTURE_REL_PATH:
                failures.append(
                    f"Research input {file_name} must link to evidence_capture_path: {EVIDENCE_CAPTURE_REL_PATH}"
                )
            if normalized(fields.get("evidence_capture_status")) != "line_evidence_unavailable":
                failures.append(f"Research input {file_name} must have evidence_capture_status: line_evidence_unavailable")
        expected_enrichment_paths = {
            "betrugsnachrichten-auf-whatsapp-erkennen.research.md": (
                "docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md"
            ),
            "smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md": (
                "docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md"
            ),
        }
        if file_name in expected_enrichment_paths:
            if fields.get("research_enrichment_path") != expected_enrichment_paths[file_name]:
                failures.append(
                    f"Research input {file_name} must link to research_enrichment_path: {expected_enrichment_paths[file_name]}"
                )
            if normalized(fields.get("enrichment_status")) != "research_enriched_candidate":
                failures.append(f"Research input {file_name} must have enrichment_status: research_enriched_candidate")
        elif "research_enrichment_path" in fields or normalized(fields.get("enrichment_status")) == "research_enriched_candidate":
            failures.append(f"Research input {file_name} must not be marked as an enrichment candidate")
        if normalized(fields.get("operator_acceptance_status")) == "accepted":
            failures.append(f"Research input {file_name} must not have accepted operator status")
        research_text = path.read_text(encoding="utf-8")
        if "approved_for_publish" in research_text:
            failures.append(f"Research input {file_name} must not contain approved_for_publish")
        if "research_enriched" in research_text and file_name not in expected_enrichment_paths:
            failures.append(f"Research input {file_name} must not contain research_enriched")

    return len(found_files)


def source_pack_table_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_table = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("| source_id | linked_brief_id |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if set(line.replace("|", "").replace("-", "").replace(" ", "")) == set():
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 10:
            row = {
                "source_id": cells[0],
                "linked_brief_id": cells[1],
                "source_type": cells[2],
                "title_or_provider": cells[3],
                "url": cells[4],
                "retrieved_at": cells[5],
                "status": cells[6],
                "supports": cells[7],
                "risks": cells[8],
                "notes": cells[9],
            }
            if len(cells) >= 14:
                row.update(
                    {
                        "verification_status": cells[10],
                        "verification_note": cells[11],
                        "duplicate_of": cells[12],
                        "source_status_after": cells[13],
                    }
                )
            rows.append(row)
    return rows


def validate_source_pack_rows(rows: list[dict[str, str]], failures: list[str]) -> None:
    if len(rows) < 12:
        failures.append(f"Source pack must contain at least 12 source candidate rows; found {len(rows)}")

    seen_ids: set[str] = set()
    required_columns = {
        "source_id",
        "linked_brief_id",
        "source_type",
        "title_or_provider",
        "url",
        "retrieved_at",
        "status",
        "supports",
        "risks",
        "notes",
        "verification_status",
        "verification_note",
        "duplicate_of",
        "source_status_after",
    }
    for index, row in enumerate(rows, start=1):
        missing = [
            column
            for column in required_columns
            if not row.get(column) and column != "duplicate_of"
        ]
        if missing:
            failures.append(
                f"Source row {index} is missing required columns: {', '.join(sorted(missing))}"
            )

        source_id = row.get("source_id", "")
        if source_id in seen_ids:
            failures.append(f"Source row source_id must be unique: {source_id}")
        if source_id:
            seen_ids.add(source_id)

        status = normalized(row.get("status"))
        if status not in ALLOWED_SOURCE_ROW_STATUSES:
            failures.append(
                f"Source row {source_id or index} has unsupported status: {row.get('status')}"
            )
        if "TBD_BY_OPERATOR_OR_RESEARCH" in row.get("url", ""):
            failures.append(f"Source row URL must not be TBD after populate: {source_id}")

        verification_status = normalized(row.get("verification_status"))
        if verification_status not in ALLOWED_VERIFICATION_STATUSES:
            failures.append(
                f"Source row {source_id or index} has unsupported verification_status: {row.get('verification_status')}"
            )
        if verification_status in {"verified", "verified_limited", "needs_manual_review", "duplicate_of"} and not row.get(
            "verification_note"
        ):
            failures.append(f"Source row {source_id or index} must have verification_note")
        if verification_status == "duplicate_of":
            if not row.get("duplicate_of"):
                failures.append(f"Duplicate source row {source_id or index} must have duplicate_of")
            if status != "rejected":
                failures.append(f"Duplicate source row {source_id or index} must be rejected")
        if status == "rejected" and verification_status != "duplicate_of":
            failures.append(f"Rejected source row {source_id or index} must declare duplicate_of")
        if row.get("source_status_after") and normalized(row.get("source_status_after")) != status:
            failures.append(
                f"Source row {source_id or index} status must match source_status_after"
            )

        if source_id in WHATSAPP_MANUAL_REVIEW_SOURCE_IDS:
            if status != "candidate":
                failures.append(f"WhatsApp manual-review source {source_id} must remain candidate")
            if verification_status != "needs_manual_review":
                failures.append(
                    f"WhatsApp manual-review source {source_id} must remain needs_manual_review"
                )
            if normalized(row.get("source_status_after")) != "candidate":
                failures.append(f"WhatsApp manual-review source {source_id} must have source_status_after candidate")
            if "WHATSAPP_SOURCE_MANUAL_REVIEW_BATCH_01" not in row.get("verification_note", ""):
                failures.append(f"WhatsApp manual-review source {source_id} must reference manual review batch")
            if "line_evidence_unavailable" not in row.get("verification_note", ""):
                failures.append(f"WhatsApp manual-review source {source_id} must keep line evidence unavailable note")


def validate_source_pack(failures: list[str]) -> int:
    source_pack_dir = ROOT / "docs/content/source_packs"
    if not source_pack_dir.exists():
        failures.append("Missing source pack directory: docs/content/source_packs")
        return 0

    required_paths = [
        source_pack_dir / "README.md",
        source_pack_dir / "SOURCE_PACK_TEMPLATE.md",
        SOURCE_PACK_PATH,
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing source pack file: {path.relative_to(ROOT).as_posix()}")

    if not SOURCE_PACK_PATH.exists():
        return 0

    text = SOURCE_PACK_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)
    missing = REQUIRED_SOURCE_PACK_FIELDS - set(fields)
    if missing:
        failures.append(
            f"Source pack is missing required fields: {', '.join(sorted(missing))}"
        )

    if fields.get("source_pack_id") != "SHO-SOURCE-PACK-BATCH-01":
        failures.append("Source pack has unexpected source_pack_id")
    if fields.get("batch_id") != "MVP_BATCH_01":
        failures.append("Source pack has unexpected batch_id")
    if normalized(fields.get("source_pack_status")) not in ALLOWED_SOURCE_PACK_STATUSES:
        failures.append(f"Source pack has unsupported source_pack_status: {fields.get('source_pack_status')}")
    if normalized(fields.get("operator_acceptance_status")) == "accepted":
        failures.append("Source pack must not have accepted operator status")
    if "approved_for_publish" in text or "research_enriched" in text:
        failures.append("Source pack must not contain approved_for_publish or research_enriched")

    rows = source_pack_table_rows(text)
    validate_source_pack_rows(rows, failures)
    rejected_duplicates = [
        row
        for row in rows
        if row.get("source_id") == "SHO-SRC-013"
        and normalized(row.get("status")) == "rejected"
        and row.get("duplicate_of") == "SHO-SRC-012"
    ]
    if not rejected_duplicates:
        failures.append("Rejected duplicate source SHO-SRC-013 must remain present and point to SHO-SRC-012")

    return 1


def claim_map_table_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_table = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("| claim_id | linked_brief_id |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if set(line.replace("|", "").replace("-", "").replace(" ", "")) == set():
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 10:
            rows.append(
                {
                    "claim_id": cells[0],
                    "linked_brief_id": cells[1],
                    "linked_brief_slug": cells[2],
                    "claim_slot": cells[3],
                    "allowed_source_ids": cells[4],
                    "source_status_basis": cells[5],
                    "claim_status": cells[6],
                    "claim_use_allowed": cells[7],
                    "evidence_note": cells[8],
                    "limitations": cells[9],
                }
            )
    return rows


def validate_claim_map_rows(rows: list[dict[str, str]], failures: list[str]) -> None:
    if len(rows) != 14:
        failures.append(f"Claim map must contain exactly 14 SHO-CLAIM rows; found {len(rows)}")

    seen_ids: set[str] = set()
    for index, row in enumerate(rows, start=1):
        claim_id = row.get("claim_id", "")
        if claim_id in seen_ids:
            failures.append(f"Claim ID must be unique: {claim_id}")
        if claim_id:
            seen_ids.add(claim_id)

        claim_status = normalized(row.get("claim_status"))
        claim_use = normalized(row.get("claim_use_allowed"))
        if claim_status not in ALLOWED_CLAIM_STATUSES:
            failures.append(f"Claim {claim_id or index} has unsupported claim_status: {row.get('claim_status')}")
        if claim_use not in ALLOWED_CLAIM_USE:
            failures.append(
                f"Claim {claim_id or index} has unsupported claim_use_allowed: {row.get('claim_use_allowed')}"
            )
        if claim_status == "blocked_duplicate" and claim_use != "not_allowed":
            failures.append(f"Blocked duplicate claim {claim_id or index} must be not_allowed")
        if claim_status == "needs_manual_review" and claim_use != "needs_manual_review_before_draft":
            failures.append(
                f"Manual-review claim {claim_id or index} must be needs_manual_review_before_draft"
            )
        if "SHO-SRC-013" in row.get("allowed_source_ids", "") and claim_use == "article_draft_candidate":
            failures.append("Rejected duplicate source SHO-SRC-013 must not be article_draft_candidate evidence")
        if claim_id in WHATSAPP_MANUAL_REVIEW_CLAIM_IDS:
            if claim_status != "needs_manual_review":
                failures.append(f"WhatsApp manual-review claim {claim_id} must remain needs_manual_review")
            if claim_use != "needs_manual_review_before_draft":
                failures.append(
                    f"WhatsApp manual-review claim {claim_id} must remain needs_manual_review_before_draft"
                )
            if "WHATSAPP_SOURCE_MANUAL_REVIEW_BATCH_01" not in row.get("evidence_note", ""):
                failures.append(f"WhatsApp manual-review claim {claim_id} must reference manual review batch")
            if "line_evidence_unavailable" not in row.get("evidence_note", ""):
                failures.append(f"WhatsApp manual-review claim {claim_id} must reference unavailable evidence capture")


def validate_claim_map(failures: list[str]) -> int:
    claim_map_dir = ROOT / "docs/content/claim_maps"
    if not claim_map_dir.exists():
        failures.append("Missing claim map directory: docs/content/claim_maps")
        return 0

    required_paths = [
        claim_map_dir / "README.md",
        claim_map_dir / "CLAIM_MAP_TEMPLATE.md",
        CLAIM_MAP_PATH,
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing claim map file: {path.relative_to(ROOT).as_posix()}")

    if not CLAIM_MAP_PATH.exists():
        return 0

    text = CLAIM_MAP_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)
    missing = REQUIRED_CLAIM_MAP_FIELDS - set(fields)
    if missing:
        failures.append(f"Claim map is missing required fields: {', '.join(sorted(missing))}")
    if fields.get("claim_map_id") != "SHO-CLAIM-MAP-BATCH-01":
        failures.append("Claim map has unexpected claim_map_id")
    if fields.get("batch_id") != "MVP_BATCH_01":
        failures.append("Claim map has unexpected batch_id")
    if fields.get("linked_source_pack") != SOURCE_PACK_REL_PATH:
        failures.append(f"Claim map must link to source pack: {SOURCE_PACK_REL_PATH}")
    if normalized(fields.get("claim_map_status")) != "claim_slots_mapped":
        failures.append("Claim map must have claim_map_status: claim_slots_mapped")
    if normalized(fields.get("operator_acceptance_status")) == "accepted":
        failures.append("Claim map must not have accepted operator status")
    if "research_enriched" in text or "approved_for_publish" in text:
        failures.append("Claim map must not contain research_enriched or approved_for_publish")

    validate_claim_map_rows(claim_map_table_rows(text), failures)
    return 1


def validate_source_review(failures: list[str]) -> int:
    source_review_dir = ROOT / "docs/content/source_reviews"
    if not source_review_dir.exists():
        failures.append("Missing source review directory: docs/content/source_reviews")
        return 0

    required_paths = [
        source_review_dir / "README.md",
        SOURCE_REVIEW_PATH,
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing source review file: {path.relative_to(ROOT).as_posix()}")

    if not SOURCE_REVIEW_PATH.exists():
        return 0

    text = SOURCE_REVIEW_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)
    required_fragments = [
        "source_review_id: SHO-WA-MANUAL-REVIEW-BATCH-01",
        "review_status: manual_review_attempted_needs_line_evidence",
        "source_status_after_review: candidate",
        "operator_acceptance_status: not_accepted",
        "SHO-SRC-001",
        "SHO-SRC-002",
        "SHO-SRC-003",
        "SHO-SRC-004",
        "SHO-CLAIM-001",
        "SHO-CLAIM-002",
        "SHO-CLAIM-003",
        "SHO-CLAIM-007",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(f"Source review file must contain: {fragment}")

    if fields.get("source_review_id") != "SHO-WA-MANUAL-REVIEW-BATCH-01":
        failures.append("Source review has unexpected source_review_id")
    if fields.get("linked_source_pack") != SOURCE_PACK_REL_PATH:
        failures.append(f"Source review must link to source pack: {SOURCE_PACK_REL_PATH}")
    if fields.get("linked_claim_map") != CLAIM_MAP_REL_PATH:
        failures.append(f"Source review must link to claim map: {CLAIM_MAP_REL_PATH}")
    if fields.get("linked_evidence_capture") != EVIDENCE_CAPTURE_REL_PATH:
        failures.append(f"Source review must link to evidence capture: {EVIDENCE_CAPTURE_REL_PATH}")
    if normalized(fields.get("review_status")) != "manual_review_attempted_needs_line_evidence":
        failures.append("Source review must have review_status: manual_review_attempted_needs_line_evidence")
    if normalized(fields.get("source_status_after_review")) != "candidate":
        failures.append("Source review must have source_status_after_review: candidate")
    if normalized(fields.get("operator_acceptance_status")) == "accepted":
        failures.append("Source review must not have accepted operator status")

    forbidden_fragments = [
        "source_status_after_review: verified",
        "operator_acceptance_status: accepted",
        "approved_for_publish",
        "research_enriched",
    ]
    for fragment in forbidden_fragments:
        if fragment in text:
            failures.append(f"Source review file must not contain: {fragment}")

    return 1


def validate_evidence_capture(failures: list[str]) -> int:
    evidence_capture_dir = ROOT / "docs/content/evidence_captures"
    if not evidence_capture_dir.exists():
        failures.append("Missing evidence capture directory: docs/content/evidence_captures")
        return 0

    required_paths = [
        evidence_capture_dir / "README.md",
        evidence_capture_dir / "EVIDENCE_CAPTURE_TEMPLATE.md",
        EVIDENCE_CAPTURE_PATH,
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing evidence capture file: {path.relative_to(ROOT).as_posix()}")

    if not EVIDENCE_CAPTURE_PATH.exists():
        return 0

    text = EVIDENCE_CAPTURE_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)
    required_fragments = [
        "evidence_capture_id: SHO-WA-LINE-EVIDENCE-BATCH-01",
        "evidence_capture_status: line_evidence_unavailable",
        "operator_acceptance_status: not_accepted",
        "SHO-EVID-WA-001",
        "SHO-EVID-WA-002",
        "SHO-EVID-WA-003",
        "SHO-EVID-WA-004",
        "SHO-SRC-001",
        "SHO-SRC-002",
        "SHO-SRC-003",
        "SHO-SRC-004",
        "SHO-CLAIM-001",
        "SHO-CLAIM-002",
        "SHO-CLAIM-003",
        "SHO-CLAIM-007",
        "not_allowed",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(f"Evidence capture file must contain: {fragment}")

    if fields.get("evidence_capture_id") != "SHO-WA-LINE-EVIDENCE-BATCH-01":
        failures.append("Evidence capture has unexpected evidence_capture_id")
    if fields.get("linked_source_review") != SOURCE_REVIEW_REL_PATH:
        failures.append(f"Evidence capture must link to source review: {SOURCE_REVIEW_REL_PATH}")
    if fields.get("linked_source_pack") != SOURCE_PACK_REL_PATH:
        failures.append(f"Evidence capture must link to source pack: {SOURCE_PACK_REL_PATH}")
    if fields.get("linked_claim_map") != CLAIM_MAP_REL_PATH:
        failures.append(f"Evidence capture must link to claim map: {CLAIM_MAP_REL_PATH}")
    if normalized(fields.get("evidence_capture_status")) != "line_evidence_unavailable":
        failures.append("Evidence capture must have evidence_capture_status: line_evidence_unavailable")
    if normalized(fields.get("operator_acceptance_status")) == "accepted":
        failures.append("Evidence capture must not have accepted operator status")

    forbidden_fragments = [
        "claim_support_allowed",
        "operator_acceptance_status: accepted",
        "approved_for_publish",
        "research_enriched",
    ]
    for fragment in forbidden_fragments:
        if fragment in text:
            failures.append(f"Evidence capture file must not contain: {fragment}")

    return 1


def validate_serp_observation(failures: list[str]) -> int:
    serp_dir = ROOT / "docs/content/serp_observations"
    if not serp_dir.exists():
        failures.append("Missing SERP observation directory: docs/content/serp_observations")
        return 0

    required_paths = [
        serp_dir / "README.md",
        serp_dir / "SERP_OBSERVATION_TEMPLATE.md",
        SERP_OBSERVATION_PATH,
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing SERP observation file: {path.relative_to(ROOT).as_posix()}")

    if not SERP_OBSERVATION_PATH.exists():
        return 0

    text = SERP_OBSERVATION_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    fields = parse_frontmatter_fields(text)
    required_fragments = [
        "serp_observation_id: SHO-SERP-OBS-BATCH-01",
        "batch_id: MVP_BATCH_01",
        'searched_at: "2026-06-01"',
        "serp_observation_status: operator_research_observed",
        "serp_review_status: needs_review",
        "operator_acceptance_status: not_accepted",
        "No search volume",
        "No keyword difficulty",
        "No ranking guarantee",
        "SHO-MVP-BRIEF-001",
        "SHO-MVP-BRIEF-002",
        "SHO-MVP-BRIEF-003",
        "SHO-MVP-BRIEF-004",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(f"SERP observation file must contain: {fragment}")

    if fields.get("serp_observation_id") != "SHO-SERP-OBS-BATCH-01":
        failures.append("SERP observation has unexpected serp_observation_id")
    if fields.get("batch_id") != "MVP_BATCH_01":
        failures.append("SERP observation has unexpected batch_id")
    if normalized(fields.get("serp_observation_status")) != "operator_research_observed":
        failures.append("SERP observation must have serp_observation_status: operator_research_observed")
    if normalized(fields.get("serp_review_status")) != "needs_review":
        failures.append("SERP observation must have serp_review_status: needs_review")
    if normalized(fields.get("operator_acceptance_status")) == "accepted":
        failures.append("SERP observation must not have accepted operator status")

    forbidden_fragments = [
        "operator_acceptance_status: accepted",
        "approved_for_publish",
        "research_enriched",
        "traffic forecast:",
        "ranking guarantee:",
    ]
    for fragment in forbidden_fragments:
        if fragment in text_lower:
            failures.append(f"SERP observation file must not contain: {fragment}")

    query_rows = [
        line
        for line in text.splitlines()
        if line.startswith("| SHO-MVP-BRIEF-") and "qualitative observation only" in line
    ]
    if len(query_rows) != 12:
        failures.append(
            f"SERP observation must contain exactly 12 qualitative query rows; found {len(query_rows)}"
        )

    return 1


def validate_research_enrichments(failures: list[str]) -> int:
    if not RESEARCH_ENRICHMENTS_DIR.exists():
        failures.append("Missing research enrichment directory: docs/content/research_enrichments")
        return 0

    required_paths = [
        RESEARCH_ENRICHMENTS_DIR / "README.md",
        RESEARCH_ENRICHMENTS_DIR / "RESEARCH_ENRICHMENT_TEMPLATE.md",
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing research enrichment file: {path.relative_to(ROOT).as_posix()}")

    found_files = {path.name for path in RESEARCH_ENRICHMENTS_DIR.glob("*.enrichment.md")}
    expected_files = set(EXPECTED_RESEARCH_ENRICHMENTS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these enrichment files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = RESEARCH_ENRICHMENTS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        text_lower = text.lower()
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_RESEARCH_ENRICHMENTS[file_name]

        required_fragments = [
            "enrichment_status: research_enriched_candidate",
            "operator_acceptance_status: not_accepted",
            "linked_source_pack:",
            "linked_claim_map:",
            "linked_serp_observation:",
            "Explicit Non-Acceptance",
            expected["brief_id"],
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Research enrichment {file_name} must contain: {fragment}")
        for claim_id in expected["required_claims"]:
            if claim_id not in text:
                failures.append(f"Research enrichment {file_name} must contain claim: {claim_id}")
        for term in expected["required_terms"]:
            if term.lower() not in text_lower:
                failures.append(f"Research enrichment {file_name} must contain marker: {term}")

        if normalized(fields.get("enrichment_status")) != "research_enriched_candidate":
            failures.append(f"Research enrichment {file_name} must have enrichment_status: research_enriched_candidate")
        if normalized(fields.get("operator_acceptance_status")) == "accepted":
            failures.append(f"Research enrichment {file_name} must not have accepted operator status")
        if fields.get("linked_source_pack") != SOURCE_PACK_REL_PATH:
            failures.append(f"Research enrichment {file_name} must link to source pack")
        if fields.get("linked_claim_map") != CLAIM_MAP_REL_PATH:
            failures.append(f"Research enrichment {file_name} must link to claim map")
        if fields.get("linked_serp_observation") != SERP_OBSERVATION_REL_PATH:
            failures.append(f"Research enrichment {file_name} must link to SERP observation")
        if fields.get("linked_research_input") != expected["research_input"]:
            failures.append(f"Research enrichment {file_name} must link to expected research input")

        forbidden_fragments = [
            "approved_for_publish",
            "operator_acceptance_status: accepted",
            "publish_ready",
            "ranking guarantee:",
            "search volume:",
            "keyword difficulty:",
        ]
        for fragment in forbidden_fragments:
            if fragment in text_lower:
                failures.append(f"Research enrichment {file_name} must not contain: {fragment}")
        if "SHO-MVP-BRIEF-001" in text or "SHO-MVP-BRIEF-004" in text:
            failures.append(f"Research enrichment {file_name} must not enrich Brief 001 or Brief 004")

    return len(found_files)


def main() -> int:
    failures: list[str] = []

    validate_required_docs(failures)
    validate_protocol_automation_files(failures)
    backlog_count = validate_backlog(failures)
    brief_count = validate_brief_scaffolds(failures)
    research_count = validate_research_inputs(failures)
    source_pack_count = validate_source_pack(failures)
    claim_map_count = validate_claim_map(failures)
    source_review_count = validate_source_review(failures)
    evidence_capture_count = validate_evidence_capture(failures)
    serp_observation_count = validate_serp_observation(failures)
    research_enrichment_count = validate_research_enrichments(failures)

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
    print(f"- Batch 01 research input files: {research_count}")
    print(f"- Batch 01 source pack files: {source_pack_count}")
    print(f"- Batch 01 claim map files: {claim_map_count}")
    print(f"- Batch 01 source review files: {source_review_count}")
    print(f"- Batch 01 evidence capture files: {evidence_capture_count}")
    print(f"- Batch 01 SERP observation files: {serp_observation_count}")
    print(f"- Batch 01 research enrichment files: {research_enrichment_count}")
    print("- YAML/frontmatter parsing: dependency-free and text-based")
    return 0


if __name__ == "__main__":
    sys.exit(main())
