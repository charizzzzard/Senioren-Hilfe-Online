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
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.accessibility-review.md",
    "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-metadata-review.md",
    "docs/operations/CONTENT_RESEARCH_OPERATING_PROTOCOL.md",
    "docs/operations/RESEARCH_BATCH_STAGE_MODEL.md",
    "docs/operations/CODEX_EXECUTOR_BOUNDARY.md",
    "docs/operations/operator_decisions/README.md",
    "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001.md",
    "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_002.md",
    "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_BRIEF_003_NO_SCREENSHOT_PATH_OPTION_C_INTERNAL_ONLY.md",
    "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md",
    "docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION.md",
    "docs/operations/operator_review_packets/HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md",
    "docs/operations/MVP_OPERATIONAL_START_PLAN_BATCH_01.md",
    "docs/operations/ROADMAP_AND_MILESTONES_MVP_2026.md",
    "docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md",
    "docs/operations/CONTENT_QUALITY_USER_PERSPECTIVE_READER_EXPERIENCE_AND_FEEDBACK_LOOP_BASELINE.md",
    "docs/operations/USER_FEEDBACK_INTAKE_PROTOCOL_BASELINE.md",
    "docs/content/article_quality_scorecards/README.md",
    "docs/content/article_quality_scorecards/CONTENT_QUALITY_SCORECARD_TEMPLATE_BATCH_01.md",
    "docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md",
    "docs/content/final_article_candidates/README.md",
    "docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md",
    "docs/content/BATCH_WORKFLOW_TEMPLATE.md",
    "docs/operations/NEXT_STAGE_DECISION_TREE.md",
    "docs/operations/STATUS_REGISTRY.yaml",
    "docs/content/batches/MVP_BATCH_01.yaml",
    "docs/operations/content_pipeline/README.md",
    "docs/operations/content_pipeline/CONTENT_PIPELINE_CONTRACT_V1.md",
    "docs/operations/content_pipeline/CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md",
    "docs/operations/content_pipeline/WORK_QUEUE_V1.yaml",
    "docs/operations/content_pipeline/CONTENT_PIPELINE_RUNNER_SPEC_V1.md",
    "docs/operations/content_pipeline/NEXT_TASK_GENERATOR_SPEC_V1.md",
    "docs/operations/website_preview/README.md",
    "docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
    "docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md",
    "docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md",
    "docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md",
    "docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md",
    "docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md",
    "docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md",
    "docs/operations/website_preview/STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY.md",
    "docs/operations/website_preview/STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md",
    "preview_static_internal/README.md",
    "preview_static_internal/index.html",
    "preview_static_internal/topics/index.html",
    "preview_static_internal/topics/smartphone-bedienung.html",
    "preview_static_internal/topics/whatsapp-sicherheit.html",
    "preview_static_internal/articles/brief-002-preview.html",
    "preview_static_internal/status/index.html",
    "preview_static_internal/styles.css",
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
ARTICLE_READINESS_DASHBOARD_PATH = ROOT / "docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md"
CONTENT_QUALITY_FEEDBACK_LOOP_PATH = (
    ROOT / "docs/operations/CONTENT_QUALITY_USER_PERSPECTIVE_READER_EXPERIENCE_AND_FEEDBACK_LOOP_BASELINE.md"
)
USER_FEEDBACK_INTAKE_PROTOCOL_PATH = ROOT / "docs/operations/USER_FEEDBACK_INTAKE_PROTOCOL_BASELINE.md"
ARTICLE_QUALITY_SCORECARD_TEMPLATE_PATH = (
    ROOT / "docs/content/article_quality_scorecards/CONTENT_QUALITY_SCORECARD_TEMPLATE_BATCH_01.md"
)
APPLIED_SCORECARD_BRIEF_002_PATH = (
    ROOT / "docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md"
)
HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002_PATH = (
    ROOT / "docs/operations/operator_review_packets/HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md"
)
FINAL_ARTICLE_CANDIDATES_DIR = ROOT / "docs/content/final_article_candidates"
FINAL_ARTICLE_CANDIDATE_BRIEF_002_PATH = (
    ROOT / "docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md"
)
ACCESSIBILITY_REVIEW_BRIEF_002_PATH = (
    ROOT / "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.accessibility-review.md"
)
FINAL_SOURCE_METADATA_REVIEW_BRIEF_002_PATH = (
    ROOT / "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-metadata-review.md"
)
CONTENT_PIPELINE_DIR = ROOT / "docs/operations/content_pipeline"
CONTENT_PIPELINE_CONTRACT_V1_PATH = CONTENT_PIPELINE_DIR / "CONTENT_PIPELINE_CONTRACT_V1.md"
CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1_PATH = (
    CONTENT_PIPELINE_DIR / "CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1.md"
)
WORK_QUEUE_V1_PATH = CONTENT_PIPELINE_DIR / "WORK_QUEUE_V1.yaml"
CONTENT_PIPELINE_RUNNER_SPEC_V1_PATH = (
    CONTENT_PIPELINE_DIR / "CONTENT_PIPELINE_RUNNER_SPEC_V1.md"
)
NEXT_TASK_GENERATOR_SPEC_V1_PATH = (
    CONTENT_PIPELINE_DIR / "NEXT_TASK_GENERATOR_SPEC_V1.md"
)
WEBSITE_PREVIEW_DIR = ROOT / "docs/operations/website_preview"
WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1_PATH = (
    WEBSITE_PREVIEW_DIR / "WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md"
)
WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR / "WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md"
)
STATIC_PREVIEW_SPEC_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR / "STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md"
)
VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR / "VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md"
)
ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR / "ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md"
)
ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR / "ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md"
)
STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR / "STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md"
)
STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR
    / "STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY.md"
)
STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY_PATH = (
    WEBSITE_PREVIEW_DIR / "STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY.md"
)
PREVIEW_STATIC_INTERNAL_DIR = ROOT / "preview_static_internal"
PREVIEW_STATIC_INTERNAL_FILES = [
    PREVIEW_STATIC_INTERNAL_DIR / "README.md",
    PREVIEW_STATIC_INTERNAL_DIR / "index.html",
    PREVIEW_STATIC_INTERNAL_DIR / "topics/index.html",
    PREVIEW_STATIC_INTERNAL_DIR / "topics/smartphone-bedienung.html",
    PREVIEW_STATIC_INTERNAL_DIR / "topics/whatsapp-sicherheit.html",
    PREVIEW_STATIC_INTERNAL_DIR / "articles/brief-002-preview.html",
    PREVIEW_STATIC_INTERNAL_DIR / "status/index.html",
    PREVIEW_STATIC_INTERNAL_DIR / "styles.css",
]
PREVIEW_STATIC_INTERNAL_HTML_FILES = [
    PREVIEW_STATIC_INTERNAL_DIR / "index.html",
    PREVIEW_STATIC_INTERNAL_DIR / "topics/index.html",
    PREVIEW_STATIC_INTERNAL_DIR / "topics/smartphone-bedienung.html",
    PREVIEW_STATIC_INTERNAL_DIR / "topics/whatsapp-sicherheit.html",
    PREVIEW_STATIC_INTERNAL_DIR / "articles/brief-002-preview.html",
    PREVIEW_STATIC_INTERNAL_DIR / "status/index.html",
]
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
    "HUMAN_OPERATOR_DECISION_BRIEF_003_NO_SCREENSHOT_PATH_OPTION_C_INTERNAL_ONLY.md": {
        "decision_id": "HUMAN_OPERATOR_DECISION_BRIEF_003_NO_SCREENSHOT_PATH_OPTION_C_INTERNAL_ONLY",
        "linked_brief_id": "SHO-MVP-BRIEF-003",
        "selected_option": "C",
        "selected_option_label": "pivot_to_another_screenshot_independent_work_item",
        "decision_status": "recorded",
    },
    "HUMAN_OPERATOR_DECISION_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md": {
        "operator_decision_id": "HUMAN_OPERATOR_DECISION_FINAL_ARTICLE_CANDIDATE_BRIEF_002",
        "brief_id": "SHO-MVP-BRIEF-002",
        "linked_final_article_candidate": "docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md",
        "linked_scorecard": "docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md",
        "linked_operator_review_packet": "docs/operations/operator_review_packets/HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md",
        "operator_review_outcome_status": "proceed_to_operator_review_candidate_not_publish_ready",
    },
    "HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION.md": {
        "decision_id": "HUMAN-OPERATOR-DECISION-STATIC-PREVIEW-SKELETON-IMPLEMENTATION",
        "linked_decision_packet": "docs/operations/website_preview/STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY.md",
        "linked_skeleton_spec": "docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md",
        "linked_accessibility_review_packet": "docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md",
        "linked_accessibility_requirements_spec": "docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md",
        "linked_visual_design_system_spec": "docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md",
        "linked_static_preview_spec": "docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md",
        "linked_ia_artifact": "docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "decision_status": "approved_for_later_internal_html_css_skeleton_no_js",
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
            "- docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.accessibility-review.md",
            "- docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-metadata-review.md",
            "article_draft_candidate_fixes:",
            "final_article_candidates:",
            "- docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md",
            "article_quality_scorecards:",
            "- docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md",
            "operator_review_packets:",
            "- docs/operations/operator_review_packets/HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md",
            "Brief 002 draft candidate fix re-review passed, but no publish readiness is set.",
            "Brief 002 final article candidate exists and is not publish-ready.",
            "Brief 002 final article candidate has scorecard review completed, but remains not publish-ready.",
            "Brief 002 human operator review packet prepared, but no Operator Acceptance or Publish Readiness is set.",
            "Brief 002 Human Operator decision allows internal operator review candidate continuation, but no Publish Readiness or Operator Acceptance is set.",
            "Brief 002 dedicated accessibility review completed not publish-ready; Final Source Metadata Review and later Human Operator publish gates remain required.",
            "Brief 002 final source metadata review completed not publish-ready; later Human Operator publish gates remain required.",
            "No publish-ready final article exists.",
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
        if "No article draft exists." in text or "No final article draft exists." in text:
            failures.append("Batch manifest must use 'No publish-ready final article exists.' after final candidate creation")

    if STATUS_REGISTRY_PATH.exists():
        registry_text = STATUS_REGISTRY_PATH.read_text(encoding="utf-8")
        required_status_fragments = [
            "re_review_passed",
            "re_review_passed_not_publish_ready",
            "packet_status:",
            "prepared_for_operator_review",
            "review_packet_status:",
            "prepared_for_human_operator_review_not_acceptance",
            "operator_review_outcome_status:",
            "proceed_to_operator_review_candidate_not_publish_ready",
            "publish_readiness_status:",
            "not_ready",
            "decision_status:",
            "proceed_to_source_citation_and_legal_wording_preparation",
            "proceed_to_final_article_preparation_not_publish_ready",
            "approved_for_later_internal_html_css_skeleton_no_js",
            "preview_runtime_status:",
            "static_generation_status:",
            "skeleton_runtime_status:",
            "skeleton_generation_status:",
            "design_runtime_status:",
            "asset_generation_status:",
            "html_generation_status:",
            "css_generation_status:",
            "js_generation_status:",
            "accessibility_testing_status:",
            "not_performed",
            "not_tested",
            "wcag_conformance_status:",
            "not_claimed",
            "implementation_status:",
            "implementation_decision_status:",
            "pending_human_operator_decision",
            "brief_002_rendering_decision:",
            "shell_only_no_article_body",
            "js_decision:",
            "js_forbidden_first_skeleton",
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
            "dashboard_status:",
            "internal_tracking_ready",
            "placeholder_status:",
            "pending_quality_loop_baseline",
            "pending_reader_experience_baseline",
            "pending_accessibility_standard",
            "feedback_not_collected",
            "accessibility_review_status:",
            "completed_not_publish_ready",
            "final_source_metadata_review_status:",
            "source_metadata_status:",
            "reviewed_from_existing_repo_metadata_not_live_verified",
            "loop_status:",
            "baseline_defined_not_live",
            "reader_experience_status:",
            "baseline_defined",
            "reader_experience_feedback_status:",
            "not_collected",
            "user_feedback_status:",
            "email_feedback_status:",
            "not_connected",
            "feedback_protocol_status:",
            "analytics_status:",
            "keyword_validation_status:",
            "not_available",
            "scorecard_status:",
            "template_defined_not_applied",
            "scorecard_recommendation_status:",
            "candidate_for_human_operator_review_not_publish_ready",
            "final_article_candidate_status:",
            "final_article_candidate_not_publish_ready",
            "needs_scorecard_review",
            "scorecard_review_completed_not_publish_ready",
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

    found_files = {
        path.name
        for path in ARTICLE_REVIEWS_DIR.glob("*.review.md")
        if not path.name.endswith(".accessibility-review.md")
        and not path.name.endswith(".final-source-metadata-review.md")
    }
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

        if file_name == "HUMAN_OPERATOR_DECISION_BRIEF_003_NO_SCREENSHOT_PATH_OPTION_C_INTERNAL_ONLY.md":
            required_fragments = [
                f"decision_id: {expected['decision_id']}",
                f"decision_status: {expected['decision_status']}",
                "decision_scope: brief_003_no_screenshot_path",
                f"linked_brief_id: {expected['linked_brief_id']}",
                f"selected_option: {expected['selected_option']}",
                f"selected_option_label: {expected['selected_option_label']}",
                "artifact_status: internal_only",
                "screenshot_evidence_status: not_available",
                "ui_path_status: not_validated",
                "own_capture_status: not_performed",
                "accessibility_testing_status: not_performed",
                "wcag_conformance_status: not_claimed",
                "brief_003_publish_readiness_status: not_ready",
                "operator_acceptance_status: not_accepted",
                "public_launch_status: not_ready",
                "monetization_status: not_approved",
                "analytics_status: not_connected",
                "search_console_status: not_connected",
                "user_feedback_status: not_collected",
                "stage_advancement_status: not_advanced",
                "queue_execution_status: not_live",
                "pivot_to_another_screenshot_independent_work_item",
                "pivot_to_next_screenshot_independent_work_item_only",
                "screenshot_evidence_not_available",
                "ui_paths_not_validated",
                "exact_device_specific_claims_blocked",
                "accessibility_testing_not_performed",
                "no_publish_gate",
                "no_operator_acceptance",
                "Brief 003 remains internal-only",
                "Brief 003 is not advanced to final article",
                "Brief 003 is not publish-ready",
                "no screenshot evidence exists",
                "no own screenshots were captured",
                "no external screenshots are used as evidence",
                "no generated visuals are used as evidence",
                "no exact Android / Samsung / One UI paths are validated",
                "no accessibility testing is claimed",
                "no WCAG conformance is claimed",
                "no Operator Acceptance is set",
                "no Public Launch is activated",
                "no Monetization is activated",
                "Brief 002 publish-candidate pre-gate decision packet preparation",
                "Keyword/source planning without invented metrics",
            ]
            for fragment in required_fragments:
                if fragment not in text:
                    failures.append(
                        f"Operator decision {file_name} must contain: {fragment}"
                    )

            if fields.get("decision_id") != expected["decision_id"]:
                failures.append(f"Operator decision {file_name} has unexpected decision_id")
            if normalized(fields.get("decision_status")) != expected["decision_status"]:
                failures.append(f"Operator decision {file_name} must have decision_status recorded")
            if fields.get("linked_brief_id") != expected["linked_brief_id"]:
                failures.append(f"Operator decision {file_name} must link to Brief 003")
            if normalized(fields.get("selected_option")) != expected["selected_option"].lower():
                failures.append(f"Operator decision {file_name} must select Option C")
            if normalized(fields.get("selected_option_label")) != expected["selected_option_label"]:
                failures.append(f"Operator decision {file_name} must select the Option C pivot label")
            if normalized(fields.get("screenshot_evidence_status")) != "not_available":
                failures.append(f"Operator decision {file_name} must keep screenshot evidence unavailable")
            if normalized(fields.get("ui_path_status")) != "not_validated":
                failures.append(f"Operator decision {file_name} must keep UI paths not validated")
            if normalized(fields.get("own_capture_status")) != "not_performed":
                failures.append(f"Operator decision {file_name} must keep own capture not performed")
            if normalized(fields.get("accessibility_testing_status")) != "not_performed":
                failures.append(f"Operator decision {file_name} must keep accessibility testing not performed")
            if normalized(fields.get("wcag_conformance_status")) != "not_claimed":
                failures.append(f"Operator decision {file_name} must keep WCAG conformance not claimed")
            if normalized(fields.get("brief_003_publish_readiness_status")) != "not_ready":
                failures.append(f"Operator decision {file_name} must keep Brief 003 not publish-ready")
            if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
                failures.append(f"Operator decision {file_name} must keep Operator Acceptance not accepted")
            if normalized(fields.get("public_launch_status")) != "not_ready":
                failures.append(f"Operator decision {file_name} must keep public launch not ready")
            if normalized(fields.get("monetization_status")) != "not_approved":
                failures.append(f"Operator decision {file_name} must keep monetization not approved")
            if normalized(fields.get("analytics_status")) != "not_connected":
                failures.append(f"Operator decision {file_name} must keep analytics not connected")
            if normalized(fields.get("search_console_status")) != "not_connected":
                failures.append(f"Operator decision {file_name} must keep Search Console not connected")
            if normalized(fields.get("user_feedback_status")) != "not_collected":
                failures.append(f"Operator decision {file_name} must keep user feedback not collected")
            if normalized(fields.get("stage_advancement_status")) != "not_advanced":
                failures.append(f"Operator decision {file_name} must keep stage not advanced")
            if normalized(fields.get("queue_execution_status")) != "not_live":
                failures.append(f"Operator decision {file_name} must keep queue execution not live")

            forbidden_fragments = [
                "screenshot_evidence_status: available",
                "ui_path_status: validated",
                "own_capture_status: performed",
                "accessibility_testing_status: performed",
                "wcag_conformance_status: claimed",
                "brief_003_publish_readiness_status: ready",
                "operator_acceptance_status: accepted",
                "public_launch_status: ready",
                "monetization_status: approved",
                "analytics_status: connected",
                "search_console_status: connected",
                "user_feedback_status: collected",
                "stage_advancement_status: advanced",
                "queue_execution_status: live",
            ]
            lower_text = text.lower()
            for fragment in forbidden_fragments:
                if fragment in lower_text:
                    failures.append(
                        f"Operator decision {file_name} must not contain active forbidden marker: {fragment}"
                    )
            continue

        if file_name == "HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION.md":
            required_fragments = [
                f"decision_id: {expected['decision_id']}",
                f"linked_decision_packet: {expected['linked_decision_packet']}",
                f"linked_skeleton_spec: {expected['linked_skeleton_spec']}",
                f"linked_accessibility_review_packet: {expected['linked_accessibility_review_packet']}",
                f"linked_accessibility_requirements_spec: {expected['linked_accessibility_requirements_spec']}",
                f"linked_visual_design_system_spec: {expected['linked_visual_design_system_spec']}",
                f"linked_static_preview_spec: {expected['linked_static_preview_spec']}",
                f"linked_ia_artifact: {expected['linked_ia_artifact']}",
                "scope: MVP_BATCH_01",
                f"decision_status: {expected['decision_status']}",
                "implementation_decision_status: approved_for_later_internal_html_css_skeleton_no_js",
                "implementation_status: not_implemented",
                "skeleton_runtime_status: not_implemented",
                "skeleton_generation_status: not_implemented",
                "preview_runtime_status: not_implemented",
                "static_generation_status: not_implemented",
                "html_generation_status: not_implemented",
                "css_generation_status: not_implemented",
                "js_generation_status: not_implemented",
                "asset_generation_status: not_implemented",
                "brief_002_rendering_decision: shell_only_no_article_body",
                "js_decision: js_forbidden_first_skeleton",
                "accessibility_testing_status: not_performed",
                "wcag_conformance_status: not_claimed",
                "public_launch_status: not_ready",
                "publish_readiness_status: not_ready",
                "operator_acceptance_status: not_accepted",
                "monetization_status: not_approved",
                "analytics_status: not_connected",
                "search_console_status: not_connected",
                "user_feedback_status: not_collected",
                "## Purpose",
                "## Decision Summary",
                "## Explicit Non-Acceptance",
                "## Approved Later Implementation Scope",
                "## Mandatory Later Implementation Constraints",
                "## Required Follow-Up",
                "## Risk Acceptance Boundary",
                "## Forbidden Outcomes",
                "## Recommended Next Step",
                "approve_internal_html_css_skeleton_no_js",
                "shell_only_no_article_body",
                "js_forbidden_first_skeleton",
                "top_and_footer_on_every_page",
                "preview_static_internal/",
                "STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY",
                "This decision is not implementation.",
                "This decision does not approve JS.",
                "This decision does not approve full Brief 002 article body rendering.",
                "not unlock SHO-CLAIM-007",
                "not include WhatsApp block/report UI instructions",
                "no implementation performed",
                "no HTML/CSS/JS files created by this patch",
                "no new article text",
                "no new claims",
                "no new sources",
                "no WhatsApp block/report UI instructions",
            ]
            for fragment in required_fragments:
                if fragment not in text:
                    failures.append(
                        f"Operator decision {file_name} must contain: {fragment}"
                    )

            if fields.get("decision_id") != expected["decision_id"]:
                failures.append(f"Operator decision {file_name} has unexpected ID")
            if fields.get("linked_decision_packet") != expected["linked_decision_packet"]:
                failures.append(f"Operator decision {file_name} must link to decision packet")
            if fields.get("linked_skeleton_spec") != expected["linked_skeleton_spec"]:
                failures.append(f"Operator decision {file_name} must link to skeleton spec")
            if (
                fields.get("linked_accessibility_review_packet")
                != expected["linked_accessibility_review_packet"]
            ):
                failures.append(
                    f"Operator decision {file_name} must link to accessibility review packet"
                )
            if (
                fields.get("linked_accessibility_requirements_spec")
                != expected["linked_accessibility_requirements_spec"]
            ):
                failures.append(
                    f"Operator decision {file_name} must link to accessibility requirements spec"
                )
            if (
                fields.get("linked_visual_design_system_spec")
                != expected["linked_visual_design_system_spec"]
            ):
                failures.append(
                    f"Operator decision {file_name} must link to visual design system spec"
                )
            if fields.get("linked_static_preview_spec") != expected["linked_static_preview_spec"]:
                failures.append(f"Operator decision {file_name} must link to static preview spec")
            if fields.get("linked_ia_artifact") != expected["linked_ia_artifact"]:
                failures.append(f"Operator decision {file_name} must link to IA artifact")
            if normalized(fields.get("decision_status")) != expected["decision_status"]:
                failures.append(f"Operator decision {file_name} must have expected decision_status")
            if (
                normalized(fields.get("implementation_decision_status"))
                != "approved_for_later_internal_html_css_skeleton_no_js"
            ):
                failures.append(
                    f"Operator decision {file_name} must have expected implementation_decision_status"
                )
            if normalized(fields.get("implementation_status")) != "not_implemented":
                failures.append(f"Operator decision {file_name} must keep implementation_status not_implemented")
            if normalized(fields.get("js_decision")) != "js_forbidden_first_skeleton":
                failures.append(f"Operator decision {file_name} must forbid JS for first skeleton")
            if (
                normalized(fields.get("brief_002_rendering_decision"))
                != "shell_only_no_article_body"
            ):
                failures.append(f"Operator decision {file_name} must keep Brief 002 shell-only")
            if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
                failures.append(f"Operator decision {file_name} must keep operator_acceptance_status not_accepted")
            if normalized(fields.get("publish_readiness_status")) != "not_ready":
                failures.append(f"Operator decision {file_name} must keep publish_readiness_status not_ready")
            if normalized(fields.get("public_launch_status")) != "not_ready":
                failures.append(f"Operator decision {file_name} must keep public_launch_status not_ready")
            if normalized(fields.get("monetization_status")) != "not_approved":
                failures.append(f"Operator decision {file_name} must keep monetization_status not_approved")
            if normalized(fields.get("analytics_status")) != "not_connected":
                failures.append(f"Operator decision {file_name} must keep analytics_status not_connected")
            if normalized(fields.get("search_console_status")) != "not_connected":
                failures.append(f"Operator decision {file_name} must keep search_console_status not_connected")
            if normalized(fields.get("user_feedback_status")) != "not_collected":
                failures.append(f"Operator decision {file_name} must keep user_feedback_status not_collected")

            forbidden_fragments = [
                "implementation_status: implemented",
                "skeleton_runtime_status: implemented",
                "skeleton_generation_status: implemented",
                "html_generation_status: implemented",
                "css_generation_status: implemented",
                "js_generation_status: implemented",
                "asset_generation_status: implemented",
                "js_decision: js_allowed",
                "brief_002_rendering_decision: full_internal_candidate_text_with_not_publish_ready_banner",
                "accessibility_testing_status: performed",
                "wcag_conformance_status: claimed",
                "wcag_conformance_status: compliant",
                "public_launch_status: ready",
                "public_launch_status: launched",
                "publish_readiness_status: publish_candidate",
                "publish_readiness_status: approved_for_publish",
                "operator_acceptance_status: accepted",
                "monetization_status: approved",
                "analytics_status: connected",
                "search_console_status: connected",
                "user_feedback_status: collected",
                "public_launch_ready: true",
                "publish_ready: true",
            ]
            lower_text = text.lower()
            for fragment in forbidden_fragments:
                if fragment in lower_text:
                    failures.append(
                        f"Operator decision {file_name} must not contain active forbidden marker: {fragment}"
                    )
            continue

        required_fragments = [
            f"operator_decision_id: {expected['operator_decision_id']}",
            "batch_id: MVP_BATCH_01",
            f"linked_brief_id: {expected['brief_id']}",
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
                    f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
                    f"decision_status: {expected['decision_status']}",
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
        elif file_name == "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_002.md":
            required_fragments.extend(
                [
                    f"linked_article_draft_candidate: {expected['linked_article_draft_candidate']}",
                    f"decision_status: {expected['decision_status']}",
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
        else:
            required_fragments.extend(
                [
                    f"linked_final_article_candidate: {expected['linked_final_article_candidate']}",
                    f"linked_scorecard: {expected['linked_scorecard']}",
                    f"linked_operator_review_packet: {expected['linked_operator_review_packet']}",
                    f"operator_review_outcome_status: {expected['operator_review_outcome_status']}",
                    "Human Operator erlaubt, den Final Article Candidate fuer `SHO-MVP-BRIEF-002` als naechsten internen Review-Kandidaten weiterzufuehren.",
                    "Diese Entscheidung erlaubt nur den naechsten internen Review-Schritt.",
                    "Diese Entscheidung ist keine Veroeffentlichungsgenehmigung.",
                    "Diese Entscheidung ist keine Monetarisierungsfreigabe.",
                    "Diese Entscheidung fuegt keine neuen Claims hinzu.",
                    "Diese Entscheidung fuegt keine neuen Sources hinzu.",
                    "Diese Entscheidung erfindet keine Source-Metadaten.",
                    "continue Final Article Candidate as internal operator review candidate",
                    "prepare Dedicated Accessibility Review before any publish-candidate step",
                    "prepare Final Source Metadata Review before any publish-candidate step",
                    "preserve allowed claims SHO-CLAIM-004, SHO-CLAIM-005, SHO-CLAIM-006",
                    "preserve allowed sources SHO-SRC-005, SHO-SRC-006, SHO-SRC-007",
                    "preserve blocked state for SHO-CLAIM-007",
                    "Dedicated Accessibility Review before any publish-candidate step.",
                    "Final Source Metadata Review before any publish-candidate step.",
                    "Later explicit Human Operator decision before any publish-candidate status.",
                    "Later explicit Human Operator decision before any Operator Acceptance.",
                    "Later explicit Human Operator decision before public launch or monetization.",
                    "public_launch_status: not_ready",
                    "monetization_status: not_approved",
                    "legal_approval_status: not_approved",
                    "publish_ready",
                    "monetization_approved",
                    "legal_approval_status: approved",
                    "invent source metadata",
                    "invent SEO, analytics, ranking, traffic, feedback, conversion or revenue data",
                ]
            )
        for fragment in required_fragments:
            if fragment not in text:
                failures.append(f"Operator decision {file_name} must contain: {fragment}")

        if fields.get("operator_decision_id") != expected["operator_decision_id"]:
            failures.append(f"Operator decision {file_name} has unexpected ID")
        if fields.get("linked_brief_id") != expected["brief_id"]:
            failures.append(f"Operator decision {file_name} must link to Brief 002")
        if file_name == "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_001.md":
            if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
                failures.append(f"Operator decision {file_name} must link to expected draft candidate")
            if fields.get("linked_operator_review_packet") != expected["linked_operator_review_packet"]:
                failures.append(f"Operator decision {file_name} must link to operator review packet")
            if fields.get("linked_legal_source_citation_review") != expected["linked_legal_source_citation_review"]:
                failures.append(f"Operator decision {file_name} must link to legal/source citation review")
        elif file_name == "HUMAN_OPERATOR_DECISION_BATCH01_BRIEF002_002.md":
            if fields.get("linked_article_draft_candidate") != expected["linked_article_draft_candidate"]:
                failures.append(f"Operator decision {file_name} must link to expected draft candidate")
            if fields.get("linked_final_source_list_review") != expected["linked_final_source_list_review"]:
                failures.append(f"Operator decision {file_name} must link to final source list review")
            if fields.get("linked_final_legal_wording_review") != expected["linked_final_legal_wording_review"]:
                failures.append(f"Operator decision {file_name} must link to final legal wording review")
            if fields.get("linked_final_article_prep_gate_review") != expected["linked_final_article_prep_gate_review"]:
                failures.append(f"Operator decision {file_name} must link to final article prep gate review")
        else:
            if fields.get("linked_final_article_candidate") != expected["linked_final_article_candidate"]:
                failures.append(f"Operator decision {file_name} must link to final article candidate")
            if fields.get("linked_scorecard") != expected["linked_scorecard"]:
                failures.append(f"Operator decision {file_name} must link to applied scorecard")
            if fields.get("linked_operator_review_packet") != expected["linked_operator_review_packet"]:
                failures.append(f"Operator decision {file_name} must link to Human Operator review packet")
            if normalized(fields.get("operator_review_outcome_status")) != expected["operator_review_outcome_status"]:
                failures.append(f"Operator decision {file_name} must have the expected operator_review_outcome_status")
            if normalized(fields.get("public_launch_status")) != "not_ready":
                failures.append(f"Operator decision {file_name} must have public_launch_status: not_ready")
            if normalized(fields.get("monetization_status")) != "not_approved":
                failures.append(f"Operator decision {file_name} must have monetization_status: not_approved")
            if normalized(fields.get("legal_approval_status")) != "not_approved":
                failures.append(f"Operator decision {file_name} must have legal_approval_status: not_approved")
        if "decision_status" in expected and normalized(fields.get("decision_status")) != expected["decision_status"]:
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


def validate_accessibility_review_brief_002(failures: list[str]) -> int:
    if not ACCESSIBILITY_REVIEW_BRIEF_002_PATH.exists():
        failures.append(
            "Missing dedicated accessibility review for Brief 002: "
            "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.accessibility-review.md"
        )
        return 0

    text = ACCESSIBILITY_REVIEW_BRIEF_002_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_frontmatter_fragments = [
        "accessibility_review_id: SHO-ACCESSIBILITY-REVIEW-BATCH01-BRIEF002",
        "batch_id: MVP_BATCH_01",
        "linked_brief_id: SHO-MVP-BRIEF-002",
        "linked_final_article_candidate: docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md",
        "linked_scorecard: docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md",
        "linked_operator_decision: docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md",
        "accessibility_review_status: completed_not_publish_ready",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
        "monetization_status: not_approved",
        "legal_approval_status: not_approved",
        "blocked_claims: SHO-CLAIM-007",
        "batch_stage_after_review: claim_slots_mapped",
    ]
    required_sections = [
        "Dedicated Accessibility Review: Betrugsnachrichten auf WhatsApp erkennen",
        "Purpose",
        "Reviewed Artifact",
        "Explicit Non-Acceptance",
        "Accessibility Criteria",
        "Findings",
        "Accessibility Review Outcome",
        "Remaining Limitations",
        "Required Follow-Up",
        "Guardrails Confirmed",
    ]
    required_criteria = [
        "Reading structure",
        "Plain-language quality",
        "Cognitive accessibility",
        "Mobile readability",
        "Print / forward usefulness",
        "Safety accessibility",
        "Screen-reader validation",
        "WCAG compliance",
        "criterion",
        "result",
        "note",
        "required_follow_up",
        "PASS",
        "PASS_WITH_REVIEW_NEEDED",
        "NEEDS_REVIEW",
        "NOT_TESTED",
        "BLOCKED",
    ]
    required_findings = [
        "finding_id",
        "category",
        "severity",
        "status",
        "summary",
        "required_action",
        "SHO-ACCESS-002-STRUCT-001",
        "SHO-ACCESS-002-PLAIN-001",
        "SHO-ACCESS-002-COG-001",
        "SHO-ACCESS-002-MOBILE-001",
        "SHO-ACCESS-002-PRINT-001",
        "SHO-ACCESS-002-TEST-001",
        "SHO-ACCESS-002-SR-001",
        "SHO-ACCESS-002-SRC-001",
        "SHO-ACCESS-002-PUB-001",
        "No real senior user accessibility test was performed.",
        "No screen-reader/device/browser validation was performed.",
        "Final Source Metadata Review remains separate and required.",
        "Publish Readiness remains blocked.",
    ]
    required_non_acceptance = [
        "This review is not Operator Acceptance.",
        "This review is not Publish Readiness.",
        "This review is not public launch approval.",
        "This review is not monetization approval.",
        "This review is not legal approval.",
        "This review does not unlock SHO-CLAIM-007.",
        "This review does not approve WhatsApp block/report UI instructions.",
        "This review does not invent user feedback, analytics, SEO or accessibility test data.",
        "Diese Review ist kein WCAG compliance claim.",
    ]
    required_limitations_and_follow_up = [
        "no real user testing performed",
        "no analytics or feedback data used",
        "no screen-reader test performed",
        "no device/browser testing performed",
        "no WCAG compliance claim",
        "Final Source Metadata Review before any publish-candidate step.",
        "Later Human Operator decision before any publish-candidate status.",
        "Later Human Operator decision before Operator Acceptance.",
        "Optional later real-reader/senior UX review.",
        "Optional later mobile/print rendering review.",
        "Optional later screen-reader/browser/device validation.",
    ]
    required_guardrails = [
        "current_stage remains claim_slots_mapped.",
        "operator_acceptance_status remains not_accepted.",
        "publish_readiness_status remains not_ready.",
        "public_launch_status remains not_ready.",
        "monetization_status remains not_approved.",
        "legal_approval_status remains not_approved.",
        "SHO-CLAIM-007 remains blocked.",
        "WhatsApp block/report UI instructions remain forbidden.",
        "No new claims added.",
        "No new sources added.",
        "No source metadata invented.",
        "No SEO, analytics, feedback, traffic, ranking, conversion or revenue data invented.",
    ]
    for fragment in (
        required_frontmatter_fragments
        + required_sections
        + required_criteria
        + required_findings
        + required_non_acceptance
        + required_limitations_and_follow_up
        + required_guardrails
    ):
        if fragment not in text:
            failures.append(f"Accessibility review Brief 002 must contain: {fragment}")

    if fields.get("accessibility_review_id") != "SHO-ACCESSIBILITY-REVIEW-BATCH01-BRIEF002":
        failures.append("Accessibility review Brief 002 has unexpected accessibility_review_id")
    if fields.get("linked_brief_id") != "SHO-MVP-BRIEF-002":
        failures.append("Accessibility review Brief 002 must link to Brief 002")
    if normalized(fields.get("accessibility_review_status")) != "completed_not_publish_ready":
        failures.append("Accessibility review Brief 002 must have accessibility_review_status: completed_not_publish_ready")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Accessibility review Brief 002 must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Accessibility review Brief 002 must have publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Accessibility review Brief 002 must have public_launch_status: not_ready")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Accessibility review Brief 002 must have monetization_status: not_approved")
    if normalized(fields.get("legal_approval_status")) != "not_approved":
        failures.append("Accessibility review Brief 002 must have legal_approval_status: not_approved")
    if normalized(fields.get("batch_stage_after_review")) != "claim_slots_mapped":
        failures.append("Accessibility review Brief 002 must keep batch_stage_after_review: claim_slots_mapped")

    batch_text = BATCH_MANIFEST_PATH.read_text(encoding="utf-8")
    if "- docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.accessibility-review.md" not in batch_text:
        failures.append("Batch manifest must link dedicated accessibility review Brief 002")
    if "Brief 002 dedicated accessibility review completed not publish-ready; Final Source Metadata Review and later Human Operator publish gates remain required." not in batch_text:
        failures.append("Batch manifest must carry accessibility review not-publish-ready blocker")

    dashboard_text = ARTICLE_READINESS_DASHBOARD_PATH.read_text(encoding="utf-8")
    if "dedicated accessibility review completed not publish-ready" not in dashboard_text:
        failures.append("Article readiness dashboard must mention dedicated accessibility review completed not publish-ready")
    if "accessibility_status: completed_not_publish_ready" not in dashboard_text:
        failures.append("Article readiness dashboard must show accessibility_status: completed_not_publish_ready for Brief 002")
    if "later Human Operator publish gates remain required" not in dashboard_text:
        failures.append("Article readiness dashboard must keep later Human Operator publish gates required")

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
        "public_launch_status: ready",
        "public_launch_status: launched",
        "monetization_status: approved",
        "accessibility_review_status: approved_for_publish",
        "accessibility_review_status: publish_ready",
        "operator_accepted",
        "wcag_compliance: true",
    ]
    lower_text = text.lower()
    for fragment in forbidden_assignments:
        if fragment in lower_text:
            failures.append(f"Accessibility review Brief 002 must not contain forbidden assignment: {fragment}")

    return 1


def validate_final_source_metadata_review_brief_002(failures: list[str]) -> int:
    if not FINAL_SOURCE_METADATA_REVIEW_BRIEF_002_PATH.exists():
        failures.append(
            "Missing final source metadata review for Brief 002: "
            "docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-metadata-review.md"
        )
        return 0

    text = FINAL_SOURCE_METADATA_REVIEW_BRIEF_002_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_frontmatter_fragments = [
        "final_source_metadata_review_id: SHO-FINAL-SOURCE-METADATA-REVIEW-BATCH01-BRIEF002",
        "batch_id: MVP_BATCH_01",
        "linked_brief_id: SHO-MVP-BRIEF-002",
        "linked_final_article_candidate: docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md",
        "linked_source_pack: docs/content/source_packs/operator-research-source-pack-batch-01.md",
        "linked_final_source_list_review: docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-list-review.md",
        "linked_accessibility_review: docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.accessibility-review.md",
        "linked_operator_decision: docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md",
        "final_source_metadata_review_status: completed_not_publish_ready",
        "source_metadata_status: reviewed_from_existing_repo_metadata_not_live_verified",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
        "monetization_status: not_approved",
        "legal_approval_status: not_approved",
        "blocked_claims: SHO-CLAIM-007",
        "batch_stage_after_review: claim_slots_mapped",
    ]
    required_sections = [
        "Final Source Metadata Review: Betrugsnachrichten auf WhatsApp erkennen",
        "Purpose",
        "Reviewed Artifacts",
        "Explicit Non-Acceptance",
        "Source Metadata Scope",
        "Source Metadata Review Table",
        "Claim/Source Boundary Check",
        "Findings",
        "Source Metadata Review Outcome",
        "Required Follow-Up",
        "Guardrails Confirmed",
    ]
    required_scope_and_status = [
        "SHO-SRC-005",
        "SHO-SRC-006",
        "SHO-SRC-007",
        "SHO-SRC-001",
        "SHO-SRC-002",
        "SHO-SRC-003",
        "SHO-SRC-004",
        "SHO-SRC-013",
        "SHO-CLAIM-007",
        "live_source_verification_status: not_performed",
        "citation_metadata_finality: reviewed_from_repo_metadata_not_publication_final",
        "PASS_REPO_METADATA_PRESENT_NOT_LIVE_VERIFIED",
        "publication_ready",
        "Existing repo metadata present.",
        "reviewed_from_existing_repo_metadata_not_live_verified",
    ]
    required_table_fields = [
        "source_id",
        "linked_brief_id",
        "source_type",
        "title_or_provider",
        "url",
        "retrieved_at",
        "verification_status",
        "source_status_after",
        "linked_claims",
        "metadata_review_result",
        "publication_ready",
        "notes",
        "| SHO-SRC-005 | SHO-MVP-BRIEF-002 | official_authority |",
        "| SHO-SRC-006 | SHO-MVP-BRIEF-002 | official_authority |",
        "| SHO-SRC-007 | SHO-MVP-BRIEF-002 | consumer_protection |",
    ]
    required_non_acceptance = [
        "This review is not Operator Acceptance.",
        "This review is not Publish Readiness.",
        "This review is not public launch approval.",
        "This review is not monetization approval.",
        "This review is not legal approval.",
        "This review does not unlock SHO-CLAIM-007.",
        "This review does not approve WhatsApp block/report UI instructions.",
        "This review does not add new sources.",
        "This review does not add new claims.",
        "This review does not invent source metadata.",
        "This review does not claim live source verification unless actually performed.",
    ]
    required_claim_boundary = [
        "SHO-CLAIM-004 only uses allowed sources already mapped for Brief 002: SHO-SRC-005; SHO-SRC-006.",
        "SHO-CLAIM-005 only uses allowed sources already mapped for Brief 002: SHO-SRC-005; SHO-SRC-006.",
        "SHO-CLAIM-006 only uses allowed sources already mapped for Brief 002: SHO-SRC-007.",
        "SHO-CLAIM-007 remains blocked.",
        "No WhatsApp block/report UI instructions are approved.",
        "No new source IDs introduced.",
        "No new claims introduced.",
        "No source metadata invented.",
    ]
    required_findings = [
        "finding_id",
        "category",
        "severity",
        "status",
        "summary",
        "required_action",
        "SHO-SRCMETA-002-META-001",
        "SHO-SRCMETA-002-LIVE-001",
        "SHO-SRCMETA-002-CITE-001",
        "SHO-SRCMETA-002-CLAIM-001",
        "SHO-SRCMETA-002-BLOCK-001",
        "SHO-SRCMETA-002-PUB-001",
        "Existing repo metadata exists for SHO-SRC-005, SHO-SRC-006, SHO-SRC-007.",
        "Live source verification was not performed.",
        "Citation metadata is reviewed from repo metadata but not public-publication-final.",
        "Publish Readiness remains blocked.",
        "Later explicit Human Operator decision remains required before any publish-candidate status.",
    ]
    required_follow_up_and_guardrails = [
        "Later Human Operator decision before any publish-candidate status.",
        "Later Human Operator decision before Operator Acceptance.",
        "No public launch without explicit later Human Operator decision.",
        "No monetization without explicit later Human Operator decision.",
        "Optional live source re-check before publication if repo policy requires freshness validation.",
        "Optional final citation-format review once publication surface/layout exists.",
        "current_stage remains claim_slots_mapped.",
        "operator_acceptance_status remains not_accepted.",
        "publish_readiness_status remains not_ready.",
        "public_launch_status remains not_ready.",
        "monetization_status remains not_approved.",
        "legal_approval_status remains not_approved.",
        "WhatsApp block/report UI instructions remain forbidden.",
        "No new claims added.",
        "No new sources added.",
        "No source metadata invented.",
        "No SEO, analytics, feedback, traffic, ranking, conversion or revenue data invented.",
    ]
    for fragment in (
        required_frontmatter_fragments
        + required_sections
        + required_scope_and_status
        + required_table_fields
        + required_non_acceptance
        + required_claim_boundary
        + required_findings
        + required_follow_up_and_guardrails
    ):
        if fragment not in text:
            failures.append(f"Final source metadata review Brief 002 must contain: {fragment}")

    if fields.get("final_source_metadata_review_id") != "SHO-FINAL-SOURCE-METADATA-REVIEW-BATCH01-BRIEF002":
        failures.append("Final source metadata review Brief 002 has unexpected final_source_metadata_review_id")
    if fields.get("linked_brief_id") != "SHO-MVP-BRIEF-002":
        failures.append("Final source metadata review Brief 002 must link to Brief 002")
    if normalized(fields.get("final_source_metadata_review_status")) != "completed_not_publish_ready":
        failures.append(
            "Final source metadata review Brief 002 must have final_source_metadata_review_status: "
            "completed_not_publish_ready"
        )
    if normalized(fields.get("source_metadata_status")) != "reviewed_from_existing_repo_metadata_not_live_verified":
        failures.append(
            "Final source metadata review Brief 002 must have source_metadata_status: "
            "reviewed_from_existing_repo_metadata_not_live_verified"
        )
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Final source metadata review Brief 002 must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Final source metadata review Brief 002 must have publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Final source metadata review Brief 002 must have public_launch_status: not_ready")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Final source metadata review Brief 002 must have monetization_status: not_approved")
    if normalized(fields.get("legal_approval_status")) != "not_approved":
        failures.append("Final source metadata review Brief 002 must have legal_approval_status: not_approved")
    if normalized(fields.get("batch_stage_after_review")) != "claim_slots_mapped":
        failures.append("Final source metadata review Brief 002 must keep batch_stage_after_review: claim_slots_mapped")

    batch_text = BATCH_MANIFEST_PATH.read_text(encoding="utf-8")
    if "- docs/content/article_reviews/betrugsnachrichten-auf-whatsapp-erkennen.final-source-metadata-review.md" not in batch_text:
        failures.append("Batch manifest must link final source metadata review Brief 002")
    if "Brief 002 final source metadata review completed not publish-ready; later Human Operator publish gates remain required." not in batch_text:
        failures.append("Batch manifest must carry final source metadata review not-publish-ready blocker")

    dashboard_text = ARTICLE_READINESS_DASHBOARD_PATH.read_text(encoding="utf-8")
    if "final source metadata review completed not publish-ready" not in dashboard_text:
        failures.append("Article readiness dashboard must mention final source metadata review completed not publish-ready")
    if "source metadata reviewed from existing repo metadata not live verified" not in dashboard_text:
        failures.append("Article readiness dashboard must mention source metadata reviewed from existing repo metadata not live verified")
    if "User-Perspective-, Reader-Experience- und Feedback-Status bleiben Platzhalter." not in dashboard_text:
        failures.append("Article readiness dashboard must preserve user/reader/feedback placeholder wording")
    if "Brief 002 Accessibility Review ist completed_not_publish_ready" not in dashboard_text:
        failures.append("Article readiness dashboard must distinguish Brief 002 accessibility completion from placeholders")

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
        "public_launch_status: ready",
        "public_launch_status: launched",
        "monetization_status: approved",
        "final_source_metadata_review_status: approved_for_publish",
        "final_source_metadata_review_status: publish_ready",
        "source_metadata_status: publication_final",
        "live_source_verification_status: performed",
        "citation_metadata_finality: publication_final",
        "operator_accepted",
        "wcag_compliance: true",
    ]
    lower_text = text.lower()
    for fragment in forbidden_assignments:
        if fragment in lower_text:
            failures.append(f"Final source metadata review Brief 002 must not contain forbidden assignment: {fragment}")

    return 1


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


def validate_article_readiness_dashboard(failures: list[str]) -> int:
    if not ARTICLE_READINESS_DASHBOARD_PATH.exists():
        failures.append("Missing article readiness dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md")
        return 0

    text = ARTICLE_READINESS_DASHBOARD_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_fragments = [
        "readiness_dashboard_id: SHO-ARTICLE-READINESS-DASHBOARD-BATCH01",
        "batch_id: MVP_BATCH_01",
        "dashboard_status: internal_tracking_ready",
        "roadmap_status: baseline_defined",
        "operational_status: internal_operations_ready",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "monetization_status: not_approved",
        "operator_acceptance_status: not_accepted",
        "Purpose",
        "Current Batch Baseline",
        "Executive Summary",
        "Article Readiness Table",
        "Brief-Level Status Details",
        "Allowed Next Work",
        "Blocked Work",
        "Quality Review Placeholders",
        "User Perspective and Reader Experience Placeholders",
        "Feedback/Analytics Placeholders",
        "Required Human Decisions",
        "Explicit Non-Acceptance",
        "brief_id",
        "slug_or_title",
        "current_artifact_level",
        "current_stage_effect",
        "allowed_next_step",
        "allowed_claims",
        "blocked_claims",
        "source_state",
        "review_state",
        "user_perspective_status",
        "reader_experience_status",
        "accessibility_status",
        "feedback_status",
        "publish_readiness",
        "operator_acceptance",
        "primary_blockers",
        "SHO-MVP-BRIEF-001",
        "SHO-MVP-BRIEF-002",
        "SHO-MVP-BRIEF-003",
        "SHO-MVP-BRIEF-004",
        "blocked_before_draft",
        "WhatsApp line evidence/manual review only",
        "WhatsApp line-level evidence unavailable",
        "WhatsApp platform sources remain candidate / needs_manual_review",
        "WhatsApp UI-sensitive instructions remain blocked",
        "final_article_candidate_prepared_not_publish_ready",
        "later Human Operator publish-candidate decision packet or another explicitly chosen internal gate",
        "SHO-CLAIM-004",
        "SHO-CLAIM-005",
        "SHO-CLAIM-006",
        "SHO-CLAIM-007",
        "SHO-SRC-005",
        "SHO-SRC-006",
        "SHO-SRC-007",
        "final article candidate exists",
        "scorecard review completed not publish-ready",
        "dedicated accessibility review completed not publish-ready",
        "final source metadata review completed not publish-ready",
        "draft candidate exists",
        "re-review passed not publish-ready",
        "final source list review exists",
        "final legal wording review exists",
        "operator decision allowed final article preparation only",
        "draft_scaffold_only",
        "article draft candidate preparation only if existing claim/source boundaries are preserved",
        "screenshot/device-version validation remains open",
        "no text candidate yet",
        "held_for_methodology",
        "product/monetization methodology review before article drafting",
        "commercial/affiliate risk",
        "product recommendation methodology open",
        "no monetization approval",
        "pending_quality_loop_baseline",
        "pending_reader_experience_baseline",
        "pending_accessibility_standard",
        "completed_not_publish_ready",
        "feedback_not_collected",
        "Einfache Sprache bedeutet nicht anspruchslose Sprache. Inhalte sollen klar, freundlich und zugänglich sein, aber ältere Leserinnen und Leser als erwachsene, erfahrene und interessierte Menschen ernst nehmen.",
        "CONTENT_QUALITY_USER_PERSPECTIVE_READER_EXPERIENCE_AND_FEEDBACK_LOOP_BASELINE",
        "CONTENT_QUALITY_SCORECARD_TEMPLATE_BATCH_01",
        "FINAL_ARTICLE_CANDIDATE_BRIEF_002",
        "BRIEF_003_ARTICLE_DRAFT_CANDIDATE",
        "WEBSITE_INFORMATION_ARCHITECTURE_MVP",
        "KEYWORD_VALIDATION_FRAMEWORK_BATCH_01",
        "public launch",
        "monetization",
        "affiliate",
        "final publication",
        "Operator Acceptance",
        "approved_for_publish",
        "publish_candidate",
        "WhatsApp block/report UI instructions",
        "unlocking SHO-CLAIM-007",
        "invented SEO/keyword/user-feedback metrics",
        "product recommendations without methodology",
        "This dashboard is internal tracking only.",
        "Dieses Dashboard aktiviert keinen Public Launch.",
        "Dieses Dashboard setzt keine Publish Readiness.",
        "Dieses Dashboard genehmigt keine Monetarisierung.",
        "Dieses Dashboard erstellt keine Operator Acceptance.",
        "User-Perspective-, Reader-Experience- und Feedback-Status bleiben Platzhalter.",
        "Brief 002 Accessibility Review ist completed_not_publish_ready; andere Accessibility-Status bleiben pending, sofern nicht separat geprueft.",
        "Dieses Dashboard schliesst User-Perspective-, Reader-Experience- oder Feedback-Reviews nicht ab; Brief 002 Accessibility Review ist completed_not_publish_ready und nicht publish-ready.",
    ]
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(f"Article readiness dashboard must contain: {fragment}")

    if fields.get("readiness_dashboard_id") != "SHO-ARTICLE-READINESS-DASHBOARD-BATCH01":
        failures.append("Article readiness dashboard has unexpected readiness_dashboard_id")
    if normalized(fields.get("batch_id")) != "mvp_batch_01":
        failures.append("Article readiness dashboard must have batch_id: MVP_BATCH_01")
    if normalized(fields.get("dashboard_status")) != "internal_tracking_ready":
        failures.append("Article readiness dashboard must have dashboard_status: internal_tracking_ready")
    if normalized(fields.get("roadmap_status")) != "baseline_defined":
        failures.append("Article readiness dashboard must have roadmap_status: baseline_defined")
    if normalized(fields.get("operational_status")) != "internal_operations_ready":
        failures.append("Article readiness dashboard must have operational_status: internal_operations_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Article readiness dashboard must have public_launch_status: not_ready")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Article readiness dashboard must have publish_readiness_status: not_ready")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Article readiness dashboard must have monetization_status: not_approved")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Article readiness dashboard must have operator_acceptance_status: not_accepted")

    row_count = sum(1 for line in text.splitlines() if line.startswith("| SHO-MVP-BRIEF-"))
    if row_count != 4:
        failures.append(f"Article readiness dashboard must contain exactly 4 Batch 01 table rows; found {row_count}")

    forbidden_assignments = [
        "public_launch_status: ready",
        "public_launch_status: launched",
        "publish_readiness_status: approved_for_publish",
        "operator_acceptance_status: accepted",
        "monetization_status: approved",
        "article_status: publish_candidate",
        "review_status: approved_for_publish",
        "dashboard_status: accepted",
        "dashboard_status: approved_for_publish",
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
            failures.append(f"Article readiness dashboard must not contain forbidden activation marker: {fragment}")

    return 1


def validate_content_quality_feedback_loop_baseline(failures: list[str]) -> int:
    if not CONTENT_QUALITY_FEEDBACK_LOOP_PATH.exists():
        failures.append(
            "Missing content quality feedback loop baseline: "
            "docs/operations/CONTENT_QUALITY_USER_PERSPECTIVE_READER_EXPERIENCE_AND_FEEDBACK_LOOP_BASELINE.md"
        )
        return 0

    text = CONTENT_QUALITY_FEEDBACK_LOOP_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_fragments = [
        "quality_loop_id: SHO-CONTENT-QUALITY-USER-PERSPECTIVE-READER-EXPERIENCE-FEEDBACK-LOOP-BASELINE",
        "scope: MVP_BATCH_01",
        "loop_status: baseline_defined_not_live",
        "reader_experience_status: baseline_defined",
        "user_feedback_status: not_collected",
        "email_feedback_status: not_connected",
        "analytics_status: not_connected",
        "keyword_validation_status: not_available",
        "monetization_status: not_approved",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
        "Purpose",
        "Current System Baseline",
        "Explicit Non-Acceptance",
        "Quality Dimensions",
        "User Perspective Dimensions",
        "Reader Experience Dimensions",
        "Target User Perspective Standard",
        "Caregiver Perspective Standard",
        "Real-World Situation Fit",
        "Reader Experience Standard",
        "Feedback Inputs Planned Later",
        "Email Feedback Intake Baseline",
        "Feedback Categories",
        "Review Cadence",
        "Refresh Triggers",
        "Article Quality Scorecard Fields",
        "Trust/Safety Guardrails",
        "SEO Guardrails",
        "Senior UX Guardrails",
        "Accessibility Guardrails",
        "Reader Experience Guardrails",
        "Monetization Guardrails",
        "Feedback Privacy Boundary Placeholder",
        "Data Inputs Not Yet Available",
        "Future Automation Opportunities",
        "Required Human Decisions",
        "Einfache Sprache bedeutet nicht anspruchslose Sprache. Inhalte sollen klar, freundlich und zugänglich sein, aber ältere Leserinnen und Leser als erwachsene, erfahrene und interessierte Menschen ernst nehmen.",
        "Keine Live-Optimierung",
        "Keine Live-Analytics",
        "kein echtes Nutzerfeedback",
        "kein Reader-Experience-Feedback",
        "Keine Ranking Proofs",
        "Keine Traffic Proofs",
        "Keine Revenue Proofs",
        "Keine Conversion Proofs",
        "keine Publish Readiness",
        "keine rechtliche Freigabe",
        "keine Operator Acceptance",
        "keine Monetarisierung",
    ]
    required_core_quality_dimensions = [
        "evidence_quality",
        "claim_source_alignment",
        "senior_readability",
        "safety_language",
        "accessibility",
        "search_intent_fit",
        "freshness",
        "trust_risk",
        "monetization_risk",
        "publish_blockers",
    ]
    required_user_perspective_dimensions = [
        "target_user_empathy_fit",
        "caregiver_perspective_fit",
        "real_world_situation_fit",
        "confusion_prevention",
        "user_question_coverage",
        "emotional_safety",
        "practical_next_step_clarity",
        "print_or_forward_usefulness",
        "feedback_learnability",
    ]
    required_reader_experience_dimensions = [
        "reader_experience_quality",
        "reading_pleasure",
        "text_flow",
        "respectful_depth",
        "adult_reader_tone",
        "clarity_without_oversimplification",
        "emotional_warmth",
        "topic_engagement",
        "narrative_coherence",
        "calm_confident_voice",
    ]
    required_user_checks = [
        "Does the article start from the real user problem?",
        "Does it avoid shame, blame and panic?",
        "Does it explain what to do first?",
        "Does it avoid unnecessary technical jargon?",
        "Does it include practical next steps?",
        "Does it help a user who is uncertain or afraid of making a mistake?",
        "Does it remain respectful and not patronizing?",
    ]
    required_caregiver_checks = [
        "Can a relative or helper forward or print the article?",
        "Does the article help someone explain the topic calmly?",
        "Are helper notes needed?",
        "Are common support situations documented?",
        "Does the article avoid pressuring the senior user?",
    ]
    required_reader_checks = [
        "Does the article read naturally and pleasantly?",
        "Does the article have a calm, clear and confident voice?",
        "Does the article avoid sounding like a dry technical manual?",
        "Does the article avoid sounding childish, patronizing or oversimplified?",
        "Does the article respect older readers as adult, experienced and interested readers?",
        "Does the article provide enough depth to feel worthwhile?",
        "Does the article maintain clarity without flattening the topic too much?",
        "Does the article use transitions, examples and structure to support reading flow?",
        "Does the article make the topic feel approachable rather than burdensome?",
        "Does the article give the reader something useful and satisfying to take away?",
    ]
    required_feedback_categories = [
        "comprehension_problem",
        "ui_difference",
        "safety_question",
        "missing_explanation",
        "readability_problem",
        "caregiver_support_need",
        "product_question",
        "trust_question",
        "print_or_forward_request",
        "article_update_request",
        "reading_experience_feedback",
        "tone_feedback",
    ]
    required_missing_data = [
        "Search Console data",
        "analytics data",
        "ranking data",
        "keyword volume data",
        "keyword difficulty data",
        "conversion data",
        "user feedback data",
        "email feedback data",
        "usability test data",
        "reader experience feedback data",
        "monetization performance data",
    ]

    for fragment in (
        required_fragments
        + required_core_quality_dimensions
        + required_user_perspective_dimensions
        + required_reader_experience_dimensions
        + required_user_checks
        + required_caregiver_checks
        + required_reader_checks
        + required_feedback_categories
        + required_missing_data
    ):
        if fragment not in text:
            failures.append(f"Content quality feedback loop baseline must contain: {fragment}")

    if fields.get("quality_loop_id") != (
        "SHO-CONTENT-QUALITY-USER-PERSPECTIVE-READER-EXPERIENCE-FEEDBACK-LOOP-BASELINE"
    ):
        failures.append("Content quality feedback loop baseline has unexpected quality_loop_id")
    if normalized(fields.get("scope")) != "mvp_batch_01":
        failures.append("Content quality feedback loop baseline must have scope: MVP_BATCH_01")
    if normalized(fields.get("loop_status")) != "baseline_defined_not_live":
        failures.append("Content quality feedback loop baseline must have loop_status: baseline_defined_not_live")
    if normalized(fields.get("reader_experience_status")) != "baseline_defined":
        failures.append("Content quality feedback loop baseline must have reader_experience_status: baseline_defined")
    if normalized(fields.get("user_feedback_status")) != "not_collected":
        failures.append("Content quality feedback loop baseline must have user_feedback_status: not_collected")
    if normalized(fields.get("email_feedback_status")) != "not_connected":
        failures.append("Content quality feedback loop baseline must have email_feedback_status: not_connected")
    if normalized(fields.get("analytics_status")) != "not_connected":
        failures.append("Content quality feedback loop baseline must have analytics_status: not_connected")
    if normalized(fields.get("keyword_validation_status")) != "not_available":
        failures.append("Content quality feedback loop baseline must have keyword_validation_status: not_available")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Content quality feedback loop baseline must have monetization_status: not_approved")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Content quality feedback loop baseline must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Content quality feedback loop baseline must have publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Content quality feedback loop baseline must have public_launch_status: not_ready")

    forbidden_assignments = [
        "analytics_status: connected",
        "loop_status: active",
        "user_feedback_status: collected",
        "email_feedback_status: connected",
        "reader_experience_feedback_status: collected",
        "feedback_protocol_status: active",
        "keyword_validation_status: documented",
        "monetization_status: approved",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: approved_for_publish",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "approved_for_publish: true",
        "publish_ready: true",
    ]
    lower_text = text.lower()
    for fragment in forbidden_assignments:
        if fragment in lower_text:
            failures.append(
                "Content quality feedback loop baseline must not contain forbidden activation marker: "
                f"{fragment}"
            )

    return 1


def validate_user_feedback_intake_protocol_baseline(failures: list[str]) -> int:
    if not USER_FEEDBACK_INTAKE_PROTOCOL_PATH.exists():
        failures.append("Missing user feedback intake protocol baseline: docs/operations/USER_FEEDBACK_INTAKE_PROTOCOL_BASELINE.md")
        return 0

    text = USER_FEEDBACK_INTAKE_PROTOCOL_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_fragments = [
        "feedback_protocol_id: SHO-USER-FEEDBACK-INTAKE-PROTOCOL-BASELINE",
        "feedback_protocol_status: baseline_defined_not_live",
        "email_feedback_status: not_connected",
        "user_feedback_status: not_collected",
        "reader_experience_feedback_status: not_collected",
        "privacy_review_status: required_before_live_use",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
        "Purpose",
        "Explicit Non-Acceptance",
        "Intended Later Sources",
        "Email Feedback Categories",
        "Reader Experience Feedback Categories",
        "Feedback Register Fields",
        "Safety Escalation Placeholder",
        "Privacy Review Placeholder",
        "Content Improvement Mapping",
        "Reader Experience Improvement Mapping",
        "Refresh Trigger Candidates",
        "Forbidden Use",
        "Required Human Decisions Before Live Use",
        "kein E-Mail-Feedback",
        "kein Nutzerfeedback",
        "kein Reader-Experience-Feedback",
        "Privacy-Review",
    ]
    required_feedback_register_fields = [
        "feedback_id",
        "received_at",
        "article_slug",
        "user_type",
        "topic",
        "problem_type",
        "confusion_point",
        "safety_relevance",
        "reading_experience_signal",
        "tone_signal",
        "content_gap",
        "suggested_action",
        "privacy_sensitive",
        "status",
        "linked_refresh_patch",
    ]
    required_feedback_categories = [
        "comprehension_problem",
        "ui_difference",
        "safety_question",
        "missing_explanation",
        "readability_problem",
        "caregiver_support_need",
        "product_question",
        "trust_question",
        "print_or_forward_request",
        "article_update_request",
        "reading_experience_feedback",
        "tone_feedback",
    ]

    for fragment in required_fragments + required_feedback_register_fields + required_feedback_categories:
        if fragment not in text:
            failures.append(f"User feedback intake protocol baseline must contain: {fragment}")

    if fields.get("feedback_protocol_id") != "SHO-USER-FEEDBACK-INTAKE-PROTOCOL-BASELINE":
        failures.append("User feedback intake protocol baseline has unexpected feedback_protocol_id")
    if normalized(fields.get("feedback_protocol_status")) != "baseline_defined_not_live":
        failures.append("User feedback intake protocol baseline must have feedback_protocol_status: baseline_defined_not_live")
    if normalized(fields.get("email_feedback_status")) != "not_connected":
        failures.append("User feedback intake protocol baseline must have email_feedback_status: not_connected")
    if normalized(fields.get("user_feedback_status")) != "not_collected":
        failures.append("User feedback intake protocol baseline must have user_feedback_status: not_collected")
    if normalized(fields.get("reader_experience_feedback_status")) != "not_collected":
        failures.append("User feedback intake protocol baseline must have reader_experience_feedback_status: not_collected")
    if normalized(fields.get("privacy_review_status")) != "required_before_live_use":
        failures.append("User feedback intake protocol baseline must have privacy_review_status: required_before_live_use")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("User feedback intake protocol baseline must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("User feedback intake protocol baseline must have publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("User feedback intake protocol baseline must have public_launch_status: not_ready")

    forbidden_assignments = [
        "analytics_status: connected",
        "loop_status: active",
        "user_feedback_status: collected",
        "email_feedback_status: connected",
        "reader_experience_feedback_status: collected",
        "feedback_protocol_status: active",
        "keyword_validation_status: documented",
        "monetization_status: approved",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: approved_for_publish",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "approved_for_publish: true",
        "publish_ready: true",
    ]
    lower_text = text.lower()
    for fragment in forbidden_assignments:
        if fragment in lower_text:
            failures.append(
                "User feedback intake protocol baseline must not contain forbidden activation marker: "
                f"{fragment}"
            )

    return 1


def validate_content_quality_scorecard_template_batch_01(failures: list[str]) -> int:
    readme_path = ROOT / "docs/content/article_quality_scorecards/README.md"
    if not readme_path.exists():
        failures.append("Missing article quality scorecards README: docs/content/article_quality_scorecards/README.md")
        return 0
    if not ARTICLE_QUALITY_SCORECARD_TEMPLATE_PATH.exists():
        failures.append(
            "Missing content quality scorecard template: "
            "docs/content/article_quality_scorecards/CONTENT_QUALITY_SCORECARD_TEMPLATE_BATCH_01.md"
        )
        return 0

    readme_text = readme_path.read_text(encoding="utf-8")
    template_text = ARTICLE_QUALITY_SCORECARD_TEMPLATE_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(template_text)

    readme_required_fragments = [
        "Article Quality Scorecards",
        "Scorecards sind Bewertungs- und Review-Raster.",
        "Keine Scorecard setzt `approved_for_publish`.",
        "Der Human Operator bleibt finale Annahmeautorität.",
    ]
    for fragment in readme_required_fragments:
        if fragment not in readme_text:
            failures.append(f"Article quality scorecards README must contain: {fragment}")

    required_frontmatter_fragments = [
        "scorecard_template_id: SHO-CONTENT-QUALITY-SCORECARD-TEMPLATE-BATCH01",
        "batch_id: MVP_BATCH_01",
        "scorecard_status: template_defined_not_applied",
        "loop_status: baseline_defined_not_live",
        "user_feedback_status: not_collected",
        "email_feedback_status: not_connected",
        "reader_experience_feedback_status: not_collected",
        "analytics_status: not_connected",
        "keyword_validation_status: not_available",
        "monetization_status: not_approved",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
    ]
    required_sections = [
        "Purpose",
        "Scope",
        "Explicit Non-Acceptance",
        "How To Use This Scorecard",
        "Required Article Metadata",
        "Score Scale",
        "Core Quality Score Fields",
        "User Perspective Score Fields",
        "Reader Experience Score Fields",
        "Safety and Trust Fields",
        "Accessibility Fields",
        "SEO/Search Intent Fields",
        "Freshness and Refresh Fields",
        "Monetization Risk Fields",
        "Feedback Fields",
        "Publish Blocker Fields",
        "Required Reviewer Notes",
        "Required Human Decisions",
        "Output Recommendation Values",
    ]
    required_placeholders = [
        "TBD_BY_REVIEW",
        "NOT_APPLIED",
        "NOT_AVAILABLE",
        "BLOCKED",
        "NEEDS_REVIEW",
        "PASS",
        "FAIL",
    ]
    required_article_metadata_fields = [
        "article_slug",
        "linked_brief_id",
        "linked_article_candidate_path",
        "review_date",
        "reviewer_role",
        "source_pack_path",
        "claim_map_path",
        "article_readiness_dashboard_path",
        "quality_loop_baseline_path",
        "operator_acceptance_status",
        "publish_readiness_status",
    ]
    required_score_scale = [
        "0 = blocked / missing / unsafe",
        "1 = weak / needs major revision",
        "2 = usable but needs review or improvement",
        "3 = strong for current stage, not automatically publish-ready",
        "A score of 3 does not imply publish readiness, legal approval or Operator Acceptance.",
    ]
    required_core_quality_fields = [
        "evidence_quality",
        "claim_source_alignment",
        "senior_readability",
        "safety_language",
        "accessibility",
        "search_intent_fit",
        "freshness",
        "trust_risk",
        "monetization_risk",
        "publish_blockers",
    ]
    required_user_perspective_fields = [
        "target_user_empathy_fit",
        "caregiver_perspective_fit",
        "real_world_situation_fit",
        "confusion_prevention",
        "user_question_coverage",
        "emotional_safety",
        "practical_next_step_clarity",
        "print_or_forward_usefulness",
        "feedback_learnability",
    ]
    required_reader_experience_fields = [
        "reader_experience_quality",
        "reading_pleasure",
        "text_flow",
        "respectful_depth",
        "adult_reader_tone",
        "clarity_without_oversimplification",
        "emotional_warmth",
        "topic_engagement",
        "narrative_coherence",
        "calm_confident_voice",
    ]
    required_safety_trust_checks = [
        "no panic amplification",
        "no blame toward affected users",
        "no guarantee that fraud is always detectable",
        "no legal advice",
        "no legal approval claim",
        "no blocked WhatsApp UI instructions",
        "no use of SHO-CLAIM-007 unless later explicitly unlocked",
        "no source-less factual claims",
    ]
    required_feedback_fields = [
        "user_feedback_status",
        "email_feedback_status",
        "reader_experience_feedback_status",
        "feedback_summary",
        "feedback_source",
        "feedback_review_status",
        "linked_feedback_register",
        "privacy_review_status",
    ]
    required_seo_fields = [
        "search_intent_fit",
        "keyword_validation_status",
        "search_volume_status",
        "keyword_difficulty_status",
        "ranking_data_status",
        "traffic_data_status",
    ]
    required_output_values = [
        "blocked",
        "needs_major_revision",
        "needs_targeted_revision",
        "ready_for_next_internal_review",
        "candidate_for_human_operator_review_not_publish_ready",
        "approved_for_publish",
        "publish_ready",
        "operator_accepted",
        "public_launch_ready",
    ]
    required_fragments = (
        required_frontmatter_fragments
        + required_sections
        + required_placeholders
        + required_article_metadata_fields
        + required_score_scale
        + required_core_quality_fields
        + required_user_perspective_fields
        + required_reader_experience_fields
        + required_safety_trust_checks
        + required_feedback_fields
        + required_seo_fields
        + required_output_values
        + [
            "Einfache Sprache bedeutet nicht anspruchslose Sprache. Inhalte sollen klar, freundlich und zugänglich sein, aber ältere Leserinnen und Leser als erwachsene, erfahrene und interessierte Menschen ernst nehmen.",
            "No numeric SEO metrics may be invented.",
            "These fields must default to unavailable or not collected states.",
            "Diese Scorecard-Vorlage ist keine angewendete Review.",
            "Diese Scorecard-Vorlage setzt keine Publish Readiness.",
            "Diese Scorecard-Vorlage erstellt keine Operator Acceptance.",
            "Diese Scorecard-Vorlage aktiviert keine Analytics.",
            "Diese Scorecard-Vorlage aktiviert kein Live-Feedback.",
            "Diese Scorecard-Vorlage behauptet keine SEO-Metriken.",
            "Diese Scorecard-Vorlage genehmigt keine Monetarisierung.",
        ]
    )
    for fragment in required_fragments:
        if fragment not in template_text:
            failures.append(f"Content quality scorecard template must contain: {fragment}")

    if fields.get("scorecard_template_id") != "SHO-CONTENT-QUALITY-SCORECARD-TEMPLATE-BATCH01":
        failures.append("Content quality scorecard template has unexpected scorecard_template_id")
    if normalized(fields.get("batch_id")) != "mvp_batch_01":
        failures.append("Content quality scorecard template must have batch_id: MVP_BATCH_01")
    if normalized(fields.get("scorecard_status")) != "template_defined_not_applied":
        failures.append("Content quality scorecard template must have scorecard_status: template_defined_not_applied")
    if normalized(fields.get("loop_status")) != "baseline_defined_not_live":
        failures.append("Content quality scorecard template must have loop_status: baseline_defined_not_live")
    if normalized(fields.get("user_feedback_status")) != "not_collected":
        failures.append("Content quality scorecard template must have user_feedback_status: not_collected")
    if normalized(fields.get("email_feedback_status")) != "not_connected":
        failures.append("Content quality scorecard template must have email_feedback_status: not_connected")
    if normalized(fields.get("reader_experience_feedback_status")) != "not_collected":
        failures.append("Content quality scorecard template must have reader_experience_feedback_status: not_collected")
    if normalized(fields.get("analytics_status")) != "not_connected":
        failures.append("Content quality scorecard template must have analytics_status: not_connected")
    if normalized(fields.get("keyword_validation_status")) != "not_available":
        failures.append("Content quality scorecard template must have keyword_validation_status: not_available")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Content quality scorecard template must have monetization_status: not_approved")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Content quality scorecard template must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Content quality scorecard template must have publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Content quality scorecard template must have public_launch_status: not_ready")

    forbidden_assignments = [
        "scorecard_status: accepted",
        "scorecard_status: approved_for_publish",
        "scorecard_status: publish_ready",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: approved_for_publish",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "monetization_status: approved",
        "analytics_status: connected",
        "user_feedback_status: collected",
        "email_feedback_status: connected",
        "reader_experience_feedback_status: collected",
        "keyword_validation_status: documented",
        "approved_for_publish: true",
        "publish_ready: true",
    ]
    lower_text = template_text.lower()
    for fragment in forbidden_assignments:
        if fragment in lower_text:
            failures.append(
                "Content quality scorecard template must not contain forbidden activation marker: "
                f"{fragment}"
            )

    return 1


def validate_final_article_candidate_brief_002(failures: list[str]) -> int:
    readme_path = FINAL_ARTICLE_CANDIDATES_DIR / "README.md"
    if not readme_path.exists():
        failures.append("Missing final article candidates README: docs/content/final_article_candidates/README.md")
        return 0
    if not FINAL_ARTICLE_CANDIDATE_BRIEF_002_PATH.exists():
        failures.append(
            "Missing final article candidate for Brief 002: "
            "docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md"
        )
        return 0

    readme_text = readme_path.read_text(encoding="utf-8")
    text = FINAL_ARTICLE_CANDIDATE_BRIEF_002_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    readme_required_fragments = [
        "Final Article Candidates",
        "Final Article Candidates sind interne Artikelkandidaten",
        "Sie sind trotzdem keine veröffentlichten Artikel.",
        "Final Article Candidates sind nicht Publish Readiness.",
        "Final Article Candidates sind nicht Operator Acceptance.",
        "Scorecard Review.",
    ]
    for fragment in readme_required_fragments:
        if fragment not in readme_text:
            failures.append(f"Final article candidates README must contain: {fragment}")

    required_frontmatter_fragments = [
        "final_article_candidate_id: SHO-FINAL-ARTICLE-CANDIDATE-BATCH01-BRIEF002",
        "batch_id: MVP_BATCH_01",
        "linked_brief_id: SHO-MVP-BRIEF-002",
        "slug: betrugsnachrichten-auf-whatsapp-erkennen",
        "article_status: final_article_candidate_not_publish_ready",
        "review_status: scorecard_review_completed_not_publish_ready",
        "scorecard_status: review_completed_not_publish_ready",
        "linked_scorecard_template: docs/content/article_quality_scorecards/CONTENT_QUALITY_SCORECARD_TEMPLATE_BATCH_01.md",
        "linked_applied_scorecard: docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md",
        "linked_article_draft_candidate: docs/content/article_draft_candidates/betrugsnachrichten-auf-whatsapp-erkennen.article-draft-candidate.md",
        "linked_article_readiness_dashboard: docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md",
        "linked_quality_loop_baseline: docs/operations/CONTENT_QUALITY_USER_PERSPECTIVE_READER_EXPERIENCE_AND_FEEDBACK_LOOP_BASELINE.md",
        "allowed_claims: SHO-CLAIM-004; SHO-CLAIM-005; SHO-CLAIM-006",
        "blocked_claims: SHO-CLAIM-007",
        "allowed_sources: SHO-SRC-005; SHO-SRC-006; SHO-SRC-007",
        "user_feedback_status: not_collected",
        "email_feedback_status: not_connected",
        "reader_experience_feedback_status: not_collected",
        "analytics_status: not_connected",
        "keyword_validation_status: not_available",
        "monetization_status: not_approved",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
    ]
    required_sections = [
        "Purpose",
        "Explicit Non-Acceptance",
        "Source and Claim Boundaries",
        "Reader Experience Note",
        "Final Article Candidate Text",
        "Internal Source/Claim Marker Notes",
        "Blocked Claim Carry-Forward",
        "Required Later Reviews",
        "Required Human Decisions",
        "Forbidden Work",
    ]
    required_article_structure = [
        "# Betrugsnachrichten auf WhatsApp erkennen",
        "Das Wichtigste zuerst",
        "3-Schritte-Sofort-Check",
        "Woran Sie eine Betrugsnachricht erkennen",
        "Was Sie tun können, wenn Sie unsicher sind",
        "Für Angehörige und unterstützende Personen",
        "Ruhige Checkliste",
        "Häufige Fehler, die Sie vermeiden können",
        "Was dieser Artikel bewusst nicht abdeckt",
        "Internal source/claim marker note",
        "Explicit non-acceptance note",
    ]
    required_safety_fragments = [
        "Es ist in Ordnung, zuerst innezuhalten.",
        "das ist kein Grund, sich zu schämen",
        "Er gibt keine Garantie, Betrug immer sicher zu erkennen.",
        "Der sicherste erste Schritt ist nicht Eile, sondern Prüfung.",
        "Öffnen Sie keine Links, wenn Sie unsicher sind.",
        "Überweisen Sie kein Geld",
        "Nutzen Sie einen bekannten direkten Kontaktweg",
        "Dieser Artikel beschreibt keine rechtlichen Schritte und ersetzt keine Beratung im Einzelfall.",
        "Er ist auch keine juristische Beratung.",
    ]
    required_caregiver_fragments = [
        "Wenn Ihnen ein Elternteil, Großelternteil oder eine andere ältere Person eine verdächtige Nachricht zeigt, bleiben Sie ruhig.",
        "Vorwürfe helfen nicht.",
        "Lesen Sie die Nachricht gemeinsam.",
        "Helfen Sie beim Prüfen über bekannte Kontaktwege",
        "Du hast nichts falsch gemacht.",
    ]
    required_boundary_fragments = [
        "Einfache Sprache bedeutet nicht anspruchslose Sprache. Inhalte sollen klar, freundlich und zugänglich sein, aber ältere Leserinnen und Leser als erwachsene, erfahrene und interessierte Menschen ernst nehmen.",
        "SHO-CLAIM-004",
        "SHO-CLAIM-005",
        "SHO-CLAIM-006",
        "SHO-CLAIM-007 remains blocked.",
        "WhatsApp block/report UI instructions remain forbidden.",
        "No WhatsApp block/report step-by-step instructions are included.",
        "No publish readiness is set.",
        "No Operator Acceptance is set.",
        "SHO-SRC-005",
        "SHO-SRC-006",
        "SHO-SRC-007",
        "[claim: SHO-CLAIM-004 | sources: SHO-SRC-005, SHO-SRC-006]",
        "[claim: SHO-CLAIM-005 | sources: SHO-SRC-005, SHO-SRC-006]",
        "[claim: SHO-CLAIM-006 | sources: SHO-SRC-007]",
        "Die Arbeitsmarker im Artikel sind interne Review-Marker. Sie sind keine finalen Leserzitate.",
        "scorecard_review_completed_not_publish_ready",
    ]
    for fragment in (
        required_frontmatter_fragments
        + required_sections
        + required_article_structure
        + required_safety_fragments
        + required_caregiver_fragments
        + required_boundary_fragments
    ):
        if fragment not in text:
            failures.append(f"Final article candidate Brief 002 must contain: {fragment}")

    if fields.get("final_article_candidate_id") != "SHO-FINAL-ARTICLE-CANDIDATE-BATCH01-BRIEF002":
        failures.append("Final article candidate Brief 002 has unexpected final_article_candidate_id")
    if normalized(fields.get("batch_id")) != "mvp_batch_01":
        failures.append("Final article candidate Brief 002 must have batch_id: MVP_BATCH_01")
    if fields.get("linked_brief_id") != "SHO-MVP-BRIEF-002":
        failures.append("Final article candidate Brief 002 must have linked_brief_id: SHO-MVP-BRIEF-002")
    if normalized(fields.get("article_status")) != "final_article_candidate_not_publish_ready":
        failures.append("Final article candidate Brief 002 must have article_status: final_article_candidate_not_publish_ready")
    if normalized(fields.get("review_status")) != "scorecard_review_completed_not_publish_ready":
        failures.append(
            "Final article candidate Brief 002 must have review_status: "
            "scorecard_review_completed_not_publish_ready"
        )
    if normalized(fields.get("scorecard_status")) != "review_completed_not_publish_ready":
        failures.append("Final article candidate Brief 002 must have scorecard_status: review_completed_not_publish_ready")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Final article candidate Brief 002 must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Final article candidate Brief 002 must have publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Final article candidate Brief 002 must have public_launch_status: not_ready")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Final article candidate Brief 002 must have monetization_status: not_approved")
    if normalized(fields.get("analytics_status")) != "not_connected":
        failures.append("Final article candidate Brief 002 must have analytics_status: not_connected")
    if normalized(fields.get("keyword_validation_status")) != "not_available":
        failures.append("Final article candidate Brief 002 must have keyword_validation_status: not_available")
    if normalized(fields.get("user_feedback_status")) != "not_collected":
        failures.append("Final article candidate Brief 002 must have user_feedback_status: not_collected")
    if normalized(fields.get("email_feedback_status")) != "not_connected":
        failures.append("Final article candidate Brief 002 must have email_feedback_status: not_connected")
    if normalized(fields.get("reader_experience_feedback_status")) != "not_collected":
        failures.append("Final article candidate Brief 002 must have reader_experience_feedback_status: not_collected")

    if "[claim: SHO-CLAIM-007" in text:
        failures.append("Final article candidate Brief 002 must not use active SHO-CLAIM-007 working marker")

    forbidden_fragments = [
        "tippen Sie auf Blockieren",
        "tippen sie auf blockieren",
        "Chat melden",
        "chat melden",
        "Kontakt blockieren",
        "kontakt blockieren",
        "Blockieren und melden",
        "blockieren und melden",
    ]
    for fragment in forbidden_fragments:
        if fragment in text:
            failures.append(f"Final article candidate Brief 002 must not contain WhatsApp UI instruction: {fragment}")

    forbidden_activation_markers = [
        "article_status: publish_candidate",
        "review_status: approved_for_publish",
        "approved_for_publish: true",
        "publish_ready: true",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: approved_for_publish",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "monetization_status: approved",
        "analytics_status: connected",
        "user_feedback_status: collected",
        "email_feedback_status: connected",
        "reader_experience_feedback_status: collected",
        "keyword_validation_status: documented",
    ]
    lower_text = text.lower()
    for fragment in forbidden_activation_markers:
        if fragment in lower_text:
            failures.append(
                "Final article candidate Brief 002 must not contain forbidden activation marker: "
                f"{fragment}"
            )

    return 1


def validate_applied_scorecard_brief_002(failures: list[str]) -> int:
    if not APPLIED_SCORECARD_BRIEF_002_PATH.exists():
        failures.append(
            "Missing applied scorecard for Brief 002: "
            "docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md"
        )
        return 0

    text = APPLIED_SCORECARD_BRIEF_002_PATH.read_text(encoding="utf-8")
    fields = parse_frontmatter_fields(text)

    required_frontmatter_fragments = [
        "scorecard_id: SHO-SCORECARD-BATCH01-BRIEF002-FINAL-ARTICLE-CANDIDATE",
        "batch_id: MVP_BATCH_01",
        "linked_brief_id: SHO-MVP-BRIEF-002",
        "linked_article_candidate_path: docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md",
        "linked_scorecard_template: docs/content/article_quality_scorecards/CONTENT_QUALITY_SCORECARD_TEMPLATE_BATCH_01.md",
        "scorecard_status: review_completed_not_publish_ready",
        "scorecard_recommendation_status: ready_for_next_internal_review",
        "review_status: scorecard_review_completed_not_publish_ready",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "user_feedback_status: not_collected",
        "email_feedback_status: not_connected",
        "reader_experience_feedback_status: not_collected",
        "keyword_validation_status: not_available",
    ]
    required_sections = [
        "Purpose",
        "Explicit Non-Acceptance",
        "Reviewed Artifact",
        "Review Method",
        "Score Scale",
        "Executive Review Summary",
        "Core Quality Scores",
        "User Perspective Scores",
        "Reader Experience Scores",
        "Safety and Trust Review",
        "Accessibility Review",
        "SEO/Search Intent Review",
        "Freshness and Refresh Review",
        "Monetization Risk Review",
        "Feedback Review",
        "Publish Blocker Review",
        "Strengths",
        "Findings",
        "Required Follow-Up",
        "Recommendation",
        "Required Human Decisions",
        "Forbidden Conclusions",
    ]
    required_score_scale = [
        "0 = blocked / missing / unsafe",
        "1 = weak / needs major revision",
        "2 = usable but needs review or improvement",
        "3 = strong for current stage, not automatically publish-ready",
        "A score of 3 does not imply publish readiness, legal approval or Operator Acceptance.",
    ]
    required_core_quality_fields = [
        "evidence_quality",
        "claim_source_alignment",
        "senior_readability",
        "safety_language",
        "accessibility",
        "search_intent_fit",
        "freshness",
        "trust_risk",
        "monetization_risk",
        "publish_blockers",
    ]
    required_user_perspective_fields = [
        "target_user_empathy_fit",
        "caregiver_perspective_fit",
        "real_world_situation_fit",
        "confusion_prevention",
        "user_question_coverage",
        "emotional_safety",
        "practical_next_step_clarity",
        "print_or_forward_usefulness",
        "feedback_learnability",
    ]
    required_reader_experience_fields = [
        "reader_experience_quality",
        "reading_pleasure",
        "text_flow",
        "respectful_depth",
        "adult_reader_tone",
        "clarity_without_oversimplification",
        "emotional_warmth",
        "topic_engagement",
        "narrative_coherence",
        "calm_confident_voice",
    ]
    required_safety_checks = [
        "no panic amplification",
        "no blame toward affected users",
        "no guarantee that fraud is always detectable",
        "no legal advice",
        "no legal approval claim",
        "no blocked WhatsApp UI instructions",
        "no active use of SHO-CLAIM-007 as working marker",
        "no source-less factual claims found within the reviewed scope, or list any found issues as findings",
    ]
    required_seo_fragments = [
        "keyword_validation_status: not_available",
        "search_volume_status: NOT_AVAILABLE",
        "keyword_difficulty_status: NOT_AVAILABLE",
        "ranking_data_status: NOT_AVAILABLE",
        "traffic_data_status: NOT_AVAILABLE",
        "no numeric SEO metrics were reviewed or invented",
    ]
    required_feedback_fragments = [
        "user_feedback_status: not_collected",
        "email_feedback_status: not_connected",
        "reader_experience_feedback_status: not_collected",
        "feedback_summary: NOT_AVAILABLE",
        "feedback_source: NOT_AVAILABLE",
        "privacy_review_status: required_before_live_use",
        "no real user feedback or email feedback was reviewed or invented",
    ]
    required_publish_blocker_fragments = [
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "public_launch_status: not_ready",
        "legal_approval_status: not_approved",
        "SHO-CLAIM-007 remains blocked",
        "WhatsApp block/report UI instructions remain forbidden",
        "scorecard review does not create publish readiness",
    ]
    required_finding_ids = [
        "SHO-SCORECARD-002-SRC-001",
        "SHO-SCORECARD-002-UX-001",
        "SHO-SCORECARD-002-READ-001",
        "SHO-SCORECARD-002-ACC-001",
        "SHO-SCORECARD-002-SEO-001",
        "SHO-SCORECARD-002-FB-001",
        "SHO-SCORECARD-002-PUB-001",
    ]
    required_finding_columns = [
        "finding_id",
        "category",
        "severity",
        "status",
        "summary",
        "required_action",
    ]
    required_fragments = (
        required_frontmatter_fragments
        + required_sections
        + required_score_scale
        + required_core_quality_fields
        + required_user_perspective_fields
        + required_reader_experience_fields
        + required_safety_checks
        + required_seo_fragments
        + required_feedback_fragments
        + required_publish_blocker_fragments
        + required_finding_ids
        + required_finding_columns
        + [
            "Einfache Sprache bedeutet nicht anspruchslose Sprache. Inhalte sollen klar, freundlich und zugänglich sein, aber ältere Leserinnen und Leser als erwachsene, erfahrene und interessierte Menschen ernst nehmen.",
            "Source/claim marker alignment reviewed; no new sources added; final citation metadata remains open.",
            "Senior/user perspective is strong enough for next internal review but still requires later human review.",
            "Reader experience is strong enough for next internal review but still requires later human review.",
            "Accessibility requires later dedicated accessibility standard/review.",
            "SEO metrics not available; no metrics invented.",
            "Feedback not collected; no feedback invented.",
            "Publish readiness remains blocked/not_ready.",
            "ready_for_next_internal_review",
        ]
    )
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(f"Applied scorecard Brief 002 must contain: {fragment}")

    if fields.get("scorecard_id") != "SHO-SCORECARD-BATCH01-BRIEF002-FINAL-ARTICLE-CANDIDATE":
        failures.append("Applied scorecard Brief 002 has unexpected scorecard_id")
    if normalized(fields.get("batch_id")) != "mvp_batch_01":
        failures.append("Applied scorecard Brief 002 must have batch_id: MVP_BATCH_01")
    if fields.get("linked_brief_id") != "SHO-MVP-BRIEF-002":
        failures.append("Applied scorecard Brief 002 must have linked_brief_id: SHO-MVP-BRIEF-002")
    if normalized(fields.get("scorecard_status")) != "review_completed_not_publish_ready":
        failures.append("Applied scorecard Brief 002 must have scorecard_status: review_completed_not_publish_ready")
    if normalized(fields.get("scorecard_recommendation_status")) != "ready_for_next_internal_review":
        failures.append("Applied scorecard Brief 002 must have scorecard_recommendation_status: ready_for_next_internal_review")
    if normalized(fields.get("review_status")) != "scorecard_review_completed_not_publish_ready":
        failures.append("Applied scorecard Brief 002 must have review_status: scorecard_review_completed_not_publish_ready")
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Applied scorecard Brief 002 must have operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Applied scorecard Brief 002 must have publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Applied scorecard Brief 002 must have public_launch_status: not_ready")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Applied scorecard Brief 002 must have monetization_status: not_approved")
    if normalized(fields.get("analytics_status")) != "not_connected":
        failures.append("Applied scorecard Brief 002 must have analytics_status: not_connected")
    if normalized(fields.get("user_feedback_status")) != "not_collected":
        failures.append("Applied scorecard Brief 002 must have user_feedback_status: not_collected")
    if normalized(fields.get("email_feedback_status")) != "not_connected":
        failures.append("Applied scorecard Brief 002 must have email_feedback_status: not_connected")
    if normalized(fields.get("reader_experience_feedback_status")) != "not_collected":
        failures.append("Applied scorecard Brief 002 must have reader_experience_feedback_status: not_collected")
    if normalized(fields.get("keyword_validation_status")) != "not_available":
        failures.append("Applied scorecard Brief 002 must have keyword_validation_status: not_available")

    candidate_text = FINAL_ARTICLE_CANDIDATE_BRIEF_002_PATH.read_text(encoding="utf-8")
    if "linked_applied_scorecard: docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md" not in candidate_text:
        failures.append("Final article candidate Brief 002 must link the applied scorecard")
    if "publish_readiness_status: not_ready" not in candidate_text:
        failures.append("Final article candidate Brief 002 must remain publish_readiness_status: not_ready")
    if "operator_acceptance_status: not_accepted" not in candidate_text:
        failures.append("Final article candidate Brief 002 must remain operator_acceptance_status: not_accepted")

    batch_text = BATCH_MANIFEST_PATH.read_text(encoding="utf-8")
    if "article_quality_scorecards:" not in batch_text:
        failures.append("Batch manifest must contain article_quality_scorecards section")
    if "- docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md" not in batch_text:
        failures.append("Batch manifest must link applied scorecard Brief 002")

    dashboard_text = ARTICLE_READINESS_DASHBOARD_PATH.read_text(encoding="utf-8")
    if "scorecard review completed not publish-ready" not in dashboard_text:
        failures.append("Article readiness dashboard must mention scorecard review completed not publish-ready")

    forbidden_activation_markers = [
        "article_status: publish_candidate",
        "review_status: approved_for_publish",
        "approved_for_publish: true",
        "publish_ready: true",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: approved_for_publish",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "monetization_status: approved",
        "analytics_status: connected",
        "user_feedback_status: collected",
        "email_feedback_status: connected",
        "reader_experience_feedback_status: collected",
        "keyword_validation_status: documented",
        "scorecard_recommendation_status: approved_for_publish",
        "scorecard_recommendation_status: publish_ready",
        "scorecard_recommendation_status: operator_accepted",
    ]
    lower_text = text.lower()
    for fragment in forbidden_activation_markers:
        if fragment in lower_text:
            failures.append(
                "Applied scorecard Brief 002 must not contain forbidden activation marker: "
                f"{fragment}"
            )

    return 1


def validate_human_operator_review_packet_final_article_candidate_brief_002(
    failures: list[str],
) -> int:
    if not HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002_PATH.exists():
        failures.append(
            "Missing Human Operator review packet for Final Article Candidate Brief 002: "
            "docs/operations/operator_review_packets/HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md"
        )
        return 0

    text = HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002_PATH.read_text(
        encoding="utf-8"
    )
    fields = parse_frontmatter_fields(text)

    required_frontmatter_fragments = [
        "operator_review_packet_id: SHO-HUMAN-OPERATOR-REVIEW-PACKET-BATCH01-BRIEF002-FINAL-ARTICLE-CANDIDATE",
        "batch_id: MVP_BATCH_01",
        "linked_brief_id: SHO-MVP-BRIEF-002",
        "linked_final_article_candidate: docs/content/final_article_candidates/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.md",
        "linked_applied_scorecard: docs/content/article_quality_scorecards/betrugsnachrichten-auf-whatsapp-erkennen.final-article-candidate.scorecard.md",
        "review_packet_status: prepared_for_human_operator_review_not_acceptance",
        "operator_acceptance_status: not_accepted",
        "publish_readiness_status: not_ready",
        "public_launch_status: not_ready",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "user_feedback_status: not_collected",
        "email_feedback_status: not_connected",
        "reader_experience_feedback_status: not_collected",
        "keyword_validation_status: not_available",
    ]
    required_sections = [
        "Purpose",
        "Explicit Non-Acceptance",
        "Reviewed Artifacts",
        "Current Article State",
        "Scorecard Review Summary",
        "Allowed Claims and Sources",
        "Blocked Claims and Carry-Forward",
        "Remaining Blockers",
        "Human Operator Review Questions",
        "Possible Human Operator Outcomes",
        "Forbidden Outcomes",
        "Required Follow-Up Depending on Decision",
        "Guardrails Confirmed",
    ]
    required_non_acceptance_fragments = [
        "This packet is not Operator Acceptance.",
        "This packet is not Publish Readiness.",
        "This packet does not approve public launch.",
        "This packet does not approve monetization.",
        "This packet does not approve legal wording.",
        "This packet does not unlock SHO-CLAIM-007.",
        "This packet does not approve WhatsApp block/report UI instructions.",
    ]
    required_human_outcomes = [
        "request_revision",
        "request_accessibility_review",
        "request_final_source_metadata_review",
        "proceed_to_operator_review_candidate_not_publish_ready",
        "hold_blocked",
    ]
    required_forbidden_codex_outcomes = [
        "approved_for_publish",
        "publish_ready",
        "operator_accepted",
        "public_launch_ready",
        "monetization_approved",
    ]
    required_review_questions = [
        "Ist der Artikel aus Sicht der Zielgruppe ruhig, wuerdevoll und hilfreich genug?",
        "Trifft der Artikel die reale Situation aelterer Leserinnen und Leser?",
        "Ist die Balance aus Einfachheit und Anspruch angemessen?",
        "Sind die Safety-Hinweise ausreichend ruhig und klar?",
        "Soll der Artikel in eine gezielte Revision gehen?",
        "Soll eine zusaetzliche Accessibility-/Final-Source-Metadata-Review vorgeschaltet werden?",
        "Soll der Artikel als Human-Operator-Review-Kandidat weitergefuehrt werden, weiterhin nicht publish-ready?",
    ]
    required_guardrail_fragments = [
        "article_status: final_article_candidate_not_publish_ready",
        "review_status: scorecard_review_completed_not_publish_ready",
        "scorecard_status: review_completed_not_publish_ready",
        "scorecard_recommendation_status: ready_for_next_internal_review",
        "legal_approval_status: not_approved",
        "SHO-CLAIM-004",
        "SHO-CLAIM-005",
        "SHO-CLAIM-006",
        "SHO-SRC-005",
        "SHO-SRC-006",
        "SHO-SRC-007",
        "SHO-CLAIM-007 remains blocked",
        "WhatsApp block/report UI instructions remain forbidden",
        "No new claims added.",
        "No new sources added.",
        "No source metadata invented.",
        "No SEO, analytics, feedback, revenue or conversion data invented.",
    ]
    required_fragments = (
        required_frontmatter_fragments
        + required_sections
        + required_non_acceptance_fragments
        + required_human_outcomes
        + required_forbidden_codex_outcomes
        + required_review_questions
        + required_guardrail_fragments
    )
    for fragment in required_fragments:
        if fragment not in text:
            failures.append(
                "Human Operator review packet Final Article Candidate Brief 002 must contain: "
                f"{fragment}"
            )

    if (
        fields.get("operator_review_packet_id")
        != "SHO-HUMAN-OPERATOR-REVIEW-PACKET-BATCH01-BRIEF002-FINAL-ARTICLE-CANDIDATE"
    ):
        failures.append("Human Operator review packet Brief 002 has unexpected operator_review_packet_id")
    if normalized(fields.get("batch_id")) != "mvp_batch_01":
        failures.append("Human Operator review packet Brief 002 must have batch_id: MVP_BATCH_01")
    if fields.get("linked_brief_id") != "SHO-MVP-BRIEF-002":
        failures.append("Human Operator review packet Brief 002 must have linked_brief_id: SHO-MVP-BRIEF-002")
    if normalized(fields.get("review_packet_status")) != "prepared_for_human_operator_review_not_acceptance":
        failures.append(
            "Human Operator review packet Brief 002 must have review_packet_status: "
            "prepared_for_human_operator_review_not_acceptance"
        )
    if normalized(fields.get("operator_acceptance_status")) != "not_accepted":
        failures.append("Human Operator review packet Brief 002 must keep operator_acceptance_status: not_accepted")
    if normalized(fields.get("publish_readiness_status")) != "not_ready":
        failures.append("Human Operator review packet Brief 002 must keep publish_readiness_status: not_ready")
    if normalized(fields.get("public_launch_status")) != "not_ready":
        failures.append("Human Operator review packet Brief 002 must keep public_launch_status: not_ready")
    if normalized(fields.get("monetization_status")) != "not_approved":
        failures.append("Human Operator review packet Brief 002 must keep monetization_status: not_approved")
    if normalized(fields.get("analytics_status")) != "not_connected":
        failures.append("Human Operator review packet Brief 002 must keep analytics_status: not_connected")
    if normalized(fields.get("user_feedback_status")) != "not_collected":
        failures.append("Human Operator review packet Brief 002 must keep user_feedback_status: not_collected")
    if normalized(fields.get("email_feedback_status")) != "not_connected":
        failures.append("Human Operator review packet Brief 002 must keep email_feedback_status: not_connected")
    if normalized(fields.get("reader_experience_feedback_status")) != "not_collected":
        failures.append(
            "Human Operator review packet Brief 002 must keep "
            "reader_experience_feedback_status: not_collected"
        )
    if normalized(fields.get("keyword_validation_status")) != "not_available":
        failures.append("Human Operator review packet Brief 002 must keep keyword_validation_status: not_available")

    batch_text = BATCH_MANIFEST_PATH.read_text(encoding="utf-8")
    if "operator_review_packets:" not in batch_text:
        failures.append("Batch manifest must contain operator_review_packets section")
    if "- docs/operations/operator_review_packets/HUMAN_OPERATOR_REVIEW_PACKET_FINAL_ARTICLE_CANDIDATE_BRIEF_002.md" not in batch_text:
        failures.append("Batch manifest must link Human Operator review packet Brief 002")
    if "Brief 002 human operator review packet prepared, but no Operator Acceptance or Publish Readiness is set." not in batch_text:
        failures.append("Batch manifest must carry Human Operator review packet non-acceptance blocker")

    dashboard_text = ARTICLE_READINESS_DASHBOARD_PATH.read_text(encoding="utf-8")
    if "human operator review packet prepared not acceptance" not in dashboard_text:
        failures.append("Article readiness dashboard must mention human operator review packet prepared not acceptance")
    if "SHO-CLAIM-007 remains blocked" not in dashboard_text:
        failures.append("Article readiness dashboard must keep SHO-CLAIM-007 blocked")

    forbidden_activation_markers = [
        "approved_for_publish: true",
        "publish_ready: true",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: approved_for_publish",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "monetization_status: approved",
        "analytics_status: connected",
        "user_feedback_status: collected",
        "email_feedback_status: connected",
        "reader_experience_feedback_status: collected",
        "keyword_validation_status: documented",
        "review_packet_status: accepted",
        "review_packet_status: approved_for_publish",
        "operator_review_outcome_status: approved_for_publish",
        "operator_review_outcome_status: publish_ready",
        "operator_review_outcome_status: operator_accepted",
    ]
    lower_text = text.lower()
    for fragment in forbidden_activation_markers:
        if fragment in lower_text:
            failures.append(
                "Human Operator review packet Brief 002 must not contain forbidden activation marker: "
                f"{fragment}"
            )

    return 1


def validate_content_pipeline_contract_and_work_queue_v1(failures: list[str]) -> int:
    required_paths = [
        CONTENT_PIPELINE_DIR / "README.md",
        CONTENT_PIPELINE_CONTRACT_V1_PATH,
        CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1_PATH,
        WORK_QUEUE_V1_PATH,
        CONTENT_PIPELINE_RUNNER_SPEC_V1_PATH,
        NEXT_TASK_GENERATOR_SPEC_V1_PATH,
    ]
    count = 0
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing content pipeline artifact: {path.relative_to(ROOT)}")
        else:
            count += 1

    if count != len(required_paths):
        return count

    contract_text = CONTENT_PIPELINE_CONTRACT_V1_PATH.read_text(encoding="utf-8")
    role_text = CONTENT_PRODUCTION_ROLE_BOUNDARIES_V1_PATH.read_text(encoding="utf-8")
    queue_text = WORK_QUEUE_V1_PATH.read_text(encoding="utf-8")
    runner_text = CONTENT_PIPELINE_RUNNER_SPEC_V1_PATH.read_text(encoding="utf-8")
    generator_text = NEXT_TASK_GENERATOR_SPEC_V1_PATH.read_text(encoding="utf-8")

    required_stage_ids = [
        "STAGE_00_STRATEGY_TRUST_PORTFOLIO_INTAKE",
        "STAGE_01_TOPIC_INTAKE",
        "STAGE_02_KEYWORD_QUALIFICATION",
        "STAGE_03_SOURCE_DISCOVERY_EVIDENCE_GATE",
        "STAGE_04_CLAIM_EXTRACTION_CLAIM_MAPPING",
        "STAGE_05_CONTENT_BRIEF",
        "STAGE_06_SEO_BRIEF_ADDENDUM",
        "STAGE_07_DRAFT_SCAFFOLD",
        "STAGE_08_ARTICLE_CANDIDATE",
        "STAGE_09_QUALITY_READER_ACCESSIBILITY_SAFETY_REVIEWS",
        "STAGE_10_HUMAN_OPERATOR_REVIEW_PACKET",
        "STAGE_11_PUBLISH_CANDIDATE_DECISION",
        "STAGE_12_WEBSITE_PREVIEW_RELEASE_PREPARATION",
        "STAGE_13_PUBLIC_LAUNCH_DECISION",
        "STAGE_14_ANALYTICS_SEARCH_CONSOLE_FEEDBACK_INTAKE",
        "STAGE_15_REFRESH_REWRITE_MERGE_EXPANSION_LOOP",
        "STAGE_16_MONETIZATION_METHODOLOGY_TRUST_CONFLICT_GATE",
    ]
    required_stage_fields = [
        "stage_id",
        "stage_name",
        "purpose",
        "required_inputs",
        "produced_outputs",
        "allowed_actions",
        "forbidden_actions",
        "blocking_conditions",
        "validator_expectations",
        "human_gate_required",
        "automation_level",
        "allowed_next_stage",
        "non_acceptance_status",
    ]
    for stage_id in required_stage_ids:
        if stage_id not in contract_text:
            failures.append(f"Content Pipeline Contract V1 missing stage ID: {stage_id}")
    for field in required_stage_fields:
        if f"| {field} |" not in contract_text:
            failures.append(f"Content Pipeline Contract V1 missing stage field: {field}")
    for fragment in [
        "Build Mode Exit Gate",
        "Anti-Endless-Prompting Rules",
        "Pipeline Contract exists.",
        "Work Queue exists.",
        "Role Boundaries exist.",
        "Next tasks can be derived from repo state instead of ad hoc prompting.",
        "Documentation progress must not be confused with product progress.",
    ]:
        if fragment not in contract_text:
            failures.append(f"Content Pipeline Contract V1 must contain: {fragment}")

    required_role_fragments = [
        "Human Operator",
        "ChatGPT / Review and Prompt Controller",
        "Codex / Execution Agent",
        "Validators / Deterministic Checks",
        "Future Pipeline Runner",
        "External Primary Sources / Data Inputs",
        "Codex may produce, structure, inspect, validate, and report.",
        "Codex may not strategically approve, publish, monetize, accept, or invent missing data.",
        "publish_candidate",
        "publish_ready",
        "approved_for_publish",
        "operator_accepted",
        "public_launch_ready",
        "monetization_approved",
        "unlock blocked claims",
        "Codex must create a blocker report",
    ]
    for fragment in required_role_fragments:
        if fragment not in role_text:
            failures.append(f"Content Production Role Boundaries V1 must contain: {fragment}")

    required_queue_metadata = [
        "queue_id: CONTENT-WORK-QUEUE-V1",
        "queue_status: draft_operational_baseline",
        "batch_id: MVP_BATCH_01",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "queue_items:",
    ]
    for fragment in required_queue_metadata:
        if fragment not in queue_text:
            failures.append(f"Work Queue V1 must contain metadata fragment: {fragment}")

    required_queue_item_fields = [
        "queue_item_id:",
        "title:",
        "linked_stage_id:",
        "required_inputs:",
        "produced_outputs:",
        "blockers:",
        "allowed_next_action:",
        "forbidden_actions:",
        "human_gate_required:",
        "automation_candidate:",
        "status:",
    ]
    queue_item_blocks = re.split(r"\n  - queue_item_id: ", queue_text)
    queue_items = []
    if len(queue_item_blocks) > 1:
        queue_items = ["queue_item_id: " + block for block in queue_item_blocks[1:]]
    if len(queue_items) < 7:
        failures.append("Work Queue V1 must contain at least seven queue items")
    for index, item in enumerate(queue_items, start=1):
        for field in required_queue_item_fields:
            if field not in item:
                failures.append(f"Work Queue V1 item {index} missing field: {field}")

    required_queue_items = [
        "CQ-V1-001",
        "CQ-V1-002",
        "CQ-V1-003",
        "CQ-V1-004",
        "CQ-V1-005",
        "CQ-V1-006",
        "CQ-V1-007",
        "Brief 002 later publish-candidate decision packet preparation",
        "Brief 003 device/version scope decision",
        "Website information architecture / internal preview structure",
        "Pipeline runner / next task generator specification",
        "Keyword validation framework",
        "Monetization methodology",
    ]
    for fragment in required_queue_items:
        if fragment not in queue_text:
            failures.append(f"Work Queue V1 must contain queue item fragment: {fragment}")

    forbidden_active_status_values = [
        "status: publish_ready",
        "status: public_launch_ready",
        "status: monetization_approved",
        "status: operator_accepted",
        "status: approved_for_publish",
        "queue_status: publish_ready",
        "queue_status: public_launch_ready",
        "queue_status: monetization_approved",
        "queue_status: operator_accepted",
        "queue_status: approved_for_publish",
        "publish_readiness_status: publish_ready",
        "public_launch_status: public_launch_ready",
        "monetization_status: monetization_approved",
        "operator_acceptance_status: accepted",
    ]
    lower_queue_text = queue_text.lower()
    for fragment in forbidden_active_status_values:
        if fragment in lower_queue_text:
            failures.append(f"Work Queue V1 must not contain active forbidden status: {fragment}")

    forbidden_data_claims = [
        "analytics_status: connected",
        "search_console_status: connected",
        "user_feedback_status: collected",
        "ranking_status: available",
        "traffic_status: available",
        "conversion_status: available",
        "revenue_status: available",
    ]
    for fragment in forbidden_data_claims:
        if fragment in lower_queue_text:
            failures.append(f"Work Queue V1 must not claim live data: {fragment}")

    required_runner_fragments = [
        "runner_spec_status: specification_only_not_implemented",
        "runtime_status: not_implemented",
        "queue_execution_status: not_live",
        "This specification does not implement runtime execution.",
        "inspect_only",
        "validate_only",
        "propose_next_task",
        "generate_operator_packet_candidate",
        "blocked_report_only",
        "future_execute_template_stage",
        "auto_publish",
        "auto_accept",
        "auto_monetize",
        "operator_decision_required_report",
        "no_safe_task_available_report",
        "human_gate_required: yes",
        "Never publish, accept, monetize, or connect live data.",
    ]
    for fragment in required_runner_fragments:
        if fragment not in runner_text:
            failures.append(f"Content Pipeline Runner Spec V1 must contain: {fragment}")

    required_generator_fragments = [
        "next_task_generator_spec_status: specification_only_not_implemented",
        "runtime_status: not_implemented",
        "queue_execution_status: not_live",
        "human_gate_required",
        "non_acceptance_guardrails",
        "forbidden data invention guardrail",
        "pending_human_operator_gate",
        "pending_human_operator_decision",
        "generate operator decision required report",
        "blocked_until_human_operator_decision",
        "keine erfundenen SEO-, Analytics-, Ranking-, Traffic-, CTR-, Conversion-, Revenue-, Nutzerfeedback- oder Source-Freshness-Daten",
    ]
    for fragment in required_generator_fragments:
        if fragment not in generator_text:
            failures.append(f"Next Task Generator Spec V1 must contain: {fragment}")

    forbidden_runner_generator_markers = [
        "runtime_status: implemented",
        "runtime_status: active",
        "queue_execution_status: live",
        "analytics_status: connected",
        "search_console_status: connected",
        "user_feedback_status: collected",
        "ranking_status: available",
        "traffic_status: available",
        "conversion_status: available",
        "revenue_status: available",
        "monetization_status: approved",
        "operator_acceptance_status: accepted",
        "publish_readiness_status: publish_ready",
        "public_launch_status: public_launch_ready",
    ]
    lower_runner_generator_text = (runner_text + "\n" + generator_text).lower()
    for fragment in forbidden_runner_generator_markers:
        if fragment in lower_runner_generator_text:
            failures.append(
                "Runner/Generator specs must not contain active forbidden marker: "
                f"{fragment}"
            )

    return count


def validate_website_information_architecture_internal_preview_v1(
    failures: list[str],
) -> int:
    required_paths = [
        WEBSITE_PREVIEW_DIR / "README.md",
        WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1_PATH,
        WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY_PATH,
        STATIC_PREVIEW_SPEC_INTERNAL_ONLY_PATH,
        VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY_PATH,
        ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY_PATH,
        ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY_PATH,
        STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY_PATH,
        STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY_PATH,
        STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY_PATH,
    ]
    count = 0
    for path in required_paths:
        if not path.exists():
            failures.append(f"Missing website preview artifact: {path.relative_to(ROOT)}")
        else:
            count += 1

    if count != len(required_paths):
        return count

    readme_text = (WEBSITE_PREVIEW_DIR / "README.md").read_text(encoding="utf-8")
    ia_text = WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1_PATH.read_text(
        encoding="utf-8"
    )
    review_packet_text = WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY_PATH.read_text(
        encoding="utf-8"
    )
    static_preview_spec_text = STATIC_PREVIEW_SPEC_INTERNAL_ONLY_PATH.read_text(
        encoding="utf-8"
    )
    visual_design_system_spec_text = (
        VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY_PATH.read_text(encoding="utf-8")
    )
    accessibility_requirements_text = (
        ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY_PATH.read_text(
            encoding="utf-8"
        )
    )
    accessibility_review_packet_text = (
        ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY_PATH.read_text(
            encoding="utf-8"
        )
    )
    static_preview_skeleton_spec_text = (
        STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY_PATH.read_text(encoding="utf-8")
    )
    static_preview_skeleton_decision_packet_text = (
        STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY_PATH.read_text(
            encoding="utf-8"
        )
    )
    static_preview_skeleton_review_packet_text = (
        STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY_PATH.read_text(
            encoding="utf-8"
        )
    )
    queue_text = WORK_QUEUE_V1_PATH.read_text(encoding="utf-8")

    required_ia_fragments = [
        "artifact_status: internal_preview_structure_defined",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "internal preview only",
        "Proposed Internal Website Structure",
        "Internal Preview Navigation",
        "Page Template Definitions",
        "Mapping to Current Batch Articles",
        "Senior UX / Accessibility Principles",
        "Forbidden Outcomes",
        "Build-Mode-Exit Note",
        "no public launch",
        "no publish article",
        "no publish candidate status",
        "no approved_for_publish",
        "no Operator Acceptance",
        "no monetization",
        "no affiliate",
        "no ads",
        "no Analytics/Search Console connection",
        "no blocked claim unlock",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_ia_fragments:
        if fragment not in ia_text:
            failures.append(
                "Website IA internal preview V1 must contain required fragment: "
                f"{fragment}"
            )

    required_readme_fragments = [
        "interne Website-Informationsarchitektur",
        "Keine Publish Readiness",
        "Keine Operator Acceptance",
        "Keine Monetarisierung",
        "Blockierte Claims bleiben blockiert",
    ]
    for fragment in required_readme_fragments:
        if fragment not in readme_text:
            failures.append(f"Website preview README must contain: {fragment}")

    required_review_packet_fragments = [
        "review_packet_status: prepared_for_human_operator_review_not_acceptance",
        "linked_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Review Checklist",
        "## Human Operator Review Questions",
        "## Findings",
        "## Allowed Outcomes",
        "## Forbidden Outcomes",
        "STATIC_PREVIEW_SPEC_INTERNAL_ONLY",
        "SHO-WEBPREVIEW-IA-001",
        "SHO-WEBPREVIEW-IA-002",
        "SHO-WEBPREVIEW-IA-003",
        "no website runtime",
        "no static site launch",
        "no article text",
        "no new claims",
        "no new sources",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_review_packet_fragments:
        if fragment not in review_packet_text:
            failures.append(
                "Website Preview Review Packet Internal Only must contain: "
                f"{fragment}"
            )

    required_static_preview_spec_fragments = [
        "static_preview_spec_id: STATIC-PREVIEW-SPEC-INTERNAL-ONLY",
        "linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "linked_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md",
        "spec_status: specification_only_not_implemented",
        "preview_runtime_status: not_implemented",
        "static_generation_status: not_implemented",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Current Baseline",
        "## Static Preview Concept",
        "## Template-Level Specification",
        "## Content State Mapping Rules",
        "## Status Banner Requirements",
        "## Human Operator Decisions Needed Before Implementation",
        "## Allowed Outcomes",
        "## Forbidden Outcomes",
        "VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY",
        "These files are not created by this patch.",
        "no HTML/CSS/JS preview files",
        "no new claims",
        "no new sources",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_static_preview_spec_fragments:
        if fragment not in static_preview_spec_text:
            failures.append(
                "Static Preview Spec Internal Only must contain: " f"{fragment}"
            )

    required_visual_design_spec_fragments = [
        "visual_design_system_spec_id: VISUAL-DESIGN-SYSTEM-SPEC-INTERNAL-ONLY",
        "linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md",
        "linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "linked_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md",
        "spec_status: specification_only_not_implemented",
        "design_runtime_status: not_implemented",
        "asset_generation_status: not_implemented",
        "css_generation_status: not_implemented",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Current Baseline",
        "## Design Principles",
        "## Visual Identity Direction",
        "## Typography Specification",
        "## Color System Specification",
        "## Layout and Spacing Specification",
        "## Component Specification",
        "## Status Banner Visual Rules",
        "## Content State Visual Mapping",
        "## Accessibility / Senior UX Requirements",
        "## Anti-Patterns",
        "## Human Operator Decisions Needed Before Implementation",
        "## Allowed Outcomes",
        "## Forbidden Outcomes",
        "ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY",
        "Do not create CSS.",
        "no HTML/CSS/JS files",
        "no design asset files",
        "no new claims",
        "no new sources",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_visual_design_spec_fragments:
        if fragment not in visual_design_system_spec_text:
            failures.append(
                "Visual Design System Spec Internal Only must contain: "
                f"{fragment}"
            )

    required_accessibility_requirements_fragments = [
        "accessibility_requirements_id: ACCESSIBILITY-REQUIREMENTS-STATIC-PREVIEW-INTERNAL-ONLY",
        "linked_visual_design_system_spec: docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md",
        "linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md",
        "linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "linked_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md",
        "spec_status: specification_only_not_implemented",
        "accessibility_testing_status: not_performed",
        "wcag_conformance_status: not_claimed",
        "preview_runtime_status: not_implemented",
        "static_generation_status: not_implemented",
        "css_generation_status: not_implemented",
        "asset_generation_status: not_implemented",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Current Baseline",
        "## Accessibility Requirement Categories",
        "## Testable Requirements Table",
        "## Status Banner Accessibility Rules",
        "## Content-State Accessibility Mapping",
        "## Senior-UX Writing and Label Rules",
        "## Later Manual Review Checklist",
        "## Forbidden Outcomes",
        "## Human Operator Decisions Needed Before Implementation",
        "## Allowed Outcomes",
        "ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY",
        "SHO-A11Y-SP-001",
        "SHO-A11Y-SP-017",
        "No WCAG compliance/conformance claim exists.",
        "no WCAG conformance claim",
        "no accessibility certification claim",
        "no HTML/CSS/JS files",
        "no design asset files",
        "no new claims",
        "no new sources",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_accessibility_requirements_fragments:
        if fragment not in accessibility_requirements_text:
            failures.append(
                "Accessibility Requirements Static Preview Internal Only must contain: "
                f"{fragment}"
            )

    required_accessibility_review_packet_fragments = [
        "accessibility_review_packet_id: ACCESSIBILITY-REQUIREMENTS-REVIEW-PACKET-INTERNAL-ONLY",
        "linked_accessibility_requirements_spec: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md",
        "linked_visual_design_system_spec: docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md",
        "linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md",
        "linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "linked_website_preview_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md",
        "review_packet_status: prepared_for_human_operator_review_not_acceptance",
        "accessibility_testing_status: not_performed",
        "wcag_conformance_status: not_claimed",
        "preview_runtime_status: not_implemented",
        "static_generation_status: not_implemented",
        "css_generation_status: not_implemented",
        "asset_generation_status: not_implemented",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Reviewed Artifact Summary",
        "## Scope Confirmation",
        "## Requirements Coverage Review",
        "## Findings",
        "## Human Operator Review Questions",
        "## Allowed Outcomes",
        "## Forbidden Outcomes",
        "## Recommended Next Step",
        "SHO-A11Y-REVIEW-001",
        "SHO-A11Y-REVIEW-004",
        "STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY",
        "This packet does not perform tests.",
        "no accessibility tests",
        "no WCAG conformance claim",
        "no accessibility certification claim",
        "no HTML/CSS/JS files",
        "no design asset files",
        "no new claims",
        "no new sources",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_accessibility_review_packet_fragments:
        if fragment not in accessibility_review_packet_text:
            failures.append(
                "Accessibility Requirements Review Packet Internal Only must contain: "
                f"{fragment}"
            )

    required_static_preview_skeleton_spec_fragments = [
        "static_preview_skeleton_spec_id: STATIC-PREVIEW-SKELETON-SPEC-INTERNAL-ONLY",
        "linked_accessibility_review_packet: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md",
        "linked_accessibility_requirements_spec: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md",
        "linked_visual_design_system_spec: docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md",
        "linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md",
        "linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "linked_website_preview_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md",
        "spec_status: specification_only_not_implemented",
        "skeleton_runtime_status: not_implemented",
        "skeleton_generation_status: not_implemented",
        "preview_runtime_status: not_implemented",
        "static_generation_status: not_implemented",
        "html_generation_status: not_implemented",
        "css_generation_status: not_implemented",
        "js_generation_status: not_implemented",
        "asset_generation_status: not_implemented",
        "accessibility_testing_status: not_performed",
        "wcag_conformance_status: not_claimed",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Current Baseline",
        "## Skeleton Concept",
        "## Planning-Only Future Directory Layout",
        "## Required Future Skeleton Pages",
        "## Template-to-Skeleton Mapping",
        "## Mandatory Status Banner Contract",
        "## Content-State Skeleton Rules",
        "## Accessibility Carry-Forward Requirements",
        "## Visual Design Carry-Forward Requirements",
        "## Implementation Guardrails for Later Skeleton Patch",
        "## Later Manual Review Checklist",
        "## Human Operator Decisions Needed Before Implementation",
        "## Allowed Outcomes",
        "## Forbidden Outcomes",
        "## Recommended Next Step",
        "These files are not created by this patch.",
        "STATIC_PREVIEW_SKELETON_IMPLEMENTATION_DECISION_PACKET_INTERNAL_ONLY",
        "no HTML/CSS/JS files",
        "no design asset files",
        "no new claims",
        "no new sources",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_static_preview_skeleton_spec_fragments:
        if fragment not in static_preview_skeleton_spec_text:
            failures.append(
                "Static Preview Skeleton Spec Internal Only must contain: "
                f"{fragment}"
            )

    required_static_preview_skeleton_decision_packet_fragments = [
        "decision_packet_id: STATIC-PREVIEW-SKELETON-IMPLEMENTATION-DECISION-PACKET-INTERNAL-ONLY",
        "linked_skeleton_spec: docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md",
        "linked_accessibility_review_packet: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_REVIEW_PACKET_INTERNAL_ONLY.md",
        "linked_accessibility_requirements_spec: docs/operations/website_preview/ACCESSIBILITY_REQUIREMENTS_FOR_STATIC_PREVIEW_INTERNAL_ONLY.md",
        "linked_visual_design_system_spec: docs/operations/website_preview/VISUAL_DESIGN_SYSTEM_SPEC_INTERNAL_ONLY.md",
        "linked_static_preview_spec: docs/operations/website_preview/STATIC_PREVIEW_SPEC_INTERNAL_ONLY.md",
        "linked_ia_artifact: docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "linked_website_preview_review_packet: docs/operations/website_preview/WEBSITE_PREVIEW_REVIEW_PACKET_INTERNAL_ONLY.md",
        "decision_packet_status: prepared_for_human_operator_decision_not_acceptance",
        "implementation_decision_status: pending_human_operator_decision",
        "skeleton_runtime_status: not_implemented",
        "skeleton_generation_status: not_implemented",
        "preview_runtime_status: not_implemented",
        "static_generation_status: not_implemented",
        "html_generation_status: not_implemented",
        "css_generation_status: not_implemented",
        "js_generation_status: not_implemented",
        "asset_generation_status: not_implemented",
        "accessibility_testing_status: not_performed",
        "wcag_conformance_status: not_claimed",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Decision Context",
        "## Decision Needed",
        "## Recommended Safe Default",
        "## Proposed Allowed Scope If Approved Later",
        "## Mandatory Future Implementation Constraints",
        "## Brief Rendering Decision",
        "## JS Decision",
        "## Review and Acceptance After Later Implementation",
        "## Risk Register",
        "## Human Operator Decision Questions",
        "## Allowed Outcomes",
        "## Forbidden Outcomes",
        "## Recommended Next Step",
        "approve_internal_html_css_skeleton_no_js",
        "js_forbidden_first_skeleton",
        "shell_only_no_article_body",
        "HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION",
        "STATIC_PREVIEW_SKELETON_REVIEW_PACKET_INTERNAL_ONLY",
        "These files are not created by this patch.",
        "no implementation approved",
        "no Human Operator decision simulated",
        "no HTML/CSS/JS files",
        "no design asset files",
        "no new claims",
        "no new sources",
        "no WhatsApp block/report UI instructions",
    ]
    for fragment in required_static_preview_skeleton_decision_packet_fragments:
        if fragment not in static_preview_skeleton_decision_packet_text:
            failures.append(
                "Static Preview Skeleton Implementation Decision Packet Internal Only "
                f"must contain: {fragment}"
            )

    required_static_preview_skeleton_review_packet_fragments = [
        "review_packet_id: STATIC-PREVIEW-SKELETON-REVIEW-PACKET-INTERNAL-ONLY",
        "linked_operator_decision: docs/operations/operator_decisions/HUMAN_OPERATOR_DECISION_STATIC_PREVIEW_SKELETON_IMPLEMENTATION.md",
        "linked_skeleton_spec: docs/operations/website_preview/STATIC_PREVIEW_SKELETON_SPEC_INTERNAL_ONLY.md",
        "linked_skeleton_readme: preview_static_internal/README.md",
        "review_packet_status: prepared_for_human_operator_review_not_acceptance",
        "skeleton_review_status: reviewed_internal_only_not_accepted",
        "skeleton_runtime_status: not_implemented",
        "static_generation_status: not_implemented",
        "js_generation_status: not_implemented",
        "asset_generation_status: not_implemented",
        "accessibility_testing_status: not_performed",
        "wcag_conformance_status: not_claimed",
        "public_launch_status: not_ready",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "monetization_status: not_approved",
        "analytics_status: not_connected",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "## Purpose",
        "## Explicit Non-Acceptance",
        "## Reviewed Files",
        "## Approved Scope Compliance Review",
        "## Page-by-Page Review",
        "## Brief State Review",
        "## Accessibility / Senior-UX Review Status",
        "## Governance Cleanup Review",
        "## Findings",
        "## Residual Risks",
        "## Allowed Outcomes",
        "## Forbidden Outcomes",
        "## Recommended Next Step",
        "HUMAN_OPERATOR_REVIEW_STATIC_PREVIEW_SKELETON_INTERNAL_ONLY",
        "SHO-SKEL-REVIEW-001",
        "SHO-SKEL-REVIEW-005",
        "shell_only_no_article_body",
        "SHO-CLAIM-007 remains blocked",
        "no article body",
        "No accessibility test performed.",
        "No WCAG conformance claimed.",
    ]
    for fragment in required_static_preview_skeleton_review_packet_fragments:
        if fragment not in static_preview_skeleton_review_packet_text:
            failures.append(
                "Static Preview Skeleton Review Packet Internal Only must contain: "
                f"{fragment}"
            )

    required_queue_fragments = [
        "queue_item_id: CQ-V1-004",
        "docs/operations/website_preview/WEBSITE_INFORMATION_ARCHITECTURE_INTERNAL_PREVIEW_V1.md",
        "allowed_next_action: prepare_internal_preview_review_packet_only",
        "status: completed_internal_planning",
        "activate_public_launch",
        "publish_article",
        "connect_analytics",
    ]
    for fragment in required_queue_fragments:
        if fragment not in queue_text:
            failures.append(f"Work Queue V1 CQ-V1-004 must contain: {fragment}")

    forbidden_active_markers = [
        "public_launch_status: ready",
        "public_launch_status: launched",
        "publish_readiness_status: publish_ready",
        "operator_acceptance_status: accepted",
        "monetization_status: approved",
        "analytics_status: connected",
        "search_console_status: connected",
        "user_feedback_status: collected",
        "publish_candidate: true",
        "approved_for_publish: true",
        "publish_ready: true",
        "operator_accepted: true",
        "public_launch_ready: true",
        "monetization_approved: true",
    ]
    lower_ia_text = ia_text.lower()
    for fragment in forbidden_active_markers:
        if fragment in lower_ia_text:
            failures.append(
                "Website IA internal preview V1 must not contain active forbidden marker: "
                f"{fragment}"
            )
    lower_review_packet_text = review_packet_text.lower()
    for fragment in forbidden_active_markers:
        if fragment in lower_review_packet_text:
            failures.append(
                "Website Preview Review Packet Internal Only must not contain active forbidden marker: "
                f"{fragment}"
            )
    forbidden_static_preview_active_markers = forbidden_active_markers + [
        "preview_runtime_status: implemented",
        "static_generation_status: implemented",
        "public_launch_ready: true",
        "publish_ready: true",
    ]
    lower_static_preview_spec_text = static_preview_spec_text.lower()
    for fragment in forbidden_static_preview_active_markers:
        if fragment in lower_static_preview_spec_text:
            failures.append(
                "Static Preview Spec Internal Only must not contain active forbidden marker: "
                f"{fragment}"
            )
    forbidden_visual_design_active_markers = forbidden_active_markers + [
        "design_runtime_status: implemented",
        "asset_generation_status: implemented",
        "css_generation_status: implemented",
        "public_launch_ready: true",
        "publish_ready: true",
    ]
    lower_visual_design_system_spec_text = visual_design_system_spec_text.lower()
    for fragment in forbidden_visual_design_active_markers:
        if fragment in lower_visual_design_system_spec_text:
            failures.append(
                "Visual Design System Spec Internal Only must not contain active forbidden marker: "
                f"{fragment}"
            )
    forbidden_accessibility_requirements_active_markers = forbidden_active_markers + [
        "accessibility_testing_status: performed",
        "wcag_conformance_status: claimed",
        "wcag_conformance_status: compliant",
        "preview_runtime_status: implemented",
        "static_generation_status: implemented",
        "css_generation_status: implemented",
        "asset_generation_status: implemented",
        "public_launch_ready: true",
        "publish_ready: true",
    ]
    lower_accessibility_requirements_text = accessibility_requirements_text.lower()
    for fragment in forbidden_accessibility_requirements_active_markers:
        if fragment in lower_accessibility_requirements_text:
            failures.append(
                "Accessibility Requirements Static Preview Internal Only must not contain active forbidden marker: "
                f"{fragment}"
            )
    lower_accessibility_review_packet_text = accessibility_review_packet_text.lower()
    for fragment in forbidden_accessibility_requirements_active_markers:
        if fragment in lower_accessibility_review_packet_text:
            failures.append(
                "Accessibility Requirements Review Packet Internal Only must not contain active forbidden marker: "
                f"{fragment}"
            )
    forbidden_static_preview_skeleton_active_markers = forbidden_active_markers + [
        "skeleton_runtime_status: implemented",
        "skeleton_generation_status: implemented",
        "preview_runtime_status: implemented",
        "static_generation_status: implemented",
        "html_generation_status: implemented",
        "css_generation_status: implemented",
        "js_generation_status: implemented",
        "asset_generation_status: implemented",
        "accessibility_testing_status: performed",
        "wcag_conformance_status: claimed",
        "wcag_conformance_status: compliant",
        "public_launch_ready: true",
        "publish_ready: true",
    ]
    lower_static_preview_skeleton_spec_text = static_preview_skeleton_spec_text.lower()
    for fragment in forbidden_static_preview_skeleton_active_markers:
        if fragment in lower_static_preview_skeleton_spec_text:
            failures.append(
                "Static Preview Skeleton Spec Internal Only must not contain active forbidden marker: "
                f"{fragment}"
            )
    forbidden_static_preview_skeleton_decision_packet_active_markers = (
        forbidden_static_preview_skeleton_active_markers
        + [
            "implementation_decision_status: approved",
            "implementation_decision_status: accepted",
        ]
    )
    lower_static_preview_skeleton_decision_packet_text = (
        static_preview_skeleton_decision_packet_text.lower()
    )
    for fragment in forbidden_static_preview_skeleton_decision_packet_active_markers:
        if fragment in lower_static_preview_skeleton_decision_packet_text:
            failures.append(
                "Static Preview Skeleton Implementation Decision Packet Internal Only "
                "must not contain active forbidden marker: "
                f"{fragment}"
            )
    forbidden_static_preview_skeleton_review_packet_active_markers = (
        forbidden_static_preview_skeleton_active_markers
        + [
            "skeleton_review_status: accepted",
            "publish_readiness_status: publish_candidate",
            "publish_readiness_status: approved_for_publish",
            "monetization_status: approved",
        ]
    )
    lower_static_preview_skeleton_review_packet_text = (
        static_preview_skeleton_review_packet_text.lower()
    )
    for fragment in forbidden_static_preview_skeleton_review_packet_active_markers:
        if fragment in lower_static_preview_skeleton_review_packet_text:
            failures.append(
                "Static Preview Skeleton Review Packet Internal Only "
                "must not contain active forbidden marker: "
                f"{fragment}"
            )

    forbidden_data_claims = [
        "real ranking data",
        "real traffic data",
        "real revenue data",
        "real conversion data",
        "real user feedback data",
        "ranking_status: available",
        "traffic_status: available",
        "revenue_status: available",
        "conversion_status: available",
    ]
    for fragment in forbidden_data_claims:
        if fragment in lower_ia_text:
            failures.append(
                "Website IA internal preview V1 must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_review_packet_text:
            failures.append(
                "Website Preview Review Packet Internal Only must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_static_preview_spec_text:
            failures.append(
                "Static Preview Spec Internal Only must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_visual_design_system_spec_text:
            failures.append(
                "Visual Design System Spec Internal Only must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_accessibility_requirements_text:
            failures.append(
                "Accessibility Requirements Static Preview Internal Only must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_accessibility_review_packet_text:
            failures.append(
                "Accessibility Requirements Review Packet Internal Only must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_static_preview_skeleton_spec_text:
            failures.append(
                "Static Preview Skeleton Spec Internal Only must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_static_preview_skeleton_decision_packet_text:
            failures.append(
                "Static Preview Skeleton Implementation Decision Packet Internal Only "
                "must not claim real metric data: "
                f"{fragment}"
            )
        if fragment in lower_static_preview_skeleton_review_packet_text:
            failures.append(
                "Static Preview Skeleton Review Packet Internal Only "
                "must not claim real metric data: "
                f"{fragment}"
            )

    forbidden_design_asset_patterns = [
        "*.css",
        "*.js",
        "*.html",
        "*.png",
        "*.svg",
        "*.jpg",
        "*.jpeg",
        "*.webp",
    ]
    for pattern in forbidden_design_asset_patterns:
        for path in WEBSITE_PREVIEW_DIR.rglob(pattern):
            failures.append(
                "Visual Design System Spec Internal Only must not create design/runtime asset: "
                f"{path.relative_to(ROOT)}"
            )

    return count


def validate_static_preview_skeleton_internal_only(failures: list[str]) -> int:
    count = 0
    for path in PREVIEW_STATIC_INTERNAL_FILES:
        if not path.exists():
            failures.append(f"Missing static preview skeleton file: {path.relative_to(ROOT)}")
        else:
            count += 1

    if not PREVIEW_STATIC_INTERNAL_DIR.exists():
        return count

    approved_paths = {path.resolve() for path in PREVIEW_STATIC_INTERNAL_FILES}
    for path in PREVIEW_STATIC_INTERNAL_DIR.rglob("*"):
        if not path.is_file():
            continue
        if path.resolve() not in approved_paths:
            failures.append(
                "Static Preview Skeleton Internal Only contains unapproved file: "
                f"{path.relative_to(ROOT)}"
            )

    forbidden_patterns = [
        "*.js",
        "*.png",
        "*.svg",
        "*.jpg",
        "*.jpeg",
        "*.webp",
        "*.gif",
        "*.ico",
        "package.json",
        "package-lock.json",
        "vite.config.*",
        "webpack.config.*",
        "rollup.config.*",
        "*.map",
        "robots.txt",
        "sitemap.xml",
    ]
    for pattern in forbidden_patterns:
        for path in PREVIEW_STATIC_INTERNAL_DIR.rglob(pattern):
            failures.append(
                "Static Preview Skeleton Internal Only must not contain forbidden file: "
                f"{path.relative_to(ROOT)}"
            )

    required_html_fragments = [
        "internal_only",
        "not_public",
        "publish_readiness_status: not_ready",
        "operator_acceptance_status: not_accepted",
        "public_launch_status: not_ready",
        "analytics_status: not_connected",
        "monetization_status: not_approved",
        "search_console_status: not_connected",
        "user_feedback_status: not_collected",
        "accessibility_testing_status: not_performed",
        "wcag_conformance_status: not_claimed",
    ]
    forbidden_active_html_markers = [
        "publish_readiness_status: publish_candidate",
        "publish_readiness_status: approved_for_publish",
        "public_launch_status: ready",
        "public_launch_status: launched",
        "operator_acceptance_status: accepted",
        "analytics_status: connected",
        "search_console_status: connected",
        "user_feedback_status: collected",
        "wcag_conformance_status: claimed",
        "wcag_conformance_status: compliant",
        "accessibility_testing_status: performed",
    ]
    forbidden_html_fragments = [
        "<script",
        "<form",
        "analytics script",
        "tracking code",
        "search console verification",
        "contact form",
        "newsletter form",
        "affiliate block",
        "ads block",
        "product recommendation block",
        "whatsapp block/report ui instructions",
        "http://",
        "https://",
    ]

    for path in PREVIEW_STATIC_INTERNAL_HTML_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        lower_text = text.lower()
        for fragment in required_html_fragments:
            if fragment not in text:
                failures.append(
                    f"Static Preview Skeleton page {path.relative_to(ROOT)} "
                    f"must contain: {fragment}"
                )
        for fragment in forbidden_active_html_markers:
            if fragment in lower_text:
                failures.append(
                    f"Static Preview Skeleton page {path.relative_to(ROOT)} "
                    f"must not contain active forbidden marker: {fragment}"
                )
        for fragment in forbidden_html_fragments:
            if fragment in lower_text:
                failures.append(
                    f"Static Preview Skeleton page {path.relative_to(ROOT)} "
                    f"must not contain forbidden fragment: {fragment}"
                )

    brief_002_path = PREVIEW_STATIC_INTERNAL_DIR / "articles/brief-002-preview.html"
    if brief_002_path.exists():
        brief_002_text = brief_002_path.read_text(encoding="utf-8")
        required_brief_002_fragments = [
            "shell_only_no_article_body",
            "final_article_candidate_prepared_not_publish_ready",
            "no article body",
            "SHO-CLAIM-007 remains blocked",
        ]
        for fragment in required_brief_002_fragments:
            if fragment not in brief_002_text:
                failures.append(
                    "Static Preview Skeleton Brief 002 shell must contain: "
                    f"{fragment}"
                )

    if (PREVIEW_STATIC_INTERNAL_DIR / "styles.css").exists():
        css_text = (PREVIEW_STATIC_INTERNAL_DIR / "styles.css").read_text(
            encoding="utf-8"
        )
        lower_css_text = css_text.lower()
        for fragment in ["@import", "http://", "https://", "url("]:
            if fragment in lower_css_text:
                failures.append(
                    "Static Preview Skeleton styles.css must not contain external "
                    f"dependency marker: {fragment}"
                )
        for fragment in [
            ".status-banner",
            "@media print",
            "@media (max-width:",
            ":focus",
        ]:
            if fragment not in css_text:
                failures.append(
                    "Static Preview Skeleton styles.css must contain: "
                    f"{fragment}"
                )

    source_text = Path(__file__).read_text(encoding="utf-8")
    required_summary_labels = [
        "Content Pipeline V1 files",
        "Website Preview V1 files",
    ]
    forbidden_summary_labels = [
        "Content Pipeline Contract and Work Queue V1 " + "files",
        "Website Information Architecture Internal Preview V1 " + "files",
    ]
    for fragment in required_summary_labels:
        if fragment not in source_text:
            failures.append(f"Validator summary label must contain: {fragment}")
    for fragment in forbidden_summary_labels:
        if fragment in source_text:
            failures.append(f"Validator summary label must not contain old label: {fragment}")

    return count


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
    accessibility_review_brief_002_count = validate_accessibility_review_brief_002(failures)
    final_source_metadata_review_brief_002_count = validate_final_source_metadata_review_brief_002(failures)
    mvp_operational_start_plan_count = validate_mvp_operational_start_plan(failures)
    roadmap_mvp_2026_count = validate_roadmap_mvp_2026(failures)
    article_readiness_dashboard_count = validate_article_readiness_dashboard(failures)
    content_quality_feedback_loop_count = validate_content_quality_feedback_loop_baseline(failures)
    user_feedback_intake_protocol_count = validate_user_feedback_intake_protocol_baseline(failures)
    content_quality_scorecard_template_count = validate_content_quality_scorecard_template_batch_01(failures)
    final_article_candidate_brief_002_count = validate_final_article_candidate_brief_002(failures)
    applied_scorecard_brief_002_count = validate_applied_scorecard_brief_002(failures)
    human_operator_review_packet_final_article_candidate_brief_002_count = (
        validate_human_operator_review_packet_final_article_candidate_brief_002(failures)
    )
    content_pipeline_contract_and_work_queue_v1_count = (
        validate_content_pipeline_contract_and_work_queue_v1(failures)
    )
    website_information_architecture_internal_preview_v1_count = (
        validate_website_information_architecture_internal_preview_v1(failures)
    )
    static_preview_skeleton_internal_only_count = (
        validate_static_preview_skeleton_internal_only(failures)
    )

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
    print(f"- Batch 01 dedicated accessibility review Brief 002 files: {accessibility_review_brief_002_count}")
    print(f"- Batch 01 final source metadata review Brief 002 files: {final_source_metadata_review_brief_002_count}")
    print(f"- Batch 01 MVP operational start plan files: {mvp_operational_start_plan_count}")
    print(f"- Batch 01 MVP roadmap files: {roadmap_mvp_2026_count}")
    print(f"- Batch 01 article readiness dashboard files: {article_readiness_dashboard_count}")
    print(f"- Batch 01 content quality feedback loop baseline files: {content_quality_feedback_loop_count}")
    print(f"- Batch 01 user feedback intake protocol baseline files: {user_feedback_intake_protocol_count}")
    print(f"- Batch 01 content quality scorecard template files: {content_quality_scorecard_template_count}")
    print(f"- Batch 01 final article candidate Brief 002 files: {final_article_candidate_brief_002_count}")
    print(f"- Batch 01 applied scorecard Brief 002 files: {applied_scorecard_brief_002_count}")
    print(
        "- Batch 01 Human Operator review packet Final Article Candidate Brief 002 files: "
        f"{human_operator_review_packet_final_article_candidate_brief_002_count}"
    )
    print(
        "- Content Pipeline V1 files: "
        f"{content_pipeline_contract_and_work_queue_v1_count}"
    )
    print(
        "- Website Preview V1 files: "
        f"{website_information_architecture_internal_preview_v1_count}"
    )
    print(
        "- Static Preview Skeleton Internal Only files: "
        f"{static_preview_skeleton_internal_only_count}"
    )
    print("- YAML/frontmatter parsing: dependency-free and text-based")
    return 0


if __name__ == "__main__":
    sys.exit(main())
