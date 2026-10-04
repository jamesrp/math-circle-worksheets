# Week 63 revised student source: cards away from home

Fresh revision-stage source, October 4, 2026, packet IDs W63-S-v2 and W63-M-v2. This folder contains original editable student/material sources and a portable builder. It contains no guide, workflow prompts, borrowed writing exemplars, book PDFs, or rendered intermediates. The independent critic and mathematical reviews preceded revision; final digital revision checks are recorded alongside the delivered PDFs in revision.md and in the run's revision-evidence/ folder. The adult-guide stage has not been performed. This is an unpiloted local revision for review, with no remote publication or upload claimed.

Build with a system Python 3 and TeX Live containing `pdflatex`, `geometry`, `helvet`, `fontenc`, `tikz` (arrows.meta and calc), `fancyhdr`, `array` and `amsmath`:

```sh
python3 build.py --out /absolute/path/to/build-output
```

Run from any directory. The output directory must be outside this source directory. It receives `students.pdf` (9 pages), `materials.pdf` (3 pages) and build intermediates. The first is the one combined packet requested by the direct stage-routing instruction. The builder does not depend on another repository file. `verify.py --pdf-dir <build-output> --out <evidence.json>` uses PyMuPDF for independent mathematical and actual-PDF checks. The project runtime `tmp/bonus-35-51-venv/bin/python` has that optional dependency.

## Band and prerequisite decisions

Pages 1-2 are an adult-supported Grades 2-5 entry: identify A-C labels, keep three fixed homes, place every card once, count to six, and recognize a complete outcome in two groups. Adults may read and record; children retain the placement, comparison and grouping choices. Page 1's two three-card home-free rows are reused entry mathematics: Week 43 upper p. 3, Problem 5 already obtains BCA/CAB from a particular swap procedure. This page does not claim a new three-card collection. A home-match condition applies to the final unchanged row, rather than the sequence of swaps.

Pages 3-5 are Grades 3-5 with support: retain four labels, compare full rows, organize a finite catalog, and understand overlaps. Arithmetic uses totals up to 24, repeated subtraction/addition and counts of chosen home-groups; an adult may write those counts. Page 5 is readiness dependent. Cards in overlaps may have additional home matches; the fixed home strip is never sequentially updated.

Pages 6-9 are Grades 4-5 continuations: reason about a chosen subset of fixed homes, transfer a row to a card-to-home arrow map, reverse a construction, and justify disjoint exhaustive cases. Arithmetic reaches 120; factorial notation is unnecessary. A general counting rule on page 9 is a further readiness-dependent explanation, not a prerequisite for physical placement. That task asks for the two-family rule for two or more distinct cards. The adult mathematical domain is n>=2, with exceptional starting counts D0=1 (the unique empty row) and D1=0. These pages support multiple visits. There is no forced K-1 packet. A younger child may try physical placements with an adult if the child retains the whole-row rule.

## Materials and physical limits

Materials page 1 provides two A-E decks and two fixed five-home strips per print: cards are 30 by 40 mm; home cells are 35 by 45 mm, with the home letter in the upper 5 mm. Place cards against the lower cell edge to leave the home letters visible. Cover D/E or E when using A-C or A-D; retain all remaining labels without renaming or moving them. Page 2 provides all six A-C outcomes, five movable home-group labels, and 12 blank A-E outcome cards. Page 3 provides all 24 A-D outcomes. Outcome cards are 56 by 27 mm and show fixed home labels, the complete row, and its persistent row ID.

Print at 100% on US Letter. Each working pair uses one page-1 print. A table doing two-home overlaps uses one six-outcome deck, one 24-outcome deck, and two open grouping rings (paper, cord or tape) large enough for these outcome cards. For more than two groups, put the group labels on the table and allow one outcome to belong to several groups; the labels do not prescribe an impossible four/five-circle planar picture. Use open rings or markers; one shared outcome is one object, not two different rows. Do not use closed opaque containers that hide overlapping membership. Five-card catalogs can be divided by E's chosen home; each branch contains 11 outcomes. Page 9 has 16 blank rows, and page-2 material copies provide 12 movable blank records per branch. No child needs to transcribe the 120-row universe or all 44 valid rows. Pool one recoverable row collection and derive its count afterward.

Page 2 demonstrates one complete VUWX outcome, checks W-home and X-home on that unchanged row, and records both memberships under the same row ID. Its 56 by 27 mm whole-outcome frame matches the material-card format; the two property boxes are markers of that one object, not separate outcomes. The working boxes on student pages 2, 4 and 5 are for records or drawings. Sort the outcome cards on a separate tabletop: in particular, 24 cards at 56 by 27 mm require more area than the page-4/page-5 boxes.

Keep the E-at-A branch from page 8 when pooling the page-9 catalog. The three upper children or rotating roles can cover E-at-B/C/D, contributing branches to one shared collection. This is a preparation suggestion pending rehearsal, not a classroom observation.

No physical cutting, exact-fit rehearsal, property-marker/grouping-ring handling, reversal-procedure rehearsal or classroom piloting has been performed. Dimensions and geometry have only been checked digitally. Kit-copy quantities and readiness decisions require the subsequent adult-guide stage.

## Established mathematics and original adaptation

Primary mathematical precedents are Alan Frieze, CMU Discrete Mathematics D14, **Derangements, pp. 2-4**, <https://www.math.cmu.edu/~af1p/Teaching/DM/D14.pdf>, and D16, **Inclusion-Exclusion, pp. 1-2 and 4-7**, <https://www.math.cmu.edu/~af1p/Teaching/DM/D16.pdf>. The research stage's exact local trail is `plans/new-themes-52-63/week-63/source-notes.md`; it visually inspected those pages. Their mathematics supplies fixed points, alternating intersection correction, and the reciprocal-pair/longer-loop recurrence. Source attribution does not validate our classroom adaptation.

Pedagogical source observations, consulted in the supplied research notes: *Math Circle by the Bay*, Preface printed pp. viii-x (PDF pp. 9-11), supports manipulatives and readiness-dependent independent work; Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 3 “At the lesson,” item 1, describes attempts before a table, and Lesson 8 “At the lesson,” item 2, reports reducing copying/coloring when pace differs. Local organizer Handouts 2, 6 and 8 supply relevant fixed-seat, counting and recurrence precedents. The outcome-card grouping, non-task convention visuals, wording and diagram design here are original author adaptations. Their exact source-derived facts and local adaptations are distinguished in the research notes.

The new mathematical substance is the four/five-card catalogs, counting rows that avoid only specified homes, correcting overlapping home-match groups, and reversible distinguished-card constructions. Students are asked to repair incorrect subtract-only counts rather than being given the full inclusion-exclusion formula.

## Verification contract

`verify.py` uses independent backtracking (not `itertools.permutations` or a builder-generated answer table), checks the exact small catalogs, all fixed-home intersections, multiplicity cancellation, and both directions of the construction bijections. It reads outcome rows from the actual rendered PDF's text positions, checks actual card/home/outcome rectangle sizes and icon geometry, page headers, problem sequence, and letter-page dimensions. Rendering and a human inspection of every page are separate checks, reported outside this source folder. Clean copied and ZIP-extracted rebuilds must reproduce extracted text, page dimensions and rendered pixels. PDF byte equality is additional evidence when obtained, not a substitute for these checks.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
