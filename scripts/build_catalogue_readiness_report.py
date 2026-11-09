#!/usr/bin/env python3
"""Build a private, non-destructive DAG catalogue intake readiness report.

The report contains internal product IDs and blocker summaries only. It does
not copy source titles, descriptions, prices, source exports, or image files.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

try:
    from .validate_catalogue_intake import _load_photo_audit, _read_rows, _value, validate_catalogue_directory
except ImportError:
    from validate_catalogue_intake import _load_photo_audit, _read_rows, _value, validate_catalogue_directory  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
REPORT_JSON = "catalogue-readiness.json"
REPORT_MARKDOWN = "catalogue-readiness.md"


def _inside(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def _overlaps(left: Path, right: Path) -> bool:
    return _inside(left, right) or _inside(right, left)


def _rows(root: Path, filename: str) -> list[dict[str, str]]:
    parsed, _issues = _read_rows(root, filename, [])
    return [row for _line, row in parsed]


def _is_approved_fact(row: dict[str, str]) -> bool:
    return (
        _value(row, "verification_status") == "owner_verified"
        and bool(_value(row, "evidence_reference"))
        and _value(row, "prototype_use_approval") == "approved"
        and bool(_value(row, "prototype_use_evidence_reference"))
    )


def _is_approved_primary_image(row: dict[str, str], photo_inventory: dict[str, dict[str, str]] | None) -> bool:
    if (
        _value(row, "image_role") != "primary"
        or _value(row, "rights_status") != "cleared"
        or not _value(row, "rights_evidence_reference")
        or _value(row, "prototype_use_approval") != "approved"
        or not _value(row, "prototype_use_evidence_reference")
        or not _value(row, "alt_text_en")
        or photo_inventory is None
    ):
        return False
    audited = photo_inventory.get(_value(row, "source_relative_path"))
    return bool(
        audited and audited.get("status") == "ok"
        and not audited.get("duplicate_group")
        and audited.get("sha256") and audited.get("detected_format")
    )


def _safe_paths(directory: Path, output_dir: Path, photo_audit_csv: Path | None, photo_audit_summary: Path | None):
    errors: list[str] = []
    source_input = directory.expanduser()
    output_input = output_dir.expanduser()
    if source_input.is_symlink():
        errors.append("catalogue input directory must not be a symbolic link")
    if output_input.is_symlink():
        errors.append("report output directory must not be a symbolic link")
    if errors:
        return source_input, output_input, errors
    try:
        source = source_input.resolve(strict=True)
    except (OSError, RuntimeError):
        errors.append("catalogue input directory does not exist or cannot be resolved")
        source = source_input
    if not errors and not source.is_dir():
        errors.append("catalogue input path is not a directory")
    try:
        output = output_input.resolve(strict=False)
    except (OSError, RuntimeError):
        errors.append("report output path cannot be resolved")
        output = output_input
    repository = ROOT.resolve()
    if _overlaps(output, repository):
        errors.append("readiness reports must remain outside the public Git repository")
    if _overlaps(output, source):
        errors.append("readiness reports must remain separate from the catalogue source directory")
    for label, raw_path in (
        ("photo-audit CSV", photo_audit_csv),
        ("photo-audit summary", photo_audit_summary),
    ):
        if raw_path is None:
            continue
        expanded = raw_path.expanduser()
        if expanded.is_symlink():
            errors.append(f"{label} must not be a symbolic link")
            continue
        try:
            resolved = expanded.resolve(strict=True)
        except (OSError, RuntimeError):
            errors.append(f"{label} does not exist or cannot be resolved")
            continue
        if not resolved.is_file():
            errors.append(f"{label} is not a regular file")
        if _overlaps(resolved, repository):
            errors.append(f"{label} must remain outside the public Git repository")
        if _overlaps(resolved, source):
            errors.append(f"{label} must remain outside the catalogue source directory")
    return source, output, errors


def _product_readiness(products, sources, facts, images, photo_inventory):
    source_by_ref = {
        _value(row, "source_record_ref"): row
        for row in sources if _value(row, "source_record_ref")
    }
    facts_by_product: dict[str, list[dict[str, str]]] = {}
    images_by_product: dict[str, list[dict[str, str]]] = {}
    for row in facts:
        facts_by_product.setdefault(_value(row, "product_id"), []).append(row)
    for row in images:
        images_by_product.setdefault(_value(row, "product_id"), []).append(row)
    results: list[dict[str, Any]] = []
    seen: set[str] = set()
    for product in products:
        product_id = _value(product, "product_id")
        if not product_id or product_id in seen:
            continue
        seen.add(product_id)
        blockers: list[str] = []
        source = source_by_ref.get(_value(product, "source_record_ref"))
        source_ok = bool(
            source and _value(source, "product_id") == product_id
            and _value(source, "reconciliation_status") == "owner_reconciled"
        )
        if not source_ok:
            blockers.append("owner-reconciled source record and source-row reference")
        product_approval_ok = (
            _value(product, "prototype_use_approval") == "approved"
            and bool(_value(product, "prototype_use_evidence_reference"))
        )
        if not product_approval_ok:
            blockers.append("product-level private prototype-use approval/evidence")
        fact_ok = any(_is_approved_fact(row) for row in facts_by_product.get(product_id, []))
        if not fact_ok:
            blockers.append("at least one owner-verified, prototype-approved fact with evidence")
        primary_ok = any(
            _is_approved_primary_image(row, photo_inventory)
            for row in images_by_product.get(product_id, [])
        )
        if not primary_ok:
            blockers.append("rights-cleared, prototype-approved primary image matched to a clean photo audit")
        private_state_ok = _value(product, "publication_status") in {"draft", "in_review"}
        if not private_state_ok:
            blockers.append("product publication state draft/in_review (not public)")
        results.append({
            "product_id": product_id,
            "status": "READY" if not blockers else "BLOCKED",
            "source_record_ready": source_ok,
            "product_prototype_use_ready": product_approval_ok,
            "verified_fact_ready": fact_ok,
            "primary_image_ready": primary_ok,
            "private_publication_state": private_state_ok,
            "blockers": blockers,
        })
    return results


def _markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# DAG Private Catalogue Intake — Readiness Report", "",
        f"- Overall result: **{report['status']}**",
        f"- Validation mode: **{'M2 private sample' if report['m2_sample_enabled'] else 'general draft intake'}**",
        "- Privacy: internal product IDs and validation findings only; source titles, descriptions, prices, exports and images are not copied.",
        "", "## Intake summary", "", "| Measure | Count |", "|---|---:|",
        f"| Product records | {summary['product_records']} |",
        f"| Product fact rows | {summary['fact_rows']} |",
        f"| Owner-verified fact rows | {summary['owner_verified_fact_rows']} |",
        f"| Prototype-approved fact rows | {summary['prototype_approved_fact_rows']} |",
        f"| Product image rows | {summary['image_rows']} |",
        f"| Primary image rows | {summary['primary_image_rows']} |",
        f"| Rights-cleared image rows | {summary['rights_cleared_image_rows']} |",
        f"| Prototype-approved image rows | {summary['prototype_approved_image_rows']} |",
        f"| Source-record rows | {summary['source_record_rows']} |",
        f"| Owner-reconciled source rows | {summary['owner_reconciled_source_rows']} |",
        f"| Photo-audit records | {summary['photo_audit_records']} |",
        f"| Clean, readable, non-duplicate audit records | {summary['photo_audit_clean_records']} |",
        f"| Blocking validation findings | {summary['blocking_issue_count']} |", "",
    ]
    if report["m2_sample_enabled"]:
        lines.extend([
            "## M2 sample gate", "",
            "- Required product range: 10–20",
            f"- Product count in range: **{'yes' if summary['product_count_in_m2_range'] else 'no'}**",
            f"- Product-level ready records: {summary['product_ready_count']}/{summary['product_records']}",
            f"- Product-level blocked records: {summary['product_blocked_count']}", "",
            "| Product ID | Gate | Blockers |", "|---|---|---|",
        ])
        for product in report["products"]:
            blockers = "; ".join(product["blockers"]) if product["blockers"] else "None"
            lines.append(f"| {product['product_id']} | {product['status']} | {blockers} |")
        lines.append("")
    if report["validation_issues"]:
        lines.extend(["## Validation findings", ""])
        lines.extend(f"- {item}" for item in report["validation_issues"])
        lines.append("")
    lines.extend([
        "## Approval boundary", "",
        "This is a structural readiness report, not verification of real-world product claims or legal image rights. Private prototype-use approval is separate from public publication approval. No records were imported or modified.", "",
    ])
    return "\n".join(lines)


def build_catalogue_readiness_report(
    directory: Path,
    output_dir: Path,
    photo_audit_csv: Path | None = None,
    photo_audit_summary: Path | None = None,
    require_m2_sample: bool = False,
) -> dict[str, Any]:
    """Write JSON/Markdown readiness reports without changing intake inputs."""
    source, output, path_errors = _safe_paths(directory, output_dir, photo_audit_csv, photo_audit_summary)
    if path_errors:
        return {"ok": False, "status": "BLOCKED", "errors": path_errors}
    if bool(photo_audit_csv) != bool(photo_audit_summary):
        return {"ok": False, "status": "BLOCKED", "errors": ["photo-audit CSV and summary must be provided together"]}
    if require_m2_sample and (photo_audit_csv is None or photo_audit_summary is None):
        return {"ok": False, "status": "BLOCKED", "errors": ["M2 sample report requires both photo-audit CSV and summary"]}

    validation_issues = validate_catalogue_directory(source, photo_audit_csv, photo_audit_summary, require_m2_sample)
    products = _rows(source, "products.csv")
    facts = _rows(source, "product-facts.csv")
    images = _rows(source, "product-images.csv")
    sources = _rows(source, "product-source-records.csv")
    photo_inventory = None
    if photo_audit_csv is not None and photo_audit_summary is not None:
        photo_inventory, _photo_issues = _load_photo_audit(photo_audit_csv, photo_audit_summary)

    product_results = _product_readiness(products, sources, facts, images, photo_inventory)
    photo_records = list((photo_inventory or {}).values())
    unique_product_count = len(product_results)
    summary = {
        "product_records": len(products),
        "unique_product_count": unique_product_count,
        "fact_rows": len(facts),
        "owner_verified_fact_rows": sum(1 for row in facts if _value(row, "verification_status") == "owner_verified"),
        "prototype_approved_fact_rows": sum(
            1 for row in facts
            if _value(row, "prototype_use_approval") == "approved"
            and _value(row, "verification_status") == "owner_verified"
            and _value(row, "evidence_reference")
            and _value(row, "prototype_use_evidence_reference")
        ),
        "image_rows": len(images),
        "primary_image_rows": sum(1 for row in images if _value(row, "image_role") == "primary"),
        "rights_cleared_image_rows": sum(1 for row in images if _value(row, "rights_status") == "cleared"),
        "prototype_approved_image_rows": sum(1 for row in images if _value(row, "prototype_use_approval") == "approved"),
        "source_record_rows": len(sources),
        "owner_reconciled_source_rows": sum(1 for row in sources if _value(row, "reconciliation_status") == "owner_reconciled"),
        "photo_audit_records": len(photo_records),
        "photo_audit_clean_records": sum(
            1 for row in photo_records
            if row.get("status") == "ok" and not row.get("duplicate_group")
            and row.get("sha256") and row.get("detected_format")
        ),
        "blocking_issue_count": len(validation_issues),
        "product_count_in_m2_range": 10 <= unique_product_count <= 20,
        "product_ready_count": sum(1 for item in product_results if item["status"] == "READY"),
        "product_blocked_count": sum(1 for item in product_results if item["status"] == "BLOCKED"),
    }
    report: dict[str, Any] = {
        "report_schema_version": 1,
        "status": "READY" if not validation_issues else "BLOCKED",
        "m2_sample_enabled": require_m2_sample,
        "summary": summary,
        "products": product_results,
        "validation_issues": [str(issue) for issue in validation_issues],
    }
    report["ok"] = not validation_issues
    report["output_files"] = [REPORT_JSON, REPORT_MARKDOWN]

    output.mkdir(parents=True, exist_ok=True)
    json_path = output / REPORT_JSON
    markdown_path = output / REPORT_MARKDOWN
    if json_path.exists() or markdown_path.exists() or json_path.is_symlink() or markdown_path.is_symlink():
        return {"ok": False, "status": "BLOCKED", "errors": ["readiness report files already exist; choose an empty output directory"]}
    try:
        with json_path.open("x", encoding="utf-8") as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        with markdown_path.open("x", encoding="utf-8") as handle:
            handle.write(_markdown(report))
    except (OSError, UnicodeError) as exc:
        for path in (json_path, markdown_path):
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass
        return {"ok": False, "status": "BLOCKED", "errors": [f"could not write private readiness report ({type(exc).__name__})"]}
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a private DAG catalogue readiness report; never imports or modifies source data."
    )
    parser.add_argument("directory", type=Path, help="Private directory containing the five catalogue CSV files")
    parser.add_argument("--output-dir", type=Path, required=True, help="Private report directory outside the Git repository and catalogue source")
    parser.add_argument("--photo-audit-csv", type=Path, help="CSV inventory from one completed read-only photo audit")
    parser.add_argument("--photo-audit-summary", type=Path, help="JSON summary from the same photo-audit run")
    parser.add_argument("--m2-sample", action="store_true", help="Apply the 10–20 product private-prototype acceptance gate")
    args = parser.parse_args(argv)
    if bool(args.photo_audit_csv) != bool(args.photo_audit_summary):
        parser.error("--photo-audit-csv and --photo-audit-summary must be used together")
    if args.m2_sample and not args.photo_audit_csv:
        parser.error("--m2-sample requires both photo-audit reports")
    try:
        result = build_catalogue_readiness_report(
            args.directory, args.output_dir, args.photo_audit_csv,
            args.photo_audit_summary, args.m2_sample
        )
    except (OSError, RuntimeError, ValueError, csv.Error) as exc:
        print(f"Catalogue readiness report: FAILED ({type(exc).__name__})")
        return 1
    if not result.get("ok"):
        print(f"Catalogue readiness report: BLOCKED ({result.get('status', 'BLOCKED')})")
        for error in result.get("errors", []):
            print(f"- {error}")
        for issue in result.get("validation_issues", []):
            print(f"- {issue}")
        return 1
    print("Catalogue readiness report: READY")
    print(f"- Products: {result['summary']['product_records']}")
    print(f"- Owner-ready products: {result['summary']['product_ready_count']}")
    print(f"- Reports: {', '.join(result['output_files'])}")
    print("- Source CSVs, product photos and catalogue records were not modified or copied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
