=================== Report 1: adversarial review ===================

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


=================== Report 2: simulated classroom session ===================

# Session simulation: Week 7 / Take-away games (draft in base/)

Materials at every table: counters (plenty), paper, pencils, small whiteboards. Children play in pairs or threes. Work time is about 40 minutes. All sizes below are as printed at 100% on US Letter.

Cast:
- K–1 (parent volunteer, reads each problem aloud exactly as printed): kindergartners Ava and Ben-K, both non-readers who count to about 20; first grader Finn, who reads a few words. Finn is the quickest child at this table.
- Grades 2–3 (mathematician): third graders Quinn (quick, impatient), Sara (strong), Max (middle), Wes (weaker).
- Grades 4–5 (mathematician nearby): fourth graders Dev and Lia; fifth grader Vera (fast).

---

## K–1 (5 pages, 10 problems)

**Opening rule (p1).** The parent reads the rule paragraph. The children have just seen the whole-group demonstration, so taking 1 or 2 makes sense to them right away.

**Problem 1 (p1), piles 1–5. Clock for Finn: 0–5.** The parent reads "Circle the counters you take to be sure to win, or cross out the pile if you cannot be sure to win." The kindergartners keep "circle the counters" and lose the "or cross out" half after one hearing. Piles 1 and 2 are instant and the children enjoy them. On pile 3, Ava plays Ben-K with real counters. She takes 1, Ben-K takes 1 by mistake, and Ava takes the last one. She says "I can win 3" and circles a counter, so the parent has to explain what "be sure" means. On pile 4, Finn takes 1, then later takes the last 2, and circles all three counters he took over the game. Literally, those are "the counters you take", but the sheet now looks as if he took 3 from a pile of 4, and that move is not allowed. The parent can see the trays at 0.72 cm counters on a 1.0 cm pitch. Children who are engaged play the piles out. Finn takes about 5 minutes and the kindergartners about 7.

**Problem 2 (p1), piles 6–9, 1st/2nd. Finn: 5–11.** The parent reads "Circle 1st or 2nd to show whether you would rather go first or second with each pile." Both kindergartners shout "first" and circle 1st four times in about 20 seconds. Asked whether they would rather go first, a five-year-old always says yes, and the sentence never says the choice is about winning. The parent re-asks: "which one wins?" Then they play 6 with counters. Finn sees that whatever he takes from 6, the parent can leave 3, and he changes his circle. The kindergartners circle according to whoever won the last game. The \Large 1st/2nd labels are easy to circle. Finn: about 6 minutes.

**Problem 3 (p2), piles 10–12. Finn: 11–14.** This is the same task as Problem 1 with bigger piles. Finn uses "leave 9" from Problem 2 and is done in about 3 minutes, so he is starting to race. The kindergartners count out 10–12 counters reliably and play long games, but they cannot reason backward from 9. They circle a counter in every pile and never cross one out. They are moderately engaged because they are playing.

**Problem 4 (p2), traps 1–20 under {1, 2}. Finn: 14–16.** The parent reads "A pile is a trap if the player whose turn it is cannot be sure to win." Ava asks "what's a trap?" The parent re-reads the same abstract sentence, and it does not connect to anything the children have done. Only after a pause does the parent say "like the ones you crossed out." Finn copies 3, 6, 9, 12 from Problems 1–3 and counts three boxes at a time on the track to get 15 and 18. That is about 2 minutes, mostly copying. The kindergartners put X's where Finn does. The 1.65 cm boxes are easy to mark.

**Problem 5 (p2), Ben takes 2 first. Finn: 16–22.** The parent reads "Ben always starts by taking 2 counters. Circle each pile where Ben can still be sure to win after that." Two things go wrong:
- Ben-K hears "always ... taking 2" and plays Ben taking 2 on every turn. From a pile of 5 he gets stuck: "Ben can't take 2, there's only 1."
- Problems 1 and 3 have trained everyone to circle the counters that get taken, so Ava circles 2 counters in each of the six trays. The parent can no longer tell which piles she meant.

Once the parent sorts out "first turn only", Finn plays all six piles and finds 5, 8, and 11. This is good, engaged work, about 6 minutes.

**Problem 6 (p3), every way a game of 4 and of 5 can go. Finn: 22–29.** The parent reads it twice. "Different way" is not defined. Finn asks whether "1 then 2" is different from "2 then 1", and the parent cannot answer from the page. She guesses yes. The page prints 8 rows for 4 counters and 10 rows for 5. Finn finds the 5 ways for 4 counters (1111, 112, 121, 211, 22). The parent sees three empty rows and says "there must be three more," so Finn fills them with repeats. With 5 counters he finds 6 of the 8 ways, then starts copying. Recording fails at this size:
- The counters are 0.72 cm across, with gaps of 0.43 cm sideways and 0.58 cm between rows.
- The kindergartners' loops around a pair spill into the neighbouring counter and the row above, so a 2 and a 1 look the same.
- Nobody can check the rows for duplicates afterwards.

The kindergartners stop after 2–3 rows. Finn is engaged for about 4 minutes and bored for about 3.

**Problem 7 (p3), traps 1–20 under {1, 2, 3}. Finn: 29–34.** The rule is clear. There are no pile pictures, so the children use counters. Finn finds that 4 is a trap, then 8, and guesses "every 4". The kindergartners test 1–5 with counters and then wander. Finn: about 5 minutes.

**Problem 8 (p4), two piles, 1st/2nd. Finn: 34–40.** The words "1st" and "2nd" sit directly under the left and right piles (confirmed at 150 dpi), so they read as labels on the piles. Ben-K circles "2nd" under the bigger pile, meaning "take from that one". Ava again circles 1st everywhere, because once more the sentence asks what she "would rather" do. When the parent restates the task, Finn gets (1,1), (2,2), and (3,3) as 2nd by playing. He is unsure about (2,3) and (1,4). Finn: about 6 minutes.

**Problem 9 (p4), two piles of 6.** Finn has time left at minute 40 and does not run out. If he reaches this problem, he plays 12-counter games and may notice "do the same thing in the other pile". The answer is spoken. The parent can tell it worked but cannot tell whether it is the whole answer.

**Problem 10 (p5), misère traps 1–20.** The parent reads "Now there is one pile again, and whoever takes the last counter loses." The last single-pile game the children played (Problem 7) allowed 1, 2, or 3, so Finn asks "can we take 3?" The parent cannot tell from the page: Problem 7 said 1, 2, or 3; Problem 8 said 1 or 2. Which rule is right changes the answer: 1, 4, 7, … under {1, 2}, but 1, 5, 9, … under {1, 2, 3}.

Result: Finn still had Problems 9 and 10 left at minute 40. He was engaged for about 33 of the 40 minutes. The time he lost went to copying in Problem 4 and the padded rows in Problem 6. The kindergartners worked mainly on Problems 1–3, 5, and part of 8, and lost several minutes to the "rather", "circle", and "always" misreadings.

---

## Grades 2–3 (5 pages, 8 problems)

**Problem 1 (p1), {1, 2}, piles 5–10. Quinn: 0–4.** Quinn plays a pile of 5 twice against Sara, sees "leave 3", and fills the table in about 4 minutes. Wes plays every pile and writes "first" for most of them, because Max misplays. Wes takes about 12 minutes. The table cells (1.15 cm tall) are fine.

**Problem 2 (p1), Lee and Mo. Quinn: 4–6.** Both claims use piles that Problem 1 has already settled: 10 means take 1, and 12 is a multiple of 3. Quinn writes "Lee right, 3 each time. Mo wrong, take 2 to leave 6" in under 2 minutes. He is racing. Sara and Max spend about 6 minutes and write real explanations.

**Problem 3 (p2), {1, 3, 4}, Jo leaves 7, Kai leaves 8. Quinn: 6–12.** This is the first contact with the new rule. Max takes 2 out of habit and has to be corrected. Quinn works out 1–6 with counters, then shows that from 7 every reply can be answered: 6→2, 4→0, 3→0. He groans at "all the way to the end of the game" and writes a cramped half-tree. Kai's 8 falls quickly once 7 is known. The 10.5 cm of space is enough. Quinn: about 6 minutes, engaged. Wes is still here at minute 30.

**Problem 4 (p2), {1, 3, 4}, piles 1–20. Quinn: 12–18.** Quinn already has 1–8 from Problem 3. He sees "+5, +2" by 14 and 16 and finishes in about 6 minutes. The 1.6 cm boxes leave room for "1 or 3".

**Problem 5 (p3), piles 30, 50, 61, 100. Quinn: 18–21.** Quinn extends the pattern by adding 5 and 2 alternately up to 100. It is mechanical, about 3 minutes. Sara notices that it repeats every 7.

**Problem 6 (p3), {1, 3, 5}. Quinn: 21–25.** Quinn shades the evens quickly. He writes "all moves are odd so even goes to odd, then I take 1." That is about 4 minutes, partly racing.

**Problem 7 (p4), two piles, {1, 2}. Quinn: 25–31.** The only equal pair is (3,3). Quinn says "Second, because 3 is a trap and 3 is a trap." To "When the two piles are the same size, which player can always win? Explain why", he answers "Second, because both piles are traps." That reason is wrong for every equal pair that is not a multiple of 3. No case on the page tests it, so his wrong reason survives. The mathematician has to invent a (4,4) case on the spot. Wes briefly reads "First" and "Second" as labels on the two piles, which is the same layout problem as K–1 Problem 8. The instruction sentence sorts him out. Quinn spends about 6 minutes on (4,2), (4,1), and (5,3) by playing them.

**Problem 8 (p5), a rule with losing piles at multiples of 5. Quinn: 31–38.** Quinn guesses "take 1, 2, 3, or 4" by analogy with the 1-or-2 game and checks it in about 3 minutes. For "a different rule" he tries "2 or 3". At a pile of 1 nobody can move, and he asks who wins, which the page never says. He then tries "1 or 4" and "1, 2, 3", which fail. Around minute 38 he declares that no other rule exists.

**Quinn at minute 38–40: out of work.** Nothing is left in the packet. He asks for more, and the mathematician hands him a 4–5 page. Of about 38 minutes, roughly 30 were engaged. Problem 2 and Problem 5 were raced through.

---

## Grades 4–5 (6 pages, 9 problems)

**Problem 1 (p1), {1, 3, 4}, piles 1–24. Vera: 0–7.** Vera builds the chart from 1 upward with counters and then by reasoning. By 21 and 23 she sees that it repeats every 7. Dev and Lia take about 14 minutes. The 1.4 cm boxes work.

**Problem 2 (p1), piles 100, 1000, 2026. Vera: 7–11.** Vera divides by 7: 100 is losing, 1000 means take 4, 2026 means take 1 or 3. Dev adds 7s on scrap paper for 2026 and takes about 8 minutes.

**Problem 3 (p2), four games on strips 1–20. Vera: 11–19.** The 0.78 cm strip boxes shade fine. Vera is surprised that {1, 2, 4} gives the same pattern as {1, 2}, and she finds {1, 4} gives 0 and 2 mod 5 and {1, 3, 5} gives the evens. It is engaged work, about 8 minutes. The fourth graders find four strips long but stay with it.

**Problem 4 (p3), Dana always takes as much as she can. Vera: 19–24.** Lia asks what Dana does in {1, 3, 4} with 2 counters left, since "the rule allows" 4. She wonders whether Dana takes both. The mathematician answers. Vera finds failing piles of 4, 5, and 8 for {1, 2}, {1, 3, 4}, and {1, 4}, and explains why {1, 3, 5} always works ("odd minus odd is even"). About 5 minutes.

**Problem 5 (p3), why the Problem 1 pattern continues forever. Vera: 24–30.** Vera, with a nudge, checks each remainder mod 7. Dev writes "because it keeps repeating" in 1 minute and stops, because he cannot see what an answer would look like. The mathematician has to step in.

**Problem 6 (p4), games with moves from 1–6 whose losing piles are the multiples of 4. Vera: 30–38.** Dev and Vera both first read "whose allowed moves come from the numbers 1, 2, 3, 4, 5, and 6" as the single game where you may take 1 to 6. They compute that its losing piles are the multiples of 7 and say "there aren't any." The phrase does not say that a game can use only some of the numbers. The mathematician clarifies. Vera then finds {1, 2, 3} and starts testing additions. Testing {2, 3, 5}, she hits a pile of 1 where nobody can move and asks who wins. Same gap as in grades 2–3 Problem 8. At minute 38 she has 3 of the 4 games: {1, 2, 3}, {1, 2, 3, 5}, and {1, 2, 3, 6}.

**Problems 7–9 (pp. 4–6).** Vera is starting Problem 7 at minute 40, so Problems 8 and 9 are unused reserve. The packet holds more than the hour, as it should. A child who reaches Problem 8 asks about the square at row 0, column 0, where there is no game. The question comes up, but it does not spread errors to other squares.

Vera was engaged for about 38 of the 40 minutes.

---

## Problems the simulation exposed

Ordered by how much session time they cost.

1. **Grades 2–3, too little work for the quick child (whole packet, ends p5, Problem 8).** Eight problems, and Quinn reaches the end of Problem 8 at minute 38 with nothing left. Problems 2, 5, and 6 each take him 4 minutes or less. **Fix:** add a Problem 9 with a 20-box chart. For example: "Now whoever takes the last counter loses. On each turn a player takes 1, 3, or 4 counters. Shade the box of every starting pile from 1 to 20 where you would rather go second." In make.py, that is one more `problem(...)` call with `chart(20)`.

2. **K–1, p1 Problem 2 and p4 Problem 8: "Circle 1st or 2nd to show whether you would rather go first or second".** Asked what they "would rather" do, kindergartners always want to go first. Both circled 1st everywhere in seconds, and the page never says the choice is about winning. **Fix:** in both problems, write "Circle 1st or 2nd to show which player can be sure to win with each pile."

3. **K–1, p4 Problem 8 layout (also grades 2–3, p4 Problem 7).** "1st" is printed directly under the left pile and "2nd" directly under the right pile. Ben-K read them as names for the two piles and circled the pile to take from. **Fix:** in `two_pile_panel` (make.py lines 108–109), set both words close together and centered under the pair, as in K–1 Problem 2, instead of at 0.25 and 0.75 of the case width.

4. **K–1, p3 Problem 6: 8 rows for 4 counters and 10 rows for 5 (counters 0.72 cm, gaps 0.43 cm sideways and 0.58 cm between rows).**
   - The extra rows told the parent and Finn that more ways existed, so Finn padded them with repeats.
   - Kindergartners' loops swallowed neighbouring counters and spilled into the next row, so the records could not be read or checked.
   - "Different way" was undefined, and the parent had to guess whether order matters.

   **Fix:** print exactly 5 and 8 rows, at about 1.5 cm horizontal and 1.8 cm vertical spacing (P6 then fills the page and Problem 7 moves to the next). Add "Taking 1 then 2 is different from taking 2 then 1." If the organizer would rather not reveal the count, keep 8 and 10 rows and add "Some rows may stay empty."

5. **K–1, p5 Problem 10: "Now there is one pile again, and whoever takes the last counter loses."** "Again" points back to Problem 7, which allowed 1, 2, or 3. The parent could not say which moves are allowed, and the answer depends on it. **Fix:** "Now there is one pile again. Each player takes 1 or 2 counters, and whoever takes the last counter loses."

6. **K–1, p2 Problem 5: "Ben always starts by taking 2 counters. Circle each pile where Ben can still be sure to win after that."**
   - Ben-K heard "always taking 2" and played Ben taking 2 on every turn.
   - Ava circled 2 counters in every tray, the habit from Problems 1 and 3, so her pile choices were unreadable.

   **Fix:** "Ben goes first and takes 2 counters. Put a check by each pile where Ben can still be sure to win."

7. **K–1, p1 Problem 1 and p2 Problem 3: "Circle the counters you take to be sure to win".** On a pile of 4, Finn circled every counter he took during the whole game (3 of 4), not his move. **Fix:** "Circle the counters you take now to be sure to win, or cross out the pile if you cannot be sure to win."

8. **Grades 2–3, p4 Problem 7: the only equal pair is (3,3), followed by "When the two piles are the same size, which player can always win? Explain why."** Quinn explained it as "both piles are traps." That is true for 3 and 3 but is not why equal piles lose, and nothing on the page tests it. **Fix:** replace (3,3) with (4,4) (make.py line 299). Each single pile of 4 is a winning pile, so only the copying idea explains the result.

9. **Grades 4–5, p4 Problem 6: "Find every game whose allowed moves come from the numbers 1, 2, 3, 4, 5, and 6".** Two of the three children read this as the single game {1, …, 6} and answered "none." **Fix:** "Choose some of the numbers 1, 2, 3, 4, 5, 6 to be the allowed moves. Find every choice whose losing piles are exactly the multiples of 4. Explain why your list is complete."

10. **K–1, p2 Problem 4: "A pile is a trap if the player whose turn it is cannot be sure to win."** After one hearing the definition meant nothing to the kindergartners, and the parent had to invent the link to the piles they had crossed out. **Fix:** "A pile is a trap if you cannot be sure to win when it is your turn, like the pile of 3."

11. **Grades 2–3, p1 Problem 2: Lee with 12 counters, Mo with 10.** Both piles are already settled by the Problem 1 table, so Quinn finished in under 2 minutes. **Fix:** move the claims past the table. Lee: "With 21 counters, I will go second and always win…" Mo: "With 20 counters, I will go first and take 1, and then I can always win." Lee is still right, Mo is still wrong, and the answer is take 2 to leave 18.

12. **Grades 2–3, p5 Problem 8 and grades 4–5, p4 Problem 6: what happens when no move is possible.** Children testing rules without 1, such as {2, 3} or {2, 3, 5}, reached a pile of 1 and asked who wins. The page never says. **Fix:** add to the rule paragraph at the top of page 1 in both packets: "If you cannot take any counters, you lose."

13. **Grades 4–5, p3 Problem 4: "Dana's plan is to always take as many counters as the rule allows."** Lia could not tell what Dana does when the pile is smaller than the biggest move, such as 2 counters under {1, 3, 4}. **Fix:** "Dana's plan is to always take the biggest number of counters she is allowed to take from the pile."

14. **K–1, p2 Problems 3 and 4 overlap.** Problem 4's track repeats piles 1–12, which Problems 1–3 already settled. Finn spent about 2 minutes on it, mostly copying X's. **Fix:** start Problem 4's track at 13 (boxes 13–20), or drop Problem 3 and let Problem 4 carry 10–12.

---

## Quick child's engaged minutes (out of about 40)

- **K–1 (Finn, first grader):** about 33 engaged minutes. He did not run out (Problems 9–10 untouched). He lost time to copying in Problem 4, to padded rows in Problem 6, and to re-reading after the "rather" wording.
- **Grades 2–3 (Quinn):** about 30 engaged minutes. He ran out of work at about minute 38. Problems 2, 5, and 6 were raced through.
- **Grades 4–5 (Vera):** about 38 engaged minutes. She did not run out (Problems 7–9 in reserve). About 2 minutes went to the misreading of Problem 6.


=================== Report 3: mathematical check ===================

# Correctness review: Week 7 take-away games (base draft)

Method: I rendered all 16 pages (K-1: 5, grades 2-3: 5, grades 4-5: 6) and looked at each one. I regenerated the .tex files from `src/make.py` and they match the submitted sources byte for byte. I parsed every TikZ picture to count the counters in each tray and to check the box, strip and grid labels. Then I solved every game by brute force (`scratch/solve.py`, `scratch/solve2.py`): win/lose labels, winning moves, Grundy values, direct minimax on the two-pile games (no Grundy shortcut), a game tree for the claims in 2-3 P3, a minimax against Dana's greedy plan, and a search over all move sets for the "find a rule" and "find every game" problems.

**Overall:** every intended answer is correct, and every diagram matches its text (pile sizes, pair sizes, box and strip numbering, grid labels). No problem is impossible, and no claim on any page is false. I found four wording or layout issues. Two of them (items 1 and 2) can change a child's answer.

---

## Located problems

### 1. Two-pile games: "the last counter" has a second reading that changes the answers (all three bands)

- **Where:**
  - K-1, page 4: Problems 8 and 9.
  - Grades 2-3, page 4: Problem 7.
  - Grades 4-5, pages 5-6: Problems 8 and 9.
- **Text:**
  - The general rule on each page 1 is stated for a single pile: "Two players take turns taking counters from a pile. … Whoever takes the last counter wins."
  - The two-pile problems then say only "Now there are two piles, and on your turn you take 1 or 2 counters from one pile" (K-1 P8) and "Now there are two piles. On each turn, a player takes 1 or 2 counters from one of the piles" (2-3 P7).
  - 4-5 P8 says "…from one of the piles, and whoever takes the last counter wins."
- **The problem:** With two piles, each pile has its own last counter. A child can easily hear "whoever takes the last counter wins" as "whoever empties a pile wins", especially K-1 children, who hear the problem read aloud once. The intended reading is "the last counter of all".
- **Evidence (brute force under both readings, take 1 or 2):**

  | Position | Intended reading | "Empty a pile wins" reading |
  |---|---|---|
  | K-1 P8 (1,1) | 2nd | 1st |
  | K-1 P8 (2,2) | 2nd | 1st |
  | K-1 P8 (1,4) | 2nd | 1st |
  | 2-3 P7 (4,1) | Second | First |

  - Under the second reading, five of the six K-1 cases become "1st". That makes the problem nearly trivial and destroys the contrast the author built in with (1,4).
  - The 4-5 P8 grid also changes completely. Under the intended reading the "second" squares are exactly those with a ≡ b (mod 3). Under the other reading, every square with a pile of 1 or 2 is a first-player win.
- **Smallest fix:** Name the winning counter explicitly in each two-pile problem.
  - K-1 P8: "Now there are two piles. On your turn, take 1 or 2 counters from one pile. Whoever takes the very last counter on the table wins."
  - 2-3 P7: add "Whoever takes the last counter on the table wins."
  - 4-5 P8: change "whoever takes the last counter wins" to "whoever takes the last counter on the table wins".
  - P9 in K-1 and in 4-5 refers back to P8, so it is covered.

### 2. K-1, page 5, Problem 10: the move rule is not restated after Problem 7 changed it

- **Text:** "Now there is one pile again, and whoever takes the last counter loses. Put an X on every trap from 1 to 20."
- **The problem:** Problem 7 switched the moves to "1, 2, or 3". Problems 8 and 9 restate "1 or 2", but Problem 10 says nothing about the moves. An adult reading aloud, or a child who starts at this page (the brief allows stopping and starting anywhere), may carry "1, 2, or 3" over from the last one-pile track problem, which is P7.
- **Evidence:** In the misère game the traps depend on the move rule:

  | Moves | Traps from 1 to 20 |
  |---|---|
  | {1, 2} (intended) | 1, 4, 7, 10, 13, 16, 19 |
  | {1, 2, 3} (carried over from P7) | 1, 5, 9, 13, 17 |

- **Smallest fix:** "Now there is one pile again. Take 1 or 2 counters on each turn, and whoever takes the last counter loses. Put an X on every trap from 1 to 20."

### 3. K-1, page 3, Problem 6: the number of blank rows suggests the wrong number of ways

- **Text and diagram:** "Show every different way a game with 4 counters can go, and then every way a game with 5 counters can go." The page gives 8 blank rows of 4 counters and 10 blank rows of 5 counters.
- **Evidence:** The games are the ordered sequences of 1s and 2s with the right sum.
  - 4 counters: 5 ways (1111, 112, 121, 211, 22).
  - 5 counters: 8 ways (11111, 1112, 1121, 1211, 122, 2111, 212, 221).
  - A K-1 child, or the adult, who sees 8 rows and 10 rows will expect 8 and 10 ways. They may keep searching, or fill the extra rows with repeats, on a "find all" task whose real answer is 5 and 8.
- **Smallest fix:** In `make.py`, change `range(8)` to `range(5)` and `range(10)` to `range(8)` so the page shows exactly 5 and 8 rows.
  - If the organizer would rather not reveal the count, keep spare rows but make the difference obvious and not suggestive. For example, put one extra row in each column, so a child can see a spare row is left over.

### 4. Grades 4-5, page 5, Problem 8: the row 0 / column 0 square is not a playable starting position

- **Text:** "row 0 or column 0 stands for an empty pile. Shade every square where you would rather go second."
- **The problem:** Square (row 0, column 0) is two empty piles. No counter is ever taken, so the page's rule ("whoever takes the last counter wins") does not decide who wins, and "would you rather go first or second" has no answer. In the backward-induction sense it counts as a loss for the player to move. A careful child will be stuck on it, or will argue either way.
  - The rest of row 0 and column 0 is fine: those squares are one-pile games. For example, (0,3) and (0,6) are "second" squares.
  - In P9 the task asks only for unequal piles from 1 to 8, so the corner square is not part of that task.
- **Smallest fix:** Cross out or grey out the top-left square of the grid, in P8 and, for consistency, in P9. The alternative is to say "Shade every other square where…". The text would not need to say anything else.

---

## Bands checked with no further problems (verified answers)

### K-1 (moves 1 or 2, last counter wins, unless stated)

| Problem | Verified answer |
|---|---|
| P1 | 1 → take 1; 2 → take 2; 3 → cross out; 4 → take 1; 5 → take 2. The winning move is unique in each pile. |
| P2 | 6: 2nd; 7: 1st; 8: 1st; 9: 2nd. |
| P3 | 10 → take 1; 11 → take 2; 12 → cross out. |
| P4 | Traps 3, 6, 9, 12, 15, 18. |
| P5 | After Ben takes 2, he can be sure to win only at 5, 8, 11 (they leave 3, 6, 9). At 4, 7, 10 he cannot. |
| P6 | 5 ways and 8 ways. See item 3 for the row counts. |
| P7 | Moves {1, 2, 3}: traps 4, 8, 12, 16, 20. |
| P8 | (1,1) 2nd; (1,2) 1st; (2,2) 2nd; (2,3) 1st; (3,3) 2nd; (1,4) 2nd. Checked by direct minimax. |
| P9 | (6,6): the second player wins by copying each move in the other pile. |
| P10 | Misère {1, 2}: traps 1, 4, 7, 10, 13, 16, 19. |

All tray counts match their labels: 1-5; 6-9; 10-12; 4, 5, 7, 8, 10, 11; the six P8 pairs; 6 and 6.

### Grades 2-3

| Problem | Verified answer |
|---|---|
| P1 | 5: first, take 2. 6: second. 7: first, take 1. 8: first, take 2. 9: second. 10: first, take 1. |
| P2 | Lee is right: 12 is a multiple of 3 and his reply always restores a multiple of 3. Mo is wrong: 10 − 2 = 8, so the opponent takes 2 (leaving 6) and then makes 3 each round. Mo should take 1. |
| P3 | Jo is right; 7 is losing under {1, 3, 4}. Full tree from 7: partner takes 1 → 6, Jo takes 4 → 2, partner must take 1, Jo takes the last. Partner takes 3 → 4, Jo takes 4. Partner takes 4 → 3, Jo takes 3. Kai is wrong: from 8 the partner takes 1, leaving 7. Kai's winning move from 12 was 3. |
| P4 | Shade 2, 7, 9, 14, 16. In every other box, take 4 at 4, 6, 11, 13, 18, 20; take 3 at 5, 12, 19; take 1 at 1, 8, 15; take 1 or 3 at 3, 10, 17 (two correct answers there). |
| P5 | 30: second. 50: first, take 1. 61: first, take 3. 100: second. |
| P6 | {1, 3, 5}: shade the even piles. Every move is odd, so the number of moves has the same parity as the pile. From an even pile the second player makes the last move however anyone plays. |
| P7 | (3,3) Second; (4,2) First; (4,1) Second; (5,3) First. The second player wins on equal piles by copying. See item 1. |
| P8 | {1, 2, 3, 4} works. A rule works exactly when it contains 1, 2, 3 and 4 and no multiple of 5; 64 such rules use numbers up to 12. A different rule therefore has to add a non-multiple of 5 above 5, for example {1, 2, 3, 4, 6}. The task is solvable as posed. |

The P7 diagram pairs (3,3), (4,2), (4,1), (5,3) match.

### Grades 4-5

| Problem | Verified answer |
|---|---|
| P1 | {1, 3, 4}: shade 2, 7, 9, 14, 16, 21, 23. The winning first moves are as in 2-3 P4, plus 22 → 1 and 24 → 1 or 3. |
| P2 | 100: losing (100 mod 7 = 2). 1000: winning, take 4. 2026: winning, take 1 or 3 (2026 mod 7 = 3). |
| P3 | {1, 2}: multiples of 3. {1, 2, 4}: multiples of 3. {1, 4}: 2, 5, 7, 10, 12, 15, 17, 20 (remainder 0 or 2 mod 5). {1, 3, 5}: the even numbers. |
| P4 | Greedy fails in {1, 2} (e.g. 4), {1, 3, 4} (e.g. 5) and {1, 4} (e.g. 8; 3 is fine because only 1 is allowed there). Checked by minimax with Dana greedy on every turn. It always wins in {1, 3, 5}, because every play wins from an odd pile. |
| P5 | The {1, 3, 4} pattern (losing iff n mod 7 is 0 or 2) holds for every n. |
| P6 | Exactly 4 games: {1, 2, 3}, {1, 2, 3, 5}, {1, 2, 3, 6}, {1, 2, 3, 5, 6}. Searched all 63 subsets, checked to n = 1000. |
| P7 | Misère {1, 2}: 1, 4, 7, 10, 13, 16, 19. Misère {1, 3, 4}: 1, 3, 8, 10, 15, 17. Both are the normal-play pattern shifted up by one. |
| P8 | "Second" squares are exactly those with a ≡ b (mod 3). Equal piles are a second-player win. See items 1 and 4. |
| P9 | The unequal pairs from 1 to 8 are exactly {1,3}, {1,8}, {3,8}, {2,7}, {4,6}: 5 pairs. Grundy values 0,1,0,1,2,3,2 repeat with period 7. Confirmed by direct minimax. |

All strip, chart and grid labels are correct: 1-24; 1-20 on each strip; grids 0-7 and 0-8.
