# Shortest reflected paths: Week 21 editable release

Draft and unpiloted. Week 21 identifies an unscheduled activity-library slot, not a booked meeting. This is a new draft, not an approved replacement for the organizer's plans. No adoption, classroom success or tested pacing is claimed. Prepared October 3, 2026.

## Print-ready material and readiness gates

Four reviewed PDFs accompany this ZIP, with identical reference copies in `reference-pdfs/`.

k-1: 7 pages, 7 problems; grades-2-3: 7 pages, 7 problems; grades-4-5: 7 pages, 7 problems; facilitator-guide: 18 pages. Student total: 21 distinct numbered problems. A continued problem is counted once, not once per page.

Print selected student pages single-sided on US Letter at 100% / actual size. Start with a few pages and allow deep work; completing a packet is not the goal. Grade labels are approximate starting points. Choose by readiness and interest:

- K-1: Follow and compare two-leg routes; fold or trace with adult help, without numerical measurement.
- Grades 2-3: Use a straightedge, match reflected points and explain equal lengths; check that the contact lies on the allowed segment.
- Grades 4-5: Explain lengths preserved by folding and distinguish a tested guess from a claim about every allowed contact.

Mathematical kernel: Unfolding reflected paths, straight-line lower bounds and constrained reflection contacts.

The adult guide provides preparation, solutions, reasoning, held hints and optional extensions. Quantities and timing are editorial suggestions, not verified inventory or classroom evidence.

## Mathematical overview and example revision

The guide now begins with one concise, unnumbered mathematical overview. It states the assumptions, principal facts, intended discoveries, grade-band routes, and the difference between trials, conjectures and explanations. Original numbered guide pages and their printed-page references follow. The student PDFs are byte-identical to the preceding release. Existing labeled diagrams and explicit adult demonstrations already introduce the required objects and procedures.

Edit `facilitator-src/overview-content.json` for overview prose and `facilitator-src/build_overview.py` for its layout. The top-level build first regenerates and checks the numbered guide, then prepends the overview. Earlier detailed-guide QA records refer to the numbered body; the current reference manifest and release validation cover the complete PDFs.

## Contents and editing

- `src/build_packets.py` and `src/*.tex`: final student text, examples, diagrams and generated LaTeX.
- `facilitator-src/build_guide.py` and any accompanying JSON: editable adult-guide prose and drawings.
- Mathematics-check scripts and checked data remain beside their sources.
- `outlines/`: kernels, prerequisites, source attribution and materials.
- `review/`: historical student reviews, original adult QA, reference hashes and release-validation results. Original adult build instructions are historical; use this README and the top-level build for the portable release.
- `verify_rebuild.py`: checks reference hashes and compares every rebuilt page's text, US Letter size and 100-dpi grayscale pixels.

Edit the generators or guide data for changes that survive rebuilding. Normal build regenerates the student LaTeX; `bash build.sh --from-tex` instead preserves manual LaTeX edits. The adult guide is regenerated in either mode. Checks are tied to these examples and need deliberate updates if the examples change. Keep reference PDFs unchanged unless issuing a newly reviewed release.

## Portable local rebuild

Requirements: Python 3.10 or later, the Python packages in `requirements.txt`, a normal TeX Live or MacTeX providing pdflatex, TikZ/PGF, Latin Modern and standard LaTeX packages, and installed DejaVu Sans regular, bold and oblique fonts. Poppler's pdftoppm is required for the reference comparison; pdftotext is also used by the reflected-route prompt audit.

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
