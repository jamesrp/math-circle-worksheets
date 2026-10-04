# Week 8 return-visit writer notes

Current writer-stage draft: `draft/return-visit.pdf`, five landscape US Letter pages, packet id `F08-RV-draft-v1`. This is one shared companion with three numbered investigations, rather than three copies by band. It is prepared and unpiloted. No physical rehearsal or classroom test has been performed.

## Mathematical destination and limits

1. **Misère Nim:** a move removes a positive number from exactly one pile; taking the final counter ends the game and loses. With all nonempty piles of size one, the next player loses exactly when their number is odd. Otherwise the next player loses exactly when the pile sizes have xor zero. For two piles, the losing nonempty positions are `(1,0)`, `(0,1)`, and `(a,a)` for `a >= 2`; `(1,1)` is winning. When at least two piles exceed one, the usual move to xor zero remains appropriate. At the boundary with exactly one pile exceeding one, reduce that pile to zero or one so that an odd number of single counters remain. The empty position is not a playable continuation after the final removal. The printed task seeks a two-pile rule, with three-pile cases available for deeper boundary work.
2. **Coin row:** squares 1 through 12 are playable; the thick left boundary is the wall, not a square. A coin slides left through empty squares without jumping. No legal move loses. For two coins, losing positions are exactly adjacent pairs, wherever they sit. For three coins at `x1 < x2 < x3`, losing positions have `x1-1 = x3-x2-1`. In general, pair coins from the right, take the empty gaps inside those pairs, include the left-wall gap if a left coin is unpaired, and xor those gaps. This records the invariant; it does not make every legal coin move a pile-removal move. The student pages do not introduce gap or binary notation: acting precedes any optional adult representation.
3. **Two rook boards:** one move changes one coordinate of one token by moving left or down. The next player loses exactly when the four distances from the two bottom-left stars have xor zero. Each component alone loses on its diagonal. Identical winning components cancel, but so do some different winning components. Equal coordinate totals do not decide cancellation. All printed boards are 4 by 4, with distances 0 through 3. The student invention task asks for an additional pair whose two components are each first-player wins and whose sum is a second-player win.

The first coin page offers K–3 concrete entry with adult reading and two counters. The second coin page requires counting positions to 12 and following three coins, and is marked 2–5. Misère play is marked 2–5; the two-board strategy task is marked 4–5. Winning a few experimental plays supports a conjecture; a strategy against every legal reply supplies the explanation. The tables below describe optimal play, rather than promising that experimental games will have those winners.

## Exact printed cases and solutions

`First` means the player about to move can force a win. The indicated first move reaches a second-player-winning position. `Second` means there is no winning first move.

### Problem 1, page 1

| Start | Pile sizes | Winner | One winning first move |
|---|---|---|---|
| 1 | `(1,0)` | Second | — |
| 2 | `(1,1)` | First | Remove either pile, leaving one counter |
| 3 | `(1,2)` | First | Remove the entire two-counter pile |
| 4 | `(2,2)` | Second | — |
| 5 | `(2,3)` | First | Make the three-counter pile size 2 |
| 6 | `(3,3)` | Second | — |
| 7 | `(3,4)` | First | Make the four-counter pile size 3 |
| 8 | `(1,1,1)` | Second | — |
| 9 | `(1,1,2)` | First | Make the two-counter pile size 1 |
| 10 | `(1,2,2)` | First | Remove the one-counter pile |
| 11 | `(1,2,3)` | Second | — |
| 12 | `(2,3,4)` | First | Make the four-counter pile size 1 |

### Problem 2, pages 2–3

| Start | Coin squares | Relevant gaps (left-wall gap, right-pair gap for 3 coins) | Winner | One winning first move |
|---|---|---|---|---|
| 1 | `(1,2)` | `0` | Second | — |
| 2 | `(1,4)` | `2` | First | Slide 4 to 2 |
| 3 | `(4,5)` | `0` | Second | — |
| 4 | `(4,6)` | `1` | First | Slide 6 to 5 |
| 5 | `(7,8)` | `0` | Second | — |
| 6 | `(7,10)` | `2` | First | Slide 10 to 8 |
| 7 | `(1,2,3)` | `(0,0)` | Second | — |
| 8 | `(1,4,6)` | `(0,1)` | First | Slide 6 to 5 |
| 9 | `(2,3,5)` | `(1,1)` | Second | — |
| 10 | `(2,4,7)` | `(1,2)` | First | Slide 7 to 6 |
| 11 | `(3,4,7)` | `(2,2)` | Second | — |
| 12 | `(3,5,9)` | `(2,3)` | First | Slide 9 to 8 |
| 13 | `(4,7,11)` | `(3,3)` | Second | — |
| 14 | `(4,7,12)` | `(3,4)` | First | Slide 12 to 11 |

For two adjacent coins, a move of the left coin creates a gap; move the right coin left by the same distance to restore adjacency. The terminal position is `(1,2)`. For three coins with equal relevant gaps, moving the left or right coin decreases one of those gaps, and moving the middle coin left increases the right-pair gap. Each move breaks equality, and the other player can legally restore it. From unequal gaps, reduce the larger one to the smaller by moving the leftmost or rightmost coin. These arguments establish the two printed rules without binary prerequisites.

The non-task example before first play is `(4,10)`, sliding the coin at 4 through square 3 to square 2, then showing `(2,10)`. The input, path/destination intermediate, and output all use matching labels. It does not reveal the adjacent-pair strategy.

### Problem 3, pages 4–5

Coordinates below are **only for these notes**, measured right/up from the star. Every printed reference start shows its tokens directly on the grids.

| Start | Board A | Board B | Component xor values | Winner | One winning first move |
|---|---|---|---|---|---|
| 1 | `(1,2)` | `(1,2)` | `3,3` | Second | — |
| 2 | `(1,1)` | `(2,2)` | `0,0` | Second | — |
| 3 | `(1,0)` | `(2,3)` | `1,1` | Second | — |
| 4 | `(1,3)` | `(2,2)` | `2,0` | First | Move A down 2 to `(1,1)` |
| 5 | `(0,2)` | `(1,3)` | `2,2` | Second | — |
| 6 | `(0,1)` | `(1,3)` | `1,2` | First | Move B down 3 to `(1,0)` |

One answer to the invention task is A at `(0,3)` and B at `(1,2)`: both component xor values are 3, so neither component is a diagonal loser, and their combined game loses for the next player. Other pairs with matching nonzero component xor values also work.

The non-task shared-board example is A `(2,2)`, B `(1,3)` → A moves left 2 to `(0,2)` while B stays fixed → B moves down 2 to `(1,1)` while A stays fixed. It explicitly shows one board changing per turn and does not duplicate any catalog start.

## Diagram dimensions and use

- Every page is 11 by 8.5 inches (PDF MediaBox 792 by 612 points), landscape, to print at 100 percent actual size.
- Pages 2 and 3 each provide a **blank active strip**: 12 squares, 0.85 by 0.85 inches, total width 10.2 inches, from page x = 0.4 to 10.6 inches. PDF vector measurements find cell lines of 61.201 points and strip edges of 734.415 points, within rounding of 61.2 and 734.4 points. Counters go on this strip; none are preprinted there.
- Coin worked examples and catalog starts are **references**, with 0.23-inch squares and a thick left wall. Each reference is 2.76 inches wide. Movable counters are set on the large blank strip from these starts.
- Page 4 provides two **active 4 by 4 rook boards**, each with 0.85-inch squares, measuring 3.4 by 3.4 inches, with a star in the bottom-left cell. PDF grid lines measure 244.805 points, within rounding of 244.8. Their x origins are 0.85 and 6.2 inches. They are labeled `A: play here` and `B: play here`, and no start tokens are preprinted.
- The rook procedure example uses 0.18-inch reference cells. Page 5 catalog grids use 0.31-inch reference cells. The invented-pair record uses 0.28-inch cells. These are drawings/records, not token-placement boards.
- Page 1 pile mats are 2.9 by 1.4 inches each. Printed circles above them are reference counts. The maximum printed start uses nine counters; the supplied 24 counters per pair suffice.

## Build and checks

Portable sources: `draft/src/return-visit.tex`, `draft/src/build.sh`, and `draft/src/check_math.py`. Run `sh draft/src/build.sh` from the run directory, or run the script from any current directory. It uses two pdfLaTeX passes because the diagrams use remembered page anchors, builds into `draft/build/`, and writes `draft/return-visit.pdf`. It respects `PDFLATEX` and otherwise finds `pdflatex` on PATH or its conventional macOS location. It requires no external diagram assets or third-party Python package for mathematics.

Independent recursive checks passed for all nonempty two- and three-pile Nim states with entries 0 through 6; every two-, three-, and four-coin start on squares 1 through 12; and all 256 positions on two 4 by 4 rook boards. These checks compare actual legal-move recursion with the stated formulas, rather than just recomputing the formulas for selected cases. The exact printed cases are included in the script. `draft/build/math-check.json` records the results.

After the final build, all five pages were rendered with PyMuPDF and inspected individually at approximately 104 dpi. All references match the tables above; active spaces, header bands, stars, move example, number labels, footer, and page numbers were checked. No clipped or overlapping content was seen, and no text spans lie outside the page. The rendered images are in `draft/render/`; measured dimensions and text-bound checks are in `draft/build/layout-check.json`.

This completes only the writer stage. Fresh critique, revision, facilitator guide, source ZIP/rebuild check, release copies, combined sets, indexes, and classroom use remain with the parent workflow. Source context is the supplied outline's finite-game recurrences and pairing invariant; no base worksheet, global index, or adult guide was edited.
