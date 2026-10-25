# Review of the facilitator guide: Poisoned cookie (draft v1)

Reviewer stage. I did not write the guide, and I edited neither the guide nor the student pages.

## What I checked

- I rendered all 6 guide pages, plus the final student pages: K–1 (6 pages), grades 2–3 (5) and grades 4–5 (6). I read every page, and I re-rendered the guide's small diagrams at 220 dpi. The guide recompiles from `draft/src/facilitator.tex` with no overfull, underfull or other warnings, to 6 pages.
- I recompiled the three student `.tex` files in a scratch folder. Every page is pixel-identical to the final PDFs, so board shapes read from the `.tex` are the shapes children see.
- `review-guide-check/review_check.py` reads every board from the TikZ coordinates in the final `.tex` files. It records page, problem, cell size, and whether each drawing is a play board or a colouring grid. It does not import `chomp.py` or `check_guide.py`. It solves Chomp with its own cell-set solver, cross-checked by a row-tuple solver, and then re-derives every answer and general claim the guide prints:
  - every X and circle in the K–1 key;
  - all three refutation lists, for (3,2), (4,2,2) and the 10 losing first bites on 3×4;
  - the 9 + 1 second-player boards inside 4×4, with the flip pairs;
  - the 5 three-row second-player boards inside 3×5, and the 5 more inside 3×7;
  - the 4–5 Problem 2 labels in page order;
  - the (4,4,3) reply and the (3,1,1) argument;
  - 3×5, 3×6, 3×7, 3×8 and 4×5;
  - the two-row rule up to rows of 30 and the L-shape rule for arms up to 11;
  - the uniqueness claim for every rectangle with sides 2–9 and every 2×n and 3×n up to n = 24;
  - the tempting 3×n pattern, which fits 3×4 to 3×8 and fails at 3×9 with (3,7);
  - the launch counts (six counters, then four).

  The output is in `review-guide-check/review_check.txt`. **Every printed answer and every computed claim is correct.**
- I checked every problem number, page number, board size and count of grids against the PDFs. For example: 9 grids in K–1 P6, 6 in 2–3 P7, 12 in 4–5 P5, 19 boards in 4–5 P2, 25 mm cells on K–1 pages 1–5 and on the 4–5 page-6 3×6 board, and 17 cookies plus the poison as the largest built board. All of them agree with the final PDFs.
- I compared the guide with the Week 98 model guide and with `worksheet-workflow/context.md`, which gives the group, the staffing and the shape of the hour.

**Verdict.** The guide is mathematically sound and keyed to the final pages. The overview meets the theorem-first rule well. There are no must-fix findings. The should-fix items are usability problems. The most important is that the hour plan does not match this group's actual hour.

---

## Must-fix

None. No answer is wrong, no "find all" list is incomplete, no general claim is false, and nothing is keyed to an earlier draft.

## Should-fix

**S1. The first-hour plan conflicts with the group's real hour (page 2, "A first hour").**
- The guide plans "about 45 minutes of work and 5 minutes to share" after a 5-minute launch.
- `context.md` gives this hour as 5 minutes of running around, then the launch, then 35–40 minutes at the tables, then a few minutes of sharing. The guide never mentions the movement opening; the Week 98 model guide says "Launch after the movement opening".
- So every first route is planned for 5–10 more minutes than exist. No problem has a suggested time, although AGENTS.md "Make activities usable" asks for timing.
- The routes are long for 35–40 minutes:
  - Grades 4–5 Problems 1–4 include a 19-board classification and two general explanations.
  - Grades 2–3 Problems 1–5 include the two-row rule and two explanations.

*Fix:* Say "after the five-minute movement opening and five-minute launch, about 35–40 minutes at the tables". Give rough minutes for each first route, and mark a core that ends the hour comfortably. For example:
- K–1: Problems 1–3, with 4 if time.
- Grades 2–3: Problems 1–3, with 4–5 as the continuation.
- Grades 4–5: Problems 1–3, with 4 as the continuation.

The exact choice is the writer's. Whatever it is, it should fit 35–40 minutes.

**S2. "L" means both a losing board and an L-shaped board (pages 1, 4, 5).**
- The overview defines italic *L* as "loses for the player to move" (page 1) and in the next paragraph states the "L shapes" theorem.
- 2–3 Problem 1 then says "each leaves an L board" (page 4). Two of the boards left, (2,1) twice, are L-shaped; the third, (3,2), is not.
- This is the same collision that made the page reviewers remove "L position" from Ana's argument, because it flipped the answer. An adult who repeats "an L board" to a child brings it back.

*Fix:* In prose, write "losing board" or "a board that loses for the player to move". Keep W/L only where 4–5 Problem 2 uses the letters (page 5). On page 1 this means "a board is *losing* if every bite leaves a winning board…" and "(3,1,1) loses for the player to move". On page 4 it means "each leaves a losing board".

**S3. Unpiloted predictions are written as observations (pages 3–4).**
- "Children usually find it by losing first" (K–1 P2).
- "Children explain with copying" (K–1 P3).
- "Children often try the top-right cookie" (2–3 P6).

The guide itself says the pages are unpiloted (page 2, Status). AGENTS.md asks for observations to be kept separate from hypotheses.

*Fix:* Use "may": "Children may find it by losing first…", "A child may explain with copying…", "A child may try the top-right cookie first; its answer is (2,3)."

**S4. The materials leave out what the colouring problems need (page 2, "Per pair").**
- K–1 Problem 6 says "Color each board you find on a grid".
- 2–3 Problem 7 says "Color each one you find on a grid".
- The materials list "pencils" only.

*Fix:* Add "crayons or coloured pencils (K–1 and grades 2–3)" to the per-pair list.

**S5. The split suggested for 4–5 Problem 2 works against working backward (page 2, "A first hour"; page 5, Problem 2).**
- "Partners splitting Problem 2's boards" can give one child the large boards in rows 1–2. That child cannot label them until the small boards in rows 3–4 are labelled.
- The key itself says "working backward means starting at the end".

*Fix:* Say "label the last row together, then split the rest and check each other's labels by playing". Alternatively, split by roles, one labelling and one testing.

**S6. The first-hour job of the 4–5 adult, and the trio, are not described (page 2, Staffing).**
- Staffing gives the 4–5 adult only Problem 5's bookkeeping and reading Ana's argument. Both of those are in the return visit (page 2, "A first hour").
- The 4–5 table is a pair plus a third child (`context.md`), and the guide never says what the third child does.

*Fix:* Add one sentence. In the first hour, the adult plays against claimed strategies and checks Problem 2 labels by playing. The third child plays the other side against a claimed strategy or acts as referee for the card, and the roles rotate.

## Minor

**M1. The launch does not say which board the demonstration game uses, or what children will look for (page 2, Launch step 3).**
- "Two children play one game to the end" does not name the board.

*Fix:* Write "on the rebuilt 2 by 5". Close with a neutral goal such as "Today you'll look for bites that make sure you win", which reveals no answer.

The launch otherwise meets the rule. It is brief and concrete, and children handle the counters first. The 2×5 board is no problem's task. Its second bite contrasts with the pictured one, and its worked visual shows input, card and output. It states neither the theorem nor any answer.

**M2. The K–1 key, the parent's section, uses adult notation (page 3).**
- Problem 6 says "(3,2) and (4,3) follow the two-row rule". The row-length notation is defined only in the overview.
- The check pictures use 2.4 mm cells. The parent compares them with coloured 14 mm grids.

*Fix:* Write "the two two-row boards". Draw the Problem 6 check pictures at about 4 mm per cell; there is room on the page.

**M3. Two hints are procedures, not questions (page 3, K–1 P3; page 4, 2–3 P6).**
- "Put a finger on each arm. Which is longer?" points straight at the key feature.
- "Try the square trick and the two-row trick. What does your partner do?"

*Fix:* "Is there anything different about the two boards?" and "What happens if you use a trick that worked before?"

**M4. Winning bites are listed for only some W boards in 4–5 Problem 2 (page 5).**

An adult checking a child's W for (3,3,1), (3,2,2), (3,2,1), (3), (2), (1,1,1) or (1,1) has no listed bite.

*Fix:* Add one line, each verified by `review_check.py`:
- (3,3,1): (2,2) or (1,3)
- (3,2,2): (2,2) or (3,1)
- (3,2,1): (1,3), (2,2) or (3,1)
- (3) and (2): (1,2)
- (1,1,1) and (1,1): (2,1)

**M5. The guide does not give print totals (page 2, "What to print").**

A parent preparing alone has to work out the numbers.

*Fix:* Add one line: 4 K–1 packets, 4 grades 2–3 packets, 3 grades 4–5 packets, and 3 board sets. Each board set is K–1 pages 2, 4 and 5 plus grades 4–5 page 6, one for each older pair or trio. That makes about 74 single-sided pages.

**M6. "Play starts on a rectangle" (page 1, The game) does not match the pages.**

K–1 P1 and P3, 2–3 P1 and much of 4–5 start on L shapes or staircases.

*Fix:* "A game usually starts on a rectangle; the pages also start from other boards."

**M7. Brevity: the guide spills onto a mostly empty page 6 (9 lines).**

Trimming the following would bring it to 5 pages, like the Week 98 model:
- "each the only winning bite" appears about ten times (pages 3–5). State once: "Every winning bite listed is the only one on its board."
- 2–3 P3's "Why" restates the two-row reply rule from Theorem 2 and the K–1 adult strategies. Refer to the overview, as 4–5 P4 already does.
- The K–1 per-problem text for P2, P4 and P5 repeats the answer pictures.
- The K–1 P2 extension ("try it on the 2×6 board of Problem 5") is simply the next problem.
- The Sources paragraph cites `check_guide.py`, a path in this temporary run that will not travel with the guide. Write "checked by computer; script kept with the source".

## What works and should be kept

- **The overview is a model of the theorem-first rule.**
  - Strategy stealing has a followable proof, with its assumptions stated. The note that "one cookie lies in every bite" holds *exactly* for rectangles explains where the argument stops.
  - The limits are stated: the argument names no bite, only "the top-right bite or the reply that beats it".
  - The L-shape, square and two-row strategies come with reply rules that work at every size.
  - Computed facts are kept apart from theorems, with "do not tell children the bite is always unique".
  - The 3×9 trap for the tempting three-row pattern is included.
  - Experiment, conjecture and explanation are separated cleanly, and the band map is brief.
- **The K–1 adult strategies in plain words, with the picture key.** They give the non-mathematician parent what is needed to play the other side without choosing bites for the children.
- **The refutation tables:** (3,2) in 2–3 P1, (4,2,2) in 2–3 P6, and the full ten-bite table for 4–5 P5. Also "a full answer covers every kind of reply, not every reply" in 4–5 P4.
- **4–5 Problem 6:** "the stolen move is visible", the 2×n case as "the other case", and especially "'It is not a rectangle' is not yet the step; ask which sentence fails."
- **Status and print mapping:**
  - the honest list of what is physically untested, including the card on counters, the corner placement and borrowed boards;
  - "No separate board sheet exists", with the exact pages to use as boards, including 3×6 standing in for 3×4 and 3×5;
  - "an adult choosing bites is a signal to return to smaller boards".
- **The launch:** a non-task 2×5 board, a contrasting second bite, and a comment on legality only. Keep it with the M1 touch.
- **The closing list of what to record** once the activity is piloted.
