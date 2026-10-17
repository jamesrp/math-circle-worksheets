# Week 97 fresh revision stage

Scope: only the one Grades 3–5 student packet. The six substantive investigations remain; no other bands, guide, or shared workflow files were authored.

## Changes

- R1: Before Problem 1, added the non-task bundle-size-4 collection for inputs 0–3, with a labelled input/output table and a worked reading: output 1 hides inputs 1 and 3; two different outputs occur, 0 and 1. This separates possible-input counts from output counts without giving the mod-5 or mod-7 inventory or prescribing a method. The existing fixed-input diagram remains unchanged: input 3 → 9 counters → 4+4+1 → output 1.
- R2: Shared removal rule now says to continue until fewer than one bundle's worth remain. Stated once, before use.
- Page 4: Changed ambiguous “between 0 and 14” to “one of the whole numbers 0–14,” making the inclusive finite range clear.
- Page 1 workspace reduced from 9 cm to 6 cm high to accommodate the necessary convention example. It remains wide and usable with the separate whiteboard/counter materials. Other working spaces are unchanged.

## Verification

The final PDF has six US Letter pages, Problems 1–6 consecutively, and consistent header/footer strings. Rendered every page at 1.3× with PyMuPDF and visually inspected each image. Page 1: complete nine-counter sequence, labelled collection table, five starting arrays including zero, and blank working rectangle all fit without collision. Page 2: partner task and all seven support facts fit. Page 3: three finite domains and nine support facts fit. Page 4: inclusive range, fifteen support facts, and working rectangle fit. Page 5: universal-input task, nine support facts and working space fit. Page 6: prime-count question and eleven support facts fit. No missing glyphs, clipping, overflows, overlap, or accidental blank pages were found. Equal scaling and counts in all dot arrays were retained.

Ran the independent math reviewer's unmodified checker in a separate `final-math-check/` directory with the final source at its supported `student/students.tex` location. It returned PASS, checked all 51 printed fact-card occurrences, all finite answer inventories, prime criteria through 97, and periodicity identities through 700. Separately checked the new bundle-4 collection: outputs [0,1,0,1], output-1 inputs [1,3], two different outputs. These finite checks do not replace the universal proofs in the independent answer report.

Compiled twice with pdfTeX, SOURCE_DATE_EPOCH=1792195200 and FORCE_SOURCE_DATE=1; no overfull boxes. Copied only students.tex to a clean rebuild directory, compiled twice there, and confirmed identical PDF bytes. Deterministic metadata directives remain in the source.

Final PDF: `final/students.pdf` (129835 bytes), SHA256 `0300f0ba01ce6d27df59ffd80603c6ee876ffe99215dbcd9c9a59b3421f8aa22`.
Editable source: `final/src/students.tex`.
Rendered QA evidence: `final/rendered/page-1.png` through `page-6.png`.
Checker evidence: `final-math-check/results.json`.

No blocker remains for this revision stage. Portable ZIP assembly, final student/guide pair review, and integration remain the coordinator's work. Physical rehearsal and classroom piloting have not occurred.
