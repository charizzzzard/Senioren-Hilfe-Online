#!/usr/bin/env python3
"""Validate the canonical release state and non-indexable staging contract."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
RELEASE_STATE_PATH = ROOT / "docs/operations/RELEASE_STATE_V1.yaml"
WORKFLOW_PATH = ROOT / ".github/workflows/deploy-pages.yml"
PUBLIC_SITE = ROOT / "public_site"
NEXT_ACTION = "implement_and_run_external_pages_verifier"

ROOT_README = ROOT / "README.md"
HANDOFF = ROOT / "external_review_packet/HANDOFF_LATEST_CONTEXT.md"
DASHBOARD = ROOT / "docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md"
WORK_QUEUE = ROOT / "docs/operations/content_pipeline/WORK_QUEUE_V1.yaml"
PUBLIC_README = PUBLIC_SITE / "README.md"

TRACKING_SIGNATURES = {
    "googletagmanager": "Google Tag Manager",
    "google-analytics.com": "Google Analytics",
    "gtag(": "Google gtag",
    "analytics.js": "analytics.js",
    "matomo": "Matomo",
    "plausible.io/js": "Plausible",
    "cdn.segment.com": "Segment",
    "mixpanel": "Mixpanel",
    "fbq(": "Meta Pixel",
    "connect.facebook.net": "Meta tracking",
    "adsbygoogle": "Google Ads",
    "doubleclick.net": "DoubleClick",
    "amazon-adsystem": "Amazon Ads",
    "hotjar": "Hotjar",
    "clarity.ms/tag": "Microsoft Clarity",
}


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def add(failures: list[str], path: Path, cause: str) -> None:
    failures.append(f"{relative(path)}: {cause}")


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_minimal_yaml(path: Path) -> dict[str, Any]:
    """Parse the mappings and scalar lists used by RELEASE_STATE_V1.yaml."""

    raw_lines: list[tuple[int, str, int]] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if "\t" in raw:
            raise ValueError(f"line {number} contains a tab")
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        raw_lines.append((indent, stripped, number))

    if not raw_lines:
        raise ValueError("file is empty")

    def parse_block(index: int, indent: int) -> tuple[Any, int]:
        is_list = raw_lines[index][1].startswith("- ")
        container: Any = [] if is_list else {}

        while index < len(raw_lines):
            current_indent, text, number = raw_lines[index]
            if current_indent < indent:
                break
            if current_indent > indent:
                raise ValueError(f"line {number} has unexpected indentation")

            if is_list:
                if not text.startswith("- "):
                    raise ValueError(f"line {number} mixes a mapping into a list")
                item = text[2:].strip()
                if not item or ":" in item:
                    raise ValueError(
                        f"line {number} must be a non-empty scalar list item"
                    )
                container.append(scalar(item))
                index += 1
                continue

            if text.startswith("- ") or ":" not in text:
                raise ValueError(f"line {number} is not a key/value mapping")
            key, value = text.split(":", 1)
            key = key.strip()
            if not key or key in container:
                reason = "empty key" if not key else f"duplicate key {key!r}"
                raise ValueError(f"line {number} has {reason}")

            value = value.strip()
            if value:
                container[key] = scalar(value)
                index += 1
                continue

            index += 1
            if index >= len(raw_lines) or raw_lines[index][0] <= current_indent:
                container[key] = {}
                continue
            child_indent = raw_lines[index][0]
            child, index = parse_block(index, child_indent)
            container[key] = child

        return container, index

    parsed, next_index = parse_block(0, raw_lines[0][0])
    if next_index != len(raw_lines) or not isinstance(parsed, dict):
        raise ValueError("top-level YAML value must be one mapping")
    return parsed


def nested(data: dict[str, Any], dotted: str) -> Any:
    value: Any = data
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def expect(
    failures: list[str], data: dict[str, Any], dotted: str, expected: Any
) -> None:
    actual = nested(data, dotted)
    if actual != expected:
        add(
            failures,
            RELEASE_STATE_PATH,
            f"{dotted} must be {expected!r}; found {actual!r}",
        )


def require_fragments(
    failures: list[str], path: Path, text: str, fragments: list[str]
) -> None:
    for fragment in fragments:
        if fragment not in text:
            add(failures, path, f"missing required release-state marker: {fragment}")


def yaml_named_block(text: str, key: str, indent: int) -> str | None:
    """Return one indentation-delimited YAML mapping block as text."""

    lines = text.splitlines(keepends=True)
    marker = f"{' ' * indent}{key}:"
    start = next(
        (index for index, line in enumerate(lines) if line.rstrip() == marker),
        None,
    )
    if start is None:
        return None
    end = len(lines)
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if not line.strip():
            continue
        current_indent = len(line) - len(line.lstrip(" "))
        if current_indent <= indent:
            end = index
            break
    return "".join(lines[start:end])


class ResourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = {name.lower(): value for name, value in attrs if value is not None}
        for attribute in ("href", "src", "poster"):
            value = values.get(attribute)
            if value:
                self.references.append((attribute, value))
        for attribute in ("srcset", "imagesrcset"):
            value = values.get(attribute)
            if not value:
                continue
            for candidate in value.split(","):
                url = candidate.strip().split()[0] if candidate.strip() else ""
                if url:
                    self.references.append((attribute, url))


class RobotsMetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.robot_directives: list[set[str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag.lower() != "meta":
            return
        values = {
            name.lower(): (value or "").strip().lower() for name, value in attrs
        }
        if values.get("name") != "robots":
            return
        directives = {
            item.strip() for item in values.get("content", "").split(",") if item.strip()
        }
        self.robot_directives.append(directives)


def validate_release_yaml(failures: list[str]) -> None:
    if not RELEASE_STATE_PATH.exists():
        add(failures, RELEASE_STATE_PATH, "canonical release-state file does not exist")
        return

    text = RELEASE_STATE_PATH.read_text(encoding="utf-8")
    try:
        data = parse_minimal_yaml(RELEASE_STATE_PATH)
    except (OSError, UnicodeError, ValueError) as exc:
        add(failures, RELEASE_STATE_PATH, f"cannot parse deterministic YAML subset: {exc}")
        return

    for section in (
        "content_batch",
        "candidate",
        "release",
        "legal",
        "domain",
        "staging_verifier",
        "blocked_items",
    ):
        if section not in data:
            add(failures, RELEASE_STATE_PATH, f"missing required top-level section: {section}")

    expected_values = {
        "release_state_id": "SHO-RELEASE-STATE-V1",
        "candidate_id": "SHO-INTERNAL-CANDIDATE-001",
        "status_scope_version": "1.0",
        "content_batch.batch_id": "MVP_BATCH_01",
        "content_batch.current_stage": "claim_slots_mapped",
        "content_batch.operator_acceptance_status": "not_accepted",
        "candidate.publication_preparation_acceptance_status": "accepted",
        "candidate.content_scope_status": "locked",
        "candidate.publish_candidate_status": "corrected_after_acceptance_findings",
        "candidate.publish_readiness_status": "not_ready",
        "release.staging_status": "deployed_awaiting_repo_verifier",
        "release.launch_acceptance_status": "not_accepted",
        "release.public_launch_status": "not_ready",
        "release.indexing_status": "blocked",
        "release.analytics_status": "not_connected",
        "release.search_console_status": "not_connected",
        "release.monetization_status": "not_approved",
        "legal.pages_status": "completed_pending_external_legal_review",
        "legal.legal_approval_status": "not_approved",
        "domain.canonical_domain": "https://netzleicht.de",
        "domain.configuration_status": "externally_observed",
        "domain.observation_date": "2026-07-16",
        "domain.observation_evidence_status": "external_observation_not_yet_repo_verifier_output",
        "domain.individual_page_http_status": "unverified",
        "domain.custom_domain_repo_file_status": "no_cname_file_present",
        "staging_verifier.implementation_status": "implemented",
        "staging_verifier.workflow": ".github/workflows/deploy-pages.yml",
        "staging_verifier.deployment_environment": "github-pages",
        "staging_verifier.deployment_ref_policy": "main_only",
        "staging_verifier.runtime_result_source": "github_actions",
        "staging_verifier.report_artifact_name_pattern": "sho-release-verifier-*",
        "staging_verifier.latest_repo_verifier_result": "governed_by_github_actions_not_hardcoded",
        "current_allowed_next_action": NEXT_ACTION,
    }
    for dotted, expected_value in expected_values.items():
        expect(failures, data, dotted, expected_value)

    next_action_count = len(
        re.findall(r"(?m)^current_allowed_next_action\s*:", text)
    )
    if next_action_count != 1:
        add(
            failures,
            RELEASE_STATE_PATH,
            "must contain exactly one root current_allowed_next_action; "
            f"found {next_action_count}",
        )

    batch_acceptance = nested(data, "content_batch.operator_acceptance_status")
    candidate_acceptance = nested(
        data, "candidate.publication_preparation_acceptance_status"
    )
    launch_acceptance = nested(data, "release.launch_acceptance_status")
    if batch_acceptance == candidate_acceptance:
        add(
            failures,
            RELEASE_STATE_PATH,
            "Batch Acceptance must remain separate from Candidate Publication Preparation Acceptance",
        )
    if candidate_acceptance == launch_acceptance:
        add(
            failures,
            RELEASE_STATE_PATH,
            "Candidate Publication Preparation Acceptance must remain separate from Launch Acceptance",
        )

    scope = nested(data, "domain.observation_scope")
    if not isinstance(scope, list) or set(scope) != {
        "https_reachability",
        "robots_reachability",
    } or len(scope) != 2:
        add(
            failures,
            RELEASE_STATE_PATH,
            "domain.observation_scope must be limited to HTTPS and robots reachability",
        )

    blocked = nested(data, "blocked_items")
    if not isinstance(blocked, list):
        add(failures, RELEASE_STATE_PATH, "blocked_items must be a scalar list")
    else:
        for item in ("SHO-CLAIM-007", "SHO-SRC-004"):
            if item not in blocked:
                add(failures, RELEASE_STATE_PATH, f"blocked_items must retain {item}")

    if nested(data, "staging_verifier.verification_tag_pattern") is not None:
        add(
            failures,
            RELEASE_STATE_PATH,
            "staging_verifier.verification_tag_pattern is obsolete; Pages deployment is main-only",
        )
    if nested(data, "staging_verifier.trigger_modes") is not None:
        add(
            failures,
            RELEASE_STATE_PATH,
            "staging_verifier.trigger_modes is obsolete; use separate preflight and deployment modes",
        )

    preflight_modes = nested(data, "staging_verifier.preflight_trigger_modes")
    expected_preflight_modes = {
        "pull_request_to_main",
        "push_to_main",
        "workflow_dispatch",
    }
    if (
        not isinstance(preflight_modes, list)
        or len(preflight_modes) != len(expected_preflight_modes)
        or set(preflight_modes) != expected_preflight_modes
    ):
        add(
            failures,
            RELEASE_STATE_PATH,
            "staging_verifier.preflight_trigger_modes must contain exactly "
            "pull_request_to_main, push_to_main and workflow_dispatch",
        )

    deployment_modes = nested(data, "staging_verifier.deployment_trigger_modes")
    expected_deployment_modes = {
        "push_to_main",
        "workflow_dispatch_on_main",
    }
    if (
        not isinstance(deployment_modes, list)
        or len(deployment_modes) != len(expected_deployment_modes)
        or set(deployment_modes) != expected_deployment_modes
    ):
        add(
            failures,
            RELEASE_STATE_PATH,
            "staging_verifier.deployment_trigger_modes must contain exactly "
            "push_to_main and workflow_dispatch_on_main; tags, feature branches "
            "and pull requests must not deploy",
        )

    verifier_result = str(
        nested(data, "staging_verifier.latest_repo_verifier_result") or ""
    ).lower()
    positive_result = verifier_result in {
        "pass",
        "passed",
        "success",
        "successful",
        "verified",
    }
    verifier_reference = nested(
        data, "staging_verifier.latest_repo_verifier_output_reference"
    )
    if positive_result and not verifier_reference:
        add(
            failures,
            RELEASE_STATE_PATH,
            "positive repo verifier result requires a referenced GitHub Actions verifier output",
        )


def validate_workflow_contract(failures: list[str]) -> None:
    if not WORKFLOW_PATH.exists():
        add(failures, WORKFLOW_PATH, "Pages workflow does not exist")
        return

    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    on_block = yaml_named_block(text, "on", 0)
    jobs_block = yaml_named_block(text, "jobs", 0)
    if on_block is None:
        add(failures, WORKFLOW_PATH, "missing top-level on trigger mapping")
        return
    if jobs_block is None:
        add(failures, WORKFLOW_PATH, "missing top-level jobs mapping")
        return

    pull_request_block = yaml_named_block(on_block, "pull_request", 2)
    push_block = yaml_named_block(on_block, "push", 2)
    if pull_request_block is None or not re.search(
        r"(?m)^      - main\s*$", pull_request_block
    ):
        add(failures, WORKFLOW_PATH, "pull_request trigger must target main")
    if push_block is None or not re.search(r"(?m)^      - main\s*$", push_block):
        add(failures, WORKFLOW_PATH, "push trigger must target main")
    if not re.search(r"(?m)^  workflow_dispatch:\s*$", on_block):
        add(failures, WORKFLOW_PATH, "workflow_dispatch trigger must be present")
    if "verify-pages-*" in text:
        add(failures, WORKFLOW_PATH, "verify-pages-* tag trigger is obsolete")
    if re.search(r"(?m)^\s+tags(?:-ignore)?:\s*$", on_block):
        add(failures, WORKFLOW_PATH, "tag triggers are forbidden for Pages deployment")

    required_paths = (
        "public_site/**",
        "docs/operations/RELEASE_STATE_V1.yaml",
        "docs/operations/ARTICLE_READINESS_DASHBOARD_BATCH_01.md",
        "docs/operations/content_pipeline/WORK_QUEUE_V1.yaml",
        "external_review_packet/HANDOFF_LATEST_CONTEXT.md",
        "README.md",
        "scripts/validate_content_contracts.py",
        "scripts/validate_stage_transitions.py",
        "scripts/validate_release_state.py",
        ".github/workflows/deploy-pages.yml",
    )
    for trigger_name, trigger_block in (
        ("pull_request", pull_request_block),
        ("push", push_block),
    ):
        if trigger_block is None:
            continue
        for required_path in required_paths:
            if f'- "{required_path}"' not in trigger_block:
                add(
                    failures,
                    WORKFLOW_PATH,
                    f"{trigger_name} trigger missing required path filter: {required_path}",
                )

    job_names = re.findall(r"(?m)^  ([A-Za-z0-9_-]+):\s*$", jobs_block)
    if len(job_names) != 2 or set(job_names) != {"preflight", "deploy"}:
        add(
            failures,
            WORKFLOW_PATH,
            f"jobs must be exactly preflight and deploy; found {job_names!r}",
        )
    preflight_block = yaml_named_block(jobs_block, "preflight", 2)
    deploy_block = yaml_named_block(jobs_block, "deploy", 2)
    if preflight_block is None:
        add(failures, WORKFLOW_PATH, "preflight job is missing")
        return
    if deploy_block is None:
        add(failures, WORKFLOW_PATH, "deploy job is missing")
        return

    preflight_permissions = yaml_named_block(preflight_block, "permissions", 4)
    preflight_entries = (
        re.findall(r"(?m)^      ([A-Za-z0-9_-]+):\s*(\S+)\s*$", preflight_permissions)
        if preflight_permissions
        else []
    )
    if preflight_entries != [("contents", "read")]:
        add(
            failures,
            WORKFLOW_PATH,
            "preflight permissions must contain only contents: read",
        )
    if re.search(r"(?m)^    environment:\s*$", preflight_block):
        add(failures, WORKFLOW_PATH, "preflight must not reference an environment")
    for forbidden in (
        "github-pages",
        "pages: write",
        "id-token: write",
        "actions/upload-pages-artifact",
        "actions/deploy-pages",
        "group: pages",
    ):
        if forbidden in preflight_block:
            add(failures, WORKFLOW_PATH, f"preflight must not contain {forbidden}")

    required_preflight_steps = (
        "actions/checkout@v6",
        "actions/setup-python@v6",
        "python scripts/validate_content_contracts.py",
        "python scripts/validate_stage_transitions.py",
        "python scripts/validate_release_state.py",
        "python -m py_compile scripts/validate_release_state.py",
        "python scripts/validate_release_state.py --check links",
        "python scripts/validate_release_state.py --check guards",
    )
    for step in required_preflight_steps:
        if step not in preflight_block:
            add(failures, WORKFLOW_PATH, f"preflight missing required step: {step}")

    if not re.search(
        r"(?ms)^    needs:\s*\n      - preflight\s*$", deploy_block
    ):
        add(failures, WORKFLOW_PATH, "deploy must declare needs: preflight")
    for condition_fragment in (
        "github.ref == 'refs/heads/main'",
        "github.event_name == 'push'",
        "github.event_name == 'workflow_dispatch'",
    ):
        if condition_fragment not in deploy_block:
            add(
                failures,
                WORKFLOW_PATH,
                f"deploy main-only condition missing: {condition_fragment}",
            )
    if "github.event_name == 'pull_request'" in deploy_block:
        add(failures, WORKFLOW_PATH, "pull requests must never execute deploy")

    deploy_permissions = yaml_named_block(deploy_block, "permissions", 4)
    deploy_entries = (
        set(
            re.findall(
                r"(?m)^      ([A-Za-z0-9_-]+):\s*(\S+)\s*$",
                deploy_permissions,
            )
        )
        if deploy_permissions
        else set()
    )
    expected_deploy_permissions = {
        ("contents", "read"),
        ("pages", "write"),
        ("id-token", "write"),
    }
    if deploy_entries != expected_deploy_permissions:
        add(
            failures,
            WORKFLOW_PATH,
            "deploy permissions must be contents: read, pages: write and id-token: write",
        )

    if not re.search(
        r"(?ms)^    environment:\s*\n      name: github-pages\s*$", deploy_block
    ):
        add(failures, WORKFLOW_PATH, "only deploy must use github-pages environment")
    if "group: pages" not in deploy_block or "cancel-in-progress: false" not in deploy_block:
        add(failures, WORKFLOW_PATH, "Pages concurrency must be scoped to deploy")

    outside_deploy = text.replace(deploy_block, "", 1)
    for deployment_only in ("github-pages", "pages: write", "id-token: write"):
        if deployment_only in outside_deploy:
            add(
                failures,
                WORKFLOW_PATH,
                f"{deployment_only} must appear only in deploy job",
            )

    invariants = {
        "actions/upload-pages-artifact@v4": 1,
        "actions/deploy-pages@v4": 1,
    }
    for marker, expected_count in invariants.items():
        count = text.count(marker)
        if count != expected_count:
            add(
                failures,
                WORKFLOW_PATH,
                f"{marker} must occur exactly once; found {count}",
            )
        if marker not in deploy_block:
            add(failures, WORKFLOW_PATH, f"{marker} must be contained in deploy")
    for marker in (
        "sho-release-verifier-${{ github.run_id }}",
        "steps.deployment.outputs.page_url",
    ):
        if marker not in deploy_block:
            add(failures, WORKFLOW_PATH, f"deploy must retain marker: {marker}")


def validate_document_consistency(failures: list[str]) -> None:
    for path in (ROOT_README, HANDOFF, DASHBOARD, WORK_QUEUE, PUBLIC_README):
        if not path.exists():
            add(failures, path, "required synchronized release-state source is missing")
            return

    root_text = ROOT_README.read_text(encoding="utf-8")
    require_fragments(
        failures,
        ROOT_README,
        root_text,
        [
            "docs/operations/RELEASE_STATE_V1.yaml",
            "Batch 01 is not operator-accepted.",
            "is accepted only for publication preparation.",
            "There is no final Launch Acceptance",
            "No publish readiness.",
            "No public launch.",
        ],
    )
    if "No Operator Acceptance." in root_text:
        add(
            failures,
            ROOT_README,
            "ambiguous 'No Operator Acceptance.' statement contradicts scoped acceptance axes",
        )

    handoff_text = HANDOFF.read_text(encoding="utf-8")
    if handoff_text.count("## Current Status") != 1:
        add(failures, HANDOFF, "must contain exactly one '## Current Status' block")
    current_start = handoff_text.find("## Current Status")
    history_start = handoff_text.find("## Historical / Superseded Context")
    if current_start < 0 or history_start <= current_start:
        add(failures, HANDOFF, "current status must precede historical/superseded context")
    else:
        current = handoff_text[current_start:history_start]
        require_fragments(
            failures,
            HANDOFF,
            current,
            [
                "operator_acceptance_status: not_accepted",
                "publication_preparation_acceptance_status: accepted",
                "publish_readiness_status: not_ready",
                "launch_acceptance_status: not_accepted",
                "public_launch_status: not_ready",
                "pages_status: completed_pending_external_legal_review",
                "legal_approval_status: not_approved",
                "configuration_status: externally_observed",
                "individual_page_http_status: unverified",
                "SHO-CLAIM-007",
                "SHO-SRC-004",
                f"current_allowed_next_action: {NEXT_ACTION}",
            ],
        )
        if current.count("current_allowed_next_action:") != 1:
            add(failures, HANDOFF, "current block must contain exactly one current next action")

    dashboard_text = DASHBOARD.read_text(encoding="utf-8")
    require_fragments(
        failures,
        DASHBOARD,
        dashboard_text,
        [
            "operator_acceptance_status: not_accepted",
            "### Current Candidate Release Status",
            "candidate_publication_preparation_acceptance_status: accepted",
            "candidate_publish_readiness_status: not_ready",
            "launch_acceptance_status: not_accepted",
            "legal_pages_status: completed_pending_external_legal_review",
            "domain_observation_status: externally_observed_https_and_robots_only",
            f"current_candidate_next_step: {NEXT_ACTION}",
        ],
    )
    if dashboard_text.count("current_candidate_next_step:") != 1:
        add(failures, DASHBOARD, "must contain exactly one current Candidate next step")

    queue_text = WORK_QUEUE.read_text(encoding="utf-8")
    require_fragments(
        failures,
        WORK_QUEUE,
        queue_text,
        [
            f"current_allowed_next_action: {NEXT_ACTION}",
            "current_release_task_id: CQ-V1-084",
            "queue_item_id: CQ-V1-084",
            "internal_candidate_id: SHO-INTERNAL-CANDIDATE-001",
            "task_scope: bounded_release_verification_only",
            f"allowed_next_action: {NEXT_ACTION}",
            "status: current_executable_release_verification_task",
        ],
    )
    root_actions = re.findall(r"(?m)^current_allowed_next_action:\s*(\S+)\s*$", queue_text)
    current_task_count = len(
        re.findall(
            r"(?m)^\s+status:\s*current_executable_release_verification_task\s*$",
            queue_text,
        )
    )
    if root_actions != [NEXT_ACTION]:
        add(failures, WORK_QUEUE, "must expose exactly one canonical current release action")
    if current_task_count != 1:
        add(
            failures,
            WORK_QUEUE,
            f"must contain exactly one current executable release task; found {current_task_count}",
        )

    public_text = PUBLIC_README.read_text(encoding="utf-8")
    require_fragments(
        failures,
        PUBLIC_README,
        public_text,
        [
            "externally observed over HTTPS on 2026-07-16",
            "covers only HTTPS reachability and the robots response",
            "no repository-owned GitHub Actions verifier report",
            "completed_pending_external_legal_review",
            "legal approval is not granted",
            "Indexing remains blocked",
            "Analytics and Search Console remain not connected",
            "This patch does not add `public_site/CNAME`",
            "configured in the repository Pages settings",
        ],
    )


def is_external_or_ignored(reference: str) -> bool:
    stripped = reference.strip()
    if not stripped or stripped.startswith(("#", "//")):
        return True
    scheme = urlsplit(stripped).scheme.lower()
    return scheme in {
        "http",
        "https",
        "mailto",
        "tel",
        "data",
        "javascript",
    }


def local_target(source: Path, reference: str) -> Path | None:
    if is_external_or_ignored(reference):
        return None
    parsed = urlsplit(reference)
    path_text = unquote(parsed.path).replace("\\", "/")
    if not path_text:
        return None
    if path_text.startswith("/"):
        target = PUBLIC_SITE / path_text.lstrip("/")
    else:
        target = source.parent / path_text
    return target.resolve()


def target_exists_inside_site(target: Path) -> tuple[bool, str]:
    try:
        target.relative_to(PUBLIC_SITE.resolve())
    except ValueError:
        return False, "target escapes public_site"
    if target.is_dir():
        target = target / "index.html"
    if target.exists():
        return True, ""
    return False, f"target does not exist: {relative(target)}"


def validate_local_links(failures: list[str]) -> None:
    if not PUBLIC_SITE.exists():
        add(failures, PUBLIC_SITE, "public site directory is missing")
        return

    for html_path in sorted(PUBLIC_SITE.rglob("*.html")):
        try:
            text = html_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            add(failures, html_path, f"cannot read HTML: {exc}")
            continue
        parser = ResourceParser()
        try:
            parser.feed(text)
        except Exception as exc:  # HTMLParser errors are rare but actionable.
            add(failures, html_path, f"cannot parse HTML references: {exc}")
            continue
        for attribute, reference in parser.references:
            target = local_target(html_path, reference)
            if target is None:
                continue
            exists, reason = target_exists_inside_site(target)
            if not exists:
                add(
                    failures,
                    html_path,
                    f"{attribute}={reference!r} is invalid: {reason}",
                )

    css_url_pattern = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
    for css_path in sorted(PUBLIC_SITE.rglob("*.css")):
        try:
            text = css_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            add(failures, css_path, f"cannot read stylesheet: {exc}")
            continue
        for match in css_url_pattern.finditer(text):
            reference = match.group(2).strip()
            target = local_target(css_path, reference)
            if target is None:
                continue
            exists, reason = target_exists_inside_site(target)
            if not exists:
                add(failures, css_path, f"url({reference!r}) is invalid: {reason}")


def validate_staging_guards(failures: list[str]) -> None:
    robots_path = PUBLIC_SITE / "robots.txt"
    if not robots_path.exists():
        add(failures, robots_path, "robots.txt is missing")
    else:
        effective_lines = []
        for raw_line in robots_path.read_text(encoding="utf-8").splitlines():
            effective = raw_line.split("#", 1)[0].strip()
            if effective:
                effective_lines.append(effective)
        disallow_lines = [
            line for line in effective_lines if line.lower().startswith("disallow:")
        ]
        if disallow_lines != ["Disallow: /"]:
            add(
                failures,
                robots_path,
                "must contain exactly one effective 'Disallow: /' and no other Disallow rule; "
                f"found {disallow_lines!r}",
            )

    html_paths = sorted(PUBLIC_SITE.rglob("*.html"))
    if not html_paths:
        add(failures, PUBLIC_SITE, "no delivered HTML pages were found")
    for html_path in html_paths:
        text = html_path.read_text(encoding="utf-8")
        parser = RobotsMetaParser()
        parser.feed(text)
        if not any({"noindex", "nofollow"}.issubset(item) for item in parser.robot_directives):
            add(
                failures,
                html_path,
                "delivered HTML must contain a robots meta directive with noindex, nofollow",
            )

    script_like_paths = sorted(
        path
        for path in PUBLIC_SITE.rglob("*")
        if path.is_file() and path.suffix.lower() in {".html", ".js", ".css"}
    )
    for path in script_like_paths:
        text = path.read_text(encoding="utf-8").lower()
        for signature, label in TRACKING_SIGNATURES.items():
            if signature in text:
                add(
                    failures,
                    path,
                    f"unexpected analytics/tracking/monetization signature: {label} ({signature})",
                )

    cname = PUBLIC_SITE / "CNAME"
    if cname.exists():
        add(failures, cname, "tracked public_site/CNAME is not authorized by this patch")


def validate_no_positive_compliance_claims(failures: list[str]) -> None:
    paths = [RELEASE_STATE_PATH, ROOT_README, HANDOFF, DASHBOARD, WORK_QUEUE, PUBLIC_README]
    paths.extend(sorted(PUBLIC_SITE.rglob("*.html")))
    patterns = [
        re.compile(
            r"wcag_conformance_status\s*:\s*(claimed|compliant|conformant|passed|approved)",
            re.IGNORECASE,
        ),
        re.compile(r"\bwcag\b.{0,30}\b(compliant|conformant|certified)\b", re.IGNORECASE),
        re.compile(r"\bbfsg\b.{0,30}\b(compliant|conformant|certified)\b", re.IGNORECASE),
        re.compile(
            r"legal_approval_status\s*:\s*(approved|accepted|granted)", re.IGNORECASE
        ),
        re.compile(r"\blegally\s+(approved|compliant|certified)\b", re.IGNORECASE),
    ]
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in patterns:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                add(
                    failures,
                    path,
                    f"line {line} contains an unauthorized positive WCAG/BFSG/Legal claim: {match.group(0)!r}",
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        choices=("all", "links", "guards"),
        default="all",
        help="run the full contract or one workflow-specific deterministic subset",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    failures: list[str] = []

    if args.check == "all":
        validate_release_yaml(failures)
        validate_workflow_contract(failures)
        validate_document_consistency(failures)
        validate_local_links(failures)
        validate_staging_guards(failures)
        validate_no_positive_compliance_claims(failures)
        label = "release state validation"
    elif args.check == "links":
        validate_local_links(failures)
        label = "public_site link/asset validation"
    else:
        validate_staging_guards(failures)
        validate_no_positive_compliance_claims(failures)
        label = "robots/noindex/tracking guard validation"

    if failures:
        print(f"FAIL: SHO-OS {label} failed", file=sys.stderr)
        for finding in failures:
            print(f"- {finding}", file=sys.stderr)
        return 1

    print(f"PASS: SHO-OS {label} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
