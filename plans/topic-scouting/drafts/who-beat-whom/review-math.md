# Math review: who-beat-whom-v1 draft

Reviewer: independent math check (CRITIC-MATH stage). Draft PDFs: `draft/k-1.pdf` (4 pp.), `draft/grades-2-3.pdf` (6 pp.), `draft/grades-4-5.pdf` (7 pp.).

## Method

- I wrote my own parser. It reads every `draft/src/figs/*.tex` file and recovers each drawn tournament from the geometry alone: the circles and their labels, the link segments, and each arrowhead polygon (tip against notch, matched to the segment it sits on). I did not use `gen.py`, `tourn.py` or `answers-check.txt`. The parser also checks that every pair of players is linked exactly once, that no link runs through a third player's circle, and that no arrowhead sits ambiguously close to another line.
- I recompiled the three `.tex` files from those figure files in a scratch copy. Every page renders pixel-identical to the delivered PDFs, so the parsed figures are the printed figures.
- I wrote my own code for line-ups (Hamiltonian paths), win counts and kings for every printed tournament. I enumerated all tournaments on 3–6 players to check the general claims the pages rely on.
- I rendered every page and looked at it at 70–200 dpi to compare diagrams with the text.

General facts verified by full enumeration (labelled tournaments):

| n | line-up counts that occur | king counts that occur | sorted win lists |
|---|---|---|---|
| 3 | 1, 3 | 1, 3 | 2 |
| 4 | 1, 3, 5 | 1, 3 | 4 |
| 5 | 1, 3, 5, 9, 11, 13, 15 | 1, 3, 4, 5 | 9 |
| 6 | all odd, 1 to 45 | 1, 3, 4, 5, 6 | 22 |

Every top scorer was a king in all 2^15 six-player tournaments. Landau's test agreed with brute-force realizability on every printed win list. No three-animal tournament has two unbeaten animals, and no four-animal tournament has equal win counts (6 games cannot split evenly among 4 players).

## Grades K–1: mathematics correct throughout

| Problem | Asks | Verified answer |
|---|---|---|
| Rules (p1) | Example tournament: cat beat dog, dog beat bear, cat beat bear; line-up cat, dog, bear | Matches; the only line-up |
| P1 (p1) | Play all 6 games on the board, then line up | Always possible (Rédei) |
| P2 (p2) | Number of line-ups, two triangles | Left (frog beat pig and rabbit, pig beat rabbit): **1**. Right (dog beat cat, cat beat bear, bear beat dog): **3** |
| P3 (p2) | Line up each of 4 pictures | TL 1 line-up (pig cat dog frog); TR 3; BL 3; BR 5. All solvable |
| P4 (p3) | Arrows giving exactly one line-up | Possible: any strict ranking (24 of 64 boards) |
| P5 (p3) | Most line-ups possible | **5** (24 of 64 boards) |
| P6 (p3) | No line-up at all? | Impossible |
| P7 (p4) | Equal wins with 3 animals; equal wins with 4 animals; two unbeaten among 4 | Yes (a cycle); No; No |
| P8 (p4) | Which animals can be first | Left: **dog only**. Middle: **cat, pig, rabbit** (not bear). Right: **all four** |
| P9 (p4) | Frog, then pig, insert into the line-up | Always possible |

The arrowheads match the parsed edges in every picture, and none is hidden by a crossing or a circle.

Located problems (diagram or material size; the mathematics is correct):

**K1-a. Page 1, Problem 1, the board.** The dashed lanes are drawn for arrow cards that the outline sizes at "about 2 by 10 cm". From `k1_board.tex`, the four side lanes are 8.2 cm × 2 cm, so a 10 cm card overhangs by 1.8 cm onto the animal squares. The two diagonal lanes are 11.6 cm long and cross, so one diagonal card lies on top of the other at the centre. The arrowheads at the card ends stay visible, so that crossing is harmless. **Smallest fix:** cut arrow strips to about 2 × 8 cm. Another option is to accept the overhang and note it in the materials. The board cannot grow, because it already spans 18.2 cm of the 19.1 cm text width. The fit has not been rehearsed physically.

**K1-b. Page 3, Problems 4 and 5.** "Lay the arrows on the board so that…" sits directly above a small four-animal drawing: centres 4.6 cm apart, side links 2.7 cm long. A 10 cm arrow card cannot be laid on that picture. Read aloud, "the board" will be taken to mean the picture under the sentence, but only the Problem 1 board can hold the cards. Problem 6 says "on the board" with no picture, which supports the big-board reading. **Smallest fix:** "Lay the arrows on the big board so that the four animals can line up in only one way. Then draw them here." Make the same change in Problem 5. The other option is to tell children to draw the arrows on the picture.

## Grades 2–3: mathematics correct throughout

| Problem | Asks | Verified answer |
|---|---|---|
| Rules (p1) | Example: B beat A, A beat C, B beat C; line-up B, A, C | Matches; the only line-up |
| P1 (p1) | Three played 4-animal tournaments, a line-up each | Always possible |
| P2 (p2) | A line-up for each; which have only one | TL 5 line-ups; **TR 1** (D B A C); **BL 1** (C E A D B); BR 3. Alphabetical and clockwise order is never a line-up |
| P3 (p3) | Insert frog, then pig | Always possible |
| P4 (p3) | Every place X can join A→B→C→D→E | TL (X lost to A, B, C; beat D, E): **between C and D** only. TR (lost to all): **after E** only. BL (beat only B): **between A and B, and after E**. BR (beat A and D): **before A, between C and D, after E** |
| P5 (p4) | Results for X so X cannot join | Impossible |
| P6 (p4) | 6 players with no line-up | Impossible |
| P7 (p5) | All kings | TL **A, C, D**; TR **C**; BL **A, C, D, E**; BR **all five** (each wins 2) |
| P8 (p6) | Four players with exactly 1, 2, 3, 4 kings | 1 and 3 can be made; 2 and 4 cannot |
| P9 (p6) | Is a top scorer always a king? | Yes (Landau) |

I checked the four P4 pictures arrow by arrow against the results listed above.

Located problem (diagram position):

**G23-a. Page 3, Problem 4, bottom row.** Two correct answers need marks in the same strip of paper. The bottom-left case needs a mark after E, and the bottom-right case needs one before A. The strip between the left picture's E and the right picture's A is 1.2 cm wide: the 0.25 cm figure padding on each side plus the 0.7 cm column gap. A mark there could belong to either picture. The front-of-line space for the left-column pictures is also only about 0.55 cm before the text margin. **Smallest fix:** widen the column gap to about 2 cm and give each picture about 1 cm of padding at both ends of the row. A fuller fix is a short empty stub line before A and after E in every newcomer picture, so that "front" and "back" read as places. The same newcomer figure is used in grades 4–5 Problem 3. Neither correct answer there needs an end mark, but the padding is just as tight.

## Grades 4–5: mathematics correct throughout

| Problem | Asks | Verified answer |
|---|---|---|
| P1 (p1) | Play 5 animals, line up, insert pig | Always possible |
| P2 (p1) | Every line-up | 1st: **5** (A C B D, A D C B, B A D C, C B A D, D C B A). 2nd: **3** (B D C A, C B D A, D C B A). 3rd: **1** (C A D B). 4th: **3** (D A C B, D B A C, D C B A). 6 ruled lines each is enough |
| P3 (p2) | Places for X; then explain why X can always join | Left (beat C and E only): **between B and C, and between D and E**. Right (beat E only): **between D and E** only. The general claim holds |
| P4 (p2) | Every tournament has a line-up | True (insertion and induction) |
| P5 (p3) | All kings | Pentagon 1: **A, C, D**. Pentagon 2: **B, C, D, E**. Hexagon 1: **all six**. Hexagon 2: **A, D, F** (F has 1 win but beat D, who beat everyone else) |
| P6 (p3) | Top scorer is a king | True |
| P7 (p4) | King counts for 4 and 5 players | 4 players: **{1, 3}**. 5 players: **{1, 3, 4, 5}** |
| P8 (p4) | Exactly two kings? | Never (Maurer), confirmed up to 6 players |
| P9 (p5) | Realize printed win counts (5 players) | (1,3,1,4,1) possible; (0,3,4,0,3) **impossible** (two players with 0); (2,2,2,2,2) possible; (4,1,0,4,1) **impossible** (two players with 4); (3,0,3,1,3) possible |
| P10 (p6) | Same for 6 players | (4,1,4,1,4,1) possible; (0,4,1,5,1,4) **impossible** (the 0, 1, 1 players play 3 games among themselves but have only 2 wins); (2,3,2,3,2,3) possible; (5,0,2,4,2,2) possible |
| P11 (p6) | All sorted win lists for 4 and 5 players | **4** lists: (0,1,2,3), (0,2,2,2), (1,1,1,3), (1,1,2,2). **9** lists for 5 players |
| P12 (p7) | A test for win lists | Landau's condition. The page asks only for a test and an explanation, and claims nothing false. The "enough" direction is a genuine theorem, which is fine for a late problem |
| P13 (p7) | Exactly 2 or exactly 4 line-ups with 4 players? | Neither. The four tournament types give 1, 3, 3, 5 line-ups |

The numbers printed in the P9 and P10 dots match the lists above position by position, and every printed list has the correct total (10 or 15). The P9 and P10 drawings are complete graphs with no line through a third dot.

Located problems (minor; the mathematics is correct):

**G45-a. Page 3, Problem 5, both hexagons.** In each hexagon, three arrowheads sit 0.29 cm from a second line where diagonals cross. For example, in the left hexagon the B→D head lies 0.29 cm from line A–C. At 200 dpi each head clearly lies along its own line and points the right way, so no edge reads wrong. This is a legibility margin to keep in mind if the figures shrink. No change is needed at the current size.

**G45-b. Page 4, Problem 7.** Exactly four blank pentagons are printed, and exactly four king counts are achievable for five players. A child who tries for 2 kings with five players has nowhere spare to draw the attempt. The matching count may also hint at the answer. **Smallest fix:** add one or two more small pentagons, labelled as extra workspace, or allow the back of the sheet.

## Not mathematical errors, noted for the general critic

- K–1 Problem 9 and grades 2–3 Problem 3: neither page shows a place for the frog's and pig's games (no lanes and no picture with six animals), or a 5- or 6-box strip in K–1. The insertion itself is always possible.
- Grades 2–3 Problem 5 figure draws X twice, once by the generic routine and once by the overlay. The two are identical and print identically.
