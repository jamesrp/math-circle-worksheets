# Week 52 independent facilitator guide source

Current guide: **F52-FAC-v2**, 10 US Letter pages, separately authored October 4, 2026 for the final 12-page student packet **F52-S-v2**, Problems 1–14. No student page, historical output, workflow prompt or global file was edited. Physical fabrication/fit, pin freedom/slop/friction, tabletop handling, three-adult servicing rehearsal and classroom piloting are unperformed.

## Portable build

A standard TeX Live installation needs `pdflatex`, article, geometry, fontenc, helvet, TikZ (arrows.meta), amsmath, amssymb, array, tabularx, fancyhdr, microtype, xcolor, enumitem and hyperref. All text, tables and TikZ figures are authored in `facilitator.tex`; there are no external images, repository include paths or special fonts. Build from any working directory:

```sh
sh /absolute/path/to/guide/build.sh /absolute/output/directory
```

The builder writes `facilitator.pdf` only; intermediate files go into a temporary directory and are removed. It rejects overfull boxes. It uses a fixed build date for reproducibility. The portable bundle contains original guide source, build/check scripts and this README. No generated prompts, borrowed exemplar blocks, downloaded books, rendered images or duplicate reference PDFs belong in it. Root `REPUBLISHING.md` was read and preserved.

## Independent verification

The mathematical verifier does not import student source, research/reviewer checks or their computed answers. The cell sets were read from final student diagrams and independently checked against actual PDF vector paths. Graph groups are compared with exact rational ranks of separately constructed physical joint/bar rigidity matrices. The finite-flex routine constructs actual joint positions by sums of independently rotated strip vectors, checks all bar lengths and both possible diagonal orientations, and verifies an unbraced diagonal changes. It also independently checks all four exact circle-intersection choices for P3, including both square placements and both coincident-corner doubled triangles, and a sampled continuous fixed-side path from the square through collinear collapse to overlap with the diagonal removed. It recomputes K–1 lengths, all small minimum designs, all 15 P10 pairs, P11 addition locations, all covered six-brace 3-by-3 cases, extremal covered disconnected bounds and exact base/spare kit totals. Geometry reasoning in the guide establishes the universal facts; finite samples are supplementary checks.

```sh
python3 guide/verify_guide.py --output /absolute/output/guide-math-checks.json
```

Optional actual-student-PDF path audit needs **PyMuPDF** (import `pymupdf`) and checks 17 printed braced grids: P4A–D, P7A/B, P8A/B, P9, four P10 references, P11A/B and both non-task worked-example input/intermediate grids. It checks brace cell positions, opposite-corner endpoints and equal cell axis scale. It records the audited student PDF hash. All other final student pages were visually read, including K–1 triangle/square, blank minimum maps and upper blank investigation grids.

```sh
python3 guide/verify_guide.py --students /absolute/path/students.pdf --output /absolute/output/guide-math-checks.json
python3 guide/check_pdf.py /absolute/output/facilitator.pdf /absolute/output/guide-render --clean-rebuild
```

`check_pdf.py` needs PyMuPDF and creates one PNG per guide page, extracted text and a digital report. It checks 10 Letter pages, headers/footers and text bounds. Its clean rebuild copies the full source and separately ZIP-extracts it into fresh temporary directories, builds both from `/tmp`, and compares every page's text, dimensions and rendered pixels. All temporary copied/extracted packages are deleted after checking. In this repository, `tmp/bonus-35-51-venv/bin/python` supplies PyMuPDF. Generated reports/renders stay outside `guide/`. Bounds checks do not replace visual inspection of every final page.

## Session and age fit

Eleven children: KK11, 3333, 445; three adults anchored at fixed tables. Two pairs at each younger table; upper trio rotates builder/tester/recorder. K–1 needs adult reading and pin service, no arithmetic. Third graders count to four and retain cell positions; the physical core is P4–5. Ready Grades 3–5 count to six and retain two label systems after a meaning-bearing physical handoff. Ready upper minimum/universal arguments require connectivity and group reasoning; they are usually return-visit material. No algebra or calculus is required. Children own pushes, placements, records and conjectures; an adult can read or handle fasteners without choosing their mathematics.

P3 is an open refitting question with no printed ban on overlapping bars or coincident joints. Its full ideal answer is a square when the two remaining corners occupy distinct circle intersections, or an overlapping doubled right-isosceles triangle when they coincide. Only the square fits on the ordinary nondegenerate simple rhombus branch. A child who finds the overlap exception should receive credit; a real kit may prevent it physically. The removed-diagonal transition passes through a collapsed placement and is not a motion of the square with its diagonal attached.

The grid theorem concerns continuous local rigidity/flex from the initial nondegenerate square placement, rather than every remote or collapsed embedding after removing constraints. It assumes complete initial planar square grids, freely turning non-sliding joints, fixed side bars and rigid cell diagonals; it excludes holes, masks/missing bars, long braces, cables, locked/sliding joints and out-of-plane motion. The guide opens theorem-first, explicitly separates first-order from finite continuous rigidity and supplies a separate finite propagation/construction proof. It includes every task/diagram answer; P6 asks several designs, characterized as any four cells except an omitted full column rather than requiring children to enumerate all 12. P10's 15 unordered removals are completely classified for adults. P13's 78 covered six-brace cases are verified, but the capacity proof is the explanation. The P14 nine-brace covered counterexample is also checked as an actual finite flex.

The child-owned two-group handoff uses the spare standard 2-by-3 model with (1,1),(1,2),(2,3), or P4B's finished 2-by-2. It labels actual strip bar directions, retains all dots, and lets children choose an added brace and test it before the paper-only criterion. No 3-by-3 kit is required for the main route. The material fabrication dimensions are hole-center distances, not total bar lengths. The 45–60 minute initial preparation and 10–15 minute reset are forecasts under stated ready-stock/tool assumptions, not measurements.

## Source/provenance record

Established mathematical precedents:

- Ethan D. Bolker and Henry Crapo, **Bracing Rectangular Frameworks. I**, SIAM Journal on Applied Mathematics 36(3) (1979), 473–490. [Publisher abstract](https://epubs.siam.org/doi/abs/10.1137/0136036), DOI 10.1137/0136036. The abstract/bibliography were read; full original article was unavailable. The abstract identifies minimal rigidifying plane-square-grid brace sets with complete-bipartite spanning trees. No internal page-specific proof was claimed read.
- Georg Grasegger and Jan Legerský, **Bracing frameworks consisting of parallelograms**, [arXiv:2008.11521v1](https://arxiv.org/abs/2008.11521v1) (2020), Theorem 1.1 p. 3; Definition 3.8 p. 8 and 3.17/3.19 pp. 13–14; finite-flex/graph proof pp. 16–17. Those pages were read directly from the repository's local primary PDF. Its general P-framework theorem supports the distinction between first order and finite motion; the guide's elementary complete-grid argument is independently written.

Pedagogical evidence read directly:

- Natasha Rozhkovskaya, **Math Circles for Elementary School Students** (AMS, 2014), Lesson 7, “At the lesson,” §2, printed p. 122, local EPUB `OEBPS/part0017.xhtml`: reported enthusiastic K’nex polygon construction, not a bracing-criterion lesson.
- Laura Givental, Maria Nemirovskaya and Ilya Zakharevich, **Math Circle by the Bay** (AMS, 2018), “How we teach,” printed p. ix (PDF p. 10): manipulatives, accessible clear statements, independent solving and explaining.
- Organizer's year-1 **Handouts 3.docx**, P3.4–3.7, and **Handouts 4.docx**, P4.2–4.5: physical pattern-block constructions, varied filling and symmetry grouping. Exact task text was read; it is not reproduced here.
- Current `worksheet-workflow/context.md`: organiser's concrete materials versus paper-rule experience. The actual group is its October 3 update, eleven children; the older README group count was not used for fabrication.

The sources provide mathematical/teaching precedents, not evidence our adaptation has been rehearsed. Guide wording, lookup tables, TikZ figures, elementary proofs and verifier are newly authored around established mathematics. The particular material kit, preparation time, physical-to-link route and flexible pacing are untested design choices. No novelty or public-republication clearance is claimed. Local research/reviews were read as context but not used as answer evidence in the independent check.

## P3 scope correction after independent root review

The earlier guide incorrectly limited P3 to squares under all ideal flat bar rules. This version qualifies square-only to the simple nondegenerate rhombus branch, supplies the coincident-corner overlap solution, and credits it without adding a student restriction. `verify_guide.py` checks squared lengths exactly for all four labeled intersection choices and numerically checks the continuous removed-diagonal path. The current guide PDF omits the obsolete internal pending-review sentence. No student page changed. Other mathematical answers and kit routes are retained.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
