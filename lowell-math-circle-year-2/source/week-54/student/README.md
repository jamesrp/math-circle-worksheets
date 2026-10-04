# Week 54 revised student source

This is the unpiloted revised student packet, not an approved release or facilitator guide.

Build one nine-page US Letter combined packet:

```sh
sh build.sh /absolute/path/to/output-directory
python3 verify_math.py > /absolute/path/to/math-checks.json
```

`students.tex` contains original authored wording, diagrams and layout. TeX Live packages: article, geometry, fontenc, lmodern, helvet, TikZ (arrows.meta). `build.sh` accepts a fresh output directory and uses a temporary directory for all TeX intermediates. Python mathematical verification uses only the standard library. Render inspection uses PyMuPDF outside the source bundle; it is not a build dependency.

## Prerequisites and access

- Pages 1–5, approximate Grades 2–5: count identical units, compare sizes, add to totals 4–24, recognize odd/even sizes and divide even strips into equal halves. The longest-first row or sum-of-sizes record is demonstrated on page 1. An adult may read and record while children make the grouping and rebuilding choices. Catalog completeness and matching require comparison of whole collections and retention of a legal joining/splitting rule.
- Pages 6–9, approximate Grades 4–5: additionally follow two rebuilding histories, read rows and columns, classify whole catalogs, and explain why a correspondence or joining result works for any total. Binary numeral notation, algebra and advanced reading are not prerequisites. Pictures, physical strips and oral explanations may carry the reasoning.
- No independent K–1 packet is claimed. A younger child may physically form small groups with an adult, but the complete comparison and reversible-map tasks are beyond that shallow entry.

## Materials and preparation

For each active pair: 24 identical unit squares or snap cubes, preferably 10–15 mm across; about 42 × 30 cm of table area; two trays or paper lanes labelled before and after; pencil, eraser, blank paper or whiteboard. Three active pairs use 72 units. At the 4–5 table the third child rotates builder/checker or partners with the mathematician. Work beside the sheet: printed diagrams and boxes are records, not exact-fit manipulatives mats. Every printed physical case uses at most 24 units and preserves its total. Extra paper supports shared catalogs and longer rebuilding histories.

The group should handle pieces before the short common demonstration of a legal grouping and record. The student page depicts the first record, join, split and row/column conversion through input, a meaningful intermediate state, and output. This note records intended preparation; material handling, rule retention, staffing fit and classroom pacing remain untested.

## Mathematics and provenance

The destination is Euler's equality between partitions into odd parts and partitions into distinct parts, established by joining equal pairs and splitting even parts. Joining within an odd core is carrying in powers of two; this gives termination, independence of order, and both inverse identities. Rows/columns give the involutive correspondence between at most three strips and largest size at most three. All parts are positive and unordered; moving, recolouring or labelling units creates no extra collections. The two restricted families overlap and are counted separately by their respective rules.

Adaptation precedents, actually consulted in the outline research: Peter Koroteev, *Integer Partitions* (Berkeley Math Circle 2020), §1 pp.1–3 and §2.2 pp.6–9; Elysee Wilson-Egolf, *Counting: Partitions* (2018), p.1 for the row/column comparison. Wilson-Egolf's p.3 total-seven count is erroneous; it is excluded. Mathematical and pedagogical research citations and prior-packet overlap audit remain in `plans/new-themes-52-63/week-54/research.md` at the repository root. No source wording, reference figures, borrowed exemplar blocks, books, workflow prompts or reference PDFs are included in this authored source directory.

All examples and catalog data are checked by `verify_math.py`; finite checking does not prove the general theorems. The general arguments are recorded above and in the research notes. Fresh student and independent mathematical reviews identified one required edit: Problem 6 now requires joining routes to continue until all sizes are different. The open order-independence question and all-total explanation remain child-owned. Page 8 also keeps the word "total" unbroken. A separate future adult guide remains outside this revision stage.

Revision verification rendered and inspected all nine pages, recomputed the 18-unit joining case and all existing finite mathematical checks, and built from a fresh copied source directory. Text, page dimensions and rendered pixels matched the delivered PDF. No physical handling rehearsal or classroom piloting was performed.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
