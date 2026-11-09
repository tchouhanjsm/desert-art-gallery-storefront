from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from test_catalogue_intake import CatalogueIntakeTests, write_package
ROOT = Path(__file__).resolve().parents[1]
from scripts.build_catalogue_readiness_report import build_catalogue_readiness_report


class CatalogueReadinessReportTests(unittest.TestCase):
    def test_valid_m2_sample_produces_private_ready_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = base / "catalogue"
            output = base / "private-readiness"
            fixture = CatalogueIntakeTests()
            audit_csv, audit_json, _products, _facts, _images = fixture.write_m2_sample(source, 10)
            result = build_catalogue_readiness_report(source, output, audit_csv, audit_json, require_m2_sample=True)
            self.assertTrue(result["ok"])
            self.assertEqual(result["status"], "READY")
            self.assertEqual(result["summary"]["product_ready_count"], 10)
            self.assertEqual(result["summary"]["product_blocked_count"], 0)
            self.assertTrue((output / "catalogue-readiness.json").is_file())
            self.assertTrue((output / "catalogue-readiness.md").is_file())
            saved = json.loads((output / "catalogue-readiness.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["summary"]["unique_product_count"], 10)
            self.assertTrue(saved["ok"])

    def test_underfilled_m2_sample_writes_blockers_without_copying_product_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = base / "catalogue"
            output = base / "private-readiness"
            fixture = CatalogueIntakeTests()
            audit_csv, audit_json, _products, _facts, _images = fixture.write_m2_sample(source, 9)
            result = build_catalogue_readiness_report(source, output, audit_csv, audit_json, require_m2_sample=True)
            self.assertFalse(result["ok"])
            self.assertEqual(result["status"], "BLOCKED")
            self.assertEqual(result["summary"]["product_records"], 9)
            markdown = (output / "catalogue-readiness.md").read_text(encoding="utf-8")
            self.assertIn("10–20", markdown)
            self.assertNotIn("Sample title", markdown)
            self.assertNotIn("Synthetic verified fixture fact", markdown)
            self.assertIn("p-001", markdown)

    def test_report_output_inside_catalogue_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "catalogue"
            source.mkdir()
            output = source / "reports"
            result = build_catalogue_readiness_report(source, output)
            self.assertFalse(result["ok"])
            self.assertTrue(any("separate from the catalogue source" in item for item in result["errors"]))
            self.assertFalse(output.exists())

    def test_report_output_inside_public_repository_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "catalogue"
            source.mkdir()
            output = ROOT / "readiness-report-must-not-be-created"
            result = build_catalogue_readiness_report(source, output)
            self.assertFalse(result["ok"])
            self.assertTrue(any("outside the public Git repository" in item for item in result["errors"]))
            self.assertFalse(output.exists())

    def test_report_does_not_overwrite_existing_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = base / "catalogue"
            source.mkdir()
            output = base / "reports"
            output.mkdir()
            existing = output / "catalogue-readiness.json"
            existing.write_text('{"owner":"keep"}', encoding="utf-8")
            result = build_catalogue_readiness_report(source, output)
            self.assertFalse(result["ok"])
            self.assertEqual(json.loads(existing.read_text(encoding="utf-8")), {"owner": "keep"})
            self.assertFalse((output / "catalogue-readiness.md").exists())

    def test_product_blockers_are_separated_by_approval_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            source = base / "catalogue"
            output = base / "private-readiness"
            fixture = CatalogueIntakeTests()
            audit_csv, audit_json, products, facts, images = fixture.write_m2_sample(source, 10)
            products[0]["prototype_use_approval"] = "not_reviewed"
            facts[1]["prototype_use_approval"] = "not_reviewed"
            images[2]["rights_status"] = "unknown"
            with (source / "product-source-records.csv").open(encoding="utf-8", newline="") as handle:
                source_rows = list(csv.DictReader(handle))
            write_package(source, products=products, facts=facts, images=images, sources=source_rows)
            result = build_catalogue_readiness_report(source, output, audit_csv, audit_json, require_m2_sample=True)
            product_map = {item["product_id"]: item for item in result["products"]}
            self.assertFalse(product_map["p-001"]["product_prototype_use_ready"])
            self.assertTrue(product_map["p-001"]["source_record_ready"])
            self.assertIn("product-level private prototype-use approval/evidence", product_map["p-001"]["blockers"])
            self.assertFalse(product_map["p-002"]["verified_fact_ready"])
            self.assertFalse(product_map["p-003"]["primary_image_ready"])


if __name__ == "__main__":
    unittest.main()
