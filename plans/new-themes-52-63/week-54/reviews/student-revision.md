# Week 54 revision record

October 4, 2026. Fresh revision stage only; direct combined-packet routing applies. The current revision is `students.pdf` (nine US Letter pages), rebuilt from `src/`. Source files were copied from the draft before editing. No guide, new band variants, workflow restart, older packet edits or remote writes were made.

## Addressed review items

- **R1, page 6 / Problem 6:** added “until all sizes are different” directly to the joining-route task. This makes each route run to termination while preserving the open question about its result and the general all-odd question.
- **Optional typography, page 8 / Problem 8:** kept “total” as a whole word rather than “to- / tal.”
- Updated the source README to identify this revision and its checks. All unordered catalog searches, three contrasting join/split cases, row/column involution work and upper general explanation questions are retained.

## Verification and page coverage

All nine final pages were rendered at 144 dpi with the prescribed Python environment and individually inspected. Pages 1–5 retain Grades 2–5 headers; pages 6–9 retain Grades 4–5 headers. Problems remain consecutive 1–9. No clipping, overlapping text, damaged diagram, unequal square scaling or inconsistent footer was found. There are no polygon, arc or additional grade-band variants. Render evidence is `qa/render/page-01.png` through `page-09.png`.

`src/verify_math.py` passed for all 7,338 partitions of totals 0–24, the complete requested catalogs and the unchanged joining/splitting/conjugation examples. A separate exhaustive size-choice route computation for Problem 6 found all 70 completed routes end at `(12,4,2)`; `qa/p6-route-check.json` records it. The diagram coordinate check matched every final unit square to the actual authored positions within 0.02 PDF points; square counts per page remain `6,0,69,83,0,18,60,0,0`. The finite checks support the examples; they do not replace the general reversible-correspondence arguments.

A newly created clean directory received a byte-identical copy of every current `src/` file and built successfully using its standalone build script without TeX warnings. The rebuild matched every final page's extracted text, 612×792-point dimensions and all rendered pixels at 144 dpi. Only pages 6 and 8 differ from the draft's rendered pixels. Detailed evidence and source/PDF hashes are in `qa/rebuild-checks.json`; the fresh copy named there is current, not an older extraction.

Physical handling, the dense page-4 record, rule retention, age fit and classroom pacing remain untested. The catalog/recording and multiple-visit observations in the adversarial review remain operational hypotheses for the later separate guide and rehearsal; they did not justify removing the accepted mathematical core. No physical rehearsal or classroom piloting was performed.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
