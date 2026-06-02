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
    "docs/content/article_draft_scaffolds/README.md",
    "docs/content/article_draft_scaffolds/ARTICLE_DRAFT_SCAFFOLD_TEMPLATE.md",
    "docs/content/article_draft_scaffolds/betrugsnachrichten-auf-whatsapp-erkennen.draft-scaffold.md",
    "docs/content/article_draft_scaffolds/smartphone-schriftgroesse-und-bedienhilfen-einstellen.draft-scaffold.md",
    "docs/content/article_draft_candidates/README.md",
    "docs/content/article_draft_candidates/ARTICLE_DRAFT_CANDIDATE_TEMPLATE.md",
    "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
    "docs/content/article_reviews/README.md",
    "docs/content/article_reviews/ARTICLE_REVIEW_TEMPLATE.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.review.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.operator-review-packet.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.legal-source-citation-review.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.source-citation-formatting-prep.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.legal-wording-review-prep.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-article-prep-gate-review.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.citation-display-label-review.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.citation-text-prep.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-legal-wording-review.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-list-review.md",
    "docs/operations/CONTENT_RESEARCH_OPERATING_PROTOCOL.md",
    "docs/operations/RESEARCH_BATCH_STAGE_MODEL.md",
    "docs/operations/CODEX_EXECUTOR_BOUNDARY.md",
    "docs/operations/operator_decisions/README.md",
    "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001.md",
    "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_002.md",
    "docs/operations/MVP_OPERATIONAL_START_PLAN_BATCH_01.md",
    "docs/operations/ROADMAP_AND_MILESTONES_MVP_2026.md",
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
BATCH_MANIFEST_PATH = ROOT / "docs/content/batches/MVP_BATCH_01.yaml"
STATUS_REGISTRY_PATH = ROOT / "docs/operations/STATUS_REGISTRY.yaml"
REVIEW_FINDINGS_REGISTER_PATH = ROOT / "docs/operations/REVIEW_FINDINGS_REGISTER.md"
MVP_OPERATIONAL_START_PLAN_PATH = ROOT / "docs/operations/MVP_OPERATIONAL_START_PLAN_BATCH_01.md"
ROADMAP_MVP_2026_PATH = ROOT / "docs/operations/ROADMAP_AND_MILESTONES_MVP_2026.md"
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
        "draft_scaffold": "docs/content/article_draft_scaffolds/betrugsnachrichten-auf-whatsapp-erkennen.draft-scaffold.md",
        "required_claims": ["SHO-CLAIM-004", "SHO-CLAIM-005", "SHO-CLAIM-006", "SHO-CLAIM-007"],
        "required_terms": ["excluded", "blocked"],
    },
    "smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md": {
        "brief_id": "SHO-MVP-BRIEF-003",
        "research_input": "docs/content/research_inputs/smartphone-schriftgroesse-und-bedienhilfen-einstellen.research.md",
        "draft_scaffold": "docs/content/article_draft_scaffolds/smartphone-schriftgroesse-und-bedienhilfen-einstellen.draft-scaffold.md",
        "required_claims": ["SHO-CLAIM-008", "SHO-CLAIM-009", "SHO-CLAIM-010"],
        "required_terms": ["support_only"],
    },
}
ARTICLE_DRAFT_SCAFFOLDS_DIR = ROOT / "docs/content/article_draft_scaffolds"
EXPECTED_ARTICLE_DRAFT_SCAFFOLDS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.draft-scaffold.md": {
        "brief_id": "SHO-MVP-BRIEF-002",
        "enrichment": "docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md",
        "article_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "required_claims": ["SHO-CLAIM-004", "SHO-CLAIM-005", "SHO-CLAIM-006", "SHO-CLAIM-007"],
        "required_terms": ["excluded", "not allowed"],
    },
    "smartphone-schriftgroesse-und-bedienhilfen-einstellen.draft-scaffold.md": {
        "brief_id": "SHO-MVP-BRIEF-003",
        "enrichment": "docs/content/research_enrichments/smartphone-schriftgroesse-und-bedienhilfen-einstellen.enrichment.md",
        "article_candidate": "",
        "required_claims": ["SHO-CLAIM-008", "SHO-CLAIM-009", "SHO-CLAIM-010"],
        "required_terms": ["support_only"],
    },
}
ARTICLE_DRAFT_CANDIDATES_DIR = ROOT / "docs/content/article_draft_candidates"
ARTICLE_REVIEWS_DIR = ROOT / "docs/content/article_reviews"
ARTICLE_REVIEW_REL_PATH = "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.review.md"
OPERATOR_REVIEW_PACKET_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.operator-review-packet.md"
)
LEGAL_SOURCE_CITATION_REVIEW_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.legal-source-citation-review.md"
)
SOURCE_CITATION_FORMATTING_PREP_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.source-citation-formatting-prep.md"
)
LEGAL_WORDING_REVIEW_PREP_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.legal-wording-review-prep.md"
)
FINAL_ARTICLE_PREP_GATE_REVIEW_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-article-prep-gate-review.md"
)
CITATION_DISPLAY_LABEL_REVIEW_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.citation-display-label-review.md"
)
CITATION_TEXT_PREP_REL_PATH = "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.citation-text-prep.md"
FINAL_LEGAL_WORDING_REVIEW_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-legal-wording-review.md"
)
FINAL_SOURCE_LIST_REVIEW_REL_PATH = (
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-list-review.md"
)
OPERATOR_DECISIONS_DIR = ROOT / "docs/operations/operator_decisions"
OPERATOR_DECISION_REL_PATH = "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001.md"
EXPECTED_ARTICLE_DRAFT_CANDIDATES = {
    "betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md": {
        "article_draft_candidate_id": "SHO-ARTICLE-DRAFT-CANDIDATE-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "draft_scaffold": "docs/content/article_draft_scaffolds/betrugsnachrichten-auf-whatsapp-erkennen.draft-scaffold.md",
        "research_enrichment": "docs/content/research_enrichments/betrugsnachrichten-auf-whatsapp-erkennen.enrichment.md",
        "article_review": ARTICLE_REVIEW_REL_PATH,
        "required_claims": ["SHO-CLAIM-004", "SHO-CLAIM-005", "SHO-CLAIM-006", "SHO-CLAIM-007"],
        "required_sources": ["SHO-SRC-005", "SHO-SRC-006", "SHO-SRC-007"],
    },
}
EXPECTED_ARTICLE_REVIEWS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.review.md": {
        "article_review_id": "SHO-ARTICLE-REVIEW-BATCH01-BRIEF002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "finding_ids": [
            "SHO-ARTICLE-002-UX-001",
            "SHO-ARTICLE-002-UX-002",
            "SHO-ARTICLE-002-SAFE-001",
            "SHO-ARTICLE-002-SRC-001",
            "SHO-ARTICLE-002-GATE-001",
            "SHO-ARTICLE-002-MON-001",
            "SHO-ARTICLE-002-PUB-001",
        ],
    },
}
EXPECTED_OPERATOR_REVIEW_PACKETS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.operator-review-packet.md": {
        "operator_review_packet_id": "SHO-OPERATOR-REVIEW-PACKET-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_article_review": ARTICLE_REVIEW_REL_PATH,
        "linked_findings_register": "docs/operations/REVIEW_FINDINGS_REGISTER.md",
    },
}
EXPECTED_LEGAL_SOURCE_CITATION_REVIEWS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.legal-source-citation-review.md": {
        "legal_source_citation_review_id": "SHO-LEGAL-SOURCE-CITATION-REVIEW-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_article_review": ARTICLE_REVIEW_REL_PATH,
        "linked_operator_review_packet": OPERATOR_REVIEW_PACKET_REL_PATH,
    },
}
EXPECTED_OPERATOR_DECISIONS = {
    "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001.md": {
        "operator_decision_id": "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_operator_review_packet": OPERATOR_REVIEW_PACKET_REL_PATH,
        "linked_legal_source_citation_review": LEGAL_SOURCE_CITATION_REVIEW_REL_PATH,
        "decision_status": "proceed_to_source_citation_and_legal_wording_preparation",
    },
    "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_002.md": {
        "operator_decision_id": "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_final_source_list_review": FINAL_SOURCE_LIST_REVIEW_REL_PATH,
        "linked_final_legal_wording_review": FINAL_LEGAL_WORDING_REVIEW_REL_PATH,
        "linked_final_article_prep_gate_review": FINAL_ARTICLE_PREP_GATE_REVIEW_REL_PATH,
        "decision_status": "proceed_to_final_article_preparation_not_publish_ready",
    },
}
EXPECTED_SOURCE_CITATION_FORMATTING_PREPS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.source-citation-formatting-prep.md": {
        "source_citation_formatting_prep_id": "SHO-SOURCE-CITATION-FORMATTING-PREP-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_article_review": ARTICLE_REVIEW_REL_PATH,
        "linked_operator_decision": OPERATOR_DECISION_REL_PATH,
    },
}
EXPECTED_LEGAL_WORDING_REVIEW_PREPS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.legal-wording-review-prep.md": {
        "legal_wording_review_prep_id": "SHO-LEGAL-WORDING-REVIEW-PREP-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_operator_decision": OPERATOR_DECISION_REL_PATH,
        "linked_source_citation_formatting_prep": SOURCE_CITATION_FORMATTING_PREP_REL_PATH,
    },
}
EXPECTED_FINAL_ARTICLE_PREP_GATE_REVIEWS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.final-article-prep-gate-review.md": {
        "final_article_prep_gate_review_id": "SHO-FINAL-ARTICLE-PREP-GATE-REVIEW-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_article_review": ARTICLE_REVIEW_REL_PATH,
        "linked_operator_review_packet": OPERATOR_REVIEW_PACKET_REL_PATH,
        "linked_operator_decision": OPERATOR_DECISION_REL_PATH,
        "linked_source_citation_formatting_prep": SOURCE_CITATION_FORMATTING_PREP_REL_PATH,
        "linked_legal_wording_review_prep": LEGAL_WORDING_REVIEW_PREP_REL_PATH,
    },
}
EXPECTED_CITATION_DISPLAY_LABEL_REVIEWS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.citation-display-label-review.md": {
        "citation_display_label_review_id": "SHO-CITATION-DISPLAY-LABEL-REVIEW-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_source_citation_formatting_prep": SOURCE_CITATION_FORMATTING_PREP_REL_PATH,
        "linked_final_article_prep_gate_review": FINAL_ARTICLE_PREP_GATE_REVIEW_REL_PATH,
    },
}
EXPECTED_CITATION_TEXT_PREPS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.citation-text-prep.md": {
        "citation_text_prep_id": "SHO-CITATION-TEXT-PREP-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_citation_display_label_review": CITATION_DISPLAY_LABEL_REVIEW_REL_PATH,
        "linked_source_citation_formatting_prep": SOURCE_CITATION_FORMATTING_PREP_REL_PATH,
        "linked_final_article_prep_gate_review": FINAL_ARTICLE_PREP_GATE_REVIEW_REL_PATH,
    },
}
EXPECTED_FINAL_LEGAL_WORDING_REVIEWS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.final-legal-wording-review.md": {
        "final_legal_wording_review_id": "SHO-FINAL-LEGAL-WORDING-REVIEW-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_article_draft_candidate": "docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_legal_wording_review_prep": LEGAL_WORDING_REVIEW_PREP_REL_PATH,
        "linked_citation_text_prep": CITATION_TEXT_PREP_REL_PATH,
    },
}
EXPECTED_FINAL_SOURCE_LIST_REVIEWS = {
    "betrugsnachrichten-auf-whatsapp-erkennen.final-source-list-review.md": {
        "final_source_list_review_id": "SHO-FINAL-SOURCE-LIST-REVIEW-BATCH01-BRIEF002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_citation_display_label_review": CITATION_DISPLAY_LABEL_REVIEW_REL_PATH,
        "linked_citation_text_prep": CITATION_TEXT_PREP_REL_PATH,
        "linked_final_legal_wording_review": FINAL_LEGAL_WORDING_REVIEW_REL_PATH,
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

    if BATCH_MANIFEST_PATH.exists():
        text = BATCH_MANIFEST_PATH.read_text(encoding="utf-8")
        required_fragments = [
            "batch_id: MVP_BATCH_01",
            "current_stage: claim_slots_mapped",
            "operator_acceptance_status: not_accepted",
            "claim_map: docs/content/claim_maps/source-to-claim-map-batch-01.md",
            f"- {SOURCE_REVIEW_REL_PATH}",
            f"- {EVIDENCE_CAPTURE_REL_PATH}",
            f"serp_observation: {SERP_OBSERVATION_REL_PATH}",
            f"- {ARTICLE_REVIEW_REL_PATH}",
            "article_draft_candidates:",
            "article_reviews:",
            "article_draft_candidate_fixes:",
            "Brief 002 draft candidate fix re-review passed, but no publish readiness is set.",
            "No final article draft exists.",
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
            "current_stage: article_draft_candidate",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "publish_ready",
        ]
        for fragment in forbidden_fragments:
            if fragment in text:
                failures.append(f"Batch manifest must not contain: {fragment}")
        if "No article draft exists." in text:
            failures.append("Batch manifest must use 'No final article draft exists.' after draft candidate creation")

    if STATUS_REGISTRY_PATH.exists():
        registry_text = STATUS_REGISTRY_PATH.read_text(encoding="utf-8")
        required_status_fragments = [
            "re_review_passed",
            "re_review_passed_not_publish_ready",
            "packet_status:",
            "prepared_for_operator_review",
            "publish_readiness_status:",
            "not_ready",
            "decision_status:",
            "proceed_to_source_citation_and_legal_wording_preparation",
            "proceed_to_final_article_preparation_not_publish_ready",
            "prep_status:",
            "prepared_not_final",
            "legal_approval_status:",
            "not_approved",
            "gate_status:",
            "blocked_pending_final_citation_and_legal_review",
            "label_status:",
            "operational_status:",
            "internal_operations_ready",
            "public_launch_status:",
            "roadmap_status:",
            "baseline_defined",
            "citation_text_status:",
            "legal_wording_review_status:",
            "wording_review_prepared_no_legal_approval",
            "source_list_review_status:",
            "source_list_prepared_not_final",
            "review_status:",
            "human_controlled:",
            "approved_for_publish",
            "forbidden_by_codex:",
            "publish_ready",
            "operator_accepted",
        ]
        for fragment in required_status_fragments:
            if fragment not in registry_text:
                failures.append(f"STATUS_REGISTRY.yaml must contain hardened status marker: {fragment}")

        if "approved_for_publish\n" in registry_text and "forbidden_by_codex:" not in registry_text:
            failures.append("STATUS_REGISTRY.yaml must document approved_for_publish as forbidden for Codex")


def validate_review_findings_register(failures: list[str]) -> None:
    if not REVIEW_FINDINGS_REGISTER_PATH.exists():
        failures.append("Missing review findings register: docs/operations/REVIEW_FINDINGS_REGISTER.md")
        return

    lines = REVIEW_FINDINGS_REGISTER_PATH.read_text(encoding="utf-8").splitlines()
    by_id = {}
    for line in lines:
        if line.startswith("| SHO-"):
            parts = [part.strip() for part in line.strip("|").split("|")]
            if parts:
                by_id[parts[0]] = parts

    expected_re_review_passed = [
        "SHO-ARTICLE-002-UX-001",
        "SHO-ARTICLE-002-UX-002",
        "SHO-ARTICLE-002-SAFE-001",
        "SHO-ARTICLE-002-SRC-001",
    ]
    for finding_id in expected_re_review_passed:
        parts = by_id.get(finding_id)
        if not parts:
            failures.append(f"Review findings register must contain {finding_id}")
            continue
        if len(parts) < 4 or parts[3] != "re_review_passed":
            failures.append(f"Review finding {finding_id} must have status re_review_passed")

    expected_guardrails = [
        "SHO-ARTICLE-002-GATE-001",
        "SHO-ARTICLE-002-MON-001",
        "SHO-ARTICLE-002-PUB-001",
    ]
    for finding_id in expected_guardrails:
        parts = by_id.get(finding_id)
        if not parts:
            failures.append(f"Review findings register must contain {finding_id}")
            continue
        if len(parts) < 4 or parts[3] != "pass_carried_forward":
            failures.append(f"Guardrail finding {finding_id} must stay pass_carried_forward")


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
        if fields.get("article_draft_scaffold_path") != expected["draft_scaffold"]:
            failures.append(f"Research enrichment {file_name} must link to expected draft scaffold")
        if normalized(fields.get("draft_scaffold_status")) != "article_draft_scaffold":
            failures.append(f"Research enrichment {file_name} must have draft_scaffold_status: article_draft_scaffold")

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


def validate_article_draft_scaffolds(failures: list[str]) -> int:
    if not ARTICLE_DRAFT_SCAFFOLDS_DIR.exists():
        failures.append("Missing article draft scaffold directory: docs/content/article_draft_scaffolds")
        return 0

    required_paths = [
        ARTICLE_DRAFT_SCAFFOLDS_DIR / "README.md",
        ARTICLE_DRAFT_SCAFFOLDS_DIR / "ARTICLE_DRAFT_SCAFFOLD_TEMPLATE.md",
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing article draft scaffold file: {path.relative_to(ROOT).as_posix()}")

    found_files = {path.name for path in ARTICLE_DRAFT_SCAFFOLDS_DIR.glob("*.draft-scaffold.md")}
    expected_files = set(EXPECTED_ARTICLE_DRAFT_SCAFFOLDS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these draft scaffold files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_DRAFT_SCAFFOLDS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        text_lower = text.lower()
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_ARTICLE_DRAFT_SCAFFOLDS[file_name]

        required_fragments = [
            "draft_scaffold_status: article_draft_scaffold",
            "operator_acceptance_status: not_accepted",
            "linked_research_enrichment:",
            "linked_claim_map:",
            "linked_serp_observation:",
            "Explicit Non-Acceptance",
            expected["brief_id"],
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Draft scaffold {file_name} must contain: {fragment}")
        for claim_id in expected["required_claims"]:
            if claim_id not in text:
                failures.append(f"Draft scaffold {file_name} must contain claim: {claim_id}")
        for term in expected["required_terms"]:
            if term.lower() not in text_lower:
                failures.append(f"Draft scaffold {file_name} must contain marker: {term}")

        if normalized(fields.get("draft_scaffold_status")) != "article_draft_scaffold":
            failures.append(f"Draft scaffold {file_name} must have draft_scaffold_status: article_draft_scaffold")
        if normalized(fields.get("operator_acceptance_status")) == "accepted":
            failures.append(f"Draft scaffold {file_name} must not have accepted operator status")
        if fields.get("linked_research_enrichment") != expected["enrichment"]:
            failures.append(f"Draft scaffold {file_name} must link to expected research enrichment")
        if expected["article_candidate"]:
            if fields.get("article_draft_candidate_path") != expected["article_candidate"]:
                failures.append(f"Draft scaffold {file_name} must link to expected article draft candidate")
            if normalized(fields.get("article_status")) != "article_draft_candidate":
                failures.append(f"Draft scaffold {file_name} must have article_status: article_draft_candidate")
        elif "article_draft_candidate_path" in fields or normalized(fields.get("article_status")) == "article_draft_candidate":
            failures.append(f"Draft scaffold {file_name} must not link to an article draft candidate")
        if fields.get("linked_claim_map") != CLAIM_MAP_REL_PATH:
            failures.append(f"Draft scaffold {file_name} must link to claim map")
        if fields.get("linked_serp_observation") != SERP_OBSERVATION_REL_PATH:
            failures.append(f"Draft scaffold {file_name} must link to SERP observation")

        forbidden_fragments = [
            "approved_for_publish",
            "operator_acceptance_status: accepted",
            "publish_ready",
            "final_article_text",
            "ranking guarantee",
            "search volume",
            "keyword difficulty",
        ]
        for fragment in forbidden_fragments:
            if fragment in text_lower:
                failures.append(f"Draft scaffold {file_name} must not contain: {fragment}")
        if "SHO-MVP-BRIEF-001" in text or "SHO-MVP-BRIEF-004" in text:
            failures.append(f"Draft scaffold {file_name} must not scaffold Brief 001 or Brief 004")

    return len(found_files)


def has_forbidden_status_assignment(text: str) -> bool:
    forbidden_patterns = [
        "approved_for_publish: true",
        "review_status: approved_for_publish",
        "current_stage: publish_candidate",
        "operator_acceptance_status: accepted",
        "publish_ready: true",
    ]
    lower_text = text.lower()
    return any(pattern in lower_text for pattern in forbidden_patterns)


def validate_article_draft_candidates(failures: list[str]) -> int:
    if not ARTICLE_DRAFT_CANDIDATES_DIR.exists():
        failures.append("Missing article draft candidate directory: docs/content/article_draft_candidates")
        return 0

    required_paths = [
        ARTICLE_DRAFT_CANDIDATES_DIR / "README.md",
        ARTICLE_DRAFT_CANDIDATES_DIR / "ARTICLE_DRAFT_CANDIDATE_TEMPLATE.md",
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing article draft candidate file: {path.relative_to(ROOT).as_posix()}")

    found_files = {path.name for path in ARTICLE_DRAFT_CANDIDATES_DIR.glob("*.article-draft-candidate.md")}
    expected_files = set(EXPECTED_ARTICLE_DRAFT_CANDIDATES)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these article draft candidate files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_DRAFT_CANDIDATES_DIR / file_name
        text = path.read_text(encoding="utf-8")
        text_lower = text.lower()
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_ARTICLE_DRAFT_CANDIDATES[file_name]

        required_fragments = [
            f"article_draft_candidate_id: {expected['article_draft_candidate_id']}",
            f"linked_brief_id: {expected['brief_id']}",
            "article_status: article_draft_candidate",
            "review_status: re_review_passed_not_publish_ready",
            "operator_acceptance_status: not_accepted",
            f"article_review_path: {expected['article_review']}",
            "fix_patch_id: ARTICLE_DRAFT_CANDIDATE_FIX_BATCH_01_BRIEF_002",
            "fixed_review_findings",
            "SHO-ARTICLE-002-UX-001",
            "SHO-ARTICLE-002-UX-002",
            "SHO-ARTICLE-002-SAFE-001",
            "SHO-ARTICLE-002-SRC-001",
            "3-Schritte-Sofort-Check",
            "Evidence Markers Used",
            "Explicit Non-Acceptance",
            "SHO-CLAIM-007",
            "blocked",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Article draft candidate {file_name} must contain: {fragment}")
        for claim_id in expected["required_claims"]:
            if claim_id not in text:
                failures.append(f"Article draft candidate {file_name} must contain claim: {claim_id}")
        for source_id in expected["required_sources"]:
            if source_id not in text:
                failures.append(f"Article draft candidate {file_name} must contain source: {source_id}")

        if fields.get("article_draft_candidate_id") != expected["article_draft_candidate_id"]:
            failures.append(f"Article draft candidate {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Article draft candidate {file_name} must link to Brief 002")
        if fields.get("linked_draft_scaffold") != expected["draft_scaffold"]:
            failures.append(f"Article draft candidate {file_name} must link to expected draft scaffold")
        if fields.get("linked_research_enrichment") != expected["research_enrichment"]:
            failures.append(f"Article draft candidate {file_name} must link to expected research enrichment")
        if fields.get("article_review_path") != expected["article_review"]:
            failures.append(f"Article draft candidate {file_name} must link to expected article review")
        if fields.get("linked_claim_map") != CLAIM_MAP_REL_PATH:
            failures.append(f"Article draft candidate {file_name} must link to claim map")
        if fields.get("linked_source_pack") != SOURCE_PACK_REL_PATH:
            failures.append(f"Article draft candidate {file_name} must link to source pack")
        if fields.get("linked_serp_observation") != SERP_OBSERVATION_REL_PATH:
            failures.append(f"Article draft candidate {file_name} must link to SERP observation")
        if normalized(fields.get("article_status")) != "article_draft_candidate":
            failures.append(f"Article draft candidate {file_name} must have article_status: article_draft_candidate")
        if normalized(fields.get("review_status")) != "re_review_passed_not_publish_ready":
            failures.append(f"Article draft candidate {file_name} must have review_status: re_review_passed_not_publish_ready")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Article draft candidate {file_name} must have operator_acceptance_status: not_accepted")

        if "article_status: publish_candidate" in text_lower or "article_status: review_ready" in text_lower:
            failures.append(f"Article draft candidate {file_name} must not be review_ready or publish_candidate")
        if "SHO-CLAIM-007 remains blocked" not in text:
            failures.append(f"Article draft candidate {file_name} must preserve SHO-CLAIM-007 as blocked")
        if "SHO-CLAIM-007" in text and "[claim: SHO-CLAIM-007" in text:
            failures.append(f"Article draft candidate {file_name} must not use SHO-CLAIM-007 as an evidence marker")

        forbidden_fragments = [
            "ranking guarantee",
            "search volume",
            "keyword difficulty",
            "affiliate",
            "product recommendation",
            "affiliate-link",
            "affiliate link",
            "produktempfehlung:",
            "empfohlenes produkt",
            "jetzt kaufen",
            "kaufen sie dieses",
        ]
        for fragment in forbidden_fragments:
            if fragment in text_lower:
                failures.append(f"Article draft candidate {file_name} must not contain: {fragment}")
        forbidden_whatsapp_ui_steps = [
            "tippen sie auf blockieren",
            "tippen sie auf melden",
            "kontakt blockieren",
            "chat melden",
            "menue > blockieren",
            "menü > blockieren",
            "einstellungen > blockieren",
            "blockieren-tipps",
        ]
        for fragment in forbidden_whatsapp_ui_steps:
            if fragment in text_lower:
                failures.append(f"Article draft candidate {file_name} must not contain WhatsApp UI instruction: {fragment}")
        forbidden_transliterations = [
            "Pruefen",
            "pruefen",
            "koennen",
            "Angehoerige",
            "Grosseltern",
            "Menuewege",
            "Ueberweisen",
            "verdaechtig",
            "spaeter",
            "naechsten",
            "Passwoerter",
        ]
        for fragment in forbidden_transliterations:
            if fragment in text:
                failures.append(f"Article draft candidate {file_name} must not contain transliteration: {fragment}")
        if has_forbidden_status_assignment(text):
            failures.append(f"Article draft candidate {file_name} contains a forbidden status assignment")
        if "SHO-MVP-BRIEF-001" in text or "SHO-MVP-BRIEF-003" in text or "SHO-MVP-BRIEF-004" in text:
            failures.append(f"Article draft candidate {file_name} must not target Brief 001, 003 or 004")

    return len(found_files)


def validate_article_reviews(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    required_paths = [
        ARTICLE_REVIEWS_DIR / "README.md",
        ARTICLE_REVIEWS_DIR / "ARTICLE_REVIEW_TEMPLATE.md",
    ]
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing article review file: {path.relative_to(ROOT).as_posix()}")

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.review.md")}
    expected_files = set(EXPECTED_ARTICLE_REVIEWS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these article review files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_ARTICLE_REVIEWS[file_name]

        required_fragments = [
            f"article_review_id: {expected['article_review_id']}",
            "review_status: review_completed_with_findings",
            "operator_acceptance_status: not_accepted",
            "ACCEPTED_FOR_FIX_PATCH",
            "Fix Patch Link",
            "ARTICLE_DRAFT_CANDIDATE_FIX_BATCH_01_BRIEF_002",
            "Re-Review Result",
            "ARTICLE_DRAFT_CANDIDATE_RE_REVIEW_BATCH_01_BRIEF_002",
            "re_review_status: re_review_passed_not_publish_ready",
            "Re-Review Finding Results",
            "SHO-ARTICLE-002-UX-001 | fixed_pending_re_review | re_review_passed",
            "SHO-ARTICLE-002-UX-002 | fixed_pending_re_review | re_review_passed",
            "SHO-ARTICLE-002-SAFE-001 | fixed_pending_re_review | re_review_passed",
            "SHO-ARTICLE-002-SRC-001 | fixed_pending_re_review | re_review_passed",
            "Blocked claim protection for SHO-CLAIM-007: pass",
            "Monetization guardrail: pass",
            "Publish readiness: not_ready",
            "Explicit Non-Acceptance",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Article review {file_name} must contain: {fragment}")
        for finding_id in expected["finding_ids"]:
            if finding_id not in text:
                failures.append(f"Article review {file_name} must contain finding: {finding_id}")

        if fields.get("article_review_id") != expected["article_review_id"]:
            failures.append(f"Article review {file_name} has unexpected ID")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Article review {file_name} must link to expected article draft candidate")
        if normalized(fields.get("review_status")) != "review_completed_with_findings":
            failures.append(f"Article review {file_name} must have review_status: review_completed_with_findings")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Article review {file_name} must have operator_acceptance_status: not_accepted")
        if "re_review_status: re_review_passed_not_publish_ready" not in text:
            failures.append(f"Article review {file_name} must keep separate body re_review_status")
        if normalized(fields.get("review_status")) == "re_review_passed_not_publish_ready":
            failures.append(f"Article review {file_name} must not replace original frontmatter review_status with re_review_status")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_ready: true",
            "review_status: approved_for_publish",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Article review {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_operator_review_packets(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.operator-review-packet.md")}
    expected_files = set(EXPECTED_OPERATOR_REVIEW_PACKETS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these operator review packet files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_OPERATOR_REVIEW_PACKETS[file_name]

        required_fragments = [
            f"operator_review_packet_id: {expected['operator_review_packet_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
            f"linked_article_review: {expected['linked_article_review']}",
            f"linked_findings_register: {expected['linked_findings_register']}",
            "packet_status: prepared_for_operator_review",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "Explicit Non-Acceptance",
            "Dieses Paket ist keine Operator Acceptance.",
            "Dieses Paket ist keine Publish Readiness.",
            "Dieses Paket schaltet keine blockierten Claims frei.",
            "Operator Review Checklist",
            "Senior UX pruefen",
            "Verstaendlichkeit fuer Senior:innen pruefen",
            "Sicherheitsformulierung pruefen",
            "Keine Angstverstaerkung pruefen",
            "Quellen-/Claim-Marker pruefen",
            "Blockierte WhatsApp-UI-Anweisungen pruefen",
            "Keine Monetarisierung pruefen",
            "Keine Produkt-/Affiliate-Empfehlung pruefen",
            "Claim/Source Summary",
            "SHO-CLAIM-004",
            "SHO-CLAIM-005",
            "SHO-CLAIM-006",
            "SHO-SRC-005",
            "SHO-SRC-006",
            "SHO-SRC-007",
            "SHO-CLAIM-007",
            "SHO-ARTICLE-002-UX-001`: re_review_passed",
            "SHO-ARTICLE-002-UX-002`: re_review_passed",
            "SHO-ARTICLE-002-SAFE-001`: re_review_passed",
            "SHO-ARTICLE-002-SRC-001`: re_review_passed",
            "Remaining Blockers",
            "no final legal review",
            "no final source citation formatting",
            "no Operator Acceptance",
            "no publish readiness",
            "WhatsApp block/report UI claim remains blocked",
            "no WhatsApp line evidence / UI review for `SHO-CLAIM-007`",
            "Permitted Future Operator Decisions",
            "request another content fix",
            "request legal/source citation review",
            "request final article preparation",
            "keep as draft candidate",
            "reject candidate",
            "Forbidden Automated Decisions",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not unlock `SHO-CLAIM-007`",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Operator review packet {file_name} must contain: {fragment}")

        if fields.get("operator_review_packet_id") != expected["operator_review_packet_id"]:
            failures.append(f"Operator review packet {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Operator review packet {file_name} must link to Brief 002")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Operator review packet {file_name} must link to expected draft candidate")
        if fields.get("linked_article_review") != expected["linked_article_review"]:
            failures.append(f"Operator review packet {file_name} must link to expected article review")
        if fields.get("linked_findings_register") != expected["linked_findings_register"]:
            failures.append(f"Operator review packet {file_name} must link to findings register")
        if normalized(fields.get("packet_status")) != "prepared_for_operator_review":
            failures.append(f"Operator review packet {file_name} must have packet_status: prepared_for_operator_review")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Operator review packet {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Operator review packet {file_name} must have publish_readiness_status: not_ready")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Operator review packet {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_legal_source_citation_reviews(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.legal-source-citation-review.md")}
    expected_files = set(EXPECTED_LEGAL_SOURCE_CITATION_REVIEWS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these legal/source citation review files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_LEGAL_SOURCE_CITATION_REVIEWS[file_name]

        required_fragments = [
            f"legal_source_citation_review_id: {expected['legal_source_citation_review_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
            f"linked_article_review: {expected['linked_article_review']}",
            f"linked_operator_review_packet: {expected['linked_operator_review_packet']}",
            "review_status: prepared_for_operator_review",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "Explicit Non-Acceptance",
            "Diese Review ist keine Rechtsberatung.",
            "Diese Review ist keine rechtliche Freigabe.",
            "Diese Review ist keine Operator Acceptance.",
            "Diese Review ist keine Publish Readiness.",
            "Diese Review schaltet keine blockierten Claims frei.",
            "Legal / Safety Review Points",
            "keine Garantieversprechen",
            "keine Panikverstaerkung",
            "keine juristische Beratung",
            "keine Handlungsanweisungen, die Beweise/Kommunikation rechtlich riskant veraendern koennten",
            "keine Behauptung vollstaendiger Betrugserkennung",
            "bei Unsicherheit Vertrauensperson oder zustaendige Stelle fragen",
            "Source Citation Formatting Review",
            "SHO-CLAIM-004",
            "SHO-CLAIM-005",
            "SHO-CLAIM-006",
            "SHO-SRC-005",
            "SHO-SRC-006",
            "SHO-SRC-007",
            "markers present",
            "final citation formatting still missing",
            "no final source list for publication prepared",
            "source formatting review required before final article preparation",
            "Blocked Claims",
            "SHO-CLAIM-007` remains blocked",
            "no WhatsApp line evidence / UI review available",
            "no WhatsApp block/report UI instructions allowed",
            "SHO-ARTICLE-002-LEGAL-001",
            "SHO-ARTICLE-002-CITE-001",
            "SHO-ARTICLE-002-PUB-GATE-001",
            "Recommended Next Operator Decisions",
            "request final source citation formatting",
            "request legal wording review",
            "request another content fix",
            "keep draft as candidate",
            "reject candidate",
            "later request final article preparation",
            "Forbidden Automated Decisions",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not unlock `SHO-CLAIM-007`",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Legal/source citation review {file_name} must contain: {fragment}")

        if fields.get("legal_source_citation_review_id") != expected["legal_source_citation_review_id"]:
            failures.append(f"Legal/source citation review {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Legal/source citation review {file_name} must link to Brief 002")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Legal/source citation review {file_name} must link to expected draft candidate")
        if fields.get("linked_article_review") != expected["linked_article_review"]:
            failures.append(f"Legal/source citation review {file_name} must link to expected article review")
        if fields.get("linked_operator_review_packet") != expected["linked_operator_review_packet"]:
            failures.append(f"Legal/source citation review {file_name} must link to operator review packet")
        if normalized(fields.get("review_status")) != "prepared_for_operator_review":
            failures.append(f"Legal/source citation review {file_name} must have review_status: prepared_for_operator_review")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Legal/source citation review {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Legal/source citation review {file_name} must have publish_readiness_status: not_ready")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "rechtliche_freigabe: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Legal/source citation review {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_operator_decisions(failures: list[str]) -> int:
    if not OPERATOR_DECISIONS_DIR.exists():
        failures.append("Missing operator decisions directory: docs/operations/operator_decisions")
        return 0

    readme = OPERATOR_DECISIONS_DIR / "README.md"
    if not readme.exists():
        failures.append("Missing operator decisions README: docs/operations/operator_decisions/README.md")

    found_files = {path.name for path in OPERATOR_DECISIONS_DIR.glob("HUMAN_OPERATOR_DECISION_*.md")}
    expected_files = set(EXPECTED_OPERATOR_DECISIONS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these operator decision files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = OPERATOR_DECISIONS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_OPERATOR_DECISIONS[file_name]

        required_fragments = [
            f"operator_decision_id: {expected['operator_decision_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
            f"decision_status: {expected['decision_status']}",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "batch_stage_after_decision: claim_slots_mapped",
            "Decision Summary",
            "Explicit Non-Acceptance",
            "Diese Entscheidung ist keine Operator Acceptance.",
            "Diese Entscheidung ist keine Publish Readiness.",
            "Diese Entscheidung ist keine rechtliche Freigabe.",
            "Diese Entscheidung schaltet keine blockierten Claims frei.",
            "Diese Entscheidung erlaubt keine WhatsApp block/report UI instructions.",
            "Diese Entscheidung erlaubt keine Monetarisierung.",
            "Allowed Next Work",
            "Forbidden Work",
            "approve_for_publish",
            "operator_accepted",
            "publish_candidate",
            "review_ready stage transition",
            "add WhatsApp block/report UI instructions",
            "add monetization",
            "add new claims",
            "add new sources",
            "Required Next Gates",
            "no final article without explicit later Operator decision",
        ]
        if file_name == "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001.md":
            required_fragments.extend(
                [
                    f"linked_operator_review_packet: {expected['linked_operator_review_packet']}",
                    f"linked_legal_source_citation_review: {expected['linked_legal_source_citation_review']}",
                    "final source citation formatting preparation und legal wording review preparation",
                    "Der Draft bleibt Article Draft Candidate.",
                    "Der Batch bleibt nicht publish-ready.",
                    "Es wird keine Operator Acceptance gesetzt.",
                    "prepare final source citation formatting",
                    "prepare legal wording review",
                    "preserve claim/source traceability",
                    "preserve senior-first safety language",
                    "preserve blocked state for `SHO-CLAIM-007`",
                    "unlock `SHO-CLAIM-007`",
                    "final source citation formatting preparation",
                    "legal wording review preparation",
                    "later Human Operator review before any final article preparation",
                ]
            )
        else:
            required_fragments.extend(
                [
                    f"linked_final_source_list_review: {expected['linked_final_source_list_review']}",
                    f"linked_final_legal_wording_review: {expected['linked_final_legal_wording_review']}",
                    f"linked_final_article_prep_gate_review: {expected['linked_final_article_prep_gate_review']}",
                    "Human Operator erlaubt finale Artikelvorbereitung für Brief 002.",
                    "Diese Entscheidung erlaubt keine Veröffentlichung.",
                    "Diese Entscheidung setzt keine Operator Acceptance.",
                    "Diese Entscheidung setzt keine Publish Readiness.",
                    "Diese Entscheidung lässt SHO-CLAIM-007 blockiert.",
                    "Diese Entscheidung ist keine Veröffentlichungsgenehmigung.",
                    "prepare final article candidate text for Brief 002",
                    "preserve existing approved claim/source boundaries",
                    "use only allowed claims SHO-CLAIM-004, SHO-CLAIM-005, SHO-CLAIM-006",
                    "use only allowed sources SHO-SRC-005, SHO-SRC-006, SHO-SRC-007",
                    "preserve senior-first safety language",
                    "preserve blocked state for SHO-CLAIM-007",
                    "preserve non-final source metadata status",
                    "public_launch_ready",
                    "unlock SHO-CLAIM-007",
                    "claim legal approval",
                    "final article candidate preparation",
                    "final article candidate review",
                    "later Human Operator review before publish candidate",
                ]
            )
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Operator decision {file_name} must contain: {fragment}")

        if fields.get("operator_decision_id") != expected["operator_decision_id"]:
            failures.append(f"Operator decision {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Operator decision {file_name} must link to Brief 002")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Operator decision {file_name} must link to expected draft candidate")
        if file_name == "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001.md":
            if fields.get("linked_operator_review_packet") != expected["linked_operator_review_packet"]:
                failures.append(f"Operator decision {file_name} must link to operator review packet")
            if fields.get("linked_legal_source_citation_review") != expected["linked_legal_source_citation_review"]:
                failures.append(f"Operator decision {file_name} must link to legal/source citation review")
        else:
            if fields.get("linked_final_source_list_review") != expected["linked_final_source_list_review"]:
                failures.append(f"Operator decision {file_name} must link to final source list review")
            if fields.get("linked_final_legal_wording_review") != expected["linked_final_legal_wording_review"]:
                failures.append(f"Operator decision {file_name} must link to final legal wording review")
            if fields.get("linked_final_article_prep_gate_review") != expected["linked_final_article_prep_gate_review"]:
                failures.append(f"Operator decision {file_name} must link to final article prep gate review")
        if normalized(fields.get("decision_status")) != expected["decision_status"]:
            failures.append(f"Operator decision {file_name} must have the expected decision_status")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Operator decision {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Operator decision {file_name} must have publish_readiness_status: not_ready")
        if normalized(fields.get("batch_stage_after_decision")) != "claim_slots_mapped":
            failures.append(f"Operator decision {file_name} must keep batch_stage_after_decision: claim_slots_mapped")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "rechtliche_freigabe: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Operator decision {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_source_citation_formatting_preps(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.source-citation-formatting-prep.md")}
    expected_files = set(EXPECTED_SOURCE_CITATION_FORMATTING_PREPS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these source citation formatting prep files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_SOURCE_CITATION_FORMATTING_PREPS[file_name]

        required_fragments = [
            f"source_citation_formatting_prep_id: {expected['source_citation_formatting_prep_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
            f"linked_article_review: {expected['linked_article_review']}",
            f"linked_operator_decision: {expected['linked_operator_decision']}",
            "prep_status: prepared_not_final",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "Explicit Non-Acceptance",
            "Dieses Artefakt ist keine finale Quellenliste.",
            "Dieses Artefakt ist keine Publish Readiness.",
            "Dieses Artefakt ist keine Operator Acceptance.",
            "Dieses Artefakt ist keine rechtliche Freigabe.",
            "Dieses Artefakt schaltet keine blockierten Claims frei.",
            "Claim/Source Marker Inventory",
            "SHO-CLAIM-004 -> SHO-SRC-005, SHO-SRC-006",
            "SHO-CLAIM-005 -> SHO-SRC-005, SHO-SRC-006",
            "SHO-CLAIM-006 -> SHO-SRC-007",
            "SHO-CLAIM-007 remains blocked",
            "no WhatsApp line evidence / UI review available",
            "no WhatsApp block/report UI instructions allowed",
            "do not cite SHO-CLAIM-007 in final article until separately unblocked",
            "Source Formatting Preparation",
            "TBD_BY_OPERATOR_OR_SOURCE_FORMATTING_REVIEW",
            "publication_ready",
            "| SHO-SRC-005 |",
            "| SHO-SRC-006 |",
            "| SHO-SRC-007 |",
            "final display labels need review",
            "final citation text needs review",
            "final source list needs review",
            "legal wording review still required",
            "later Human Operator review required before final article preparation",
            "Forbidden Automated Decisions",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not unlock SHO-CLAIM-007",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
            "Codex must not add new claims",
            "Codex must not add new sources",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Source citation formatting prep {file_name} must contain: {fragment}")

        if fields.get("source_citation_formatting_prep_id") != expected["source_citation_formatting_prep_id"]:
            failures.append(f"Source citation formatting prep {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Source citation formatting prep {file_name} must link to Brief 002")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Source citation formatting prep {file_name} must link to expected draft candidate")
        if fields.get("linked_article_review") != expected["linked_article_review"]:
            failures.append(f"Source citation formatting prep {file_name} must link to expected article review")
        if fields.get("linked_operator_decision") != expected["linked_operator_decision"]:
            failures.append(f"Source citation formatting prep {file_name} must link to operator decision")
        if normalized(fields.get("prep_status")) != "prepared_not_final":
            failures.append(f"Source citation formatting prep {file_name} must have prep_status: prepared_not_final")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Source citation formatting prep {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Source citation formatting prep {file_name} must have publish_readiness_status: not_ready")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "rechtliche_freigabe: true",
            "publication_ready: yes",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(
                    f"Source citation formatting prep {file_name} must not contain forbidden assignment: {fragment}"
                )

    return len(found_files)


def validate_legal_wording_review_preps(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.legal-wording-review-prep.md")}
    expected_files = set(EXPECTED_LEGAL_WORDING_REVIEW_PREPS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these legal wording review prep files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_LEGAL_WORDING_REVIEW_PREPS[file_name]

        required_fragments = [
            f"legal_wording_review_prep_id: {expected['legal_wording_review_prep_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
            f"linked_operator_decision: {expected['linked_operator_decision']}",
            f"linked_source_citation_formatting_prep: {expected['linked_source_citation_formatting_prep']}",
            "prep_status: prepared_not_final",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "legal_approval_status: not_approved",
            "Explicit Non-Acceptance",
            "Dieses Artefakt ist keine Rechtsberatung.",
            "Dieses Artefakt ist keine rechtliche Freigabe.",
            "Dieses Artefakt ist keine Publish Readiness.",
            "Dieses Artefakt ist keine Operator Acceptance.",
            "Dieses Artefakt finalisiert keine Artikelpassage.",
            "Dieses Artefakt schaltet keine blockierten Claims frei.",
            "Legal Wording Risk Review",
            "keine Garantie, Betrug immer sicher zu erkennen",
            "keine juristische Beratung",
            "Sicherheitsorientierung statt Rechtsberatung",
            "keine Aufforderung zu riskanter Kommunikation mit Betruegern",
            "keine Panikverstaerkung",
            "keine vollstaendige Rechts-/Sicherheitszusage",
            "keine finalen WhatsApp block/report UI instructions",
            "Existing Safe Wording Markers",
            "Dieser Entwurf gibt keine Garantie, Betrug immer sicher zu erkennen.",
            "Er ist keine juristische Beratung.",
            "Dieser Text ist ein Draft Candidate.",
            "Er ist noch keine finale Anleitung.",
            "SHO-CLAIM-007 remains blocked",
            "SHO-ARTICLE-002-LEGAL-WORDING-001",
            "SHO-ARTICLE-002-LEGAL-WORDING-002",
            "SHO-ARTICLE-002-LEGAL-WORDING-003",
            "SHO-ARTICLE-002-LEGAL-WORDING-004",
            "final legal wording review required",
            "final source citation formatting still required",
            "final article preparation still not started",
            "later Human Operator review required before final article preparation",
            "no final article without explicit later Operator decision",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not claim legal approval",
            "Codex must not unlock SHO-CLAIM-007",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
            "Codex must not add new claims",
            "Codex must not add new sources",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Legal wording review prep {file_name} must contain: {fragment}")

        if fields.get("legal_wording_review_prep_id") != expected["legal_wording_review_prep_id"]:
            failures.append(f"Legal wording review prep {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Legal wording review prep {file_name} must link to Brief 002")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Legal wording review prep {file_name} must link to expected draft candidate")
        if fields.get("linked_operator_decision") != expected["linked_operator_decision"]:
            failures.append(f"Legal wording review prep {file_name} must link to operator decision")
        if fields.get("linked_source_citation_formatting_prep") != expected["linked_source_citation_formatting_prep"]:
            failures.append(f"Legal wording review prep {file_name} must link to source citation formatting prep")
        if normalized(fields.get("prep_status")) != "prepared_not_final":
            failures.append(f"Legal wording review prep {file_name} must have prep_status: prepared_not_final")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Legal wording review prep {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Legal wording review prep {file_name} must have publish_readiness_status: not_ready")
        if normalized(fields.get("legal_approval_status")) != "not_approved":
            failures.append(f"Legal wording review prep {file_name} must have legal_approval_status: not_approved")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "legal_approval_status: approved",
            "rechtliche_freigabe: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Legal wording review prep {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_final_article_prep_gate_reviews(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.final-article-prep-gate-review.md")}
    expected_files = set(EXPECTED_FINAL_ARTICLE_PREP_GATE_REVIEWS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these final article prep gate review files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_FINAL_ARTICLE_PREP_GATE_REVIEWS[file_name]

        required_fragments = [
            f"final_article_prep_gate_review_id: {expected['final_article_prep_gate_review_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
            f"linked_article_review: {expected['linked_article_review']}",
            f"linked_operator_review_packet: {expected['linked_operator_review_packet']}",
            f"linked_operator_decision: {expected['linked_operator_decision']}",
            f"linked_source_citation_formatting_prep: {expected['linked_source_citation_formatting_prep']}",
            f"linked_legal_wording_review_prep: {expected['linked_legal_wording_review_prep']}",
            "gate_status: blocked_pending_final_citation_and_legal_review",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "legal_approval_status: not_approved",
            "batch_stage_after_gate_review: claim_slots_mapped",
            "Explicit Non-Acceptance",
            "Diese Gate Review ist keine finale Artikelvorbereitung.",
            "Diese Gate Review ist keine Publish Readiness.",
            "Diese Gate Review ist keine Operator Acceptance.",
            "Diese Gate Review ist keine rechtliche Freigabe.",
            "Diese Gate Review schaltet keine blockierten Claims frei.",
            "Diese Gate Review erlaubt keine WhatsApp block/report UI instructions.",
            "Diese Gate Review erlaubt keine Monetarisierung.",
            "Gate Checklist",
            "| Article Draft Candidate exists | yes |",
            "| Re-review passed | yes |",
            "| Operator Review Packet exists | yes |",
            "| Human Operator next-gate decision exists | yes |",
            "| Source Citation Formatting Prep exists | yes |",
            "| Legal Wording Review Prep exists | yes |",
            "| Final source citation formatting completed | no |",
            "| Final legal wording review completed | no |",
            "| Legal approval claimed | no |",
            "| Operator Acceptance exists | no |",
            "| Publish Readiness exists | no |",
            "| SHO-CLAIM-007 remains blocked | yes |",
            "| WhatsApp block/report UI instructions allowed | no |",
            "| Monetization allowed | no |",
            "final_article_preparation_blocked_pending_final_citation_and_legal_review",
            "reason: final citation display labels and final citation texts are still TBD",
            "reason: legal_approval_status remains not_approved",
            "reason: no later Human Operator decision for final article preparation exists",
            "Allowed Next Work",
            "final citation display label review",
            "final citation text preparation",
            "final legal wording review",
            "later Human Operator decision before final article preparation",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not claim legal approval",
            "Codex must not mark final article preparation as approved",
            "Codex must not unlock SHO-CLAIM-007",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
            "Codex must not add new claims",
            "Codex must not add new sources",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Final article prep gate review {file_name} must contain: {fragment}")

        if fields.get("final_article_prep_gate_review_id") != expected["final_article_prep_gate_review_id"]:
            failures.append(f"Final article prep gate review {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Final article prep gate review {file_name} must link to Brief 002")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Final article prep gate review {file_name} must link to expected draft candidate")
        if fields.get("linked_article_review") != expected["linked_article_review"]:
            failures.append(f"Final article prep gate review {file_name} must link to article review")
        if fields.get("linked_operator_review_packet") != expected["linked_operator_review_packet"]:
            failures.append(f"Final article prep gate review {file_name} must link to operator review packet")
        if fields.get("linked_operator_decision") != expected["linked_operator_decision"]:
            failures.append(f"Final article prep gate review {file_name} must link to operator decision")
        if fields.get("linked_source_citation_formatting_prep") != expected["linked_source_citation_formatting_prep"]:
            failures.append(f"Final article prep gate review {file_name} must link to source citation formatting prep")
        if fields.get("linked_legal_wording_review_prep") != expected["linked_legal_wording_review_prep"]:
            failures.append(f"Final article prep gate review {file_name} must link to legal wording review prep")
        if normalized(fields.get("gate_status")) != "blocked_pending_final_citation_and_legal_review":
            failures.append(
                f"Final article prep gate review {file_name} must have gate_status: blocked_pending_final_citation_and_legal_review"
            )
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Final article prep gate review {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Final article prep gate review {file_name} must have publish_readiness_status: not_ready")
        if normalized(fields.get("legal_approval_status")) != "not_approved":
            failures.append(f"Final article prep gate review {file_name} must have legal_approval_status: not_approved")
        if normalized(fields.get("batch_stage_after_gate_review")) != "claim_slots_mapped":
            failures.append(f"Final article prep gate review {file_name} must keep batch_stage_after_gate_review: claim_slots_mapped")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "legal_approval_status: approved",
            "final_article_preparation_approved: true",
            "rechtliche_freigabe: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Final article prep gate review {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_citation_display_label_reviews(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.citation-display-label-review.md")}
    expected_files = set(EXPECTED_CITATION_DISPLAY_LABEL_REVIEWS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these citation display label review files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_CITATION_DISPLAY_LABEL_REVIEWS[file_name]

        required_fragments = [
            f"citation_display_label_review_id: {expected['citation_display_label_review_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_source_citation_formatting_prep: {expected['linked_source_citation_formatting_prep']}",
            f"linked_final_article_prep_gate_review: {expected['linked_final_article_prep_gate_review']}",
            "label_status: prepared_not_final",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "Explicit Non-Acceptance",
            "Diese Review ist keine finale Quellenliste.",
            "Diese Review ist keine Publish Readiness.",
            "Diese Review ist keine Operator Acceptance.",
            "Diese Review ist keine rechtliche Freigabe.",
            "Diese Review fuegt keine neuen Quellen hinzu.",
            "Diese Review schaltet keine blockierten Claims frei.",
            "Source ID Scope",
            "SHO-SRC-005",
            "SHO-SRC-006",
            "SHO-SRC-007",
            "SHO-SRC-001",
            "SHO-SRC-002",
            "SHO-SRC-003",
            "SHO-SRC-004",
            "SHO-SRC-013",
            "Prepared Display Labels",
            "Quelle zu Betrugsmaschen mit neuer Nummer und Verifikationshinweisen",
            "Quelle zu Familien-/Seniorenkontext und Rückrufprüfung",
            "Quelle zu allgemeinen Phishing-/Smishing-Warnsignalen",
            "final_citation_text_status",
            "not_prepared",
            "publication_ready",
            "| SHO-SRC-005 |",
            "| SHO-SRC-006 |",
            "| SHO-SRC-007 |",
            "no new source IDs introduced",
            "no new claims introduced",
            "no final citation text prepared",
            "no final source list prepared",
            "SHO-CLAIM-007 remains blocked",
            "WhatsApp block/report UI instructions remain out of scope",
            "final citation text preparation",
            "final source list review",
            "final legal wording review",
            "later Human Operator review before final article preparation",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not claim legal approval",
            "Codex must not mark final article preparation as approved",
            "Codex must not unlock SHO-CLAIM-007",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
            "Codex must not add new claims",
            "Codex must not add new sources",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Citation display label review {file_name} must contain: {fragment}")

        if fields.get("citation_display_label_review_id") != expected["citation_display_label_review_id"]:
            failures.append(f"Citation display label review {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Citation display label review {file_name} must link to Brief 002")
        if fields.get("linked_source_citation_formatting_prep") != expected["linked_source_citation_formatting_prep"]:
            failures.append(f"Citation display label review {file_name} must link to source citation formatting prep")
        if fields.get("linked_final_article_prep_gate_review") != expected["linked_final_article_prep_gate_review"]:
            failures.append(f"Citation display label review {file_name} must link to final article prep gate review")
        if normalized(fields.get("label_status")) != "prepared_not_final":
            failures.append(f"Citation display label review {file_name} must have label_status: prepared_not_final")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Citation display label review {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Citation display label review {file_name} must have publish_readiness_status: not_ready")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "legal_approval_status: approved",
            "gate_status: approved",
            "label_status: approved",
            "final_citation_text_status: prepared",
            "publication_ready: yes",
            "final_source_list: true",
            "final_article_preparation_approved: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Citation display label review {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_citation_text_preps(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.citation-text-prep.md")}
    expected_files = set(EXPECTED_CITATION_TEXT_PREPS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these citation text prep files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_CITATION_TEXT_PREPS[file_name]

        required_fragments = [
            f"citation_text_prep_id: {expected['citation_text_prep_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_citation_display_label_review: {expected['linked_citation_display_label_review']}",
            f"linked_source_citation_formatting_prep: {expected['linked_source_citation_formatting_prep']}",
            f"linked_final_article_prep_gate_review: {expected['linked_final_article_prep_gate_review']}",
            "citation_text_status: prepared_not_final",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "Explicit Non-Acceptance",
            "Dieses Artefakt ist keine finale Quellenliste.",
            "Dieses Artefakt ist keine finale Citation-Freigabe.",
            "Dieses Artefakt ist keine Publish Readiness.",
            "Dieses Artefakt ist keine Operator Acceptance.",
            "Dieses Artefakt ist keine rechtliche Freigabe.",
            "Dieses Artefakt fuegt keine neuen Quellen hinzu.",
            "Dieses Artefakt schaltet keine blockierten Claims frei.",
            "Source ID Scope",
            "SHO-SRC-005",
            "SHO-SRC-006",
            "SHO-SRC-007",
            "Prepared Citation Texts",
            "Quelle zu Betrugsmaschen mit neuer Nummer und Verifikationshinweisen. Finaler Titel, Herausgeber, URL und Abrufdatum müssen vor Veröffentlichung geprüft werden.",
            "Quelle zu Familien-/Seniorenkontext und Rückrufprüfung. Finaler Titel, Herausgeber, URL und Abrufdatum müssen vor Veröffentlichung geprüft werden.",
            "Quelle zu allgemeinen Phishing-/Smishing-Warnsignalen. Finaler Titel, Herausgeber, URL und Abrufdatum müssen vor Veröffentlichung geprüft werden.",
            "citation_text_status",
            "prepared_not_final",
            "metadata_review_status",
            "needs_final_metadata_review",
            "publication_ready",
            "| SHO-SRC-005 |",
            "| SHO-SRC-006 |",
            "| SHO-SRC-007 |",
            "no new source IDs introduced",
            "no new claims introduced",
            "no final source list prepared",
            "no final citation approval claimed",
            "no source metadata invented",
            "SHO-CLAIM-007 remains blocked",
            "WhatsApp block/report UI instructions remain out of scope",
            "final source metadata review",
            "final citation text approval by Human Operator or defined source-formatting gate",
            "final source list review",
            "final legal wording review",
            "later Human Operator review before final article preparation",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not claim legal approval",
            "Codex must not claim final citation approval",
            "Codex must not mark final article preparation as approved",
            "Codex must not unlock SHO-CLAIM-007",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
            "Codex must not add new claims",
            "Codex must not add new sources",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Citation text prep {file_name} must contain: {fragment}")

        if fields.get("citation_text_prep_id") != expected["citation_text_prep_id"]:
            failures.append(f"Citation text prep {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Citation text prep {file_name} must link to Brief 002")
        if fields.get("linked_citation_display_label_review") != expected["linked_citation_display_label_review"]:
            failures.append(f"Citation text prep {file_name} must link to citation display label review")
        if fields.get("linked_source_citation_formatting_prep") != expected["linked_source_citation_formatting_prep"]:
            failures.append(f"Citation text prep {file_name} must link to source citation formatting prep")
        if fields.get("linked_final_article_prep_gate_review") != expected["linked_final_article_prep_gate_review"]:
            failures.append(f"Citation text prep {file_name} must link to final article prep gate review")
        if normalized(fields.get("citation_text_status")) != "prepared_not_final":
            failures.append(f"Citation text prep {file_name} must have citation_text_status: prepared_not_final")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Citation text prep {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Citation text prep {file_name} must have publish_readiness_status: not_ready")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "legal_approval_status: approved",
            "gate_status: approved",
            "citation_text_status: approved",
            "metadata_review_status: approved",
            "publication_ready: yes",
            "final_source_list: true",
            "final_citation_approval: true",
            "final_article_preparation_approved: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Citation text prep {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_final_legal_wording_reviews(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.final-legal-wording-review.md")}
    expected_files = set(EXPECTED_FINAL_LEGAL_WORDING_REVIEWS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these final legal wording review files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_FINAL_LEGAL_WORDING_REVIEWS[file_name]

        required_fragments = [
            f"final_legal_wording_review_id: {expected['final_legal_wording_review_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
            f"linked_legal_wording_review_prep: {expected['linked_legal_wording_review_prep']}",
            f"linked_citation_text_prep: {expected['linked_citation_text_prep']}",
            "legal_wording_review_status: wording_review_prepared_no_legal_approval",
            "legal_approval_status: not_approved",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "Explicit Non-Acceptance",
            "Diese Review ist keine Rechtsberatung.",
            "Diese Review ist keine rechtliche Freigabe.",
            "Diese Review ist keine Publish Readiness.",
            "Diese Review ist keine Operator Acceptance.",
            "Diese Review finalisiert keinen Artikel.",
            "Diese Review schaltet keine blockierten Claims frei.",
            "Legal Wording Checks",
            "| no-guarantee wording present | yes |",
            "| legal-advice disclaimer present | yes |",
            "| draft/non-final wording present | yes |",
            "| no panic amplification found | yes |",
            "| no WhatsApp block/report UI wording added | yes |",
            "| no claim of complete fraud detection | yes |",
            "| no legal approval claimed | yes |",
            "| final legal approval exists | no |",
            "| Operator Acceptance exists | no |",
            "| Publish Readiness exists | no |",
            "legal_wording_review_prepared_no_legal_approval",
            "wording appears suitable for later Human Operator final article review",
            "legal approval remains not_approved",
            "final article preparation remains blocked pending Human Operator decision and final source list review",
            "final source list review",
            "final metadata review",
            "later Human Operator decision for final article preparation",
            "no final article without explicit later Operator decision",
            "SHO-CLAIM-007 remains blocked",
            "No WhatsApp line evidence / UI review is available.",
            "No WhatsApp block/report UI instructions are allowed by this review.",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not claim legal approval",
            "Codex must not mark final article preparation as approved",
            "Codex must not unlock SHO-CLAIM-007",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
            "Codex must not add new claims",
            "Codex must not add new sources",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Final legal wording review {file_name} must contain: {fragment}")

        if fields.get("final_legal_wording_review_id") != expected["final_legal_wording_review_id"]:
            failures.append(f"Final legal wording review {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Final legal wording review {file_name} must link to Brief 002")
        if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
            failures.append(f"Final legal wording review {file_name} must link to expected draft candidate")
        if fields.get("linked_legal_wording_review_prep") != expected["linked_legal_wording_review_prep"]:
            failures.append(f"Final legal wording review {file_name} must link to legal wording review prep")
        if fields.get("linked_citation_text_prep") != expected["linked_citation_text_prep"]:
            failures.append(f"Final legal wording review {file_name} must link to citation text prep")
        if normalized(fields.get("legal_wording_review_status")) != "wording_review_prepared_no_legal_approval":
            failures.append(
                f"Final legal wording review {file_name} must have legal_wording_review_status: wording_review_prepared_no_legal_approval"
            )
        if normalized(fields.get("legal_approval_status")) != "not_approved":
            failures.append(f"Final legal wording review {file_name} must have legal_approval_status: not_approved")
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Final legal wording review {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Final legal wording review {file_name} must have publish_readiness_status: not_ready")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "legal_approval_status: approved",
            "legal_wording_review_status: approved",
            "gate_status: approved",
            "final_source_list: true",
            "final_article_preparation_approved: true",
            "rechtliche_freigabe: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Final legal wording review {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_final_source_list_reviews(failures: list[str]) -> int:
    if not ARTICLE_REVIEWS_DIR.exists():
        failures.append("Missing article review directory: docs/content/article_reviews")
        return 0

    found_files = {path.name for path in ARTICLE_REVIEWS_DIR.glob("*.final-source-list-review.md")}
    expected_files = set(EXPECTED_FINAL_SOURCE_LIST_REVIEWS)
    if found_files != expected_files:
        failures.append(
            "Batch 01 must contain exactly these final source list review files: "
            f"{', '.join(sorted(expected_files))}; found {', '.join(sorted(found_files))}"
        )

    for file_name in sorted(expected_files & found_files):
        path = ARTICLE_REVIEWS_DIR / file_name
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter_fields(text)
        expected = EXPECTED_FINAL_SOURCE_LIST_REVIEWS[file_name]

        required_fragments = [
            f"final_source_list_review_id: {expected['final_source_list_review_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
            f"linked_citation_display_label_review: {expected['linked_citation_display_label_review']}",
            f"linked_citation_text_prep: {expected['linked_citation_text_prep']}",
            f"linked_final_legal_wording_review: {expected['linked_final_legal_wording_review']}",
            "source_list_review_status: source_list_prepared_not_final",
            "operator_acceptance_status: not_accepted",
            "publish_readiness_status: not_ready",
            "Explicit Non-Acceptance",
            "Diese Review ist keine finale Quellenliste.",
            "Diese Review ist keine Publish Readiness.",
            "Diese Review ist keine Operator Acceptance.",
            "Diese Review ist keine rechtliche Freigabe.",
            "Diese Review fuegt keine neuen Quellen hinzu.",
            "Diese Review fuegt keine neuen Claims hinzu.",
            "Diese Review schaltet keine blockierten Claims frei.",
            "Source Scope",
            "SHO-SRC-005",
            "SHO-SRC-006",
            "SHO-SRC-007",
            "SHO-SRC-001",
            "SHO-SRC-002",
            "SHO-SRC-003",
            "SHO-SRC-004",
            "SHO-SRC-013",
            "SHO-CLAIM-007",
            "Prepared Source List Review Table",
            "Quelle zu Betrugsmaschen mit neuer Nummer und Verifikationshinweisen",
            "Quelle zu Familien-/Seniorenkontext und Rückrufprüfung",
            "Quelle zu allgemeinen Phishing-/Smishing-Warnsignalen",
            "Finaler Titel, Herausgeber, URL und Abrufdatum müssen vor Veröffentlichung geprüft werden.",
            "metadata_status",
            "needs_final_metadata_review",
            "source_list_status",
            "prepared_not_final",
            "publication_ready",
            "| SHO-SRC-005 |",
            "| SHO-SRC-006 |",
            "| SHO-SRC-007 |",
            "no new source IDs introduced",
            "no new claims introduced",
            "no final source metadata invented",
            "no final source list approval claimed",
            "no publish readiness claimed",
            "SHO-CLAIM-007 remains blocked",
            "WhatsApp block/report UI instructions remain out of scope",
            "final source metadata review",
            "later Human Operator decision for final article preparation",
            "final article preparation still not approved",
            "no final article without explicit later Operator decision",
            "Codex must not approve for publish",
            "Codex must not mark operator accepted",
            "Codex must not claim legal approval",
            "Codex must not claim final source list approval",
            "Codex must not mark final article preparation as approved",
            "Codex must not unlock SHO-CLAIM-007",
            "Codex must not add WhatsApp block/report UI instructions",
            "Codex must not add monetization",
            "Codex must not add new claims",
            "Codex must not add new sources",
        ]
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Final source list review {file_name} must contain: {fragment}")

        if fields.get("final_source_list_review_id") != expected["final_source_list_review_id"]:
            failures.append(f"Final source list review {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Final source list review {file_name} must link to Brief 002")
        if fields.get("linked_citation_display_label_review") != expected["linked_citation_display_label_review"]:
            failures.append(f"Final source list review {file_name} must link to citation display label review")
        if fields.get("linked_citation_text_prep") != expected["linked_citation_text_prep"]:
            failures.append(f"Final source list review {file_name} must link to citation text prep")
        if fields.get("linked_final_legal_wording_review") != expected["linked_final_legal_wording_review"]:
            failures.append(f"Final source list review {file_name} must link to final legal wording review")
        if normalized(fields.get("source_list_review_status")) != "source_list_prepared_not_final":
            failures.append(
                f"Final source list review {file_name} must have source_list_review_status: source_list_prepared_not_final"
            )
        if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
            failures.append(f"Final source list review {file_name} must have operator_acceptance_status: not_accepted")
        if normalized(fields.get("publish_readiness_status")) != "not_ready":
            failures.append(f"Final source list review {file_name} must have publish_readiness_status: not_ready")

        forbidden_assignments = [
            "approved_for_publish: true",
            "operator_acceptance_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "publish_ready: true",
            "current_stage: review_ready",
            "current_stage: publish_candidate",
            "legal_approval: true",
            "legal_approval_status: approved",
            "gate_status: approved",
            "source_list_review_status: approved",
            "publication_ready: yes",
            "final_source_list: true",
            "final_source_list_approval: true",
            "final_article_preparation_approved: true",
            "rechtliche_freigabe: true",
        ]
        lower_text = text.lower()
        for fragment in forbidden_assignments:
            if fragment in lower_text:
                failures.append(f"Final source list review {file_name} must not contain forbidden assignment: {fragment}")

    return len(found_files)


def validate_mvp_operational_start_plan(failures: list[str]) -> int:
    if not MVP_OPERATIONAL_START_PLAN_PATH.exists():
        failures.append("Missing MVP operational start plan: docs/operations/MVP_OPERATIONAL_START_PLAN_BATCH_01.md")
        return 0

    text = MVP_OPERATIONAL_START_PLAN_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_fragments = [
        "operational_start_plan_id: SHO-MVP-OPERATIONAL-START-BATCH01",
        "batch_id: MVP_BATCH_01",
        "operational_status: internal_operations_ready",
        "public_launch_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "Executive Summary",
        "Projekt kann operativ intern starten.",
        "Kein Artikel ist publish-ready.",
        "Brief 002 bleibt blockiert bis final citation/legal gates.",
        "Website-/Content-Operations duerfen vorbereitet werden.",
        "Monetarisierung bleibt out of scope.",
        "Operational Workstreams",
        "Content pipeline operations",
        "Website structure / information architecture",
        "Internal preview workflow",
        "Article readiness dashboard",
        "Brief 002 finalization gates",
        "Brief 003 draft candidate preparation",
        "Trust/legal/source workflow",
        "Analytics/feedback later, without public claims",
        "What Can Start Now",
        "repo-based content operations",
        "internal preview structure",
        "article readiness tracking",
        "next article candidate work",
        "design/UX system documentation",
        "website skeleton planning",
        "What Cannot Start Yet",
        "public launch",
        "monetization",
        "affiliate",
        "final publication",
        "WhatsApp UI block/report instructions",
        "publishing Brief 002",
        "claiming legal approval",
        "Current Brief 002 Gate State",
        "Article Draft Candidate exists.",
        "Re-review passed.",
        "Operator Decision exists.",
        "Source Citation Formatting Prep exists.",
        "Legal Wording Review Prep exists.",
        "Final Article Prep Gate Review blocks final article preparation.",
        "Citation Display Label Review exists.",
        "No Publish Readiness.",
        "No Operator Acceptance.",
        "SHO-CLAIM-007 remains blocked.",
        "WEBSITE_INFORMATION_ARCHITECTURE_MVP",
        "ARTICLE_READINESS_DASHBOARD_BATCH_01",
        "BRIEF_003_ARTICLE_DRAFT_CANDIDATE",
        "FINAL_CITATION_TEXT_PREPARATION_BRIEF_002",
        "FINAL_LEGAL_WORDING_REVIEW_BRIEF_002",
        "approve final article preparation",
        "approve publication candidate",
        "approve public launch",
        "approve monetization policy",
        "Explicit Non-Acceptance",
        "This plan is not Operator Acceptance.",
        "This plan is not Publish Readiness.",
        "This plan is not public launch approval.",
        "This plan does not approve monetization.",
        "This plan does not publish any article.",
        "This plan does not unlock SHO-CLAIM-007.",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(f"MVP operational start plan must contain: {fragment}")

    if fields.get("operational_start_plan_id") != "SHO-MVP-OPERATIONAL-START-BATCH01":
        failures.append("MVP operational start plan has unexpected ID")
    if normalized(fields.get("operational_status")) != "internal_operations_ready":
        failures.append("MVP operational start plan must have operational_status: internal_operations_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("MVP operational start plan must have public_launch_status: not_ready")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("MVP operational start plan must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("MVP operational start plan must have publish_readiness_status: not_ready")

    forbidden_assignments = [
        "approved_for_publish: true",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: publish_candidate",
        "publish_readiness_status: approved_for_publish",
        "publish_ready: true",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "current_stage: review_ready",
        "current_stage: publish_candidate",
        "legal_approval: true",
        "legal_approval_status: approved",
        "monetization_status: approved",
    ]
    lower_text = text.lower()
    for fragment in forbidden_assignments:
        if fragment in lower_text:
            failures.append(f"MVP operational start plan must not contain forbidden assignment: {fragment}")

    return 1


def validate_roadmap_mvp_2026(failures: list[str]) -> int:
    if not ROADMAP_MVP_2026_PATH.exists():
        failures.append("Missing MVP roadmap: docs/operations/ROADMAP_AND_MILESTONES_MVP_2026.md")
        return 0

    text = ROADMAP_MVP_2026_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_fragments = [
        "roadmap_id: SHO-ROADMAP-MVP-2026",
        "roadmap_status: baseline_defined",
        "scope: MVP_BATCH_01",
        'planning_horizon: "2026-06_to_2026-11"',
        "operational_status: internal_operations_ready",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "monetization_status: not_approved",
        "operator_acceptance_status: not_accepted",
        "Purpose",
        "Current Baseline",
        "Strategic Goal",
        "30-Day Goals",
        "60-Day Goals",
        "90-Day Goals",
        "6-Month Goals",
        "Milestones",
        "Phase Plan",
        "Quality Gates",
        "SEO/Analytics Gates",
        "Feedback Gates",
        "Monetization Gates",
        "Non-Goals",
        "Explicit Non-Acceptance",
        "Required Human Decisions",
        "M0 Governance Foundation",
        "M1 Quality Baseline",
        "M2 First Reviewed Article Candidates",
        "M3 Internal Website Preview",
        "M4 Launch Candidate Package",
        "M5 Controlled Public MVP Launch Candidate",
        "M6 First Optimization Loop",
        "M7 Validated Content System v1",
        "Phase 0: Foundation and Governance",
        "Phase 1: System Readiness and Quality Standard",
        "Phase 2: First Content Candidates",
        "Phase 3: Website MVP and Internal Preview",
        "Phase 4: SEO/Keyword Validation and Launch Gates",
        "Phase 5: Controlled MVP Launch Candidate",
        "Phase 6: Measurement, Feedback and Refresh Loop",
        "Phase 7: Scaling and Monetization Preparation",
        "No public launch without later explicit Operator decision.",
        "No monetization without later explicit Operator decision.",
        "No affiliate without monetization policy and product methodology.",
        "No publish readiness without article-level gates.",
        "No Operator Acceptance by Codex.",
        "No ranking, traffic or revenue claims without data.",
        "No user feedback claims before feedback exists.",
        "No WhatsApp block/report UI instructions while evidence remains blocked.",
        "SHO-CLAIM-007 remains blocked.",
        "Quality KPIs",
        "SEO KPIs",
        "User Feedback KPIs",
        "Operational KPIs",
        "Monetization KPIs later only",
        "roadmap is planning only",
        "Diese Roadmap ist planning only.",
        "Diese Roadmap aktiviert keinen Public Launch.",
        "Diese Roadmap setzt keine Publish Readiness.",
        "Diese Roadmap genehmigt keine Monetarisierung.",
        "Diese Roadmap erstellt keine Operator Acceptance.",
        "Quantitative SEO metrics are not available and must not be invented.",
        "Analytics/feedback loop is planned but not live.",
        "No real user emails or user feedback data exist yet and must not be invented.",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(f"MVP roadmap must contain: {fragment}")

    if fields.get("roadmap_id") != "SHO-ROADMAP-MVP-2026":
        failures.append("MVP roadmap has unexpected roadmap_id")
    if normalized(fields.get("roadmap_status")) != "baseline_defined":
        failures.append("MVP roadmap must have roadmap_status: baseline_defined")
    if normalized(fields.get("scope")) != "MVP_BATCH_01".lower():
        failures.append("MVP roadmap must have scope: MVP_BATCH_01")
    if (fields.get("planning_horizon") or "").strip('"') != "2026-06_to_2026-11":
        failures.append("MVP roadmap must have planning_horizon: 2026-06_to_2026-11")
    if normalized(fields.get("operational_status")) != "internal_operations_ready":
        failures.append("MVP roadmap must have operational_status: internal_operations_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("MVP roadmap must have public_launch_status: not_ready")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("MVP roadmap must have publish_readiness_status: not_ready")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("MVP roadmap must have monetization_status: not_approved")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("MVP roadmap must have operator_acceptance_status: not_accepted")

    forbidden_assignments = [
        "public_launch_status: ready",
        "public_launch_status: launched",
        "publish_readiness_status: approved_for_publish",
        "publish_readiness_status: publish_candidate",
        "operator_acceptance_status: accepted",
        "monetization_status: approved",
        "roadmap_status: active",
        "approved_for_publish: true",
        "publish_ready: true",
        "legal_approval: true",
        "legal_approval_status: approved",
        "current_stage: review_ready",
        "current_stage: publish_candidate",
    ]
    lower_text = text.lower()
    for fragment in forbidden_assignments:
        if fragment in lower_text:
            failures.append(f"MVP roadmap must not contain forbidden activation marker: {fragment}")

    return 1


def main() -> int:
    failures: list[str] = []

    validate_required_docs(failures)
    validate_protocol_automation_files(failures)
    validate_review_findings_register(failures)
    backlog_count = validate_backlog(failures)
    brief_count = validate_brief_scaffolds(failures)
    research_count = validate_research_inputs(failures)
    source_pack_count = validate_source_pack(failures)
    claim_map_count = validate_claim_map(failures)
    source_review_count = validate_source_review(failures)
    evidence_capture_count = validate_evidence_capture(failures)
    serp_observation_count = validate_serp_observation(failures)
    research_enrichment_count = validate_research_enrichments(failures)
    article_draft_scaffold_count = validate_article_draft_scaffolds(failures)
    article_draft_candidate_count = validate_article_draft_candidates(failures)
    article_review_count = validate_article_reviews(failures)
    operator_review_packet_count = validate_operator_review_packets(failures)
    legal_source_citation_review_count = validate_legal_source_citation_reviews(failures)
    operator_decision_count = validate_operator_decisions(failures)
    source_citation_formatting_prep_count = validate_source_citation_formatting_preps(failures)
    legal_wording_review_prep_count = validate_legal_wording_review_preps(failures)
    final_article_prep_gate_review_count = validate_final_article_prep_gate_reviews(failures)
    citation_display_label_review_count = validate_citation_display_label_reviews(failures)
    citation_text_prep_count = validate_citation_text_preps(failures)
    final_legal_wording_review_count = validate_final_legal_wording_reviews(failures)
    final_source_list_review_count = validate_final_source_list_reviews(failures)
    mvp_operational_start_plan_count = validate_mvp_operational_start_plan(failures)
    roadmap_mvp_2026_count = validate_roadmap_mvp_2026(failures)

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
    print(f"- Batch 01 article draft scaffold files: {article_draft_scaffold_count}")
    print(f"- Batch 01 article draft candidate files: {article_draft_candidate_count}")
    print(f"- Batch 01 article review files: {article_review_count}")
    print(f"- Batch 01 operator review packet files: {operator_review_packet_count}")
    print(f"- Batch 01 legal/source citation review files: {legal_source_citation_review_count}")
    print(f"- Batch 01 operator decision files: {operator_decision_count}")
    print(f"- Batch 01 source citation formatting prep files: {source_citation_formatting_prep_count}")
    print(f"- Batch 01 legal wording review prep files: {legal_wording_review_prep_count}")
    print(f"- Batch 01 final article prep gate review files: {final_article_prep_gate_review_count}")
    print(f"- Batch 01 citation display label review files: {citation_display_label_review_count}")
    print(f"- Batch 01 citation text prep files: {citation_text_prep_count}")
    print(f"- Batch 01 final legal wording review files: {final_legal_wording_review_count}")
    print(f"- Batch 01 final source list review files: {final_source_list_review_count}")
    print(f"- Batch 01 MVP operational start plan files: {mvp_operational_start_plan_count}")
    print(f"- Batch 01 MVP roadmap files: {roadmap_mvp_2026_count}")
    print("- YAML/frontmatter parsing: dependency-free and text-based")
    return 0


if __name__ == "__main__":
    sys.exit(main())
