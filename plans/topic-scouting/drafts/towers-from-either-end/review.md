# Review: Towers from either end, draft v1

Reviewed: `draft/k-1.pdf` (6 pages, Problems 1–7), `draft/grades-2-3.pdf` (7 pages, Problems 1–9), `draft/grades-4-5.pdf` (6 pages, Problems 1–11), and the sources in `draft/src/`. Every page was rendered and inspected at 80 dpi, with the tight spots checked at 150–200 dpi and one colour page checked in grayscale. I re-solved every printed row with my own full game-tree solver, which is separate from the author's `check.py` and `verify.py`.

## Overall verdict

This is a strong draft. The mathematics is correct: every intended answer, unique winning move, colour total and table value checks out (key in the appendix). The problem sequence follows the outline closely in all three bands: free play, then a winning first move, then rows of three as traps, then a search for a losing even row, and only then the tinted strips, the colour plan and odd rows. The pages are clean. There are no titles, encouragement, hints, lettered sub-steps, exclamation marks or dashes, and no overfull boxes. The headers, footers and problem labels follow the standard, and nothing overlaps.

The issues worth fixing are mostly about recording conventions and the precision of a few phrases, not about the mathematics. In priority order:

1. K–1 Problem 1 has no way to record a tie, and "1st / 2nd" reads as first place. One of its three rows is a tie under best play.
2. "Play as well as they can" is undefined where the pages ask "by how many cubes" or ask for a best first move on a losing row.
3. 2–3 Problem 6 uses a new recording convention (slot numbers in order) with no example, and it clashes with the intro's convention (heights).
4. "The red towers / the blue towers" is ambiguous if the snap cubes come in colours, and the red/blue distinction does not survive black-and-white printing.
5. A few smaller problems: a duplicate row in 4–5, every 2–3 Problem 2 answer being "the shorter end", too many recording rows in 2–3 Problem 6, and staffing bottlenecks for the problems where children play the grown-up.

## High priority

### H1. K–1 Problem 1: no tie option, and "1st / 2nd" is ambiguous (page 1)

Text: "Play each row two times, taking turns to go first. Ring who won each game." Each game gets a rounded box reading "1st  2nd".

- **There is no tie choice.** The opening rules on the same page say "If the stacks are the same height, it is a tie." Row 3 (2, 4, 3, 1) ties 5–5 under best play whichever end is taken first. Row 1 (5, 2, 1, 4) ties 6–6 if the first player takes the 4. So the first thing K–1 children do often produces an outcome the page cannot record. This is the very first problem, where a confusing record does the most damage.
- **"1st" reads as a placing.** Ringing "who won" with the choices "1st" and "2nd" invites a five-year-old to ring "1st" because the winner came first. What the page means is "the player who went first".
- **Reading demand.** The outline says K–1 needs "no reading beyond slot numbers"; "1st/2nd" is a small reading demand on top of that.

Fix: give each game three choices that an adult can read once and a child can then recognise, for example "went first / went second / tie", or pictograms: a "1" and a "2" in circles plus two equal stacks for a tie. Reword to "Ring who won each game, or ring tie." Keep the "1st / 2nd" boxes in K–1 Problem 3, where the question really is "better to go first or second". None of the Problem 3 rows is a tie, so no tie choice is needed there.

### H2. "As well as they can" is undefined where the margin matters (4–5 intro, P1, P6, P10, P11; 2–3 P7, P8)

The 4–5 intro defines "who wins" as "who wins when both players play as well as they can". It then asks "by how many cubes" (P1, P6, P10) and asks for "the first player's best first move" on a row the first player loses (P10, row 5, 2, 6, 1, 3).

If players only try to win, lose or tie, the winning margin is not well defined. On a losing row, both first moves are equally "best". On 5, 2, 6, 1, 3, taking the 5 loses 8–9 and taking the 3 loses 6–11; a child who reasons "both lose, so neither is better" is right under that reading. The intended answers (the author's key, and mine) assume each player collects as many cubes as possible. That is equivalent to maximising the margin, since the total is fixed. P11 already uses this objective ("the most cubes the player whose turn it is can be sure of collecting"), so the packet is consistent only if the intro says so.

Fix: in the 4–5 intro, replace the definition with something like "Playing as well as you can means collecting as many cubes as you can be sure of." In 2–3, P7 and P8 ask for "the totals when both players play as well as they can". Add the same sentence to the 2–3 intro, or to P7 where the phrase first appears.

### H3. 2–3 Problem 6: an undemonstrated recording convention that conflicts with the intro (page 5)

Text: "…write each game as the slot numbers in the order the towers were taken."

The intro has just taught a different convention: "A row is written as its tower heights from slot 1, so 3, 1, 4, 2 is this row". Problem 6 now asks for a game record made of slot numbers, not heights. On the row 2, 4, 1, 1, 3, 2, a child who writes heights produces "2, 2, 3, 1, 1, 4" for the game whose slot record is "6, 1, 2, 3, 4, 5". Heights repeat, so a record written in heights cannot be read back unambiguously. AGENTS.md asks for a small worked example before the first use of an unfamiliar recording convention, placed with the relevant problem and using a non-task instance.

Also, the 2–3 intro's list notation is never used anywhere in the 2–3 packet: every 2–3 row is a picture, and the blank strips in P4 and P9 take heights written in squares. The sentence teaches the one convention 2–3 does not need and omits the two it does need.

Fix:
- Drop the list-notation sentence from the 2–3 intro. If it is kept, show the launch row 3, 1, 4, 2 as heights written in squares, which is what P4 and P9 need.
- Put a one-line worked record inside Problem 6 on the launch row. For example, show the 3, 1, 4, 2 strip with a filled record row "4 1 2 3" beside it, and no explanatory sentence. The picture shows that the record lists slots in the order taken.

## Medium priority

### M1. "Red towers / blue towers" can be misread, and the colours do not survive grayscale (2–3 P6–P9; 4–5 P6–P9)

The outline allows "mixed colours that carry no meaning" for the snap cubes. With a mixed tub that includes red and blue cubes, "the red towers and the blue towers have the same number of cubes" (2–3 P7, 4–5 P6) can be read as towers built from red cubes. The same goes for "make you take a tower of the other color" (2–3 P6) and "the blue towers have more cubes than the red towers" (4–5 P7, P8).

Separately, the tints (RGB 247,172,172 and 128,168,236) print as two mid-greys of similar lightness. I rendered 4–5 page 4 in grayscale: the slots are distinguishable, but nothing on the page is recognisably "red" or "blue". If any copy is printed in black and white, every sentence that names a colour loses its referent.

Fix: write "towers on red slots / towers on blue slots" (or "red-slot towers"), and in 2–3 P6 "a tower on the other color". Confirm that the packets will be printed in colour. If that is not certain, add a non-colour cue to one class of slots, such as light hatching or a dot. That cue costs no reading.

### M2. The tinted pages sit in the same stapled packet as the plain-strip problems (all bands)

The outline is explicit: "The tinted version must not appear before children have played on plain strips, because the tint is the discovery." The coloured diagrams start on K–1 page 5, 2–3 page 4 and 4–5 page 3. Children who flip ahead, as quick children do, will see the alternating colouring before the plain-strip problems have done their work. In 4–5 it is one page turn after Problem 3, "Is there a row of four towers … on which the first player loses?", which is exactly the question the colouring answers.

Fix (no change to the problems): print the coloured pages as a second stapled set, handed out when a child reaches the grown-up problem (K–1 P5, 2–3 P5, 4–5 P4). Mention this in the facilitator guide. If the reviser prefers to keep one packet, at least make sure no tinted diagram appears on a page facing or immediately behind the search-for-a-losing-row problem.

### M3. Staffing bottleneck in the "play the grown-up" problems (K–1 P5, 2–3 P5, 4–5 P4)

These problems need the table's one adult to play each child, row by row: 4 children × 4 rows in K–1 and 4 × 3 rows in 2–3, at roughly two minutes a game. P6 in both bands depends on having seen the plan, so the children who are waiting cannot simply move on. In K–1 the adult is the non-mathematician parent, who must also apply the colour plan reliably.

Fix: on the page, "You and your partner play together against the grown-up" halves the games and makes the plan a shared observation. In the facilitator guide (not on the page), give the parent a one-line card: "Choose the colour whose towers have more cubes. Always take the end tower of that colour."

### M4. 4–5 Problem 6 repeats a row from Problem 1 (pages 1 and 4)

6, 2, 1, 5 is the last row of P1 and the last row of P6. Children who solved it in P1 get nothing new from it, and the repeat looks like an error. Replace it in P6 with another equal-colour first-player win. Verified options: 3, 2, 4, 5 (red 7, blue 7; the first player wins 8–6 by taking the 5; taking the 3 only ties 7–7), or 4, 2, 1, 3 (red 5, blue 5; the first player wins 6–4 by taking the 4; taking the 3 ties 5–5).

### M5. 2–3 Problem 2: every answer is "the shorter end" (page 2)

All four rows have a unique winning first move, and the other first move loses, which is good. But in every row the winning tower is the shorter end: 2 of (2, 1, 5, 3), 2 of (3, 6, 1, 2), 1 of (1, 4, 6, 2), 3 of (4, 5, 3, 3). The author checked that "take the taller end" fails on each row. A third grader who sees four "take the smaller one" answers in a row will leave with the false rule "take the shorter end". The K–1 version mixes the answers well: four shorter ends and two taller.

Fix: replace one row with a row where the taller end is the unique winning move and the other move loses. Verified: 2, 3, 1, 5 (taking the 5 wins 8–3, taking the 2 loses 5–6) or 5, 1, 3, 2 (taking the 5 wins 8–3, taking the 2 loses 5–6). As in every current row, the winning move still matches the colour-plan move, so the later colour discovery is unaffected.

### M6. 2–3 Problem 6: eight recording rows for four games (page 5)

Under the plan, the first player's moves are forced and the partner chooses only at five towers and at three towers, so there are exactly 4 games: 6-1-2-3-4-5, 6-1-2-5-4-3, 6-5-4-1-2-3, 6-5-4-3-2-1. The planner collects 7 against 6 in every one. "Try every way your partner can play" together with eight ruled record rows suggests there are eight, and children may hunt for games that do not exist, or invent illegal ones to fill the rows. Since "every way" is the point of the problem, the space should not mislead.

Fix: print 4 record rows plus 2 rows set slightly apart as extra space. Alternatively print 6 rows. That still leaves room for mistakes without implying a count of 8.

## Low priority and judgement calls

- **4–5 Problem 3 asks for the explanation that Problem 5 asks for again.** P3: "Find one or explain why there is none". The explanation is the colouring argument, which children meet only in P4, and P5 then asks for it outright. Consider ending P3 at "Is there a row … on which the first player loses?", as 2–3 P4 does, and keeping the explanation in P5. The ruled lines on P3 can stay for recording attempts.
- **4–5 Problem 5's wording "never fails"** is looser than P4's "never loses". A child might call a tie a failure, and P6 is full of rows where the plan only ties. Use "never loses" in P5 too.
- **4–5 order of P1 and P2.** P1 asks for exact best play on six rows of four before P2 gives the rows-of-three rule, which every row of four reduces to after the first move. The outline's "working backward from short rows" suggests rows of three first. Either order is defensible: P1 first lets the children start by playing. If P1 stays first, consider cutting it to four rows so that P2 is reached sooner.
- **4–5 P1 and P2 answer blanks.** The question is "who wins and by how many cubes", but the blanks read "first player ___ second player ___", which asks for totals. Totals answer both parts, so this is consistent, but say so: "write each player's total".
- **The K–1 P2 rows 1, 1, 5, 2 and 2, 5, 1, 1 are mirror images**, and K–1 P5 reuses both rows. The mirror pair could be a nice noticing moment, but the reuse in P5 means two of the four grown-up games are on rows the child has already solved from the first player's side. Consider fresh rows in P5. For a K–1 colour-plan row, a useful property is that the plan's move looks wrong (it takes the shorter end), as in 1, 1, 5, 2 now. 1, 2, 5, 2 (red 6, blue 4) has that property.
- **K–1 Problem 6, "Can you play so that you never lose?"** The opponent is not named (partner or grown-up). Name it; "never lose" is only tested if the opponent tries hard. Also an age-fit note for the guide, not a page change: on rows of four with heights 1 to 5, the colour plan is needed (the taller end loses) only when the colour totals differ by 1 or 2. I checked every such row, and none with a gap of 3 or more needs the plan. So the close totals in P6 (5 v 6, 3 v 5, 6 v 5, 5 v 6) are inherent to the task. K–1 children can compare them only by building a red-slot stack and a blue-slot stack from spare cubes. The adult should know that this is the intended comparison.
- **K–1 Problem 4 drawing boxes** are 6.5 mm dashed squares, small for kindergarten pencil control, and the bottom half of page 4 is empty. Enlarge them to about 9–10 mm. The dashed columns also go to 6 cubes, while K–1 towers are 1 to 5 cubes; 5 is enough.
- **The K–1 packet has no "find a trap row of four" problem**, though 2–3 P4 and 4–5 P3 do. K–1 meets traps only in rows of three (P3–P4) and then goes straight to the colour plan. A K–1 version ("Can you make a row of four where whoever goes first loses?", with blank 4-slot strips) would give the youngest children the same impossible-search experience before the coloured strips explain it. This is optional, since the packet already has enough work.
- **2–3 Problem 9 can be answered by copying.** The last row of P7 (3, 2, 1, 2, 2, 2) is a valid answer to P9. That is acceptable, but if the reviser wants P9 to be invention, replace the P7 six-row with a fifth row of four and keep six-rows for P9.
- **Sentences that restate a diagram.** "In each of these colored rows, the red towers and the blue towers have the same number of cubes" (2–3 P7, 4–5 P6) and the hypotheses in 4–5 P7 and P8 state facts the diagram already shows. I would keep them: they are the hypothesis of each problem, not narration. "Each box below shows a row of towers that can be on the strip at some point in a game on 2, 3, 6, 2, 1, 4" (4–5 P11) could be tightened to "In each box, write the most cubes the player whose turn it is can be sure of collecting from that row, in a game on 2, 3, 6, 2, 1, 4."
- **Physical materials are not part of this packet.** The outline's 25 mm slot strips (3, 4, 5, 6 and 8 slots, plain and tinted) still have to be made. An 8-slot strip is 200 mm long, which does not fit across a portrait Letter page inside 0.75 in margins, so it needs landscape or two joined halves. The tinted strips need the same printing decision as M1. This is for whoever prepares the session, not a change to these pages.

## Checked and fine (keep)

- **Sequence and the outline.** Every band plays on plain strips before any tint. Each band meets 1, 5, 1 as a trap. Every even-row problem sits before any odd-row colour problem. The outline's band emphases are all present: K–1 compares stacks, plays the grown-up and finds 1, 5, 1; 2–3 tests the plan against every reply (P6), breaks it on rows of five (P8) and finds equal-colour wins (P7, P9); 4–5 explains the plan (P5), handles odd rows (P7–P9) and fills a backward table (P10–P11).
- **The launch row.** 3, 1, 4, 2 is used only as the notation example and never as a task row.
- **Well-chosen contrasts.**
  - The K–1 P3 and 2–3 P3 rows of three mix losses, wins and (in 2–3) a tie, with near-misses such as 2, 6, 3 and 4, 6, 1.
  - 2–3 P8 and 4–5 P8 include 2, 1, 5, 1, 2: the first player loses 4–7 even though the red slots hold 9 cubes against 2. That is a vivid break of the plan on odd rows.
  - 4–5 P7 (blue > red, so the first player always loses) and P9 (equal, so the first player never wins) are true statements children can prove with the even-row plan. I checked them for every row of five with heights 1 to 6.
  - 4–5 P11's row has equal colour totals (9 and 9), yet the first player wins 11–7, which ties back to P6.
- **The 4–5 P11 triangle.** Totals ("most cubes … can be sure of") are a better entry point for children than the outline's margins, and the recurrence total − min(two smaller boxes) is left for the child to find. The box layout shows which boxes depend on which without arrows.
- **K–1 load.** K–1 gets the same ideas at a smaller scale and plenty to do: 7 problems over 6 pages. Every K–1 problem is one or two short sentences.
- **Rendering.** Diagrams match the source data on every page (I checked all tower heights and colours against `gen.py`). Slot 1 is red throughout, squares are square, there is no overflow, and the tight spots (the 8-slot strips above the ruled lines in 2–3 P5 and 4–5 P4) do not touch.

## Appendix: answer key from my independent solver

Results are first player – second player under best play (each player maximises their own cubes). "L"/"R" means taking the left or right end; red = slots 1, 3, 5, …

**K–1**
- P1: 5,2,1,4 → 7–5 (L; R ties 6–6). 1,5,2,3 → 8–3 (R). 2,4,3,1 → 5–5 tie (either end).
- P2 (unique winning first move): 2,1,5,3 L(2). 3,5,1,2 R(2). 1,1,5,2 L(1). 2,5,1,1 R(1). 5,1,3,2 L(5). 2,3,1,4 R(4); L only ties.
- P3: 1,5,1 2nd; 5,1,5 1st; 1,4,2 2nd; 3,4,2 1st; 2,5,2 2nd. Rule: the first player loses exactly when middle > ends combined, ties when they are equal.
- P4: with heights ≤ 5 there are 10 losing rows of three (1,3,1; 1,4,1; 1,4,2; 1,5,1; 1,5,2; 1,5,3; 2,4,1; 2,5,1; 2,5,2; 3,5,1).
- P5 (plan colour → grown-up wins): 1,1,5,2 red 6 v 3; 2,5,1,1 blue 6 v 3; 4,1,5,2 red 9 v 3; 1,4,2,3 blue 7 v 3.
- P6 (child first; plan colour): 3,1,2,5 blue 6 v 5 (best 7–4); 2,4,1,1 blue 5 v 3; 1,3,2,1,3,1 red 6 v 5; 2,1,1,3,2,2 blue 6 v 5.
- P7 (equal colours): 2,1,2,3 win 5–3 (take 3); 1,3,4,2 tie 5–5; 4,1,2,5 win 7–5 (take 5).

**Grades 2–3**
- P1: 5,2,1,4 → 7–5. 2,6,3,4 → 10–5. 2,4,3,1 → 5–5.
- P2: 2,1,5,3 L 7–4. 3,6,1,2 R 8–4. 1,4,6,2 L 7–6. 4,5,3,3 R 8–7. In each row the other move loses.
- P3: 1,5,1 second; 5,1,5 first; 2,6,3 second; 3,4,2 first; 2,5,3 no difference; 4,6,1 second.
- P4: no such row (checked for heights 1–6 on rows of four; the colour plan proves it for any heights).
- P5: 1,2,5,1,3,2 red 9 v 5; 3,1,1,4,2,2 blue 7 v 6 (best play 8–5 starts with the red 3); 1,2,3,1,2,1,3,2 red 9 v 6.
- P6: 2,4,1,1,3,2: blue 7 v red 6, start at slot 6; exactly 4 games, listed under M6, each 7–6.
- P7: 2,1,2,3 → 5–3. 1,3,4,2 → 5–5. 4,1,2,5 → 7–5. 2,4,5,3 → 7–7. 3,2,1,2,2,2 → 7–5 (take 3).
- P8: 2,1,5,1,2 → 4–7. 4,1,1,1,4 → 6–5. 1,4,2,4,1 → 4–8. 1,2,4,2,1 → 5–5.
- P9: 1,974 of the 4,332 equal-colour rows of six with heights 1–6 are first-player wins.

**Grades 4–5**
- P1: 2,1,5,3 → 7–4. 4,6,2,3 → 9–6. 1,4,6,2 → 7–6. 2,4,3,1 → 5–5. 4,5,3,3 → 8–7. 6,2,1,5 → 8–6.
- P2: 1,5,1 → 2–5. 5,1,5 → 6–5. 2,6,3 → 5–6. 3,4,2 → 5–4. 2,5,3 → 5–5. 6,1,2 → 7–2.
- P3: none.
- P4: as in 2–3 P5.
- P6: 2,1,2,3 → 5–3. 1,3,4,2 → tie. 4,1,2,5 → 7–5. 2,4,5,3 → tie. 3,1,1,3 → 4–4. 6,2,1,5 → 8–6.
- P7 (all second-player wins): 1,4,2,4,1 → 4–8. 2,3,1,5,2 → 5–8. 3,5,2,4,1 → 6–9. 1,3,3,3,1 → 5–6.
- P8: 4,1,1,1,4 → 6–5. 1,2,4,2,1 → 5–5. 2,1,5,1,2 → 4–7. 4,2,1,2,4 → 7–6. 4,1,6,2,3 → 7–9.
- P9: no. Whatever end the first player takes is red; the second player then collects every blue-slot tower, so the first player gets at most the red total. Checked for every row of five with heights 1–6.
- P10: 3,1,4,1,5 → take 5, tie 7–7. 2,6,3,1,4 → take 4, win 9–7. 5,2,6,1,3 → take 5, lose 8–9 (taking 3 loses 6–11).
- P11 (most cubes for the player to move), from the bottom row up:
  - Single towers: 2, 3, 6, 2, 1, 4
  - Pairs: 2,3 = 3; 3,6 = 6; 6,2 = 6; 2,1 = 2; 1,4 = 4
  - Threes: 2,3,6 = 8; 3,6,2 = 5; 6,2,1 = 7; 2,1,4 = 5
  - Fours: 2,3,6,2 = 8; 3,6,2,1 = 7; 6,2,1,4 = 8
  - Fives: 2,3,6,2,1 = 7; 3,6,2,1,4 = 9
  - Whole row: 2,3,6,2,1,4 = 11 (the first player wins 11–7 by taking the 4; taking the 2 ties 9–9)

The outline's counts also check: among the rows of five with heights 1–4, the first player loses 143 and ties 147, and no even row of 2, 4, 6 (heights 1–4) or 8 towers (heights 1–3) is a first-player loss.
