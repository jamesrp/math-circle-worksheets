# Week 5 v3 review — September 27, 2026

Status: **prepared, unpiloted**. Week 1 classroom observations informed these revisions; no Week 5 trial or success is inferred. Earlier sources, PDFs, and reviews are preserved in the separate `archive-before-classroom-guidance-2026-09/` folders.

## Pedagogical revision

Rebuilt student work around contrasting skyline viewpoints, physical city changes, row candidate lists before case tables, explicit deletion checks, and four executed switches before entry-clue bounds.

Every student page uses the consistent 10/12-point `Week 5 / topic / level` header, numbered `Problem N:` text, required diagrams/records, and a v3 footer. Name/date fields, competing titles, separate rule boxes, hints, proof quotas, “go further,” and generic encouragement have been removed from student pages. Essential rules remain inside numbered problems. The facilitator retains mathematical depth, hints, prerequisites, materials, timing, a common concrete launch after handling materials, optional proof conversations, and a record-after-use prompt.

Default preparation is seven starting sheets for the seven-child roster, with continuation masters ready. Earlier candidate lists, score records, and charts travel with later pages. Complete packet counts are K–1 **3**, grades 2–3 **3**, grades 4–5 **5**, extra **2**, facilitator **5** pages. These stages are not a required session quota.

## Mathematical verification

`python3 plans/verify-week-05.py` passes. Enumerated all 12 Latin squares of order 3 and 576 of order 4. Checked middle uniqueness/optimality; upper five-clue uniqueness, all deletion witnesses and counts, the target-specific three-clue minimum, all block switches, and the concrete four-entry alternative. New deleted-clue views are 3,3,3,3,4. The facilitator preserves the small complete case proof and distinguishes visibility from entry clues.

The numbered student cases and guide answers were manually checked in addition to the finite computations. Root's independent content review identified recording clarity improvements, which were incorporated. Source lessons and exact adaptations remain distinguished in the weekly plan and the Week 1 classroom review.

## Build and visual review

Built all five current PDFs using the existing `build.sh` and pdfLaTeX. Final console logs contain no overfull or underfull box warnings. PDF extraction verifies a numbered problem on every student page, consecutive problem numbering within each packet, current v3 IDs, and no obsolete worksheet labels. No accidental extra pages occurred.

Rendered and visually inspected **all 18 pages**, including the facilitator, in contact sheets under `tmp/pdfs/weeks-05-07-review/` at a 1,250-pixel page rendering size. Detailed inspection included dense guide notes and representative multi-column recording pages. Final inspection checked clipping, overlap, column widths, clue placement, footer clearance, and room to write. The few final revised pages were rendered again and inspected. No remaining layout defect was found.

The current revision is ready to print selectively and evaluate with children; static review does not establish classroom effectiveness.

Final source-freshness rebuild: all five PDFs were rebuilt after the unused legacy macros were removed from `common.tex`. Every page's extracted text and decoded drawing stream matches the frozen, visually reviewed output exactly (37 pages across Weeks 5–6); no visual content changed. Comparison hashes are in `tmp/pdfs/weeks-05-07-review/before-final-rebuild/`.
