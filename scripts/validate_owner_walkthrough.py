#!/usr/bin/env python3
"""Validate a private DAG owner walkthrough record without publishing its notes.

The tool checks the six D-016 review areas and five established viewport widths.
It never edits the owner's record, prototype, screenshots, catalogue or source assets.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path
from typing import Any

try:
    from .private_review_output import ensure_private_directory, has_symlink_component
except ImportError:
    from private_review_output import ensure_private_directory, has_symlink_component

ROOT = Path(__file__).resolve().parents[1]
REPORT_JSON = "owner-walkthrough-readiness.json"
REPORT_MARKDOWN = "owner-walkthrough-readiness.md"

AREAS = {
    "homepage": ("index.html",),
    "shop_and_collections": ("pages/shop.html", "pages/collection.html"),
    "product_detail": ("pages/product.html",),
    "about_and_makers": ("pages/about.html", "pages/makers.html"),
    "journal_and_stories": ("pages/journal.html", "pages/article.html"),
    "contact_and_support": ("pages/contact.html",),
}
VIEWPORTS = ("390", "430", "768", "1280", "1440")
OBSERVATIONS = (
    "visual_hierarchy_and_density",
    "image_ratio_crop_placeholder_clarity",
    "content_and_factual_evidence_gaps",
    "navigation_and_shared_shell",
    "keyboard_focus_and_disabled_state_clarity",
)
DECISIONS = {"pending", "accept", "request_revision", "reject"}
REVIEW_STATES = {"pending", "reviewed", "blocked"}
ROUTES = {
    "index.html",
    "pages/shop.html",
    "pages/collection.html",
    "pages/product.html",
    "pages/about.html",
    "pages/makers.html",
    "pages/journal.html",
    "pages/article.html",
    "pages/contact.html",
}


def _inside(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def _overlaps(left: Path, right: Path) -> bool:
    return _inside(left, right) or _inside(right, left)


def _is_text(value: Any, *, limit: int = 1000) -> bool:
    return isinstance(value, str) and bool(value.strip()) and len(value) <= limit


def _valid_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _check_keys(value: Any, required: set[str], label: str, errors: list[str]) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return False
    missing = required - set(value)
    extra = set(value) - required
    for key in sorted(missing):
        errors.append(f"{label} is missing required field: {key}")
    for key in sorted(extra):
        errors.append(f"{label} contains unsupported field: {key}")
    return True


def _validate_record(record: Any) -> list[str]:
    errors: list[str] = []
    top_keys = {
        "schema_version", "decision_reference", "prototype_revision",
        "review_date", "owner_confirmation", "confirmation_date", "areas",
    }
    if not _check_keys(record, top_keys, "record", errors):
        return errors

    version = record.get("schema_version")
    if type(version) is not int or version != 1:
        errors.append("schema_version must be integer 1")
    if record.get("decision_reference") != "D-017":
        errors.append("decision_reference must be D-017")
    revision = record.get("prototype_revision")
    if not _is_text(revision, limit=120) or "\n" in revision or "\r" in revision:
        errors.append("prototype_revision must be a non-empty single-line label (max 120 characters)")

    review_date = record.get("review_date")
    if review_date is not None and not _valid_date(review_date):
        errors.append("review_date must be null or a real YYYY-MM-DD calendar date")

    confirmation = record.get("owner_confirmation")
    if not isinstance(confirmation, str) or confirmation not in {"pending", "confirmed"}:
        errors.append("owner_confirmation must be pending or confirmed")
    confirmation_date = record.get("confirmation_date")
    if confirmation_date is not None and not _valid_date(confirmation_date):
        errors.append("confirmation_date must be null or a real YYYY-MM-DD calendar date")
    if confirmation == "pending" and confirmation_date is not None:
        errors.append("confirmation_date must remain null while owner_confirmation is pending")
    if confirmation == "confirmed" and confirmation_date is None:
        errors.append("confirmation_date is required when owner_confirmation is confirmed")

    areas = record.get("areas")
    if not isinstance(areas, list):
        errors.append("areas must be a JSON array")
        return errors
    if len(areas) != len(AREAS):
        errors.append(f"areas must contain exactly {len(AREAS)} D-016 review areas")

    seen: set[str] = set()
    valid_area_count = 0
    any_review_started = False
    all_area_acceptances = True

    for index, area in enumerate(areas):
        label = f"areas[{index}]"
        area_keys = {"area_id", "decision", "viewport_reviews", "observations", "requested_changes"}
        if not _check_keys(area, area_keys, label, errors):
            all_area_acceptances = False
            continue

        area_id = area.get("area_id")
        if not isinstance(area_id, str) or area_id not in AREAS:
            errors.append(f"{label}.area_id must identify one of the six D-016 review areas")
            all_area_acceptances = False
        else:
            if area_id in seen:
                errors.append(f"duplicate review area: {area_id}")
                all_area_acceptances = False
            seen.add(area_id)
            valid_area_count += 1

        decision = area.get("decision")
        if not isinstance(decision, str) or decision not in DECISIONS:
            errors.append(f"{label}.decision must be one of: {', '.join(sorted(DECISIONS))}")
            decision = "pending"
            all_area_acceptances = False
        if decision != "accept":
            all_area_acceptances = False

        viewport_reviews = area.get("viewport_reviews")
        if not _check_keys(viewport_reviews, set(VIEWPORTS), f"{label}.viewport_reviews", errors):
            viewport_reviews = {}
            all_reviewed = False
        else:
            all_reviewed = True

        for width in VIEWPORTS:
            review = viewport_reviews.get(width)
            review_label = f"{label}.viewport_reviews.{width}"
            if not _check_keys(review, {"status", "notes"}, review_label, errors):
                all_reviewed = False
                continue
            state = review.get("status")
            notes = review.get("notes")
            if not isinstance(state, str) or state not in REVIEW_STATES:
                errors.append(f"{review_label}.status must be pending, reviewed or blocked")
                all_reviewed = False
            elif state != "reviewed":
                all_reviewed = False
            if not isinstance(notes, str) or len(notes) > 1000:
                errors.append(f"{review_label}.notes must be text (max 1000 characters)")
            elif isinstance(state, str) and state in {"reviewed", "blocked"} and not notes.strip():
                errors.append(f"{review_label}.notes is required for a reviewed or blocked viewport")
            if isinstance(state, str) and state in {"reviewed", "blocked"}:
                any_review_started = True

        observations = area.get("observations")
        if not _check_keys(observations, set(OBSERVATIONS), f"{label}.observations", errors):
            observations = {}
        for key in OBSERVATIONS:
            value = observations.get(key, "")
            if not isinstance(value, str) or len(value) > 1000:
                errors.append(f"{label}.observations.{key} must be text (max 1000 characters)")
            elif decision != "pending" and not value.strip():
                errors.append(f"{label}.observations.{key} is required for a decided area")

        requested = area.get("requested_changes")
        if not isinstance(requested, list):
            errors.append(f"{label}.requested_changes must be a JSON array")
            requested = []
        if len(requested) > 25:
            errors.append(f"{label}.requested_changes cannot exceed 25 entries")
        for change_index, change in enumerate(requested):
            change_label = f"{label}.requested_changes[{change_index}]"
            if not _check_keys(change, {"route", "component", "request"}, change_label, errors):
                continue
            if not isinstance(change.get("route"), str) or change.get("route") not in ROUTES:
                errors.append(f"{change_label}.route must be one of the nine D-014 routes")
            if not _is_text(change.get("component"), limit=120):
                errors.append(f"{change_label}.component must be non-empty text (max 120 characters)")
            if not _is_text(change.get("request"), limit=1000):
                errors.append(f"{change_label}.request must be non-empty text (max 1000 characters)")

        if decision != "pending":
            if not all_reviewed:
                errors.append(f"{label} cannot be decided until all five approved viewport widths are reviewed")
            if decision in {"request_revision", "reject"} and not requested:
                errors.append(f"{label} requires at least one route/component-scoped requested change")
            if decision == "accept" and requested:
                errors.append(f"{label} cannot be accepted while requested_changes remain")
        if decision == "pending" and requested:
            errors.append(f"{label} must use request_revision or reject when recording requested changes")

    missing_areas = set(AREAS) - seen
    for area_id in sorted(missing_areas):
        errors.append(f"record is missing D-016 review area: {area_id}")

    decided = any(
        isinstance(area, dict) and isinstance(area.get("decision"), str) and area.get("decision") in {"accept", "request_revision", "reject"}
        for area in areas
    )
    if (decided or any_review_started) and not _valid_date(review_date):
        errors.append("review_date is required once any viewport review or area decision is recorded")

    if confirmation == "confirmed":
        if valid_area_count != len(AREAS) or seen != set(AREAS):
            errors.append("owner confirmation requires the exact six D-016 review areas")
        if not all_area_acceptances:
            errors.append("owner confirmation requires all six areas to be accepted")
        if not _valid_date(review_date):
            errors.append("owner confirmation requires a valid review_date")
        if not _valid_date(confirmation_date):
            errors.append("owner confirmation requires a valid confirmation_date")

    return errors


def _status(record: dict[str, Any]) -> str:
    decisions = [area.get("decision") for area in record["areas"] if isinstance(area, dict)]
    if "reject" in decisions:
        return "REJECTED"
    if "request_revision" in decisions:
        return "REVISION_REQUIRED"
    if (
        len(decisions) == len(AREAS)
        and set(area.get("area_id") for area in record["areas"] if isinstance(area, dict)) == set(AREAS)
        and all(decision == "accept" for decision in decisions)
        and record.get("owner_confirmation") == "confirmed"
    ):
        return "OWNER_VISUAL_ACCEPTED"
    return "REVIEW_INCOMPLETE"


def _report(record: dict[str, Any]) -> dict[str, Any]:
    areas: list[dict[str, Any]] = []
    reviewed_total = 0
    blocked_total = 0
    accepted = revisions = rejected = pending = 0

    for area in record["areas"]:
        reviews = area["viewport_reviews"]
        reviewed = [width for width in VIEWPORTS if reviews[width]["status"] == "reviewed"]
        blocked = [width for width in VIEWPORTS if reviews[width]["status"] == "blocked"]
        pending_widths = [width for width in VIEWPORTS if reviews[width]["status"] == "pending"]
        reviewed_total += len(reviewed)
        blocked_total += len(blocked)
        decision = area["decision"]
        accepted += decision == "accept"
        revisions += decision == "request_revision"
        rejected += decision == "reject"
        pending += decision == "pending"
        areas.append({
            "area_id": area["area_id"],
            "decision": decision,
            "reviewed_viewport_count": len(reviewed),
            "reviewed_viewports": reviewed,
            "blocked_viewports": blocked,
            "pending_viewports": pending_widths,
            "requested_change_count": len(area["requested_changes"]),
        })

    summary = {
        "area_count": len(areas),
        "accepted_area_count": accepted,
        "revision_requested_area_count": revisions,
        "rejected_area_count": rejected,
        "pending_area_count": pending,
        "reviewed_viewport_count": reviewed_total,
        "blocked_viewport_count": blocked_total,
        "expected_viewport_count": len(AREAS) * len(VIEWPORTS),
    }
    return {
        "report_type": "DAG private owner walkthrough readiness",
        "decision_reference": "D-017",
        "status": _status(record),
        "review_date": record.get("review_date"),
        "owner_confirmation": record.get("owner_confirmation"),
        "summary": summary,
        "areas": areas,
        "privacy_note": "Detailed owner observations and requested-change text are intentionally excluded from this summary; retain them in the private source record.",
        "acceptance_boundary": "A confirmed result records owner visual acceptance of the D-016/D-017 local/private non-transactional prototype only. It does not approve customer research, publication, commerce, production architecture or deployment.",
    }


def _markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# DAG Private Owner Walkthrough — Readiness Report", "",
        f"- Overall result: **{report['status']}**",
        f"- Decision reference: **{report['decision_reference']}**",
        f"- Review date: **{report['review_date'] or 'not recorded'}**",
        f"- Owner confirmation: **{report['owner_confirmation']}**",
        "", "## Coverage", "",
        "| Measure | Count |", "|---|---:|",
        f"| Review areas | {summary['area_count']} / 6 |",
        f"| Accepted areas | {summary['accepted_area_count']} |",
        f"| Revision requested | {summary['revision_requested_area_count']} |",
        f"| Rejected areas | {summary['rejected_area_count']} |",
        f"| Pending areas | {summary['pending_area_count']} |",
        f"| Reviewed area/viewport checks | {summary['reviewed_viewport_count']} / {summary['expected_viewport_count']} |",
        f"| Blocked area/viewport checks | {summary['blocked_viewport_count']} |",
        "", "## Area status", "",
        "| Area | Decision | Reviewed widths | Blocked widths | Pending widths | Requested changes |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for area in report["areas"]:
        lines.append(
            f"| {area['area_id']} | {area['decision']} | "
            f"{area['reviewed_viewport_count']}/5 | {len(area['blocked_viewports'])} | "
            f"{len(area['pending_viewports'])} | {area['requested_change_count']} |"
        )
    lines.extend([
        "", "## Privacy and acceptance boundary", "",
        report["privacy_note"], "", report["acceptance_boundary"], "",
        "This report does not include the owner's free-text observations, local paths, product content, photographs or evidence files.", "",
    ])
    return "\n".join(lines)


def _write_new(path: Path, content: str) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
        handle.write(content)


def build_owner_walkthrough_report(record_path: Path, output_dir: Path) -> dict[str, Any]:
    raw_record = Path(record_path).expanduser()
    raw_output = Path(output_dir).expanduser()
    errors: list[str] = []

    if has_symlink_component(raw_record):
        errors.append("owner walkthrough record path must not contain symbolic links")
    if has_symlink_component(raw_output):
        errors.append("report output path must not contain symbolic links")
    if errors:
        return {"ok": False, "status": "INVALID_INPUT", "errors": errors}

    try:
        source = raw_record.resolve(strict=True)
    except (OSError, RuntimeError):
        return {"ok": False, "status": "INVALID_INPUT", "errors": ["owner walkthrough record does not exist or cannot be resolved"]}
    if not source.is_file():
        errors.append("owner walkthrough record must be a regular file")

    repository = ROOT.resolve()
    if _inside(source, repository):
        errors.append("owner walkthrough record must remain outside the public Git repository")

    try:
        output = raw_output.resolve(strict=False)
    except (OSError, RuntimeError):
        output = raw_output
        errors.append("report output directory cannot be resolved")
    if _overlaps(output, repository):
        errors.append("owner walkthrough reports must remain outside the public Git repository")
    if output.exists() and not output.is_dir():
        errors.append("report output path must be a directory")
    if errors:
        return {"ok": False, "status": "INVALID_INPUT", "errors": errors}

    try:
        record = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return {"ok": False, "status": "INVALID_INPUT", "errors": [f"cannot read owner walkthrough JSON: {error}"]}

    validation_errors = _validate_record(record)
    if validation_errors:
        return {"ok": False, "status": "INVALID_INPUT", "errors": validation_errors}

    report = _report(record)
    json_path = output / REPORT_JSON
    markdown_path = output / REPORT_MARKDOWN
    existing = [path.name for path in (json_path, markdown_path) if path.exists()]
    if existing:
        return {
            "ok": False,
            "status": "INVALID_INPUT",
            "errors": ["refusing to overwrite existing report file(s): " + ", ".join(existing)],
        }

    created: list[Path] = []
    try:
        output = ensure_private_directory(output)
        for path, content in (
            (json_path, json.dumps(report, indent=2, ensure_ascii=False) + "\n"),
            (markdown_path, _markdown(report)),
        ):
            _write_new(path, content)
            created.append(path)
    except OSError as error:
        for path in created:
            try:
                path.unlink()
            except OSError:
                pass
        return {"ok": False, "status": "INVALID_INPUT", "errors": [f"could not write private readiness report: {error}"]}

    return {
        "ok": report["status"] == "OWNER_VISUAL_ACCEPTED",
        "status": report["status"],
        "errors": [],
        "json_report": str(json_path),
        "markdown_report": str(markdown_path),
        "summary": report["summary"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a private D-016 owner walkthrough record; never edits the record or prototype."
    )
    parser.add_argument("--record", required=True, type=Path, help="Private owner walkthrough JSON record outside the Git repository")
    parser.add_argument("--output-dir", required=True, type=Path, help="Private report directory outside the Git repository")
    args = parser.parse_args(argv)

    result = build_owner_walkthrough_report(args.record, args.output_dir)
    if result.get("errors"):
        for error in result["errors"]:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(f"Owner walkthrough status: {result['status']}")
    if result.get("summary"):
        summary = result["summary"]
        print(
            f"Areas accepted: {summary['accepted_area_count']}/6; "
            f"viewport reviews: {summary['reviewed_viewport_count']}/{summary['expected_viewport_count']}"
        )
        print(f"Private report: {result['markdown_report']}")
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
