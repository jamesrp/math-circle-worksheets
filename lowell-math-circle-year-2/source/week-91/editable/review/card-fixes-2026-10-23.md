# Week 91 review-card fixes, October 23, 2026

From [plans/review/week-91.md](../../../../../plans/review/week-91.md) (verdict keep, no must). Made in the problem files after the conversion, then in the return-visit and materials generator and the guide.

## Changed

| Card item | Where | Change |
|---|---|---|
| should 1 | guide pp. 1–3 | A K–1 route with adult reading on the one-switch board and the four-exit tree: Problem 1 with "Can X come twice in a row?", "Send four counters. Does every exit get one?", "Make the first counter land on D", and a plain-words key. That K–1 sustains it is a prediction. |
| should 2 | student pp. 1–3; guide p. 2; band views | Pages 1–3 are headed Grades 2–5, since both older tables start there. The print list and the routes now agree: an upper trio that finishes P1–3 early continues to P4 in the same visit, otherwise P4–6 make the next visit. The band-view index is updated: the Grades 4–5 slice is now the whole packet, so it is no longer printed separately. |
| should 3 | student p. 4, P4 | Each target word sits 10 mm lower, level with its own tree's root (centres within 0.2 mm), 12 mm below the tree above. |
| should 4 | student p. 5, P5; guide p. 4 | P5 is now "How many different arrival orders can the eight-exit tree make? Explain why." The guide's key: 128, one per start, because the first counter through each switch shows its starting side. |
| should 5 | guide p. 3, P3 | DABC fails "for the same root reason, one step later": counters 2 and 3, A and B, are both left. |
| should 6 | guide p. 5, return P4 | "both 0040" (was 0004), and the first-block rule: a block of m launches leaves R…RL…L, so the cards can change only during the first block, exactly when the start has L before R. The return packet's page needed no change. |
| could 9 | all four PDFs | Footers F91-S-v1, F91-RV-v1, F91-M-v1, matching F91-FAC-v1. |
| could 10 | guide pp. 1–2 | Production notes cut ("no multi-level coverage is implied", the apparatus-set and sleeving sentences). |
| could 11 | guide p. 4, P4 | AECGBFDH named as the bit-reversal order. |

Deferred: could 7 (a second, extra-workspace board for P2), since page 2 has no room without shrinking both boards; the arrival strips on materials p. 7 serve. Could 8 (a measured preparation time and a counter source) needs a physical rehearsal. No problem moved page, so the guide's page references stand. Student pages 1–3 and 6 differ from the conversion's build only in the header or footer, and the return-visit and materials pages only in the footer (body pixels identical when both are built here).

## Checks

- `verify_card_fixes_2026_10_23.py`: by simulation, the K–1 key, the D-first starts, the Problem 3 key and its root reason, 128 different orders from 128 starts, the bit-reversal order, the return Problem 4 trace (0040 0040; LLR, RLL, RLL), the first-block rule on every road up to m = 10, and the block-size claim on the printed roads; from the PDFs, the headers, footers, Problem 4 label positions, the new Problem 5, the guide's changed sentences, and the unchanged pages. 0 failures.
- `check_math.py` (run by the build) passes; its Problem 5 line now states the 128 count.
- `problem-files/compare.py`: the problem-file packet matches the new print PDF (text identical, 0 differing pixels).
- Every changed page was rendered at 80 dpi and inspected.

Unpiloted; printing, cutting, flipping, counter placement and timing remain physically unrehearsed.
