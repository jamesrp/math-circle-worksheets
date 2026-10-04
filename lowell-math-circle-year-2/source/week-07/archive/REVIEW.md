# Week 7 v3 review — September 27, 2026

Status: **prepared, unpiloted**. Week 1 classroom observations informed these revisions; no Week 7 trial or success is inferred. Earlier sources, PDFs, and reviews are preserved in the separate `archive-before-classroom-guidance-2026-09/` folders.

## Pedagogical revision

Added repeated games and legal-option records before W/L; grouped counters before remainders; matched and extended four-label windows before the eventual-periodicity proof; and two-pile play before mex labels and equalizing replies.

Every student page uses the consistent 10/12-point `Week 7 / topic / level` header, numbered `Problem N:` text, required diagrams/records, and a v3 footer. Name/date fields, competing titles, separate rule boxes, hints, proof quotas, “go further,” and generic encouragement have been removed from student pages. Essential rules remain inside numbered problems. The facilitator retains mathematical depth, hints, prerequisites, materials, timing, a common concrete launch after handling materials, optional proof conversations, and a record-after-use prompt.

Default preparation is seven starting sheets for the seven-child roster, with continuation masters ready. Earlier candidate lists, score records, and charts travel with later pages. Complete packet counts are K–1 **3**, grades 2–3 **3**, grades 4–5 **4**, extra **3**, facilitator **5** pages. These stages are not a required session quota.

## Mathematical verification

`python3 plans/verify-week-07.py` passes. Checked single-pile recurrences through 1,000 and independent two-pile outcomes through size 30. Added checks for both winning moves from (1,4), all six equalizing replies from (4,6), actual four-label window extensions, and the explicit printed winning move 24 → 23. Facilitator proofs retain both losing-position obligations, legal small cases, termination, and the distinction between eventual periodicity and repetition from zero.

The numbered student cases and guide answers were manually checked in addition to the finite computations. Root's independent content review identified recording clarity improvements, which were incorporated. Source lessons and exact adaptations remain distinguished in the weekly plan and the Week 1 classroom review.

## Build and visual review

Built all five current PDFs using the existing `build.sh` and pdfLaTeX. Final console logs contain no overfull or underfull box warnings. PDF extraction verifies a numbered problem on every student page, consecutive problem numbering within each packet, current v3 IDs, and no obsolete worksheet labels. No accidental extra pages occurred.

Rendered and visually inspected **all 18 pages**, including the facilitator, in contact sheets under `tmp/pdfs/weeks-05-07-review/` at a 1,250-pixel page rendering size. Detailed inspection included dense guide notes and representative multi-column recording pages. Final inspection checked clipping, overlap, column widths, clue placement, footer clearance, and room to write. Week 7's W1 chart was widened after detailed inspection; the recording convention is explicitly demonstrated in its problem. The few final revised pages were rendered again and inspected. No remaining layout defect was found.

The current revision is ready to print selectively and evaluate with children; static review does not establish classroom effectiveness.

Independent cross-review caught an incorrect 23 → 22 example in the new guide (23 is already losing). Upper Problem 7 now starts at 24 and the guide takes 1 to leave 23. The verifier explicitly checks both statuses and the legal move. The upper page 3 and guide page 5 were rebuilt, rerendered, and visually inspected after correction.
