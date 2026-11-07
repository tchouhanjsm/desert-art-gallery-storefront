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

from build_etsy_review_bundle import build_private_review_bundle  # noqa: E402
from verify_etsy_review_bundle import main, verify_review_bundle  # noqa: E402

HEADERS = [
    "TITLE", "DESCRIPTION", "PRICE", "CURRENCY_CODE", "QUANTITY",
    "SKU", "MATERIALS", "TAGS", "IMAGE1", "IMAGE2",
]


def create_bundle(root: Path) -> Path:
    source_dir = root / "source"
    source_dir.mkdir()
    source = source_dir / "etsy.csv"
    with source.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(HEADERS)
        writer.writerow([
            "A title", "A description with\nmultiple lines", "120", "USD", "1",
            "SKU-A", "Cotton", "textile", "https://i.etsystatic.com/a.jpg", "",
        ])
        writer.writerow([
            "A title", "Another description", "120", "USD", "1",
            "SKU-A", "Wool", "object", "https://images.example.com/b.jpg", "",
        ])
    bundle = root.parent / (root.name + "-bundle")
    build_private_review_bundle(source, bundle)
    return bundle


class EtsyReviewBundleVerificationTests(unittest.TestCase):
    def test_builder_writes_manifest_and_verifier_accepts_complete_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = create_bundle(Path(tmp))
            manifest = json.loads((bundle / "bundle-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["manifest_format"], "dag-etsy-review-bundle-manifest-v1")
            self.assertEqual(len(manifest["files"]), 5)
            valid, errors = verify_review_bundle(bundle)
            self.assertTrue(valid, errors)
            self.assertEqual(main([str(bundle)]), 0)

    def test_verifier_detects_tampered_raw_source_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = create_bundle(Path(tmp))
            raw_file = bundle / "source-rows.jsonl"
            raw_file.write_text(raw_file.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            valid, errors = verify_review_bundle(bundle)
            self.assertFalse(valid)
            self.assertTrue(any("SHA-256 mismatch" in error for error in errors))

    def test_verifier_detects_missing_and_unexpected_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = create_bundle(Path(tmp))
            (bundle / "README.txt").unlink()
            (bundle / "surprise.txt").write_text("unexpected", encoding="utf-8")
            valid, errors = verify_review_bundle(bundle)
            self.assertFalse(valid)
            self.assertTrue(any("Missing expected files" in error for error in errors))
            self.assertTrue(any("Unexpected files present" in error for error in errors))

    def test_verifier_detects_image_rights_tampering_even_with_rebuilt_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            bundle = create_bundle(Path(tmp))
            image_path = bundle / "image-source-references.csv"
            with image_path.open("r", encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
                fields = list(rows[0].keys())
            rows[0]["rights_status"] = "approved"
            with image_path.open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)

            manifest_path = bundle / "bundle-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for entry in manifest["files"]:
                file_bytes = (bundle / entry["path"]).read_bytes()
                entry["bytes"] = len(file_bytes)
                entry["sha256"] = hashlib.sha256(file_bytes).hexdigest()
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

            valid, errors = verify_review_bundle(bundle)
            self.assertFalse(valid)
            self.assertTrue(any("rights must remain unknown" in error for error in errors))

    def test_verifier_rejects_symlinked_bundle_and_member(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = create_bundle(root)
            link = root / "bundle-link"
            try:
                link.symlink_to(bundle, target_is_directory=True)
                member_link = bundle / "note-link"
                member_link.symlink_to(bundle / "README.txt")
            except OSError:
                self.skipTest("symlinks are not available on this runner")
            self.assertFalse(verify_review_bundle(link)[0])
            self.assertFalse(verify_review_bundle(bundle)[0])


if __name__ == "__main__":
    unittest.main()
