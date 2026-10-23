# Sorting networks and fixed machines: Week 23 editable release

Draft and unpiloted. Week 23 identifies an unscheduled activity-library slot, not a booked meeting. No adoption, classroom success or tested pacing is claimed. Prepared October 3, 2026.

## Table kit, October 23, 2026

`materials/build_materials.py` builds `materials.pdf` (reference copy in `reference-pdfs/`; print copy `week-23-materials.pdf`), four US Letter pages to print at 100%: a four-lane mat on two taped sheets (lanes 45 mm apart, 38 mm start and finish boxes), a card-stock sheet of 35 mm cards (K–1 dot cards 0, 0, 1, 1, 2, 3, 4; number cards 1–4 twice; four 0s and four 1s) and a card-stock sheet of 14 comparator bars (8 neighboring, 4 skipping a lane, 2 from lane 1 to lane 4) with a time strip. Every page has a 10 cm scale check and says how many to print per table. `materials/verify_materials.py` reads every size back from the PDF and checks the cards and bars against each problem's starts and machines; `build.sh` runs both, and the check needs PyMuPDF (now in `requirements.txt`). The guide's preparation section now names the kit and counts cutting time; no other guide page and no student page changed. The previous guide and source ZIP are archived in the project. The kit is physically unrehearsed.

## Problem files, October 23, 2026

The student pages are now stored as problem files, one per problem, in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-23/`): `week.toml`, `figures.py` (the old builder's drawing code and page template) and `problems/*.md`, with each band's wording and machines inside them. The conversion changed no wording or figure: the regenerated LaTeX matches the old `src/build_packets.py` byte for byte, and the three packets rebuild with identical text and pixels. `src/regenerate.py` writes the student LaTeX from the problem files, `src/check_networks.py` runs the old builder's exhaustive checks unchanged (writing `src/math-audit.json`), and `problem-files/tools/build.py` also builds first-route and return packets, a one-page problem menu and a key arranged by problem. The old builder is archived in the project.

## Print-ready material and flexible readiness

Four reviewed PDFs accompany this ZIP, with identical reference copies in `reference-pdfs/`.

k-1: 6 pages, 6 numbered problem entries; grades-2-3: 6 pages, 6 numbered problem entries; grades-4-5: 7 pages, 7 numbered problem entries; facilitator-guide: 13 pages. Student total: 19 numbered problem entries across the three bands. A continued problem is counted once. Related adaptations across bands are not claimed as distinct mathematical ideas.

Print selected student pages single-sided on US Letter at 100% / actual size. Start with a few pages and allow deep work; completing a packet is not the goal. Grade labels are approximate starting points. Choose by readiness and interest; adults can read, move materials or scribe:

- K-1: Compare two lengths or dot counts and follow three lanes under a fixed compare-exchange rule.
- Grades 2-3: Invent or repair a network while keeping the same comparisons for every starting order.
- Grades 4-5: Distinguish a counterexample from complete case coverage; threshold and reversible-history arguments are developed in the packet.

Mathematical kernel: Fixed compare-exchange networks, zero-one certification and exact small comparator minima.

The adult guide provides preparation, keyed solutions, reasoning, held hints and optional extensions. Quantities and timing are editorial suggestions, not verified inventory or classroom evidence.

## Mathematical overview and example revision

The guide now begins with one concise, unnumbered mathematical overview. It states the assumptions, principal facts, intended discoveries, grade-band routes, and the difference between trials, conjectures and explanations. Original numbered guide pages and their printed-page references follow. Upper p3 adds a position-matched threshold conversion (3,7,4 at t=4); p6 adds a two-comparator trace with S/N record. Student page and problem counts are unchanged.

Edit `facilitator-src/overview-content.json` for overview prose and `facilitator-src/build_overview.py` for its layout. The top-level build first regenerates and checks the numbered guide, then prepends the overview. Earlier detailed-guide QA records refer to the numbered body; the current reference manifest and release validation cover the complete PDFs.

## Contents and editing

- `problem-files/problems/*.md`: the student text, machines and examples, one file per problem; `problem-files/figures.py`: the drawing code and page template; `problem-files/tools/`: the problem-file tools. `src/regenerate.py` writes `src/*.tex` from them; `src/check_networks.py` checks every printed machine by exhaustion.
- `facilitator-src/build.py` and accompanying local modules/data: editable adult-guide prose and drawings.
- `materials/build_materials.py`, its generated `materials.tex` and `verify_materials.py`: the table kit and its measurements.
- Mathematics-check scripts and checked data remain beside their sources.
- `outlines/`: kernels, prerequisites, source attribution and materials.
- `review/`: historical student reviews, original adult QA, reference hashes and release-validation results. Original adult build instructions are historical; they may describe bundled fonts in the authoring workspace. This release excludes font binaries. Use this README and top-level build for the portable release.
- `verify_rebuild.py`: checks reference hashes and compares every rebuilt page's text, US Letter size and 100-dpi grayscale pixels.

Edit student problems in `problem-files/problems/*.md` (figures and the page template in `problem-files/figures.py`); `build.sh` regenerates `src/*.tex` from them and reruns `src/check_networks.py`, so do not edit the TeX by hand. When a machine changes, change it in `src/check_networks.py` too. To build every view: `python3 problem-files/tools/build.py problem-files --out views`. Edit the guide data for guide changes. Normal build regenerates student LaTeX; `bash build.sh --from-tex` instead preserves manual LaTeX edits. The adult guide is regenerated in either mode. Checks are tied to these examples and need deliberate updates if examples change. Keep reference PDFs unchanged unless issuing a newly reviewed release.

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
