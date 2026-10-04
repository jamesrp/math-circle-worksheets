# Averaging and the maximum principle: Week 20 editable release

## Worked-example revision — October 4, 2026

K-1 page 1 now shows fixed square values 0 and 6, a separate six-spare-cube copy, two neighbor mats including the zero neighbor, equal 3-cube piles, and circle 3 while the squares stay unchanged. K-1 page 2 shows completed 2-square--3-circle--4-circle--5-square and checks both circles with spare copies from that same unchanged board.

Grades 2-3 page 2 and grades 4-5 page 1 show the same completed chain, with (2+4)/2=3 and (3+5)/2=4 connected by leaders to their matching circles. These are simultaneous harmonic-value checks, not iterative updates. Examples do not duplicate a task solution. All 20 numbered tasks and checked answers are unchanged, and page counts remain 7 / 6 / 7. Packet IDs are GA20-K-v3, GA20-23-v2, and GA20-45-v3. Other page bodies retain their original source; their footer versions are updated.

The 25-page guide's shared launch now uses 0 and 6 with two piles of three; revision status, packet IDs, and fidelity wording are current. All solutions, page references and mathematical arguments remain unchanged. Run `python3 src/check_worked_examples.py` for independent example checks and the standard `python3 verify_rebuild.py` for all 45 current reference/rebuilt pages. See `review/worked-examples-2026-10-04.md`.

## Mathematical overview and examples revision

The guide now begins with a one-page mathematical overview: precise setting and hypotheses, main facts and limits, grade-band progression, and the distinction between experimentation, conjecture and proof. Original detailed solutions remain afterward, with guide-page references updated.

The October 3 guide revision left student PDFs byte-identical; the subsequent October 4 worked-example update is described above. The current 0-and-6-square launch explicitly demonstrates sharing into two piles with spare cubes; square/circle diagrams already identify the fixed and averaging places. No numbered problem was added or removed. Student page counts are unchanged; the guide has one additional page.

Editable overview content is in `facilitator-src/mathematical-overview.json`. Edit the student generator for the new examples; normal builds regenerate the supplied LaTeX. Reference PDFs and hashes describe this revision.

Draft and unpiloted. Week 20 identifies an unscheduled activity-library slot, not a booked meeting. This is a new draft, not an approved replacement for the organizer's plans. No adoption, classroom success or tested pacing is claimed. Prepared October 3, 2026.

## Print-ready material and readiness gates

Four final PDFs accompany this ZIP, with identical reference copies in `reference-pdfs/`.

k-1: 7 pages, 7 problems; grades-2-3: 6 pages, 6 problems; grades-4-5: 7 pages, 7 problems; facilitator-guide: 25 pages. Student total: 20 distinct numbered problems. A continued problem is counted once, not once per page.

Print selected student pages single-sided on US Letter at 100% / actual size. Start with a few pages and allow deep work; completing a packet is not the goal. Grade labels are approximate starting points. Choose by readiness and interest:

- K-1: Share small equal piles and compare values; use physical counters and oral directions.
- Grades 2-3: Read a graph as neighbors; add small collections and divide evenly by two or three to check all balances simultaneously.
- Grades 4-5: Check simultaneous averages and compare extremes; reserve uniqueness for children ready for signed differences, and gate fractions separately.

Mathematical kernel: Discrete harmonic functions, maximum propagation, uniqueness and boundary influence.

The adult guide provides preparation, solutions, reasoning, held hints and optional extensions. Quantities and timing are editorial suggestions, not verified inventory or classroom evidence.

## Contents and editing

- `src/build_packets.py` and `src/*.tex`: final student text, examples, diagrams and generated LaTeX.
- `facilitator-src/build_guide.py` and any accompanying JSON: editable adult-guide prose and drawings.
- Mathematics-check scripts and checked data remain beside their sources.
- `outlines/`: kernels, prerequisites, source attribution and materials.
- `review/`: historical student reviews, original adult QA, reference hashes and release-validation results. Original adult build instructions are historical; use this README and the top-level build for the portable release.
- `verify_rebuild.py`: checks reference hashes and compares every rebuilt page's text, US Letter size and 100-dpi grayscale pixels.

Edit the generators or guide data for changes that survive rebuilding. Normal build regenerates the student LaTeX; `bash build.sh --from-tex` instead preserves manual LaTeX edits. The adult guide is regenerated in either mode. Checks are tied to these examples and need deliberate updates if the examples change. Keep reference PDFs unchanged unless issuing a newly reviewed release.

## Portable local rebuild

Requirements: Python 3.10 or later, the Python packages in `requirements.txt`, a normal TeX Live or MacTeX providing pdflatex, TikZ/PGF, Latin Modern and standard LaTeX packages, and the Vera regular/bold/italic/bold-italic fonts supplied by the installed ReportLab package. Poppler's pdftoppm is required for the reference comparison.

Typical Debian/Ubuntu packages are texlive-latex-base, texlive-latex-recommended, texlive-latex-extra, texlive-pictures, lmodern, fonts-dejavu-core and poppler-utils. Use your usual local package manager. The adult guide finds Vera.ttf, VeraBd.ttf, VeraIt.ttf and VeraBI.ttf in the installed ReportLab package. Set MATH_CIRCLE_FONT_DIR to another folder containing those exact fonts if necessary. Font files are not bundled.

```sh
python3 -m pip install -r requirements.txt
bash build.sh
python3 verify_rebuild.py
```

Set PYTHON to your chosen Python executable if needed. Outputs and build logs stay in `build/`. No absolute project paths, downloaded dependencies, cached TeX formats or cloud-specific configuration are required. A working distribution supplies the normal TeX configuration. Rebuilt PDF bytes may differ because of timestamps or document IDs; release validation checks displayed content instead. Inspect every new page after editing. Intentional content changes make reference comparison fail until reviewed.

## Review and rights

Student writing, separate review and revision are complete for this draft. Historical review records describe the earlier student draft; final copies include the documented repairs. The adult guide is a separate, untested teaching step with independent mathematical checks and visual QA. See `review/release-validation.md` for the extracted-ZIP check.

Exact mathematical and pedagogical sources are identified in the outline and adult guide. The local problems, prose, drawings and code are supplied as editable project material. Third-party sources retain their copyrights and licenses. No third-party font files, source PDFs, books, downloads, cache files, logs, rendered images or TeX binaries are bundled. No project-wide open-source license was present in the supplied material.

## Review guidance addendum

See [the approved review guidance addendum](AGENTS-review-guidance.md) when editing this material. It supplements any existing AGENTS.md.
