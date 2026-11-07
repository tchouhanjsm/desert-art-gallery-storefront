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

from build_etsy_review_bundle import build_private_review_bundle, main  # noqa: E402


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


class EtsyReviewBundleTests(unittest.TestCase):
    def test_bundle_preserves_raw_rows_and_separates_image_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "etsy.csv"
            multiline = "First paragraph\nSecond paragraph, preserved"
            rows = [
                [
                    "Textile title", multiline, "120", "USD", "1", "SKU-A", "Cotton",
                    "tag-a,tag-b", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
                ],
                [
                    "Textile title", "Second description", "120", "USD", "1", "SKU-A", "Wool",
                    "tag-c", "https://images.example.com/review.jpg", "", "", "", "",
                ],
            ]
            write_export(source, rows, bom=True)
            source_before = source.read_bytes()
            bundle = root.parent / (root.name + "-review-bundle")

            result = build_private_review_bundle(source, bundle)

            self.assertEqual(source.read_bytes(), source_before)
            self.assertEqual(result["source_rows"], 2)
            self.assertEqual(result["image_source_rows"], 2)
            summary = json.loads((bundle / "source-summary.json").read_text(encoding="utf-8"))
            self.assertEqual(summary["bundle_format"], "dag-etsy-private-review-bundle-v1")
            self.assertFalse(summary["product_assignments_created"])
            self.assertFalse(summary["image_downloaded"])
            self.assertEqual(summary["source_sha256"], hashlib.sha256(source_before).hexdigest())

            raw_lines = (bundle / "source-rows.jsonl").read_text(encoding="utf-8").splitlines()
            raw_records = [json.loads(line) for line in raw_lines]
            self.assertEqual(len(raw_records), 2)
            self.assertEqual(raw_records[0]["source_fields"]["DESCRIPTION"], multiline)
            self.assertEqual(raw_records[0]["source_fields"]["SKU"], "SKU-A")
            self.assertEqual(raw_records[1]["source_record_ref"], f"etsy:{summary['source_sha256']}:row:2")
            self.assertEqual(raw_records[0]["source_fields"]["TAGS"], "tag-a,tag-b")

            with (bundle / "image-source-references.csv").open("r", encoding="utf-8-sig", newline="") as handle:
                image_rows = list(csv.DictReader(handle))
            self.assertEqual(len(image_rows), 2)
            self.assertEqual(image_rows[0]["source_url_status"], "allowed_source_host")
            self.assertEqual(image_rows[1]["source_url_status"], "review_required")
            self.assertEqual(image_rows[0]["local_asset_id"], "")
            self.assertEqual(image_rows[0]["rights_status"], "unknown")
            self.assertEqual(image_rows[0]["publication_status"], "not_approved")
            self.assertNotIn("product_id", image_rows[0])
            self.assertTrue((bundle / "source-row-review.csv").is_file())
            self.assertTrue((bundle / "README.txt").is_file())

    def test_bundle_cli_creates_package_and_refuses_existing_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_dir = root / "source"
            source_dir.mkdir()
            source = source_dir / "etsy.csv"
            write_export(source, [[
                "Textile piece", "Description", "149", "USD", "1",
                "SKU-1", "Cotton", "textile", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]])
            bundle = root / "private-review"
            self.assertEqual(main([str(source), str(bundle)]), 0)
            self.assertTrue((bundle / "source-rows.jsonl").is_file())
            self.assertEqual(main([str(source), str(bundle)]), 2)

    def test_bundle_rejects_destination_inside_source_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "etsy.csv"
            write_export(source, [[
                "Textile piece", "Description", "149", "USD", "1",
                "SKU-1", "Cotton", "textile", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]])
            with self.assertRaises(ValueError):
                build_private_review_bundle(source, root / "nested" / "bundle")

    def test_bundle_rejects_destination_inside_git_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "etsy.csv"
            write_export(source, [[
                "Textile piece", "Description", "149", "USD", "1",
                "SKU-1", "Cotton", "textile", "https://i.etsystatic.com/photo.jpg", "", "", "", "",
            ]])
            repository = root / "repository"
            repository.mkdir()
            (repository / ".git").mkdir()
            with self.assertRaises(ValueError):
                build_private_review_bundle(source, repository / "private-bundle")

    def test_bundle_rejects_fatal_export_and_symlinked_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / "bad.csv"
            write_export(bad, [["Title", "Description"]], headers=["TITLE", "DESCRIPTION"])
            with self.assertRaises(ValueError):
                build_private_review_bundle(bad, root / "bad-bundle")

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
            self.assertEqual(main([str(link), str(root.parent / (root.name + "-link-bundle"))]), 2)

    def test_bundle_records_extra_cells_and_missing_cells_without_losing_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "etsy.csv"
            with source.open("w", encoding="utf-8", newline="") as handle:
                handle.write("TITLE,DESCRIPTION,PRICE,CURRENCY_CODE,QUANTITY,IMAGE1,EXTRA\n")
                handle.write('Piece,Description,10,USD,1,https://i.etsystatic.com/a.jpg,extra,unexpected\n')
                handle.write('Piece 2,Description,10,USD,1,https://i.etsystatic.com/b.jpg\n')
            bundle = root.parent / (root.name + "-review")
            result = build_private_review_bundle(source, bundle)
            self.assertEqual(result["source_rows"], 2)
            records = [
                json.loads(line)
                for line in (bundle / "source-rows.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual(records[0]["extra_cells"], ["unexpected"])
            self.assertEqual(records[1]["source_fields"]["EXTRA"], "")

    def test_bundle_does_not_modify_source_or_download_anything(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "etsy.csv"
            write_export(source, [[
                "Piece", "Description", "10", "USD", "1",
                "SKU", "", "", "https://i.etsystatic.com/a.jpg", "", "", "", "",
            ]])
            original = source.read_bytes()
            bundle = root.parent / (root.name + "-private-bundle")
            build_private_review_bundle(source, bundle)
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(
                sorted(path.name for path in bundle.iterdir()),
                [
                    "README.txt",
                    "image-source-references.csv",
                    "source-row-review.csv",
                    "source-rows.jsonl",
                    "source-summary.json",
                ],
            )


if __name__ == "__main__":
    unittest.main()
