# Week 55 facilitator source

This is the separately authored facilitator guide W55-F-v1 for the final ten-page Grades 3–5 student packet W55-S-v2. It supplies the exact mathematical overview, concrete setup/launch, fixed-table staffing and print counts, readiness gates, complete keys, arbitrary-size proofs, return visits and evidence-scoped provenance. It contains no student edits or borrowed worksheet prose/figures. Physical kit-fit pretests, handling rehearsal, launch rehearsal and classroom piloting have not been performed.

## Build anywhere

Requires Python 3 (standard library), `pdflatex`, and standard TeX Live packages `geometry`, `fontenc`, `helvet`, `amsmath`, `amssymb`, `array`, `tabularx`, `booktabs`, `tikz`/PGF (`arrows.meta`), `fancyhdr`, `hyperref`. No repository data, workflow prompts, external book, asset file or student source is needed to build. The checker additionally needs PyMuPDF (`pymupdf`).

```sh
python3 /absolute/path/to/guide/build.py --out /absolute/path/to/output
python3 /absolute/path/to/guide/verify.py --pdf /absolute/path/to/output/facilitator.pdf --work /absolute/path/to/checks
```

The builder compiles twice in a temporary directory beneath `--out`, rejects overfull boxes, and writes only `facilitator.pdf`. It fixes the source timestamp and omits PDF creation dates and trailer IDs. The deliverable is nine US Letter portrait pages (612 × 792 points). The student packet is landscape; do not confuse print orientations.

The fresh verifier imports no student/research/reviewer code. It transcribes every printed fixed input, enumerates all 45 Problem 5 candidates, checks minimum/maximum kit designs for the printed sizes, independently generates every route in all three page-8 grids, and tests the common-gap theorem on all nonempty subsets of a finite kit. It also tests the alternate fixed-A and signed continuation examples. These finite tests are not the universal proof, which is fully written in the guide.

For digital portability it builds a clean copied source folder and a new ZIP-extracted folder, comparing every page's extracted text, dimensions and rendered pixels at 120 dpi to the supplied PDF. It writes JSON evidence and renders all pages under `--work`, outside this source folder. Inspect each rendered page visually after changes. Generated PDFs, source ZIP tests, logs, renders and evidence are not source assets.

## Provenance and boundaries

Read `AGENTS.md`, root `README.md` and `REPUBLISHING.md`, stage routing, final actual students.pdf and student notes, the independent math review/audit, Week 55 research/outline, current context and the current Week 1 K–1 pages/guide. Also read the local Tao–Vu sample pp.6–7, 67–71; *Math Circle by the Bay* Preface pp.viii–ix (PDF 9–10); *A Decade of the Berkeley Math Circle* pp.113–114 (PDF 133–134); and original year-1 *Handouts 1* DOCX XML. The guide's sources page distinguishes material actually found from new design inferences. Tao's entropy post's limited scope is retained from the research record, rather than claimed as a fresh primary consultation.

The sharp integer theorem/local path-swap proof is independently reconstructed elementary mathematics, not attributed to an uninspected chapter of Tao–Vu and not claimed as new mathematics. The guide does not claim to prove the general Freiman theorem. All figures and teaching prose in this source were newly authored. The portable source contains only this README, `facilitator.tex`, `build.py`, and `verify.py`; no exemplar prompt, borrowed book or third-party image is packaged.

K–1 uses a separate current Week 1 tiling option, with its own existing guide. This does not create or validate a sumset K–1 route. Printing/kit dimensions are digital specifications; physical handling and classroom piloting remain unperformed. No publication, remote upload, or current-release indexing is claimed by this guide-author stage.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
