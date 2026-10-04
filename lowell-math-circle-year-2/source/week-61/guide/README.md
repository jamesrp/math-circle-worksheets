# Week 61 original facilitator guide

W61-F-v1 accompanies the accepted seven-page student packet W61-S-v2. Authoring is separate from the worksheet stages. The current roster is 4/4/3 children at fixed K–1 / Grades 2–3 / Grades 4–5 tables, with three anchored adults. All fabrication, exact marking, material fit/handling rehearsal and classroom piloting remain unperformed.

This portable guide source is self-contained: original `facilitator.tex`, standard-library `build.py` and independent mathematical `verify_math.py`, plus this README. It imports no student generator or source figures and needs no external assets. No reference book, borrowed exemplar, prompt, intermediate or render belongs in the package.

Build requires Python 3 and pdfLaTeX with the standard packages declared in the TeX file:

```sh
python3 build.py /absolute/path/to/output
python3 verify_math.py /absolute/path/to/output/math-checks.json
```

All TeX intermediates go to the output directory's `build/`; the source stays clean. The deliverable is `facilitator.pdf`, nine single-sided US Letter pages. Source/build checks, clean copied and ZIP-extracted rebuilds, render comparisons, per-page inspection and mathematics evidence are retained in the run's separate `guide-qa/` directory. Numerical checks illustrate the exact general proof; they are not a substitute for it or a physical rehearsal.

Mathematical and pedagogical references with exact page/lesson locators are in the guide. Wording and detailed sign-cell explanation are newly authored around credited established mathematics. Root REPUBLISHING.md was read unchanged. This guide claims neither publication clearance nor a current remote copy.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
