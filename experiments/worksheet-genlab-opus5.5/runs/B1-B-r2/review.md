# Review of the Week 7 (Take-away games) draft packet

Reviewed: `base/k-1.pdf` (5 pp., 10 problems), `base/grades-2-3.pdf` (5 pp., 7 problems), `base/grades-4-5.pdf` (5 pp., 9 problems), plus `src/*.tex`, `src/mc.sty`, `src/check.py`.

## How I checked it

- I rendered every page at 80 dpi and zoomed in at 200 dpi on the dense regions: the 4–5 Problem 3 strips, the 2–3 Problem 6 table and the K–1 Problem 9/10 ring rows.
- I rebuilt all three sources from copies in `scratch/build`. There are no overfull or underfull boxes and no warnings. All pages are US Letter.
- I checked every answer independently in `scratch/verify.py` and `scratch/alt.py`. This covered:
  - backward induction for single piles;
  - brute-force game trees for each two-pile position;
  - a full game-tree search of every "plan" problem against every reply, including whether each move the plan makes is legal.
- I read every sentence against the organizer's standard and its "leave these off" list.

## Overall verdict

The draft is strong.

**What it gets right:**
- **Format:** Headers, footers, "Problem N:" labels, US Letter page size, and the single packet-wide rule at the top of page 1 all follow the standard.
- **Wording:** There are no extra headings, no encouragement, no exclamation marks, no dashes used for asides, and no lettered sub-steps.
- **Answers:** Every answer I checked is correct (table below).
- **K–1 depth:** The K–1 packet is real mathematics at a smaller scale. It covers traps under three rules, the greedy player (Ben), extending the pattern to 20, two piles, and counting game lines.
- **Quantity:** Each band has five pages, which is enough for the hour.

**What needs work:** Most of the problems are about wording and logic, not arithmetic. The changes I would make before printing, most important first:
1. **4–5 Problem 8:** the word "number" is ambiguous, and the definition is introduced before the child has used the idea.
2. **2–3 Problem 6:** checking piles 1 to 15 cannot settle Jon's claim. The explanation, which is the actual mathematics, is never asked for, and the table does not say what to write.
3. **2–3 Problems 2 and 5:** "wins every time" is only circled, so the kernel idea of answering every reply is never written down.
4. **K–1 Problem 9:** it is too long to understand after one hearing, and the ring rows are cramped for kindergarten hands.
5. **K–1 Problem 8:** it never says that the last counter overall wins.

## Answer verification (for the organizer's own reference)

| Band / Problem | Correct answer (checked) |
|---|---|
| K–1 P1 ({1,2}; 2,3,4,5) | 1st, 2nd, 1st, 1st |
| K–1 P2 (4,5,7,8) | take 1, 2, 1, 2 (leave 3, 3, 6, 6) |
| K–1 P3 ({1,2}, 1–12) | colour 3, 6, 9, 12 |
| K–1 P4 (Ben greedy, Ben first, 2–7) | beatable at 3, 4, 6, 7; not at 2, 5 |
| K–1 P5 ({1,2,3}) | colour 4, 8, 12 |
| K–1 P6 ({1,3}) | colour 2, 4, 6, 8, 10, 12 |
| K–1 P7 (20) | {1,2}: 1st; {1,2,3}: 2nd; {1,3}: 2nd |
| K–1 P8 ((2,2),(1,2),(3,3),(1,4)) | 2nd, 1st, 2nd, 2nd |
| K–1 P9 / P10 | 5 ways / 8 ways (rows supplied: 7 / 10) |
| 2–3 P1 ({1,2}; 4,6,7,9,11,12) | first, second, first, second, first, second |
| 2–3 P2 | Mia wins; Leo can lose; Ana wins; Sam can lose (in fact Sam's plan loses against **every** reply, since he always leaves 10, 7, 4, 1) |
| 2–3 P3 ({1,3,4}, 1–20) | 2nd at 2, 7, 9, 14, 16; 1st elsewhere |
| 2–3 P4 (25, 30, 37, 50) | first, second, second, first (0 or 2 mod 7) |
| 2–3 P5 | Kai can lose (10→6→5→1→0); Theo can lose (all 1s); Zoe wins every time (every move her plan makes is legal) |
| 2–3 P6 | Jon is wrong: both rules give 3, 6, 9, 12, 15 |
| 2–3 P7 ((5,5),(3,6),(1,5),(2,5)) | second, second, first, second |
| 4–5 P1 | 2nd at 3, 6, 9, 12, 15; 100 → first, take 1 |
| 4–5 P2 | L at 2, 7, 9, 14, 16, 21, 23, 28, 30 (0, 2 mod 7) |
| 4–5 P3 | pairs {1,2}={1,2,4}, {1,3}={1,3,5}, {1,4}={1,4,6} |
| 4–5 P4 | 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29; greedy always right for {1,3} and {1,3,5} |
| 4–5 P5 | {1,2,3}; {1,4}; {1,2,6}; impossible (2 must be a move because pile 2 is not losing, but then 5 → 3) |
| 4–5 P6 | losing iff a ≡ b (mod 3) |
| 4–5 P7 | losing iff values equal: values 0,1,0,1,2,3,2,0,1 for 0–8 |
| 4–5 P8 | values 0,1,0,1,2,3,2 repeating (period 7); (11,13) losing; (12,18) winning (e.g. 12→11) |
| 4–5 P9 ({1,6,9}) | L at 2, 4, 7, 12, 14, 17, 19, …; period 5 from pile 10 on (pile 9 is the last exception) |

**Verification gap in the author's script:** `check.py` models Sam as copying his partner's move (`sam=lambda p,last,k: 1 if k==0 else last`). The page gives Sam a different plan: take 1, then answer 1 with 2 and 2 with 1. Both plans can lose, so the printed answer stands. However, the printed plan was never actually checked, and the script missed that Sam's printed plan *always* loses. An adult needs to know this. A child who finds that "every game I try loses" has made the right discovery, and should not be told that some games win.

---

## Findings, most important first

### 1. Grades 4–5, Problem 8: the word "number" is overloaded, and the idea arrives before it has been used (high)

> "give each single pile a number as follows. An empty pile gets 0. Any other pile gets the smallest of the numbers 0, 1, 2, 3, … that is not the number of a pile you can move to. Find the numbers of the piles from 0 to 20."

**The ambiguity:** Throughout the packet, "the number of a pile" has meant how many counters it has. Here it means a computed value. "Find the numbers of the piles from 0 to 20" can be read as a request for the pile sizes. A careful child will be confused, and a quick one may simply write 0, 1, 2, … 20 in the table.

**The standard:** "Introduce a new word or notation only after the child has used the idea it names." Nothing earlier has the child use this value. The problem also stacks four different tasks:
- a definition;
- a 21-cell computation;
- two two-pile decisions;
- an explanation.

The explanation for (12, 18) needs the whole two-pile Sprague–Grundy argument. This is far beyond the suggested 4–5 emphasis ("find and explain repeating patterns and compare what happens when the rule changes"). Yet P8 sits *before* P9, the problem that does hit that emphasis. A child who stops after P8 never meets the pigeonhole argument.

**Fix:**
- Give the value its own word ("label each pile", "the pile's label"), never "number".
- Consider letting P7's grid motivate it. For example, the child has just seen that (4, 6) is a losing pair even though 4 ≠ 6.
- Swap P8 and P9, so the on-emphasis periodicity problem comes first and the Grundy problem is the last-page stretch.

### 2. Grades 2–3, Problem 6: checking piles cannot answer the question asked, the table does not say what to write, and there is no answer space (high)

> "Jon says that when a turn may take 1, 2, or 4 counters, the starting piles where you would rather go second are different from when a turn may take only 1 or 2. Is Jon right? Check every starting pile from 1 to 15 counters."

**The logical gap:** Jon's claim is about all starting piles. Finding the same second-player piles from 1 to 15 is evidence, but it does not show Jon is wrong. A mathematician organizer will see this immediately. The real mathematics is *why* adding the 4 changes nothing: if your partner takes 4, you take 2, and you are back to a multiple of 3. That explanation is exactly the kind the standard says to ask for. Here it is not asked for.

**Smaller problems:**
- The two-row table never says what goes in the cells (1st/2nd? W/L? colour?).
- The cells are only 0.98 cm wide, which is tight for a third grader writing "2nd".
- There is nowhere to write the answer to "Is Jon right?".

**Fix:** "Is Jon right? Explain how you know." Say what to write in each cell, or switch to "colour the piles where you would rather go second". Add a writing box below the table. Page 5 has room if the P7 box shrinks slightly.

### 3. Grades 2–3, Problems 2 and 5: "wins every time" is only circled (medium-high)

The kernel's key point is: "a winning strategy … must answer every possible reply of the opponent, not just the replies you expect". The brief names this as the 2–3 emphasis ("test claimed strategies against every reply").

In both P2 and P5, a plan that can lose gets a written counterexample. A plan that wins (Mia, Ana, Zoe) gets only a circle. A child can circle "wins every time" after two friendly test games, and the page records nothing that shows they checked every reply. The standard's own list of where explanation is the point includes "why a strategy always wins".

**Fix:** Ask once, not for every plan. For example, in P5: "For a plan that wins every time, explain why it wins whatever the partner does." Zoe's plan is the best choice because her "leave 7 or 2" rule must be checked against every reply. Do not add this to every box. That would become the automatic follow-up the standard forbids.

### 4. K–1, Problem 9: too long to follow after one hearing, the recording format is unclear, and the rows are cramped (medium)

> "A game starts with 4 counters, and each turn takes 1 or 2. Draw rings around the counters taken on each turn to show every different way the game can go."

**Length:** The second sentence is 19 words long and carries two new ideas: rings stand for turns, and different orders count as different games. The standard asks for "one or two short sentences" that "make sense after one hearing" and says to "let the pictures and objects carry the rest". Here the picture carries nothing, because every row is blank. P10 ("Now find every different way a game with 5 counters can go…") does not repeat the ring instruction. It relies on the child remembering P9's instruction when an adult reads P10 aloud separately.

**Cramped rows:** At the printed size, counters are 5.6 mm across, with 7.9 mm gaps sideways and only 9.9 mm between rows. Kindergarten rings around pairs will run into the rows above and below. The 7-row box uses less than half the column, so there is room to space the rows out.

**Weak link to the kernel:** As posed, this is a counting problem (Fibonacci numbers 5 and 8). It is a fine "find every way" task, but it never connects to winning.

**Fix:**
- Shorten it to: "Show every different way a game with 4 counters can go. Ring the counters taken on each turn."
- Pre-ring one row as a format example, such as the 2+2 game. That is the same move as the organizer's EEENNN example in the walking problem, and it shows the format without giving away any of the answers.
- Use 5 or 6 rows at about 2 cm spacing for 4 counters, and 8 or 9 rows for 5 counters, with a second column or the back of the page.
- Optionally add one more sentence to P10 tying it to the game: "Put a star next to each game the first player wins."

### 5. K–1, Problem 8: the two-pile winning condition is not stated (medium)

> "Take 1 or 2 counters from one of the two piles on each turn. For each pair of piles, circle whether you want to go 1st or 2nd."

The 2–3 and 4–5 versions both say "whoever takes the very last counter wins". The K–1 version relies on the page-1 rule "Whoever takes the last counter wins". A five-year-old hearing that rule with two piles in front of them will often think emptying either pile wins. Under that misreading, (1, 2) and (1, 4) become trivial first-player wins, and the problem collapses.

**Fix:** Add "Whoever takes the very last counter wins." The problem is still two short sentences if the first is trimmed: "Take 1 or 2 counters from one pile on each turn. Whoever takes the very last counter wins."

### 6. Grades 4–5, Problem 3: you cannot circle a number inside a 6 mm cell (medium)

There are seven strips of 24 cells, each 0.625 cm wide, with two-digit numbers filling the cells (see the zoomed render). A 9-year-old's circle around "13" will spill into "12" and "14", and for rules such as {1,3} the circles will touch along the whole strip. The ruled boxes around the numbers make this worse.

**Fix:** Do one of these:
- Drop the cell borders, print the numbers as a plain row with 9 to 10 mm spacing, and split each rule into two lines of 12.
- Keep the cells and change "circle" to "shade" or "put a dot under".

The page has room: the writing box can lose about 1 cm.

### 7. Grades 4–5, Problem 4: the second question asks "always" but wants no reason, and the wording overloads "winning" (medium-low)

> "list every winning pile from 1 to 30 where Kai's move leaves his partner a winning pile. For which of the seven rules in Problem 3 does Kai's move from a winning pile always leave a losing pile?"

**"Always" without a reason:** "Always" is a claim about every pile. The child's data stops at 24, so this has the same logic gap as finding 2. The interesting reason, that with only odd moves the greedy move flips odd to even, is never asked for.

**Overloaded wording:** "a winning pile … leaves his partner a winning pile" uses the word twice from two players' points of view in one breath.

**Fix:**
- "…always leave a losing pile? Explain why for one of them."
- Consider: "list every winning pile from 1 to 30 where Kai's move is a mistake", and let the child work out what a mistake means.

### 8. Grades 4–5, Problem 5: half the cases are lookups (low-medium)

The first two lists (4, 8, 12, … and 2, 5, 7, 10, …) appear exactly as rows of Problem 3 ({1,2,3} and {1,4}, also {1,4,6}). A child who did P3 reads the answers straight off the previous page. Only the third case (needs {1,2,6}) and the fourth (impossible) carry the problem. The opening definition "A rule is a list of how many counters a turn may take" arrives after "rule" has been used in the intro and in P2–P4. Delete it.

**Fix:** Replace one of the first two lists with one that is not in P3. For example, "2, 8, 10, 16, 18, 24, …" is {1,4,5} (0 or 2 mod 8, checked), and "2, 4, 11, 13, 15, 22, 24, …" is {1,5,6}. Keep the {1,2,6} case and the impossible case.

### 9. Grades 4–5, Problem 7: a grid with no question (low)

P7 is 81 cells of W/L with no question about them. It reads as setup for P8, but P8 never refers back to it. As a stand-alone problem, a child who finishes the grid has nothing to aim at. The space to the right of the grid is empty.

**Fix:** Add one short question that is the point: "Which pairs of different piles are losing pairs?" The answer, (0,2), (0,7), (1,3), (1,8), (2,7), (3,8) and (4,6), is surprising after P6's "same remainder" pattern, and it sets up P8 without a hint. Use the empty space for the box.

### 10. K–1: some redundancy at the start (low)

P1 asks 1st/2nd for piles 2–5 under {1,2}. P2 asks for the winning move from 4, 5, 7 and 8. P3 then asks for every pile from 1 to 12 under the same rule. P3 includes everything P1 asks. For a quick first grader, P1 is a two-minute task, which falls short of the standard's "at least five minutes".

This is acceptable as a concrete opening, but a better case set would make P1 more substantial. For example, P1 could use piles 3, 4, 5, 6 so that it contains two traps.

**K–1 Problem 4:** Someone has to play Ben. The page does not say whether the partner or the adult does, and a child who hears it once may not realise their partner should follow Ben's rule. Consider "Your partner plays Ben. Ben always takes 2…"

### 11. Packet intros: talk about the packet (low)

The 2–3 intro has "…and each problem says how many counters a turn may take." The 4–5 intro has "…and each problem gives the rule for how many counters a turn may take." Each is a clause about the packet rather than a rule of the game. The standard allows rules to be "stated once, briefly". These clauses can go, and the paragraph still works.

### 12. Small items (nits)

- **Header level:** The K–1 header reads "Week 7 / Take-away games / K–1". The other two read "Grades 2–3" and "Grades 4–5". Use "Grades K–1" for consistency, or leave it if the organizer prefers that form.
- **"Color" versus materials:** K–1 P3, P5 and P6 say "Color every pile". The materials list has pencils and no crayons. "Color" with a pencil works, but "Shade" or "Put an X on" matches the materials.
- **"I start with 8 counters":** In the 2–3 plans, Mia's "I start with 8 counters" can be heard as Mia owning 8 counters. "The pile starts with 8 counters and I go first" is clearer. This is minor because an adult is present.
- **Recording format:** 2–3 P5 says "write down a game where it loses" without P2's format ("listing how many counters are left after each turn"). That is fine because P2 already set the format.
- **4–5 Problem 9:** "find where the pattern starts to repeat" has two reasonable answers: pile 10, where the period-5 block starts, or pile 12, the first repeated L. Both are good, and the adult should accept either if the child can say why pile 9 breaks the pattern.
- **Blank space:** K–1 pages 1, 2 and 4 are a third to half blank. That is harmless, but the space could be used for the larger P9/P10 spacing (finding 4) instead of crowding page 5.

## Things checked and found fine

- **Diagrams:** Every counter diagram shows the stated count. I checked the drawing loops in `\counters`, `\twelve` and `\pilerow`, and the renders: K–1 boxes 1–12, the 20-box, and the two-pile pairs in both bands.
- **Fit:** Nothing overflows or overlaps at any size I rendered. Every table and box fits within the margins.
- **Banned items:** There are no headings beyond the header and the "Problem N:" labels. There are none of the banned phrases, no exclamation marks, no dashes used for asides, no "not X but Y" constructions, and no lettered sub-steps.
- **Hints:** The only places strategy content shows up are inside the claimed plans (Mia, Ana, Zoe). Those plans are the objects being tested, as the brief's 2–3 emphasis intends, so they are not hints.
- **Order:** Each band moves from concrete cases to explanation. Stopping anywhere is fine, apart from the P8/P9 ordering in 4–5 (finding 1).
- **Characters:** The named children (Ben, Mia, Leo, Ana, Sam, Kai, Theo, Zoe, Jon) each carry a strategy or a claim. They are not decoration. Kai uses the same greedy plan in 2–3 and 4–5, which helps a child who moves between bands.
- **Quantity:** Every band has more than most children will finish.
