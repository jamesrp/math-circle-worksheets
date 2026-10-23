# Week 100 (Distance in nested worlds): math check

Scope: the current packet in `lowell-math-circle-year-2/week-100/`, which is `week-100-grades-3-5.pdf` (8 pp., Problems 1–10, the only band) and `week-100-facilitator.pdf` (5 pp.). Both are byte-identical to the reference copies in `source/week-100/reference-pdfs/`. The sources are `source/week-100/student/grades-3-5.tex` and `guide/facilitator.tex` with `guide/solutions.tex`. There are no archive folders. My scripts and their outputs are in the run folder (to be committed as `checks/week-100/`). Checked October 23, 2026.

**Result: every student problem is correct as printed. Every diagram matches its text, and every answer, proof, hint and extension in the guide is true. I found one problem, a minor one: two cross-references in the guide say "page 1" when they mean the guide's own page 1, though the guide uses page numbers everywhere else to mean student pages.** I also give two notes that I did not count as problems.

## How it was checked

- **`check_diagrams.py` reads the delivered PDF itself, not the TeX.** It uses PyMuPDF on the vector and text layers. Output: `check_diagrams.py.out`, 36 checks, 0 failures. Its extracted data goes to `pdf_extract.json`.
  - **Rebuilding the worlds.** It finds the loops (rounded rectangles), cards (10 mm squares) and labels (the digit on each loop's top edge) in the page 1 X/Y/Z example, the Problem 1 world and the Problem 3 world. It works out which cards each loop holds and confirms that loops never cross, that no card straddles a loop and that one loop holds every card. It confirms that labels strictly increase outward, then computes the distances from the smallest common loop.
  - **What the rebuilt worlds give.**
    - The example gives X–Y = 3 and X–Z = Y–Z = 6, as printed.
    - The Problem 1 world is AB@2 ⊂ ABD@4, CE@2 and all six @8. Its 15 distances equal the guide's table on page 3.
    - The Problem 3 world is the same world.
  - **Cut-outs and printed data.**
    - The page 1 label cards are four 2s, two 4s and two 8s.
    - Among the letter-card icons, the square, pentagon and hexagon are regular. The triangle is isosceles (8 mm base, 8.94 mm sides). It only tells the cards apart, so it is not a problem.
    - It reads the six triples on page 2, the ten clue cards on page 4, the A–C = 2 card on page 5, and the number cards 0–7 with the three rules on page 7.
  - **Quotations.** It confirms that every guide and student sentence this report quotes is in the PDFs.
- **`check_math.py` enumerates worlds exactly as page 1 defines them.** It builds trees of loops with at least two children each, labels strictly increasing outward and distance equal to the label of the smallest common loop. (One-child loops are redundant frames and never change a distance.) It does not use the package's `check_math.py`. Output: `check_math.py.out`, 45 checks, 0 failures.
  - **Loop worlds are exactly the strong-inequality tables.** For 2–6 cards, the tables loop worlds can make with labels {2, 4, 8} are exactly the tables with values in {2, 4, 8} where the largest of every three distances occurs at least twice: 3, 12, 60, 358 and 2,471 tables. For 6 cards there are also exactly 2,471 non-redundant labelled loop structures, one per table, so complete data determine the loops.
  - **Problem 6.** No world has a triple with exactly one largest distance. This holds for every world on 3–6 cards with labels {2, 4, 8}, and for every world on 3–5 cards with arbitrary labels 1–6.
  - **Problem 7.** In all 2,471 six-card worlds, with radii 0, 0.5, …, 9 and every centre, overlapping balls are always nested. Moving the centre to any member never changes a ball.
  - **Problem 5.** All 20 single-clue changes, the other reading of the second paragraph and the guide's completeness argument.
  - **Problems 8–9.** The rules against 8·2^(−v(a−b)), the loop realisation, the label count, the balls, all 56 triples and the 2-adic strong inequality on −20…20.
  - **Problem 10.** The adversary witnesses, and an exact minimax search for 3, 4 and 5 cards.

## Grades 3–5: checks out completely

- **Page 1, rules and worked example.**
  - The rules make distance well defined. Two loops that both hold two cards meet, so one is inside the other, and "smallest common group" is unambiguous.
  - The example's arrows are correct: input X, Z; the inner loop 3 misses Z; the thick loop 6 holds both; output 6. X–Y = 3 and X–X = 0 are also correct.
- **P1.** The world is AB@2 inside ABD@4, CE@2, and F joining only at 8. It uses labels 2, 2, 4 and 8, all of which the label cards supply. Any six pairs may be chosen. Rearranging within loops keeps every distance, so the task can always be done.
- **P2 (A–B, A–C, B–C).** Possible: 2,2,2; 2,4,4; 4,4,4; 2,8,8. Impossible: 2,2,4 and 2,4,8, so there are two sets to cross out. The full list of possible triples confirms that no hidden arrangement makes either impossible set.
- **P3.**
  - The page's own examples are right: radius 1 around X gives {X} and radius 4 gives {X, Y}.
  - The radius-3 balls are {A,B} around A, {C,E} around C, {D} and {F}.
  - With radii 0, 1, 2, 3, 4, 7 and 8, the balls containing B are {B} for 0 and 1, {A,B} for 2 and 3, {A,B,D} for 4 and 7, and all six cards for 8.
  - For every listed radius, every ball containing B is the same set whichever card is the centre, so the answer does not depend on whether a child uses only B as the centre.
- **P4.** Among the 358 five-card structures, exactly one fits the ten clues: AB@2, ABC@4, DE@2, all @8. It stays the only one even if any labels from 1 to 8 were allowed. "Two different-looking worlds" can only differ in layout, frame shapes or redundant frames, and the page asks for nothing more. The hidden world is not the Problem 1 world without F (C and D are swapped), so page 1 does not give the answer away.
- **P5.**
  - With A–C = 2, the triple A, B, C reads 2, 2, 4, so no world fits.
  - Of the 20 changes of one clue to another value in {2, 4, 8}, exactly three make a world possible: A–C back to 4, A–B to 4, and B–C to 2. "Find every repair" has a definite, short answer.
- **P6.** No. See the enumeration above; the guide's nesting proof is general.
- **P7.** No and no. See the enumeration above.
- **P8.**
  - The three rules are exactly 8·2^(−v), where v is the number of factors of 2 in a − b. On 0–7, "same remainder after division by 4" is the same as "difference 4". The 1-and-5 example (distance 2) is right.
  - The loops {0,4}, {2,6}, {1,5}, {3,7} @2, evens and odds @4, and all @8 reproduce every distance. They use four 2s, two 4s and one 8, which the label cards supply.
  - The radius-3 balls are the four pairs. The radius-5 balls are the evens and the odds.
- **P9.** All 56 triples have their largest distance at least twice. The number world has no triple with all three distances equal.
- **P10.**
  - The game is well posed: asking all 15 pairs always settles the world.
  - The fewest questions that always suffice is 15. If every answer is 8, then for each pair the all-8 world and the world with just that pair joined at 2 both fit every other answer. Exact minimax search gives 3, 6 and 10 for 3, 4 and 5 cards, which fits the guide's 15 for six.

## Adult guide

The overview and every solution, hint and extension check out except the cross-reference below.

- **Overview.** These claims are all true, with the right hypotheses:
  - the nesting proof of d(A,C) ≤ max{d(A,B), d(B,C)};
  - "largest occurs at least twice", with 2,4,4 and 4,4,4 possible and 2,2,4 not;
  - balls are closed (at most r) and contain their centre; every member is a centre; balls that share a card are nested, so a smaller-radius ball lies inside the larger one;
  - a radius need not be a label;
  - "distance at most r" is an equivalence relation whose classes rebuild the loops, with left/right order arbitrary;
  - one altered clue need not identify the error;
  - the factor-8 scaling of 2^(−v) on 0–7, and the divisibility proof.
- **Solutions.** These all agree with the enumeration:
  - the P1 table;
  - the P2 lists and both impossibility arguments;
  - the P3 balls and radius table;
  - the P4 groups and matrix (including the note about redundant frames);
  - the P5 three repairs and their completeness argument;
  - the P6–7 proofs;
  - the P8 loops and balls, and the P9 case argument;
  - the P10 deductions: AB = 2 and AC = 4 force BC = 4; A at 2 from all five others forces all 2s; 15 in the worst case.
- **Launch.** The launch demonstration (centre X, radius 3, giving {X, Y}) is correct.

## Problem found

### 1. Guide, page 5: two cross-references say "page 1" but mean the guide's page 1, not the student page 1

- **Quoted text:**
  - Under "Problems 6–7, page 6: beyond a few examples": "Exactly one largest distance is impossible by the nested-group argument on page 1."
  - Under "Problems 8–9, page 7: the eight-number world": "The divisibility proof on page 1 explains the wider 2-adic connection."
- **Evidence:**
  - Every solution heading in the guide uses page numbers to mean student pages ("Problem 1, page 1" … "Problem 10, page 8"). So "page 1" here reads as student page 1.
  - Student page 1 holds only the rules, the X/Y/Z example and Problem 1. It has no nesting argument and no divisibility proof (checked in `check_diagrams.py.out`).
  - Both arguments are in the guide's overview on its own page 1, under "Strong triangle inequality" and "Later number world". The mathematics is right; the pointer sends the adult to the wrong sheet.
- **Smallest fix:** in `guide/solutions.tex`, change "on page 1" to "in the mathematical overview" in both sentences.

## Notes, not counted

- **P5, second paragraph: another reading changes the answer.**
  - The printed sentence is "Change exactly one of the ten clues to a different value chosen from 2, 4, 8, so that a world is possible."
  - The intended reading is that "the ten clues" means the set with A–C = 2, and that gives the guide's three repairs. Read as a fresh start from Problem 4's ten clues, it asks for single changes that keep a world possible. Those are A–B to 4, D–E to 4 and D–E to 8 (computed in `check_math.py.out`), and the guide does not mention them.
  - The words "repair" and "so that a world is possible", and the A–C = 2 card that has just replaced A–C = 4, make the intended reading the natural one, so I did not count this.
  - If the page is ever revised, "Change exactly one of these ten clues (with A–C = 2)…" removes the doubt.
- **P10, label supply.**
  - One page-1 set has only two 4-labels. Fifteen of the 2,471 possible secret six-card worlds need three, for example AB@4, CD@4, EF@4 and all @8.
  - The guide already says to print extra copies of page 1 for cutting, which covers this. Its "Per pair" list says only "labels 2, 4 and 8", with no counts.
  - This is a kit detail, not a mathematical error.
