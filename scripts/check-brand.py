#!/usr/bin/env python3
"""Sanity-check SCAYLORE brand assets and README. Stdlib only."""

from __future__ import annotations

import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "docs" / "brand"
README = ROOT / "README.md"

REQUIRED = [
    "scaylore-heroes.png",
    "logo-mark.png",
    "logo-mark.svg",
    "lockup.png",
    "og.png",
    "favicon.ico",
    "favicon-32.png",
    "apple-touch-icon.png",
]

CREW = ["Echo", "Shelf", "Lore", "Scout", "Knot"]
TAGLINE = "Fresh sources. Lasting memory."

# Fake-metric phrases that must not appear as claimed stats.
FORBIDDEN = [
    "k stars",
    "m downloads",
    "million users",
    "10/10 on product hunt",
]


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit(f"{path.name}: not a PNG")
    if data[12:16] != b"IHDR":
        raise SystemExit(f"{path.name}: missing IHDR")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    errors: list[str] = []

    if not README.exists():
        errors.append("README.md missing")
    else:
        text = README.read_text(encoding="utf-8")
        if "SCAYLORE" not in text:
            errors.append("README.md does not mention SCAYLORE")
        if TAGLINE not in text:
            errors.append(f"README.md missing tagline: {TAGLINE!r}")
        last = -1
        for name in CREW:
            idx = text.find(f"**{name}**")
            if idx < 0:
                idx = text.find(f"## {name}")
            if idx < 0:
                idx = text.find(name)
            if idx < 0:
                errors.append(f"README.md missing crew member {name}")
            elif idx < last:
                errors.append(f"README.md crew order: {name} appears before the previous member")
            else:
                last = idx
        lowered = text.lower()
        for phrase in FORBIDDEN:
            if phrase in lowered:
                errors.append(f"README.md contains forbidden metric phrasing: {phrase!r}")

    for name in REQUIRED:
        path = BRAND / name
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        if path.stat().st_size < 200:
            errors.append(f"{path.name} is empty")
        if path.suffix.lower() == ".png":
            try:
                png_size(path)
            except SystemExit as exc:
                errors.append(str(exc))

    heroes = BRAND / "scaylore-heroes.png"
    if heroes.exists():
        w, h = png_size(heroes)
        if w < 1000 or h < 500:
            errors.append(f"scaylore-heroes.png too small: {w}x{h}")
        ratio = w / h
        if not 1.5 < ratio < 2.0:
            errors.append(f"scaylore-heroes.png expected ~16:9, got {w}x{h}")

    og = BRAND / "og.png"
    if og.exists():
        w, h = png_size(og)
        if w < 1200 or h < 600:
            errors.append(f"og.png expected at least 1200x600, got {w}x{h}")

    mark = BRAND / "logo-mark.png"
    if mark.exists():
        w, h = png_size(mark)
        if abs(w - h) > 8:
            errors.append(f"logo-mark.png should be square, got {w}x{h}")

    if errors:
        print("brand check failed:")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("brand check passed")
    print(f"  README crew: {' → '.join(CREW)}")
    print(f"  heroes: {png_size(heroes)[0]}x{png_size(heroes)[1]}")
    print(f"  mark:   {png_size(mark)[0]}x{png_size(mark)[1]}")
    print(f"  og:     {png_size(og)[0]}x{png_size(og)[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
