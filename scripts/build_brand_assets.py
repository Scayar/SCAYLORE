#!/usr/bin/env python3
"""Derive SCAYLORE rasters from the official hero.

Source of truth: docs/brand/_src/scaylore-heroes.png
Every lockup, mark, favicon, OG, and crew portrait is a crop of that file.
The mark is two horizontal rounded bars + an orange square — never a letter S.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "docs" / "brand"
SRC = BRAND / "_src" / "scaylore-heroes.png"
VOID = (0, 0, 4, 255)

# Pixel boxes on the 1280x720 source hero.
CROPS = {
    "lockup": (370, 0, 910, 305),
    "mark": (500, 12, 772, 176),
    "echo": (8, 260, 355, 705),
    "shelf": (368, 305, 548, 705),
    "lore": (550, 308, 736, 712),
    "scout": (758, 298, 925, 705),
    "knot": (992, 278, 1279, 712),
}


def save_rgb(im: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(path, "PNG", optimize=True)


def pad_square(im: Image.Image, background=VOID, extra: int = 48) -> Image.Image:
    side = max(im.width, im.height) + extra * 2
    tile = Image.new("RGBA", (side, side), background)
    tile.alpha_composite(
        im,
        ((side - im.width) // 2, (side - im.height) // 2),
    )
    return tile


def fit_icon(mark: Image.Image, size: int) -> Image.Image:
    tile = Image.new("RGBA", (size, size), VOID)
    padded = int(size * 0.82)
    ratio = padded / max(mark.width, mark.height)
    fitted = mark.resize(
        (max(1, int(mark.width * ratio)), max(1, int(mark.height * ratio))),
        Image.Resampling.LANCZOS,
    )
    tile.alpha_composite(
        fitted,
        ((size - fitted.width) // 2, (size - fitted.height) // 2),
    )
    return tile


def portrait(crop: Image.Image, width: int = 280, height: int = 360) -> Image.Image:
    tile = Image.new("RGBA", (width, height), VOID)
    ratio = min((width - 12) / crop.width, (height - 12) / crop.height)
    fitted = crop.resize(
        (max(1, int(crop.width * ratio)), max(1, int(crop.height * ratio))),
        Image.Resampling.LANCZOS,
    )
    x = (width - fitted.width) // 2
    y = height - fitted.height - 6
    tile.alpha_composite(fitted.convert("RGBA"), (x, y))
    return tile


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"missing source hero: {SRC}")
    hero = Image.open(SRC).convert("RGBA")
    if hero.size != (1280, 720):
        print(f"warn: source is {hero.size}, crops assume 1280x720")
    # Always emit a real PNG (GenerateImage may hand us a JPEG with a .png name).
    save_rgb(hero, SRC)
    save_rgb(hero, BRAND / "scaylore-heroes.png")

    lockup = hero.crop(CROPS["lockup"])
    save_rgb(lockup, BRAND / "lockup.png")

    mark = hero.crop(CROPS["mark"]).convert("RGBA")
    mark_sq = pad_square(mark).resize((1024, 1024), Image.Resampling.LANCZOS)
    save_rgb(mark_sq, BRAND / "logo-mark.png")
    save_rgb(mark, BRAND / "logo-mark-crop.png")

    save_rgb(fit_icon(mark, 32), BRAND / "favicon-32.png")
    save_rgb(fit_icon(mark, 16), BRAND / "favicon-16.png")
    save_rgb(fit_icon(mark, 180), BRAND / "apple-touch-icon.png")
    save_rgb(fit_icon(mark, 192), BRAND / "icon-192.png")
    save_rgb(fit_icon(mark, 512), BRAND / "icon-512.png")
    fit_icon(mark, 32).save(
        BRAND / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )
    fit_icon(mark, 32).save(
        ROOT / "docs" / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32)],
    )

    save_rgb(hero.crop((0, 40, 1280, 680)), BRAND / "og.png")

    crew_dir = BRAND / "crew"
    crew_dir.mkdir(exist_ok=True)
    for name in ("echo", "shelf", "lore", "scout", "knot"):
        save_rgb(portrait(hero.crop(CROPS[name])), crew_dir / f"{name}.png")

    print("derived brand rasters from", SRC.relative_to(ROOT))


if __name__ == "__main__":
    main()
