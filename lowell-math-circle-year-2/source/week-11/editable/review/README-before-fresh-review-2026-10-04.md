# Chip firing with a sink: Week 11 editable release

New, draft and unpiloted. Week 11 is an activity-library label, not a scheduled meeting. No classroom success or organizer approval is claimed. Prepared October 3, 2026.

## Print and choose

Four final PDFs accompany this ZIP; identical reference copies are inside `reference-pdfs/`. The adult guide now begins with a theorem-first overview and concise problem-to-fact map. All three student PDFs and their source files are unchanged. Counts: k-1: 6 pages, grades-2-3: 6 pages, grades-4-5: 6 pages, facilitator-guide: 12 pages. The three student packets contain 18 distinct numbered problems in total. Where a problem continues onto another page, it is not counted twice.

Print selected student pages single-sided on US Letter at 100% / actual size. Give each child only a few pages at a time. Finishing every page is not the goal. Grade bands are approximate entry points, not age restrictions.

Prerequisites: Small counts and a spoken one-chip-per-line rule; older entries add move records and reasoning about all legal orders.

Mathematical kernel: Abelian stabilization with an absorbing sink; staged addition and non-reversible dynamics.

The guide supplies a proposed ten-child preparation plan, brief shared launch, flexible one-hour menu, held hints, extensions and keyed reasoning. Quantities are preparation suggestions, not verified inventory; pacing and classroom suitability remain untested.

## Editable contents

- `src/build_packets.py`: final student text, instances, diagrams and generator.
- `src/*.tex`: generated editable student LaTeX.
- `facilitator-src/mathematical-overview.tex`: editable theorem summary, grade map, proofs, and final-state calculation methods.
- `facilitator-src/build_guide.py`: editable adult preparation notes and detailed solutions; reads the overview and generates the complete guide.
- `facilitator-src/verify.py` and checked JSON data: independent final-instance mathematics.
- `outlines/`: mathematical kernels, prerequisites, references and physical constraints.
- `review/`: historical student reviews, facilitator QA record, reference hashes and release validation. Historical records may mention work files or original paths; those excluded intermediates are not required for rebuilding.
- `verify_rebuild.py`: reference integrity, page counts, paper sizes, extracted text and every-page 100-dpi grayscale comparison.

Prefer editing the Python generators for changes that survive rebuilding, and edit `facilitator-src/mathematical-overview.tex` for the three opening adult pages. The normal build regenerates LaTeX. `bash build.sh --from-tex` preserves supplied or edited LaTeX. Example-specific checks must be deliberately updated if examples change. Reference PDFs should stay unchanged until a new reviewed release is issued.

## Portable local rebuild

Requirements: Python 3.10 or later; the packages in `requirements.txt`; a normal TeX Live or MacTeX providing `pdflatex`, TikZ/PGF, Latin Modern, and standard packages including geometry, fontenc, amsmath, amssymb, array, booktabs, enumitem, fancyhdr and hyperref. Week 11 also needs type1cm. Typical Debian/Ubuntu packages: texlive-latex-base, texlive-latex-recommended, texlive-latex-extra, texlive-pictures, lmodern. Poppler's `pdftoppm` is required for `verify_rebuild.py`; `pdfinfo` is useful for inspection.



```sh
python3 -m pip install -r requirements.txt
bash build.sh
python3 verify_rebuild.py
```

Set `PYTHON=/path/to/python` if needed. Run in a local Python environment. Build outputs and logs stay under `build/`. No cached TeX format, downloaded dependency, absolute project path or cloud-specific TeX configuration is required. Intentional text/geometry edits make reference comparison fail until a new release is reviewed. Inspect all newly generated pages after editing.

## Review status, attribution and rights

Student writing, separate adversarial review and revision are complete for this draft. Historical review records describe the earlier draft; the final PDFs include the documented revisions. The facilitator guide is a separate, untested teaching step with independent mathematical checks and visual QA. See `review/release-validation.md` for the extracted-ZIP rebuild comparison.

The exact mathematical and teaching references, sections and page numbers are recorded in the topic outline and adult guide. The local problems, examples, prose, drawings and check code are supplied as editable project material. Third-party sources retain their own copyrights and licenses; reference PDFs/books, fonts, render caches and TeX binaries are not bundled. This package does not assign an open-source license to third-party works or imply a blanket redistribution permission. No project-wide license was present in the supplied source tree.

## Review guidance addendum

See [the approved review guidance addendum](AGENTS-review-guidance.md) when editing this material. It supplements any existing AGENTS.md.
