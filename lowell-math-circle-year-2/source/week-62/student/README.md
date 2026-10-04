# Week 62 revised student source

Original student wording and TikZ figures around conflict-graph mathematics; precedents and local references are recorded in `plans/new-themes-52-63/week-62/source-notes.md`. No source figures or exemplar problems are reproduced. This is the revision-stage student packet, not a facilitator guide or classroom-tested release. The nine investigations preserve the draft's mathematical scope.

## Build

```sh
python3 /absolute/path/to/student/build.py --out /absolute/path/to/build-directory
```

`build.py` uses the same Python executable that invokes it, generates `students.tex` and `graphs.json` in the output directory, and runs `pdflatex` there. It produces `students.pdf`; build intermediates stay in that output directory. The included `students.tex` and `graphs.json` are current editable/reference snapshots of `make_source.py`'s output. Regenerate them intentionally with `python3 make_source.py` after changing the builder. No absolute paths or system fonts are required by the worksheet source.

Build dependencies: Python 3 standard library; `pdflatex` with standard TeX Live packages `geometry`, `fontenc`, `helvet`, `tikz` with `arrows.meta`, `fancyhdr`, and `array`.

## Checks

```sh
python3 /absolute/path/to/student/verify.py
python3 /absolute/path/to/student/verify_pdf.py --pdf /absolute/path/to/build-directory/students.pdf --tex /absolute/path/to/build-directory/students.tex --report /absolute/path/to/checks/pdf.json
python3 /absolute/path/to/student/render.py /absolute/path/to/build-directory/students.pdf --out /absolute/path/to/render-directory
python3 /absolute/path/to/student/compare_builds.py /absolute/path/to/first/students.pdf /absolute/path/to/second/students.pdf --report /absolute/path/to/checks/rebuild.json
```

Finite source checks use the Python standard library and current `graphs.json`; `checks.json` records their results. PDF extraction, rendering and rebuild comparisons additionally require PyMuPDF. Pillow is available for image QA but is not a build dependency. The designated repository QA environment is `tmp/bonus-35-51-venv/bin/python`; its path is not required for portability. `verify_pdf.py` adapts the independently authored reviewer checker in this run's `math-assets/independent_check.py`: it extracts actual PDF circles and conflict strokes, compares raw TikZ, enumerates finite answers, and checks the revised wording and all page 6 connection clearances. It does not load source-check results or builder JSON.

## Layout and prerequisites

All 104 full-size network circles are 20 mm in diameter for counters no larger than 15 mm. Activity letters occupy the upper part, leaving the lower part for slot numbers; small worked-output circles show the matching record. Slot cards are used on an unrestricted tabletop. The two page 6 boards use convex staggered sites; every straight connection stays at least 13 mm from every third site's center (10 mm radius).

Pages 1–3: Grades 2–5 entry, matching A–H card labels, counting through eight, retaining and checking pairwise conflicts; routine adult reading may help. Pages 4–8: Grades 4–5 reasoning, paths, several components, explaining impossibility and first-fit ordered trials; no multiplication required. Page 9: Grades 4–5 continuation, named assignments, systematic counting and small multiplication. These are readiness requirements, not age restrictions. The arbitrary-network explanation, eight-vertex first-fit tree, and complete named-assignment counting remain substantial continuations or return visits.

Digital verification does not establish material handling, kit preparation time, physical rehearsal or classroom fit. All remain unperformed/unpiloted. No remote upload or publication is claimed.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
