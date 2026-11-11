#!/usr/bin/env python3
"""Validate a private M2-B fieldwork authorization record without initiating research.

The tool is a fail-closed preflight for the eight D-016 owner approvals. It
never contacts participants, processes participant data, starts recording, or
authorizes spending. Evidence references are recorded but not opened or
independently verified.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

try:
    from .private_review_output import ensure_private_directory
except ImportError:
    from private_review_output import ensure_private_directory

ROOT = Path(__file__).resolve().parents[1]
REPORT_JSON = "m2b-fieldwork-authorization.json"
REPORT_MARKDOWN = "m2b-fieldwork-authorization.md"

APPROVAL_ITEMS = {
    "recruitment_route": "Recruitment route/provider and screening approach",
    "invitation_and_screener": "Final invitation text and screener",
    "moderator_and_language": "Moderator and session language",
    "participant_information_and_consent": "Participant information, consent and recording wording",
    "private_data_handling": "Private storage, access, retention and deletion arrangements",
    "research_budget": "Participant incentive and recruitment/moderator spend ceiling",
    "vendor_processing_and_transfer": "Vendor terms, processing, subcontracting and transfer arrangements",
    "date_range_and_schedule": "Fieldwork date range and scheduling plan",
}
COHORT = {
    "home_interior": 3,
    "craft_material": 2,
    "trade_design": 1,
    "gift_considered_purchase": 1,
    "total": 7,
}
APPROVAL_STATES = {"pending", "approved", "rejected"}
OWNER_STATES = {"pending", "confirmed"}
RECORDING_MODES = {"not_authorized", "no_recording", "optional_separate_participant_consent"}
VENDOR_MODES = {"unreviewed", "no_vendor", "vendor_involved"}
TRANSFER_MODES = {"unreviewed", "none", "reviewed_and_approved"}
CURRENCY = re.compile(r"^[A-Z]{3}$")
AMOUNT = re.compile(r"^(?:0|[1-9][0-9]*)(?:\.[0-9]{1,2})?$")
DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
REFERENCE_LIMIT = 240
TOP_KEYS = {
    "schema_version", "decision_reference", "cohort", "approvals",
    "fieldwork_details", "owner_confirmation",
}
APPROVAL_KEYS = {"status", "approved_on", "evidence_reference"}
DETAIL_KEYS = {
    "moderator_reference", "session_languages",
    "participant_information_reference", "consent_wording_reference",
    "recording_mode", "recording_consent_reference",
    "storage_reference", "access_control_reference", "retention_days",
    "deletion_reference", "transfer_mode", "transfer_review_reference",
    "vendor_mode", "vendor_terms_reference",
    "spend_currency", "spend_ceiling", "budget_breakdown_reference",
    "schedule_timezone", "start_date", "end_date", "schedule_reference",
}
OWNER_KEYS = {"status", "confirmed_on", "scope_reference"}


def _check_object(value: Any, keys: set[str], label: str, errors: list[str]) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return False
    for key in sorted(keys - set(value)):
        errors.append(f"{label} is missing required field: {key}")
    for key in sorted(set(value) - keys):
        errors.append(f"{label} contains unsupported field: {key}")
    return True


def _nonempty_text(value: Any, *, limit: int = REFERENCE_LIMIT) -> bool:
    return (
        isinstance(value, str)
        and bool(value.strip())
        and len(value) <= limit
        and "\n" not in value
        and "\r" not in value
        and "\x00" not in value
    )


def _optional_reference(value: Any, label: str, errors: list[str]) -> bool:
    if value is None:
        return False
    if not _nonempty_text(value):
        errors.append(f"{label} must be null or a non-empty single-line reference (max {REFERENCE_LIMIT} characters)")
        return False
    return True


def _valid_date(value: Any) -> bool:
    if not isinstance(value, str) or not DATE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _validate_approvals(value: Any, errors: list[str]) -> dict[str, str]:
    states: dict[str, str] = {}
    if not _check_object(value, set(APPROVAL_ITEMS), "approvals", errors):
        return states
    for item_id in APPROVAL_ITEMS:
        entry = value.get(item_id)
        label = f"approvals.{item_id}"
        if not _check_object(entry, APPROVAL_KEYS, label, errors):
            states[item_id] = "pending"
            continue
        status = entry.get("status")
        if not isinstance(status, str) or status not in APPROVAL_STATES:
            errors.append(f"{label}.status must be pending, approved or rejected")
            status = "pending"
        states[item_id] = status
        approved_on = entry.get("approved_on")
        evidence = entry.get("evidence_reference")
        if status == "approved":
            if not _valid_date(approved_on):
                errors.append(f"{label}.approved_on must be a real YYYY-MM-DD date when approved")
            if not _nonempty_text(evidence):
                errors.append(f"{label}.evidence_reference must be a non-empty private reference when approved")
        else:
            if approved_on is not None:
                errors.append(f"{label}.approved_on must be null unless the item is approved")
            if evidence is not None:
                errors.append(f"{label}.evidence_reference must be null unless the item is approved")
    return states


def _validate_details(value: Any, errors: list[str]) -> dict[str, Any]:
    details: dict[str, Any] = {}
    if not _check_object(value, DETAIL_KEYS, "fieldwork_details", errors):
        return details
    details.update(value)

    for key in (
        "moderator_reference", "participant_information_reference",
        "consent_wording_reference", "recording_consent_reference",
        "storage_reference", "access_control_reference", "deletion_reference",
        "transfer_review_reference", "vendor_terms_reference",
        "budget_breakdown_reference", "schedule_reference",
    ):
        raw = value.get(key)
        if raw is not None:
            _optional_reference(raw, f"fieldwork_details.{key}", errors)

    languages = value.get("session_languages")
    if not isinstance(languages, list):
        errors.append("fieldwork_details.session_languages must be an array")
    else:
        if any(not _nonempty_text(item, limit=60) for item in languages):
            errors.append("fieldwork_details.session_languages entries must be non-empty single-line labels (max 60 characters)")
        if len(languages) != len(set(item for item in languages if isinstance(item, str))):
            errors.append("fieldwork_details.session_languages must not contain duplicates")

    recording_mode = value.get("recording_mode")
    if not isinstance(recording_mode, str) or recording_mode not in RECORDING_MODES:
        errors.append("fieldwork_details.recording_mode must be not_authorized, no_recording or optional_separate_participant_consent")

    vendor_mode = value.get("vendor_mode")
    if not isinstance(vendor_mode, str) or vendor_mode not in VENDOR_MODES:
        errors.append("fieldwork_details.vendor_mode must be unreviewed, no_vendor or vendor_involved")

    transfer_mode = value.get("transfer_mode")
    if not isinstance(transfer_mode, str) or transfer_mode not in TRANSFER_MODES:
        errors.append("fieldwork_details.transfer_mode must be unreviewed, none or reviewed_and_approved")

    retention_days = value.get("retention_days")
    if retention_days is not None and (type(retention_days) is not int or retention_days < 1 or retention_days > 36500):
        errors.append("fieldwork_details.retention_days must be null or an integer from 1 to 36500")

    currency = value.get("spend_currency")
    if currency is not None and (not isinstance(currency, str) or not CURRENCY.fullmatch(currency)):
        errors.append("fieldwork_details.spend_currency must be null or a three-letter uppercase currency code")

    ceiling = value.get("spend_ceiling")
    if ceiling is not None:
        if not isinstance(ceiling, str) or not AMOUNT.fullmatch(ceiling):
            errors.append("fieldwork_details.spend_ceiling must be null or a non-negative decimal amount with up to two decimals")
        else:
            try:
                if Decimal(ceiling) < 0:
                    errors.append("fieldwork_details.spend_ceiling must not be negative")
            except InvalidOperation:
                errors.append("fieldwork_details.spend_ceiling must be a valid decimal amount")

    timezone = value.get("schedule_timezone")
    if timezone is not None and not _nonempty_text(timezone, limit=80):
        errors.append("fieldwork_details.schedule_timezone must be null or a non-empty single-line timezone label")

    for key in ("start_date", "end_date"):
        raw = value.get(key)
        if raw is not None and not _valid_date(raw):
            errors.append(f"fieldwork_details.{key} must be null or a real YYYY-MM-DD calendar date")
    start = value.get("start_date")
    end = value.get("end_date")
    if _valid_date(start) and _valid_date(end) and end < start:
        errors.append("fieldwork_details.end_date must be on or after start_date")
    return details


def _blockers(states: dict[str, str], details: dict[str, Any], owner: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    for item_id, label in APPROVAL_ITEMS.items():
        status = states.get(item_id, "pending")
        if status == "pending":
            blockers.append(f"{label}: owner approval pending")
        elif status == "rejected":
            blockers.append(f"{label}: owner approval rejected")

    if not _nonempty_text(details.get("moderator_reference")):
        blockers.append("Name/reference the moderator and confirm supported session language(s)")
    if not details.get("session_languages"):
        blockers.append("At least one session language must be explicitly selected")
    if not _nonempty_text(details.get("participant_information_reference")):
        blockers.append("Participant information sheet reference is missing")
    if not _nonempty_text(details.get("consent_wording_reference")):
        blockers.append("Final consent wording reference is missing")
    recording_mode = details.get("recording_mode")
    if recording_mode == "not_authorized":
        blockers.append("Recording approach is undecided; recording remains unauthorized")
    if recording_mode == "optional_separate_participant_consent" and not _nonempty_text(details.get("recording_consent_reference")):
        blockers.append("Separate optional recording-consent wording reference is missing")

    for key, label in (
        ("storage_reference", "Private data-storage arrangement reference"),
        ("access_control_reference", "Data access-control arrangement reference"),
        ("deletion_reference", "Data deletion procedure reference"),
    ):
        if not _nonempty_text(details.get(key)):
            blockers.append(f"{label} is missing")
    if type(details.get("retention_days")) is not int or details.get("retention_days", 0) < 1:
        blockers.append("A defined data-retention period is missing")
    transfer_mode = details.get("transfer_mode")
    if transfer_mode == "unreviewed":
        blockers.append("Cross-border data-transfer arrangement has not been reviewed")
    if transfer_mode == "reviewed_and_approved" and not _nonempty_text(details.get("transfer_review_reference")):
        blockers.append("Approved data-transfer review reference is missing")

    vendor_mode = details.get("vendor_mode")
    if vendor_mode == "unreviewed":
        blockers.append("Vendor/processor involvement has not been decided")
    if vendor_mode == "vendor_involved" and not _nonempty_text(details.get("vendor_terms_reference")):
        blockers.append("Vendor terms, processing, subcontracting and transfer review reference is missing")

    if not isinstance(details.get("spend_currency"), str) or not CURRENCY.fullmatch(details.get("spend_currency", "")):
        blockers.append("An explicit research-spend currency is missing")
    ceiling = details.get("spend_ceiling")
    if not isinstance(ceiling, str) or not AMOUNT.fullmatch(ceiling):
        blockers.append("An explicit total research-spend ceiling is missing")
    if not _nonempty_text(details.get("budget_breakdown_reference")):
        blockers.append("The incentive, recruitment and moderator budget breakdown reference is missing")

    for key, label in (
        ("schedule_timezone", "Scheduling timezone"),
        ("start_date", "Fieldwork start date"),
        ("end_date", "Fieldwork end date"),
        ("schedule_reference", "Scheduling plan reference"),
    ):
        value = details.get(key)
        missing = not _valid_date(value) if key in {"start_date", "end_date"} else not _nonempty_text(value)
        if missing:
            blockers.append(f"{label} is missing")

    if owner.get("status") == "pending":
        blockers.append("Explicit owner confirmation of the complete eight-item fieldwork scope is pending")
    return blockers


def _inside(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def _has_symlink_component(path: Path) -> bool:
    absolute = path.expanduser().absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        try:
            if current.is_symlink():
                return True
        except OSError:
            return True
    return False


def _safe_paths(record_path: Path, output_dir: Path) -> tuple[Path, Path, list[str]]:
    errors: list[str] = []
    raw_record = record_path.expanduser().absolute()
    raw_output = output_dir.expanduser().absolute()
    if _has_symlink_component(raw_record):
        errors.append("authorization record path must not contain symbolic links")
    if _has_symlink_component(raw_output):
        errors.append("report output path must not contain symbolic links")
    try:
        record = raw_record.resolve(strict=True)
    except (OSError, RuntimeError):
        record = raw_record
        errors.append("authorization record does not exist or cannot be resolved")
    try:
        output = raw_output.resolve(strict=False)
    except (OSError, RuntimeError):
        output = raw_output
        errors.append("report output path cannot be resolved")
    if not errors and not record.is_file():
        errors.append("authorization record must be a regular file")
    repository = ROOT.resolve()
    if _inside(record, repository):
        errors.append("authorization record must remain outside the public Git repository")
    if _inside(output, repository):
        errors.append("authorization report must remain outside the public Git repository")
    if _inside(output, record.parent) or _inside(record.parent, output):
        errors.append("authorization report directory must be separate from the private record directory")
    return record, output, errors


def _validate_record(record: Any) -> tuple[list[str], list[str], dict[str, Any]]:
    errors: list[str] = []
    if not _check_object(record, TOP_KEYS, "record", errors):
        return errors, [], {}

    version = record.get("schema_version")
    if type(version) is not int or version != 1:
        errors.append("schema_version must be integer 1")
    if record.get("decision_reference") != "D-016":
        errors.append("decision_reference must be D-016")

    cohort = record.get("cohort")
    if not _check_object(cohort, set(COHORT), "cohort", errors):
        cohort = {}
    else:
        for key, expected in COHORT.items():
            value = cohort.get(key)
            if type(value) is not int or value != expected:
                errors.append(f"cohort.{key} must remain the D-016 approved count ({expected})")

    states = _validate_approvals(record.get("approvals"), errors)
    details = _validate_details(record.get("fieldwork_details"), errors)

    owner = record.get("owner_confirmation")
    if not _check_object(owner, OWNER_KEYS, "owner_confirmation", errors):
        owner = {}
    owner_status = owner.get("status")
    if not isinstance(owner_status, str) or owner_status not in OWNER_STATES:
        errors.append("owner_confirmation.status must be pending or confirmed")
        owner_status = "pending"
    confirmed_on = owner.get("confirmed_on")
    scope_reference = owner.get("scope_reference")
    if owner_status == "confirmed":
        if not _valid_date(confirmed_on):
            errors.append("owner_confirmation.confirmed_on must be a real YYYY-MM-DD date when confirmed")
        _optional_reference(scope_reference, "owner_confirmation.scope_reference", errors)
    else:
        if confirmed_on is not None:
            errors.append("owner_confirmation.confirmed_on must be null while status is pending")
        if scope_reference is not None:
            errors.append("owner_confirmation.scope_reference must be null while status is pending")

    blockers = _blockers(states, details, owner)
    all_approved = len(states) == len(APPROVAL_ITEMS) and all(states.get(item) == "approved" for item in APPROVAL_ITEMS)
    if owner_status == "confirmed" and (not all_approved or blockers):
        errors.append("owner confirmation cannot be recorded while any approval or required fieldwork detail is incomplete")
    if errors:
        return errors, blockers, {"status": "INVALID_INPUT"}

    report = {
        "report_version": 1,
        "decision_reference": "D-016",
        "status": "OWNER_AUTHORIZATION_RECORDED" if not blockers else "FIELDWORK_NOT_AUTHORIZED",
        "cohort": dict(COHORT),
        "approval_items": [
            {"item_id": item_id, "label": label, "status": states[item_id]}
            for item_id, label in APPROVAL_ITEMS.items()
        ],
        "summary": {
            "approval_item_count": len(APPROVAL_ITEMS),
            "approved_count": sum(state == "approved" for state in states.values()),
            "pending_count": sum(state == "pending" for state in states.values()),
            "rejected_count": sum(state == "rejected" for state in states.values()),
            "blocker_count": len(blockers),
            "owner_confirmation_recorded": owner_status == "confirmed",
        },
        "blockers": blockers,
        "limitations": [
            "This report records the contents of a private owner-authored authorization record; it does not authenticate the author or independently verify evidence references.",
            "A recorded authorization does not replace participant-by-participant informed consent or separate optional recording consent.",
            "This utility does not recruit, contact, schedule or interview participants; collect or process participant data; start recording; engage vendors; or authorize/execute payment.",
            "It is not legal, privacy, security, vendor or ethics approval and does not establish compliance with any applicable law.",
        ],
    }
    return errors, blockers, report


def _markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# M2-B Fieldwork Authorization Preflight",
        "",
        f"**Status:** {report['status']}",
        "",
        f"**Decision:** {report['decision_reference']}",
        "",
        "## Approved research-plan scope",
        "",
        "| Cohort context | Places |",
        "|---|---:|",
        f"| Home/interior | {report['cohort']['home_interior']} |",
        f"| Craft/material | {report['cohort']['craft_material']} |",
        f"| Trade/design | {report['cohort']['trade_design']} |",
        f"| Gift/considered-purchase | {report['cohort']['gift_considered_purchase']} |",
        f"| **Total** | **{report['cohort']['total']}** |",
        "",
        "## Authorization coverage",
        "",
        f"- Approval items: {summary['approved_count']}/{summary['approval_item_count']} approved",
        f"- Pending: {summary['pending_count']}",
        f"- Rejected: {summary['rejected_count']}",
        f"- Owner confirmation recorded: {'yes' if summary['owner_confirmation_recorded'] else 'no'}",
        "",
        "| Required owner approval | Status |",
        "|---|---|",
    ]
    for item in report["approval_items"]:
        lines.append(f"| {item['label']} | {item['status']} |")
    lines.extend(["", "## Remaining blockers", ""])
    if report["blockers"]:
        lines.extend(f"- {blocker}" for blocker in report["blockers"])
    else:
        lines.append("No structural blockers remain in the owner-authored record.")
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {item}" for item in report["limitations"])
    lines.append("")
    return "\n".join(lines)


def _write_new(path: Path, content: str) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(path, flags, 0o600)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        try:
            path.chmod(0o600)
        except OSError:
            pass
    except Exception:
        try:
            path.unlink()
        except OSError:
            pass
        raise


def build_fieldwork_authorization_report(record_path: Path, output_dir: Path) -> dict[str, Any]:
    record, output, path_errors = _safe_paths(record_path, output_dir)
    if path_errors:
        return {"ok": False, "status": "INVALID_INPUT", "errors": path_errors}

    try:
        raw = json.loads(record.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return {"ok": False, "status": "INVALID_INPUT", "errors": [f"cannot read authorization JSON: {exc}"]}

    errors, blockers, report = _validate_record(raw)
    if errors:
        return {"ok": False, "status": "INVALID_INPUT", "errors": errors, "blockers": blockers}

    try:
        output = ensure_private_directory(output)
        json_path = output / REPORT_JSON
        markdown_path = output / REPORT_MARKDOWN
        if json_path.exists() or markdown_path.exists():
            raise FileExistsError("authorization reports already exist; choose a new private output directory")
        _write_new(json_path, json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        try:
            _write_new(markdown_path, _markdown(report))
        except Exception:
            try:
                json_path.unlink()
            except OSError:
                pass
            raise
    except (OSError, RuntimeError) as exc:
        return {"ok": False, "status": "WRITE_ERROR", "errors": [f"cannot write private authorization report: {exc}"]}

    return {
        "ok": report["status"] == "OWNER_AUTHORIZATION_RECORDED",
        "status": report["status"],
        "summary": report["summary"],
        "blockers": report["blockers"],
        "json_report": str(json_path),
        "markdown_report": str(markdown_path),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", required=True, type=Path, help="private owner-authored D-016 authorization JSON")
    parser.add_argument("--output-dir", required=True, type=Path, help="new private report directory outside the record folder and repository")
    args = parser.parse_args(argv)
    result = build_fieldwork_authorization_report(args.record, args.output_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "OWNER_AUTHORIZATION_RECORDED":
        return 0
    if result["status"] == "FIELDWORK_NOT_AUTHORIZED":
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
