=================== Report 1: adversarial review ===================

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


=================== Report 2: simulated classroom session ===================

# Week 7 take-away games: session simulation review

Draft reviewed: base/k-1.pdf, base/grades-2-3.pdf, base/grades-4-5.pdf (5 pages each). I rendered every page at 80 dpi and checked measurements and answers against src/*.tex. To work out what the children would find, I ran every game by computer: the win/lose labels, every plan in the 2–3 packet played against every possible reply, and the losing-pile lists in 4–5.

Materials on the table are the ones in the brief: plenty of counters, paper, pencils and small whiteboards. There are no crayons. Times are working minutes after the demonstration, out of about 40.

---

## K–1 (parent volunteer reads each problem aloud exactly as printed)

Children: K1 and K2 (kindergartners who cannot read and count reliably to about 20), and F (a first grader who reads a few words; the quick child for this band). Three children means one pair plus one child who plays the parent, or a rotating three.

**Problem 1 (p.1), "Take 1 or 2 counters on each turn. For each pile, circle whether you want to go 1st or 2nd."** The parent reads the packet rule and the problem. The children build the piles from loose counters, because the printed dots are too small to play on. Pile 2: the first player grabs both and wins, and everyone circles 1st. Pile 3: K1 goes first, takes 2, and K2 takes the last one. They try again and K1 takes 1, then loses again, so it's "2nd." Piles 4 and 5: the kindergartners take 1 or 2 at random, so the winner changes from game to game. K1 asks "Who's right?" The parent cannot tell from the page and lets them circle whoever won last. F notices that "if I leave 3 I win" by pile 5. Circling "1st"/"2nd" is easy, since kindergartners can recognize the digit. **F: 0–6 min, engaged.** K1 and K2: about 8 minutes, engaged.

**Problem 2 (p.1), "Cross out the counters you would take to be sure to win."** Piles 4, 5, 7 and 8. F uses the 3-trap: cross 1 on the 4, cross 2 on the 5. On 7 and 8 she rebuilds the piles and plays them out, and finds 1 and 2. The kindergartners cross out 2 everywhere because "more is better," then test with counters and change one of them. The 0.38 cm printed counters are easy to X. **F: 6–12 min, engaged.**

**Problem 3 (p.2), "Take 1 or 2 counters on each turn. Color every pile where you would rather go second."** After one hearing, K2 picks up "Color every pile" and starts shading box 1. The parent re-reads the problem. They have only pencils, and shading a 2.7 × 3.3 cm box with a pencil takes a kindergartner most of a minute. F remembers 3 and works out 6 by playing ("whatever she takes, I make it 3"). At 9 she says "it goes 3, 6, 9" and colors 12 without playing. K1 and K2 counted out and played piles up to about 7, but their random play gave 7 a "second" result once, so K1 colored 7. The parent cannot correct this from the page. **F: 12–23 min.** She was engaged up to pile 9, then just shaded boxes for the last three minutes.

**Problem 4 (p.2), "Ben always takes 2 counters when he can, and you take 1 or 2. Circle each pile where you can beat Ben when he goes first."** K2 asks "Who's Ben?" The page does not say who plays him, so the parent makes K1 be Ben. K1 wants to win, so on pile 5 he takes 1 instead of 2. The parent re-reads "always takes 2" and they replay it. With 1 left, "when he can" leaves the parent unsure whether Ben takes the last 1. She decides he does. F finds that 3, 4, 6 and 7 can be beaten and 2 and 5 cannot. Pile 7 needs two replays. This is the most engaging problem in the packet for this group. **F: 23–30 min, engaged.**

**Problem 5 (p.3), "Now take 1, 2, or 3 counters on each turn. Color every pile where you would rather go second."** The page shows the same twelve boxes as page 2. K1 says "We did this one." Only the words in the problem tell this game apart from Problem 3. Three minutes in, nobody at the table still remembers the rule, and nothing on the page shows it. K2 keeps taking at most 2, and F has to re-ask the parent "is it 1, 2, 3?" F finds 4 and then 8 and guesses 12. K1 and K2 stop playing: at about minute 33 they push the page away. The parent flips ahead to page 4 for them. **F: 30–38 min**, engaged about half the time; the rest is repetition.

**Problem 6 (p.3), "Take 1 or 3 counters on each turn. Color every pile where you would rather go second."** F starts this at minute 38 and is in the middle of it at minute 40. On this sheet random play gives consistent results, because every move changes the pile from odd to even or back, so F's results agree from game to game. That only holds while the rule is kept, though. Twice F's partner takes 2, a habit from the five earlier problems, and the parent misses it because the rule is not shown in a picture. **F: 38–40+ min.**

**Problem 7 (p.4), "Start with a pile of 20 counters. For each rule, circle whether you want to go 1st or 2nd."** K1 and K2 do this one after the parent flips ahead at minute 33. Counting out 20 is at the edge of what they can do: K1's pile has 18 and K2's has 22. One game of "take 1 or 2" from about 20 takes them about 4 minutes of random play. They circle the winner's position, and the result means nothing. They do not attempt the other two rules. F would reach this only after minute 40; she could group the counters in threes off the Problem 3 pattern, but no one at the table can check her. **K1/K2: 33–37 min.**

**Problem 8 (p.4), "Take 1 or 2 counters from one of the two piles on each turn. For each pair of piles, circle whether you want to go 1st or 2nd."** K1 and K2, minutes 37–40+. On the 1-and-4 board K2 goes first, takes the single counter, and shouts "I took the last counter, I win." The only rule on the page is the one at the top of page 1, "Whoever takes the last counter wins," and it was written for one pile. The parent cannot say from the page whether it means the last counter of one pile or of both. K1 also takes one counter from each pile in a single turn ("that's 2"). The parent rules that both piles have to be empty and the move has to come from one pile, but by then the 1-and-4 and 2-and-2 boards have been circled under the wrong rule.

**Problems 9 and 10 (p.5), "Draw rings around the counters taken on each turn to show every different way the game can go." / "Now find every different way a game with 5 counters can go…"** Nobody reaches these in 40 minutes. When a child does, this is what happens. The sentence is long and abstract for one hearing, and K1 rings single counters across all seven rows. F rings 2, 1, 1 and then 1, 1, 2 and asks "Is that the same?" The parent cannot answer from the page, because "every different way the game can go" does not say whether order matters. It decides whether the answer is 3 or 5 for four counters, and 3 or 8 for five. The box has 7 rows for 4 counters, so F keeps going after her fifth way and fills the last two rows with repeats. A ring around two counters has to fit through a 0.79 cm gap to the next counter, with 1.55 cm between rows. K1's ovals catch a third counter or run into the row below.

---

## Grades 2–3 (second mathematician at the table)

Children: Q (a quick, impatient third grader), M1 and M2 (middle), and W (weaker). They play in two pairs.

**Problem 1 (p.1), "Play with each starting pile below until you are sure whether you would rather go first or second, and circle your choice."** All four play piles 4, 6 and 7. Q sees "leave 3" on the 4. On 9 he announces "it's the threes" and circles 11 and 12 without playing them. M1 and M2 get the pattern by pile 9. W plays every pile and needs about 12 minutes. **Q: 0–5 min, engaged but fast.**

**Problem 2 (p.2), the plans of Mia, Leo, Ana and Sam (rule 1 or 2).** Q plays Leo once and Leo loses straight away. He writes "8, 7, 5, 4, 2, 0" in the box, which has plenty of room. He plays Mia once, Mia wins, and he circles "wins every time." Ana: one game, a win, circled. Sam: Sam loses in the first game, and in fact in every possible game. By computer, Leo loses in 3 of his 5 possible games, Sam in 8 of 8, and Mia and Ana in none. So one casual game always gives the right circle, and nobody has to think about "whatever the partner does." The mathematician asks Q "did you try every reply?" Q says "it won." The page gives him no reason to check further. **Q: 5–10 min**, racing. M1 and M2 take about 10 minutes and get the same answers the same way.

**Problem 3 (p.3), "Now each turn takes 1, 3, or 4 counters. For every starting pile from 1 to 20 counters, decide whether you would rather go first or second."** The 1.75 × 1.2 cm cells hold "1st"/"2nd" easily. Piles 1 to 6 go fast by play. Pile 7 is the first surprise ("second wins!"). By 10 Q is impatient and guesses "every 5" (7, 12, 17). The mathematician challenges 12, Q finds he can take 3 to leave 9, and he corrects it. He finishes with 2, 7, 9, 14, 16. M1, M2 and W are still in this table at minute 40. **Q: 10–23 min**, engaged apart from about 2 minutes of impatient guessing.

**Problem 4 (p.3), piles 25, 30, 37, 50.** Q continues "+5, +2" from his table and circles first, second, second, first. "Explain how you know" gets "the pattern keeps going," and the box is large enough. **Q: 23–27 min, engaged.**

**Problem 5 (p.4), the plans of Kai, Theo and Zoe (rule 1, 3 or 4).** This goes the same way as Problem 2. Kai loses Q's first game (6, 5, 1, 0) and Theo loses his first game. Zoe wins both games Q tries, so he circles "wins every time" after two games, which happens to be correct. By computer, Kai loses 2 of his 3 possible games, Theo 4 of 6, and Zoe 0 of 5. No plan loses only to an unusual reply, so the core point for this band, testing a plan against every reply, never comes up. **Q: 27–32 min**, racing.

**Problem 6 (p.5), Jon's claim, "Check every starting pile from 1 to 15 counters."** The table does not say what to write in the cells. Q asks "1st and 2nd, or W and L?" and the mathematician answers from memory of Problem 3. The cells are 0.98 cm wide. Q's "2nd" spills over the lines, so after three cells he switches to "1" and "2." He copies the "take 1 or 2" row from what he already knows. He works out the "1, 2, or 4" row by play and finds it is the same: multiples of 3. There is no place to write "Jon is wrong," so he writes it in the margin. **Q: 32–38 min, engaged.**

**Problem 7 (p.5), two piles, rule 1 or 2 from one pile.** Q plays 5-and-5, loses going first twice, and finds that copying the other player's move works. He starts 3-and-6 at minute 38 and is still working at 40. The box under the boards holds his explanation of the copying move. **Q: 38–40+ min, engaged.** He does not run out, but if he had raced Problem 3 as he did Problems 2 and 5, he would have reached the end of the packet at about minute 40.

---

## Grades 4–5 (mathematician nearby)

Children: F5 (a fast fifth grader, the quick child for this band) and two fourth graders, G1 and G2.

**Problem 1 (p.1), rule 1 or 2, piles 1–15, then 100.** This is the game from the whole-group demonstration. F5 fills "2nd" under 3, 6, 9, 12 and 15 in a minute, writes "first, take 1, then make 3 each round," and moves on. The 1.17 cm cells are a little tight for "2nd," but readable. G1 and G2 take about 8 minutes. **F5: 0–4 min**, racing.

**Problem 2 (p.1), definition of winning and losing piles; rule 1, 3 or 4; W or L for 1–30; describe the pattern and explain why it continues.** F5 works up from small piles and sees "W L W W W W L" repeating by pile 16, then fills the rest. His first "why it continues" is "because it repeats," which is circular. The mathematician asks "what does pile 20 depend on?" and he gets to "only the four piles before it." G1 and G2 play the small piles and are slow; they are still in this problem at about minute 26. **F5: 4–14 min, engaged.**

**Problem 3 (p.2), seven rules, "circle the losing piles from 1 to 24."** Each number sits in a 0.625 × 0.8 cm cell and fills most of it. F5 copies the "1 or 2" row from Problem 1. On "1 or 3" he circles every even number. His roughly 1 cm circles around 2, 4, 6… overlap the odd numbers between them, so the row looks as if everything is circled. The same happens on "1, 3, or 5" and around 5 and 7 on "1 or 4." When he compares rows to find matches, he misreads his own "1 or 4" row and at first pairs it with nothing. He works the rows out by the Problem 2 method. About 5 minutes in the middle is just copying, which he complains about ("this is the same thing again"). He finds the pairs {1,3}/{1,3,5}, {1,2}/{1,2,4} and {1,4}/{1,4,6}, and explains the odd-moves pair. G1 and G2 start this at about minute 27 and finish 3 rows by minute 40. **F5: 14–30 min**, engaged for about 11 of the 16 minutes.

**Problem 4 (p.2), "Kai always takes as many counters as the rule allows… list every winning pile from 1 to 30 where Kai's move leaves his partner a winning pile."** F5 needs the mathematician to untangle the two "winning piles" (the second one is the partner's). Using his Problem 2 table, he lists 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29, then picks "1 or 3" and "1, 3, or 5" for the second question. **F5: 30–38 min, engaged.**

**Problem 5 (p.3), find a rule for each list of losing piles.** F5 reads "4, 8, 12, 16, 20, 24, …" and says "that's my 1, 2, 3 row." He reads "2, 5, 7, 10, 12, 15, …" and says "that's 1 or 4, from Problem 3." These are rows he has already circled, so the first two cases take him about a minute. At minute 40 he is working on "3, 7, 10, 14, 17, 21, …" and building the rule move by move (2 has to be allowed, 3 must not be, 6 has to be). **F5: 38–40+ min**: two cases were look-ups, then real work.

**Problems 6–9 (pp.4–5): not reached by anyone in 40 minutes.** Simulated for F5 continuing:
- **Problem 6.** He fills the 8 × 8 grid from row 0 and the diagonal and finds that the losing pairs leave the same remainder when divided by 3. He asks what to write in the 0-and-0 cell; the mathematician answers from "whoever takes the very last counter wins." About 12 minutes, engaged.
- **Problem 7.** He faces 81 cells, each needing up to six look-ups, and the page asks for nothing beyond filling them. After two rows he asks "What's this for?" The page gives no goal, and he makes two errors that spread through the grid. About 15 minutes, bored for half of it.
- **Problem 8, "Any other pile gets the smallest of the numbers 0, 1, 2, 3, … that is not the number of a pile you can move to."** Everywhere else in the packet, "a pile of 11" means eleven counters, so F5 reads "the number of a pile" as its size. From pile 5 the piles he can move to are 4, 2 and 1, so he writes 0. From 6 they are 5, 3 and 2, so 0 again, and every pile from 5 to 20 gets 0. He decides that 11-and-13 is "both 0, so losing" (right by accident) and that 12-and-18 is "both 0, so losing" (wrong; it is winning). The mathematician has to re-teach the definition.
- **Problem 9.** The 0.88 cm cells hold W/L. He finds L at 2, 4, 7, then 12, 14, 17, 19… and says it "repeats every 5 starting at 12." The general "why must it repeat" argument is out of reach without heavy help.

---

## Problems the simulation exposed

**1. K–1, p.2–4, Problems 3, 5, 6 and 7: the rule exists only in words.** The texts are "Take 1 or 2 counters on each turn," "Now take 1, 2, or 3 counters on each turn," "Take 1 or 3 counters on each turn," and the three text-only rule rows in Problem 7. Problems 3, 5 and 6 sit above three identical twelve-box grids.
- **What went wrong:** the children forgot the rule a few minutes into each sheet. K2 kept taking at most 2 on the 1-2-3 sheet, and F's partner took 2 on the 1-or-3 sheet without anyone noticing. The kindergartners said "we did this one" and quit Problem 5 at minute 33.
- **Smallest fix:** beside each rule, print the allowed takes as pictures of counter groups at the size of the pile drawings (●  ●● for 1 or 2; ●  ●●  ●●● for 1, 2 or 3; ●  ●●● for 1 or 3), including on each row of Problem 7.

**2. K–1, p.2–3, Problems 3, 5 and 6: "Color every pile where you would rather go second."**
- **What went wrong:** after one hearing, a kindergartner caught "color every pile" and started shading every box. The materials list has only pencils, and shading a box with one costs about a minute each.
- **Smallest fix:** "Circle the piles where you would rather go second."

**3. K–1, p.2, Problem 4: "Ben always takes 2 counters when he can…"**
- **What went wrong:** nobody knew who Ben was. The kindergartner cast as Ben broke Ben's rule so he could win, and the pile-5 result came out wrong until the parent stepped in. "When he can" also left the parent unsure what Ben does with 1 counter left.
- **Smallest fix:** "The grown-up plays Ben. Ben takes 2 counters each turn, or 1 when only 1 is left."

**4. K–1, p.4, Problem 8: "Take 1 or 2 counters from one of the two piles on each turn."** The only win rule is "Whoever takes the last counter wins," written for one pile on page 1.
- **What went wrong:** a kindergartner emptied the 1-pile and claimed the win, and another took one counter from each pile in a single turn. The parent could not settle either from the page. The 1-and-4 and 2-and-2 answers flipped. The 2–3 and 4–5 packets avoid this with "whoever takes the very last counter wins."
- **Smallest fix:** add "Take from just one pile. Whoever takes the very last counter of all wins."

**5. K–1, p.5, Problems 9 and 10: "Draw rings around the counters taken on each turn to show every different way the game can go."**
- **What went wrong:**
  - F asked whether 2, 1, 1 and 1, 1, 2 count as different. The parent could not tell from the page, and the answer is 3 or 5 (for 5 counters, 3 or 8) depending on her ruling.
  - The 7 and 10 printed rows (for 5 and 8 answers) invited filler repeats.
  - With 0.79 cm between counters and 1.55 cm between rows, kindergartners' rings caught a third counter or ran into the next row.
- **Smallest fix:** add the sentence "Taking 2, then 1, then 1 is a different way from taking 1, then 1, then 2." Put Problem 10 on its own page so both boxes can have about 2 cm between rows and 1.8 cm between counters.

**6. Grades 2–3, p.2 and p.4, Problems 2 and 5: every plan is either always right or loses to most replies.** The plans are Mia, Leo, Ana and Sam; then Kai, Theo and Zoe.
- **What went wrong:** each losing plan lost the first casual game (Leo in 3 of 5 possible games, Sam 8 of 8, Kai 2 of 3, Theo 4 of 6). Each winning plan won every game. One game per plan gave the right circle, so "whatever the partner does" was never tested and Q raced both problems in about 5 minutes each.
- **Smallest fix:** add a fourth plan to page 4 that differs from Zoe's in one sentence:
  > Max: I start with 9 counters and go second. After each of my partner's turns, I leave 7 counters or 2 counters if I can. If I can't, I take 1.

  This plan loses only when the partner takes 1 and later takes 3 when 7 are left (9, 8, 7, 4, 3, 0). That happens in about 1 random game in 9, so the children have to check every reply. Shrink the three existing boxes from 6.6 cm to about 4.8 cm so four fit.

**7. Grades 2–3, p.5, Problem 6: "Check every starting pile from 1 to 15 counters."** The table has two blank rows of 0.98 cm cells.
- **What went wrong:** the page does not say what to write. "1st"/"2nd" in a third grader's hand does not fit in 0.98 cm, so Q spilled over the lines and switched to "1"/"2." There is no space for the answer to "Is Jon right?"
- **Smallest fix:** "Put an X under each pile where you would rather go second. Is Jon right?" Add one answer line under the table.

**8. Grades 4–5, p.2, Problem 3: "For each rule, circle the losing piles from 1 to 24."** Each number is printed inside a 0.625 cm cell.
- **What went wrong:** circles around every other number (rules 1 or 3, and 1, 3 or 5) and around close pairs (5 and 7 on 1 or 4) overlapped the numbers between them. F5 misread his own row when hunting for matching rules.
- **Smallest fix:** add a blank row of cells under each numbered row and change the task to "write L under each losing pile."

**9. Grades 4–5, p.3, Problem 5: the first two lists are Problem 3 answers.** The lists are "4, 8, 12, 16, 20, 24, …" and "2, 5, 7, 10, 12, 15, …"
- **What went wrong:** these are exactly the 1-2-3 and 1-or-4 rows F5 had just circled, so half the problem took him one minute of looking up.
- **Smallest fix:** replace them with "5, 10, 15, 20, 25, 30, …" (rule 1, 2, 3, 4) and "2, 8, 10, 16, 18, 24, …" (rule 1, 4, 5). I checked both lists by computer.

**10. Grades 4–5, p.4, Problem 7: "Write W or L for each pair of piles with 0 to 8 counters each."** It is an 81-cell grid with no question attached. *(Past minute 40.)*
- **What went wrong:** F5 asked "What's this for?" He filled cells without a goal, and his errors spread through the grid.
- **Smallest fix:** end with "Which pairs are losing pairs?"

**11. Grades 4–5, p.5, Problem 8: "…the smallest of the numbers 0, 1, 2, 3, … that is not the number of a pile you can move to."** *(Past minute 40.)*
- **What went wrong:** in a packet where piles are named by how many counters they hold, F5 read "the number of a pile" as its size. That reading gives 0 for every pile from 5 to 20 and leads to the wrong verdict on 12 and 18.
- **Smallest fix:** call it a label: "Give each pile a label… An empty pile gets label 0. Any other pile gets the smallest of 0, 1, 2, 3, … that is not the label of a pile you can move to."

---

## Quick child's engaged minutes (out of about 40)

| Band | Quick child | Engaged minutes | Where they are at minute 40 | Ran out of work? |
|---|---|---|---|---|
| K–1 | First grader F | about 33 | Problem 6 | No |
| Grades 2–3 | Quick third grader Q | about 32 | Problem 7 | No, but only just; about 6 of his 10 minutes on Problems 2 and 5 were racing |
| Grades 4–5 | Fast fifth grader F5 | about 31 | Problem 5 | No |

Lost minutes, by band:
- **K–1:** about 3 minutes of shading in Problem 3, and the repeated sheet in Problem 5.
- **Grades 2–3:** Q raced Problems 2 and 5 and spent about 2 minutes guessing in Problem 3.
- **Grades 4–5:** F5 raced Problem 1, spent about 5 minutes copying in Problem 3, and needed only a minute for the two look-up lists in Problem 5.


=================== Report 3: mathematical check ===================

# Mathematical review: Week 7 take-away games (base draft)

Method: I rendered all 15 pages (5 per band) and read every one, then checked each problem with my own script (`scratch/verify.py`). The script does the following:
- computes W/L labels by backward induction;
- brute-forces the two-pile games directly, without using Grundy values;
- tries every plan in 2–3 Problems 2 and 5 against every possible partner reply, flagging illegal moves;
- brute-forces 4–5 Problem 5 over all rules {1} ∪ C with C ⊆ {2..19} and |C| ≤ 5;
- finds the start and period of the 4–5 Problem 9 pattern by checking up to 2000.

I also checked every counter picture, table and grid against the source coordinates and the rendered pages.

Overall, the mathematics is sound. Every intended answer exists and is correct, and every plan can be carried out in every line of play. Every "find them" or "is it possible" task has the answer the page implies. I found two issues, both on the K–1 packet. Grades 2–3 and grades 4–5 check out completely.

---

## Located problems

### 1. K–1, page 4, Problem 8: the winning rule for two piles is ambiguous, and the answers depend on it

Quoted text: "Take 1 or 2 counters from one of the two piles on each turn. For each pair of piles, circle whether you want to go 1st or 2nd." The pictures show the pairs 2|2, 1|2, 3|3 and 1|4.

The only winning rule a K–1 child hears is the packet-wide line "Take turns taking counters from **the pile**. Whoever takes **the last counter** wins." That line was written for one pile. With two piles, a young child (or the non-mathematician parent reading aloud) can easily take "the last counter" to mean the last counter of a pile, so that emptying either pile wins. The 2–3 and 4–5 versions of this problem avoid this by saying "whoever takes the very last counter wins". The K–1 version does not.

Evidence (both readings brute-forced):

| Piles | Intended reading (very last counter) | Alternative reading (empty either pile) |
|---|---|---|
| 2, 2 | 2nd | **1st** (take both from one pile) |
| 1, 2 | 1st | 1st |
| 3, 3 | 2nd | 2nd |
| 1, 4 | 2nd | **1st** (take the single counter) |

Under the alternative reading, two of the four cases flip, and two of them become one-move wins.

Smallest fix: add the sentence the older bands already use: "Take 1 or 2 counters from one of the two piles on each turn. **Whoever takes the very last counter wins.** For each pair of piles, circle whether you want to go 1st or 2nd."

### 2. K–1, page 5, Problems 9 and 10: the number of rows suggests more ways than there are (minor)

Quoted text:
- Problem 9: "A game starts with 4 counters, and each turn takes 1 or 2. Draw rings around the counters taken on each turn to show every different way the game can go." The box has **7 rows** of 4 counters.
- Problem 10: "Now find every different way a game with 5 counters can go, taking 1 or 2 on each turn." The box has **10 rows** of 5 counters.

Evidence: I enumerated the ordered sequences of 1s and 2s.
- A sum of 4 has **5** ways: 1111, 112, 121, 211, 22.
- A sum of 5 has **8** ways: 11111, 2111, 1211, 1121, 1112, 221, 212, 122.

(These are Fibonacci numbers. On a row of counters, contiguous ring patterns match these sequences one to one, so the count does not depend on how the rings are read.)

A kindergartner, or the parent volunteer, will naturally treat the rows as the number of answers to find. They may then hunt for 2 more ways that do not exist, or fill the rows with repeats or with rings around counters that are not next to each other.

Smallest fix: keep the spare rows, so the page does not give away the count, and add one short sentence to each problem: "Some rows may stay empty." If the organizer prefers, he could instead draw exactly 5 and 8 rows. That gives the count away, but it keeps the task of finding distinct ways.

---

## Problems verified correct (answer key from independent computation)

### K–1
All problems are correct apart from the two issues above.

| Problem | Task | Verified answer |
|---|---|---|
| 1 | Moves {1,2}, piles 2–5: go 1st or 2nd | 2: 1st, 3: 2nd, 4: 1st, 5: 1st |
| 2 | Moves {1,2}, piles 4, 5, 7, 8: cross out a winning take | 4: take 1, 5: take 2, 7: take 1, 8: take 2. Each move is unique. All four piles are winning, so the instruction can always be carried out. |
| 3 | Moves {1,2}, piles 1–12: color where 2nd is better | 3, 6, 9, 12 |
| 4 | Ben moves first and always takes 2 when he can: where can you beat him? | Piles 3, 4, 6, 7. You cannot beat him at 2 or 5. |
| 5 | Moves {1,2,3}, piles 1–12 | 4, 8, 12 |
| 6 | Moves {1,3}, piles 1–12 | 2, 4, 6, 8, 10, 12 |
| 7 | Pile of 20 under each rule | {1,2}: 1st; {1,2,3}: 2nd; {1,3}: 2nd |
| 8 | Two piles, moves {1,2}, "very last counter" reading | 2,2: 2nd; 1,2: 1st; 3,3: 2nd; 1,4: 2nd. See issue 1. |
| 9, 10 | Every way a game can go | 5 ways and 8 ways. See issue 2. |

All counter counts in the pictures match their numerals (checked on the rendered pages).

### Grades 2–3
This band checks out completely. Every plan was tested against every possible partner reply, and no plan ever calls for an illegal move.

| Problem | Task | Verified answer |
|---|---|---|
| 1 | Moves {1,2}, piles 4, 6, 7, 9, 11, 12 | first, second, first, second, first, second |
| 2 | Plans with moves {1,2} | Mia (8, first): wins every time. Leo (10, first): can lose, for example 10, 8, 7, 5, 4, 2, 0. Ana (9, second): wins every time. Sam (11, first): can lose; in fact he loses in all 8 lines of play, for example 11, 10, 9, 7, 6, 4, 3, 1, 0. |
| 3 | Moves {1,3,4}, piles 1–20 | Second at 2, 7, 9, 14, 16; first at all the others |
| 4 | Moves {1,3,4}, piles 25, 30, 37, 50 | first, second, second, first (losing piles leave remainder 0 or 2 when divided by 7) |
| 5 | Plans with moves {1,3,4} | Kai (10, first, always takes the most): can lose, for example 10, 6, 5, 1, 0. Theo (7, second, copies his partner): can lose, for example 7, 6, 5, 4, 3, 2, 1, 0. Zoe (9, second): wins every time; her "take all" step only happens at piles 4 or 1, where it is legal. |
| 6 | Jon's claim about {1,2,4} versus {1,2} | Jon is wrong. Both rules have losing piles 3, 6, 9, 12, 15, and they stay the same at least up to 500. |
| 7 | Two piles, moves {1,2} | 5,5: second (copy the partner's move in the other pile); 3,6: second; 1,5: first; 2,5: second |

### Grades 4–5
This band checks out completely.

| Problem | Task | Verified answer |
|---|---|---|
| 1 | Moves {1,2}, piles 1–15, and a pile of 100 | Second at 3, 6, 9, 12, 15. With 100, go first: take 1, then always make each pair of turns add up to 3. |
| 2 | Moves {1,3,4}, W/L for piles 1–30 | WLWWWWL repeating; L at 2, 7, 9, 14, 16, 21, 23, 28, 30 (remainder 0 or 2 when divided by 7) |
| 3 | Seven rules, losing piles 1–24, pairs with the same losing piles | Three pairs: {1,2} and {1,2,4} (multiples of 3); {1,3} and {1,3,5} (even piles); {1,4} and {1,4,6} (remainder 0 or 2 when divided by 5). There are no other coincidences up to 24, and each pair stays identical up to 2000. |
| 4 | Kai always takes the most | Under {1,3,4}, his move hands his partner a winning pile at 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29. His move always leaves a losing pile only for {1,3} and {1,3,5}. For the other rules, the first pile where it fails is 4 for {1,2}, 5 for {1,2,3}, 8 for {1,4}, 5 for {1,2,4} and 9 for {1,4,6}. |
| 5 | Find a rule (including 1) for each list of losing piles | 4, 8, 12, …: {1,2,3}. 2, 5, 7, 10, …: {1,4}. 3, 7, 10, 14, …: {1,2,6}. 3, 5, 8, 10, …: impossible. Pile 2 must be winning, so 2 must be an allowed move. Then 5 can move to the losing pile 3, so 5 cannot be losing. A brute-force search found no rule. |
| 6 | Two piles, moves {1,2}, piles 0–7 | A pair is losing exactly when both piles leave the same remainder when divided by 3. Checked by brute force up to 30 by 30. |
| 7 | Two piles, moves {1,3,4}, piles 0–8 | Losing pairs (with the smaller pile first): the 9 equal pairs from 0,0 to 8,8, plus 0,2; 0,7; 1,3; 1,8; 2,7; 3,8; 4,6. All of these are pairs of piles with equal numbers from Problem 8. |
| 8 | Pile numbers (Grundy values) for {1,3,4}, piles 0–20, and two pairs | 0,1,0,1,2,3,2 repeating. 11 and 13 (both numbered 2) are a losing pair. 12 and 18 (numbered 3 and 2) are a winning pair: take 1 from the 12 to reach 11 and 18. Both results were confirmed by brute force of the two-pile game. |
| 9 | Moves {1,6,9}, W/L for piles 1–40, and where the pattern starts to repeat | L at 2, 4, 7, 12, 14, 17, 19, …, 39. From pile 10 on, the pattern WWLWL repeats every 5 (checked up to 2000). Before that, pile 9 is the only pile from 1 on that breaks the pattern. That makes the task a fair one: careless reading gives "repeats from the start". |
