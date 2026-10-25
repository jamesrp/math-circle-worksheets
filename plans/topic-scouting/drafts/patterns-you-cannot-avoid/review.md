# Review: Week NN, Patterns you cannot avoid (draft v1)

Reviewed: `draft/k-1.pdf` (4 pages, 6 problems), `draft/grades-2-3.pdf` (5 pages, 8 problems), `draft/grades-4-5.pdf` (6 pages, 9 problems), and `draft/src/` (gen.py, verify.py, build.sh). I rendered every page at 80 dpi and the rule diagrams at 200 dpi. Regenerating from `gen.py` in a scratch folder reproduces the three `.tex` files byte for byte and compiles with no overfull boxes. All three packets are US Letter.

## Verdict

This is a strong draft. Every answer the pages depend on is correct (checked independently, below). The three thresholds appear in the right bands. Headers, footers and problem labels follow the standard. There are no titles, no encouragement, no hints and no exclamation marks. Most problems ask a substantial question in one or two sentences.

The problems worth fixing before the organizer sees the draft are practical rather than mathematical:

- The K–1 page strips are too small for the counters and combs.
- One K–1 rule picture can be misread.
- Grades 4–5 record an 8-square answer on 9-square strips.
- Grades 4–5 ask the same question in two problems in a row.
- One open-ended task in grades 4–5 is not well defined.
- The phrase "in order" works against the "how far can you go" questions.
- A third colour is used but never named.

## 1. Mathematics (independently verified)

I wrote my own enumerations rather than relying on `verify.py`:

| Claim the pages rely on | Check | Result |
|---|---|---|
| Good strips of length 3–9: 6, 10, 14, 20, 16, 6, 0 | brute force | correct |
| Six good 8-strips: RRBBRRBB, RBRBBRBR, RBBRRBBR and their swaps | brute force | correct |
| K–1 P3 has one completion per strip: 7 with R at 2,3 → BRRBBRR; 8 with R at 1,2 → RRBBRRBB; 8 with B at 2,4 → RBRBBRBR; 8 with R at 5,8 → RBBRRBBR | brute force | correct. The three 8-strips are the three patterns up to a colour swap. |
| Strip game (either player may use either colour; whoever completes a one-colour equally spaced three loses) | full game tree | 8 squares: a draw with perfect play, lasting all 8 moves. 9 squares: the second player wins, and the first player loses on move 9. |
| Sums, 2 colours, 2+2=4 counts: longest run 1–4, only RBBR and BRRB | search | correct |
| Same with 2+2=4 not counting (4–5 P8): longest run 1–8, only RRBRBBBR and its swap | search | correct |
| Sums, 3 colours, 2+2=4 counts (2–3 P8, 4–5 P9): longest run 1–13 | search | correct. There are 18 colourings of 1–13, which is 3 up to renaming colours. Colouring 1, 2, 3, … greedily without going back gets stuck at 7. |
| Five dots: 12 of 1,024 colourings have no one-colour triangle | brute force | correct |
| Six dots: every colouring has at least 2 one-colour triangles; 1,760 colourings have exactly 2 | brute force | correct |
| Rule diagrams: K–1 combs at 2,4,6 (RRR, ✗) and 1,4,7 (RBR, ✓); upper comb windows at 2,5,8, matching the text | inspected at 200 dpi | match |

No problem is impossible when the page assumes it is possible, or the reverse. Spacings 1–4 cover every equally spaced three on strips up to 9, so the four combs are a complete check.

## 2. Problems to fix

### 2.1 K–1: the page strips are smaller than the counters and combs (all K–1 problems, P3 most of all)

The counters and combs are made for the printed 25 mm strips. The page draws its strips smaller:

| K–1 problem | Square size on the page |
|---|---|
| P1 | 1.7 cm |
| P2 and P3 | 1.5 cm |
| P4 and P5 (game pictures) | 1.45 cm |
| P6 | 1.35 cm |

Counters will not sit on these squares and the combs will not line up with them. That makes the page a record sheet only:

- **P3, "Finish each strip so that it is good."** This is naturally done on the page, since the given counters are printed there. Done on the page, it loses the comb check, which is the material that enforces the rule (the main lesson of the lamp-puzzle session). Done properly, a K–1 child first copies the givens onto a loose strip, then copies the answer back.
- **P4 and P5.** The page draws a 1.45 cm strip, but the game has to be played on the loose strip.

Smallest fix: draw K–1 P3 at the material size, 25 mm squares, so counters and combs go straight onto the page. A 9-square strip is 22.5 cm, and an 8-square strip is 20 cm. Either one fits only on a landscape page; the portrait text width is 17.8 cm. A landscape P3 page with four 25 mm strips would work. In P4 and P5, either draw the strip at the material size or remove the strip picture and keep only the two counters.

### 2.2 K–1 rule picture: the ✓ marks one comb position, not a good strip (page 1)

The right-hand picture shows one comb position (squares 1, 4, 7 showing R B R) with a large ✓. The sentence above it says a strip is good only if no comb shows three of one colour "wherever you slide it". A pre-reader is likely to read the ✓ as "this strip is good" and conclude that one check is enough. There are also two smaller problems:

- In the left picture, squares 1 and 7 are visible and empty, even though the rule says to put a counter on every square.
- In the right picture, the card covers the whole strip, so it no longer looks like a comb on a strip.

Smallest fix: keep only the ✗ picture, which shows what failure looks like, and let the launch show sliding. Alternatively, show one full strip with every square filled and the comb in two positions, without a ✓.

### 2.3 Grades 4–5 P1: 9-square strips record an 8-square answer (page 1)

"What is the longest strip you can make good? Find every good way to color a strip of that length." All eight recording strips have nine squares, but the answer is eight. A child either takes the strip length as a hint that 9 is possible, or has to remember to leave square 9 blank in every row.

Smallest fix: print eight 8-square strips, which matches the 2–3 packet's P2. If showing the length would give the answer away, print unnumbered 10-square strips instead.

### 2.4 Grades 4–5 P5 and P6 ask the same question (page 4)

P5 ends "Can a game end with all fifteen lines colored and nobody losing?" P6 then asks "Can the fifteen lines joining six dots be colored red or blue so that no three dots are joined by three lines of the same color? Explain how you know." Coming one after the other, the first question adds nothing for 4–5. It is also the weaker form of the question: a full Sim board always has 8 red and 7 blue lines.

Smallest fix: in 4–5 P5, replace the last sentence with a strategy question such as "Would you rather go first or second?" Keep P6 as it is. The 2–3 packet can keep the full-board question, since it is that band's only six-dot question.

Facilitator notes, which do not belong on the page:
- With perfect play the second player wins Sim (computer result).
- Children can explain part of this: if nobody has lost before the fifteenth line, that line is red and must complete a red triangle, so the first player loses.

### 2.5 Grades 4–5 P4: "Find as many different ways as you can" has no clear goal (page 3)

There are 12 good colourings of the drawn board. Each colour forms a loop through all five dots, and only two of the twelve look like "outer pentagon, inner star". The page gives four boards and does not say what counts as different. A child who finds the pentagon/star colouring and its swap may stop there, believing that rotations repeat it (they do). A child who goes on cannot record more than four.

Make the goal precise in one of two ways:
- **"Find every way"** (answer 12). Add enough small boards for 12 answers plus spares: 3.8 cm five-dot boards fit four across and four down on one page (16 boards), or 4.5 cm boards spread over two pages. This is a substantial "find all" task for 4–5, and the 4–5 table's adult can ask why every answer is two loops.
- **Ask for one colouring** (as in 2–3 P6). Leave the count to the facilitator guide.

### 2.6 "In order" steers children toward never going back (2–3 P8; 4–5 P3, which P9 inherits)

The wording is "Color the numbers 1, 2, 3, 4, … in order with three colors" and "Color the numbers 1, 2, 3, … in order, red or blue, as far as you can." Saying "in order" prescribes a method. It also suggests that earlier colours are fixed. With three colours, colouring in order without going back gets stuck at 7, but 13 is possible. With two colours, a child who colours 3 red gets stuck at 4 and may answer "3".

The question "How far can you go?" is about the best possible run, so the method should stay open. Smallest fix: delete "in order". In 4–5 P3, also remove the duplicated "as far as you can", since the same sentence asks "How far can you go?". The result: "Color the numbers 1, 2, 3, … red or blue. [rule] How far can you go? Explain why you cannot go further."

### 2.7 The third colour is never named, and it is not in the materials (2–3 P8, 4–5 P9)

"With three colors" does not say which. The materials list has red and blue counters and red and blue pencils only. Smallest fix: write "red, blue and green". Add green pencils to the materials list for the facilitator guide.

### 2.8 Dot boards are about 60% of the specified size and vary in size

The outline asks for boards about 12 cm across. The pages use different sizes:

| Problem | Board size |
|---|---|
| 2–3 P6 | 7.0 cm |
| 2–3 P7 | 7.6 cm |
| 4–5 P4 | 6.8 cm |
| 4–5 P5 | 7.0 cm |
| 4–5 P6 | 6.0 cm |
| 4–5 P7 | 7.0 cm |

They are legible, and the six-dot board's three long diagonals meet at the centre, which avoids extra crossings. Two problems remain:

- Coloured pencil cannot be erased. A trial-and-error task such as 2–3 P6, with two boards, will run out of boards after one or two mistakes.
- Sim is played many times, and each page offers two boards.

Recommendation:
- Use one size for each board type: about 7.5 cm for five dots and about 8 cm for six dots.
- Give 2–3 P6 four boards. Page 4 has room if P5's answer area is trimmed slightly or P6 moves to its own page.
- In the facilitator guide's materials, say that the separate 12 cm boards are the Sim boards and the page boards are spares. This assumes the 12 cm boards are kept.

## 3. Design and sequencing recommendations

These are judgement calls, and none has been piloted.

### 3.1 K–1: put the finish-the-strip puzzles before the hard 8-strip

P2 ("Make the strip of 8 squares good. Can you make the strip of 9 squares good too?") comes second. Yet only 6 of the 256 colourings of an 8-strip are good, so blind trial will mostly fail for a kindergartner. P3 then gives the forced completions, which hand over exactly the skill P2 needed, and three of P6's six answers.

A smoother K–1 route:
1. P1: free strips of 4, 6 and 7.
2. Finish-the-strip puzzles (the current P3).
3. "Make the strip of 8 squares good. Can you make the strip of 9 squares good?"
4. The games.
5. "Find every good strip of 8 squares."

In that last problem, colour swaps and reversals become the mathematics, which is real symmetry reasoning at K–1 scale. If the organizer prefers the present order, it still works because stopping anywhere is fine. The cost is that P2 may be a long, discouraging wall early in the packet.

### 3.2 K–1 P5: give the game a "how to win" question in place of the repeat

P5's second question, "Can a game on 9 squares end that way?", repeats P2's 9-square question. The 9-square game hides a K–1-sized discovery:
- A full 9-strip always contains a one-colour three.
- So if nobody slips earlier, whoever places the ninth counter loses, and that is the first player.
- Perfect play confirms that the second player wins (game-tree search above).
- On 8 squares, perfect play is a draw.

Suggested P5: "Play the same game on the strip of 8 squares. Can a game end with all the squares filled and nobody losing? On the strip of 9 squares, would you rather go first or second?" This uses the threshold the children found in P2, and the standard explicitly wants K–1 to work out how to win games.

### 3.3 K–1 game pictures may suggest one colour per player (P4, P5)

A red counter and a blue counter drawn beside the strip of a two-player game can be read as "red player, blue player". Many young children assume that, and the 2–3 and 4–5 Sim rule really does assign colours. The text says "a red or a blue counter", so this is a risk rather than an error. Drawing a small pile of each colour, or naming it in the launch, would reduce it. The facilitator guide should state it.

### 3.4 Grades 2–3 P4 wording

"When two numbers add up to a third, those three numbers must not all be the same color." Some third graders will hear "a third" as the fraction. The only example given is the special case 2 + 2 = 4. Suggested: "If two of the numbers add up to another one, like 1 + 3 = 4, those numbers must not all be the same color. A number can be added to itself: 2 + 2 = 4, so 2 and 4 cannot be the same color." The 4–5 packet's P3 uses the same SUM_RULE; apply the change there too.

The page gives six recording rows for an answer of two. More rows than answers is normal for a "find every" task, but six is generous; four would do and free space for P5.

### 3.5 Name the triangle once children have used it (grades 4–5 P6, P7; optionally 2–3)

The long phrase "no three dots are joined by three lines of the same color" appears in 2–3 P6, and in 4–5 P4 and P6. 4–5 P7 has its own variant, "as few groups of three dots as possible are joined by three lines of the same color", which is hard to follow when read aloud. By 4–5 P6, children have used the idea twice (P4 and Sim). The standard allows a new word at that point, and "a one-color triangle (three dots joined by three lines of one color)" would shorten P6 and P7 considerably. For example, P7 becomes "Color the fifteen lines joining six dots red or blue with as few one-color triangles as possible. What is the fewest you can get?"

### 3.6 What counts as a triangle in Sim (2–3 P6/P7, 4–5 P4/P5)

On the drawn boards, crossing lines form small visual triangles whose corners are not dots. "Three dots" in the rule excludes them, but this is the classic Sim confusion. The 2–3 table meets triangles for the first time in P6 with only the verbal definition. Under the convention-example rule, a tiny inline picture (three dots joined by three red lines, ✗) beside 2–3 P6 would carry the definition with fewer words. If the 2–3 adult will demonstrate this at the table, it can stay with the facilitator instead.

### 3.7 Bookkeeping risks (hypotheses, not piloted)

**K–1 P4 game.** After every move, the children slide four combs along a 9-strip, which has 16 triples. With four children and one non-mathematician adult, checking may become the main activity. Only the triples through the new counter need checking, but that is a hint for the adult, not page text.

**K–1 P6 recording.** Colouring up to 64 squares with crayons is a fine-motor load at K. Possible relief, all outside the page:
- Allow a colour dot in each square.
- Supply about six 8-strips per pair so found strips can stay built on the table. This needs about 24 counters of each colour per pair, compared with the 10 listed.

**4–5 P7 counting.** Counting one-colour triangles on a six-dot board means checking 20 triples per board. This is reasonable at the organizer's table as a late task.

## 4. Compliance with the student-page standard

**Header and footer.** Each page has "Week NN / Patterns you cannot avoid / Grades …" and "Bellingham Math Circle / Week NN / NN-K-v1 (NN-23-v1, NN-45-v1)" with a page number. Correct.

**Problem labels.** Problems are numbered consecutively in each packet, with no other headings. There are no Name or Date fields, no encouragement, no exclamation marks and no dashes used for asides.

**Shared rules.** The rules appear once at the top of page 1 in each band. The sum rule sits inside the first sum problem and is referred to by problem number afterwards, which is acceptable.

**Explanation requests.** "Explain how you know" appears only where impossibility is the point:
- 2–3: P3 and P5.
- 4–5: P2, P3 and P6.

**Length.** Every band meets the four-page minimum and has more than enough work for 40 minutes.

**K–1 sentence length.** P4 has three sentences of game rules and P5 has three, slightly over the "one or two short sentences" guideline. The game rules are essential, so this is acceptable.

**Diagram descriptions.** No sentence narrates a diagram.

**Bands against the outline.** K–1 does strips, the threshold and the game against the adult. 2–3 finds the longest strip and all its colourings, colours 1–4 by sums, and colours five dots. 4–5 proves 9 squares and 5 numbers impossible, gives the pigeonhole proof of the six-dot theorem, and plays Sim. Everything the outline asks for is present. The extra problems are 2–3 P7 and P8, and 4–5 P7, P8 and P9. They all extend the same three thresholds.

## 5. For the facilitator guide (not student-page changes)

- **Strip game.** On 9 squares the second player wins with perfect play, and the first player always places the losing ninth counter if nobody slips. An adult who goes second and plays well never loses, so let children go second sometimes. On 8 squares, perfect play is a draw.
- **Three-colour sums.** 13 is the maximum, with 18 colourings, which is 3 up to renaming colours. One of them is 1, 4, 10, 13 / 2, 3, 11, 12 / 5–9. Colouring in order without going back stops at 7.
- **Sums where a number cannot be added to itself, two colours.** 8 is the maximum. The colourings are 1, 2, 4, 8 / 3, 5, 6, 7 and the swap.
- **Six dots.** The minimum number of one-colour triangles is 2. One way to get it: two separate red triangles, with the remaining lines blue.
- **Five dots.** There are 12 good colourings, and each colour forms a loop through all five dots.
- **Physical rehearsal.** No physical rehearsal has been done. Before the session, check whether the combs fit the printed strips and whether the counters fit the 25 mm squares.
