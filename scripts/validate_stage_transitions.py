#!/usr/bin/env python3
"""Skeleton stage-transition validator for SHO-OS.

This script is intentionally dependency-free and text-based. It checks only the
current MVP_BATCH_01 manifest and STATUS_REGISTRY baseline. It should later be
replaced or backed by a real YAML parser and full transition engine.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS_REGISTRY = ROOT / "docs/operations/STATUS_REGISTRY.yaml"
BATCH_MANIFEST = ROOT / "docs/content/batches/MVP_BATCH_01.yaml"
SOURCE_PACK = ROOT / "docs/content/source_packs/operator-research-source-pack-batch-01.md"
EVIDENCE_CAPTURE = ROOT / "docs/content/evidence_captures/whatsapp-line-evidence-capture-batch-01.md"


def fail_if_missing(path: Path, failures: list[str]) -> str:
    if not path.exists():
        failures.append(f"Missing required file: {path.relative_to(ROOT).as_posix()}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    failures: list[str] = []

    registry_text = fail_if_missing(STATUS_REGISTRY, failures)
    batch_text = fail_if_missing(BATCH_MANIFEST, failures)
    source_pack_text = fail_if_missing(SOURCE_PACK, failures)
    evidence_text = EVIDENCE_CAPTURE.read_text(encoding="utf-8") if EVIDENCE_CAPTURE.exists() else ""

    if registry_text:
        if "forbidden_transitions" not in registry_text:
            failures.append("STATUS_REGISTRY.yaml must contain forbidden_transitions")
        if "forbidden_by_codex" not in registry_text:
            failures.append("STATUS_REGISTRY.yaml must contain forbidden_by_codex")

    if batch_text:
        required_fragments = [
            "batch_id: MVP_BATCH_01",
            "current_stage: claim_slots_mapped",
            "claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md",
            "operator_acceptance_status: not_accepted",
        ]
        for fragment in required_fragments:
            if fragment not in batch_text:
                failures.append(f"MVP_BATCH_01.yaml must contain: {fragment}")

        forbidden_fragments = [
            "operator_acceptance_status: accepted",
            "current_stage: operator_accepted",
            "operator_accepted",
            "approved_for_publish: true",
            "review_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: article_draft_candidate",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
        ]
        for fragment in forbidden_fragments:
            if fragment in batch_text:
                failures.append(f"MVP_BATCH_01.yaml must not contain: {fragment}")

        if "manual_source_reviews:" in batch_text and "current_stage: claim_slots_mapped" not in batch_text:
            failures.append("Manual source review presence must keep MVP_BATCH_01 at claim_slots_mapped")

        if "evidence_captures:" in batch_text and "current_stage: claim_slots_mapped" not in batch_text:
            failures.append("Evidence capture presence must keep MVP_BATCH_01 at claim_slots_mapped")

        if "serp_observation:" in batch_text and "current_stage: research_enriched_brief_candidate" in batch_text:
            failures.append(
                "SERP observation must not move MVP_BATCH_01 to research_enriched_brief_candidate without an explicit transition patch"
            )
        if "serp_observation:" in batch_text and "current_stage: claim_slots_mapped" not in batch_text:
            failures.append("SERP observation presence must keep MVP_BATCH_01 at claim_slots_mapped")
        if "research_enrichment_candidates:" in batch_text:
            if "current_stage: claim_slots_mapped" not in batch_text:
                failures.append("Research enrichment candidates require MVP_BATCH_01 to remain at claim_slots_mapped")
            if "operator_acceptance_status: not_accepted" not in batch_text:
                failures.append("Research enrichment candidates require operator_acceptance_status: not_accepted")
            if "current_stage: research_enriched_brief_candidate" in batch_text:
                failures.append("Limited enrichment candidates must not move the full batch stage")

        if "article_draft_scaffolds:" in batch_text:
            if "current_stage: claim_slots_mapped" not in batch_text:
                failures.append("Article draft scaffolds require MVP_BATCH_01 to remain at claim_slots_mapped")
            if "operator_acceptance_status: not_accepted" not in batch_text:
                failures.append("Article draft scaffolds require operator_acceptance_status: not_accepted")

        if "article_draft_candidates:" in batch_text:
            if "current_stage: claim_slots_mapped" not in batch_text:
                failures.append("Article draft candidates require MVP_BATCH_01 to remain at claim_slots_mapped")
            if "operator_acceptance_status: not_accepted" not in batch_text:
                failures.append("Article draft candidates require operator_acceptance_status: not_accepted")

        if "article_reviews:" in batch_text:
            if "current_stage: claim_slots_mapped" not in batch_text:
                failures.append("Article reviews require MVP_BATCH_01 to remain at claim_slots_mapped")
            if "operator_acceptance_status: not_accepted" not in batch_text:
                failures.append("Article reviews require operator_acceptance_status: not_accepted")

        if "article_draft_candidate_fixes:" in batch_text:
            if "current_stage: claim_slots_mapped" not in batch_text:
                failures.append("Article draft candidate fixes require MVP_BATCH_01 to remain at claim_slots_mapped")
            if "operator_acceptance_status: not_accepted" not in batch_text:
                failures.append("Article draft candidate fixes require operator_acceptance_status: not_accepted")

        if "manual_review_verified" in batch_text and "needs_manual_review" in source_pack_text:
            failures.append(
                "MVP_BATCH_01.yaml must not contain manual_review_verified while source pack still has needs_manual_review"
            )

        if "evidence_capture_status: line_evidence_available" in evidence_text and "needs_manual_review" in source_pack_text:
            failures.append(
                "Line evidence must not be available while WhatsApp source pack rows still show needs_manual_review without a verification patch"
            )

    if failures:
        print("FAIL: SHO-OS stage transition skeleton validation failed")
        for failure in failures:
            print(f"- {failure}")
        print("- YAML parsing: dependency-free and text-based skeleton")
        return 1

    print("PASS: SHO-OS stage transition skeleton validation passed")
    print("- STATUS_REGISTRY.yaml present with forbidden transition markers")
    print("- MVP_BATCH_01.yaml present at current_stage: claim_slots_mapped")
    print("- Operator Acceptance is not set")
    print("- No approved_for_publish, publish_ready or full-batch article transition detected")
    print("- YAML parsing: dependency-free and text-based skeleton")
    return 0


if __name__ == "__main__":
    sys.exit(main())
