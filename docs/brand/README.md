# SCAYLORE brand kit

Canonical files for the SCAYLORE identity. **PNG lockup, mark, favicon, OG, and crew portraits are cropped from** `scaylore-heroes.png` / `_src/scaylore-heroes.png`. Do not replace them with a redrawn letter S.

The mark is two rounded horizontal bars plus a small orange square at the top-right of the upper bar.

## Files

| File | Size / notes |
| --- | --- |
| `_src/scaylore-heroes.png` | Source hero. Rebuild rasters with `python3 scripts/build_brand_assets.py`. |
| `scaylore-heroes.png` | Same hero, public path. Left → right: **Echo**, **Shelf**, **Lore**, **Scout**, **Knot**. |
| `lockup.png` | Hero crop: two-bar mark + wordmark + tagline. |
| `logo-mark.png` | Isolated mark on the brand dark (padded crop). |
| `logo-mark-crop.png` | Tight crop of the same mark. |
| `logo-mark.svg` | Vector companion of the two-bar geometry. Prefer the PNG crop when the glow matters. |
| `og.png` | 1280×640 social preview (hero crop). |
| `favicon.ico` / `favicon-32.png` / `favicon-16.png` | Favicons from the mark crop. |
| `apple-touch-icon.png` | 180×180. |
| `icon-192.png` / `icon-512.png` | PWA / app icons. |
| `crew/echo.png` … `knot.png` | Portraits cropped from the hero, padded to 280×360. |

## Palette

Sampled from the hero mark — not a second invented system.

| Token | Hex | Use |
| --- | --- | --- |
| Void | `#000004` | Hero canvas, mark tile |
| Night | `#0B1220` | UI chrome |
| Signal | `#12D6E8` | Glow, eyes, tiles |
| Ember | `#F85720` | Orange square |
| Paper | `#F4FFFF` | Bars, wordmark |

## Wordmark

**SCAYLORE** in wide-tracking capitals. Tagline, exactly:

```
Fresh sources. Lasting memory.
```

## Crew (canonical)

1. **Echo** — Communicator (chatty / wave)
2. **Shelf** — Memory archivist (careful stack)
3. **Lore** — Core guardian (calm core)
4. **Scout** — Source hunter (curious seek)
5. **Knot** — Linker (wink / link)

## GitHub social preview

GitHub does not pick `og.png` up from the repo automatically. A maintainer pastes it in **Settings → General → Social preview**. Copy-paste text: [`docs/github-presence.md`](../github-presence.md).
