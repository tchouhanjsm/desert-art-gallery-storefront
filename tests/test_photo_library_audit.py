from __future__ import annotations

import csv
import json
import struct
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

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

    def test_rejects_missing_source_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                audit_directory(Path(tmp) / "missing")


if __name__ == "__main__":
    unittest.main()
