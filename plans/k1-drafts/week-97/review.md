# Review of draft/k-1.pdf (Week 97 K–1, W97-K-v1)

Reviewer stage. I rendered all 9 pages at 80 and 200 dpi and looked at each one, with zoomed crops of the page-1 strip, the Problem 5 record and the ring pictures. I read `draft/src/gen.py` and `check.py`. I regenerated `k-1.tex` from `gen.py` in a scratch folder and recompiled it: the `.tex` is byte-identical, it builds 9 pages, and there are no overfull or underfull boxes. I checked every answer with my own script, run with `python3 -I`. I also read the existing guide W97-FAC-v3 (launch, p. 2) and the first two pages of W97-35-v2, to check the shared launch and any overlap. The draft was not edited.

## Summary

This is a strong draft that follows the brief closely. Every printed number is correct. The header, footer, page numbers and consecutive "Problem N:" labels match the outline. There are no titles, no encouragement, no hints, no exclamation marks, no Name/Date fields, and no sentence describes a diagram. The squares are filled and drawn with equal scaling. The working board and every group card are at true size: I measured 26.0 mm cells on the board (6 × 6 = 156 mm, which fits inside the 180 mm text width) and on the cards. The page never needs a square's total. Each group card has exactly m cells, so the material enforces the group size and the child never has to count to m. The worked strip shows a group of tiles that does not have the card's shape (a top row plus one tile, moved onto a 2 × 2 card). That quietly heads off the rigid-strip trap. The order of problems carries the development the outline asks for:

- squares leave only some leftovers (P1, P2, P4);
- rectangles can leave what squares cannot (P3);
- the inverse game (P5);
- explanations late (P6, P8);
- the rings (P7, P8).

The P2 box for side 3 is prefilled with a grey "1", which respects "do not set 3 × 3 in groups of 4 as a task". None of the Grades 3–5 problems is copied. The secret game uses groups of 6 rather than 7, and P7 puts groups of 8 inside a different question.

There are two major problems:

1. The printed take-away rule gives the wrong leftover in the most common situation, when a child moves the last tiles onto the card and the card does not fill.
2. The only true-size board is on page 1, but each problem's group card and record boxes are on later pages. In a stapled packet the board and the card cannot both lie flat.

Moderate problems:

- The worked strip does not show the take-away repeating, and one of its arrows points the wrong way.
- The partner game probably comes too late for a K–1 table to reach it in the first hour, and it is the only game.
- Groups of 2, which the band emphasis lists, are missing.
- Kernel 3 stops halfway.
- P1–P3 give no place to answer the question they ask.
- P5 is long for one hearing and has no check at the end.

---

## Major

### 1. The take-away rule names the wrong tiles as the leftover when the card is only partly filled (page 1 rules, so every problem)

Page 1 says: "When the card cannot be filled, the tiles still in the square are the leftover."

The card exists so that a child does not have to count. The natural action is to keep moving tiles onto the card one at a time until the card is full or the square is empty. When too few tiles are left, the child finds out only after moving them, so the tiles that are left over are on the card and the square is empty. Read literally, the rule then makes the leftover 0. Examples:

- In P1, the 1 × 1 square in groups of 3: one tile goes onto the card, the card cannot be filled, and no tile is "still in the square". The page's own rule then says the leftover is 0, but it is 1.
- The 2 × 2 square in groups of 3 ends with one tile on a second, unfinished card, so the same misreading gives 0 instead of 1.
- In P4 (groups of 6), the 2 × 2 and 4 × 4 squares can leave 4 tiles stranded on the card.

The adult will usually catch it. But this rule is read aloud for every problem, and kindergartners will follow it as worded. The Grades 3–5 page avoids the trap ("until fewer than one bundle's worth remain").

**Fix (one sentence).** Replace the third sentence with: "When too few tiles are left to fill the card, those tiles are the leftover." That covers tiles left in the square or on the card. Leave the rest of the rules unchanged.

### 2. The board and the group cards are on different sheets, so a stapled packet cannot be used (page 1 against pages 2–6 and 8)

Every building problem needs three things on the table at once: the board (page 1), that problem's group card (on the problem page), and the record boxes (also on the problem page). The packet is printed single-sided. If it is stapled, as packets in this collection are assumed to be (see the stapled-packet discussion in `plans/topic-scouting/drafts/towers-from-either-end/review.md`), turning to page 2 lays page 1 face down under the packet. A child can then use the board or the card, not both. The brief's own sizing note ("One 6-by-6 board takes about half a page") assumes the board sits where it is used, or on its own sheet.

**Fix.** Make the board a separate sheet at the back, beside the cut-out cards on page 9, which already has to be detached. Then move the shared rules and the worked strip to the top of Problem 1's page. That page has about 128 mm of empty space between the record boxes and the group card, and the strip and rules need about 60 mm. The rules then still sit "at the top of the first page", and the demonstration sits right above the first task. If the reviser keeps the board on page 1, the guide must tell the adult not to staple the packet, or to print page 1 separately. Either way, note it in the guide.

---

## Moderate

### 3. The worked strip does not show the take-away repeating, its last arrow points backward, and it does not match the recording layout (page 1)

- **One group shown, two taken.** The strip shows the full 3 × 3, then the square with 4 tiles greyed and 5 left, one full 2 × 2 card, the cup, and finally the square with 8 tiles greyed and 1 left. The second group of 4 never appears, so a child (or the parent reading) can take "fill the card once" as the whole action. The repetition is the heart of the procedure.
- **Arrow roles.** The three arrows mean different things. The first means "next state". The one from card to cup means "move these tiles". The one from cup to final square reads naturally as "tip the cup back into the square". AGENTS.md: "give arrows a clear role or remove them."
- **Recording convention.** In P1–P4 the side number sits under each square and the leftover box sits under the number. The strip has no side label, and its box floats to the right of the final picture. A worked visual should show the record exactly as the problems use it.

**Fix.** Show both card-fills. Either draw two full cards going into the cup, or use two panels (5 left, then 1 left), each next to a full card. Drop the cup-to-square arrow, or keep only plain "next" arrows between square states. Put "3" under the starting square and the box holding "1" under the "3", the same arrangement as the P2 row. No added text is needed.

### 4. The partner game is the only game, and the table will probably not reach it in the first hour (P5, sequencing)

Estimated workload (an estimate for an unpiloted packet, not an observation):

- P1, P2 and P4 each build sides 1–6, which is 91 tile placements and about 91 tile moves onto cards. The card-fills are 29 for P1, 22 for P2 and 13 for P4.
- P3 is 43 tiles and 9 fills.
- The guide's own K–1 route used sides 1–5 for groups of 3 and 4 (55 tiles, 17 and 13 fills) and estimated about 15 minutes for the two together. The draft's P1 and P2 together are about 65% more work than that.

At K–1 handling speed, P1–P4 can easily fill 35–40 minutes. In that case the table never plays the secret square. That is kernel 2, the partner play the outline says "suits partner play", and the one problem where the other player checks the rules. Three nearly identical build-and-record pages in a row is also a lot of the same action for kindergartners. More examples should reveal a distinction, not just repeat a procedure.

Separately, P5 shows only one configuration, groups of 6 with cards 1–6. Kernel 2's main point is that "the answer depends on the group size and on which side cards are allowed", and one configuration cannot show that.

**Fix options (pick one).**

- (a) Move P4 and P5 (groups of 6, then the game) to follow P1. Groups of 6 is the quickest square build (13 fills), and the game with groups of 6 needs at most 6 fills per round behind the folder, so the guesser waits less. P2, P3 and the rest follow.
- (b) Add a short early game round right after P2: groups of 4, cards 1–5. Leftover 1 hides 1, 3 and 5, and 0 hides 2 and 4, with at most 6 fills per round. Keep the groups-of-6 game later. The two rounds then show that the same leftover hides different squares for different group sizes.

Avoid an early groups-of-3 game. A 6 × 6 square behind the folder means 12 fills while the guesser waits.

### 5. Groups of 2 are missing, although the band emphasis lists them (coverage)

The emphasis says the children "take away groups of 2, 3, 4 and 6". The draft uses 3, 4, 6 and 8. Groups of 2 is the smallest counting demand at the table. It gives the leftover pattern 1, 0, 1, 0, 1, 0, which a square shares with its side, and that pattern is the even/odd fact that P6's explanation rests on. It also makes a real contrast with P2. For squares, groups of 2 and groups of 4 give exactly the same leftovers, while for plain numbers they do not: 2, 3, 6 and 7 counters leave different amounts in groups of 2 and of 4.

**Fix.** Add a problem such as "Build each square and take away groups of 2. Which squares leave 1?" It could use sides 1–5, since a 6 × 6 square in groups of 2 means 18 fills. Place it where it does not push the game later: right after P2 as a contrast, or as an optional kindergarten entry at the start if the game moves up under item 4. If the reviser decides to leave it out, the guide should say so and why.

### 6. Kernel 3 stops halfway: P7 is thin, and the even squares and "leftover 1 hides three cards" are missing (P7, P8)

- **P7 is a short task.** It has three squares with 0, 1 and 3 card-fills (35 tiles), and the 1 × 1 is trivial. That is about 3–4 minutes, under the five-minute standard.
- **The rest of kernel 3 is missing.** The outline also has the even squares in groups of 8 (sides 2, 4 and 6 leave 4, 0 and 4), the conclusion that a square in groups of 8 leaves only 0, 1 or 4, and the composite surprise that "leftover 1 hides every odd square the side cards allow (1, 3 and 5 among sides 1 to 6)". None of these is on the pages. The packet shows only that odd squares leave 1.
- **P8 has no room.** P8 asks "Explain how you know", but its record box ends about 19 mm above the footer. The only room for an explanation is the picture itself. P6, by contrast, has about 115 mm free for the same kind of question.

**Fix.** After P8, add a groups-of-8 secret-square round with cards 1–6. The answers are: leftover 1 hides 1, 3 and 5; 4 hides 2 and 6; 0 hides only 4. That brings in the even squares, shows the three-way hiding, and is the quickest game (at most 4 fills per round). It reuses P5's record layout. Give P8 its own page, or more space, by moving the new round or P8 to a fresh page. Optionally say "Without building" in P8 to match P6. A 7 × 7 square (49 tiles) fits the kit, so building it is possible. Either choice is fine, but the two explanation problems should match.

### 7. P1–P3 give no place to answer the question they ask (P1, P2, P3)

P1 asks "Can a square leave 2?", P2 asks "Can a square leave 2 or 3?" and P3 asks "Can a rectangle leave 2 or 3?". Each page has record boxes for the leftovers but nowhere to mark the answer to the question itself. P4 has a row of numerals to circle. The adult can take the answer orally, but the inconsistency means the decision that is the point of each page leaves no trace.

**Fix.** For P1 and P2, either rephrase in P4's form ("Circle every number a square can leave.") with numerals 0 1 2 (P1) and 0 1 2 3 (P2), or keep the yes/no question and accept an oral answer. The find-all form fits the emphasis ("decide which leftovers a square can and cannot make") and is just as open.

**Caution for P3.** Do not change it to "every number a rectangle can leave" with the current four rectangles. They leave 2, 2, 0 and 3, so a find-all would wrongly suggest that rectangles cannot leave 1. Within sides of 6 or less, the only non-square rectangle that leaves 1 is a 1 × 5 strip. Keep P3 as a yes/no question.

P3 also settles "yes" with its first rectangle (3 × 2 leaves 2). Putting the 4 × 3 first (it leaves 0, as a square might) keeps the question open a little longer at no cost.

### 8. P5 is long for one hearing, has no check at the end, and its targets are small (P5)

- **Too long for one hearing.** The first sentence holds four actions: picks, builds behind the folder, takes away groups of 6, shows only the leftover. The standard asks for "one or two short sentences" that make sense after one hearing. A tighter version: "One partner secretly builds the square on one of these cards and takes away groups of 6. The other partner sees only the leftover and circles every card that could have made it."
- **No check.** The builder works unseen, and nothing ends a round. With no reveal, the guesser cannot check that the true card is among the circled ones, and a take-away mistake behind the folder goes unnoticed. The context asks for rules "enforced by the materials or by the other player wherever possible". Adding "Then show the card." (three words) lets the other player check, and it does not change the goal, which is still to circle every possible card.
- **Small targets.** The circling targets are 9.5 mm cards with 4 mm gaps (13.5 mm pitch). Circling two non-adjacent numerals, such as 1 and 5 or 2 and 4, with a crayon is fiddly for kindergartners. The page has about 75 mm free below the six rows, so the rows can be enlarged, for example to a 17–18 mm pitch.

---

## Minor

9. **"filled in like this one" (page 1).** "This one" has no clear antecedent when read aloud. The board directly below is empty, and the filled square is the first picture of the strip. "Build each square on the board with no gaps" or "Build each square on the board, filled in" works without pointing. If item 2 moves the board, "on the board" still works.

10. **Line break in P2.** "Can a square leave 2" / "or 3?" breaks the phrase across lines. Use non-breaking spaces (`2~or~3`).

11. **The 6 × 6 in groups of 3 (P1).** The brief flagged it: "6-by-6 means 12, which is likely to be slow for a kindergartner." The draft keeps it with no response. Side 6 completes the repeat (1, 1, 0, 1, 1, 0), so keeping it is defensible. But the guide should say an adult may stop at 5 for kindergartners, or the reviser could leave the side-6 box visibly optional. This is not needed if item 4(a) shortens the route to the game.

12. **The 1 × 3 group card (P1) could suggest straight runs.** This is a hypothesis, not observed. A child copying the card's shape might take only straight runs of three from the square. In a 2 × 2 square that gets stuck at 4, the trap the brief describes. The page-1 strip already shows a group that does not match the card's shape, which helps. If the reviser wants more protection, the three cells could sit in a non-line arrangement. Otherwise a guide note ("any tiles") is enough.

13. **The board's alternating L-shading (page 1).** This is a hypothesis. The shaded bands (1, 3, 5) are L-shapes, and they may compete with the thick square outlines for a kindergartner's eye. A child told to build "the 3" might fill only the shaded 3-band (5 cells). The brief already warns that kindergartners may build outlines. Outlines alone, or a lighter tint, would remove the cue. The shading is not wrong, and it previews the odd-number growth from Handouts 1. If it is kept, the launch should show a filled square on the board.

14. **"From the middle out" against a board anchored at a corner (P7).** The rules say "Build each square on the board", but P7's squares grow from a middle tile. On the board the middle must go at cell (2,2) for 3 × 3 and at (3,3) for 5 × 5, and a child will not know that. P7 can be built on the table instead. Nothing needs to change on the page, but the guide should mention it.

15. **Launch vocabulary.** The shared launch (guide p. 2) uses loops, "bundles" and "output". The K–1 pages use a card, a cup, "groups" and "leftover", as the outline does. The page-1 strip re-demonstrates the K–1 action, so the pages are fine. The guide should tell the K–1 adult to bridge the words at the table and at sharing time.

16. **Card sheet per child.** Page 9 is in every child's packet, so the table gets four card sets where two (one per pair) are needed. That is preparation, so it belongs in the guide (cut one set per pair). Single-sided printing keeps the card backs blank, which suits secret picking.

17. **Grey "1" in P2.** Keep it. It honours the outline. If the strip is revised (item 3), draw the strip's record exactly like this prefilled box so children see the connection.

---

## Answer check (independent)

All answers below were recomputed by repeated take-away in my own script. Every printed number on the pages is consistent with them.

| Problem | Task | Answer |
|---|---|---|
| P1 | sides 1–6, groups of 3 | leftovers 1, 1, 0, 1, 1, 0. A square never leaves 2, true for all sides because the leftovers repeat every 3. Fills 0, 1, 3, 5, 8, 12. |
| P2 | sides 1–6, groups of 4 | 1, 0, 1, 0, 1, 0. Never 2 or 3, for all sides. The prefilled "1" for side 3 is correct. |
| P3 | 3 × 2, 5 × 2, 4 × 3, 5 × 3 in groups of 4 | 2, 2, 0, 3. Yes, a rectangle can leave 2 and can leave 3. |
| P4 | sides 1–6, groups of 6 | 1, 4, 3, 4, 1, 0. Circle 0, 1, 3, 4; 2 and 5 never occur. Sides 1–6 are one full repeat, so the page's evidence settles the answer for every square. |
| P5 | cards 1–6, groups of 6 | 1 → {1, 5}; 4 → {2, 4}; 3 → {3}; 0 → {6}. |
| P6 | 9 × 9 and 10 × 10, groups of 4 | 1 and 0. Neither fits the 64-tile kit, so "Without building" is honest. A pair's kit cannot build either, though the table's two kits together (128) could. |
| P7 | 1, 3, 5 in groups of 8 | 1, 1, 1. The rings hold 8 and 16 tiles. |
| P8 | 7 × 7 in groups of 8 | 1. The outer ring holds 24 = 3 groups. |
| Cards | page 9 and P5 mini cards | Each card n shows an n × n dot square, n = 1–6. |
| Ring colouring | P7, P8 | Colour alternates by ring, measured from the middle. Correct for 1, 3, 5 and 7. |

## Coverage against the brief

- **Kernel 1** (squares leave only some leftovers; rectangles can leave anything): covered by P1–P4, with the explanation for groups of 4 in P6. The groups-of-3 strip explanation is adult-only, which is appropriate.
- **Kernel 2** (one leftover can hide several squares): covered by P5, one configuration only (item 4).
- **Kernel 3** (odd squares leave 1 in groups of 8): P7 and P8 cover the odd squares. The even squares and the three-way hiding are missing (item 6).
- **Emphasis**: groups of 2 missing (item 5). Everything else is present. No square total is needed, sides are at most 6 for building, and groups are at most 8.
- **Materials**: only the additions the brief allows (cup, folder, one card sheet). True size is correct. No group is a rigid piece. A filled square is shown.
- **Overlap with W97-35-v2**: none copied.

## Keep

- The group card on each problem page, at true size with m cells.
- The worked group that does not match the card's shape.
- The prefilled launch case in P2.
- P4's complete-repeat design: sides 1–6 settle groups of 6 completely.
- Groups of 6 for the secret game (rich answers, short waits).
- P6's "without building" question, which the kit size makes honest.
- The ring colouring in P7 and P8.
- The plain, short wording of P1–P4 and P6.
