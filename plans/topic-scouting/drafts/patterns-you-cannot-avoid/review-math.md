# Mathematical review: Patterns you cannot avoid (draft v1)

Reviewer: independent math critic (CRITIC-MATH stage). I did not edit the draft. I checked everything with my own code: exhaustive enumeration of strips, Schur colourings and edge colourings of five and six dots, and a full game-tree search of the strip game. I parsed every TikZ picture in `draft/src/*.tex` (square counts, sizes, labels, counter positions, comb windows, dot counts, line counts and regularity) and looked at every rendered page. Scripts: `/tmp/claude-0/-home-claude/d1d23a10-bfbf-5b59-a13a-5f6afdbf2b0f/scratchpad/ramsey-mc-22973/code/check_math.py` and `parse_tex.py` in the same folder.

## Verdict

Every mathematical claim the pages rely on is correct, and so is every intended answer. Every diagram matches its text: strips are numbered 1..n with the right lengths, the given counters sit on the stated squares, comb windows are over the squares named in the example, the 5-dot boards are complete regular pentagons with 10 lines, and the 6-dot boards are complete regular hexagons with 15 lines. Nothing is impossible where the page assumes it is possible, or the reverse.

The located problems below are about whether instructions can be carried out as written, wording that admits a reading with a different answer, and answer space that suggests a different count. None of them is a wrong answer.

## What each problem asks, and the verified answer

Independent results used throughout:
- Good red/blue strips with no one-colour equally spaced three, for lengths 3 to 10: 6, 10, 14, 20, 16, 6, 0, 0. The six of length 8 are RRBBRRBB, RBRBBRBR, RBBRRBBR, BBRRBBRR, BRBRRBRB and BRRBBRRB. The largest spacing on 9 squares is 4, so combs with spacings 1 to 4 catch every three.
- Sums where x = y is allowed, two colours: the longest is 1..4, coloured only RBBR or BRRB, and 1..5 has no colouring. The dead ends 1..3 = RBR and BRB cannot reach 4.
- Sums where x ≠ y, two colours: the longest is 1..8, coloured only RRBRBBBR or BBRBRRRB.
- Sums where x = y is allowed, three colours: the longest is 1..13, with 18 colourings of 1..13. (For x ≠ y with three colours the longest is 23. That is not used.)
- Five dots: 12 of the 1024 colourings have no one-colour triangle.
- Six dots: every colouring has at least 2 one-colour triangles, and 1760 colourings have exactly 2. No colouring with 8 red and 7 blue lines avoids one, so Sim cannot end in a draw.
- Strip game (any colour on any empty square; whoever completes a one-colour three loses): perfect play is a draw on 3 to 8 squares. On 9 squares the second player wins, and every game on 9 has a loser.

### K–1
| Problem | Asks | Intended answer | Check |
|---|---|---|---|
| Opening rule picture | Comb over 2, 4, 6 showing RRR (✗); comb over 1, 4, 7 showing RBR (✓) | Illustrates the rule | Windows lie over exactly those squares; both triples are equally spaced |
| P1 (p. 1) | Make the 4, 6 and 7 strips good | Possible (10, 20 and 16 ways) | ✓ |
| P2 (p. 2) | Make 8 good; can 9 be good? | 8 yes; 9 no | ✓ |
| P3 (p. 2) | Finish 7 with R at 2, 3; 8 with R at 1, 2; 8 with B at 2, 4; 8 with R at 5, 8 | Each has exactly one completion: BRRBBRR, RRBBRRBB, RBRBBRBR, RBBRRBBR | ✓ (all unique) |
| P4 (p. 3) | Play the strip game on 9 | Every game has a loser; the second player can always win | ✓ (not claimed on the page) |
| P5 (p. 3) | Same game on 8; can it end full with nobody losing? On 9? | 8 yes; 9 no | ✓ |
| P6 (p. 4) | Find every good strip of 8 | 6 | ✓ |

### Grades 2–3
| Problem | Asks | Intended answer | Check |
|---|---|---|---|
| Rule picture | Comb over 2, 5, 8 | Matches the "2, 5, 8" example | ✓ |
| P1 (p. 1) | Longest good strip (strips of 6 to 9 given) | 8 | ✓ |
| P2 (p. 2) | Every good colouring of 8 | 6 | ✓ |
| P3 (p. 3) | Can 9 be good? Explain | No. One accessible argument: each of the 6 good 8-strips fails at square 9 whichever colour it gets | ✓ |
| P4 (p. 3) | Every colouring of cards 1 to 4 with no one-colour x + y = z (x = y allowed) | 2: RBBR and BRRB | ✓ |
| P5 (p. 4) | Can 1 to 5 be coloured? Explain | No | ✓ |
| P6 (p. 4) | Colour the 10 lines of five dots with no one-colour triangle | Possible (red pentagon with blue star, 12 ways in all) | ✓ |
| P7 (p. 5) | Sim; can it end with 15 lines coloured and nobody losing? | No | ✓ |
| P8 (p. 5) | Three colours, x = y allowed: how far? | 13 (15 circles per row) | ✓ |

### Grades 4–5
| Problem | Asks | Intended answer | Check |
|---|---|---|---|
| P1 (p. 1) | Longest good strip, and all colourings of that length | 8; 6 colourings | ✓ |
| P2 (p. 2) | Can 9 be good? Explain | No | ✓ |
| P3 (p. 2) | Two colours, x = y allowed: how far, and why not further | 4; 5 is forced impossible | ✓ |
| P4 (p. 3) | Five dots with no one-colour triangle, as many ways as possible | 12 on labelled dots, all of the form "red 5-cycle plus blue complementary 5-cycle" | ✓ |
| P5 (p. 4) | Sim; can it end with nobody losing? | No | ✓ |
| P6 (p. 4) | Can six dots avoid a one-colour triangle? Explain | No (pigeonhole) | ✓ |
| P7 (p. 5) | Fewest one-colour triangles on six dots | 2 | ✓ |
| P8 (p. 6) | Two colours, x ≠ y: how far? | 8 (12 circles per row) | ✓ |
| P9 (p. 6) | Three colours, x = y allowed: how far? | 13 (15 circles per row) | ✓ |

## Located problems

### 1. K–1, pp. 2–3, Problems 3, 4 and 5: the combs cannot be used on the strips drawn on the page
- **Text and diagram:** The K–1 rule makes "a comb" the judge ("The strip is good if a comb never shows three counters of one color, wherever you slide it."). P3 prints its given counters on page strips with 15 mm squares. P4 ("Play … on the strip of 9 squares … If a comb shows three counters of one color, the player who just moved loses.") and P5 draw their game strips with 14.5 mm squares and red and blue counters beside them, which suggests play on the page.
- **Evidence:** The outline builds the combs for the 25 mm printed strips. The source draws the page strips with sides of 1.7, 1.5, 1.45 and 1.35 cm (`gen.py` `k1()`). I put a 25 mm comb on these strips with its first window over square 1. On 14.5 mm squares the spacing-1 comb shows squares 1, 3, 4, and the spacing-2 comb shows 1, 4, 8. On 15 mm squares the combs show 1, 3, 4 and 1, 4, 8. So a comb on the page checks the wrong squares and can call a bad strip good. The page strips cannot be redrawn at comb scale either: 9 × 25 mm = 225 mm, which is wider than the 215.9 mm Letter page (text width 177.8 mm). Counters sized for 25 mm squares will not fit 14–15 mm squares either, so the givens in P3 cannot simply be covered with counters.
- **Smallest fix:** Make clear that building and play happen on the printed 25 mm strips and the page is for recording. For example, P3: "Put these counters on your strips. Finish each strip so that it is good." P4: "Play … on your strip of 9 squares." Then either drop the page strips from P4 and P5 or keep them only to record a finished game. P1 already works this way ("Color these strips to match").

### 2. K–1, p. 3, Problem 4 (and Problem 5): the losing rule depends on when someone checks
- **Text:** "If a comb shows three counters of one color, the player who just moved loses."
- **Evidence:** Checking one placement means sliding up to four combs over as many as 8 triples (square 5 of 9 lies in 8 equally spaced threes). A one-colour three can easily be missed at the move that makes it. Read literally, whoever moved just before the three is noticed loses, and that can be the wrong player. The outcome then depends on when the check happens, not on who made the three.
- **Smallest fix:** "Check with the combs after every move. If a comb shows three counters of one color, the player who just moved loses." Another option: "The player who makes three counters of one color under a comb loses."

### 3. Grades 4–5, p. 2, Problem 3: "Explain why you cannot go further" can be answered about a dead end that is not the maximum
- **Text:** "Color the numbers 1, 2, 3, … in order, red or blue, as far as you can. … How far can you go? Explain why you cannot go further."
- **Evidence:** A child who colours in order 1 = R, 2 = B (forced by 1 + 1), 3 = R gets stuck at 3: 2 + 2 = 4 forces 4 to be red, and 1 + 3 = 4 forces 4 to be blue. My search confirms that RBR and BRB are valid colourings of 1..3 that cannot be extended. With "in order" read as "without going back", the answer is 3 or 4 depending on choices, and "why you cannot go further" invites an explanation of that particular dead end. The intended theorem is that no colouring of 1..5 exists. The same "in order … how far" wording in 2–3 P8 and 4–5 P8 and P9 has the same weakness, but there the question is exploratory and no explanation is requested. For three colours, only 6 of the 278 in-order maximal sequences (with 1 fixed to one colour) reach 13, and most stop at 9 or 10. So a child's "how far" will usually fall short of the true answer of 13 (or 8 in 4–5 P8) unless they go back and change earlier choices.
- **Smallest fix:** For P3: "How far can you go? Explain why no coloring can go further." Optionally add "You may change earlier colors." to P3, P8 and P9 (4–5) and P8 (2–3), so that "in order" is not read as "no going back".

### 4. Grades 2–3, p. 5, Problem 8 and Grades 4–5, p. 6, Problem 9: a third colour is not in the materials
- **Text:** "Color the numbers 1, 2, 3, 4, … in order with three colors" (2–3 P8). "Use three colors" (4–5 P9).
- **Evidence:** The materials provide only red and blue counters and red and blue pencils, so children cannot do these tasks as written.
- **Smallest fix:** Name the colours ("red, blue and green") and add green pencils, or green counters, to the materials.

### 5. Grades 4–5, p. 1, Problem 1: every recording strip has 9 squares, but every answer has 8
- **Text and diagram:** "What is the longest strip you can make good? Find every good way to color a strip of that length." Below it are eight strips, each numbered 1 to 9.
- **Evidence:** The longest good strip has 8 squares, and its 6 colourings each fill 8 squares. No good colouring fits the drawn 9-square strip (0 of 512), so a child who takes the diagram as the target keeps trying to do the impossible, and Problem 2 only asks about that afterwards. At best each answer leaves square 9 blank. The grades 2–3 packet avoids this by offering strips of 6 to 9 for "longest" and then 8-square strips for "every way".
- **Smallest fix:** Follow the 2–3 layout. Give one strip each of 6, 7, 8 and 9 squares (or let the children use the printed strips) for "longest", and give the "every good way" record as eight 8-square strips. If revealing the length matters, unnumbered 10-square strips would at least not point to 9.

### 6. "Find every" answer space suggests more answers than exist (minor)
- **K–1, p. 4, Problem 6** ("Find every good strip of 8 squares."): 8 blank strips for 6 answers. **Grades 2–3, p. 2, Problem 2**: 8 strips for 6 answers. **Grades 4–5, p. 1, Problem 1**: 8 strips for 6 answers. **Grades 2–3, p. 3, Problem 4** ("Find every way to color the cards."): 6 rows for 2 answers.
- **Evidence:** The counts are 6 and 2 (enumeration above). Young children tend to fill every blank, so the page suggests 8 strips, or 6 card colourings, where fewer exist. This matters most for K–1 and for 2–3 P4, where the page offers three times the true number.
- **Smallest fix:** For 2–3 P4, cut to 3 or 4 rows. For the strips, either keep 8 and have the adult treat the spare strips as trial space, or give K–1 exactly 6 strips. Knowing the target count is a reasonable K–1 scaffold, and it tells the child when they are done.

## Band summary
- **K–1:** The mathematics and diagrams are correct. Problems 1 and 2 above (comb and strip scale; timing of the losing rule) and the K–1 part of problem 6 need attention.
- **Grades 2–3:** The mathematics and diagrams are correct. Problems 4 (third colour) and 6 (P2 and P4 answer space) are minor, and the in-order caveat in problem 3 also applies to P8.
- **Grades 4–5:** The mathematics and diagrams are correct. Problem 3 (P3 wording) and problem 5 (P1 recording strips) are worth fixing. Problem 4 (third colour for P9) and problem 6 (P1 answer space) are minor.
