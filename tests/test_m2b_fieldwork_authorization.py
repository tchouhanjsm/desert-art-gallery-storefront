from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_m2b_fieldwork_authorization import (
    APPROVAL_ITEMS,
    REPORT_JSON,
    REPORT_MARKDOWN,
    build_fieldwork_authorization_report,
)

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "m2b-fieldwork-authorization.template.json"


class M2BFieldworkAuthorizationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dag-m2b-auth-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.record_path = self.base / "private-record" / "owner-authorization.json"
        self.output_dir = self.base / "private-report"

    def template_record(self):
        return json.loads(TEMPLATE.read_text(encoding="utf-8"))

    def write_record(self, record):
        self.record_path.parent.mkdir(parents=True, exist_ok=True)
        self.record_path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")

    @staticmethod
    def leave_owner_confirmation_pending(record):
        record["owner_confirmation"] = {
            "status": "pending", "confirmed_on": None, "scope_reference": None
        }
        return record

    def complete_record(self):
        record = self.template_record()
        for item_id in APPROVAL_ITEMS:
            record["approvals"][item_id] = {
                "status": "approved",
                "approved_on": "2026-11-10",
                "evidence_reference": f"PRIVATE-APPROVAL-{item_id}",
            }
        record["fieldwork_details"].update({
            "moderator_reference": "PRIVATE-MODERATOR-REVIEW",
            "session_languages": ["English"],
            "participant_information_reference": "PRIVATE-PARTICIPANT-INFORMATION",
            "consent_wording_reference": "PRIVATE-CONSENT-WORDING",
            "recording_mode": "no_recording",
            "recording_consent_reference": None,
            "storage_reference": "PRIVATE-STORAGE-PLAN",
            "access_control_reference": "PRIVATE-ACCESS-PLAN",
            "retention_days": 30,
            "deletion_reference": "PRIVATE-DELETION-PLAN",
            "transfer_mode": "none",
            "transfer_review_reference": None,
            "vendor_mode": "no_vendor",
            "vendor_terms_reference": None,
            "spend_currency": "INR",
            "spend_ceiling": "10000.00",
            "budget_breakdown_reference": "PRIVATE-BUDGET-APPROVAL",
            "schedule_timezone": "Asia/Tokyo",
            "start_date": "2026-12-01",
            "end_date": "2026-12-31",
            "schedule_reference": "PRIVATE-SCHEDULE-PLAN",
        })
        record["owner_confirmation"] = {
            "status": "confirmed",
            "confirmed_on": "2026-11-10",
            "scope_reference": "PRIVATE-OWNER-WRITTEN-AUTHORIZATION",
        }
        return record

    def test_pending_template_reports_all_eight_owner_dependencies(self):
        self.write_record(self.template_record())
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertEqual(result["summary"]["approval_item_count"], 8)
        self.assertEqual(result["summary"]["approved_count"], 0)
        self.assertGreaterEqual(result["summary"]["blocker_count"], 8)
        self.assertTrue((self.output_dir / REPORT_JSON).is_file())
        self.assertTrue((self.output_dir / REPORT_MARKDOWN).is_file())

    def test_complete_owner_record_reports_recorded_authorization_not_execution(self):
        self.write_record(self.complete_record())
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertTrue(result["ok"])
        self.assertEqual(result["status"], "OWNER_AUTHORIZATION_RECORDED")
        self.assertEqual(result["summary"]["approved_count"], 8)
        saved = json.loads((self.output_dir / REPORT_JSON).read_text(encoding="utf-8"))
        self.assertEqual(saved["status"], "OWNER_AUTHORIZATION_RECORDED")
        self.assertTrue(any("does not recruit" in item for item in saved["limitations"]))

    def test_report_excludes_private_evidence_references(self):
        record = self.complete_record()
        record["approvals"]["research_budget"]["evidence_reference"] = "PRIVATE-SECRET-BUDGET-REF"
        record["fieldwork_details"]["moderator_reference"] = "PRIVATE-MODERATOR-IDENTITY-REF"
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertTrue(result["ok"])
        output = (self.output_dir / REPORT_JSON).read_text(encoding="utf-8")
        markdown = (self.output_dir / REPORT_MARKDOWN).read_text(encoding="utf-8")
        self.assertNotIn("PRIVATE-SECRET-BUDGET-REF", output)
        self.assertNotIn("PRIVATE-MODERATOR-IDENTITY-REF", output)
        self.assertNotIn("PRIVATE-SECRET-BUDGET-REF", markdown)

    def test_each_approval_gate_is_required(self):
        for item_id in APPROVAL_ITEMS:
            with self.subTest(item_id=item_id):
                output_dir = self.base / f"report-{item_id}"
                record = self.complete_record()
                record["approvals"][item_id] = {
                    "status": "pending", "approved_on": None, "evidence_reference": None
                }
                self.leave_owner_confirmation_pending(record)
                self.write_record(record)
                result = build_fieldwork_authorization_report(self.record_path, output_dir)
                self.assertFalse(result["ok"])
                self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
                self.assertTrue(any(APPROVAL_ITEMS[item_id] in item for item in result["blockers"]))

    def test_rejected_approval_blocks_fieldwork(self):
        record = self.complete_record()
        record["approvals"]["vendor_processing_and_transfer"] = {
            "status": "rejected", "approved_on": None, "evidence_reference": None
        }
        self.leave_owner_confirmation_pending(record)
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertTrue(any("approval rejected" in item for item in result["blockers"]))

    def test_cohort_counts_cannot_be_changed(self):
        record = self.template_record()
        record["cohort"]["home_interior"] = 4
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("approved count" in item for item in result["errors"]))

    def test_boolean_schema_version_is_not_accepted_as_integer(self):
        record = self.template_record()
        record["schema_version"] = True
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertIn("schema_version must be integer 1", result["errors"])

    def test_boolean_retention_days_is_rejected(self):
        record = self.complete_record()
        record["fieldwork_details"]["retention_days"] = True
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("retention_days must be null or an integer" in item for item in result["errors"]))

    def test_invalid_calendar_dates_are_rejected(self):
        record = self.complete_record()
        record["fieldwork_details"]["start_date"] = "2026-02-30"
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("start_date must be null or a real" in item for item in result["errors"]))

    def test_end_date_before_start_date_is_rejected(self):
        record = self.complete_record()
        record["fieldwork_details"]["start_date"] = "2026-12-31"
        record["fieldwork_details"]["end_date"] = "2026-12-01"
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("end_date must be on or after" in item for item in result["errors"]))

    def test_confirmation_cannot_override_pending_approval(self):
        record = self.complete_record()
        record["approvals"]["research_budget"] = {
            "status": "pending", "approved_on": None, "evidence_reference": None
        }
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("owner confirmation cannot be recorded" in item for item in result["errors"]))

    def test_recording_requires_an_explicit_mode(self):
        record = self.leave_owner_confirmation_pending(self.complete_record())
        record["fieldwork_details"]["recording_mode"] = "not_authorized"
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertTrue(any("recording approach is undecided" in item.lower() for item in result["blockers"]))

    def test_optional_recording_requires_separate_consent_wording(self):
        record = self.leave_owner_confirmation_pending(self.complete_record())
        record["fieldwork_details"]["recording_mode"] = "optional_separate_participant_consent"
        record["fieldwork_details"]["recording_consent_reference"] = None
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertTrue(any("Separate optional recording-consent wording" in item for item in result["blockers"]))

    def test_each_data_handling_dependency_is_required(self):
        record = self.leave_owner_confirmation_pending(self.complete_record())
        details = record["fieldwork_details"]
        details["storage_reference"] = None
        details["access_control_reference"] = None
        details["retention_days"] = None
        details["deletion_reference"] = None
        details["transfer_mode"] = "unreviewed"
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertTrue(any("storage arrangement" in item for item in result["blockers"]))
        self.assertTrue(any("access-control" in item for item in result["blockers"]))
        self.assertTrue(any("retention period" in item for item in result["blockers"]))
        self.assertTrue(any("deletion procedure" in item for item in result["blockers"]))
        self.assertTrue(any("transfer arrangement" in item for item in result["blockers"]))

    def test_vendor_involvement_requires_terms_reference(self):
        record = self.leave_owner_confirmation_pending(self.complete_record())
        record["fieldwork_details"]["vendor_mode"] = "vendor_involved"
        record["fieldwork_details"]["vendor_terms_reference"] = None
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertTrue(any("Vendor terms" in item for item in result["blockers"]))

    def test_currency_and_spend_ceiling_must_be_explicit(self):
        record = self.leave_owner_confirmation_pending(self.complete_record())
        record["fieldwork_details"]["spend_currency"] = None
        record["fieldwork_details"]["spend_ceiling"] = None
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertTrue(any("research-spend currency" in item for item in result["blockers"]))
        self.assertTrue(any("spend ceiling" in item for item in result["blockers"]))

    def test_approval_requires_date_and_evidence_reference(self):
        record = self.complete_record()
        record["approvals"]["recruitment_route"]["evidence_reference"] = None
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("recruitment_route.evidence_reference" in item for item in result["errors"]))

    def test_unknown_fields_fail_closed(self):
        record = self.template_record()
        record["unexpected"] = "not permitted"
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("unsupported field" in item for item in result["errors"]))

    def test_malformed_nested_types_fail_without_traceback(self):
        record = self.template_record()
        record["approvals"]["moderator_and_language"] = ["approved"]
        record["fieldwork_details"]["session_languages"] = "English"
        record["owner_confirmation"] = ["confirmed"]
        self.write_record(record)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertGreaterEqual(len(result["errors"]), 3)

    def test_record_symlink_is_rejected(self):
        real = self.base / "real-record.json"
        real.write_text(json.dumps(self.template_record()), encoding="utf-8")
        alias = self.base / "record-link.json"
        alias.symlink_to(real)
        result = build_fieldwork_authorization_report(alias, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("symbolic links" in item for item in result["errors"]))

    def test_report_inside_public_repository_is_rejected(self):
        self.write_record(self.template_record())
        output = ROOT / "fieldwork-report-must-not-exist"
        result = build_fieldwork_authorization_report(self.record_path, output)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("outside the public Git repository" in item for item in result["errors"]))
        self.assertFalse(output.exists())

    def test_output_overlapping_record_directory_is_rejected(self):
        self.write_record(self.template_record())
        result = build_fieldwork_authorization_report(self.record_path, self.record_path.parent / "nested-report")
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("separate from the private record directory" in item for item in result["errors"]))

    def test_existing_report_directory_is_tightened_to_owner_only(self):
        import os
        import stat

        if os.name != "posix":
            self.skipTest("POSIX directory permission bits are not available")
        self.write_record(self.template_record())
        self.output_dir.mkdir(mode=0o755)
        self.output_dir.chmod(0o755)
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "FIELDWORK_NOT_AUTHORIZED")
        self.assertEqual(stat.S_IMODE(self.output_dir.stat().st_mode) & 0o077, 0)

    def test_existing_reports_are_never_overwritten(self):
        self.write_record(self.template_record())
        self.output_dir.mkdir()
        existing = self.output_dir / REPORT_JSON
        existing.write_text('{"keep": true}', encoding="utf-8")
        result = build_fieldwork_authorization_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "WRITE_ERROR")
        self.assertEqual(json.loads(existing.read_text(encoding="utf-8")), {"keep": True})
        self.assertFalse((self.output_dir / REPORT_MARKDOWN).exists())


if __name__ == "__main__":
    unittest.main()
