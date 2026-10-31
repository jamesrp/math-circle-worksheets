# Review: Week 63 return-visit facilitator guide (Cards away from home), draft v1

I reviewed `draft/facilitator.pdf` (8 pages, about 4,900 words) and its source against the final student pages: K–1, 5 pages, Problems 1–8; Grades 2–3, 6 pages, Problems 1–9; Grades 4–5, 10 pages, Problems 1–13. I rendered and read every page of the guide and of the three packets, and zoomed in on the arrow and grid worked examples. I also read the outline, both page reviews, the draft's README entry, the base week's guide (W63-G-v4, 11 pages) and materials (W63-M-v3), and the Week 98 and Week 8 return-visit model guides. I did not edit the guide or the pages.

**How I checked.** I wrote my own scripts before opening the writer's `check_guide.py`.

- `review-guide-check/extract_pages.py` reads the boards and grids straight from the final PDFs: each crossed-out letter is assigned to the home below it by its coordinates, and each grey grid square to its card line and home column. Its output is in `extract_pages.out` and `pages.json`.
- `review-guide-check/check_answers.py` re-derives every answer the guide prints. It uses breadth-first search over swaps of any two cards (up to six cards), exact-length reachability up to 7 swaps, loops read card → home, every printed shortest swap word, totals, pairs and piles up to seven cards, every board and grid by filtering all rows, all 1,820 four-spot boards, rook-number sums and the guide's F(L, k) recursion against Kaplansky's formula. It asserts every list the guide prints. Output: `check_answers.out`, 121 checks, 0 failures.
- `review-guide-check/measure_boards.py` measures the home cells. They are 35 × 45 mm on K–1 pages 4–5 and Grades 4–5 pages 7–8, and 32 × 13 mm and 36 × 13 mm on Grades 2–3 pages 5–6. Output: `measure_boards.out`.

Afterwards I ran a copy of the writer's checker in `/tmp`, and it also passes.

**Verdict.** The mathematics is right throughout. Every answer, every "find all" list, every loop decomposition and swap word, the 24 hardest five-card rows, the 16 strip and 13 ring catalogs, the coefficient tables and the 1,820-board distribution check out. Every problem number, page number and board size matches the final PDFs, including the split of the old Problem 12 into Problems 12 and 13. Nothing contradicts the base week's guide or materials. The overview is theorem-first with real proofs, and the launch is brief and uses a non-task example. There is one must-fix, in the materials plan: as written it gives away the answer to two counting problems. The should-fix items are about the overview's account of what children should discover, a few explanations adults need, the parent's page, and age-fit details.

## Must-fix

### 1. The materials plan gives away K–1 Problem 5 and, for one pair, Grades 2–3 Problem 5 (p. 2, "Per table"; p. 3, K–1 Problem 5)

- **K–1.** The guide supplies "six counters no wider than 12 mm" per young table. Problem 5 asks: "Are there more counters, more outcome cards, or the same number?" The answer is six counters and six outcome cards. With exactly six counters on the table, children can answer by looking at the supply before placing anything. A missed match also shows up as a leftover counter, which gives the error away.
  - **Fix:** "a cup of 12–20 counters no wider than 12 mm per pair". Also give each pair its own cut A–C set: the base kit cuts five copies of materials page 2, so five sets exist. Change "the six small counters" on p. 2 to match.
- **Grades 2–3.** There is one uncut page 3 per middle table, and the guide says: "Stagger the middle pairs: one does swaps while the other marks, then swap." The second pair then gets a sheet with all 24 circles already drawn, so their Problem 5 ("How many circles are there in all? How many does each letter get?") is answered before they start.
  - **Fix, either of these:**
    - Print one uncut page 3 per middle pair. That makes four extra sheets, not three, so update "print the three extra uncut sheets" on p. 2.
    - Make Problem 5 a shared table task: one pair circles A and B, the other C and D, and they pool their totals. This also fits "children can share cases and pool".
  - The upper trio shares its single sheet as one group, so that table is fine.

## Should-fix

### 1. "What children discover" lists activities, not destinations (p. 1)

- **What it says now:** "K–1 acts out swaps, compares counters with outcomes and hunts on picture boards…" That describes what each band does. AGENTS asks the overview to say what children are meant to discover. The only line on levels of evidence is generic: "Experiments suggest a rule; a complete catalog settles a finite hunt…"
- **Fix:** replace the paragraph with three short band lines that name the destinations and which claims children can explain:
  - **K–1:** Two swaps are enough to leave three or four cards all away from home. Five cards need three, because two swaps touch only four cards; children can point to the untouched card. On the A–C outcome cards there are as many counters as outcome cards, two for each letter.
  - **Grades 2–3:** The hardest four-card rows need 3 swaps, never 4, and there are six of them. One swap brings two cards home only when they sit in each other's homes. The circles always total the number of outcome cards. The number of crossed-out cards does not decide the count. "No board gives 5" and "9 is the most" stay conjectures for children.
  - **Grades 4–5:** Fewest swaps = cards − loops, with parity. Totals and piles can be predicted without listing. The ±1 alternation is a conjecture unless the base week's recurrence is available. The strip and ring counts are found by listing, then by repaired overlap counts.
- **Also add one sentence on what is new since the first visit:** the arrows are the base week's page 7 arrows, which only children at the 4–5 table met; the exact piles contrast with the base week's overlapping home-groups.

### 2. The key lemma has no example an adult can follow (p. 1, "Fewest swaps"; p. 5, "To explain the lower bound concretely")

- **The gap:** The whole lower-bound proof rests on "A swap within one loop splits it into two; a swap between loops joins them." The only reason given is one compressed sentence on p. 5: "trace the two outgoing arrows whose destinations are traded…"
- **Fix:** add a two-line instance on the printed non-task visual (Grades 4–5, page 3):
  - Swapping W and V in WUVXY gives VUWXY. The loop U → V → W → U becomes U ⇄ V plus W at home: one loop splits into two.
  - Swapping X and Y gives WUVYX. Two one-card loops join into X ⇄ Y.
  - In general, cards X and Y trade the ends of their two arrows. If X and Y are on one loop, that cuts it into two closed loops. If they are on different loops, it splices the two into one.
- This is adult background, so it does not give away anything in Problem 3.

### 3. Grades 2–3 Problem 3 needs a completeness argument children can use (p. 4)

- **What it gives now:** "The hardest rows are exactly single four-card loops." Grades 2–3 children have no arrows, so they cannot use this.
- **Missing bridge to the first visit:**
  - A row with a card at home needs at most 2 swaps, because the other three cards need at most 2.
  - So a hardest row has no card at home, which means it is one of the nine home-free rows from the first visit.
  - Of those nine, BADC, CDAB and DCBA are two exchanged pairs and need 2 swaps. The other six are exactly the six listed.
- I checked both steps by enumeration. **Fix:** add these three sentences, and a hint such as "Which of the nine rows with no card at home can you already bring home in two?"

### 4. Grades 2–3 Problem 9: replace the enumeration table with a short proof (p. 4; p. 8, "Adult certificate")

- **The problem:** The p. 8 table lists which (r₂, r₃, r₄) occur, a fact taken from the computer search. The guide then says "This finite certificate proves both the maximum and the missing five". The table explains nothing, and an adult cannot check it.
- **A short argument does exist.** With four crossed-out spots, the count is 2r₂ − r₃ + r₄:
  - If all four spots use different cards and homes, r₂ = 6, r₃ = 4, r₄ = 1, and the count is 9.
  - If no three spots are compatible (r₃ = 0), the count 2r₂ is even. Also r₂ ≤ 4, because five compatible pairs among four spots would force a compatible triple. So the count is at most 8.
  - Otherwise there is a compatible triple, and the fourth spot clashes with one or two of its spots: it can share its card with at most one and its home with at most one. That gives (r₂, r₃) = (5, 2) or (4, 1), so the count is 8 or 7.
  - So the counts are 9, 8, 7 or even numbers up to 8. Five never occurs, and nothing beats 9.
- These cases agree with my enumeration of all 1,820 boards. **Fix:** replace the table and the "certificate proves" sentence with this paragraph. Keep the note that this is adult background, not a child's proof.

### 5. The K–1 page is not yet a page the parent can run from (p. 3)

The parent is not a mathematician, and the base week gave the parent a page that could be printed on its own. This guide's K–1 page has two gaps.

- **Missing materials and route.** They are on p. 2. **Fix:** add one opening line to p. 3: the kit with D/E or E covered, one cut A–C set and a cup of counters per pair, then Problems 1–2, selected rows of Problem 4, then Problem 5.
- **Loop vocabulary the parent has not met.** For example, BCDA's key says "leaving a three-card loop needing two more", and Problem 3 says "a complete lower-bound argument". **Fix:** use plain words:
  - "Any first swap either puts one card home, leaving three mixed cards that need two more swaps, or makes two swapped pairs that need two more."
  - "Pointing to a card that never moved shows two swaps are not enough."
- **The crossed-out pictures are new to everyone.** Add one sentence for the first board (Problem 6): point to home B, name the two crossed-out pictures, and ask which cards may still go there. Then let the children place cards.

### 6. Reading and recording demands, the adult's role and later visits are thin for Grades 2–3 and 4–5 (p. 2, "First route and staffing")

- **Reading.** The account is "four labels and totals to 24", "five labels, totals to 120 and reversible reasoning". It does not say who reads the problems. Grades 2–3 Problem 9 is three sentences with three numeric targets.
- **Heavy recording and checking that the guide leaves out:**
  - Grades 2–3 Problem 9: every trial board means checking all 24 cut outcome cards against four crosses, so each attempt takes several minutes.
  - Grades 4–5 Problem 10: 16 five-letter rows to record. Pooling is mentioned only on p. 7.
  - Grades 4–5 Problems 12–13: counting 15 compatible pairs and 10 triples by hand on the extra grids.
- **Fix:** add one line per band:
  - who reads the problem aloud;
  - which records the adult may scribe;
  - which searches are shared or pooled. For 2–3 Problem 9, partners each check half the deck against one board. For 4–5 Problem 10, split the five-card search by the card in home A.
- **Later visits.** "Save 4 and 6–13" should become an order:
  - Grades 4–5: a second visit on Problems 4 and 6–9 (totals and piles), a third on Problems 10–13 (forbidden homes).
  - Grades 2–3: a second visit on Problems 6–9.
  - "Reversible reasoning" belongs to the base week's constructions and is not this route's demand. The route needs five letters, reading a swap word and comparing totals.

### 7. The launch shows the new action only as a drawing (p. 2, "Launch together")

- **The issue:** "Any two cards, near or far" is the one new rule, and it differs from Week 3's neighbour-only swaps. The guide reproduces the printed U–X picture on a board. AGENTS asks for a demonstration of the concrete action, and the Week 8 model launches with a real slide and a rejected jump.
- **Fix:** write U, V, W, X on four scrap-paper squares and lay them on a drawn four-home strip as V U W X. Ask a child to trade V and X while another names them, then write "VX". This takes under a minute to make, is still a non-task instance and reveals nothing.

## Minor

1. **K–1 Problem 5 hint (p. 3).** "Which two outcomes give A a counter?" tells the child the per-letter answer. Write "Which outcomes give A a counter?"
2. **"The same-number choice on the final page is intentional." (p. 3).** This is revision history, and "final page" reads as page 5. Delete it.
3. **K–1 Problem 8 key (p. 3).** "Home B permits D alone, home C permits A alone; B then must use D and C must use A" repeats itself and stops early. Write: "Home B can take only D and home C only A. Then home A, which refuses A and B, takes C, and home D takes B: CDAB."
4. **Grades 4–5 Problem 2 hint (p. 5).** "Can a move split off a card at home?" uses loop language before Problem 3 introduces arrows. Write "Can this swap put a card home?"
5. **Grades 4–5 Problem 3 (p. 5).** State the expected child answer to "How can you tell the fewest swaps from the arrows?" in children's terms: "a loop of k cards needs k − 1 swaps; add them up", which is 5 minus the number of loops, counting loops of one.
6. **Process notes that do not help a facilitator.** Delete these:
   - "The independent checker also filters all 120 rows" (p. 7);
   - "the reproducible checker supplies exhaustive coverage" (p. 8);
   - "The final upper grids are P12 and P13, superseding the older review's P12-only numbering" (p. 8).
   
   Also, "Children can use K–1 Problem 4's paired-home reasoning" (p. 4) points 2–3 adults to another band's pages. Write the reason out instead: one swap puts two cards home only for a pair in each other's homes.
7. **Small materials gaps (p. 2):**
   - Add erasers: Grades 2–3 Problem 9 is trial and error on printed menus.
   - If the kit was not kept, give the visit's own minimum instead of only the base week's 45–90 minutes for the full kit: page 1 ×5 cut, page 3 ×2 cut, the six A–C cards from one page 2, plus the uncut extras.
8. **Grades 2–3 Problem 6 hint (p. 4).** Add the concrete bridge: "the other four letters can be arranged in as many ways as the A–D deck has cards", so A is home in 24 of the 120 rows.
9. **Density.** The guide runs about 4,900 words, against 3,000 for Week 98 and 2,400 for the Week 8 return visit. The catalogs earn their space. The cuts in Minor 6 and Should-fix 4 save about a third of a page.

## The writer's flagged issues

- **Unpiloted, untested fit and handling, Grades 2–3 pages 5–6 as reference boards only, Problems 12–13 split:** I agree. The board measurements confirm the mat claims.
- **K–1 counters not supplied by a base PDF:** I agree that an unprinted object is needed. I disagree with the quantity of six, which gives the answer away (Must-fix 1). I also note that the base kit's five cut A–C sets allow one per pair.
- **Middle pairs sharing one uncut sheet, handled by staggering:** I disagree. Staggering gives the second pair a sheet that is already circled (Must-fix 1).
- **Middle Problem 9 backed by computer coverage, not presented as a child's proof:** I agree it is not a child's proof. But the p. 8 table does not "prove" anything an adult can follow, and a short adult proof exists (Should-fix 4).
- **U–X launch drawn because the kit prints only A–E:** I agree the kit has no U–X cards. Paper squares make the demonstration physical at no cost (Should-fix 7).
- **Frieze D14/D16 "opened directly":** I could not confirm this from the checkout, which has no local copies under `external-resources/new-themes-52-63/week62-63/`. If they were read online, say so; otherwise use the base guide's wording.

## What works

- **Correct, complete answers with completeness arguments.** Examples: the disjoint-pairs proof for K–1 Problem 2; the forced-home checks for K–1 Problems 6–8; the first-card branch table for the 16 strip rows; and the 13 ring rows obtained by deleting the three rows with E in home A from the strip list. Keep all of these.
- **The overview.** It states each fact with its assumptions and limits: n ≥ 2 for parity, ⌈n/2⌉ with both bounds proved, totals over a complete deck "not guarantees about one row", and the own-home recurrence "does not apply to arbitrary boards". It gives a short proof of each, and its D_n − nD_{n−1} = (−1)^n step is correct.
- **Conventions are pinned where children trip.**
  - Swap words name cards, not homes.
  - Arrows run card → home. The guide warns that the inverse is the wrong printed convention even though it gives the same loop count.
  - The guide checks that BCADE has A → C, not A → B.
  - The VXUW grid bridge, and "convert one already-built row to dots and back before asking for an overlap count".
- **Mats versus records.** The guide says explicitly which printed boards take real cards and which are reference boards, and keeps cards out of the answer boxes.
- **Honest status and evidence levels.**
  - Grades 4–5 Problem 9's alternation "is evidence, not a proof", with the recurrence argument offered only if it would not be adult-operated.
  - Grades 2–3 Problem 9 separates a found board from an unproved maximum.
  - Pooling is offered for the long searches.
  - Every physical step is marked untested.
- **Pacing.** The 60-minute plan (5/5/20/2/18/5/5) and the band routes are realistic starting points.
