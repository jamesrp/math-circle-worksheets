# Week 86 (Pursuit and escape): math check

Scope:
- `lowell-math-circle-year-2/week-86/week-86-shared.pdf`: Grades 2–5, 4 pages, Problems 1–4.
- `week-86-upper.pdf`: Grades 4–5, 6 pages, Problems 1–6. Problem 1 repeats shared Problem 1.
- `week-86-materials.pdf`: 3 pages. F1 and F2 (original and working copy) for upper Problem 4, then turn tiles and counters.
- `week-86-facilitator.pdf`: 6 pages.
- There is no K–1 packet.

Sources read: `source/week-86/student/build.py` (exact coordinates and road lists), `guide/facilitator.tex`, `README.md`, `SOURCES.md`, `student/README.md` and `student/QA.md`. I rendered every student, materials and guide page at 80 dpi and read them. All four delivered PDFs are byte-identical to `source/week-86/reference-pdfs/`. I did not run or import the package's `check_math.py`, `student/verify.py` or `build.py`. Checked October 23, 2026.

**Result: every student problem is well posed, and every board is exactly the graph its text needs. Every theorem, answer, strategy and proof in the guide is correct. I found 2 problems, both minor and both in the guide's solutions. (1) A sentence on p. 3 could lead an adult to reject a correct escape plan. (2) The p. 4 key does not warn that half of the two-road answers to upper Problem 2 fail.** A few non-mathematical notes for the card stage follow at the end.

## How it was checked

My scripts and their outputs are in this run folder, for `plans/review/checks/week-86/`. `check_pdf.py` finds the repository from its own location: four folders up when it sits in `plans/review/checks/week-86/`, otherwise the nearest parent with `AGENTS.md`. I also ran it from a copy laid out as `plans/review/checks/week-86/`, and its output was identical. `check_math.py` uses only the standard library and reads no repository files.

- **`check_pdf.py`** (output `check_pdf.py.out`: 153 checks, 0 failures). It reads the delivered PDFs' vector drawing with PyMuPDF:
  - dots: closed four-Bézier circles, giving centre and diameter;
  - roads: black segments whose ends sit on dot centres;
  - dot labels: the single letter below each dot;
  - board names: P5, T1, R3 and so on.

  It then compares all 29 boards, label for label, with my own transcription of the expected graphs (the same graphs `check_math.py` solves). The 29 are: shared P5, P7, T1, T2 and R3–R6; upper P5, P7, E4, E5, D1, D2, Q6 and Q8; the three rules-page panels on each p. 1; the three fold-example diagrams; and F1 and F2 (original and working). Further checks:
  - the C and R positions and tile captions in the rules-page panels;
  - which dots each blue box in the fold example encloses;
  - dot diameters and nearest-centre spacings;
  - equal radii and sides for every ring and for D1/D2, all drawn at equal x/y scale;
  - that no road passes through a dot it does not end at;
  - for E4, E5, D1 and D2, that every possible straight road between two dots would clear the other dots and that no three centres are collinear;
  - that each label is nearer its own dot than any other;
  - headers, footers and problem numbering;
  - the materials p. 3 tiles and counters.
- **`check_math.py`** (output `check_math.py.out`: 96 checks, 0 failures). It is an exact solver for the printed rules:
  - C places, then R; placing on C is capture.
  - C moves first. Each player stays or crosses one road, and sharing a dot is capture.
  - The two-cop version moves both cops in one cop turn.
  - The solver uses backward induction by rounds. It gives the least number of cop turns that guarantees capture from every position, or ∞.
  - It also replays each strategy the guide states as a restricted game, against every legal reply.
  - It enumerates every fold sequence, every set of added roads on E4 and E5, and every connected graph on at most 6 labelled dots (27,476 graphs) to test the guide's fold theory.

## Shared Grades 2–5 (pp. 1–4): checks out

- **Rules page, worked example (p. 1).** The board is the star w–x, x–y, x–z with 8 mm dots. The panels show: Start, C@w and R@y, "C turn"; C takes one road, C@x and R@y, "R turn"; R stays, C@x and R@y, "C turn". Every move shown is legal, and the tiles alternate correctly.
- **Problem 1 (p. 1), P5 and P7.**
  - The task is to choose C's start that guarantees capture in the fewest C turns.
  - The exact worst-case values by start are 4, 3, **2**, 3, 4 on P5 and 6, 5, 4, **3**, 4, 5, 6 on P7. The unique best start is c (2 turns) on P5 and d (3 turns) on P7.
  - "Move toward R" from the middle achieves the optimum. R on the farthest endpoint, staying put, forces it.
  - Both boards are paths with straight roads: 22 mm dots at 32 mm spacing on P5, and 20 mm dots at 28 mm spacing on P7.
- **Problem 2 (p. 2), T1 and T2.**
  - Both boards are trees: T1 is a five-dot row with a two-dot branch c–f–g, and T2 is a five-dot row with c–f and the fork f–g, f–h.
  - "Move toward R" wins from every start. From c it captures within 2 cop turns on both trees, and 2 is optimal: the values by start equal each dot's eccentricity.
  - "Wherever R starts" agrees with the rule that R places after C.
- **Problem 3 (p. 3).** On R3, C wins from any start on the first move. On R4, R escapes from every C start, and the guide's opposite-dot strategy is never caught. Both rings are regular.
- **Problem 4 (p. 4).** R5 and R6 are robber-win from every C start. Both rings are regular, with 22 mm dots.

## Upper Grades 4–5 (pp. 1–6): checks out

- **Problem 1 (p. 1).** The text matches shared p. 1 apart from the header and footer, and the boards are identical; see above.
- **Problem 2 (p. 2), E4 and E5.**
  - The task is to add as few roads as possible so that C can always catch R.
  - E4 needs 1 road, and both diagonals work. E5 needs 2 roads: all 5 single chords leave R an escape.
  - Of the 10 two-chord sets, 5 are cop-win, namely the pairs sharing an endpoint (ac+ad, ac+ce, ad+bd, bd+be, be+ce). The other 5 are robber-win, namely the crossing pairs (ac+bd, ac+be, ad+be, ad+ce, bd+ce). See Problem 2 below.
  - Every possible chord on the printed regular square and pentagon clears the other dots by at least 13.9 mm, so "A crossing is not a new dot" is the only drawing issue, and the page states it.
- **Problem 3 (p. 3), D1 and D2.**
  - Both kinds of map exist. Of the connected graphs on the six labelled dots with at least six roads, 14,073 are cop-win and 11,335 robber-win. A robber-win one can have up to 12 roads.
  - "At least six roads" excludes trees, since every six-dot tree has 5 roads.
  - The printed six dots form a regular hexagon (r = 32 mm) with no three centres collinear. Any straight road between two of them clears the others by at least 5 mm.
- **Problem 4 (p. 4, materials pp. 1–2), folds.**
  - The fold rule ("a neighboring dot u can reach every place v can reach by staying or taking one road") is N[v] ⊆ N[u] with u adjacent to v.
  - In the worked example, w reaches {w, x} and x reaches {w, x, y}. The blue boxes enclose exactly those dots. Folding w → x leaves x–y–z, as drawn.
  - F1 is the triangle a–b–c with tail c–d–e and pendant a–f. Every sequence of legal folds ends at one dot, and F1 is cop-win.
  - F2 is a pentagon with chord a–c. Initially only b can fold (into a or c). Every fold sequence ends at the square a, c, d, e, which has no legal fold, and F2 is robber-win.
  - The original and working copies of each board are identical graphs.
- **Problem 5 (p. 5), Q6, both cops start at a.** Two cops always win, and the optimal guarantee is 3 cop turns. If R starts at d, the cops close in from both sides.
- **Problem 6 (p. 6), Q8 and every ring.**
  - From a common start at a, two cops win in at most 4 cop turns; with free placement, 2.
  - The answer to "every ring" is yes. The blocker plan below captures on every ring from C3 to C14, and the guide's argument is general.

## Adult guide (6 pp.)

Checked:
- **The overview (p. 1).**
  - Trees are cop-win, by the shrinking component. I verified both the policy and the strict shrinking on every labelled tree with up to 8 dots.
  - On an n-dot path the best starts are the middle dot or dots, with ⌊n/2⌋ cop moves (verified for n = 1–14).
  - A bare cycle with 4 or more dots is robber-win, and the stated rule is never caught on C4–C14.
  - The fold claim and the full classification hold. On all 27,476 connected graphs with up to 6 dots: cop-win ⇔ dismantlable; every single fold preserves the winner; and the guide's evasion rule for graphs with no dominated dot is never caught.
  - One diagonal, two chords, the square retract and the two-cop cycle statement are all correct.
- **The solutions (pp. 3–5).**
  - The path, tree, triangle and square answers are correct.
  - The projection argument for the one-chord pentagon holds: b ↦ a is a homomorphism onto the reflexive square a–c–d–e.
  - The D1 example (triangle plus tail, start at c) is cop-win, and the bare six-ring is robber-win.
  - The F1 sequence e→d, d→c, f→a, a→b, b→c is legal at every step. The F2 analysis is correct.
  - The fold-lifting proofs in both directions are correct.
  - The blocker plan (C1 holds a; C2 goes to b, then toward R along the path ring − a) captures on C3–C14. Its worst cases are 2, 3, …, 13 cop turns against optima of 1, 2, 2, 3, 3, 4, 4, 5 for C3–C10. The guide claims capture, not speed.

Apart from the two items below, the guide checks out.

### 1. Guide p. 3, Shared Problem 4: a sentence calls a correct escape rule inadequate

- **Quoted text:** "“Opposite” is not an adequate general rule on an odd ring."
- **Evidence** (`check_math.py.out`, the C4–C14 "stay across from C" checks):
  - On an odd ring, "opposite" naturally means one of the two dots across from C (the farthest dots).
  - The rule "start on a farthest dot; after each cop move, go to or stay on a reachable farthest dot" is never caught on any ring from C4 to C14, under every tie-break. R keeps distance ⌊n/2⌋ throughout.
  - On R5 the dots outside C's closed neighbourhood are exactly the two dots across from C. So the guide's own rule, two sentences earlier, is this rule.
  - An adult following the sentence may tell a child who says "I always stay across from C" on the pentagon that the plan is inadequate, when it works.
  - Read literally, the sentence only means an odd ring has no single opposite dot, which is true but is not what it says.
- **Smallest fix:** replace the sentence with: "An odd ring has no single opposite dot; staying on one of the two dots across from C also works (on the pentagon these are exactly the dots outside C's neighborhood)."

### 2. Guide p. 4, Upper Problem 2: the key does not say that crossing chord pairs fail

- **Quoted text:** "A different pair of chords is acceptable if its claimed strategy is valid; the question asks a minimum, not every minimum pair."
- **Evidence** (`check_math.py.out`, "E5: adding 2 road(s)"):
  - Of the 10 ways to add two chords to the pentagon, exactly the 5 pairs that share an endpoint are cop-win. The 5 crossing pairs (ac+bd, ac+be, ad+be, ad+ce, bd+ce) are all robber-win.
  - For example, with a–c and b–d, b and c have the same closed neighbourhood {a, b, c, d}. Folding b → c leaves the square a–c–d–e, so by the guide's own fold theorem R escapes.
  - Children are likely to try crossing chords, and the page anticipates them ("A crossing is not a new dot"). A pair that "won" in a few games could be accepted, and the key gives the adult nothing to check it against.
- **Smallest fix:** add after the quoted sentence: "Two chords work only if they share an endpoint. Two crossing chords such as a–c and b–d still lose: b and c then reach the same places, and folding b leaves the square a–c–d–e."

## Notes outside the math check (not counted)

- **Guide p. 2, preparation:** "Use matching compact locators only for selecting the full boards." The delivered packet has no compact locators. The same paragraph calls the tile "“Both cops move” turn tile", but materials p. 3 prints "Both cops".
- **Upper p. 3:** D1's label "d" (x 107.1–108.9 mm, y 149.9–152.7 mm) sits 0.4 mm above the end of the heading "D2: R can escape forever" ("forever" spans x 97.8–108.3 mm from y 153.1 mm). It can read as part of the heading.
- **Labels on roads (cosmetic):** these labels sit on the road leaving the dot downward, each still nearer its own dot (`check_pdf.py.out`):
  - shared T1 f and g; T2 c;
  - R6 and Q6 b and f;
  - F1 a, on both copies;
  - the rules-example z.
- **Materials header:** "Grades 2–5" on F1/F2, which serve only upper (Grades 4–5) Problem 4.
