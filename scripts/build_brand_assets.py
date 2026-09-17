#!/usr/bin/env python3
"""Build SCAYLORE raster brand assets from the two-bar mark + crew hero.

The mark is a stylized S: two horizontal rounded bars + a small orange square.
Do not replace it with a continuous letter S.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "docs" / "brand"

ORANGE = (253, 106, 69, 255)
BAR = (247, 254, 254, 255)
GLOW = (18, 214, 232, 255)
VOID = (2, 6, 12, 255)
WORDMARK = (248, 251, 255, 255)
TAGLINE = (158, 196, 214, 255)

INTER_BOLD = Path("/usr/share/fonts/truetype/macos/Inter-Bold.ttf")
INTER = Path("/usr/share/fonts/truetype/macos/Inter-Regular.ttf")
NOTO = Path("/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf")
NOTO_REG = Path("/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")


def font(path: Path, size: int, fallback: Path | None = None) -> ImageFont.FreeTypeFont:
    for candidate in (path, fallback, NOTO, NOTO_REG):
        if candidate and candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def rounded_rect(size: tuple[int, int], radius: int, fill: tuple[int, ...]) -> Image.Image:
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=fill)
    return img


def draw_mark(width: int = 1024, height: int = 1024, *, transparent: bool = True) -> Image.Image:
    """Vector-faithful raster of the two-bar + orange-square mark."""
    bg = (0, 0, 0, 0) if transparent else VOID
    canvas = Image.new("RGBA", (width, height), bg)

    # Layout in a 256-unit design space, then scaled.
    scale = min(width, height) / 256
    bar_w, bar_h = int(148 * scale), int(40 * scale)
    radius = bar_h // 2
    gap = int(28 * scale)
    sq = int(22 * scale)
    total_h = bar_h * 2 + gap
    total_w = bar_w + int(14 * scale) + sq

    origin_x = (width - total_w) // 2
    origin_y = (height - total_h) // 2

    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    top = rounded_rect((bar_w, bar_h), radius, BAR)
    bottom = rounded_rect((bar_w, bar_h), radius, BAR)
    square = Image.new("RGBA", (sq, sq), ORANGE)

    top_xy = (origin_x, origin_y)
    bot_xy = (origin_x, origin_y + bar_h + gap)
    sq_xy = (origin_x + bar_w + int(12 * scale), origin_y + (bar_h - sq) // 2)

    for layer in (glow, canvas):
        layer.alpha_composite(top, top_xy)
        layer.alpha_composite(bottom, bot_xy)
    canvas.alpha_composite(square, sq_xy)
    # Keep the orange square mostly sharp; glow the bars only.
    glow.alpha_composite(top, top_xy)
    glow.alpha_composite(bottom, bot_xy)

    blurred = glow.filter(ImageFilter.GaussianBlur(radius=max(8, int(14 * scale))))
    tint = Image.new("RGBA", (width, height), GLOW)
    glow_colored = Image.composite(
        tint,
        Image.new("RGBA", (width, height), (0, 0, 0, 0)),
        blurred.split()[-1].point(lambda a: min(255, int(a * 1.35))),
    )
    inner = glow.filter(ImageFilter.GaussianBlur(radius=max(3, int(5 * scale))))
    inner_tint = Image.new("RGBA", (width, height), (180, 255, 255, 255))
    inner_glow = Image.composite(
        inner_tint,
        Image.new("RGBA", (width, height), (0, 0, 0, 0)),
        inner.split()[-1],
    )
    out = Image.new("RGBA", (width, height), bg)
    out.alpha_composite(glow_colored)
    out.alpha_composite(inner_glow)
    out.alpha_composite(canvas)
    return out


def crop_nontransparent(im: Image.Image, pad: int = 24) -> Image.Image:
    alpha = im.split()[-1]
    bbox = alpha.getbbox()
    if not bbox:
        return im
    l, t, r, b = bbox
    l, t = max(0, l - pad), max(0, t - pad)
    r, b = min(im.width, r + pad), min(im.height, b + pad)
    return im.crop((l, t, r, b))


def draw_lockup(width: int = 1600, height: int = 420) -> Image.Image:
    canvas = Image.new("RGBA", (width, height), VOID)
    mark = crop_nontransparent(draw_mark(640, 640), pad=8)
    mark_h = int(height * 0.52)
    ratio = mark_h / mark.height
    mark = mark.resize((max(1, int(mark.width * ratio)), mark_h), Image.Resampling.LANCZOS)

    bold = font(INTER_BOLD, int(height * 0.28), NOTO)
    tag = font(INTER, int(height * 0.085), NOTO_REG)

    word = "SCAYLORE"
    line = "Fresh sources. Lasting memory."
    draw = ImageDraw.Draw(canvas)
    word_box = draw.textbbox((0, 0), word, font=bold)
    tag_box = draw.textbbox((0, 0), line, font=tag)
    word_w, word_h = word_box[2] - word_box[0], word_box[3] - word_box[1]
    tag_w = tag_box[2] - tag_box[0]

    gap = int(height * 0.08)
    block_w = mark.width + gap + max(word_w, tag_w)
    x0 = (width - block_w) // 2
    y_mark = (height - mark.height) // 2
    canvas.alpha_composite(mark, (x0, y_mark))

    text_x = x0 + mark.width + gap
    text_block_h = word_h + int(height * 0.06) + (tag_box[3] - tag_box[1])
    text_y = (height - text_block_h) // 2 - word_box[1]
    draw.text((text_x, text_y), word, font=bold, fill=WORDMARK)
    draw.text(
        (text_x, text_y + word_h + int(height * 0.05)),
        line,
        font=tag,
        fill=TAGLINE,
    )
    return canvas


def cover_region(base: Image.Image, box: tuple[int, int, int, int], source: tuple[int, int]) -> None:
    """Clone a nearby dark patch over `box` with a soft mask."""
    l, t, r, b = box
    w, h = r - l, b - t
    sx, sy = source
    patch = base.crop((sx, sy, min(base.width, sx + w), min(base.height, sy + h)))
    if patch.size != (w, h):
        patch = patch.resize((w, h), Image.Resampling.BICUBIC)
    patch = patch.filter(ImageFilter.GaussianBlur(18))
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse((0, 0, w - 1, h - 1), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(28))
    base.paste(patch, (l, t), mask)


def cinematic_mark() -> Image.Image:
    """Prefer the extracted two-bar glow plate; fall back to the drawn mark."""
    extracted = BRAND / "_src" / "logo-mark-glow.png"
    if extracted.exists():
        im = Image.open(extracted).convert("RGBA")
        px = im.load()
        for y in range(im.height):
            for x in range(im.width):
                r, g, b, a = px[x, y]
                lum = (r + g + b) / 3
                if lum < 16:
                    px[x, y] = (0, 0, 0, 0)
                elif lum < 42:
                    px[x, y] = (r, g, b, int((lum - 16) / 26 * 255))
        return crop_nontransparent(im, pad=8)
    return crop_nontransparent(draw_mark(900, 900), pad=4)


def composite_hero(src: Path) -> Image.Image:
    hero = Image.open(src).convert("RGBA")
    # Cover the generated curved-S (not the official two-bar mark).
    cover_region(hero, (430, 0, 860, 230), source=(40, 8))
    cover_region(hero, (520, 8, 770, 200), source=(90, 12))
    mark = cinematic_mark()
    target_h = 178
    ratio = target_h / mark.height
    mark = mark.resize((max(1, int(mark.width * ratio)), target_h), Image.Resampling.LANCZOS)
    x = (hero.width - mark.width) // 2 + 6
    y = 10
    hero.alpha_composite(mark, (x, y))
    return hero


def make_favicon(mark: Image.Image, size: int) -> Image.Image:
    tile = Image.new("RGBA", (size, size), VOID)
    padded = int(size * 0.72)
    fitted = crop_nontransparent(mark, pad=2)
    ratio = padded / max(fitted.width, fitted.height)
    fitted = fitted.resize(
        (max(1, int(fitted.width * ratio)), max(1, int(fitted.height * ratio))),
        Image.Resampling.LANCZOS,
    )
    tile.alpha_composite(fitted, ((size - fitted.width) // 2, (size - fitted.height) // 2))
    return tile


def social_preview(hero: Image.Image, lockup: Image.Image) -> Image.Image:
    # GitHub recommended 1280x640 — crop the brand hero, keep the crew in frame.
    del lockup
    canvas = Image.new("RGBA", (1280, 640), VOID)
    fitted = hero.resize((1280, int(1280 * hero.height / hero.width)), Image.Resampling.LANCZOS)
    top = max(0, (fitted.height - 640) // 3)
    crop = fitted.crop((0, top, 1280, top + 640))
    canvas.alpha_composite(crop, (0, 0))
    return canvas


def save_rgb(im: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(path, "PNG", optimize=True)


def save_rgba(im: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)


def main() -> None:
    BRAND.mkdir(parents=True, exist_ok=True)

    mark_dark = draw_mark(1024, 1024, transparent=False)
    mark_clear = draw_mark(1024, 1024, transparent=True)
    save_rgb(mark_dark, BRAND / "logo-mark.png")
    save_rgba(crop_nontransparent(mark_clear, pad=32), BRAND / "logo-mark-on-transparent.png")

    lockup = draw_lockup()
    save_rgb(lockup, BRAND / "scaylore-lockup.png")

    hero_src = BRAND / "_src" / "crew-scene.png"
    if not hero_src.exists():
        raise SystemExit(f"missing crew hero source: {hero_src}")
    hero = composite_hero(hero_src)
    save_rgb(hero, BRAND / "scaylore-heroes.png")

    fav = make_favicon(mark_clear, 512)
    save_rgba(fav, BRAND / "favicon.png")
    save_rgba(make_favicon(mark_clear, 180), BRAND / "apple-touch-icon.png")
    save_rgb(social_preview(hero, lockup), BRAND / "social-preview.png")

    portraits = {
        "echo": (16, 268, 318, 632),
        "shelf": (368, 302, 528, 628),
        "lore": (548, 308, 738, 638),
        "scout": (778, 300, 948, 628),
        "knot": (982, 292, 1238, 632),
    }
    crew_dir = BRAND / "crew"
    crew_dir.mkdir(exist_ok=True)
    for name, box in portraits.items():
        save_rgb(hero.crop(box), crew_dir / f"{name}.png")

    print("wrote:")
    for p in sorted(BRAND.rglob("*")):
        if p.is_file() and p.parent.name != "_src":
            print(f"  {p.relative_to(ROOT)}  {p.stat().st_size} bytes")


if __name__ == "__main__":
    main()
