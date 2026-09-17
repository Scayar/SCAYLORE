<p align="center">
  <img src="docs/brand/lockup.png" alt="SCAYLORE — two-bar mark, wordmark, and tagline Fresh sources. Lasting memory." width="520" />
</p>

<p align="center">
  <img alt="status" src="https://img.shields.io/badge/status-brand%20home-0B1220?style=flat-square&labelColor=0B1220&color=12D6E8" />
  <img alt="license" src="https://img.shields.io/badge/license-MIT-F85720?style=flat-square&labelColor=0B1220" />
</p>

<p align="center"><strong>SCAYLORE</strong> is Scayar’s name for a simple promise:<br />keep the sources fresh, and keep the memory lasting.</p>

<p align="center">
  <img src="docs/brand/scaylore-heroes.png" alt="The SCAYLORE crew, left to right: Echo, Shelf, Lore, Scout, and Knot" width="920" />
</p>

---

## What it is

This repository is the **brand home** for SCAYLORE — the mark, the crew, and the story.

There is no application, package, or service to install here yet. That is intentional. The codebase is the identity, not a pretend product.

The idea the identity is built around:

| Keep this | Meaning |
| --- | --- |
| **Fresh sources** | New signals have to be found, checked, and brought in while they are still true. |
| **Lasting memory** | What you learned has to stay organized, linked, and retrievable — not lost in a chat that scrolls away. |

The five robots on the hero are not mascots pasted on later. They *are* that idea, named.

---

## Meet the crew

Left → right on the hero. Names and roles are canonical. Portraits are cropped from [`docs/brand/scaylore-heroes.png`](docs/brand/scaylore-heroes.png).

<table>
<tr>
<td width="20%" align="center" valign="top">
<img src="docs/brand/crew/echo.png" alt="Echo waving, three chat bubbles in the air" /><br/>
<strong>Echo</strong><br/>
<em>Communicator</em>
</td>
<td width="20%" align="center" valign="top">
<img src="docs/brand/crew/shelf.png" alt="Shelf carefully holding a stack of memory slabs" /><br/>
<strong>Shelf</strong><br/>
<em>Memory archivist</em>
</td>
<td width="20%" align="center" valign="top">
<img src="docs/brand/crew/lore.png" alt="Lore calm, holding the core cube" /><br/>
<strong>Lore</strong><br/>
<em>Core guardian</em>
</td>
<td width="20%" align="center" valign="top">
<img src="docs/brand/crew/scout.png" alt="Scout looking through a magnifying glass" /><br/>
<strong>Scout</strong><br/>
<em>Source hunter</em>
</td>
<td width="20%" align="center" valign="top">
<img src="docs/brand/crew/knot.png" alt="Knot winking with a chain-link tile" /><br/>
<strong>Knot</strong><br/>
<em>Linker</em>
</td>
</tr>
</table>

### Echo — Communicator

Chatty. Hand already up. Three glowing bubbles stacked in the air.

Echo cannot let a sentence die in a mute room. Conversations, pings, and passing remarks are how most knowledge is born — and how most of it evaporates. Echo’s job is to catch those signals while they are still alive and walk them in.

**Role:** brings fresh signals and conversations into the system.

### Shelf — Memory archivist

Careful. Both hands on a stack of three glowing slabs.

Shelf does not chase. Shelf *orders*. Lasting memory is not a pile; it is layers you can still find next month. Echo brings the signal. Shelf gives it a place without dropping what was already kept.

**Role:** organizes and stacks lasting memory.

### Lore — Core guardian (center)

Calm. Eyes closed. A translucent cube in both hands — the two-bar mark living inside it.

Lore is the quiet middle. Not the hunt, not the chat, not the index. Everything the others touch is meant to end up here, intact, as lasting memory.

**Role:** the living lore / lasting memory core.

### Scout — Source hunter

Curious. Magnifying glass. Wide eyes, leaning in.

Scout goes looking. Pages, feeds, claims, files — anything that might be a source. Fresh is not the same as true, so Scout does not just fetch. Scout checks.

**Role:** finds and validates fresh sources.

### Knot — Linker

A wink. A tile with a chain.

Knot is why the other four are a crew instead of four specialists. Sources need memory. Memory needs people. People need the next source. Knot ties those together with one small click: *this belongs with that*.

**Role:** connects sources, memory, and people.

```text
        Echo  ──►  Shelf  ──►  Lore
          ▲                      │
          │                      ▼
        Scout  ◄──────────────  Knot
```

---

## This repository

```text
docs/brand/     Canonical hero, lockup, mark crops, favicon, social preview, crew portraits
docs/           Brand page + GitHub About copy
scripts/        Brand check (stdlib) and optional crop rebuild (Pillow)
LICENSE         MIT
```

### Run the check

The only runnable thing required here is a stdlib script that verifies the brand files and that this README still names the crew in order.

```bash
git clone https://github.com/Scayar/SCAYLORE.git
cd SCAYLORE
python3 scripts/check-brand.py
```

Requires Python 3. No packages. No network.

To recrop lockup, mark, favicon, OG, and crew portraits from the source hero (optional):

```bash
python3 -m pip install Pillow
python3 scripts/build_brand_assets.py
```

### What is not here

No CLI, no npm package, no API, no demo server, no user counts. When application code lands, this README will grow an honest install section. Until then, do not `npm install scaylore` from anywhere.

---

## Brand

Canonical assets live in [`docs/brand/`](docs/brand/README.md). The lockup, mark, favicons, social preview, and crew portraits are **crops of the hero** — not a redrawn substitute.

| File | Use |
| --- | --- |
| [`scaylore-heroes.png`](docs/brand/scaylore-heroes.png) | Official crew hero |
| [`lockup.png`](docs/brand/lockup.png) | Mark + wordmark + tagline, cropped from the hero |
| [`logo-mark.png`](docs/brand/logo-mark.png) | Two-bar mark + orange square, cropped from the hero |
| [`logo-mark.svg`](docs/brand/logo-mark.svg) | Vector companion of the same geometry |
| [`og.png`](docs/brand/og.png) | Social / GitHub preview (1280×640) |
| [`favicon.ico`](docs/brand/favicon.ico) | Favicon from the same mark crop |
| [`crew/`](docs/brand/crew/) | Echo, Shelf, Lore, Scout, Knot portraits |

**Do not redraw the mark.** It is two rounded horizontal bars with a small orange square at the top-right of the upper bar — never a continuous letter S.

A static brand page (favicon + Open Graph tags) is at [`docs/index.html`](docs/index.html).

---

## Author

[Scayar](https://github.com/Scayar) · [Scayar.com](https://Scayar.com)

Issues and ideas: [github.com/Scayar/SCAYLORE/issues](https://github.com/Scayar/SCAYLORE/issues)

---

<p align="center">
  <img src="docs/brand/logo-mark.png" alt="SCAYLORE two-bar mark" width="88" /><br/>
  <sub>Made by Scayar · Fresh sources. Lasting memory.</sub>
</p>
