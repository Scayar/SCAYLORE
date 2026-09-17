#!/usr/bin/env python3
"""Sanity-check SCAYLORE brand files and README claims."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "docs" / "brand"
README = ROOT / "README.md"

REQUIRED = {
    "docs/brand/scaylore-heroes.png": (1200, 600),
    "docs/brand/logo-mark.png": (512, 512),
    "docs/brand/logo-mark.svg": None,
    "docs/brand/scaylore-lockup.png": (800, 200),
    "docs/brand/favicon.png": (32, 32),
    "docs/brand/social-preview.png": (1280, 640),
    "docs/brand/crew/echo.png": (150, 250),
    "docs/brand/crew/shelf.png": (140, 250),
    "docs/brand/crew/lore.png": (140, 250),
    "docs/brand/crew/scout.png": (140, 250),
    "docs/brand/crew/knot.png": (140, 250),
}

CREW = ("Echo", "Shelf", "Lore", "Scout", "Knot")
FORBIDDEN = (
    "10k users",
    "1M downloads",
    "production-ready SaaS",
    "reallygreatsite",
)


def fail(msg: str) -> None:
    print(f"FAIL  {msg}")
    raise SystemExit(1)


def main() -> None:
    errors = 0

    for rel, min_size in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            print(f"FAIL  missing {rel}")
            errors += 1
            continue
        if path.suffix.lower() == ".png":
            im = Image.open(path)
            w, h = im.size
            if min_size and (w < min_size[0] or h < min_size[1]):
                print(f"FAIL  {rel} is {w}x{h}, expected at least {min_size[0]}x{min_size[1]}")
                errors += 1
            else:
                print(f"ok    {rel}  {w}x{h}  {im.mode}")
        else:
            print(f"ok    {rel}  {path.stat().st_size} bytes")

    svg = (BRAND / "logo-mark.svg").read_text(encoding="utf-8")
    if "two horizontal rounded bars" not in svg:
        print("FAIL  logo-mark.svg should describe the two-bar mark")
        errors += 1
    if "FD6A45" not in svg.upper() and "fd6a45" not in svg:
        print("FAIL  logo-mark.svg is missing the orange square color")
        errors += 1

    mark = Image.open(BRAND / "logo-mark.png").convert("RGB")
    px = mark.load()
    orange_px = 0
    for y in range(mark.height):
        for x in range(mark.width):
            r, g, b = px[x, y]
            if r > 180 and 40 < g < 140 and b < 100:
                orange_px += 1
    if orange_px < 200:
        print(f"FAIL  logo-mark.png has too little orange ({orange_px} px)")
        errors += 1
    else:
        print(f"ok    logo-mark.png orange square  {orange_px} px")

    board = (BRAND / "index.html").read_text(encoding="utf-8")
    for name in CREW:
        if name not in board:
            print(f"FAIL  brand board is missing {name}")
            errors += 1

    text = README.read_text(encoding="utf-8")
    for name in CREW:
        if name not in text:
            print(f"FAIL  README is missing {name}")
            errors += 1
    if "Fresh sources. Lasting memory." not in text:
        print("FAIL  README is missing the official tagline")
        errors += 1
    if "scaylore-heroes.png" not in text:
        print("FAIL  README does not embed the brand hero")
        errors += 1
    for phrase in FORBIDDEN:
        if phrase.lower() in text.lower():
            print(f"FAIL  README contains invented/forbidden phrase: {phrase}")
            errors += 1

    if errors:
        fail(f"{errors} check(s) failed")
    print("ok    brand + README checks passed")


if __name__ == "__main__":
    sys.exit(main())
