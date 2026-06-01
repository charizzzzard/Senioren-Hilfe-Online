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


def fail_if_missing(path: Path, failures: list[str]) -> str:
    if not path.exists():
        failures.append(f"Missing required file: {path.relative_to(ROOT).as_posix()}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    failures: list[str] = []

    registry_text = fail_if_missing(STATUS_REGISTRY, failures)
    batch_text = fail_if_missing(BATCH_MANIFEST, failures)

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
            "approved_for_publish",
            "research_enriched",
        ]
        for fragment in forbidden_fragments:
            if fragment in batch_text:
                failures.append(f"MVP_BATCH_01.yaml must not contain: {fragment}")

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
    print("- No approved_for_publish or research_enriched transition detected")
    print("- YAML parsing: dependency-free and text-based skeleton")
    return 0


if __name__ == "__main__":
    sys.exit(main())
