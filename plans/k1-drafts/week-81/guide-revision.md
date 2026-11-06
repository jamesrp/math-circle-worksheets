This is the preserved reviser report from [checkpoint 24a18cb0](https://github.com/jamesrp/math-circle-worksheets/blob/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-81-v1/reviser-report.md). Its inline `final/` paths and stage-status statements describe that historical run; live Markdown links below point to this package where applicable. The packaged guide is [k1-guide.pdf](k1-guide.pdf), its portable source is [guide-src/](guide-src/), and packaging checks are in [the packaging report](../../guide-packaging.md). Original writer/critic scripts, rendered-check records and other run evidence remain at [the pinned run](https://github.com/jamesrp/math-circle-worksheets/tree/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-81-v1/). Existing companion-guide changes mentioned below remain **future work after organizer approval**; none is implemented here.

---

# Week 81 K–1 guide: reviser report

Reviser stage completed 2026-11-06. Final: `final/k1-guide.pdf`, **5 US Letter pages**, W81-K-FAC-v2, with portable sources and checker in `final/src/`. The extra page preserves readable 11-point type while adding the child explanations and operational demonstrations. All 6 should-fix and 8 minor findings are addressed; there were no must-fixes and no findings were declined. Draft and review evidence are preserved. This remains an unapproved, unpiloted guide; every activity and kit is physically unrehearsed. Packaging and integration are deferred.

## Finding dispositions

| Review finding | Disposition and location in final guide |
| --- | --- |
| Should 1: child destination/problem map | Addressed, p. 1: explicit Problems 1–12 map, child's copying explanation, and certainty that the all-paired starts are exactly the second-player forced wins. |
| Should 2: ending and recording demo | Addressed, p. 2: non-task one-counter ending, identification of the 1st/2nd record, and refill explicitly from Supply. No Problem 1 start is revealed. |
| Should 3: bucket-3 concrete demo | Addressed, p. 4: later-visit launch physically makes all four endings from non-task (1,0,2), resetting between endings; cooperative goals are explicit. |
| Should 4: two pairs/one adult | Addressed, p. 3: challenger's partner checks, other pair uses Problem 5 or chosen Problem 2 starts; swap after two games. Start with (4,2) in both turn orders; reserve (3,4) for a child explaining the copy. |
| Should 5: integration pointer | Addressed, p. 5: later integration must change both the base guide's p. 2 paragraph and stale p. 1 route sentence; this companion belongs after the existing guide. Existing guide unchanged. |
| Should 6: child reasoning | Addressed, pp. 3, 5: concrete (2,2) copy and (1,1) move-to-(2,0) explanation; child-level sequential emptying argument for Problem 12 before retained adult proof/check. |
| Minor 1: shortest-game proof | Addressed, p. 1: every original counter must be removed and never refilling attains the sum; decreasing weight establishes the longest, attained by every refill. |
| Minor 2: Problem 4 word | Addressed, p. 3: “only winning first move”. |
| Minor 3: notation | Addressed, p. 2: notation precedes solutions; unnecessary arrow sentence removed. The overview separately defines its adult three-variable notation. |
| Minor 4: repetitions | Addressed: Removed/reset reminders consolidated in the launch; common-launch limits reduced to one clause; redundant copy cross-reference removed. |
| Minor 5: demo panels | Addressed, p. 2: wider panel separation, arrow/or, and Supply 3/3/2 alongside Removed 0/1/1. |
| Minor 6: recording demands | Addressed, p. 2: numerals through 12 or dictation; enlarged scrap sketches/dictated dots; children need not know “even”. |
| Minor 7: packets | Addressed, p. 1: one seven-page packet per child; pair shares a board. |
| Minor 8: counter fit | Addressed, p. 1: test 11 counters flat in one 56 × 139 mm bucket; flat counters no wider than about 20 mm preferred. This is a rehearsal requirement, not a tested fit claim. |

## Verification

Read the final seven-page W81-K-v1 student PDF, existing four-page W81-FAC-v2 guide, Week 81 K–1 outline, original/shared board and cards, draft, review, and applicable AGENTS requirements. Student SHA-256 remains `a6a6e52ed4a391ccd6e10f7cd7444c779f612e73be21e58d97ac27d46d264738`; no student or packaged file changed.

`final/src/build.sh` completed successfully with pdfLaTeX 2026: two passes, no errors or overfull boxes. Checker independently enumerates legal descendants (781 states visited), winners, unique winning moves, copying replies, all possible lengths, exhaustive splits, and maximum board counts. It directly parses the actual student's vectors and verifies all 12 numbered problems, page map, 21 rule-diagram buckets and every task's dots. Added checks cover the non-task one-counter ending and (1,1)/(2,2) explanations. Generated answer tables retain the correct numerical answers.

Actual page map checked: Problem 1 → p. 1; 2–3 → p. 2; 4–5 → p. 3; 6–7 → p. 4; 8–9 → p. 5; 10 → p. 6; 11–12 → p. 7. In particular, Problem 1 order is 2,5,3,6,4,7,11,10; Problem 8 reads down the left column then the right; Problem 11 maxima are 6,7,12; Problem 12 begins (2,2,2) and has a 14-move upper bound. Problem 5's three responses and Problems 6–7's complete lists are exhaustively checked.

Measured materials against the actual shared PDF: three 56 × 139 mm buckets, 5 mm gaps, 86 × 40 mm Supply/Removed boxes, sixteen optional 39 × 27.5 mm cards. Guide calls for one packet per child, two shared pair kits for the table, about 30 counters plus reserve per pair, pencil and masks/scrap. The binding one-bucket 11-counter setup is named for physical testing.

Rendered and visually inspected every final guide page and every served student page. Poppler renders are the authoritative final visual check: complete headings/footers, readable text, correct diagram grouping and table placement, no clipping, overlaps or overflow. An installed PyMuPDF rasterizer showed anomalously clipped glyphs on some pages; Poppler and extracted text/vector bounds confirm those are renderer artifacts. Also inspected the existing guide and shared board/cards. No physical print/cut/handling test was performed.

Clean outside-repository rebuild: copied only `final/src/` plus pinned `k-1.pdf` to a fresh `/tmp` directory, ran its relative-path build/checker successfully, and compared `pdftotext -layout` output with the in-repository final using `cmp`: identical. No checkout-specific absolute paths are embedded. Final PDF SHA-256: `764fc5e1b13f354ce1c62eefb775e6d1d1dd7da979f18fbcf464d36cb635469e` (PDF metadata may vary on rebuild).

## Student-page issues and limits

No mathematical student-page error found. The guide works around Problem 6's five available slots by saying they are spare space rather than an answer count; small 16 × 22 mm drawing buckets by allowing larger sketches/dictated dots; numerals up to 12 by adult recording; and older/younger rule differences by keeping the one-each cap explicit and separating the uncapped upper-table game. Small setup pictures are instructions rather than counter mats. Problem 12 requires an ending argument, not counting 14 turns.

Counter fit, writing comfort, cutting/masking, handling, rule enforcement, one-adult workload, pacing and child discovery remain untested. No claimed classroom trial or physical rehearsal. Later packaging must retain both integration pointer changes; it is intentionally not performed here.
