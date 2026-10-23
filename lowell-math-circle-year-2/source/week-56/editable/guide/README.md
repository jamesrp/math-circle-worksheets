# Week 56 facilitator guide source

Original independently authored adult guide for the finished nine-page `students.pdf` (N56-S-v2) and four-page `materials.pdf` (N56-M-v1). The guide is ten US Letter pages, footer N56-FAC-v1. It does not alter the student or material files. All guide prose and inline TikZ figures are newly authored; established mathematics and teaching precedents are cited on guide p.10. There are no copied book pages, workflow prompts, exemplar blocks, reference duplicates, PDFs or intermediate renders in this directory.

## Build from any location

```sh
sh /absolute/path/to/guide/build.sh /absolute/path/to/output
```

Produces `OUTPUT/facilitator.pdf`; TeX intermediates use a disposable temporary directory. Requires `pdflatex` and standard TeX Live packages: article, geometry, fontenc, helvet, tikz/arrows.meta, array, tabularx, fancyhdr, amsmath, amssymb and hyperref. Standard Helvetica and Computer Modern math fonts are used; no machine-specific font paths or external assets are required.

## Independent mathematics and PDF checks

```sh
python3 guide/check_answers.py /absolute/path/to/qa
python3 guide/check_answers.py /absolute/path/to/qa students.pdf materials.pdf facilitator.pdf
python3 guide/clean_rebuild.py /absolute/path/to/facilitator.pdf /absolute/path/to/qa/rebuild
```

The first command uses only Python's standard library. The optional PDF checks and rebuild comparison require PyMuPDF. The repository runtime `tmp/bonus-35-51-venv/bin/python` supplies it. Put QA outside `guide-src`.

`check_answers.py` is a fresh answer checker, not a reused student/research/reviewer checker. It manually transcribes final material blue vertex labels into face cycles and supplies independently chosen 3D realizations. It reconstructs edges and their two-face incidence; computes planar face angles at all vertices; checks all four regular/equal-vertex models and the unequal square pyramid; tests all six printed fan lists using a symmetric local cone calculation; constructs all three independent cube subdivisions and checks new zero gaps; transcribes final planar cube/tetrahedron graphs and traces bounded regions without using Euler to supply their count; verifies a connected deletion route through outside merges and enumerates spanning trees; recomputes polygon sums, regular-polygon candidates and reverse inventories; independently constructs convex hulls for the two specific reverse solids. This is mathematical realization, not a physical folding test. Preparation arithmetic is also checked.

With all three PDFs supplied, the checker confirms the final problem numbers/grade labels/scope, measures all 28 net faces and 16 loose fan cutouts for 30 mm sides and correct 60/90-degree angles, measures both 80 mm circles, checks guide dimensions/margins/header/footer, and renders every guide page. Human visual inspection remains required: the numeric checks cannot detect every layout defect.

`clean_rebuild.py` makes a clean source copy and a lean temporary ZIP, extracts the ZIP into a second clean directory, and independently builds both. It compares every page's exact extracted text, dimensions and rendered pixel bytes at scale 1.5 with the delivered guide. It reruns the standard-library mathematics checker from each independent source tree. Results and the test ZIP live in QA; root owns final release packaging.

## Mathematical and teaching provenance

Mathematical precedents: Keenan Crane, *Discrete Differential Geometry: An Applied Introduction*, Exercise 2.1 (printed p.22 / PDF p.23), Exercises 5.9-5.10 (printed pp.95-96 / PDF pp.96-97); Vicky Neale, NRICH, *Euler's Formula*, planar theorem/edge-removal proof and final polyhedra discussion; Thomas F. Banchoff, *Beyond the Third Dimension*, Chapter 5 section 2 and Chapter 6 section 3. URLs and distinctions between our derivation and these precedents appear in the guide. The guide's scope requires a finite closed convex polygon-face polyhedron, or a consistent polygonal sphere cellulation with disk faces, whole-edge attachments, two-face incidence and manifold neighborhoods. Subdivision vertices may have zero defect. Positive local fan defect does not alone establish whole-solid assembly. Outside-region merges are permitted in the tree reduction.

Teaching sources actually consulted: Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, printed pp.viii-x (PDF pp.9-11); Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 7, “At the lesson,” items 1-2 (`OEBPS/part0017.xhtml`); organizer's *Handouts 4.docx*, Problems 4.2-4.5. Their actual reported evidence is distinguished from our timing, younger entry and material choices. The latter are unpiloted adaptations, not validated by citation.

## Operational limits and use

The current group is eleven children (KK11 / 3333 / 445), three fixed tables and three anchored adults. Student pp.1-6 are Grades 2-5 concrete/arithmetic-supported work; pp.7-9 are Grades 4-5 continuations. The optional younger entry is an adult-read, adult-recorded fan investigation with real child choices, not an independent K-1 packet. Several return visits are supported. The guide lists exact active/spare print allocations: 15 assembled solids; five fan sets and one spare set; 18 cardstock and 32 student sheets, plus guides.

No real print-scale measurement, cutting/folding/tape-fit rehearsal, staffing trial, preparation/session timing trial or classroom piloting was performed. The guide names those physical pretests and the limits of the digital evidence. No remote publication/upload or local release-index edit is part of this guide stage.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
