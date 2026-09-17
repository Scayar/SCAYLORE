<p align="center">
  <img src="docs/brand/lockup.png" alt="SCAYLORE — Fresh sources. Lasting memory." width="520" />
</p>

<p align="center">
  <img alt="status" src="https://img.shields.io/badge/status-brand%20home-0B1220?style=flat-square&labelColor=0B1220&color=0AA0E2" />
  <img alt="license" src="https://img.shields.io/badge/license-MIT-F96A02?style=flat-square&labelColor=0B1220" />
</p>

<p align="center"><strong>SCAYLORE</strong> is Scayar’s name for a simple promise:<br />keep the sources fresh, and keep the memory lasting.</p>

<p align="center">
  <img src="docs/brand/scaylore-heroes.png" alt="The SCAYLORE crew: Echo, Shelf, Lore, Scout, and Knot" width="920" />
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

Left → right on the hero. Names and roles are canonical.

### Echo — Communicator

Antennae with blue tips. One hand already waving. Three glowing chat tiles in the air.

Echo is the hello. Conversations, pings, and passing remarks are how most knowledge is born — and how most of it dies. Echo’s job is to catch those fresh signals and walk them into the system before they evaporate.

**Role:** brings fresh signals and conversations into the system.

### Shelf — Memory archivist

No fuss. Both hands on a stack of three glowing slabs.

Shelf does not collect clutter. Shelf stacks. Lasting memory is not a pile; it is layers you can still find when you come back next month. Echo brings the signal. Shelf gives it a place.

**Role:** organizes and stacks lasting memory.

### Lore — Core guardian (center)

Eyes closed. A translucent blue cube in both hands. Inside the cube: the SCAYLORE S-mark.

Lore is the quiet middle. Not the hunt, not the chat, not the index — the living lore itself. Everything the others touch is meant to end up here, intact, as lasting memory.

**Role:** the living lore / lasting memory core.

### Scout — Source hunter

Magnifying glass. Wide, curious eyes.

Scout goes looking. Pages, feeds, claims, files — anything that might be a source. Fresh is not the same as true, so Scout does not just fetch. Scout checks.

**Role:** finds and validates fresh sources.

### Knot — Linker

A wink. A tile with a chain.

Knot is why the other four are a crew instead of four specialists. Sources need memory. Memory needs people. People need the next source. Knot ties those together.

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
docs/brand/     Canonical hero, mark, lockup, favicon, social preview
docs/           Brand page + GitHub About copy
scripts/        Brand sanity check (no app runtime)
LICENSE         MIT
```

### Run the check

The only runnable thing in this repo is a stdlib script that verifies the brand files and that this README still names the crew in order.

```bash
git clone https://github.com/Scayar/SCAYLORE.git
cd SCAYLORE
python3 scripts/check-brand.py
```

Requires Python 3. No packages. No network.

### What is not here

No CLI, no npm package, no API, no demo server, no user counts. When application code lands, this README will grow an honest install section. Until then, do not `npm install scaylore` from anywhere.

---

## Brand

Canonical assets live in [`docs/brand/`](docs/brand/README.md).

| File | Use |
| --- | --- |
| [`scaylore-heroes.png`](docs/brand/scaylore-heroes.png) | Official crew hero |
| [`lockup.png`](docs/brand/lockup.png) | Mark + wordmark + tagline |
| [`logo-mark.png`](docs/brand/logo-mark.png) / [`logo-mark.svg`](docs/brand/logo-mark.svg) | S-mark (two rounded bars + orange square) |
| [`og.png`](docs/brand/og.png) | Social / GitHub preview (1280×640) |
| [`favicon.ico`](docs/brand/favicon.ico) | Favicon |

**Do not redraw the mark.** The S is two rounded horizontal bars with a small orange square at the top-right — not a generic letter S, not a different icon.

A static brand page (favicon + Open Graph tags) is at [`docs/index.html`](docs/index.html).

---

## Author

[Scayar](https://github.com/Scayar) · [Scayar.com](https://Scayar.com)

Issues and ideas: [github.com/Scayar/SCAYLORE/issues](https://github.com/Scayar/SCAYLORE/issues)

---

<p align="center">
  <sub>Made by Scayar · Fresh sources. Lasting memory.</sub>
</p>
