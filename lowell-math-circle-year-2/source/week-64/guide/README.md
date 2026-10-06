# Week 64 facilitator guide

The editable sources build the separate adult guide for **Straight paths on strange surfaces**. The guide is paired with the nine-problem Week 64 student packet, version W64-G35-v1. Page and problem references refer to that packet; the guide has its own page numbers.

## Build

Requirements: a normal TeX Live or MiKTeX installation with pdfLaTeX, TikZ, Helvetica and standard LaTeX packages. No external images, fonts, network access, book files or absolute paths are needed.

Run:

    bash build.sh

This makes facilitator.pdf and a disposable build/ directory. Set LATEX_ENGINE only for a compatible alternative engine.

The mathematical checks use Python 3's standard library:

    python3 verify.py

Optional visual review with Poppler:

    mkdir -p render
    pdftoppm -r 150 -png facilitator.pdf render/page

Inspect every page. A successful TeX build does not establish layout quality.

## Files

- facilitator.tex: document style and file order
- opening.tex: theorem-first overview, preparation, shared launch
- solutions.tex: flexible routes and complete solutions to Problems 1–9
- background.tex: exact coordinates, proofs, topology, finite-sheet argument limits
- sources.tex: public references and review limits
- build.sh: portable builder
- verify.py: exact mathematical checks
- PROVENANCE.md: authorship and source scope

All text and the developed-copy figure are newly authored. The underlying mathematics is established. The materials remain unpiloted; physical rehearsal with the actual paper kit has not been performed.
