#!/usr/bin/env python3
"""Safe output handling for local/private prototype review artifacts."""
from __future__ import annotations

import os
import stat
from pathlib import Path
from typing import Mapping, Sequence


def _overlaps(path: Path, protected: Path) -> bool:
    return path == protected or path in protected.parents or protected in path.parents


def has_symlink_component(path: Path) -> bool:
    """Return true when any component from the filesystem root is a symlink."""
    absolute = Path(path).expanduser().absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current = current / part
        try:
            if current.is_symlink():
                return True
        except OSError:
            return True
    return False


def ensure_private_directory(path: Path) -> Path:
    """Create or tighten a report directory so only its owner can traverse it."""
    raw = Path(path).expanduser()
    if has_symlink_component(raw):
        raise OSError(f"private output directory contains a symbolic link: {raw}")
    try:
        directory = raw.resolve(strict=False)
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    except (OSError, RuntimeError) as exc:
        raise OSError(f"cannot prepare private output directory: {type(exc).__name__}") from exc
    if not directory.is_dir():
        raise NotADirectoryError(f"private output path is not a directory: {directory}")
    if os.name == "posix":
        os.chmod(directory, 0o700)
        permissions = stat.S_IMODE(directory.stat().st_mode)
        if permissions & 0o077:
            raise PermissionError(f"private output directory is not owner-only: {directory}")
    return directory


def prepare_private_output_directory(
    output_dir: Path,
    *,
    protected_roots: Sequence[tuple[str, Path]],
    reserved_paths: Sequence[str],
    label: str,
) -> tuple[Path | None, list[str]]:
    """Resolve a private output directory and refuse links or existing artifacts."""
    raw = Path(output_dir).expanduser()
    if has_symlink_component(raw):
        return None, [f"{label} output path must not contain symbolic links"]

    try:
        output = raw.resolve(strict=False)
    except (OSError, RuntimeError):
        return None, [f"{label} output directory cannot be resolved"]

    for protected_label, protected_root in protected_roots:
        try:
            protected = Path(protected_root).expanduser().resolve(strict=False)
        except (OSError, RuntimeError):
            return None, [f"{label} protected source path cannot be resolved"]
        if _overlaps(output, protected):
            return None, [f"{label} output directory must be outside the {protected_label}"]

    if output.exists() and not output.is_dir():
        return None, [f"{label} output path must be a directory"]

    conflicts: list[str] = []
    for name in reserved_paths:
        relative = Path(name)
        if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
            return None, [f"{label} contains an unsafe reserved artifact path: {name!r}"]
        candidate = output / relative
        if candidate.exists() or candidate.is_symlink():
            conflicts.append(name)
    if conflicts:
        return None, [
            f"refusing to overwrite existing {label} artifact(s): "
            + ", ".join(conflicts)
            + "; choose a fresh private output directory"
        ]
    return output, []


def write_private_bytes(path: Path, content: bytes) -> None:
    """Create one private artifact exclusively with owner-only permissions."""
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        try:
            Path(path).unlink()
        except OSError:
            pass
        raise


def write_private_artifacts(output_dir: Path, artifacts: Mapping[str, str | bytes]) -> None:
    """Write a set of report files without replacing existing files."""
    created: list[Path] = []
    try:
        for name, content in artifacts.items():
            relative = Path(name)
            if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
                raise ValueError(f"unsafe private artifact path: {name!r}")
            path = output_dir / relative
            payload = content.encode("utf-8") if isinstance(content, str) else content
            write_private_bytes(path, payload)
            created.append(path)
    except Exception:
        for path in created:
            try:
                path.unlink()
            except OSError:
                pass
        raise
