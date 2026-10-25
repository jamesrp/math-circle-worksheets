# Review: facilitator guide for "Towers from either end", draft v1

Reviewed: `draft/facilitator.pdf` (6 pages) and its sources `draft/src/facilitator.tex` and `draft/src/solutions.tex`. I compared it with the final student pages `k-1.pdf` (7 pages, Problems 1–8), `grades-2-3.pdf` (7 pages, Problems 1–9) and `grades-4-5.pdf` (6 pages, Problems 1–11), the outline, both page reviews, `worksheet-workflow/context.md` and the Week 98 model guide.

## Method

- I rendered every page of the three student packets and the guide and read them.
- `review-guide-check/parse_pages.py` reads every tower picture and number strip in the final student `.tex` sources (cubes per slot, slot tint, page). Every row the guide cites matches what is printed, in the printed order.
- `review-guide-check/verify_guide.py` is my own solver; it does not use the writer's `check_guide.py`. It re-derives every score, alternative first move, colour total, plan game list, count and general claim in the guide. **All of them check.** That covers:
  - all K–1, 2–3 and 4–5 answers;
  - the 10 losing rows of three with columns of five;
  - 625, 1,296, 1,024 (143 losses, 147 ties) and 1,974 of 4,332;
  - the four 2–3 Problem 6 games;
  - the 4–5 Problem 11 triangle;
  - the taller-end grown-up results (4–6 and 5–5);
  - the both-greedy 6–7 in 4–5 Problem 10.
- `review-guide-check/settle_check.py` and `prefix_rule.py` test two teaching remarks; see M1 and S2.
- I recompiled a copy of the sources. It builds with no overfull or underfull boxes, and its text is identical to `draft/facilitator.pdf`.
- I checked the two web sources. Science News: "no one has yet worked out an optimal strategy that works for any number of coins", plus the penny–nickel–penny examples and the Winkler attribution. Cut-the-knot: "the first player can guarantee at least a draw", 1, 5, 1 and 5, 1, 5, and Winkler in its references. The guide reports both correctly.

Every problem number, page number, picture description, board count (six K–1 drawing boards, six 2–3 Problem 6 grids, columns of five) and material count matches the final PDFs. Nothing in the guide is keyed to the earlier draft. The rows the revision replaced all appear in their final form:

- K–1 Problem 6 is the grown-up problem;
- 2–3 Problem 2 uses 2, 3, 1, 5;
- 2–3 Problem 7 uses 3, 2, 4, 5;
- 4–5 Problem 6 uses 4, 2, 1, 3;
- 4–5 Problem 10 uses 2, 1, 2, 5, 3.

## Must-fix

### M1. "Problem 3's rule settles" a row of four: false, and it would accept a wrong answer (page 4, 2–3 Problem 4; page 5, 4–5 Problem 1)

- **2–3 Problem 4:** "A candidate is checked by trying both first moves; after either one, the partner faces a row of three, which Problem 3's rule settles." Hint: "Which row of three does your partner face after each first move?"
- **4–5 Problem 1:** "Every first move leaves a row of three, so once Problem 2's rule is found it settles these rows."

The rule says who wins the row of three. It does not say who wins the row of four, because the first player already holds the tower taken.

- **A printed counterexample:** 4–5 Problem 1's own row 6, 2, 1, 5.
  - Taking the 6 leaves 2, 1, 5, and taking the 5 leaves 6, 2, 1.
  - By the rule, the partner (moving first on the row of three) wins both.
  - Yet the first player wins the row of four 8–6.
- **The same happens on 2, 4, 3, 1:** both rows of three are partner wins, but the row of four is a 5–5 tie.
- **How often:** of the 1,296 rows of four with heights 1 to 6, 876 would be wrongly classed as first-player losses by this check (`settle_check.py`).

This matters most in 2–3 Problem 4. That problem's whole point is that no losing row of four exists, and an adult following the guide's check would confirm a child's false candidate.

**Fix.** Replace both sentences with a check that adds the tower already taken. For example: "After either first move the partner faces a row of three. Find the totals on that row (play it out, or use Problem 3's reasoning: the mover gets the two ends if the middle is the tallest, otherwise the taller end plus the smaller of the other two), then add the tower the first player already took. On 6, 2, 1, 5 the partner wins 2, 1, 5 by 6 to 2, but the first player already holds the 6 and wins 8–6." Change the hint to "After each first move, how many cubes does each player end up with?"

### M2. The overview heading makes a false claim (page 1, first line)

"Mathematical overview: a colouring settles even rows; odd rows need working backward." The colouring does not settle even rows; it only guarantees the first player a tie or better. Theorem 1's own *Limits* sentence gives the counterexample: 2, 1, 2, 3 has equal colours but is a first-player win, 5–3. The heading is the one line every adult reads, and it states the wrong destination.

**Fix:** "Mathematical overview: on even rows a colouring guarantees the first player a tie or better; best play needs working backward."

## Should-fix

### S1. The first-hour routes give no priority or trim, and the band's centrepiece is last (page 3, "A first hour, by band")

The timings are untested, so this is a hypothesis about pacing, not a ban. Two things look heavy for 35–40 minutes.

- **K–1:** the route is Problems 1–4. That is six full games in Problem 1, six rows in Problem 2 with both partner replies tried, five rows of three, and then drawing. It may already overrun, and by design it never reaches the shaded strip.
- **Grades 2–3:** the route is Problems 1–4 (six games with totals, four rows with every reply, six rows plus a written rule, an open search), and only then the grown-up game in Problem 5.

A child who comes once may never meet the colouring, which is the band's main idea. An adult running late has no guidance on what to cut. The guide's reason for deferring K–1 Problem 6 (Problem 5's search should come first) is sound. It is compatible with a shorter route.

**Fix:** keep the routes, but add what to cut so each table can reach its grown-up game. For example:

- **K–1:** Problem 1 with one or two rows; Problem 2's first three rows; Problem 3; five minutes on Problem 5; then Problem 6 if 10 minutes remain. Save Problem 4 and the rest of Problem 2 for the return visit.
- **Grades 2–3:** Problem 1 with one row played twice; Problems 2 and 3; a short search in Problem 4; then Problem 5 for the last 10 minutes.

Alternatively, say plainly that the first hour is meant to stay on plain strips.

### S2. "Putting 1, 1 in front … is not a rule" is misleading in the task's context (page 5, 2–3 Problem 9)

Problem 9 asks for a row of six, and the guide suggests growing a winning row of four from Problem 7. For rows of four, putting 1, 1 in front of an equal-colour first-player win never failed in my search: 0 failures among the 168 such rows with heights 1 to 9 (`prefix_rule.py`). It does fail for longer rows. For example, 2, 1, 1, 2, 1, 1 is an equal-colour win by 2, but 1, 1, 2, 1, 1, 2, 1, 1 is a tie; 140 of the 1,974 winning rows of six fail.

An adult who tells a child "it is not a rule" when the child claims "I can always put 1, 1 in front of a four" is contradicting what the computer finds for every row we can test.

**Fix:** "It worked on every equal-colour winning row of four we checked by computer, but it can fail on longer rows (2, 1, 1, 2, 1, 1 wins, but with 1, 1 in front it only ties), so a child's claim still needs a reason." Or drop the remark.

### S3. Strip-making materials are incomplete, and the strips are a gap in the packet (page 2, "Strips" and "Per pair")

The guide says honestly that the packets include no strips. It then asks the volunteer to cut twelve 1-inch strips "from 1-inch grid paper" and colour them, but the materials list has no grid paper (or a printable source for it), scissors, or red and blue markers.

**Fix:** add "two sheets of 1-inch grid paper (print any free 1-inch grid at 100%; each sheet gives eight strips), scissors, a pink or red marker and a blue marker" to the preparation list.

Separately, this is a note for the organizer, not something the guide can fix: the outline called for printed strips (plain and tinted, 25 mm slots). A one-page printable strip sheet added to the packet set would remove 20 minutes of hand preparation and the risk of strips whose colours do not match the pages.

## Minor

1. **Print counts are ambiguous** (page 2, "What to print"). "One per child plus a spare (currently 4 K–1, 4 grades 2–3, 3 grades 4–5)": the numbers in brackets are the children at each table (`context.md`), so "plus a spare" means 5, 5 and 4 copies. Say "print 5 K–1, 5 grades 2–3 and 4 grades 4–5 packets".
2. **The Theorem 3 limits read as a contradiction** (page 1). The theorem says best play is always found by working backward, and the next sentence reports that "no general optimal strategy was known". Clarify: "working backward always finds best play, but takes a table; the sources know no shortcut rule for odd rows (Peterson: no one has 'worked out an optimal strategy that works for any number of coins')".
3. **K–1 Problem 5: "Problem 6 shows why"** (page 3). Problem 6 shows that the grown-up wins four rows going first; it does not show why. Say "Problems 6 and 7 let them meet the plan that explains it."
4. **Spelling** (throughout). The guide writes "colour/coloured"; the student pages write "colored" and "color", and Week 98 uses American spelling. Match the pages.
5. **Launch** (page 2).
   - Name who leads the launch (presumably the organizer) and who plays the child.
   - "Grades 2–3 and 4–5 write totals" fits the 2–3 game tables, but 4–5 Problem 1 asks for best-play totals, not a game record. Say "grades 2–3 write both totals".
6. **The grown-up's card** (page 2) does not say what to do when the colour totals are equal. No printed grown-up row has equal totals, but children may hand the adult their own row. Add: "If the totals are equal, take either colour; the plan then only promises a tie."
7. **"An adult who is choosing a child's moves should shorten the row instead"** (page 2). It is unclear how to shorten a printed row. Say "switch to a row of three or four".
8. **K–1 Problem 8** (page 4) needs looking two moves ahead. Mark it as the K–1 deep end, and give the parent the careful partner's reply on 1, 3, 4, 2: after the child takes the 2, the partner must take the 4. That reply is the only one that holds the tie; the other loses 4–6.
9. **4–5 Problem 4 has no hint** (page 5). The 2–3 Problem 5 hint, "Which slots did my towers stand on?", would serve.
10. **Brevity.**
    - The plan's rule is stated five times: Theorem 1, the card, 2–3 Problem 5 "How the grown-up chooses", the second sentence of 4–5 Problem 4, and 4–5 Problem 5. Cut the 4–5 Problem 4 sentence; the card covers it.
    - "Ties will happen often, which is why the tie choice is there" (K–1 Problem 1) narrates the page.
    - "Every printed score was recomputed for this guide by an independent script" (page 6) overstates: the script is the writer's own. Say "by a script".
11. **Preparation time** (page 2). The 40-minute estimate leaves out reading this six-page guide, about 20 minutes for a parent. Mention it, or say "plus reading this guide".

## What works and should be kept

- **The overview is genuinely theorem-first.**
  - Three stated theorems with proofs an adult can follow: the colouring argument; the odd-row transfer of the plan to the second player; the interval recurrence matched to the 4–5 triangle.
  - Explicit limits with concrete counterexamples: 2, 1, 2, 3 for "the guarantee is not best play"; 1, 2, 5, 2 for "take the taller end"; 4, 1, 1, 1, 4 against 2, 1, 5, 1, 2 for red > blue.
  - A complete proof of the three-tower rule, with its heights-at-least-1 assumption stated.
  - A clean paragraph that separates experiments, conjectures and explanations, and a band map before any solution.
- **The grown-up's card** gives the K–1 parent precomputed openings and scores. Its warning that the first two openings take the shorter end on purpose is exactly what a non-mathematician needs.
- **The launch** is short, uses the non-task example row 3, 1, 4, 2, demonstrates end-only moves and stack comparison, gives an input → one move → output picture, and shows the game that is also the worked record in 2–3 Problem 6. It reveals no theorem or answer and keeps the shaded strips hidden.
- **The two-set printing plan** is tied to exact pages and problems, so the tint stays a discovery. So is the staffing plan (play two pairs at once; adults read and check but do not choose moves).
- **The solutions are complete and correct.** They include the alternative-move scores children will actually meet, and several notes worth keeping:
  - the completeness argument for the four 2–3 Problem 6 games, with the red-plan extension;
  - the equal-colour tie rows for testing 2–3 Problem 9 claims;
  - the 4–5 Problem 10 greedy contrast;
  - the 4–5 Problem 11 link back to equal colours.
- **Hints are questions**, and discretionary "how do you know" follow-ups are kept in the guide.
- **The sources section** says what was and was not consulted. **"What to record"** separates observations from guesses.
