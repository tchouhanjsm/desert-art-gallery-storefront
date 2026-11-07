from __future__ import annotations

import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from preview_etsy_export import main, preview_etsy_export  # noqa: E402


HEADERS = [
    "TITLE", "DESCRIPTION", "PRICE", "CURRENCY_CODE", "QUANTITY",
    "SKU", "MATERIALS", "TAGS", "IMAGE1", "IMAGE2",
    "VARIATION 1 TYPE", "VARIATION 1 NAME", "VARIATION 1 VALUES",
]


def write_export(path: Path, rows, headers=HEADERS, bom=False):
    with path.open("w", encoding="utf-8-sig" if bom else "utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


class EtsyExportPreviewTests(unittest.TestCase):
    def test_read_only_preview_detects_duplicate_titles_skus_and_remote_images(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "EtsyListingsDownload.csv"
            rows = [
                [
                    "Handmade jacket", "Description, with comma", "149.00", "USD", "1",
                    "SKU-1", "Cotton", "textile,handmade",
                    "https://i.etsystatic.com/123/photo-1.jpg",
                    "https://i.etsystatic.com/123/photo-2.jpg", "", "", "",
                ],
                [
                    "Handmade jacket", "Second piece", "199.00", "USD", "1",
                    "sku-1", "Wool", "jacket",
                    "https://images.example.com/photo.jpg", "", "", "", "",
                ],
            ]
            write_export(source, rows, bom=True)
            original = source.read_bytes()

            summary, previews, fatal = preview_etsy_export(source)

            self.assertFalse(fatal)
            self.assertEqual(source.read_bytes(), original)
            self.assertTrue(summary["read_only"])
            self.assertFalse(summary["imported"])
            self.assertEqual(summary["source_rows"], 2)
            self.assertEqual(summary["duplicate_sku_groups"], 1)
            self.assertEqual(summary["duplicate_sku_rows"], 2)
            self.assertEqual(summary["repeated_title_groups"], 1)
            self.assertEqual(summary["repeated_title_rows"], 2)
            self.assertEqual(summary["image_reference_count"], 3)
            self.assertEqual(summary["invalid_image_url_count"], 1)
            self.assertEqual(summary["empty_sku_rows"], 0)
            expected_hash = hashlib.sha256(original).hexdigest()
            self.assertEqual(previews[0]["source_record_ref"], f"etsy:{expected_hash}:row:1")
            self.assertTrue(previews[0]["source_sku_duplicate"])
            self.assertTrue(previews[1]["row_review_required"])

    def test_preview_counts_logical_rows_not_multiline_physical_lines(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "etsy.csv"
            row = [
                "Textile piece", "First paragraph\nSecond paragraph", "120", "USD", "1",
                "", "", "", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]
            write_export(source, [row])
            summary, previews, fatal = preview_etsy_export(source)
            self.assertFalse(fatal)
            self.assertEqual(summary["source_rows"], 1)
            self.assertEqual(previews[0]["source_data_row_number"], 1)
            self.assertEqual(summary["empty_sku_rows"], 1)

    def test_required_headers_and_image_slots_are_enforced(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "bad.csv"
            write_export(source, [["A", "B"]], headers=["TITLE", "DESCRIPTION"])
            summary, previews, fatal = preview_etsy_export(source)
            self.assertTrue(fatal)
            self.assertEqual(previews, [])
            codes = {item["code"] for item in summary["issues"]}
            self.assertIn("missing_required_headers", codes)
            self.assertIn("missing_image_columns", codes)

    def test_duplicate_headers_are_fatal(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "duplicate.csv"
            headers = HEADERS + ["TITLE"]
            row = ["X", "Y", "1", "USD", "1", "S", "Cotton", "tag", "", "", "", "", "", "X"]
            write_export(source, [row], headers=headers)
            summary, _, fatal = preview_etsy_export(source)
            self.assertTrue(fatal)
            self.assertIn("duplicate_headers", {item["code"] for item in summary["issues"]})

    def test_json_and_row_reports_are_written_privately_and_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "etsy.csv"
            write_export(source, [[
                "Textile piece", "Description", "149", "USD", "1",
                "SKU-1", "Cotton", "textile", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]])
            report_dir = root.parent / (root.name + "-private-reports")
            summary_path = report_dir / "report.json"
            rows_path = report_dir / "rows.csv"
            self.assertEqual(main([str(source), "--json", str(summary_path), "--rows-csv", str(rows_path)]), 0)
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            self.assertFalse(summary["imported"])
            with rows_path.open("r", encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            self.assertTrue(rows[0]["source_record_ref"].startswith("etsy:"))

            with self.assertRaises(SystemExit) as raised:
                main([str(source), "--json", str(summary_path)])
            self.assertEqual(raised.exception.code, 2)

    def test_rejects_report_paths_inside_source_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "etsy.csv"
            write_export(source, [[
                "Textile piece", "Description", "149", "USD", "1",
                "SKU-1", "Cotton", "textile", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]])
            with self.assertRaises(SystemExit) as raised:
                main([str(source), "--json", str(Path(tmp) / "summary.json")])
            self.assertEqual(raised.exception.code, 2)
            self.assertTrue(source.is_file())

    def test_rejects_symlinked_source_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            real = root / "real.csv"
            link = root / "link.csv"
            write_export(real, [[
                "Textile piece", "Description", "149", "USD", "1",
                "SKU-1", "Cotton", "textile", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]])
            try:
                link.symlink_to(real)
            except OSError:
                self.skipTest("symlinks are not available on this runner")
            with self.assertRaises(ValueError):
                preview_etsy_export(link)

    def test_flags_non_decimal_source_price(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "etsy.csv"
            write_export(source, [[
                "Textile piece", "Description", "USD 149", "USD", "1",
                "SKU-1", "Cotton", "textile", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]])
            summary, rows, fatal = preview_etsy_export(source)
            self.assertFalse(fatal)
            self.assertTrue(rows[0]["row_review_required"])
            self.assertIn("price_format_review", {issue["code"] for issue in summary["issues"]})

    def test_invalid_row_content_is_reported_without_importing(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "etsy.csv"
            write_export(source, [[
                "", "", "120", "", "one",
                "", "", "", "http://i.etsystatic.com/photo.jpg", "", "Size", "Size", "Large",
            ]])
            summary, previews, fatal = preview_etsy_export(source)
            self.assertFalse(fatal)
            self.assertEqual(summary["rows_requiring_review"], 1)
            self.assertGreater(summary["issue_count"], 0)
            self.assertTrue(previews[0]["row_review_required"])
            self.assertFalse(summary["imported"])


if __name__ == "__main__":
    unittest.main()
