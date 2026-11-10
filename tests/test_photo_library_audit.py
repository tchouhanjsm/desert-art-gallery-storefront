from __future__ import annotations

import csv
import hashlib
import json
import struct
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_photo_library  # noqa: E402
from audit_photo_library import audit_directory, detect_format, main, read_dimensions  # noqa: E402


def png_bytes(width: int, height: int) -> bytes:
    return b"\x89PNG\r\n\x1a\n" + struct.pack(">I", 13) + b"IHDR" + struct.pack(">II", width, height) + b"\x08\x02\x00\x00\x00"


def jpeg_bytes(width: int, height: int) -> bytes:
    return b"\xff\xd8\xff\xc0\x00\x11\x08" + height.to_bytes(2, "big") + width.to_bytes(2, "big") + b"\x03\x01\x11\x00\x02\x11\x00\x03\x11\x00"


def webp_vp8x_bytes(width: int, height: int) -> bytes:
    payload = bytes([0, 0, 0, 0]) + (width - 1).to_bytes(3, "little") + (height - 1).to_bytes(3, "little")
    chunk = b"VP8X" + len(payload).to_bytes(4, "little") + payload
    body = b"WEBP" + chunk
    return b"RIFF" + len(body).to_bytes(4, "little") + body


class PhotoLibraryAuditTests(unittest.TestCase):
    def test_detects_png_and_reads_dimensions(self):
        data = png_bytes(1600, 1200)
        self.assertEqual(detect_format(data), "PNG")
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "image.png"
            p.write_bytes(data)
            self.assertEqual(read_dimensions(p, "PNG"), (1600, 1200))

    def test_reads_jpeg_dimensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "image.jpg"
            p.write_bytes(jpeg_bytes(2400, 1600))
            self.assertEqual(read_dimensions(p, "JPEG"), (2400, 1600))

    def test_reads_gif_and_bmp_dimensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            gif = root / "image.gif"
            gif.write_bytes(b"GIF89a" + struct.pack("<HH", 700, 500))
            bmp = root / "image.bmp"
            bmp.write_bytes(b"BM" + b"\x00" * 12 + struct.pack("<I", 40) + struct.pack("<ii", 900, 600))
            self.assertEqual(read_dimensions(gif, "GIF"), (700, 500))
            self.assertEqual(read_dimensions(bmp, "BMP"), (900, 600))

    def test_reads_webp_vp8x_dimensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "image.webp"
            p.write_bytes(webp_vp8x_bytes(1024, 768))
            self.assertEqual(read_dimensions(p, "WEBP"), (1024, 768))

    def test_marks_exact_duplicate_content_without_modifying_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = png_bytes(1600, 1200)
            (root / "one.png").write_bytes(data)
            (root / "nested").mkdir()
            (root / "nested" / "copy.png").write_bytes(data)
            before = sorted((p.relative_to(root).as_posix(), p.read_bytes()) for p in root.rglob("*") if p.is_file())
            rows, summary = audit_directory(root)
            after = sorted((p.relative_to(root).as_posix(), p.read_bytes()) for p in root.rglob("*") if p.is_file())
            self.assertEqual(before, after)
            self.assertEqual(summary["duplicate_groups"], 1)
            self.assertEqual(summary["duplicate_files"], 2)
            self.assertTrue(all("exact_duplicate_content" in row.warnings for row in rows))

    def test_flags_extension_mismatch_and_corrupt_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "wrong.jpg").write_bytes(png_bytes(600, 400))
            (root / "broken.png").write_bytes(b"not a png")
            rows, summary = audit_directory(root, min_megapixels=1.0)
            by_name = {r.filename: r for r in rows}
            self.assertIn("extension_does_not_match_detected_format", by_name["wrong.jpg"].warnings)
            self.assertIn("below_configured_minimum_megapixels", by_name["wrong.jpg"].warnings)
            self.assertEqual(by_name["broken.png"].status, "review")
            self.assertGreaterEqual(int(summary["review_required"]), 2)

    def test_writes_csv_and_json_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "photos"
            root.mkdir()
            (root / "one.png").write_bytes(png_bytes(1200, 800))
            csv_out = Path(tmp) / "reports" / "audit.csv"
            json_out = Path(tmp) / "reports" / "summary.json"
            self.assertEqual(main([str(root), "--csv", str(csv_out), "--json", str(json_out)]), 0)
            with csv_out.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            summary = json.loads(json_out.read_text(encoding="utf-8"))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["width_px"], "1200")
            self.assertTrue(summary["read_only"])
            self.assertEqual(
                summary["inventory_csv_sha256"],
                hashlib.sha256(csv_out.read_bytes()).hexdigest(),
            )

    def test_skips_symlinked_files_and_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            outside = Path(tmp) / "outside"
            root.mkdir()
            outside.mkdir()
            (root / "real.png").write_bytes(png_bytes(900, 700))
            (outside / "hidden.png").write_bytes(png_bytes(900, 700))
            try:
                (root / "linked.png").symlink_to(outside / "hidden.png")
                (root / "linked-dir").symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest("symlinks are not available on this runner")
            rows, summary = audit_directory(root)
            self.assertEqual(len(rows), 1)
            self.assertEqual(summary["skipped_symlinks"], 2)

    def test_existing_reports_are_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "photos"
            root.mkdir()
            (root / "one.png").write_bytes(png_bytes(1200, 800))
            reports = Path(tmp) / "reports"
            reports.mkdir()
            existing_csv = reports / "existing.csv"
            existing_csv.write_text("owner data must survive", encoding="utf-8")
            existing_json = reports / "existing.json"
            existing_json.write_text("preserve this report", encoding="utf-8")

            self.assertEqual(main([str(root), "--csv", str(existing_csv)]), 2)
            self.assertEqual(existing_csv.read_text(encoding="utf-8"), "owner data must survive")

            new_csv = reports / "new.csv"
            self.assertEqual(main([str(root), "--csv", str(new_csv), "--json", str(existing_json)]), 2)
            self.assertFalse(new_csv.exists())
            self.assertEqual(existing_json.read_text(encoding="utf-8"), "preserve this report")

    def test_rejects_non_finite_megapixel_thresholds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for threshold in (float("nan"), float("inf"), float("-inf"), -0.1):
                with self.subTest(threshold=threshold):
                    with self.assertRaises(ValueError):
                        audit_directory(root, min_megapixels=threshold)

    def test_directory_traversal_errors_mark_scan_incomplete(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "photos"
            root.mkdir()
            csv_out = Path(tmp) / "reports" / "audit.csv"
            json_out = Path(tmp) / "reports" / "summary.json"

            def fake_walk(path, followlinks=False, onerror=None):
                if onerror is not None:
                    onerror(PermissionError(13, "permission denied", str(Path(path) / "private")))
                return iter(())

            with patch("audit_photo_library.os.walk", side_effect=fake_walk):
                result = main([str(root), "--csv", str(csv_out), "--json", str(json_out)])

            self.assertEqual(result, 1)
            summary = json.loads(json_out.read_text(encoding="utf-8"))
            self.assertFalse(summary["scan_complete"])
            self.assertEqual(summary["directory_traversal_errors"], 1)
            self.assertEqual(summary["directory_error_paths"], ["private"])

    def test_rejects_missing_source_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                audit_directory(Path(tmp) / "missing")


if __name__ == "__main__":
    unittest.main()
