# Week 8 return visits: independent mathematical review

Reviewed `draft/return-visit.pdf` (all five landscape Letter pages) and `draft/src/return-visit.tex`. I read `PROMPT.md` and `CRITIC-MATH.md`, rendered the actual PDF afresh, inspected every page, and checked its vector token centers and counts against independently computed states. I did not use the writer's checker as my verification. This report covers the one shared collection with Problems 1–3 and the actual page headers, rather than the generic three-packet harness.

**Result:** All represented playable starts, worked moves, and the rook invention task are mathematically correct. One small domain clarification is needed in Problem 1. The four-by-four rook boards provide a substantive cancellation investigation and are the coordinator's confirmed deliberate adaptation of the outline's five-by-five materials, not a mathematical failure.

## Located issue

**Grades 2–5, page 1, Problem 1.** Exact text: “Find a rule for all two-pile starts.”

The rules above it say “Whoever takes the final counter loses.” With the two-pile start `(0,0)`, nobody can remove a counter and nobody takes the final counter, so the printed ending rule supplies no winner. It would be incorrect to import the normal-play convention that no move loses: in this game taking the last counter already ends play with the mover losing. The problem's examples are all nonempty and correct; only the unrestricted domain is undefined.

**Smallest fix:** “Find a rule for all two-pile starts with at least one counter.” This needs no new rule or example. The adversarial critic's suggested `(2,0)` contrast is useful evidence for the boundary, but its absence is not an error in the existing positions or a barrier to finding the correct rule: `(2,0)` is a first-player win, whereas printed `(1,0)` is a second-player win. The coordinator reports that the revision will replace Start 7 `(3,4)` with `(2,0)`, add the nonempty-domain wording, and add a rule record. I independently verified that prospective replacement: removing one counter leaves `(1,0)`, so `(2,0)` and the replaced `(3,4)` are both first-player wins. This review still documents the actual pre-revision PDF; the later rendered replacement must be checked in its delivered revision.

## Verified mathematical outcomes

“First” means the player whose turn starts the game can force a win with optimal play; “Second” means that player loses against optimal play. No winner is printed as a supplied answer on the student pages.

### Problem 1: last-counter-loses Nim, page 1, Grades 2–5

The requested outcomes are the winners from the twelve illustrated starts and a rule for nonempty two-pile starts. A move changes exactly one pile to a smaller nonnegative size; a move leaving all piles empty immediately loses.

| Start | Actual piles | Winner |
|---|---|---|
| 1 | `(1,0)` | Second |
| 2 | `(1,1)` | First |
| 3 | `(1,2)` | First |
| 4 | `(2,2)` | Second |
| 5 | `(2,3)` | First |
| 6 | `(3,3)` | Second |
| 7 | `(3,4)` | First |
| 8 | `(1,1,1)` | Second |
| 9 | `(1,1,2)` | First |
| 10 | `(1,2,2)` | First |
| 11 | `(1,2,3)` | Second |
| 12 | `(2,3,4)` | First |

The nonempty two-pile losing starts are exactly `(1,0)`, `(0,1)`, and `(a,a)` for `a >= 2`. If every nonempty pile has one counter, odd numbers of those piles lose and even numbers win. If some pile exceeds one counter, zero xor is the losing condition. At the transition to all-one piles, a winning player leaves an odd number of one-counter piles. This is consistent with all five three-pile starts on the page.

The fresh legal-move recurrence checked **all 168 nonempty ordered two-pile states and all 2,196 nonempty ordered three-pile states with each entry 0–12** against this rule. The recurrence tests a final-counter removal as an immediate losing action, without assigning a normal-play loss to the all-empty position.

All **55 PDF pile dots** were counted by start and by column. Every count agrees with the displayed number, including the genuinely empty second pile in Start 1. The three active pile mats are 2.9 by 1.4 inches; they are collection areas rather than fixed-capacity counter cells.

### Problem 2: no-jump coin slides, pages 2–3

Page 2 has the K–3 entry and asks who can always win from six two-coin starts. Page 3 has Grades 2–5 entry, adds eight three-coin starts, and asks for the second-player rule. Legal targets are numbered squares strictly left of the moving coin and strictly right of the coin immediately to its left; the leftmost coin may move as far as square 1. The wall is not a playable square. No legal move loses.

| Start | Actual occupied squares | Relevant gaps | Winner |
|---|---|---|---|
| 1 | `(1,2)` | `0` | Second |
| 2 | `(1,4)` | `2` | First |
| 3 | `(4,5)` | `0` | Second |
| 4 | `(4,6)` | `1` | First |
| 5 | `(7,8)` | `0` | Second |
| 6 | `(7,10)` | `2` | First |
| 7 | `(1,2,3)` | `(0,0)` | Second |
| 8 | `(1,4,6)` | `(0,1)` | First |
| 9 | `(2,3,5)` | `(1,1)` | Second |
| 10 | `(2,4,7)` | `(1,2)` | First |
| 11 | `(3,4,7)` | `(2,2)` | Second |
| 12 | `(3,5,9)` | `(2,3)` | First |
| 13 | `(4,7,11)` | `(3,3)` | Second |
| 14 | `(4,7,12)` | `(3,4)` | First |

For two coins, the gap is the number of empty squares between them, and a start loses exactly when the coins are adjacent. For three coins `x1 < x2 < x3`, the table records `(x1-1, x3-x2-1)`; the losing condition is equality of those two gaps. A coin move is still a physical no-jump slide: it can increase a relevant gap, so treating every move as ordinary removal from a gap-pile would be false. The direct recurrence used actual coin coordinates and legal destinations.

An independently computed mex recurrence verified that the game value equals xor of the right-paired gaps on **all 66 two-coin, 220 three-coin, and 495 four-coin starts on squares 1–12**. For odd counts the unpaired left coin contributes its distance from square 1. The student pages do not introduce this pairing representation or print the rule as a hint.

The worked visual is correct: input `(4,10)`, a leftward arrow from square 4 to a dashed destination at square 2, and output `(2,10)`. Squares 3 and 2 are empty, so that slide is legal and does not jump the coin at square 10. PDF vector centers confirm all **18 filled circles on page 2** (six in the worked sequence and twelve in the catalog), and all **24 filled circles on page 3**, at their stated squares.

Both active strips have **12 squares, each 0.850 inches wide and high**, and a 10.200-inch total width; there are 13 boundary positions. The left boundary is visibly thicker and labelled wall. All reference rows have 12 squares of 0.230 inches; their numbers, coins and wall agree with the active strip. No square 0 appears as playable space.

### Problem 3: sum of two rook races, pages 4–5, Grades 4–5

The requested outcomes are the winning player for six pairs, then a new pair of different individually winning component starts whose combined game is a second-player win. Distances `(x,y)` are measured rightward and upward from the bottom-left star. Every turn reduces exactly one of the four distances by a positive amount. The mover reaching four zero distances wins; no further move is required.

| Start | Board A `(x,y)` | Board B `(x,y)` | Individual values `x xor y` | Combined value | Winner |
|---|---|---|---|---|---|
| 1 | `(1,2)` | `(1,2)` | `3,3` | `0` | Second |
| 2 | `(1,1)` | `(2,2)` | `0,0` | `0` | Second |
| 3 | `(1,0)` | `(2,3)` | `1,1` | `0` | Second |
| 4 | `(1,3)` | `(2,2)` | `2,0` | `2` | First |
| 5 | `(0,2)` | `(1,3)` | `2,2` | `0` | Second |
| 6 | `(0,1)` | `(1,3)` | `1,2` | `3` | First |

Starts 3 and 5 supply distinct individually winning components that cancel. Start 4 shows that equal total distance is not sufficient: both totals are four but the combined game is winning. Starts 3 and 5 also show equal total distance is not necessary. Two separately losing boards, as in Start 2, combine to a losing game.

The invention is feasible without enlarging the board: A `(0,3)` and B `(1,2)` are an additional pair; each has value 3 and their combined value is 0. On the actual four-by-four board there are **18 unordered pairs of distinct individually winning component starts that cancel**. Four component starts realize each value 0, 1, 2, 3. Each nonzero class therefore supplies `choose(4,2)=6` distinct cancelling pairs. This offers concrete cancellation beyond identical boards and includes distinct coordinate totals. It is a full entry to the intended phenomenon, even though a five-by-five board permits additional values.

The fresh direct mex recurrence verified the four-coordinate xor value on **all 256 positions of two four-by-four boards**. For completeness it also verified **all 625 positions of two five-by-five boards**; the mathematical rule works at either size. The actual draft uses distances 0–3, and every printed token is in range.

The worked sequence is legal and keeps one unchanged board on each turn: A `(2,2)` / B `(1,3)` → A `(0,2)` / B `(1,3)` after A moves left two; then A `(0,2)` / B `(1,1)` after B moves down two. The three diagrams genuinely show input, an intermediate state, and output, with the same star orientation. All **six procedure tokens on page 4** and **twelve catalog tokens on page 5** match those coordinates in the actual PDF.

Every rook diagram has **four squares per side** and its star at the center of the bottom-left square. Both active boards have **0.850-inch square cells and a 3.400-inch side**. Procedure grids have 0.180-inch cells, catalog grids 0.310-inch cells, and the blank invented-pair grids 0.280-inch cells. All share the same coordinate orientation, square count, and bottom-left destination. The catalogue transfers to the active boards without conversion or a changed boundary. These dimensions are digitally verified; physical printing/counter-fit rehearsal remains untested.

## Coverage and limits

All actual student pages were inspected: page 1 Grades 2–5, page 2 K–3, page 3 Grades 2–5, and pages 4–5 Grades 4–5. Problems 2 and 3 and every represented game instance check out completely. Problem 1 checks out for its represented nonempty states, with the empty-start wording correction above. There are no separate band variants hidden behind this one-PDF scope.

The coordinator has confirmed keeping four-by-four rook boards as a deliberate adaptation of the outline. Restoring five-by-five boards is not required for mathematical correctness, cancellation variety, or invention feasibility. All moves from a represented start decrease a coordinate, so unused larger outer cells add no reachable moves; the complete actual domain is distances 0–3. This stage did not edit sources, rebuild packages, create a facilitator guide, alter base materials/indexes, or perform physical/classroom testing.
