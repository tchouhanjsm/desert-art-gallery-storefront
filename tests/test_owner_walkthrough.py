from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_owner_walkthrough import (
    REPORT_JSON,
    REPORT_MARKDOWN,
    VIEWPORTS,
    build_owner_walkthrough_report,
)

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "owner-walkthrough-record.template.json"


class OwnerWalkthroughTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.record_path = self.base / "owner-walkthrough.json"
        self.output_dir = self.base / "private-report"

    def load_template(self):
        return json.loads(TEMPLATE.read_text(encoding="utf-8"))

    def write_record(self, record):
        self.record_path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")

    def mark_all_accepted(self, record):
        record["review_date"] = "2026-11-10"
        record["owner_confirmation"] = "confirmed"
        record["confirmation_date"] = "2026-11-10"
        for area in record["areas"]:
            area["decision"] = "accept"
            for width in VIEWPORTS:
                area["viewport_reviews"][width] = {"status":"reviewed","notes":f"Reviewed at {width} CSS px."}
            area["observations"] = {
                "visual_hierarchy_and_density": "Hierarchy and density reviewed; no outstanding issue.",
                "image_ratio_crop_placeholder_clarity": "Image frames and pending labels reviewed.",
                "content_and_factual_evidence_gaps": "Pending factual evidence remains clearly identified.",
                "navigation_and_shared_shell": "Existing navigation and shared shell reviewed.",
                "keyboard_focus_and_disabled_state_clarity": "Focus and disabled states reviewed.",
            }
        return record

    def test_pending_template_generates_incomplete_private_summary(self):
        record = self.load_template()
        record["areas"][0]["observations"]["visual_hierarchy_and_density"] = "PRIVATE OWNER NOTE — do not include in summary"
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "REVIEW_INCOMPLETE")
        self.assertEqual(result["summary"]["area_count"], 6)
        self.assertEqual(result["summary"]["expected_viewport_count"], 30)
        markdown = (self.output_dir / REPORT_MARKDOWN).read_text(encoding="utf-8")
        self.assertNotIn("PRIVATE OWNER NOTE", markdown)
        self.assertNotIn("PRIVATE OWNER NOTE", (self.output_dir / REPORT_JSON).read_text(encoding="utf-8"))

    def test_all_six_areas_and_thirty_viewports_can_be_owner_confirmed(self):
        record = self.mark_all_accepted(self.load_template())
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertTrue(result["ok"])
        self.assertEqual(result["status"], "OWNER_VISUAL_ACCEPTED")
        self.assertEqual(result["summary"]["accepted_area_count"], 6)
        self.assertEqual(result["summary"]["reviewed_viewport_count"], 30)
        saved = json.loads((self.output_dir / REPORT_JSON).read_text(encoding="utf-8"))
        self.assertEqual(saved["status"], "OWNER_VISUAL_ACCEPTED")
        self.assertNotIn("observations", saved["areas"][0])

    def test_acceptance_is_rejected_until_all_five_widths_are_reviewed(self):
        record = self.mark_all_accepted(self.load_template())
        record["areas"][0]["viewport_reviews"]["390"] = {"status":"pending","notes":""}
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("all five approved viewport widths" in item for item in result["errors"]))
        self.assertFalse(self.output_dir.exists())

    def test_revision_request_requires_route_and_component_scoped_detail(self):
        record = self.load_template()
        area = record["areas"][0]
        area["decision"] = "request_revision"
        record["review_date"] = "2026-11-10"
        for width in VIEWPORTS:
            area["viewport_reviews"][width] = {"status":"reviewed","notes":f"Reviewed {width}."}
        area["observations"] = {key:"Reviewed; revise hierarchy." for key in area["observations"]}
        area["requested_changes"] = [{
            "route":"index.html",
            "component":"Hero",
            "request":"Owner requests a documented hierarchy adjustment within the approved composition."
        }]
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertFalse(result["ok"])
        self.assertEqual(result["status"], "REVISION_REQUIRED")
        saved = json.loads((self.output_dir / REPORT_JSON).read_text(encoding="utf-8"))
        self.assertEqual(saved["areas"][0]["requested_change_count"], 1)
        self.assertNotIn("Owner requests a documented", json.dumps(saved))

    def test_reject_requires_at_least_one_requested_change(self):
        record = self.load_template()
        area = record["areas"][0]
        area["decision"] = "reject"
        record["review_date"] = "2026-11-10"
        for width in VIEWPORTS:
            area["viewport_reviews"][width] = {"status":"reviewed","notes":"Reviewed."}
        area["observations"] = {key:"Reviewed." for key in area["observations"]}
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("at least one route/component-scoped" in item for item in result["errors"]))

    def test_owner_confirmation_cannot_override_a_pending_area(self):
        record = self.mark_all_accepted(self.load_template())
        record["areas"][2]["decision"] = "pending"
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("all six areas to be accepted" in item for item in result["errors"]))

    def test_boolean_schema_version_is_not_accepted_as_integer(self):
        record = self.load_template()
        record["schema_version"] = True
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertIn("schema_version must be integer 1", result["errors"])

    def test_impossible_review_date_is_rejected(self):
        record = self.load_template()
        record["review_date"] = "2026-02-30"
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("real YYYY-MM-DD" in item for item in result["errors"]))

    def test_duplicate_area_and_unknown_route_are_rejected(self):
        record = self.load_template()
        record["areas"][1]["area_id"] = record["areas"][0]["area_id"]
        record["areas"][0]["decision"] = "request_revision"
        record["areas"][0]["requested_changes"] = [{
            "route":"pages/not-approved.html","component":"unknown","request":"Test."
        }]
        record["review_date"] = "2026-11-10"
        for width in VIEWPORTS:
            record["areas"][0]["viewport_reviews"][width] = {"status":"reviewed","notes":"Reviewed."}
        record["areas"][0]["observations"] = {key:"Reviewed." for key in record["areas"][0]["observations"]}
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("duplicate review area" in item for item in result["errors"]))
        self.assertTrue(any("one of the nine D-014 routes" in item for item in result["errors"]))

    def test_record_inside_public_repository_is_rejected(self):
        result = build_owner_walkthrough_report(TEMPLATE, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("outside the public Git repository" in item for item in result["errors"]))
        self.assertFalse(self.output_dir.exists())

    def test_output_inside_public_repository_is_rejected(self):
        self.write_record(self.load_template())
        result = build_owner_walkthrough_report(self.record_path, ROOT / "owner-walkthrough-must-not-exist")
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("outside the public Git repository" in item for item in result["errors"]))

    def test_existing_report_directory_is_tightened_to_owner_only(self):
        import os
        import stat

        if os.name != "posix":
            self.skipTest("POSIX directory permission bits are not available")
        self.write_record(self.load_template())
        self.output_dir.mkdir(mode=0o755)
        self.output_dir.chmod(0o755)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "REVIEW_INCOMPLETE")
        self.assertEqual(stat.S_IMODE(self.output_dir.stat().st_mode) & 0o077, 0)

    def test_symlinked_parent_output_path_is_rejected(self):
        self.write_record(self.load_template())
        target = self.base / "external-report-parent"
        target.mkdir()
        alias = self.base / "report-parent-link"
        try:
            alias.symlink_to(target, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("directory symlinks are unavailable on this runner")
        result = build_owner_walkthrough_report(self.record_path, alias / "report")
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("symbolic links" in item for item in result["errors"]))
        self.assertEqual(list(target.iterdir()), [])

    def test_existing_reports_are_never_overwritten(self):
        self.write_record(self.load_template())
        self.output_dir.mkdir()
        existing = self.output_dir / REPORT_JSON
        existing.write_text('{"keep":true}', encoding="utf-8")
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertEqual(json.loads(existing.read_text(encoding="utf-8")), {"keep": True})
        self.assertFalse((self.output_dir / REPORT_MARKDOWN).exists())

    def test_symlinked_private_record_is_rejected(self):
        real = self.base / "real-record.json"
        real.write_text(json.dumps(self.load_template()), encoding="utf-8")
        alias = self.base / "record-link.json"
        try:
            alias.symlink_to(real)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks are unavailable on this runner")
        result = build_owner_walkthrough_report(alias, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("symbolic links" in item for item in result["errors"]))

    def test_malformed_nested_types_fail_closed_without_traceback(self):
        record = self.load_template()
        record["owner_confirmation"] = {"state": "pending"}
        record["areas"][0]["decision"] = ["accept"]
        record["areas"][0]["viewport_reviews"]["390"]["status"] = {"state": "reviewed"}
        record["areas"][0]["requested_changes"] = [{
            "route": ["index.html"], "component": "Hero", "request": "Review."
        }]
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertGreaterEqual(len(result["errors"]), 3)
        self.assertFalse(self.output_dir.exists())

    def test_invalid_decision_state_is_rejected(self):
        record = self.load_template()
        record["areas"][0]["decision"] = "accepted"
        self.write_record(record)
        result = build_owner_walkthrough_report(self.record_path, self.output_dir)
        self.assertEqual(result["status"], "INVALID_INPUT")
        self.assertTrue(any("areas[0].decision" in item for item in result["errors"]))


if __name__ == "__main__":
    unittest.main()
