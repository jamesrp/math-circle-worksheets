# Mathematical review: Games decided before they start (draft v1)

Reviewed: `draft/k-1.pdf` (7 pp.), `draft/grades-2-3.pdf` (6 pp.), `draft/grades-4-5.pdf` (8 pp.), built from `draft/src/*.tex` (PDFs dated 15:28, Oct 24).

How I checked: I wrote my own planar game engine. A position is stored as regions, each region as its boundary walks, and each spot has its own lives. With it I searched every possible game, so the following results are exact, not sampled:

- 2-Sprigs with 1–6 dots: the only possible length is n.
- Sprouts with 1, 2 and 3 spots: possible lengths {2}, {4, 5} and {6, 7, 8}. With best play the 1st player loses, loses and wins.
- Brussels Sprouts with 1 and 2 crosses: possible lengths {3} and {8}.

On top of that:

- I played random games: Sprigs with 7 and 10 dots, and 400 games of Brussels Sprouts with 3 crosses, which all lasted 13 moves.
- I ran a cooperative strategy that reaches 3n − 1 Sprouts moves for n = 2, 3, 4 and 10, which gives 29 for 10 spots.
- I enumerated every break order for the bars.

All the scripts are in [`math-check/`](math-check/) (`planar.py`, `run1.py`–`run3.py`).

The numbers themselves are right in all three bands: every bar count, every winner and every move count that a page asks for. The problems are in the rules. Two gaps in the curve-game rules let children make legal-looking moves that break the fixed game lengths the packet depends on. One counting instruction in grades 4–5 makes Euler's rule fail for one of the two reasonable readings.

## Located problems

### 1. A loop at a dot or spot with only one token is not ruled out (all bands; this changes winners)

Quoted text:
- K–1, p. 3, 2-Sprigs rules: "Take away one token for each end of the new line. A dot with no tokens left cannot get another line."
- Grades 2–3, p. 3, and grades 4–5, p. 3, 2-Sprigs rules: "After each line, the other player takes away one token for each end of the line, and a line cannot end at a dot with no tokens left."
- Grades 2–3, p. 5, and grades 4–5, p. 5, Sprouts rules: "A line cannot end at a spot with no tokens left."

Evidence: tokens are only removed after the line is drawn. So under the literal wording, a loop at a dot that has one token is allowed: when the loop is drawn, neither end lands on a dot with no tokens. The partner then removes the single token there. The loop picture shows a dot with two tokens, but it shows one allowed case; it does not forbid this one.

- 2-Sprigs: I added these loops to the engine and searched every game. The possible lengths become {2, 3} for 2 dots, {3, 4} for 3, {4, 5, 6} for 4 and {5, 6, 7} for 5. One example with 2 dots: A–B, then A loops, then B loops, for 3 moves, so the 1st player wins. This changes the answers on these pages:
  - K–1: Problems 4–7, and the answer to Problem 6 ("Can the 2nd player win 2-Sprigs on a board with 5 dots?") becomes yes.
  - Grades 2–3: Problems 4–6.
  - Grades 4–5: Problems 4–5. The answer to Problem 5 ("Can a game of 2-Sprigs end while some dot still has a token?") also flips.
- Sprouts: a spot with one token loops, and the new spot gets one token. That new spot loops, and so on, so the game never has to end. This breaks grades 4–5 Problem 7 (largest number of moves for 10 spots is 29) and Problem 6, and grades 2–3 Problems 7–8.

Smallest fix: say that each end needs its own token.
- K–1: replace the last two rule sentences before "Whoever draws…" with: "Take away one token for each end of the new line. Each end needs a token, so a loop needs a dot with two tokens."
- Grades 2–3 and 4–5, Sprigs: replace "and a line cannot end at a dot with no tokens left" with "and each end of a line needs its own token, so a loop needs a dot with two tokens."
- Sprouts, both bands: replace "A line cannot end at a spot with no tokens left." with "Each end of a line needs its own token, so a loop needs a spot with two tokens."

### 2. Lines that cross themselves are not ruled out (2-Sprigs in all bands, Brussels Sprouts in grades 4–5; this changes winners)

Quoted text:
- K–1, p. 3: "A line may not cross another line or touch any other dot."
- Grades 2–3, p. 3, and grades 4–5, p. 3: "A line may bend, but it may not cross a line or touch any other dot."
- Grades 4–5, p. 6, Brussels Sprouts: "The line may not cross a line or touch any other cross."

The K–1 wording ("another line") actually permits a line that crosses itself, and the other wordings leave it open. The crossing picture shows only two different lines crossing.

Evidence for 2-Sprigs, with 2 dots A and B:
1. Draw the first line from A eastward.
2. Circle it once around A and cross its own first stretch.
3. Continue to B.

A now has one token and sits inside the small closed loop; B, also with one token, is outside it. Neither dot can loop, and any line joining them would cross the loop. The game ends after 1 move with two tokens left, so the 1st player wins on 2 dots. The same trap gives the 2nd player a win on 5 dots, for example:
- Move 1: A loops.
- Move 2: B–C, with the trap around B.
- Move 3: D–E.
- Move 4: D–E again, which closes them into a loop. C cannot reach B, so the game ends after 4 moves.

This flips K–1 Problem 6 and grades 4–5 Problem 5, the problem that explicitly asks children to try to make a game end early. A child who tries hard is likely to find exactly this.

Evidence for Brussels Sprouts, with 1 cross:
1. Join the top and bottom arms by a curve around the left arm. Give the curve a small outward kink that crosses itself, and put the bar on the kink, so that one new arm is inside the kink and the other is outside.
2. The regions now hold: {left arm}, {kink arm} and {right arm, outer bar arm}.
3. Join the right arm to the outer bar arm. This splits the outside into two regions with one new arm each.

Now four regions each hold one free arm, so the game ends after 2 moves instead of 3. This contradicts grades 4–5 Problem 8 and the 5n − 2 rule used in Problems 9–10.

Smallest fix:
- K–1: "A line may not cross itself or another line, or touch any other dot."
- Grades 2–3 and 4–5, Sprigs: "A line may bend, but it may not cross itself or another line, or touch any other dot."
- Brussels Sprouts: "The line may not cross itself or another line, or touch any other cross."

Add the same "itself" wording to the Sprouts rules for consistency. I did not find a Sprouts counterexample, and the 3n − 1 bound does not depend on it.

### 3. Grades 4–5, p. 8, Problem 10: the line count in the last drawing is ambiguous, and one reading breaks the rule

Quoted text: "In the last drawing, count each cross as a dot, and count only the lines between crosses, not the free arms. Find a rule that connects the three numbers."

Evidence: the last drawing is a correct finished one-cross game. Its three moves draw three curves, and each curve runs through the cross that move created, which gives:
- 4 crosses
- 6 pieces of line from one cross to the next
- 4 regions, each holding one free arm

Counting pieces, 4 − 6 + 4 = 2, which matches the other three drawings:
- the tree: 5 − 4 + 1
- the square with a diagonal: 4 − 5 + 3
- the lens with a loop: 2 − 3 + 3

A child who counts the three drawn curves as "the lines between crosses" gets 4 − 3 + 4 = 5, and the rule seems to fail on exactly the drawing that leads into Brussels Sprouts. The later explanation needs the piece count: each move adds one cross and two pieces of line, and the finished 2-cross game has 8 regions, so 2 + m − 2m + 8 = 2 gives m = 8.

Smallest fix: "In the last drawing, count each cross as a dot. Count each piece of line from one cross to the next as one line, so a line that passes through a cross counts as two. Do not count the free arms."

### 4. Minor: "play each bar twice" needs more bars than the outline provides (all bands)

Quoted text:
- K–1, p. 2, Problem 3: "Play two games on each bar"
- Grades 2–3, p. 1, and grades 4–5, p. 1, Problem 1: "Play each bar twice, switching who goes first"

Evidence: a card bar is used up once it is cut into squares. The outline provides "about six bars per pair", one of each size. Per pair, the pages actually need:
- K–1: 8 bars (two each of 3 by 3 and 2 by 4)
- Grades 2–3: 9 bars (two each of 2 by 3, 3 by 3 and 2 by 4)
- Grades 4–5: 7 bars

Snap-cube slabs can be put back together, but card bars cannot.

Smallest fix: no wording change. Print two copies of each bar used in that problem, or tell the adults that the bars for the second game are snap-cube slabs.

### 5. Minor diagram placement: K–1, p. 2, Problem 3

The bottom edge of the 3 by 3 bar sits on the "Game 1 1st 2nd" recording row, so the bar touches its text. The 2 by 4 bar next to it has clearance. This does not change the mathematics; add about 4 mm below the bars.

## Checked and correct (for the reviser's reference)

### K–1

| Problem | Answer |
|---|---|
| P1 | 2×2, 2×3, 1×6 bars: 3, 5, 5 breaks |
| P2 | 3×4: 11 breaks in every order; no one can do it in fewer |
| P3 | 3×3: 8 breaks, 2nd player wins; 2×4: 7 breaks, 1st player wins |
| P4 | 2 dots: 2nd player wins; 3 dots: 1st player wins |
| P5 | 4 dots: always 4 lines, 2nd player wins |
| P6 | 5 dots: no, the 1st player always wins |
| P7 | 6 dots: 2nd player wins |
| P8 | The groups have 6, 9 and 12 squares in 3, 5 and 7 pieces, so 2, 4 and 6 breaks. Each group really can be broken from a 2×3, 3×3 and 3×4 bar |

The break picture (2×5 into 2×2 and 2×3) and the dot counts on every board are correct. Dots are at least 4 cm apart.

### Grades 2–3

| Problem | Answer |
|---|---|
| P1 | 2×3: 1st player wins; 3×3: 2nd; 2×4: 1st. No, the loser can never change the result |
| P2 | 11, 5, 3 breaks |
| P3 | 4×5: 19 breaks, 1st player wins; 3×5: 14, 2nd; 5×5: 24, 2nd; 1×9: 8, 2nd; 6×6: 35, 1st |
| P4 | 3 dots: 1st player wins; 4 dots: 2nd |
| P5 | 5 dots: 1st player wins; 6 dots: 2nd |
| P6 | 10 dots: 2nd player wins; 25 dots: 1st |
| P7 | Sprouts with 1 spot always lasts 2 moves, so the 2nd player wins. With 2 spots a game lasts 4 or 5 moves |
| P8 | Most 5 moves, fewest 4, so yes, choices can change the winner |

The pictures in both sets of rules show the correct token counts. The bar labels match the grids.

### Grades 4–5

| Problem | Answer |
|---|---|
| P1 | As in grades 2–3 |
| P2 | Fewest = most = 11 (exhaustive) |
| P3 | 7×9: 62 breaks, 2nd player wins; 8×13: 103, 1st; 25×40: 999, 1st. Rule: the 1st player wins exactly when one side is even. Starting with 2×3 and 2×4: 12 breaks, 2nd player wins |
| P4 | 3 moves, 1st player wins; 4 moves, 2nd player wins |
| P5 | No (once the fixes in findings 1 and 2 are made). The 1st player wins exactly when the number of dots is odd |
| P6 | 2 spots: 5 and 4 moves; 3 spots: 8 and 6 moves (exhaustive) |
| P7 | 29 moves, which can be reached: keep every live spot on one region's boundary |
| P8 | 1 cross: 3 moves; 2 crosses: 8 moves, in every game (exhaustive) |
| P9 | 3 crosses: 13 moves; 10 crosses: 48 |
| P10 | Euler counts as in finding 3 |

In the Brussels Sprouts rule pictures, the bars sit at the curve midpoints and are perpendicular to the curves. The last drawing in P10 is a legal finished game with one free arm per region.
