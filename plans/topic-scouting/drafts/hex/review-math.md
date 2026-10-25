# Hex week, draft packets: mathematical review

Reviewer: independent math check (CRITIC-MATH stage). The draft was not edited.

Everything below was recomputed with code written for this review. None of it comes from the author's `check_*.py`, `hexsolve.py` or the comments in the sources. Coordinates are (row, column) with row 0 at the top. Each row is shifted half a hexagon to the right, so (0,0) and (n−1,n−1) are the sharp corners. Red joins row 0 to row n−1, Blue joins column 0 to column n−1. I recovered each drawn board from the generated `.tex`: its size, hexagon width, counters, stars and fills. I also checked every counter and fill position by eye against renders of the PDFs.

## Located problems

### 1. K–1, pages 2 and 4, Problems 2, 3 and 5: the page tells the children to do something impossible

Quoted text:
- P2 (3×3): "Put a red or a blue counter on every hexagon so that nobody wins."
- P3 (3×3): "Put a red or a blue counter on every hexagon so that Red and Blue both win."
- P5 (4×4): "Put a red or a blue counter on every hexagon so that nobody wins."

Evidence: I checked every full board exhaustively in C:

| Board | Full boards | Neither wins | Both win | Red only | Blue only |
|---|---|---|---|---|---|
| 3×3 | 512 | 0 | 0 | 256 | 256 |
| 4×4 | 65,536 | 0 | 0 | 32,768 | 32,768 |

None of the three tasks can be done. The intended outcome, from the outline, is to try hard and find that it never works. Each problem is worded as an instruction that assumes success, so the one expected result contradicts the instruction. The 2–3 and 4–5 packets ask the same thing neutrally ("Can you put…?").

Smallest fix: turn each into a question, matching the older bands:
- P2: "Can you put a red or a blue counter on every hexagon so that nobody wins?"
- P3: "Can you put a red or a blue counter on every hexagon so that Red and Blue both win?"
- P5: "Can you put a red or a blue counter on every hexagon so that nobody wins?"

A "Try to put…" opening would also work.

### 2. Grades 2–3, page 4, Problem 4: an obvious first try already answers it

Quoted text: "Put blue counters on this board so that Red cannot win, even when every other hexagon is red. Use as few blue counters as you can." (5×5 board)

Evidence: the least number of blue counters is 5. My search found no blocking set of 4 or fewer, and 48 sets of size 5. One full row of 5 blue counters is one of them, and it is the first thing most children will try. The reason 5 is the least is short: a blue chain from left to right must have a hexagon in each of the 5 columns. That reason is the mathematical content, but the page never asks for it, so the problem can end in under a minute. The answer itself is not wrong.

Smallest fix: add one sentence: "Explain why fewer blue counters will not work." K–1 Problem 7 has the same structure (answers 3 and 4). Without the explanation it is still a reasonable task at that level, so I would leave K–1 as it is.

### 3. Grades 4–5, page 4, Problem 5: the stopping point can be misread when the path reaches a coloured edge partway

Quoted text: "…draw a path along the sides of the hexagons, always with red on one side of the path and blue on the other. The coloured edges count as red and blue. Where does the path end?"

Evidence: I traced both printed boards with my own walk:
- Board 1 (rows BRBBR / BRRRB / RBBRB / BRRBR / BRBRB) takes 23 sides and ends at the bottom-left corner. Red has a chain and Blue does not.
- Board 2 (RRBRB / BRRBR / RBRBB / BBRBR / RBBRB) takes 26 sides and ends at the top-right corner. Blue has a chain and Red does not.

On both boards, sides 7 and 8 of the path run along the left blue edge, beside the red hexagon (2,0). The path then turns back into the board. A child can reasonably stop there and answer "at the blue edge", because nothing on the page says the path goes on until it cannot. The rule as written does imply that it continues, so a careful reader gets it right.

Smallest fix: change the last sentence to "Follow the path as far as it goes. Where does it end?"

The rest of this problem is correct:
- Starting from the star, the path is always uniquely determined.
- Starting from that corner, it ends at the top-right corner exactly when Blue has a chain and at the bottom-left corner exactly when Red has one. It never ends at the bottom-right corner. I checked all 2×2, 3×3 and 4×4 full boards.
- Both drawn boards match their data.

### 4. Grades 4–5, page 6, Problem 8: a reading under real-world Hex rules makes Maya right

Quoted text: "Hex players often use a board with 11 rows of 11 hexagons. Nobody knows a sure way to win on it. Maya says she has a way to always win on this board when she goes second. Explain why Maya must be wrong."

Evidence: under the packet's rules, strategy stealing shows that the second player has no winning strategy, so the problem is correct. The opening sentence, though, points to how Hex players actually play, and on 11×11 they almost always use the swap (pie) rule. Under the swap rule the second player does have a winning strategy, even though nobody knows it. A child who knows the real game could argue that Maya might be right. This is unlikely at this table, but it is a reading that changes the answer.

Smallest fix: "…a way to always win on this board when she goes second, playing by the rules on page 1."

"Nobody knows a sure way to win on it" is accurate as far as I know: 11×11 Hex has not been solved.

### 5. Grades 4–5, page 7, Problem 9: the 7×7 hexagons are smaller than the other play boards (physical fit, untested)

Diagram: the 7×7 board is drawn with hexagons 22.0 mm across the flats (25.4 mm corner to corner). Every other play board in the three packets uses 24.0 mm. The materials call for hexagons "about 25 mm across (a counter fits inside)". This is not a mathematical error, but a counter bought for 24–25 mm hexagons may not sit inside a 22 mm one.

Smallest fix: first, check the real counters on a 100% print of page 7. If they do not fit, the board needs 24 mm hexagons. With the coloured edges cut from 7 mm to about 5–6 mm, that board measures about 254 × 162–164 mm. That only just fits the landscape layout: the current box is 254 mm wide, and about 160 mm is free below the title. So the layout would need tightening, for example by reducing the space above the board.

## Bands that check out completely (apart from the items above)

- **K–1.** Problems 1, 4, 6 and 7 are correct, and so are the shared rules and the example board. Once item 1 is fixed, nothing mathematical is left.
- **Grades 2–3.** Problems 1, 2, 3, 5 and 6 are correct. The only item is 2, which is about substance and is optional.
- **Grades 4–5.** Problems 1, 2, 3, 4, 6 and 7 are correct. Items 3, 4 and 5 are small wording and size points.

## Verification record (what each problem asks and the checked answer)

Shared rules example (all bands, 6×6, a size no task uses):
- Red has 7 counters: (0,2) (1,2) (2,1) (3,1) (3,2) (4,2) (5,1). Each touches the next across a side, from the top row to the bottom row, so Red has won.
- Blue has 6 counters and no chain. That is consistent with Red moving first and winning on Red's 7th move.

### K–1
- **P1 (3×3) and P4 (4×4), play.** Both boards are correct, with 24 mm hexagons.
- **P2, P3 and P5, fill.** All three are impossible: see item 1 and the table there.
- **P6, Red's first counter on the star.** The stars are at (1,1), the centre, and (0,0), the sharp corner. I solved both positions exactly.
  - Centre: Blue cannot stop Red, so the answer is no.
  - Sharp corner: Blue can stop Red, so the answer is yes. Blue's only winning reply is the centre (1,1).
- **P7, fewest blue counters.** The least is 3 on the 3×3 board (8 different sets of 3 work) and 4 on the 4×4 board (20 sets of 4 work).

### Grades 2–3
- **P1, 5×5 play.** Correct.
- **P2 (4×4), nobody wins or both win?** No and no. I checked all 65,536 full boards.
- **P3, 4×4 squares with side-touching chains, nobody wins.** This is possible: 21,150 of the 65,536 fillings have no winner, and a checkerboard is one. On the hexagon board it is impossible, so the contrast holds.
- **P4 (5×5), fewest blue counters.** The least is 5. See item 2.
- **P5, four 4×4 positions with Blue to move.** Each position has one more red counter than blue, nobody has a chain yet, and each drawn position matches its source data.

  | Game | Red | Blue | Can Blue stop Red? |
  |---|---|---|---|
  | 1 | (0,1) (1,1) (2,1) | (3,0) (0,3) | Yes, only at (3,1) |
  | 2 | (0,2) (1,1) (3,0) | (1,2) (2,2) | No |
  | 3 | (1,1) (2,2) | (0,0) | No |
  | 4 | (0,0) (1,1) (2,2) | (2,3) (3,2) | Yes, only at (2,1) |

  In games 1 and 4 the winning move is unique, so "mark the hexagon" is well posed.
- **P6, 3×3 openings that win for Red.** There are exactly five: (0,2), (1,0), (1,1), (1,2) and (2,0). The four losing openings are the two sharp corners (0,0) and (2,2), plus (0,1) and (2,1). This matches the outline's "5 of 9", and the small recording board has the same orientation as the large one.

### Grades 4–5
- **P1, 5×5 play.** Correct.
- **P2 (5×5), nobody wins or both win?** No and no. I checked all 33,554,432 full 5×5 boards in C: none has no winner and none has two, and each player wins on exactly 16,777,216.
- **P3, the square board.**
  - With side-touching chains, nobody winning is possible (21,150 fillings).
  - When corner-touching squares also count as touching, both winning is possible (21,150 fillings; a checkerboard works).
  - Both tasks can be done, and they show the square board failing "exactly one winner" in two different ways.
- **P4 and P6, explain.** Both statements are true for every n×n Hex board, whether full or partly filled for P4, and full for P6. P5's boundary path is the standard argument for P6.
- **P5, boundary path.** See item 3.
- **P7, 3×3 openings.** Same as grades 2–3 P6: five winning openings.
- **P8, strategy stealing.** Correct under the page's rules. See item 4.
- **P9, 7×7 play.** The board is 7 by 7. See item 5 for its size.
