# Week 80 revision stage

Fresh REVISE stage only. Read the writer prompt, explicit selected-band override, adversarial review, independent mathematical review and original student source. The root facilitator source was not edited.

## Student and source changes

- Problem 1 now requires four physical halfway marks. On the supplied 180 mm working strip, the fourth remaining gap is 11.25 mm. The shared rule still continues before midnight, and the last-switch question remains open.
- Problem 2 now distinguishes whether the card settles on one side from where the counter approaches. This removes the spatial metaphor that could make the card seem to move toward MIDNIGHT.
- Revised-source README records the four-mark physical prefix, back-to-back assembly of the equal ON/OFF panels, the two strips' distinct roles, the counter-centre convention and the readiness split. Adult preparation was not added to student cutout pages.
- Problems 3–5, the fold demonstration and the large reusable strips/cards retain their mathematical content and geometry. No endpoint answer or convention is supplied as a deduction.

## Verification

`students.pdf` has five pages: core pages 1–2, Grades 4–5 pages 3–4, shared materials page 5. Every page was rendered with a newly opened PyMuPDF document and also with Ghostscript at 115 dpi, then visually inspected. No clipping, overlap or unintended layout change was found. Page 1 has the three-panel input/fold/unfold demonstration before the unfamiliar action; the cards and strips remain legible.

The image presentation layer suppressed some repeated header glyphs at matching coordinates. This was checked against actual Ghostscript PNGs: header pixels on pages 1/2/5 are identical, and pages 3/4 are identical. An offset crop of page 2 displays the complete header. PDF text extraction confirms every header/footer. No source change was made for a presentation artifact.

Two independent clean builds from separate copies of final/src produced byte-identical PDFs, also identical to the delivered PDF. The builder rejects overfull boxes. `verify_revision.py` and `QA.json` corroborate 128 exact recurrence steps, alternating card states, four physical gap sizes, free ON/OFF endpoint extensions, actual 180 mm board geometry, band labels, page numbering and all text staying within the page. Infinite claims rely on the mathematical review's induction/subsequence/endpoint-extension arguments, not the finite computation.

Final PDF SHA-256: `7325b65a4c41972749bf5124493da6a715c2b4442fb87b88a231a3f06d401e8a`.

## Root guide coordination still required

The critic's adult-guide requirements remain for the root to integrate: choose four physical marks consistently; cut and glue the equal ON/OFF panels back-to-back; place the event-time and counter-position strips side by side; keep the card fixed and use the counter's centre; stop placement before its size obscures the gap; supply a real SOURCES.md or repair that pointer. No guide was silently certified by this student-stage revision.

Digital checks do not establish physical folding accuracy, fit, timing or classroom readiness. The activity remains an unpiloted draft and physical rehearsal is untested.
