# Review: Week 7 take-away games packet (draft in base/)

## Verdict

This is a strong draft. I brute-forced every answer and the mathematics is correct throughout. The contrasting cases are well chosen. Page format and the organizer's banned list are followed almost perfectly. There are no headings beyond the header and labels, no encouragement, no exclamation marks, no hints and no lettered sub-steps. New words come only after the child has used the idea ("trap" in K–1 P4, "losing/winning pile" in 4–5 P2, brace notation in 4–5 P3).

The problems that need fixing are about how the pages work at the table, not about mathematical errors:

- one K–1 problem doesn't say which move rule applies,
- the two-pile pictures carry a labeling trap,
- one K–1 problem has drifted away from this week's ideas,
- K–1 leans on numerals up to 20 more than the standard allows.

Everything below is ranked by how much it would cost the organizer or the children.

## What I checked

- I rendered all 16 pages (K–1: 5, grades 2–3: 5, grades 4–5: 6) and inspected them at 80 dpi, then at 120–150 dpi for the denser pages. All pages are US Letter and nothing overflows or overlaps.
- `src/make.py` regenerates the three `.tex` files byte-for-byte. They compile with pdflatex with no overfull or underfull boxes and no warnings. `base/*.pdf` is identical to `src/*.pdf`.
- I computed every answer by exhaustive search (normal and misère play, two-pile games via Grundy values, Dana's greedy plan against optimal replies, and the "find every rule" problems). The answer key is at the end. Every problem has a well-defined answer that matches its intended point, apart from the ambiguity in finding 1.
- I checked format: the header reads "Week 7 / Take-away games / Grades …" and the footer "Bellingham Math Circle / Week 7" with the page number. Every problem starts with a bold "Problem N:". Packet-wide rules are stated once at the top of page 1. Each band has 4 or more pages and 8–10 problems, which is enough for 40 minutes, and the problems are ordered so that stopping anywhere is fine.

## Findings, most serious first

### 1. K–1 Problem 10 does not say which moves are allowed (Medium-high)

"Now there is one pile again, and whoever takes the last counter loses. Put an X on every trap from 1 to 20."

The last one-pile problem was P7, which used moves 1, 2 or 3, and P7's number strip looks exactly like P10's. P8 and P9 reset the moves to 1 or 2, but those were two-pile games. "One pile again" can therefore reasonably be heard as "go back to P7's game". The two readings give different answers:

- moves 1 or 2: traps at 1, 4, 7, 10, 13, 16, 19
- moves 1, 2 or 3: traps at 1, 5, 9, 13, 17

The adult reading aloud may be the non-mathematician parent and has no answer key, so this ambiguity will reach the children.

A related problem: the K–1 opening sentence states "On each turn, a player takes 1 counter or 2 counters" as if it held for the whole packet, but P7, P8 and P10 each change the game.

Fix: state the moves in P10, for example "Now there is one pile again. Each player takes 1 or 2 counters, and whoever takes the last counter loses." Optionally trim the opening rules so they only claim what is true for the whole packet, or keep them and make sure every problem that changes a rule says so in full.

### 2. In the two-pile pictures, the choice words look like labels for the piles (Medium)

This affects K–1 P8 and 2–3 P7. In `two_pile_panel` the choice words are placed at 0.25 and 0.75 of the case width, which is directly under the centre of each pile's tray. In the render, "1st" sits under the left pile and "2nd" under the right (2–3: "First" and "Second"). A child, or an adult glancing at the page, can easily read these as "first pile" and "second pile".

This is worst in K–1, where the children can't read the instruction and only see the picture. In K–1 P2 (one pile) the same words sit under a single tray and are not ambiguous, so the two-pile layout is inconsistent with the one-pile layout.

Fix: keep both choice words together, centred under the pair, so neither lines up with a pile. For example, place them at about 0.38 and 0.62 of the case width with a visible gap below the trays, or put them on their own line below the frame. Apply the change to both bands.

### 3. K–1 Problem 6 is off this week's ideas and nothing later uses it (Medium)

"Show every different way a game with 4 counters can go, and then every way a game with 5 counters can go."

This is a count of 1-or-2 compositions: 5 ways and 8 ways, the Fibonacci numbers. "Find every way" is a legitimate K–1 activity, but the problem never asks who wins any of the ways it lists. It doesn't connect to traps, winning or strategy, and no later problem uses the result. Every other K–1 problem builds the take-away ideas.

The recording space also has two practical problems:

- 8 rows for 4 counters (5 needed) and 10 rows for 5 counters (8 needed). Young children tend to fill every row they are given, which invites duplicates.
- The rows are 1.3 cm apart with 7 mm counters, leaving about 6 mm between rows for kindergartners to draw loops around groups. That is cramped.

Fix: replace it with a K–1 version of kernel 1's "answer every reply" idea, which K–1 otherwise only meets in P9. For example: "You go first with 5 counters and take 2. Show every move the other player can make, and how you win after each one", with a picture of 3 counters drawn once for each possible reply (two copies). If the counting problem stays, tie it to the game (for example, mark who took the last counter in each way) and give rows with more vertical room.

### 4. Three K–1 problems are bare numeral strips 1–20 (Medium-low)

P4, P7 and P10 are each a strip of boxes holding the numerals 1–20 and nothing else. The standard asks K–1 pages to "lean on pictures and objects" and to "draw every board or position the child needs". In the fall of kindergarten, many children can't yet reliably recognize numerals in the teens. The three strips also look identical, so nothing on the page signals the rule change between them; the only cue is the sentence the adult reads.

Fix options:
- add a small dot picture to each box (two ten-frame-style rows of small dots fit in a 1.65 cm box), or
- picture piles 1–12 as small trays, as in P1–P3, and keep numerals only for the extension to 20.

Either way, the child can count instead of having to read the numeral.

### 5. K–1 Problems 1–4 ask the same question four times (Low-medium)

All four classify piles under the 1-or-2 rule: P1 covers piles 1–5, P2 covers 6–9, P3 covers 10–12 with the same instruction as P1 ("with a bigger pile"), and P4 covers 1–20, which repeats 1–12. The standard prefers "several purposeful, contrasting cases" under one question to many small questions. P3 in particular is a three-case repeat of P1.

The build-up from pictured piles to the numeral strip is defensible for K–1, and repeating a read-aloud instruction has some value. Still, merging P1 and P3 (piles 1–5 plus 10–12, or just 1–8) would free a slot for something new, such as the replacement suggested in finding 3.

### 6. K–1 read-aloud load (Low)

The standard asks for "one or two short sentences" that make sense after one hearing. Some K–1 problems are long or abstract:

- P1 and P3: "Circle the counters you take to be sure to win, or cross out the pile if you cannot be sure to win." This is 22 words with two alternatives in one sentence.
- P4: "A pile is a trap if the player whose turn it is cannot be sure to win." The relative clause plus "cannot be sure to" is hard to take in on one hearing. "A trap is a pile you do not want to have on your turn" says the same thing in plain words.
- P6: about 30 words.
- P9: "Play the game from Problem 8 …" refers to a problem number, which means nothing to a non-reader. "Play the same game with two piles of 6" works better.

### 7. K–1 Problem 9 has nothing to record (Low)

"If you go second, how can you win every time, whatever the other player does?" The picture shows two piles of 6, but the page doesn't say what the child should produce. The standard asks for "a clear statement of what the child should produce". Possible fixes: "Show the adult how", or one or two blank pairs of trays where the child draws a game in progress.

### 8. 2–3 Problem 7 asks for a generalization from a single case (Low)

"When the two piles are the same size, which player can always win? Explain why." Only one of the four pictured pairs, (3,3), has equal piles. The standard says a child should "meet an idea in concrete cases, and use it, before being asked to explain or generalize it". K–1 P8 has three equal pairs. Replacing (5,3) with a second equal pair such as (4,4) or (5,5) would give the 2–3 children a pattern to notice. Keep (4,1), the unequal second-player win, because it is the good surprise.

### 9. 2–3 Problem 3 calls the opponent "partner" (Low)

"…says she can now win however her partner plays." Children who play in pairs may hear "partner" as a teammate. Everywhere else the packet says "the other player"; use that here too.

### 10. 2–3 Problem 8, second part: a leap to note, not necessarily to fix (Low)

Any rule whose losing piles are exactly the multiples of 5 must contain 1, 2, 3 and 4. A *different* rule must therefore add a move that is not a multiple of 5 and is at least 6, such as {1, 2, 3, 4, 6}. Nothing in the 2–3 packet shows that adding a move can leave the pattern unchanged; the 4–5 packet does this with {1, 2} versus {1, 2, 4}. As the last problem, it is a fair stretch for a quick child, so it can stay. Just be aware that most 3rd graders will find {1, 2, 3, 4} and then stall, or will rewrite the same rule in different words.

### 11. Cosmetic and layout (Low)

- The packet-rules paragraph on page 1 of both 2–3 and 4–5 hyphenates "prob-lem" across a line break. Turn off hyphenation for student pages (for example `\hyphenpenalty=10000 \exhyphenpenalty=10000`).
- In the 4–5 P4 table, the header "Does the plan always win?" wraps after "always". Widen the column or shorten the header to "Always wins?".
- The 4–5 P3 and P7 strips use 0.78 cm boxes with the numeral centred. Shading a box with pencil covers its number. Move the numeral to a corner, as `chart()` does, or make the boxes a little larger. The strips fit at 17.7 cm, so there is little room to grow; two rows of 10 would work.
- In K–1 P1, P3 and P5, the counters sit 1.0 cm apart with 7 mm diameter, leaving only about 3 mm between counters. Circling "the counters you take" out of a pile of 11 or 12 is fiddly for kindergartners. A slightly larger pitch would help, and there is room in the trays.
- K–1 page 5 holds only P10 and is about 75% empty. This is harmless. If finding 3 or 5 changes the page count, check that K–1 still has at least four full pages.
- 4–5 P8: the grid includes the (0,0) cell, which counts as "rather go second" because the first player has no move. That is mathematically right and a useful base case, but expect a question about it. No change is needed.

## Things to keep through revision

- K–1 P5 (Ben always opens with 2): every pictured pile is a winning pile, and exactly half (5, 8, 11) survive the fixed opening. A clean K–1 version of testing a claimed strategy.
- K–1 P8 includes (1,4), an unequal pair that is a second-player win. 2–3 P7 has the same surprise with (4,1).
- 2–3 P2 and P3: each pair of claims has one right and one wrong, and the right claim in P3 has a small reply tree that a child can draw in full.
- 2–3 P5 (30, 50, 61, 100) forces the child to extend the period-7 pattern without being told it exists.
- 4–5 P3: {1, 2} next to {1, 2, 4} (same pattern), then {1, 4} (period 5) and {1, 3, 5} (parity). A well-chosen contrasting set.
- 4–5 P4: the greedy plan fails in three games and works only in {1, 3, 5}, with the smallest counterexamples at 4, 5 and 8. This is exactly kernel 2's "greedy is often wrong".
- 4–5 P6 has exactly four answers ({1,2,3}, {1,2,3,5}, {1,2,3,6}, {1,2,3,5,6}) and a short completeness argument. An excellent "why is your list complete" problem.
- 4–5 P9 finds the pairs with equal Sprague–Grundy values without naming them. This is kernel 3 at the right level.

Optional: a quick 5th grader who finishes everything could be given a final problem asking why *every* rule with moves of at most 4 must eventually repeat. That is the pigeonhole argument of kernel 2, which the packet currently covers only for {1, 3, 4} in P5.

## Verified answer key (brute force)

Losing piles, normal play:

| Moves | Losing piles |
|---|---|
| {1,2} | 3, 6, 9, … |
| {1,2,3} | 4, 8, 12, … |
| {1,3,4} | 2, 7, 9, 14, 16, 21, 23 (remainder 0 or 2 mod 7) |
| {1,2,4} | multiples of 3 |
| {1,4} | 2, 5, 7, 10, 12, 15, 17, 20 (remainder 0 or 2 mod 5) |
| {1,3,5} | even piles |
| {1,2,3,4} | multiples of 5 |

Losing piles, misère play:

| Moves | Losing piles |
|---|---|
| {1,2} | 1, 4, 7, 10, 13, 16, 19 |
| {1,2,3} | 1, 5, 9, 13, 17 |
| {1,3,4} | 1, 3, 8, 10, 15, 17 (remainder 1 or 3 mod 7, the normal pattern shifted by 1) |

**K–1**
- P1: take 1 from 1, take 2 from 2, cross out 3, take 1 from 4, take 2 from 5.
- P2: 6 is 2nd, 7 is 1st, 8 is 1st, 9 is 2nd.
- P3: take 1 from 10, take 2 from 11, cross out 12.
- P4: traps at 3, 6, 9, 12, 15, 18.
- P5: Ben wins from 5, 8, 11.
- P6: 5 ways and 8 ways.
- P7: traps at 4, 8, 12, 16, 20.
- P8: (1,1) 2nd, (1,2) 1st, (2,2) 2nd, (2,3) 1st, (3,3) 2nd, (1,4) 2nd.
- P9: copy the other player's move in the other pile.
- P10: with moves 1 or 2, traps at 1, 4, 7, 10, 13, 16, 19.

**Grades 2–3**
- P1: 5 first, take 2; 6 second; 7 first, take 1; 8 first, take 2; 9 second; 10 first, take 1.
- P2: Lee is right. Mo is wrong: from 10 he takes 2, leaving 8, and the other player takes 2, leaving 6.
- P3: Jo is right: from 7, a reply of 1 is answered with 4, a reply of 3 with 4, and a reply of 4 with 3. Kai is wrong: the other player takes 1, leaving 7. Kai should have taken 3.
- P4: shade 2, 7, 9, 14, 16. First moves: 1→1, 3→1 or 3, 4→4, 5→3, 6→4, 8→1, 10→1 or 3, 11→4, 12→3, 13→4, 15→1, 17→1 or 3, 18→4, 19→3, 20→4.
- P5: 30 second; 50 first, take 1; 61 first, take 3; 100 second.
- P6: shade the even piles.
- P7: (3,3) second, (4,2) first, (4,1) second, (5,3) first.
- P8: {1,2,3,4}, plus any rule that adds non-multiples of 5 of 6 or more, for example {1,2,3,4,6}.

**Grades 4–5**
- P1: as 2–3 P4, extended with 21 and 23 losing, 22 take 1, 24 take 1 or 3.
- P2: 100 losing; 1000 winning, take 4; 2026 winning, take 1 or 3.
- P3: see the normal-play table above.
- P4: greedy fails in {1,2} (from 4), {1,3,4} (from 5) and {1,4} (from 8). It always wins in {1,3,5}.
- P6: {1,2,3}, {1,2,3,5}, {1,2,3,6}, {1,2,3,5,6}.
- P7: losing piles are shifted up by one.
- P8: a square is losing exactly when the two piles leave the same remainder after dividing by 3.
- P9: Grundy values for piles 0–8 are 0, 1, 0, 1, 2, 3, 2, 0, 1. The second-player pairs with different sizes are (1,3), (1,8), (3,8), (2,7) and (4,6).
