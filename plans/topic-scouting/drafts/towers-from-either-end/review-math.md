# Math review: Towers from either end, draft v1

Reviewer: independent math check (CRITIC-MATH stage). The draft was not edited.

## Method

- I wrote my own solver from scratch and did not use the author's `check.py` or `verify.py`. It uses the interval recurrence: margin(row) = max(left − margin(rest), right − margin(rest)). It also covers each first move separately, all outcomes reachable by any play, random-play tie probabilities, replies by a greedy opponent, and colour-plan game trees.
- Sanity check against the outline: rows 1, 5, 1 and 5, 1, 5 and 2, 1, 2, 3 come out as the outline says. For the 1,024 rows of five with heights 1–4 I get 734 first-player wins, 143 losses and 147 ties. Even rows of 2, 4 and 6 towers (heights 1–4) have no first-player losses, and none where best play falls below the colour difference.
- I parsed every tower and number strip from the `.tex` sources (cube counts per slot, slot tints, printed numbers) and compared them with the intended rows. I also rendered and looked at every page of all three PDFs.
  - Every drawn row matches its intended heights.
  - Tinted strips start at K–1 Problem 5, 2–3 Problem 5 and 4–5 Problem 4, after the plain-strip problems.
  - Every row described as equal, blue-heavier or red-heavier really is.
  - All heights are in 1–6, and K–1 heights are in 1–5.
  - The 21 boxes of the 4–5 triangle are exactly the 21 runs of consecutive towers in 2, 3, 6, 2, 1, 4.
- I checked the general claims the open problems rely on, over all heights 1–6:
  - No row of four is a first-player loss (0 of 1,296).
  - No row of five with equal colours is a first-player win (0 of 540).
  - Every row of five with more blue cubes is a second-player win (1,182 of 1,182).
  - The rule for rows of three (the first player loses if the middle tower is taller than both ends together, and ties if it equals them) holds for all 216 rows of three.

## Located problems

### 1. K–1, page 1, Problem 1: a tie cannot be recorded

- **Text:** "Play each row two times, taking turns to go first. Ring who won each game." Each game has a box offering only "1st  2nd".
- **Evidence:** The packet's own rules say "If the stacks are the same height, it is a tie," and two of the three rows tie often.
  - **Row 2, 4, 3, 1:** a tie (5–5) under best play, whichever tower the first player takes.
  - **Row 5, 2, 1, 4:** can end 6–6.
  - **Random play:** both of these rows tie in exactly 1/2 of games.
  - **Row 1, 5, 2, 3:** totals 11 cubes, so it cannot tie.

  A K–1 pair will very likely get a tie and have nothing to ring.
- **Smallest fix:** Add a third choice to each box: "1st  2nd  tie" (or "same"). Keeping the 2, 4, 3, 1 row is worthwhile, because a tie is a real outcome.

### 2. K–1, page 6, Problem 7 (also page 2, Problem 2): the opponent is not specified, and a weak opponent changes the answers

- **Problem 7 text:** "You go first on these colored rows. Which rows can you win? Ring them."
- **Problem 7 evidence:** The intended answer is rows 1 and 3. Best play gives 2, 1, 2, 3 → 5–3, 1, 3, 4, 2 → 5–5 (a tie), and 4, 1, 2, 5 → 7–5. That answer only holds if the second player plays well. Against a K–1 partner, row 2 can easily be won: take 2, partner takes 1, take 4, partner takes 3, for 6–4. Read naturally ("can you win"), every row can be won, and the tie row, which is the point of the problem, disappears.
- **Problem 2 text:** "You go first. Which tower should you take first so that you win? Ring it."
- **Problem 2 evidence:** Under best play each row has exactly one winning first tower. Against a careless partner, the other tower can also win. For example, on 2, 1, 5, 3: take 3, partner takes 2, take 5, for 8–3.
- **Smallest fix:** Name the opponent as the grown-up:
  - Problem 7: "You go first against the grown-up on these colored rows. Which rows can you win? Ring them."
  - Problem 2: "You go first against the grown-up. Which tower should you take first so that you win? Ring it."

  I checked that a grown-up who simply takes the taller end on every turn gets exactly the best-play results in all six Problem 2 rows and all three Problem 7 rows:
  - In Problem 2, the intended tower wins and the other tower loses or ties.
  - In Problem 7, the child can still win rows 1 and 3 by 2 and can at best tie row 2.

  So the parent volunteer needs no further strategy.

### 3. Grades 2–3, page 7, Problem 9: the answer is already printed on the previous page, and the wording does not ask for best play

- **Text:** "Make up a colored row of six where the red towers and the blue towers have the same number of cubes and the first player can win."
- **Evidence (the answer is already printed):** Problem 7 (page 6) prints the six-tower row 3, 2, 1, 2, 2, 2. Its colours are equal (red 3+1+2 = 6, blue 2+2+2 = 6), and best play gives a first-player win, 7–5. Copying it answers Problem 9.
- **Evidence (best play is not stated):** Problem 9 drops the "when both players play as well as they can" clause that Problems 7 and 8 carry. Read loosely, almost any row can be "won" against a partner who blunders. Under best play the task is real but very achievable: 1,974 of the 4,332 equal-colour rows of six with heights 1–6 are first-player wins.
- **Smallest fix:**
  - Take the six-tower row out of Problem 7 so that Problem 7 has only the four rows of four. Alternatively, keep it there and have Problem 9 ask for a row whose first player wins by more than 2.
  - Add the clause: "...and the first player wins when both players play as well as they can."

### 4. Grades 2–3, page 5, Problem 6: twice as many recording grids as games

- **Text:** "Try every way your partner can play, and write each game as the slot numbers in the order the towers were taken." The page has eight 6-cell grids.
- **Evidence:** On 2, 4, 1, 1, 3, 2 (red 6, blue 7) the plan player takes blue. Every one of the plan player's moves is then forced, because exactly one end shows blue each time. The partner chooses only on the row of 5 and the row of 3. That makes exactly 4 games:
  - 6-1-2-3-4-5
  - 6-1-2-5-4-3
  - 6-5-4-1-2-3
  - 6-5-4-3-2-1

  Taking red instead also gives 4 games. The page suggests 8, so a child who has found all 4 may keep hunting, or conclude they missed some.
- **Smallest fix:** Print 4 grids. If extra room is wanted, keep it unruled rather than as more numbered-looking grids.

### 5. Grades 2–3, page 2, Problem 2: every answer is the shorter end, which invites a false shortcut

- **Text:** "You go first on each of these rows. Find a first move that wins, however your partner plays after it. Ring that tower." The rows are 2, 1, 5, 3; 3, 6, 1, 2; 1, 4, 6, 2; and 4, 5, 3, 3.
- **Evidence:** The unique winning first move is the shorter end in all four rows:
  - 2, 1, 5, 3: slot 1, 7–4
  - 3, 6, 1, 2: slot 4, 8–4
  - 1, 4, 6, 2: slot 1, 7–6
  - 4, 5, 3, 3: slot 4, 8–7

  A child who notices this after two rows can ring the rest without playing. The pattern "take the smaller end" is false in general; for example, on 5, 1, 3, 2 only the taller end wins.
- **Smallest fix:** Replace one row, for example 4, 5, 3, 3, with 2, 3, 1, 4. There the taller end (slot 4) wins 7–3 and the shorter end only ties 5–5.

### 6. Grades 4–5, page 6, Problem 10: the "ring the best first move" part is solved by "take the taller end"

- **Text:** "For each row, ring the first player's best first move, and find who wins and by how many cubes." The rows are 3, 1, 4, 1, 5; 2, 6, 3, 1, 4; and 5, 2, 6, 1, 3.
- **Evidence:** The best first move is the taller end in all three rows:
  - 3, 1, 4, 1, 5: take 5, tie 7–7
  - 2, 6, 3, 1, 4: take 4, first wins 9–7
  - 5, 2, 6, 1, 3: take 5, second wins 9–8

  This is typical of rows of five. Among rows of five with heights 1–6 that have a unique best first move, the taller end is best in 4,114 and the shorter end in only 54. The "who wins and by how many" part is still substantial: in 2, 6, 3, 1, 4, greedy play by both sides gives 11–5, but best play gives 9–7.
- **Smallest fix:** Replace 2, 6, 3, 1, 4 with 2, 1, 2, 5, 3. Taking the 2 wins 7–6, and taking the taller 3 loses 6–7. This keeps the row's role (a first-player win) and gives the ring a real decision.

## Bands that otherwise check out

Apart from the items above, every problem in all three bands is correct. The answer key below was computed by my solver, and the scores are first player – second player under best play.

### K–1

| Problem | Verified result |
|---|---|
| 1 | Rows to play: 5, 2, 1, 4 is 7–5 (take 5); 1, 5, 2, 3 is 8–3 (take 3); 2, 4, 3, 1 is 5–5. See item 1. |
| 2 | Each row has a unique winning first tower: 2, 1, 5, 3 → slot 1 (7–4); 3, 5, 1, 2 → slot 4 (7–4); 1, 1, 5, 2 → slot 1 (6–3); 2, 5, 1, 1 → slot 4 (6–3); 5, 1, 3, 2 → slot 1 (8–3); 2, 3, 1, 4 → slot 4 (7–3; slot 1 only ties). The answers are a good mix of the shorter and the taller end. |
| 3 | 1, 5, 1: 2nd (2–5). 5, 1, 5: 1st (6–5). 1, 4, 2: 2nd (3–4). 3, 4, 2: 1st (5–4). 2, 5, 2: 2nd (4–5). No ties, so the 1st/2nd choice is complete. |
| 4 | Possible. Within the six-cube columns there are 20 such rows (middle taller than both ends together), for example 1, 3, 1, then 1, 4, 2, then 2, 5, 2. |
| 5 | Red–blue totals are 6–3, 3–6, 9–3 and 3–7. A grown-up using the colour plan wins every row, and the child can neither win nor tie. |
| 6 | Red–blue totals are 5–6, 3–5, 6–5 and 5–6. Taking the larger colour wins every row, so the child never loses. |
| 7 | Rows 1 and 3 are wins (5–3 and 7–5); row 2 is a tie (5–5). See item 2. |

### Grades 2–3

| Problem | Verified result |
|---|---|
| 1 | Rows to play. 2, 6, 3, 4 is 10–5 (take 4); the other rows are as in K–1. |
| 2 | Unique winning moves as listed in item 5. |
| 3 | second (2–5); first (6–5); second (5–6); first (5–4); no difference (5–5); second (5–6). The rule exists, and 3, 4, 2 rules out the tempting false rule "the tallest middle loses". |
| 4 | None exists. |
| 5 | Red–blue totals are 9–5, 6–7 and 9–6, so the grown-up wins every row with the plan. |
| 6 | The answer is no; see item 4. |
| 7 | 2, 1, 2, 3 is 5–3; 1, 3, 4, 2 is 5–5; 4, 1, 2, 5 is 7–5; 2, 4, 5, 3 is 7–7; 3, 2, 1, 2, 2, 2 is 7–5. |
| 8 | 2, 1, 5, 1, 2: second wins 4–7, although red has 9 to blue's 2. 4, 1, 1, 1, 4: first wins 6–5. 1, 4, 2, 4, 1: second wins 4–8. 1, 2, 4, 2, 1: tie 5–5. The plan does not settle rows of five. |
| 9 | Possible; see item 3. |

### Grades 4–5

| Problem | Verified result |
|---|---|
| 1 | 2, 1, 5, 3: first by 3 (7–4). 4, 6, 2, 3: first by 3 (9–6). 1, 4, 6, 2: first by 1 (7–6). 2, 4, 3, 1: tie (5–5). 4, 5, 3, 3: first by 1 (8–7). 6, 2, 1, 5: first by 2 (8–6). |
| 2 | second (2–5); first (6–5); second (5–6); first (5–4); tie (5–5); first (7–2). The rule is the middle compared with the sum of the ends. |
| 3 | None. |
| 4 | Red–blue totals are 9–5, 6–7 and 9–6, so the grown-up never loses. |
| 5 | The claim is true. |
| 6 | 2, 1, 2, 3: first by 2. 1, 3, 4, 2: tie. 4, 1, 2, 5: first by 2. 2, 4, 5, 3: tie. 3, 1, 1, 3: tie. 6, 2, 1, 5: first by 2. |
| 7 | Second wins all four: 4–8, 5–8, 6–9, 5–6. The intended explanation (both ends are red; after the first move the second player can take every blue tower) is sound. |
| 8 | 4, 1, 1, 1, 4: first by 1. 1, 2, 4, 2, 1: tie. 2, 1, 5, 1, 2: second by 3. 4, 2, 1, 2, 4: first by 1. 4, 1, 6, 2, 3: second by 2 (7–9). A good mix showing that red > blue settles nothing. |
| 9 | No; the same argument as Problem 7 shows the second player always gets at least half. |
| 10 | See item 6. |
| 11 | Most cubes for the player to move, rows of length 6 down to 1. Length 6: 11. Length 5: 7, 9. Length 4: 8, 7, 8. Length 3: 8, 5, 7, 5. Length 2: 3, 6, 6, 2, 4. Length 1: 2, 3, 6, 2, 1, 4. The whole row is 11–7 with equal colour totals (9–9), a nice closing example. |
