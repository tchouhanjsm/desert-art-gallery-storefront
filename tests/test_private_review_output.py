from __future__ import annotations

import stat
import tempfile
import unittest
from pathlib import Path

from scripts.private_review_output import (
    ensure_private_directory,
    prepare_private_output_directory,
    write_private_artifacts,
    write_private_bytes,
)


class PrivateReviewOutputTests(unittest.TestCase):
    def test_output_must_not_overlap_a_protected_source_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "prototype"
            root.mkdir()
            output, errors = prepare_private_output_directory(
                root / "reports",
                protected_roots=(("prototype source directory", root),),
                reserved_paths=("report.json",),
                label="private review",
            )
        self.assertIsNone(output)
        self.assertTrue(any("outside the prototype source directory" in error for error in errors))

    def test_reserved_symlink_is_rejected_even_when_it_is_dangling(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            output_dir = base / "reports"
            output_dir.mkdir()
            try:
                (output_dir / "report.json").symlink_to(base / "missing-target")
            except (OSError, NotImplementedError):
                self.skipTest("file symlinks are unavailable on this runner")
            output, errors = prepare_private_output_directory(
                output_dir,
                protected_roots=(),
                reserved_paths=("report.json",),
                label="private review",
            )
        self.assertIsNone(output)
        self.assertTrue(any("report.json" in error for error in errors))

    def test_existing_output_directory_is_tightened_to_owner_only(self):
        import os

        if os.name != "posix":
            self.skipTest("POSIX directory permission bits are not available")
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "reports"
            directory.mkdir(mode=0o755)
            directory.chmod(0o755)
            secured = ensure_private_directory(directory)
            self.assertEqual(secured, directory.resolve())
            self.assertEqual(stat.S_IMODE(secured.stat().st_mode) & 0o077, 0)

    def test_symlinked_parent_component_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            target = base / "target"
            target.mkdir()
            parent_link = base / "reports-link"
            try:
                parent_link.symlink_to(target, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("directory symlinks are unavailable on this runner")
            output, errors = prepare_private_output_directory(
                parent_link / "nested",
                protected_roots=(),
                reserved_paths=("report.json",),
                label="private review",
            )
            self.assertIsNone(output)
            self.assertTrue(any("symbolic links" in error for error in errors))
            self.assertEqual(list(target.iterdir()), [])

    def test_private_artifacts_are_owner_only_and_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            report = output / "report.json"
            write_private_bytes(report, b'{"safe":true}')
            mode = stat.S_IMODE(report.stat().st_mode)
            self.assertEqual(mode & 0o077, 0)
            with self.assertRaises(FileExistsError):
                write_private_artifacts(output, {"report.json": '{"replace":true}'})
            self.assertEqual(report.read_bytes(), b'{"safe":true}')

    def test_multi_file_write_removes_partial_new_reports_on_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            conflict = output / "already-there.md"
            conflict.write_text("owner report", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                write_private_artifacts(output, {
                    "new.json": '{"new":true}',
                    "already-there.md": "replacement",
                })
            self.assertFalse((output / "new.json").exists())
            self.assertEqual(conflict.read_text(encoding="utf-8"), "owner report")


if __name__ == "__main__":
    unittest.main()
