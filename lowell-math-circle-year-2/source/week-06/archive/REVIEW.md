# Week 6 v3 review — September 27, 2026

Status: **prepared, unpiloted**. Week 1 classroom observations informed these revisions; no Week 6 trial or success is inferred. Earlier sources, PDFs, and reviews are preserved in the separate `archive-before-classroom-guidance-2026-09/` folders.

## Pedagogical revision

Separated visible scoring, unrestricted play, single-place comparisons, candidate filtering, tree construction, difficult score groups, and color renaming. Expanded the extra from one compressed proof page into three concrete decoding stages.

Every student page uses the consistent 10/12-point `Week 6 / topic / level` header, numbered `Problem N:` text, required diagrams/records, and a v3 footer. Name/date fields, competing titles, separate rule boxes, hints, proof quotas, “go further,” and generic encouragement have been removed from student pages. Essential rules remain inside numbered problems. The facilitator retains mathematical depth, hints, prerequisites, materials, timing, a common concrete launch after handling materials, optional proof conversations, and a record-after-use prompt.

Default preparation is seven starting sheets for the seven-child roster, with continuation masters ready. Earlier candidate lists, score records, and charts travel with later pages. Complete packet counts are K–1 **3**, grades 2–3 **3**, grades 4–5 **4**, extra **3**, facilitator **6** pages. These stages are not a required session quota.

## Mathematical verification

`python3 plans/verify-week-06.py` passes. Exact adaptive identification costs remain 2,3,4. Exhaustive checks cover all 32 five-bit signatures, every added baseline example, and every coordinatewise color-renaming score for lengths 3 and 4. The facilitator preserves both triple/quartet obstructions and the symmetry argument needed to cover every first query. Four five-bit probes are a sufficiency claim, not a newly asserted optimum.

The numbered student cases and guide answers were manually checked in addition to the finite computations. Root's independent content review identified recording clarity improvements, which were incorporated. Source lessons and exact adaptations remain distinguished in the weekly plan and the Week 1 classroom review.

## Build and visual review

Built all five current PDFs using the existing `build.sh` and pdfLaTeX. Final console logs contain no overfull or underfull box warnings. PDF extraction verifies a numbered problem on every student page, consecutive problem numbering within each packet, current v3 IDs, and no obsolete worksheet labels. No accidental extra pages occurred.

Rendered and visually inspected **all 19 pages**, including the facilitator, in contact sheets under `tmp/pdfs/weeks-05-07-review/` at a 1,250-pixel page rendering size. Detailed inspection included dense guide notes and representative multi-column recording pages. Final inspection checked clipping, overlap, column widths, clue placement, footer clearance, and room to write. The few final revised pages were rendered again and inspected. No remaining layout defect was found.

The current revision is ready to print selectively and evaluate with children; static review does not establish classroom effectiveness.

Final source-freshness rebuild: all five PDFs were rebuilt after the unused legacy macros were removed from `common.tex`. Every page's extracted text and decoded drawing stream matches the frozen, visually reviewed output exactly (37 pages across Weeks 5–6); no visual content changed. Comparison hashes are in `tmp/pdfs/weeks-05-07-review/before-final-rebuild/`.
