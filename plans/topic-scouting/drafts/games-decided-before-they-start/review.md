# Review: Games decided before they start, draft v1

Reviewed: `draft/k-1.pdf` (7 pages, Problems 1–8), `draft/grades-2-3.pdf` (6 pages, Problems 1–8), `draft/grades-4-5.pdf` (8 pages, Problems 1–10), and the sources in `draft/src/`. I rendered every page at 80 dpi, zoomed to 200–300 dpi on the rule pictures, the Problem 1 bar tables and the Problem 10 drawings, read all three `.tex` files and `bmc.sty`, and re-ran `check_games.py`.

## Verdict

The packet is close. The mathematics is right, the progression in each band is sound, and the pages follow the format: no titles, no encouragement, no Name/Date fields, no hints, and consecutive numbering. Fix five things before it goes to the organizer:

1. The token rule, as worded, lets a child draw a loop at a dot that has only one token left. That breaks the invariant the whole week is built on.
2. The header announces the discovery on every page.
3. The bar problems use up more single-use card bars than the materials list provides.
4. Grades 2–3 never record how many lines a 2-Sprigs game takes, yet Problem 6 asks them to explain the winner for 10 and 25 dots.
5. In K–1 "last break wins", nobody switches who goes first.

The other items below are moderate or cosmetic.

## What I checked and found correct

- **Bar counts.** Every answer printed or implied is right: 2×2 takes 3 breaks, 2×3 and 1×6 take 5, 3×3 takes 8, 2×4 takes 7 and 3×4 takes 11.
  - 2–3 Problem 3: the 1st player wins 4×5 and 6×6; the 2nd player wins 3×5, 5×5 and 1×9. That gives a good mix, and the odd-by-odd bars are among them.
  - 4–5 Problem 3: 7×9 is a 2nd-player win (62 breaks), 8×13 a 1st-player win (103) and 25×40 a 1st-player win (999). Starting with a 2×3 and a 2×4 bar gives 2 pieces growing to 14, so 12 breaks, a 2nd-player win.
  - Random break orders in `check_games.py` gave only one count for each bar.
- **K–1 Problem 8.** The three groups are valid splits of a 2×3, a 3×3 and a 3×4 bar (areas 6, 9 and 12). They have 3, 5 and 7 pieces, so they took 2, 4 and 6 breaks. The trap of answering squares − 1 (5, 8, 11) is a good one.
- **2-Sprigs.** A game always lasts n moves; exact search for n ≤ 3 and random play for n ≤ 6 agree. The outline's argument holds: a dot with one free end is the end of a path, and both ends of a path lie in the same region. So the board answers are:
  - 2 dots and 4 dots (2nd player wins): K–1 Problems 4 and 5; 2–3 Problem 4; 4–5 Problem 4.
  - 3 and 5 dots (1st player wins): K–1 Problems 4 and 6; 2–3 Problems 4 and 5.
  - 6 dots (2nd player wins): K–1 Problem 7; 2–3 Problem 5.
  - 2–3 Problem 6: the 2nd player wins with 10 dots, the 1st with 25.
- **Sprouts.** A 1-spot game always lasts 2 moves. A 2-spot game lasts 4 or 5 (second-player win under best play). A 3-spot game lasts 6 to 8 (first-player win).
  - 2–3 Problem 8 ("Can the players' choices change who wins?") is answerable from the 4- and 5-move games.
  - 4–5 Problem 7: 3·10 − 1 = 29. Random search reached 3n − 1 for n ≤ 4 (11 moves for 4 spots). See minor item 14 on whether it can be reached for 10 spots.
- **Brussels Sprouts.** Random play gives exactly 3 moves for 1 cross, 8 for 2 and 13 for 3; 10 crosses gives 48 (4–5 Problem 9).
- **4–5 Problem 10 drawings.**
  - Drawing 1 has 5 dots, 4 lines and 1 region.
  - Drawing 2 has 4 dots, 5 lines and 3 regions.
  - Drawing 3 has 2 dots, 3 lines (one of them a loop) and 3 regions.
  - Drawing 4 is a legal finished 1-cross game of 3 moves, checked against the TikZ coordinates. It has 4 crosses, 6 lines between crosses and 4 regions, with exactly one free arm in each region. The lower bar at (9,−18…−26) clears the loop's lowest point (about y = −10.8), so nothing crosses.
  - V − E + F = 2 holds in all four.
- **Board geometry.** Dots are at least 40 mm apart on every board; the closest pair is 41.1 mm, on the pentagon. Crosses are 22 mm across, and arm tips are 28 mm apart on the 2-cross board. The 2-Sprigs, Sprouts and Brussels rule pictures show the right token counts: a loop takes 2 tokens, and a new spot in Sprouts gets 1.
- **Layout.** No overfull boxes in the logs. Nothing overlaps the header or footer. Font sizes are 13.5 pt for K–1, 12.5 pt for 2–3 and 12 pt for 4–5.
- **Launch examples.** The break picture uses a 2×5 bar, which is not a task bar. The rule pictures show single moves, not games.

## Must fix

### 1. The token rule allows an illegal loop (all bands, 2-Sprigs and Sprouts)

*Where:* the rules paragraphs at K–1 p3, 2–3 p3 and p5, and 4–5 p3 and p5.

- K–1 says: "Take away one token for each end of the new line. A dot with no tokens left cannot get another line."
- 2–3 and 4–5 say: "After each line, the other player takes away one token for each end of the line, and a line cannot end at a dot with no tokens left."

Read literally, a loop at a dot with one token is legal. The dot still has its token when the line is drawn, so the line does not "end at a dot with no tokens left". Only afterwards does the partner find a second token missing. The picture shows a loop at a 2-token dot but does not forbid the 1-token case.

This changes the mathematics. With 2 dots, a game could go: A to B, a loop at A, then a loop at B. That is 3 moves, the 1st player wins, and "n dots, n lines" is gone. Children are very likely to try loops at path ends, because loops look like the easy move.

*Fix:* say that each end needs its own token, for example: "Each end of a line uses up one token at its dot, so a loop needs two tokens." Say the same for Sprouts ("…so a loop needs two tokens at its spot"). Once this rule is stated, "A dot with no tokens left cannot get another line" can go in K–1, which keeps the read-aloud rules no longer than now.

### 2. The header gives away the discovery

Every page header reads "Week NN / Games decided before they start / …". That answers several printed questions in advance:

- 2–3 and 4–5 Problem 1: "Can the losing player ever win by breaking in a different way?"
- K–1 Problem 6: "Can the 2nd player win…with 5 dots?"
- 4–5 Problem 5.

It is also false for the Sprouts pages, whose point is the contrast. The header is the only text 2–3 and 4–5 children see on every page.

*Fix:* use a neutral topic, such as "Breaking bars and drawing games", "Bars, dots and spots" or "Counting moves". Keep the outline's title in the catalog and the facilitator guide.

### 3. The bar problems need more card bars than the materials list provides

Card bars cut with scissors are used up, and each "play twice" needs a fresh bar. Per pair:

| Band | Bars used | Total per pair |
|---|---|---|
| K–1 | Problem 1: 2×2, 2×3, 1×6. Problem 2: 3×4, plus more for "Can anyone…do it with fewer?". Problem 3: 3×3 twice, 2×4 twice. | 8 |
| 2–3 | Problem 1: 2×3, 3×3 and 2×4, twice each. Problem 2: 3×4, 1×6, 2×2. | 9, plus retries for "fewest" |
| 4–5 | Problem 1: six bars. Problem 2: the 3×4 bar at least twice, for fewest and most. | 8 or more |

That is at least 16 + 18 + 8 = 42 bars, against "about six bars per pair, so five sets" (30 bars). Each set also needs duplicates the list does not include: two each of 2×3, 3×3 and 2×4, and extra 3×4 bars. Preparation grows to roughly 20–30 minutes of cutting, which is no longer the stated 10–15.

*Fix (choose one, and flag it to the organizer):*

- (a) Make snap-cube slabs the default material for anything played twice, since a slab can be snapped back together.
- (b) Cut the repeats. For example, in 2–3 and 4–5 Problem 1, play the 2×3 bar once and only the 3×3 and 2×4 bars twice, switching who starts. Drop the second 3×4 attempt in 4–5 Problem 2 in favour of pooling the table's results.
- (c) Keep the pages and correct the materials count and prep time in the outline and guide.

The page wording can stay neutral about the material ("bar") in every case. This is a materials decision as much as a page decision, but the pages should not quietly assume bars that will not be on the table.

### 4. Grades 2–3 never count 2-Sprigs lines but are asked to explain them

2–3 Problems 4 and 5 record only the winner (and a prediction). Problem 6 then asks, "Who would win 2-Sprigs with 10 dots? With 25 dots? Explain how you know." The explanation is that a game always has as many lines as dots, and no 2–3 page ever collects that number. Children can guess "odd means the 1st player wins" from four winner results, but the outline asks 2–3 to "say why". The K–1 packet (Problem 5) and the 4–5 packet (Problem 4) both record the count, so 2–3 is the odd one out.

*Fix:* add "Moves: ___" next to "Winner" on the 2–3 Problem 4 boards (as in 4–5 Problem 4), and preferably on Problem 5 as well. This is a record of what happened, not a hint, and it gives Problem 6 its evidence.

### 5. K–1 "last break wins" does not switch who goes first (K–1 Problem 3)

K–1 Problem 3 says "Play two games on each bar". 2–3 and 4–5 say "switching who goes first". Without switching, on the 3×3 bar the same child loses twice. K–1 children will most likely conclude that their partner is better at breaking, not that going second wins. Switching is what separates the position from the person, which is the point of the problem.

*Fix:* "Play two games on each bar, taking turns going first, and circle…" This is still two sentences.

## Moderate

### 6. The "touching another dot" picture shows a legal position (2-Sprigs rule picture, all bands)

The crossed-out fourth box shows three dots on a straight line. That exact picture can arise legally from two moves: left to middle, then middle to right. A child can read the X as "three dots in a row is not allowed" or "a dot can't get a second line". The crossing picture is fine, because crossings cannot arise legally.

*Fix:* let the tokens show what went wrong. Draw the outer two dots with one token each and the middle dot still holding both of its tokens, so it is visible that one line passed through the middle dot without ending there. Another option is to draw the forbidden line as a curve that runs over a dot.

### 7. Problem 10 never says how to count lines, and Drawing 1 is ambiguous (4–5 Problem 10)

Drawing 1 has a straight horizontal line from the left dot, through the middle dot, to the right dot. Many children will count that as one line. They then get 5 − 3 + 1 = 3, and the rule they are looking for fails on the first example.

Drawing 4 depends on the same unstated convention. The loop through the new cross is two lines between crosses, not one. Counted as one curve per move, the drawing gives 3 lines and 4 − 3 + 4 = 5.

*Fix:*
- Bend the horizontal line at the middle dot in Drawing 1, so it plainly has two lines.
- Give the convention once, briefly: "A line runs from a dot to the next dot."
- Keep the cross convention for Drawing 4.

### 8. The last step of Problem 10 rests on a fact no earlier problem shows (4–5 Problems 8–10)

To explain 8 moves for 2 crosses, a child needs three counts after m moves: crosses 2 + m, lines between crosses 2m, and regions 8 at the end. The region count rests on "every region ends with exactly one free arm". Problems 8 and 9 record only the number of moves, so a child arrives at Problem 10 never having looked at regions in a finished game. Drawing 4 shows the pattern once, but the page gives no reason to look for it.

This is the final problem of the packet, at the organizer's table, so it can stay hard.

*Fix:* add "Regions: ___" beside "Moves: ___" in Problem 8 (and in Problem 9) as part of the record. Alternatively, have Problem 10 count the child's own finished 1- and 2-cross games from Problem 8 in addition to the printed drawings. Either way, the data feeding the explanation comes from the child's own play. Keep the argument itself with the adult.

### 9. Sprouts and Sprigs boards are cramped for physical tokens and long games (2–3 Problems 7–8, 4–5 Problem 6; less so 2–3 Problem 4 and 4–5 Problem 4)

The Sprouts boards are 86 × 60–72 mm.

- A 2-spot game ends with up to 7 spots and 5 curves.
- A 3-spot game ends with up to 11 spots and 8 curves.
- The outline also wants physical counters beside every spot: 6 to 9 at the start, plus one for each new spot.

With ordinary 15–20 mm counters, three counters beside each spot take up most of the space between spots. New-spot tokens will have nowhere to sit near their spot. Children's curves are also large and loose. The K–1 boards (88 × 52 up to 140 × 82 mm) are more generous, and the 4–5 Problem 9 Brussels board (180 × 136 mm) is a good size.

*Fix:* print Sprouts boards two per page, at least about 180 × 110 mm each. Give the 3-spot boards in 4–5 Problem 6 a half page each. If page count is a worry, cut the number of boards rather than shrinking them.

Raise with the organizer: printed token circles beside each dot, which the partner crosses out, would enforce the rule just as well on small boards and leave a record. That would change the outline's material, so do not adopt it silently. In any case, mark this as physically untested and rehearse one 3-spot game with the actual counters before printing.

### 10. Pacing: the Sprouts contrast comes late (2–3 and 4–5)

The outline's stated point is the contrast between fixed-length games and Sprouts. Sprouts appears at Problem 7 of 8 (2–3, page 5 of 6) and Problem 6 of 10 (4–5, page 5 of 8). Both bands first play six complete bar games with scissors (about 40 cuts per pair) in Problem 1.

A typical 2–3 pair will be around Problem 5 or 6 when the hour ends, and many will never meet Sprouts. That is acceptable for 4–5, where the outline expects return visits, but in 2–3 it means the contrast often won't happen.

*Fix:* shorten 2–3 Problem 1 (see item 3b), or merge 2–3 Problems 5 and 6 (item 19) to bring Sprouts a page earlier. The facilitator guide can also suggest a route that jumps to Problem 7 after Problem 4 with 15 minutes left.

### 11. Grades 4–5 never ask whether choices change who wins Sprouts (4–5 Problem 6 or 7)

4–5 Problem 6 has children make long and short Sprouts games but stops at "Write how many moves each game lasted." Only 2–3 (Problem 8) asks the contrast question, "Can the players' choices change who wins Sprouts?"

*Fix:* add that question to 4–5 Problem 6. It is one sentence and ties the Sprouts page back to the bar and Sprigs pages.

## Minor

12. **K–1 Problem 7** says "Before you play on this board", but the page has two boards. Use "on each board".
13. **4–5 Problem 5**: "If you decide it never can, explain why" leans toward the answer. "Show how, or explain why it can't happen." keeps it open, and the rest of the sentence ("say who wins 2-Sprigs with any number of dots") can stay.
14. **4–5 Problem 7** asks for "the largest number of moves a game…that starts with 10 spots could last". That assumes 29 can actually be reached. The token argument proves at most 29, and random search here reached 3n − 1 for n ≤ 4. Before the facilitator guide states 29 as the largest, someone should confirm that a 10-spot game can reach it, with a source or a construction. The printed question can stay.
15. **2–3 and 4–5 Problem 1 table:** each bar's label ("2 by 3", "3 by 3") sits about half a millimetre above the next bar's top edge, so the rows look jammed. Add 3–4 mm between rows.
16. **Brussels rule picture (4–5 p6):**
    - The "not allowed" mark is an X, which is a cross turned 45°, in a game whose pieces are called crosses. Use a different mark.
    - In the crossing box, the lines start at the cross centres, not at arm tips, unlike the other two boxes. Draw them from arm tips.
17. **K–1 rules** do not say who removes tokens. The outline and the other two bands say the partner does, and that is what makes the material enforce the rule. Use "Your partner takes away one token…".
18. **Rule paragraphs in the middle of a packet** (pages 3, 5 and 6) are unnumbered blocks that apply only to one game. They fit "rules stated once at the beginning of the activity", since each game is its own activity, and I would keep them. The alternative is to fold each block into the first problem for that game.
19. **2–3 Problem 5** is short: two games, about three minutes. It could be combined with Problem 6 under one question ("Before you play each board, decide who will win… Who would win with 10 dots? With 25?"), which also saves space for item 10.
20. **K–1 2-Sprigs rules** are six sentences read aloud. The change in item 1 lets one sentence go. Keep the rest short.

## Things to keep

- The order within each band: act, then record, then predict, then explain.
- In K–1: Problem 2 ("Can anyone at your table do it with fewer breaks?"), Problem 6 ("Can the 2nd player win…5 dots?") and Problem 8 (the groups of pieces).
- The odd-by-odd bars in 2–3 Problem 3.
- 4–5 Problem 5's question, "Can a game end while some dot still has a token?".
- The cooperative long and short Sprouts games.
- Problem 9's predict-then-play for 3 crosses, before Euler's formula appears.

Each band gets the same mathematical ideas at its own scale, and K–1 has as much to do as the other bands.
