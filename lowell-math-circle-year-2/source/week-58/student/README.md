# Week 58 revised student and material sources

Current local review candidate: `students.pdf` (7 pages) and `materials.pdf` (10 pages), footer version v2. These sources build one combined student packet, under the direct routing in `plans/new-themes-52-63/STAGE-ROUTING.md`. No K–1 packet or separate three-band variants are claimed. This source bundle contains no facilitator guide; separate guide authorship and review follow the final student-page review. Nothing has been published or uploaded.

Build from any working directory:

```sh
sh /path/to/student/build.sh /path/to/output-directory
python3 /path/to/student/verify_math.py /path/to/output-directory/math-checks.json
python3 /path/to/student/verify_pdf.py /path/to/output-directory
```

`build.sh` needs standard TeX Live `pdflatex`, `article`, `geometry`, `fontenc`, `helvet`, `TikZ`, `fancyhdr`, `array`, `xcolor`, and `pdflscape`; no custom fonts or external assets. It uses a temporary build directory and fixed compilation timestamp. Digital inspection needs PyMuPDF; the repository runtime is `tmp/bonus-35-51-venv/bin/python`. The mathematical verifier uses Python's standard library. `verify_pdf.py` renders every page, checks actual vector dimensions and inventory, and independently rebuilds both a clean copied source folder and a fresh ZIP extraction, comparing all PDF text, dimensions, rotation and rendered pixels. Its outputs go outside `src/`.

## Prerequisites and page scope

* Pages 1–2, approximate Grades 2–5: reading the problem aloud is acceptable. Add card values at most 3, compare sums at most 10, keep one observer fixed while evaluating both trays, and distinguish labelled cards. Page 1 leaves division and choice with the children; page 2 asks for a complete labelled catalog. The page-2 score table refers to one saved record, not a second ledger for every allocation. Younger children can use the oral divide/choose entry, controlling the decisions, without attempting the written catalog or receiving an arithmetic guarantee for whole cards.
* Page 3, approximate Grades 2–5: measure lengths, add the whole-panel values to 4, understand a parallel cross-cut and constant value per unit length within one color, and reason about equal own value. Children choose the cut and the chooser's piece; the sketch plus its distance label is the single recoverable record. Exact alternative-observer scores involving thirds are not required on this page. If a child cannot retain the fixed-observer/partial-panel convention after the short demonstration, return to the whole-card route rather than having an adult make the mathematical decisions.
* Page 4, approximate Grades 3–5: explain a universal guarantee using equal own values and the chooser's maximum; contrast equal-value and equal-length cuts. Adult reading or writing support may help; the argument remains the child's work. The stated theorem assumes an exact equality that a scissors experiment only approximates.
* Page 5, approximate Grades 2–5: compare whole-card counts up to 3, reason that equal counts are impossible with an odd total, and understand equal halves of a square. Objects support the impossibility argument; decimal or fraction notation is unnecessary. The paper R3 **replaces** the sturdy R3, so the total value stays 3.
* Pages 6–7, approximate Grades 3–5: add values up to 12, use one unchanged row to compare three bundles, understand a third of 12, and distinguish a counterexample from a universal explanation. Page 6's score table is explicitly for the printed initial A:X/B:Y/C:Z allocation; children then repair the physical allocation and may save it on the existing lines. The complete-allocation and additive-value assumptions are essential. No full three-person trimming procedure is included.

Readiness-dependent continuation for the later adult guide: after children have made and chosen physical cuts on page 3, fraction-ready children may find each observer's exact values for both pieces. This requires scaling 150 mm panel values to thirds and adding fractions; it is additional mathematics, not adult completion of a mandatory student table. The exact A cut is 100 mm from the red/left end: A sees (2,2), B sees (2/3,10/3) and chooses right. The exact B cut is 200 mm: B sees (2,2), A sees (10/3,2/3) and chooses left. Keep these answers with adults. Positive panel densities make the exact cuts unique.

## Exact whole-group material print recipe

The current planning group is eleven children at three fixed adult-led tables: KK11 / 3333 / 445. Prepare **five pair kits** (two younger, two middle, one upper pair with a rotating referee), plus **one additional three-person kit**. A referee in a two-person trial is not a third recipient.

Print US Letter single-sided at **100%, actual size**. Material pages 2–5 are landscape; the rest are portrait. Verify the 100 mm bar on each page before using it. The following is the recommended consumable stock, not ten compulsory strip trials:

| Material PDF pages | Copies of each page | Preparation / whole-group result |
| --- | ---: | --- |
| 1 | 5 | Print on ordinary paper. Mount only R1,R2,R3,B1,B2 on sturdy backing: 25 reusable 25×25 mm cards total. Leave the separate R3 square unmounted: 5 cuttable paper replacements. Do not mount the whole page. |
| 2 | 5 | One two-person A/B set per pair: 10 preference cards, each 100×150 mm. |
| 3 | 5 | One U/V set per pair: 10 red-only preference cards, each 100×150 mm. |
| 4–5 | 1 | One additional upper kit: 3 distinct X/Y/Z observer cards, each 100×150 mm, and 3 whole panels X,Y,Z, each 50×40 mm. Do not print these pages five times. |
| 6–10 | 5 | Twenty 150×40 mm halves per pair, forming **ten full 300×40 mm strips per pair**. Whole-group stock: 100 halves forming 50 full strips. |

This recipe uses **42 printed material sheets**, plus the sturdy backing for the reusable small cards. Each of five pair kits has five reusable goods, one paper R3 replacement, four preference cards and ten finished strips. The separate upper kit has three observer cards and three panels. There are no green goods or unused card labels in the delivered material set.

A smaller first-route subset is **five copies each of pages 1,2,3,6,7**, plus **one copy each of pages 4,5**: 27 printed sheets. It supplies four finished strips per pair (8 halves), 20 full strips total (40 halves). This allows the two page-3 role trials, the page-4 join-cut counterexample, and one retry per pair. Pages 8–10 are additional labelled consumable stock for repeated attempts or later visits. Further retries need further strip copies. The card and upper-kit quantities are the same in both recipes.

Separately supply **ten pair trays** (two 150–180 mm trays per pair), **three upper trays**, **five rulers** (one per pair), blank paper and pencils. Adults hold scissors; three adult scissors can serve the fixed tables. Butt-join each matching red and blue half by strip number, red on the left and blue on the right, with no gap or overlap; tape only on the back. Twenty halves are ten strips, not twenty strips. Keep pair kits separate when strip numbers repeat across copies.

Problem subsets: page 1 uses R1,R2,R3,B1; page 2 uses R1,R2,B1,B2; page 5 uses R1,R2,R3 with U/V. Remove other goods. In page 5's second trial, **put the sturdy R3 away before introducing the paper R3**, keeping only R1,R2 and that replacement. The whole paper square is value 1, with equal areas having equal value; the red circle is an identifying icon. Only resources explicitly declared splittable may be cut. The upper route uses its separate X/Y/Z cards, not the two-person color preferences. Keep every observer card fixed within a trial, including role reversal.

## Mathematical limits and provenance

The model is complete allocation of nonnegative additive goods, with zero-valued goods/observers still included and ties allowed. Every observer evaluates all trays on that observer's own scale. Exact cut-and-choose is envy-free and proportional for two people when the cutter makes equal own-value pieces and the chooser selects a weak maximum. The continuous constant-density panels admit such a cut. Envy-free implies proportional by summing all comparisons; the converse holds for two people but fails for three (page 6). Physical approximation does not prove exact equality. Whole-card impossibility does not imply impossibility for divisible cake. The packet does not demonstrate the naive three-person cut-three/choose procedure or teach Selfridge–Conway.

Mathematical model and cut-and-choose precedent: Ariel D. Procaccia, *Cake Cutting Algorithms*, §§13.2–13.3.1, author-hosted PDF pp. 1–4, <https://procaccia.info/wp-content/uploads/2020/03/cakechapter.pdf>. Three-person background: §13.3.3, PDF pp. 5–6. Source inspection and teaching evidence are in `plans/new-themes-52-63/week-58/research.md`; prior-use distinctions are in that folder's `novelty.md`. These references support the mathematics and design choices, not validation of this adaptation.

Student wording, figures, convention examples, recording layouts, material cards and verification code were authored for this project. Established mathematics is not claimed as novel. Root `REPUBLISHING.md` was read. No borrowed workflow exemplar text, prompt files, third-party books, reference PDFs, build intermediates or render images belong in the portable source bundle. Local review evidence stays outside `src/`.

## Unperformed physical checks

Print scale and orientation, 300 mm butt seams/flatness, scissors and 25 mm replacement-half handling, fixed-observer rehearsal with the non-mathematician adult, tray/preference-card table footprint, five-kit setup and resets, staffing, timing and classroom piloting are **unperformed**. Rehearse these before claiming physical readiness. After a brief whole-group handling and divide/choose demonstration, children should control legal attempts and choices. The actual age fit and 35–40 minute route remain unpiloted; finishing all seven pages is not expected. Preserve these limits in the separately authored adult guide.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
