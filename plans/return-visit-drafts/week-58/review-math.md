# Week 58 return visit: mathematical review of the draft

Reviewer: an independent check, run as the optional CRITIC-MATH stage. The draft was not edited.

Inputs: `draft/k-1.pdf` (5 pp.), `draft/grades-2-3.pdf` (6 pp.) and `draft/grades-4-5.pdf` (6 pp.). These are byte-identical to the PDFs in `draft/src/`. Every train, strip, panel row, value table and game mark was read from the TikZ coordinates in `draft/src/*.tex`, not from `gen.py` or the author's `check.py`, and checked against the rendered pages. All checks are exact, in fractions. My scripts:

- `/tmp/claude-0/-home-claude/d1d23a10-bfbf-5b59-a13a-5f6afdbf2b0f/scratchpad/w58chk/parse.py` extracts the diagrams from the TeX.
- `.../w58chk/verify.py` checks trains by brute force: every set of cut gaps with every tray assignment.
- `.../w58chk/verify2.py` solves the strip and X Y Z exact-halves problems as exact piecewise-linear systems, not on a grid.
- `.../w58chk/verify3.py` runs the marking game in all six orders and checks the card-row problems.

## Verdict by band

- **K–1:** P1, P2 and P5 are correct. **P3** is a "find all" task with far more answers than the page allows room for. **P4** can be solved with one lengthwise cut.
- **Grades 2–3:** P2 and P4 are correct. P3, P5 and P6 are correct apart from the issues below. **P3** has the lengthwise-cut loophole. P1 has 8 answer slots for 6 answers (low severity). In P5 and P6 one person in every game has to mark at a quarter-panel point (low severity).
- **Grades 4–5:** P1, P2, P5, P6, P7 and P8 are correct. **P3** (and, more weakly, P4) needs the rule that cuts go straight across. P8 names cards that may not be cut (low severity).
- **All bands:** the shared worked example invites a stricter reading of the rule (low severity).

## Located problems

### 1. K–1, page 3, Problem 3: the "find all" count does not fit the page (medium)

Text: "One player makes a train with four red cards and four blue cards, and the other player tries to share it by pulling it apart only once. **Draw the trains that cannot be shared that way.**" Below it are 7 blank rows of 8 cards.

Evidence: of the 70 colour orders of 4 reds and 4 blues, **34** cannot be shared with one pull-apart. These are exactly the orders whose first four cards do not hold two reds. That is 17 up to reversal and 11 up to reversal and colour swap. "Draw the trains" asks for all of them, but the page has room for 7. A child who draws 7 has not finished. A child who notices that there are many more has no room and no stopping point.

Smallest fix, keeping the "find all" intent: use **four red cards and two blue cards**. Exactly **6** of the 15 orders then need two pull-aparts (BBRRRR, BRBRRR, RBBRRR, RRRBBR, RRRBRB, RRRRBB), which fits the 7 rows. Change the blanks to 6 cards per row. The combined K–1 kits (6 reds, 4 blues) cover it. RRRRBB already appears on P2, which does no harm. If 4R4B is kept, change the task to "Draw as many trains as you can find that cannot be shared that way." and drop the claim of completeness.

### 2. Strip problems: a lengthwise cut gives a one-cut answer (medium at K–1, lower at 2–3 and 4–5)

- K–1, page 4, Problem 4: "Share one red and blue strip between the two trays so that both trays get the same amount of red and the same amount of blue. Mark where an adult should cut, using as few cuts as you can."
- 2–3, page 3, Problem 3: "… Use as few cuts as you can. Can one cut do it? …"
- 4–5, page 2, Problem 3: "… Use as few cuts as you can, and explain why fewer cuts cannot work. …"

Evidence: no page says that cuts go straight across the strip. The outline's constraint does: cut "parallel to the colour join". One cut along the length, top half and bottom half, gives each tray exactly half the red and half the blue. Because both cards are additive, it also gives each tray exactly half the value for A and for B. So under that reading the answer to "Can one cut do it?" becomes yes, and "explain why fewer cuts cannot work" asks for something false.

At K–1 this is the most natural move: folding the strip "in half" lengthwise, the hot-dog fold. At 2–3 and 4–5, "value follows length" leaves the value of a lengthwise half undefined, which weakens the loophole there but does not close it.

Under the intended rule (cuts straight across) the intended answers are right. I checked them exactly:

- One cut cannot work. A's only exact one-cut point is 80 mm and B's is 160 mm.
- Two cuts at **60 and 180 mm** work, with the middle piece in one tray. This is the **unique** two-cut answer: 3r + s = 2 and r + 3s = 2 force a piece with 60 mm of red and 60 mm of blue. This settles 4–5's "Is there more than one way?" as no, apart from swapping the trays.
- The K–1 colour-only version has the same unique answer (60, 180).

Smallest fix: add one sentence. At K–1: "…Mark where an adult should cut **straight across the strip**, using as few cuts as you can." At 2–3 and 4–5, end the strip rule with "Every cut goes straight across the strip." At 4–5 P4 (X Y Z), add "Every cut goes straight across a panel." There, a single lengthwise line drawn through the whole row could otherwise be called "one cut". Since the panels are separate pieces, cutting each one lengthwise still takes 3 cuts. The intended answer of 3 is right either way: each panel must be split exactly in half (see the P4 check below).

### 3. 2–3, pages 5–6, Problems 5–6: one second-round mark per game falls at a quarter panel (low)

Text: "The other two mark again from the new left end, aiming at 4 again…". The only cutting example on the page shows halves ("25 mm, worth 4").

Evidence, from exact runs of the game:

| Order | Round 1 marks (A, B, C) | Taker | Round 2 marks | Taker | Last |
|---|---|---|---|---|---|
| X Z Y | 50, 75, 25 | C, 0–25 | A **112.5**, B 75 | B, 25–75 | A, 75–150, worth 8 |
| Y X Z | 25, 50, 75 | A, 0–25 | B **112.5**, C 75 | C, 25–75 | B, 75–150, worth 8 |
| Z Y X | 75, 25, 50 | B, 0–25 | A 75, C **112.5** | A, 25–75 | C, 75–150, worth 8 |

The cuts are all at half-panel points, as the outline says. But in every 2–3 game the person who does not take a piece in round 2 must mark 12.5 mm into the last panel (a quarter panel, worth 2 of 8). The page never shows this, and the outline gives quarters to grades 4–5. The outcome does not depend on that mark: it is clearly to the right of the taker's 75 mm. So this is a feasibility point, not an error.

Smallest fix: tell the facilitator or referee that a non-taker only needs to see that their mark lies past the leftmost one. Alternatively, add "12.5 mm, worth 2" to the panel-cut example on page 5.

Everything else in P5 and P6 checks out. The worked first round on X Y Z is correct: C at 25 mm, A at 50 mm, B at 100 mm, and C takes 0–25 mm. The arrow points to 25 mm. No mark is tied. Nobody gets less than 4. Someone envies in every game: in XZY, B envies A (8 vs 4) and C envies B (6 vs 4); in YXZ, A envies C (6) and C envies B (8); in ZYX, A envies C (8) and B envies A (6). So the expected answers are "no" and "yes".

### 4. 2–3, page 1, Problem 1: 8 answer slots for 6 answers (low)

Text: "Find every train you can make with two red cards and two blue cards, counting only the order of the colours." There are 8 blank four-card rows.

Evidence: there are exactly C(4,2) = 6 colour orders. RRBB and BBRR need 2 cuts and the other four need 1. Eight slots suggest there are 8 to find, and children may hunt for two that don't exist or count a reversal twice.

Smallest fix: print 6 rows. If you want to avoid revealing the count, 7 rows is less suggestive than 8.

### 5. All bands, shared worked example: the picture suggests a stricter rule (low)

Diagram: RBRRBR is cut in the middle, and **both trays show the identical sequence R B R**. The text rule is correct ("the same number of red cards and the same number of blue cards"). But for K–1 children, who do not read and generalize from the picture, it suggests that the trays must hold the same train. Under that reading, BRRB (BR | RB) and RBBR (RB | BR) on K–1 P1 would look unsharable with one pull-apart, and other answers would change too.

Smallest fix: use a non-task example whose trays hold equal counts in different orders, such as **RRBBRR → RRB | BRR** or **RBRBRR → RBR | BRR**. Each is a one-cut train (checked), and neither appears in any band's tasks.

### 6. 2–3, page 3, Problem 3: printed strips are at 70% scale (low)

Text: "Measure from the red end, and mark in pencil before anyone cuts." The printed strips are 168 mm long for the 240 mm strip, with tick labels in real millimetres (ticks every 7 mm on the page, labels every 40 strip-mm). The labels are consistent. But a child who measures 60 mm on the page with a ruler lands at about 86 strip-mm.

Smallest fix: "Measure on your strip from the red end…". Alternatively, rely on the printed tick labels only.

### 7. 4–5, page 6, Problem 8: the named cards may not be cut (low, materials)

Text: "They share the two red cards R1 and R2, lying side by side." R1 and R2 are the sturdy mounted cards. The kit allows only the paper R3, or unmounted copies, to be cut. If children act out the marking game, it cuts **both** reds: at 2/3 of the way into the first and 1/3 of the way into the second (checked). They cannot do that with these cards.

Smallest fix: "They share two paper red cards, lying side by side." All reds are worth 1 to these people, so the names do not matter.

The mathematics of P8 is right. With only one card cut, the uncut card goes whole to someone, and the other two must each get 2/3 from the one cut card, which is worth 1. Since 4/3 > 1, it cannot be done, even if that card is cut more than once. So the answer is no. The marking game makes two cuts, each through at most one card, so at most two cards are cut.

## Checks that passed, with intended answers

**Shared example (all bands).** RBRRBR is shared with one cut, after card 3. This is its unique one-cut answer.

**K–1**

- P1. The six 2R2B trains are exactly all six orders, and the drawn trains match the TeX. RBRB, BRRB, RBBR and BRBR need 1 pull-apart, each at the middle and unique. RRBB and BBRR need 2, at R|RB|B and B|BR|R, each unique.
- P2. The drawn trains match the TeX.
  - 1 pull-apart: BRRBRR, RRBBBBRR, RRRBBBBRRR.
  - 2 pull-aparts: RRRRBB (RR|RRB|B), RRRRBBBB (RR|RRBB|BB), RRRRRRBBBB (RRR|RRRBB|BB).
  - Cross out RBRBR (3 reds).
  - Every train uses at most 6 reds and 4 blues.
- P5. Answer: no. I checked all 790 trains with at most 6 reds and at most 4 blues, of any parity: 441 cannot be shared at all (odd counts), 179 need 1 pull-apart and 170 need 2. None needs 3.

**Grades 2–3**

- P2. The drawn trains match the TeX.
  - 1 cut: BRRBRRBB, RBBRRRRBBR.
  - 2 cuts: RRRRBB, RBBRRR, RRRBBBBR, RRBRRRBBBR (two different 2-cut answers).
  - Cross out RBRRBRB (3 blues).
- P3. The two-person cards are drawn correctly (A: red 3, blue 1; B: red 1, blue 3), and "40 mm of red is worth 1 to A" is right. For the answers, see item 2.
- P4. Answer: no. Brute force over every even-count two-colour train up to 12 cards finds a maximum of 2 cuts, and the sliding-window argument covers all lengths. (A third colour, as in RRBBGG, would need 3, but the goods cards have only two colours.)
- P5/P6. The value table matches the outline: A (4, 8, 0), B (0, 4, 8), C (8, 0, 4). The worked example "Y, 50 mm, worth 8 to card A → 25 mm, worth 4" is right. The rest is under item 3.

**Grades 4–5**

- P1. The drawn trains match the TeX.
  - 1 cut: BRRBRBBR, BBRRRRRRBB.
  - 2 cuts: RRRBBBBR, RRRRBBBB, RBRRRRBRBB (the window covers cards 5–9), RRRRRRBB.
  - The 4R4B question: 36 of 70 orders take one cut, exactly those whose first four cards hold two reds. I checked this criterion against brute force.
- P2. Answer: no. Verified as for 2–3 P4.
- P4. Answer: 3 cuts, at 25, 75 and 125 mm, with alternate pieces in each tray. A tray worth 6 to A, B and C must hold fractions x, y, z of X, Y, Z with 4x + 8y = 6, 4y + 8z = 6 and 8x + 4z = 6. The determinant is 576, so the only solution is x = y = z = 1/2. Every panel must therefore be cut inside, which proves at least 3 cuts are needed. An exact piecewise-linear solve finds no 1-cut or 2-cut solution in any of the six orders. With three cuts, the positions 25, 75, 125 and the alternating assignment are forced. Children can see x = y = z by adding the three equations (x + y + z = 3/2) and comparing that with each equation.
- P5. In all six orders: no mark is tied, both takers get exactly 4, the last person gets 8 or 11, and at least one person envies another.
  - XYZ: C takes 0–25, A takes 25–62.5, B gets 11. A values B's piece at 6.
  - YZX: A takes 0–25, B takes 25–62.5, C gets 11. B envies C (6).
  - ZXY: B takes 0–25, C takes 25–62.5, A gets 11. C envies A (6).
  - XZY, YXZ, ZYX: as in the table under item 3.
- P6. The explanation is the standard one (each taken piece was worth at most 4 to everyone still marking, so the last person keeps at least 12 − 4 − 4). "Can the game ever do that well for all three?" has the answer no: each of the two takers always gets exactly 4 by their own card.
- P7. The cards are drawn in the order R1 B1 R3 B2 R2. With card A the total is 11 and half is 5.5, so the cut goes **halfway through R3** (62.5 mm from the left of the 125 mm row, using the paper R3). "Can you arrange … between two cards, or inside a blue card?": no. In all 120 arrangements the cut falls strictly inside a red card. The running totals are whole numbers, so they never equal 5.5. A blue card would need the cards before it to total 5 = 3 + 1 + 1, which uses up both blues.
- P8. Correct; see item 7.
