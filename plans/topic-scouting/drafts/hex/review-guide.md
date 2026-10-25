# Review: Hex facilitator guide, draft v1 (`draft/facilitator.pdf`, 7 pages)

Adversarial review. I did not write the guide or the student pages, and I did not edit either.

## What I checked

- **Pages read.** I rendered and read all 7 guide pages and all 23 student pages: K–1 has 6, grades 2–3 has 8 and grades 4–5 has 9, one of them landscape. I zoomed in on every guide figure: the launch panels, the 2–3 Problem 5 answer, the four 2–3 puzzle boards, the 3×3 openings and the two boundary paths.
- **Board data.** I read the board data from the student source, `plans/topic-scouting/drafts/hex/src/build.py`, and checked the drawn positions against the renders.
- **Rebuild.** I rebuilt the guide from a copy of `draft/src/` (`build.py`, which also runs `check_guide.py`). The result is byte-identical to `draft/facilitator.pdf`, with no overfull or underfull boxes and no check failures.
- **Answers.** I re-derived every answer with my own code, not the writer's `check_guide.py`:
  - `review-guide-check/hexcheck.py`: full-board enumeration, the square-board counts, the fewest-blocker searches, and an exact game solver for 3×3, 4×4 and 3×4 boards.
  - `review-guide-check/walkcheck.py`: the boundary path. Its border colours are taken from the drawing code in `hexgeom.py`.
  - Both scripts end with ALL OK.
- **Comparison.** I compared the guide with `week-98-facilitator.pdf`, the outline, both page reviews and the README entry.

**Verdict.** I found no must-fix problem:

- Every printed answer, count, coordinate and figure is correct for the final pages.
- Every problem number, page number, board size and page count matches the final PDFs. The guide is keyed to the revised pages, not to the draft the reviews describe. For example, K–1 Problem 6 now asks "Can Red always win?", grades 2–3 has 8 problems and grades 4–5 has 11.
- The overview is theorem-first and meets AGENTS.md.
- The launch is concrete, uses a board size no problem uses, and gives away neither the theorem nor any answer.

The findings below are a gap in one explanation, a missing prerequisites statement, and wording and usability points.

## Must-fix

None.

## Should-fix

**S1. Grades 2–3 Problem 6, top game: the follow-up strategy covers only two of Red's replies (guide page 4).**
- Quoted: "Then Blue wins: whichever of (3,3) and (4,3) Red takes, Blue takes the other, and then has two ways to the right edge, (3,4)/(4,4) after (4,3) or (2,4)/(3,4) after (3,3)."
- The answer (yes, only at (4,2)) is correct. But after Blue's (4,2), Red's most natural reply is (3,4), the hexagon shared by both of Blue's routes, or else (2,4) or (4,4). The text gives the adult no answer for these. If Red has taken (3,4), the stated "two ways (2,4)/(3,4)" no longer exists.
- My solver: after Red (3,4), Blue wins only with (3,3), (4,3) or (4,4). After any Red move other than (3,3) or (4,3), Blue's (3,3) and (4,3) both still win.
- Fix: add one sentence. "If Red plays anywhere else, for example (3,4), Blue takes (3,3). From there Blue reaches the right edge at (2,4), or through (2,3) to Blue's (1,4)."

**S2. No prerequisites statement (guide pages 1–2).**
- AGENTS.md ("Level by prerequisites", "Make activities usable") asks for the reading and arithmetic requirements and the reasoning involved.
- The band map says only "K–1 (adult reads)". The guide says nowhere that no arithmetic beyond counting to about 25 is needed, nor what each band reads or writes.
- It also does not name the escalating reasoning demands:
  - tracing a bending chain (all bands);
  - looking two moves ahead (K–1 P6; 2–3 P6–P8; 4–5 P3, P9);
  - sustaining a 23-to-26-side pencil path on 16 mm boards (4–5 P6–P7);
  - argument by contradiction (4–5 P10).
- Fix: add two or three sentences to the band map or to Staffing. For example: "Prerequisites: counting only. K–1 reads nothing; grades 2–3 read one-to-three-sentence problems with help and write short reasons (P3, P4); grades 4–5 write explanations (P5, P8–P10). The demand grows from tracing chains, to looking two moves ahead, to proof by contradiction."

**S3. Unpiloted predictions are stated as observations (guide pages 3, 4 and 5).**
- K–1 Problems 2, 3 and 5: "Children often notice: 'When I stop Red…'".
- 2–3 Problem 8: "…lose, which surprises children".
- 4–5 Problem 2: "Children usually try, fail and start explaining".
- The Status paragraph rightly says nothing has been piloted. AGENTS.md asks to keep observations separate from hypotheses.
- Fix: "Children may notice…", "which may surprise children", "Expect children to try, fail and start explaining…".

**S4. The Sources paragraph overclaims (guide page 6).**
- Quoted: "every statement here is proved in the overview or checked by `check_guide.py`."
- Several background statements are neither proved nor computed, and no source was consulted for them:
  - that Hex is equivalent to the Brouwer fixed-point theorem (Gale 1979);
  - "computers have found strategies only on small boards" and "11×11 is unsolved";
  - that the swap rule gives the second player the win;
  - the general claim about unequal boards (only the 3×4 case is computed).
- Fix: "Every answer and count is proved here or checked by `check_guide.py`. The background facts (the Brouwer equivalence, that 11×11 is unsolved, the swap rule, unequal boards) follow the outline and general knowledge and were not checked against a source."
- Optional: Gardner's "The Game of Hex" is, I believe, chapter 8 of *Hexaflexagons and Other Mathematical Diversions*. Add the chapter number only after confirming it in the book.

**S5. The fill problems are a different action from the game, and nothing tells the K–1 adult so (guide page 2 Staffing, or page 3 K–1 Problems 2, 3, 5).**
- The launch teaches "one counter per turn" for the game. K–1 Problems 2, 3 and 5 then ask the pair to fill the board freely.
- A non-mathematician parent may have the children keep alternating turns as opponents, or keep the colour counts equal. That turns a cooperative attempt to beat the theorem into a game.
- Fix: one sentence in the K–1 notes. "In the fill problems nobody takes turns: the pair works together and may use any number of each color."

## Minor

1. **Materials (page 2).** Quoted: "The fullest boards take 16 counters (K–1 4×4) or 25". The 7×7 board (4–5 Problem 11) has 49 hexagons. The per-pair supply still suffices, because a full 7×7 game uses at most 25 red and 24 blue, so say that instead. Separately, the README's Hex row says counters "no wider than 24 mm" and the guide says 20 mm. The guide's figure is the safer one; record it in the README when the week is filed.
2. **Continuations (page 3).**
   - Grades 2–3 trying the boundary path or the extra counter needs spare copies of grades 4–5 pages 5–7, plus colored pencils at the 2–3 table. Neither Printing nor Materials lists them.
   - The 3-rows-by-4-columns board is not printed. Say how to make one: "fill the bottom row of a 4×4 board with red counters; it then counts as part of Red's bottom edge."
3. **Overview, limits of Theorem 3 (page 1).** Say which step fails on unequal boards: step (b), because no reflection swaps the colors. Note that Theorem 1 still holds on any n-by-m board. That one line is the point of the 3×4 continuation, and it matches the Poisoned cookie draft's "which step breaks" question.
4. **K–1 Problems 1 and 4 (page 3).** "Starting in the middle wins with good play (Problem 6)." Add "keep this for Problem 6", so that the volunteer does not give the answer away during the first games.
5. **Status (page 2).** "(especially on the 7×7 landscape page and the launch board)": both boards use the same 24 mm hexagons as every other play board, so "especially" is unexplained. Name the actual worry, which is that a printer may scale the landscape page, or drop "especially".
6. **Preparation (page 2).** The 45 minutes leaves out buying the counters. Add "order about 150 red and 150 blue 3/4-inch bingo chips ahead of time".
7. **Brevity.** Three cuts would help without losing substance:
   - The Menger sentence in Theorem 2 (page 1). The 2–3 Problem 5 answer already gives the six-route certificate.
   - The "Computed facts" restatement of the 3×3 openings (page 1). It repeats 2–3 Problem 8.
   - The second statement of strategy stealing in 4–5 Problem 10 (page 6). It could point to Theorem 3 and keep only the children's version and the hints.
   - Otherwise the guide is dense rather than padded. There is no generic encouragement and no narration of the pages beyond the definitions adults need.

## Point-by-point against the brief

1. **Correctness.** Everything I checked matches my own code:
   - Full boards: 3×3 (512) and 4×4 (65,536) each have exactly one winner, split 256/256 and 32,768/32,768.
   - 4×4 square board: 21,150 fillings with no winner under side contact, and 21,150 with two winners under corner contact. The checkerboard does both.
   - Fewest blockers: 3, 4 and 5, with 8, 20 and 48 minimal sets. Every minimal set is a blue chain.
   - 2–3 Problem 5: 6 is the minimum, there are exactly 4 optimal sets, all four contain (4,1), (4,2), (5,2) and (5,3), and the four completions are those the guide lists. The drawn answer blocks Red. The six listed red routes are real routes and share no empty hexagon.
   - 3×3 openings: Red wins at exactly (1,3), (2,1), (2,2), (2,3) and (3,1). Against each of the four losing openings, Blue's only winning reply is the middle. Every case reply in the 2–3 Problem 8 analysis wins, and after Red (2,1), Blue (3,1), Red's only winning answer is (2,3).
   - K–1 Problem 6: yes (centre), no (sharp corner).
   - The four puzzle games:
     - Answers: yes only at (4,2); no; no; yes only at (3,2).
     - P6 bottom: Red has exactly two one-move wins, (3,1) and (3,2).
     - P7 bottom: both "tempting wrong moves" lose as stated.
   - 4–5 Problem 9:
     - Red's only winning move is (2,3), and 12 hexagons are empty.
     - With an extra red counter on any one of them, Red still wins: at (2,3), or with any move if the extra counter is at (2,3).
     - With Blue to move, Blue's winning moves are exactly (1,3), (1,4), (2,3), (3,2) and (3,3).
   - Boundary path: board 1 ends at the bottom-left corner after 23 sides, and board 2 at the top-right after 26. On both boards, sides 7 and 8 run along the left edge beside (3,1). The guide's red chain on board 1 lies entirely beside the path, and its blue chain on board 2 is a valid chain. On every 2×2, 3×3 and 4×4 coloring, the path ends bottom-left exactly when Red has a chain and top-right exactly when Blue does, and never bottom-right.
   - Continuations: the winning 4×4 first moves are exactly (1,4), (2,3), (3,2) and (4,1). On the 3×4 board, Red wins moving second.
   - Reflection: the transpose preserves adjacency, which justifies step (b).
   - The overview's proofs are correct: the crossing argument, Gale's path with its uniqueness, termination and "same hand" step, the slanted-line lower bound, and strategy stealing with the occupied-hexagon case.
   - The only gap is the explanation in S1.
2. **Agreement with the pages.**
   - All 7 K–1, 8 grades 2–3 and 11 grades 4–5 problem numbers and page numbers match.
   - Board sizes match: 24 mm play boards, the 7×7 also at 24 mm, 13 mm recording boards and 16 mm path boards.
   - The page counts (6, 8 and 9), the landscape page 9 and the drawn positions all match.
3. **The overview.**
   - It states three theorems with assumptions and limits: a full board only; three hexagons at a corner; the square-board counterexamples; the swap rule; unequal boards.
   - It gives a proof idea an adult can follow for each.
   - It separates experiments, conjectures and explanations, and maps the bands, all before any solution.
   - It meets the standard. The only small addition is minor item 3.
4. **The launch.**
   - It is brief, five minutes, after the movement opening, and lets children handle the counters first.
   - It uses a 6×6 board that no problem uses.
   - It has three labelled panels (input, one step, output). The step shows the sideways move children misread.
   - It ends on the page-1 example, so the launch and the shared rules match.
   - It explicitly withholds the no-draw theorem and any first-move advice. It reveals no answer.
5. **Usability.**
   - Staffing is realistic and matches the current group.
   - There is a 35–40-minute first route per band, with return visits.
   - Hints are questions.
   - Materials and printing match what the pages need, apart from minor items 1 and 2.
   - Gaps: S2 (prerequisites) and S5 (fill versus turns).
6. **Brevity.** Seven pages, including the launch-board page. That is within the model guides' range, and the density is like Week 98's. Small cuts are in minor item 7.

## What works and should be kept

- **The overview is a genuine theorem-first page.** It gives both halves of the no-draw theorem with real proofs, and the square board serves as the limit case in both directions. It sets out strategy stealing in four steps, including the occupied-hexagon case and the reflection that makes a second-player strategy work for either color. It distinguishes computer checks ("settle small boards") from proofs.
- **The K–1 section is in plain words, with no coordinates, written for a non-mathematician.** It says outright that Problems 2, 3 and 5 cannot be done, says how to respond to "I can't", says how to check a bending chain, and gives a pair strategy the adult can actually play in Problem 6.
- **The "find all" answer is complete and shows why.** The 3×3 openings use the half-turn reduction to five cases, with a short winning or losing line for each. Every line checks out.
- **Every minimum comes with a certificate.** Slanted lines give the lower bound in K–1 Problem 7 and 2–3 Problem 4, and six disjoint routes do so in 2–3 Problem 5.
- **The launch** has three panels on a board no problem uses, ends on the page-1 picture, and lists what not to say.
- **The staffing rule** "an adult choosing [moves] means the board is too big" is good, and so are the pooling advice (split the nine openings; pool the coloured path boards) and the advice to show the path rule on the launch board, not on a task board.
- **Status and sources are honest.** The guide says what is physically untested and says plainly that no source was consulted (apart from the overclaim in S4).
- **The build is reproducible.** It runs its checker and refuses overfull boxes.
