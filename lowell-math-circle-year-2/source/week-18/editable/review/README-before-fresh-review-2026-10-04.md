# Error-correcting codebooks: Week 18 editable release

## Mathematical overview and examples revision

The guide now begins with a one-page mathematical overview: precise setting and hypotheses, main facts and limits, grade-band progression, and the distinction between experimentation, conjecture and proof. Original detailed solutions remain afterward, with guide-page references updated.

All three packets add a training page before Problem 1: 0101 becomes 0111 by changing only the third position. Only the final row crosses the folder in the game. Zero changes remain allowed. Each packet now has 7 pages; Problems 1-6 are unchanged and appear on pages 2-7.

Editable overview content is in `facilitator-src/guide.json`. Edit the student generator for the new examples; normal builds regenerate the supplied LaTeX. Reference PDFs and hashes describe this revision.

Draft and unpiloted. Week 18 identifies an unscheduled activity-library slot, not a booked meeting. This is a new draft, not an approved replacement for the organizer's plans. No adoption, classroom success or tested pacing is claimed. Prepared October 3, 2026.

## Print-ready material and readiness gates

Four final PDFs accompany this ZIP, with identical reference copies in `reference-pdfs/`.

k-1: 7 pages, 6 problems; grades-2-3: 7 pages, 6 problems; grades-4-5: 7 pages, 6 problems; facilitator-guide: 10 pages. Student total: 18 distinct numbered problems. A continued problem is counted once, not once per page.

Print selected student pages single-sided on US Letter at 100% / actual size. Start with a few pages and allow deep work; completing a packet is not the goal. Grade labels are approximate starting points. Choose by readiness and interest:

- K-1: Match two symbols and compare short rows; an adult can read directions.
- Grades 2-3: Keep ordered positions fixed; enumerate every outcome of zero or one change.
- Grades 4-5: Track positions and zero-or-one changes, and keep a proposed codebook distinct from a claim about every possible codebook.

Mathematical kernel: Hamming-distance separation, one-error correction and packing bounds.

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

Requirements: Python 3.10 or later, the Python packages in `requirements.txt`, a normal TeX Live or MacTeX providing pdflatex, TikZ/PGF, Latin Modern and standard LaTeX packages, and installed DejaVu Sans regular, bold and oblique fonts. Poppler's pdftoppm is required for the reference comparison.

Typical Debian/Ubuntu packages are texlive-latex-base, texlive-latex-recommended, texlive-latex-extra, texlive-pictures, lmodern, fonts-dejavu-core and poppler-utils. Use your usual local package manager. The font lookup consults ReportLab's font search path, Fontconfig when available, and user font folders. Set DEJAVU_FONT_DIR to a folder containing DejaVuSans.ttf, DejaVuSans-Bold.ttf and DejaVuSans-Oblique.ttf when needed. Font files are not bundled.

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

## Targeted worked examples, 4 October 2026

The example drawing lives in `src/examples.py`; the normal builder imports it and regenerates the TeX. `python3 src/check_examples.py` independently checks the example geometry or conversion without importing the packet generator or answer data. All pages were rendered and inspected; original task text/order and working-diagram dimensions were checked. References and the portable source ZIP describe this current revision. Earlier source releases are archived separately. These revisions remain unpiloted.
