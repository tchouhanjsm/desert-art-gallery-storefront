#!/usr/bin/env python3
"""Create a read-only inventory of an image folder (stdlib only).

The scanner never renames, edits, moves, optimizes, uploads, or deletes source files.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import struct
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif", ".tiff",
    ".heic", ".heif", ".avif", ".svg",
}
EXTENSION_FORMATS = {
    ".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG", ".gif": "GIF",
    ".webp": "WEBP", ".bmp": "BMP", ".tif": "TIFF", ".tiff": "TIFF",
    ".heic": "HEIC/AVIF", ".heif": "HEIC/AVIF", ".avif": "HEIC/AVIF",
    ".svg": "SVG",
}


@dataclass(frozen=True)
class PhotoRecord:
    relative_path: str
    filename: str
    extension: str
    detected_format: str
    bytes: int
    width_px: int | None
    height_px: int | None
    aspect_ratio: float | None
    megapixels: float | None
    sha256: str
    duplicate_group: str
    status: str
    warnings: str

    def csv_dict(self) -> dict[str, str | int | float]:
        row = asdict(self)
        for key in ("width_px", "height_px", "aspect_ratio", "megapixels"):
            if row[key] is None:
                row[key] = ""
        return row  # type: ignore[return-value]


def detect_format(header: bytes) -> str | None:
    if header.startswith(b"\xff\xd8\xff"):
        return "JPEG"
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        return "PNG"
    if header.startswith((b"GIF87a", b"GIF89a")):
        return "GIF"
    if len(header) >= 12 and header[:4] == b"RIFF" and header[8:12] == b"WEBP":
        return "WEBP"
    if header.startswith(b"BM"):
        return "BMP"
    if header.startswith((b"II*\x00", b"MM\x00*")):
        return "TIFF"
    svg_prefix = header.lstrip().lower()
    if svg_prefix.startswith(b"<svg") or (svg_prefix.startswith(b"<?xml") and b"<svg" in svg_prefix[:4096]):
        return "SVG"
    if len(header) >= 12 and header[4:8] == b"ftyp":
        brand = header[8:12]
        if brand in {b"avif", b"avis", b"heic", b"heix", b"hevc", b"hevx", b"mif1", b"msf1"}:
            return "HEIC/AVIF"
    return None


def _jpeg_dimensions(data: bytes) -> tuple[int, int] | None:
    if not data.startswith(b"\xff\xd8"):
        return None
    sof_markers = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
    pos = 2
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        while pos < len(data) and data[pos] == 0xFF:
            pos += 1
        if pos >= len(data):
            return None
        marker = data[pos]
        pos += 1
        if marker in {0xD8, 0xD9, 0x01} or 0xD0 <= marker <= 0xD7:
            continue
        if pos + 2 > len(data):
            return None
        length = int.from_bytes(data[pos:pos + 2], "big")
        if length < 2 or pos + length > len(data):
            return None
        if marker in sof_markers and length >= 7:
            height = int.from_bytes(data[pos + 3:pos + 5], "big")
            width = int.from_bytes(data[pos + 5:pos + 7], "big")
            return (width, height) if width > 0 and height > 0 else None
        if marker == 0xDA:
            return None
        pos += length
    return None


def _webp_dimensions(data: bytes) -> tuple[int, int] | None:
    if len(data) < 30 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return None
    chunk = data[12:16]
    if chunk == b"VP8X" and len(data) >= 30:
        width = 1 + int.from_bytes(data[24:27], "little")
        height = 1 + int.from_bytes(data[27:30], "little")
        return width, height
    if chunk == b"VP8 " and len(data) >= 30 and data[23:26] == b"\x9d\x01\x2a":
        width = int.from_bytes(data[26:28], "little") & 0x3FFF
        height = int.from_bytes(data[28:30], "little") & 0x3FFF
        return (width, height) if width and height else None
    if chunk == b"VP8L" and len(data) >= 25 and data[20] == 0x2F:
        b1, b2, b3, b4 = data[21:25]
        width = 1 + b1 + ((b2 & 0x3F) << 8)
        height = 1 + (b2 >> 6) + (b3 << 2) + ((b4 & 0x0F) << 10)
        return width, height
    return None


def read_dimensions(path: Path, detected_format: str) -> tuple[int, int] | None:
    # Read only a bounded header; large source images are never loaded into memory.
    with path.open("rb") as handle:
        header = handle.read(1024 * 1024)
    if detected_format == "PNG" and len(header) >= 24:
        width, height = struct.unpack(">II", header[16:24])
        return (width, height) if width and height else None
    if detected_format == "GIF" and len(header) >= 10:
        width, height = struct.unpack("<HH", header[6:10])
        return (width, height) if width and height else None
    if detected_format == "JPEG":
        return _jpeg_dimensions(header)
    if detected_format == "WEBP":
        return _webp_dimensions(header)
    if detected_format == "BMP" and len(header) >= 26:
        dib_size = int.from_bytes(header[14:18], "little")
        if dib_size == 12:
            width, height = struct.unpack("<HH", header[18:22])
        elif dib_size >= 40:
            width = abs(int.from_bytes(header[18:22], "little", signed=True))
            height = abs(int.from_bytes(header[22:26], "little", signed=True))
        else:
            return None
        return (width, height) if width and height else None
    return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_candidates(root: Path) -> tuple[list[Path], int]:
    files: list[Path] = []
    skipped_symlinks = 0
    for current, dirs, names in os.walk(root, followlinks=False):
        current_path = Path(current)
        symlink_dirs = [name for name in dirs if (current_path / name).is_symlink()]
        skipped_symlinks += len(symlink_dirs)
        dirs[:] = sorted(
            [name for name in dirs if name not in symlink_dirs],
            key=str.casefold,
        )
        for name in names:
            path = current_path / name
            if path.is_symlink():
                skipped_symlinks += 1
                continue
            if path.suffix.lower() in IMAGE_EXTENSIONS:
                files.append(path)
                continue
            try:
                with path.open("rb") as handle:
                    signature = handle.read(32)
            except OSError:
                continue
            if detect_format(signature):
                files.append(path)
    return sorted(files, key=lambda p: p.relative_to(root).as_posix().casefold()), skipped_symlinks


def audit_directory(root: Path, min_megapixels: float | None = None) -> tuple[list[PhotoRecord], dict[str, object]]:
    root = root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Source directory does not exist or is not a directory: {root}")
    candidates, skipped_symlinks = iter_candidates(root)
    raw: list[dict[str, object]] = []
    hash_paths: dict[str, list[int]] = {}
    format_counts: Counter[str] = Counter()
    errors = 0

    for path in candidates:
        relative = path.relative_to(root).as_posix()
        extension = path.suffix.lower()
        warnings: list[str] = []
        try:
            size = path.stat().st_size
            with path.open("rb") as handle:
                header = handle.read(1024 * 1024)
            fmt = detect_format(header) or EXTENSION_FORMATS.get(extension, "UNKNOWN")
            actual_format = detect_format(header)
            if actual_format is None:
                warnings.append("unrecognized_or_corrupt_image_content")
            elif EXTENSION_FORMATS.get(extension) and EXTENSION_FORMATS[extension] != actual_format:
                warnings.append("extension_does_not_match_detected_format")
            dims = read_dimensions(path, actual_format) if actual_format else None
            if actual_format and dims is None:
                warnings.append("dimensions_not_available_or_header_invalid")
            width, height = dims if dims else (None, None)
            ratio = round(width / height, 4) if width and height else None
            megapixels = round((width * height) / 1_000_000, 3) if width and height else None
            if megapixels is not None and min_megapixels is not None and megapixels < min_megapixels:
                warnings.append("below_configured_minimum_megapixels")
            digest = sha256_file(path)
            format_counts[fmt] += 1
            hash_paths.setdefault(digest, []).append(len(raw))
            status = "ok" if actual_format and dims and not warnings else "review"
            raw.append({
                "relative_path": relative, "filename": path.name, "extension": extension,
                "detected_format": fmt, "bytes": size, "width_px": width,
                "height_px": height, "aspect_ratio": ratio, "megapixels": megapixels,
                "sha256": digest, "status": status, "warnings": warnings,
            })
        except OSError as exc:
            errors += 1
            raw.append({
                "relative_path": relative, "filename": path.name, "extension": extension,
                "detected_format": EXTENSION_FORMATS.get(extension, "UNKNOWN"),
                "bytes": 0, "width_px": None, "height_px": None, "aspect_ratio": None,
                "megapixels": None, "sha256": "", "status": "unreadable",
                "warnings": [f"read_error:{type(exc).__name__}"],
            })

    duplicate_groups = 0
    records: list[PhotoRecord] = []
    for digest, indices in hash_paths.items():
        if len(indices) > 1:
            duplicate_groups += 1
            for index in indices:
                warnings = raw[index]["warnings"]
                assert isinstance(warnings, list)
                warnings.append("exact_duplicate_content")
                raw[index]["status"] = "review"
                raw[index]["duplicate_group"] = "dup-" + digest[:12]
    for row in raw:
        warnings = row.get("warnings", [])
        group = str(row.get("duplicate_group", ""))
        records.append(PhotoRecord(
            relative_path=str(row["relative_path"]), filename=str(row["filename"]),
            extension=str(row["extension"]), detected_format=str(row["detected_format"]),
            bytes=int(row["bytes"]), width_px=row["width_px"], height_px=row["height_px"],
            aspect_ratio=row["aspect_ratio"], megapixels=row["megapixels"],
            sha256=str(row["sha256"]), duplicate_group=group, status=str(row["status"]),
            warnings=";".join(str(item) for item in warnings),
        ))

    summary: dict[str, object] = {
        "source_directory": str(root),
        "image_candidates": len(records),
        "dimensioned_candidates": sum(1 for r in records if r.width_px is not None and r.height_px is not None and r.sha256),
        "review_required": sum(1 for r in records if r.status in {"review", "unreadable"}),
        "read_errors": errors,
        "duplicate_groups": duplicate_groups,
        "duplicate_files": sum(1 for r in records if r.duplicate_group),
        "total_bytes": sum(r.bytes for r in records),
        "formats": dict(sorted(format_counts.items())),
        "skipped_symlinks": skipped_symlinks,
        "min_megapixels_threshold": min_megapixels,
        "read_only": True,
    }
    return records, summary


def write_csv(records: Iterable[PhotoRecord], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    fields = list(PhotoRecord.__dataclass_fields__.keys())
    with destination.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(record.csv_dict())


def write_json(summary: dict[str, object], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Inventory image assets without changing source files.",
        epilog="Read-only: no source image is renamed, edited, moved, optimized, uploaded, or deleted.",
    )
    parser.add_argument("source_dir", type=Path, help="Folder containing the selected image sample or photo library")
    parser.add_argument("--csv", dest="csv_path", type=Path, required=True, help="CSV report path (must be outside the source directory)")
    parser.add_argument("--json", dest="json_path", type=Path, help="Optional JSON summary report path")
    parser.add_argument("--min-megapixels", type=float, default=None, help="Optional warning threshold; no default quality threshold is imposed")
    args = parser.parse_args(argv)
    if args.min_megapixels is not None and args.min_megapixels < 0:
        parser.error("--min-megapixels must be zero or greater")
    try:
        source_root = args.source_dir.expanduser().resolve()
        csv_destination = args.csv_path.expanduser().resolve()
        json_destination = args.json_path.expanduser().resolve() if args.json_path else None
        if csv_destination.is_relative_to(source_root):
            parser.error("--csv report must be outside the source directory")
        if json_destination and json_destination.is_relative_to(source_root):
            parser.error("--json report must be outside the source directory")
        if json_destination and json_destination == csv_destination:
            parser.error("--csv and --json must use different output paths")
        records, summary = audit_directory(source_root, args.min_megapixels)
        write_csv(records, csv_destination)
        if json_destination:
            write_json(summary, json_destination)
    except (OSError, ValueError) as exc:
        print(f"Photo audit failed: {exc}", file=sys.stderr)
        return 2
    print(f"Photo audit complete (read-only): {summary['image_candidates']} image candidates")
    print(f"- Formats: {summary['formats']}")
    print(f"- Review required: {summary['review_required']}")
    print(f"- Exact duplicate groups: {summary['duplicate_groups']}")
    print(f"- Source bytes: {summary['total_bytes']}")
    print(f"- CSV report: {csv_destination}")
    if json_destination:
        print(f"- JSON summary: {json_destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
