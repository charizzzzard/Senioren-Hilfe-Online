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
ARTICLE_DRAFT_CANDIDATE = (
    ROOT
    / "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md"
)
ARTICLE_REVIEW = ROOT / "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.review.md"
REVIEW_FINDINGS_REGISTER = ROOT / "docs/operations/REVIEW_FINDINGS_REGISTER.md"


def fail_if_missing(path: Path, failures: list[str]) -> str:
    if not path.exists():
        failures.append(f"Missing required file: {path.relative_to(ROOT).as_posix()}")
        return ""
    return path.read_text(encoding="utf-8")


def has_forbidden_assignment(text: str) -> bool:
    forbidden_patterns = [
        "operator_acceptance_status: accepted",
        "approved_for_publish: true",
        "review_status: approved_for_publish",
        "publish_ready: true",
        "article_status: publish_candidate",
        "article_status: review_ready",
    ]
    lower_text = text.lower()
    return any(pattern in lower_text for pattern in forbidden_patterns)


def main() -> int:
    failures: list[str] = []

    registry_text = fail_if_missing(STATUS_REGISTRY, failures)
    batch_text = fail_if_missing(BATCH_MANIFEST, failures)
    source_pack_text = fail_if_missing(SOURCE_PACK, failures)
    evidence_text = EVIDENCE_CAPTURE.read_text(encoding="utf-8") if EVIDENCE_CAPTURE.exists() else ""
    article_candidate_text = fail_if_missing(ARTICLE_DRAFT_CANDIDATE, failures)
    article_review_text = fail_if_missing(ARTICLE_REVIEW, failures)
    findings_register_text = fail_if_missing(REVIEW_FINDINGS_REGISTER, failures)

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
            if "review_status: re_review_passed_not_publish_ready" not in article_candidate_text:
                failures.append(
                    "Brief 002 article draft candidate must stay at review_status: re_review_passed_not_publish_ready"
                )

        if "article_reviews:" in batch_text:
            if "current_stage: claim_slots_mapped" not in batch_text:
                failures.append("Article reviews require MVP_BATCH_01 to remain at claim_slots_mapped")
            if "operator_acceptance_status: not_accepted" not in batch_text:
                failures.append("Article reviews require operator_acceptance_status: not_accepted")
            if "review_status: review_completed_with_findings" not in article_review_text:
                failures.append("Article review must retain original review_status: review_completed_with_findings")
            if "re_review_status: re_review_passed_not_publish_ready" not in article_review_text:
                failures.append("Article review must contain separate re_review_status: re_review_passed_not_publish_ready")

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

    if article_candidate_text:
        required_candidate_fragments = [
            "article_status: article_draft_candidate",
            "review_status: re_review_passed_not_publish_ready",
            "operator_acceptance_status: not_accepted",
            "SHO-CLAIM-007 remains blocked",
            "Explicit Non-Acceptance",
        ]
        for fragment in required_candidate_fragments:
            if fragment not in article_candidate_text:
                failures.append(f"Article draft candidate must contain: {fragment}")
        if "[claim: SHO-CLAIM-007" in article_candidate_text:
            failures.append("SHO-CLAIM-007 must not be used as a draft candidate evidence marker")
        if has_forbidden_assignment(article_candidate_text):
            failures.append("Article draft candidate contains a forbidden publish/review assignment")
        lower_candidate = article_candidate_text.lower()
        forbidden_candidate_fragments = [
            "affiliate-link",
            "affiliate link",
            "product recommendation",
            "produktempfehlung:",
            "empfohlenes produkt",
            "jetzt kaufen",
            "tippen sie auf blockieren",
            "tippen sie auf melden",
            "kontakt blockieren",
            "chat melden",
        ]
        for fragment in forbidden_candidate_fragments:
            if fragment in lower_candidate:
                failures.append(f"Article draft candidate must not contain forbidden fragment: {fragment}")

    if article_review_text:
        required_review_fragments = [
            "review_status: review_completed_with_findings",
            "operator_acceptance_status: not_accepted",
            "Fix Patch Link",
            "Re-Review Result",
            "re_review_status: re_review_passed_not_publish_ready",
            "SHO-ARTICLE-002-UX-001 | fixed_pending_re_review | re_review_passed",
            "SHO-ARTICLE-002-UX-002 | fixed_pending_re_review | re_review_passed",
            "SHO-ARTICLE-002-SAFE-001 | fixed_pending_re_review | re_review_passed",
            "SHO-ARTICLE-002-SRC-001 | fixed_pending_re_review | re_review_passed",
            "Explicit Non-Acceptance",
        ]
        for fragment in required_review_fragments:
            if fragment not in article_review_text:
                failures.append(f"Article review must contain: {fragment}")
        if has_forbidden_assignment(article_review_text):
            failures.append("Article review contains a forbidden publish/review assignment")

    if findings_register_text:
        required_register_fragments = [
            "SHO-ARTICLE-002-UX-001 | article_draft_candidate_review | P2 | re_review_passed",
            "SHO-ARTICLE-002-UX-002 | article_draft_candidate_review | P2 | re_review_passed",
            "SHO-ARTICLE-002-SAFE-001 | article_draft_candidate_review | P2 | re_review_passed",
            "SHO-ARTICLE-002-SRC-001 | article_draft_candidate_review | P2 | re_review_passed",
            "SHO-ARTICLE-002-GATE-001 | article_draft_candidate_review | P1 | pass_carried_forward",
            "SHO-ARTICLE-002-MON-001 | article_draft_candidate_review | P1 | pass_carried_forward",
            "SHO-ARTICLE-002-PUB-001 | article_draft_candidate_review | P1 | pass_carried_forward",
        ]
        for fragment in required_register_fragments:
            if fragment not in findings_register_text:
                failures.append(f"Review findings register must contain hardened status row: {fragment}")

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
