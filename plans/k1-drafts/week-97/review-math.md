# Week 97 K–1 (W97-K-v1): mathematical review

Reviewed: `draft/k-1.pdf` (9 pages; identical to `draft/src/k-1.pdf`) and `draft/src/k-1.tex`. Checks were independent of the author's `check.py` and comments. I wrote my own scripts that (a) parse every TikZ picture in `k-1.tex` and count tiles, rows, columns, ring colours, group-card cells and card dots from the coordinates, and (b) compute leftovers by repeated take-away. I also measured page 1 at 10 px/mm: the printed board is 156 mm wide, which is actual size with 26 mm cells.

## Verdict

The K–1 band is mathematically correct. Every leftover the pages lead to is right, every diagram matches its text, and every group card has the right number of 26 mm cells. One minor diagram issue is listed below. It does not change any answer.

## Per-problem verification

| Page / problem | What it asks | Intended answer | Independent check | Diagram check |
|---|---|---|---|---|
| p. 1, shared rules | Build on the board, remove groups with the card, leftover is what remains | Worked example 3×3 in groups of 4 leaves 1 | 9 − 4 − 4 = 1 | Board: 6×6, 26 mm cells, nested outlines for sides 1–5 plus frame for 6, anchored top-left, labels 1–6 on both edges. Shading = cells with max(i, j) odd, so the L-bands of sides 1, 3, 5 are shaded. Correct. Strip: 9 tiles, then 5 tiles + 4 on a 2×2 card, then 1 tile with box "1". See finding 1 |
| p. 2, Problem 1 | Squares of side 1–6, groups of 3: can a square leave 2? | Leftovers 1, 1, 0, 1, 1, 0, so no | Matches. Leftovers for all sides 0–499: {0, 1} only | Squares 1×1 … 6×6 have 1, 4, 9, 16, 25, 36 tiles. Card has 3 cells of 26 mm |
| p. 3, Problem 2 | Same, groups of 4: can a square leave 2 or 3? | 1, 0, 1, 0, 1, 0, so no | Matches. All sides 0–499: {0, 1}. The grey "1" pre-filled for side 3 is correct | Squares correct. Card is 2×2, 26 mm |
| p. 4, Problem 3 | Rectangles 3×2, 5×2, 4×3, 5×3, groups of 4: can a rectangle leave 2 or 3? | Yes: 6 → 2, 10 → 2, 12 → 0, 15 → 3 | Matches | Tile blocks are 3×2 (6), 5×2 (10), 4×3 (12), 5×3 (15). Width label below, height label at left, all correct. Card is 2×2 |
| p. 5, Problem 4 | Squares 1–6, groups of 6: circle every leftover a square can make (numerals 0–5) | Leftovers 1, 4, 3, 4, 1, 0, so circle 0, 1, 3, 4 | Matches. All sides 0–499 give {0, 1, 3, 4}. Sides 1–6 cover a full repeat, so the six squares settle the general claim | Squares correct. Numerals 0–5 complete. Card is 2×3 = 6 cells |
| p. 6, Problem 5 | Secret square from cards 1–6, groups of 6, circle every card that could give the shown leftover | 1 → {1, 5}, 4 → {2, 4}, 3 → {3}, 0 → {6}. Leftovers 2 and 5 never occur | Matches | The six mini cards show 1, 4, 9, 16, 25, 36 dots in n×n grids. Six record rows, each with a leftover box and cards 1–6. Card is 2×3. P4's completed record answers P5 by reading it backwards. That is the intended inverse reading, not a defect |
| p. 7, Problem 6 | 9×9 and 10×10 without building, groups of 4, explain | 81 → 1, 100 → 0 | Matches (a 64-tile kit cannot build either square, so "without building" is forced honestly) | Blocks are 9×9 = 81 and 10×10 = 100 tiles, labelled 9 and 10 |
| p. 8, Problem 7 | Sides 1, 3, 5 built ring by ring, groups of 8 | 1, 1, 1 | 1, 9, 25 each leave 1. Rings are 8 and 16 | Ring colouring parsed by Chebyshev distance from the centre. Centre is colour A (1). Ring 1 is B (8). Ring 2 is A (16). Card is 2×4 = 8 cells of 26 mm |
| p. 8, Problem 8 | 7×7 in groups of 8, explain | 1 | 49 = 6·8 + 1. Rings 8, 16, 24 | 7×7 = 49 tiles. Rings: centre A 1, B 8, A 16, B 24. Correct |
| p. 9, cut-out cards | Side cards 1–6 | n with an n×n dot picture | Dots counted: 1, 4, 9, 16, 25, 36 in n×n grids | 3×2 grid of 58×74 mm cards with dashed cut lines. Fits inside the margins |

I checked these edge cases, and none is a defect:
- A square with fewer pieces than the group size (side 1 in groups of 3, 6 or 8; side 2 in groups of 6) is handled by the rule "When the card cannot be filled … the leftover".
- Tiles are moved one at a time into the card's cells, so the 1×3 card on p. 2 does not impose straight-strip removal.
- The page 1 example shows a non-straight choice of four tiles (the top row plus one more) going onto a 2×2 card. That models free selection.
- Every secret-square question names its allowed cards.
- No "find all" task has a count different from what the page implies.

## Located problems

### 1. The launch strip shows one take-away but ends at the state after two (minor, diagram)

- **Band / page / problem:** K–1, p. 1, the shared-rules worked strip above the board.
- **Diagram:** filled 3×3 → square with 5 tiles left, plus a full 2×2 card → cup → square with 1 tile left and a box reading "1".
- **Evidence:** 9 − 4 = 5, and five tiles can still fill the card. Getting from the 5-tile panel to the 1-tile panel needs a second card-fill, and the strip never draws it. The text ("When the card cannot be filled, the tiles still in the square are the leftover") implies repeating, so the rule as written is right. But a non-reader looking at the strip, or a parent skimming it, can read the procedure as "take away one group, and what is left is the leftover". With that reading, Problem 1's 6×6 in groups of 3 would give 33 instead of 0.
- **Smallest fix:** make the strip show two groups. Either add one frame between the cup and the last panel (the square with 1 tile, beside a full 2×2 card), or draw the cup holding two stacked groups of 4 (8 tiles). Do not add any text.

No other mathematical or diagram problems were found in the K–1 band.
