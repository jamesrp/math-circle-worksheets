# Week 59 separate facilitator guide

Separately authored from the revised six-page `students.pdf` (W59-S-v2) and
three-page `materials.pdf` (W59-M-v1), after the independent student reviews.
This directory is a standalone original guide source, not a student rebuild.
It contains exactly five original files and needs no assets, references,
books, worksheet geometry, prompts or workflow exemplars. Root
`REPUBLISHING.md` was read and preserved. Established mathematics is not
claimed as newly invented. Source precedents and pedagogical passages are
identified on the guide's final page; local research references are not bundled.

From any working directory:

```sh
python3 /path/to/guide/build.py /path/to/output
python3 /path/to/guide/verify_math.py /path/to/output
python3 /path/to/guide/verify_rebuild.py /path/to/output
```

The builder uses Python's standard library and `pdflatex` on PATH. It writes
`facilitator.pdf` and `.guide-build/` inside OUTPUT, never source. Standard TeX
Live packages: article, geometry, T1 fontenc, helvet, amsmath, amssymb, booktabs,
array, TikZ/arrows.meta, fancyhdr and hyperref. Verification needs PyMuPDF
(`pymupdf`). Tested with `/Library/TeX/texbin/pdflatex` and the repository's
`tmp/bonus-35-51-venv/bin/python`. No network or nonstandard fonts are needed.

`verify_math.py` reconstructs disk-intersection extremum candidates independently,
checks both construction sizes in 7,200 directions, sector endpoints, all controls,
the marked-centroid bounds, fixed-gap classes, convention examples and direct
perimeter equality. It imports no author geometry. It checks both compiled guide
Reuleaux sketches, their three equilateral vertices, whole-body support lines and
perpendicular gap using analytic cubic-projection extrema. Finite samples catch
errors; they do not replace the all-direction proof or certify uniform errors.

Optional checks on the revised companion PDFs, without their source:

```sh
python3 /path/to/guide/verify_math.py /path/to/output \
  --students /path/to/students.pdf --materials /path/to/materials.pdf
```

These inspect the actual three 100 mm bars, 200 mm grid, both full-size template
variants, both Reuleaux cutouts, the sampled cubic disk, R1's current rules and
R2's off-center rectangle/32 mm display segments. Companion PDFs are not needed
to build or verify the standalone guide and are not bundled in this directory.

`verify_rebuild.py` uses an explicit five-file inventory, copies it and separately
ZIP-extracts it into clean directories, builds and independently checks each,
then compares all eight guide pages' text, dimensions and pixels at 108 dpi.
Its check ZIP and logs remain in OUTPUT/guide-qa/rebuild as QA intermediates.
Root owns final packaging/review/promotion. Neither the guide nor its sources
have been published or uploaded; no earlier week or global index is modified.

The guide begins with precise theorems/assumptions and distinguishes observation,
conjecture and explanation. It supplies P1–6 solutions, adult hints, five pair
kits for the actual eleven children/three anchored adults, an oral shallow K–1
entry or familiar alternative, first-hour/return routes and original equal-scale
proof sketches. The diagrams are not new actual-size templates. Material counts
come from the actual materials PDF; kit assembly is reusable. Preparation and
timing estimates are explicitly untested.

**Unperformed:** actual printer scale/margins, stiff-card cutting/contact, rail
clearance/parallelism/fixed 60 mm gap, right-angle guide operation, perpendicular
measurement, compass-radius retention, timing and classroom piloting. A proposed
±1–2 mm apparent-width tolerance is not a verified guarantee. No smooth rolling,
platform, axle or square-hole apparatus has been tested. Digital support widths
refer to PDF cubic approximations; source reviews' disk range
60.000456–60.016920 mm and greatest sampled Reuleaux error 0.001631 mm are
finite samples, not certified universal bounds or physical tolerances.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
