<p align="center">
  <img src="docs/brand/scaylore-lockup.png" alt="SCAYLORE — Fresh sources. Lasting memory." width="560" />
</p>

<p align="center">
  <em>Fresh sources. Lasting memory.</em>
</p>

<p align="center">
  <a href="#what-it-is">What it is</a>
  ·
  <a href="#meet-the-crew">Meet the crew</a>
  ·
  <a href="#how-the-crew-fits-together">How it fits</a>
  ·
  <a href="#in-this-repository">This repo</a>
  ·
  <a href="#brand">Brand</a>
</p>

<p align="center">
  <img alt="Brand home" src="https://img.shields.io/badge/status-brand%20home-12d6e8?style=flat-square&labelColor=070b14" />
  <img alt="No application runtime yet" src="https://img.shields.io/badge/runtime-not%20shipped%20yet-fd6a45?style=flat-square&labelColor=070b14" />
</p>

---

# SCAYLORE

SCAYLORE is Scayar's name for a simple, stubborn idea: **sources should stay fresh, and memory should last.**

This repository is the brand home for that idea — the mark, the tagline, and the five-robot crew who carry it. It is not a packaged app, a SaaS dashboard, or a metrics page. There is no runtime to start, and this README will not invent one.

The name is **Scayar + lore**. The work, when it lands in code, is meant to keep living knowledge close: new signals on one side, a memory that does not evaporate on the other.

## What it is

Most systems are good at one of two things. They chase whatever is new, then forget it. Or they archive everything, then go stale.

SCAYLORE is the tension between those two instincts, written as a brand:

- **Fresh sources** — find, check, and bring in what is happening now.
- **Lasting memory** — keep what mattered, stacked so it can be found again.
- **The link between them** — so people, sources, and memory stay connected instead of drifting into separate piles.

Today this GitHub repository holds the identity for that story. The official crew lives here. The two-bar mark lives here. Application code does not, yet.

If you cloned this repo looking for `npm start` or `pip install scaylore`, you are early — and you are in the right place to watch the brand take shape.

## Meet the crew

<p align="center">
  <img src="docs/brand/scaylore-heroes.png" alt="The SCAYLORE crew, left to right: Echo, Shelf, Lore, Scout, and Knot" width="920" />
</p>

Five small specialists. One job: keep sources fresh and memory lasting.

<table>
<tr>
<td width="20%" align="center">
<img src="docs/brand/crew/echo.png" alt="Echo, the communicator" /><br/>
<strong>Echo</strong><br/>
<em>Communicator</em>
</td>
<td width="20%" align="center">
<img src="docs/brand/crew/shelf.png" alt="Shelf, the memory archivist" /><br/>
<strong>Shelf</strong><br/>
<em>Memory archivist</em>
</td>
<td width="20%" align="center">
<img src="docs/brand/crew/lore.png" alt="Lore, the core guardian" /><br/>
<strong>Lore</strong><br/>
<em>Core guardian</em>
</td>
<td width="20%" align="center">
<img src="docs/brand/crew/scout.png" alt="Scout, the source hunter" /><br/>
<strong>Scout</strong><br/>
<em>Source hunter</em>
</td>
<td width="20%" align="center">
<img src="docs/brand/crew/knot.png" alt="Knot, the linker" /><br/>
<strong>Knot</strong><br/>
<em>Linker</em>
</td>
</tr>
</table>

### Echo — Communicator

Antennae with blue tips. A wave. Three glowing chat-bubble tiles.

Echo is first to hear the room. He catches the half-finished thought, the ping, the conversation that would otherwise vanish into a scrollback. **His role is to bring fresh signals and conversations into the system** — not to decide what they mean, just to make sure they arrive while they are still alive.

### Shelf — Memory archivist

Both hands on a stack of three glowing blue slabs.

Shelf does not chase. Shelf *orders*. Each slab is a layer of what has already been worth keeping, stacked so the next layer has somewhere to sit. **His role is to organize and stack lasting memory** — the quiet work that makes “we already knew this” possible.

### Lore — Core guardian

Center. Closed smile. A translucent cyan cube that holds the SCAYLORE mark.

Lore is the one the others orbit. The cube is not a toy; it is the place a fresh source becomes something the system can still find next month. **Lore is the living lore / lasting memory core** — the guardian in the middle of the line.

### Scout — Source hunter

Magnifying glass. Wide, curious eyes.

Scout lives at the edge of the map. He does not take a source on reputation. He looks. He checks. He comes back with something that can be trusted enough to keep. **His role is to find and validate fresh sources** before they ever reach Shelf's stack.

### Knot — Linker

A wink. A tile with a chain / link icon.

Knot is how the line becomes a loop. Sources without people are trivia. Memory without a link is a drawer. **His role is to connect sources, memory, and people** — the small click that means *this belongs with that*.

## How the crew fits together

This is the brand's working picture, not a shipped architecture. There is no service graph in this repository to match it.

```text
   Echo                         Scout
  signals                      sources
     \                           /
      \                         /
       v                       v
         Shelf  ------>  Lore
         stacks         holds
              \         /
               v       v
                 Knot
                links
```

1. **Echo** brings the live conversation in.
2. **Scout** finds and validates the source behind it.
3. **Shelf** stacks what should last.
4. **Knot** ties source, memory, and people together.
5. **Lore** keeps the core — the lore that remains when the tab is closed.

## In this repository

```text
SCAYLORE/
├── README.md
├── Makefile
├── requirements.txt          # Pillow, for brand tooling only
├── docs/brand/               # Canonical brand kit
│   ├── scaylore-heroes.png   # Crew hero
│   ├── scaylore-lockup.png   # Mark + wordmark + tagline
│   ├── logo-mark.svg         # Two-bar S + orange square
│   ├── logo-mark.png
│   ├── favicon.png
│   ├── apple-touch-icon.png
│   ├── social-preview.png    # 1280×640
│   ├── tokens.css
│   ├── index.html            # Local brand board
│   └── crew/                 # Echo, Shelf, Lore, Scout, Knot
└── scripts/
    ├── build_brand_assets.py
    └── verify_brand.py
```

There is no `src/`, no server, no tests for product behavior. That is accurate, not a placeholder for a hidden app.

### Clone and check

You need Git and Python 3.10+. Pillow is only required if you rebuild rasters.

```bash
git clone https://github.com/Scayar/SCAYLORE.git
cd SCAYLORE

python3 -m pip install -r requirements.txt
python3 scripts/verify_brand.py
```

To rebuild lockup, favicon, social preview, and crew crops from the brand sources:

```bash
make brand
make check
```

Open `docs/brand/index.html` in a browser to see the kit on a dark board.

## Brand

The mark is a stylized **S**: two horizontal rounded bars and a small orange square. Do not redraw it as a continuous letter S.

| Token | Role | Hex |
| --- | --- | --- |
| Void | Background | `#070B14` |
| Snow | Bars / wordmark | `#F7FEFE` |
| Cyan | Glow / eyes / signal | `#12D6E8` |
| Orange | The square — a spark of the new | `#FD6A45` |
| Mute | Tagline | `#9EC4D6` |

Canonical files:

| File | Use |
| --- | --- |
| [`docs/brand/logo-mark.svg`](docs/brand/logo-mark.svg) | Vector mark |
| [`docs/brand/scaylore-lockup.png`](docs/brand/scaylore-lockup.png) | README / header |
| [`docs/brand/scaylore-heroes.png`](docs/brand/scaylore-heroes.png) | Crew hero |
| [`docs/brand/favicon.png`](docs/brand/favicon.png) | App icon / favicon |
| [`docs/brand/social-preview.png`](docs/brand/social-preview.png) | GitHub social preview (1280×640) |

To set the GitHub social image: **Settings → General → Social preview** → upload `docs/brand/social-preview.png`.

## What this README will not do

- Invent a feature list for software that is not in the tree.
- Quote stars, downloads, or user counts.
- Pretend `make` starts a product.

When application code arrives, this page should grow an honest install path beside the crew — not instead of them.

## Author

**Scayar**

- GitHub: [github.com/Scayar](https://github.com/Scayar)
- Site: [Scayar.com](https://scayar.com)

---

<p align="center">
  <img src="docs/brand/logo-mark.png" alt="SCAYLORE mark" width="88" /><br/>
  <sub>Fresh sources. Lasting memory.</sub>
</p>
