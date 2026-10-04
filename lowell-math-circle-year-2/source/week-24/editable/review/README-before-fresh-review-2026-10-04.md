# Nontransitive dice and decks: Week 24 editable release

Draft and unpiloted. Week 24 identifies an unscheduled activity-library slot, not a booked meeting. No adoption, classroom success or tested pacing is claimed. Prepared October 3, 2026.

## Print-ready material and flexible readiness

Four reviewed PDFs accompany this ZIP, with identical reference copies in `reference-pdfs/`.

k-1: 8 pages, 8 numbered problem entries; grades-2-3: 7 pages, 7 numbered problem entries; grades-4-5: 7 pages, 7 numbered problem entries; facilitator-guide: 14 pages. Student total: 22 numbered problem entries across the three bands. A continued problem is counted once. Related adaptations across bands are not claimed as distinct mathematical ideas.

Print selected student pages single-sided on US Letter at 100% / actual size. Start with a few pages and allow deep work; completing a packet is not the goal. Grade labels are approximate starting points. Choose by readiness and interest; adults can read, move materials or scribe:

- K-1: Compare two card values after an oral demonstration and keep all nine card pairs distinct; fractions are not required.
- Grades 2-3: Organize every pair and distinguish wins, losses and ties; repeated equal faces remain separate cards.
- Grades 4-5: Use complete pair counts and follow order restrictions; construction and impossibility arguments are developed in the packet.

Mathematical kernel: Cyclic pairwise winning probabilities, exhaustive product-space comparisons and small-deck obstructions.

The adult guide provides preparation, keyed solutions, reasoning, held hints and optional extensions. Quantities and timing are editorial suggestions, not verified inventory or classroom evidence.

## Mathematical overview and example revision

The guide now begins with one concise, unnumbered mathematical overview. It states the assumptions, principal facts, intended discoveries, grade-band routes, and the difference between trials, conjectures and explanations. Original numbered guide pages and their printed-page references follow. The student PDFs are byte-identical to the preceding release. Existing labeled diagrams and explicit adult demonstrations already introduce the required objects and procedures.

Edit `facilitator-src/overview-content.json` for overview prose and `facilitator-src/build_overview.py` for its layout. The top-level build first regenerates and checks the numbered guide, then prepends the overview. Earlier detailed-guide QA records refer to the numbered body; the current reference manifest and release validation cover the complete PDFs.

## Contents and editing

- `src/build_packets.py` and `src/*.tex`: editable student text, examples, diagrams and generated LaTeX.
- `facilitator-src/build.py` and accompanying local modules/data: editable adult-guide prose and drawings.
- Mathematics-check scripts and checked data remain beside their sources.
- `outlines/`: kernels, prerequisites, source attribution and materials.
- `review/`: historical student reviews, original adult QA, reference hashes and release-validation results. Original adult build instructions are historical; they may describe bundled fonts in the authoring workspace. This release excludes font binaries. Use this README and top-level build for the portable release.
- `verify_rebuild.py`: checks reference hashes and compares every rebuilt page's text, US Letter size and 100-dpi grayscale pixels.

Edit the generators or guide data for changes that survive rebuilding. Normal build regenerates student LaTeX; `bash build.sh --from-tex` instead preserves manual LaTeX edits. The adult guide is regenerated in either mode. Checks are tied to these examples and need deliberate updates if examples change. Keep reference PDFs unchanged unless issuing a newly reviewed release.

## Portable local rebuild

Requirements: Python 3.10 or later, packages in `requirements.txt`, a working TeX Live or MacTeX providing pdflatex, TikZ/PGF, Latin Modern and standard LaTeX packages, and installed Liberation Sans regular, bold, italic and bold-italic fonts. Poppler's pdftoppm is required for reference comparison.

Typical Debian/Ubuntu packages are texlive-latex-base, texlive-latex-recommended, texlive-latex-extra, texlive-pictures, lmodern, fonts-liberation and poppler-utils. Use your usual local package manager. Font discovery consults ReportLab's search path, Fontconfig when available, and user font folders. Set LIBERATION_FONT_DIR to a folder containing LiberationSans-Regular.ttf, LiberationSans-Bold.ttf, LiberationSans-Italic.ttf and LiberationSans-BoldItalic.ttf when needed. Font files are not bundled. Release font hashes are recorded in `review/font-dependencies.json` to make exact-render comparisons diagnosable across font versions.

```sh
python3 -m pip install -r requirements.txt
bash build.sh
python3 verify_rebuild.py
```

Set PYTHON to your chosen Python executable if needed. PDF outputs and build logs stay in `build/`; exact-check data may be refreshed beside its generator. No absolute project paths, downloaded dependencies, cached TeX formats or cloud-specific configuration are required. A working distribution supplies normal TeX configuration. Rebuilt PDF bytes may differ because of timestamps or document IDs; validation checks displayed content instead. Inspect every new page after editing. Intentional changes make reference comparison fail until reviewed.

## Review and rights

Student writing, separate review and revision are complete for this draft. Historical reviews describe an earlier draft; final copies include documented repairs. The adult guide is a separate, untested teaching step with mathematical checks and visual QA. See `review/release-validation.md` for extracted-ZIP checks.

Exact mathematical and pedagogical sources are identified in the outline and adult guide. Local problems, prose, drawings and code are supplied as editable project material. Third-party sources retain copyrights and licenses. No third-party font files, source books/PDFs, downloads, caches, logs, rendered images or TeX binaries are bundled. No project-wide open-source license was present in the supplied material.

## Review guidance addendum

See [the approved review guidance addendum](AGENTS-review-guidance.md) when editing this material. It supplements any existing AGENTS.md.
