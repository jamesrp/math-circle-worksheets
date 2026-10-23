# Week 87 (Voting and agendas): math check

Scope:
- `lowell-math-circle-year-2/week-87/week-87-shared.pdf`: the Grades 2–5 packet, 3 pages.
  - p. 1: the opening rule, a worked D/E vote on the cards DFE, EFD, FED, then Problem 1 (cards ABC, BCA, CAB).
  - p. 2: the knockout rule and a worked knockout, then Problem 2 (make A, B, C win).
  - p. 3: Problem 3 (design a set with one winner, and a set where the waiting letter matters).
- `week-87-line.pdf`: the Grades 3–5 packet, 4 pages.
  - p. 1: the rules, a launch example (favorites 0, 1, 5, 8, 10 with X = 2 and Y = 8), then Problem 1 (favorites 0, 2, 4, 7, 10).
  - p. 2: Problem 2 (three sets of five favorites). p. 3: Problem 3 (is the third favorite always the winner?). p. 4: Problem 4 (four voters at 1, 3, 7, 9).
- `week-87-upper.pdf`: the Grades 4–5 packet, 2 pages. Problem 1 has two card sets. Problem 2 asks whether ABC, BCA, CAB can come from distances on one line, after a worked conversion.
- `week-87-materials.pdf` (5 pages): the fixed cards, tiles, tokens, blank cards and slips, the tally and knockout mats, and the lane board.
- `week-87-facilitator.pdf` (6 pages).

There is no K–1 packet. The delivered PDFs are byte-identical to `source/week-87/reference-pdfs/`. Rebuilding from `student/build.py` and `guide/facilitator.tex` in a scratch folder gives the same text as the delivered PDFs.

Sources read: `source/week-87/student/build.py`, `guide/facilitator.tex`, `README.md`, `SOURCES.md`, `student/QA.md` and `student/README.txt`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-87/`. Checked October 23, 2026.

**Result: every printed diagram, worked example, answer and proof is correct, in all three packets and the guide. I found 1 problem, minor and in the guide only. Shared Problem 3's second half has exactly two answers up to voter order: Problem 1's own cards and their mirror. The guide's "or invent another" suggests there are more.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures). It is written from scratch, with the printed data typed in from the pages; `check_diagrams.py` confirms that data against the PDFs.
  - **Card votes.** Every pair vote and knockout, with both orders of the first pair, for:
    - the worked D/E/F example;
    - shared Problems 1 and 2;
    - both upper Problem 1 sets;
    - the guide's Problem 3 example.
  - **Shared Problem 3.** All 20 sets of three different cards, and all 216 three-voter profiles with repeats allowed. For each, the script tests whether one letter wins every agenda.
  - **Upper Problem 2.** Exact rational arithmetic. Two brute-force searches and a check by cases:
    - every placement of distinct A, B, C on half-ticks 0–10, with favorites every quarter step from −2 to 12;
    - every triple l < m < r on a third-step grid, testing the lemma that the middle candidate is never a voter's strict last choice;
    - for each of the 6 orders of A, B, C, whether the middle letter is last on one of the cards.
  - **Line packet.**
    - The launch table and its tally.
    - Problems 1, 2 and 4 on the ticks, and on an eighth-step grid from −2 to 12, which includes points off the board.
    - All 3,003 five-favorite multisets for Problem 3, against every tick and against off-tick opponents.
    - Other readings of the wording: voters who share a favorite counted once; "third favorite" read as the third distinct place.
    - Every count the guide gives.
  - **Tally-well geometry.** The clearance figures the guide quotes.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures). It reads the delivered PDFs' words and vectors with PyMuPDF, not the builder:
  - **Every page.** Headers, footers, page numbers and consecutive problem numbers.
  - **Cards.** Each printed ranking card is rebuilt from its V label and its 1st, 2nd and 3rd rows.
  - **Number lines.** Every favorite line is matched to its V label, and its tick value read from the tick positions.
  - **Line p. 1 launch.** The lane circles; the X square and Y diamond against the reference line; the distance table; the contents of the three tally boxes.
  - **Upper p. 2 example.** The V1 favorite and the D/E/F tiles against the small number line.
  - **Materials sizes.** The 100 mm bar; cards, tiles, tokens, slips, markers and labels; lane pitch, and lane ticks lined up with the numbered line; the tally wells and target clearances; and whether each knockout box holds the 28 mm tiles it needs.
  - **Guide.** Every sentence quoted below is present in the PDF text.

The general facts are proved in the guide, and I checked those proofs by hand:
- **Median winner.** Sort the five favorites with repeats as p1 ≤ … ≤ p5. If q < p3, voters 3–5 are strictly nearer p3. If q > p3, voters 1–3 are. Three strict votes cannot be beaten by the other two.
- **Four voters at 1, 3, 7, 9.** Two voters on each side defend any x in [3, 7]. Two locations inside [3, 7] split 2–2. A location outside [3, 7] loses 3–1 to the nearer end.
- **Middle candidate.** If l < m < r and p ≤ m, then r − p > m − p. The case p ≥ m is symmetric. So the middle candidate is never a voter's strict last choice. ABC, BCA, CAB put each letter last once.
- **Three voters, three options.** Majority on each pair is a 3-vertex tournament: either transitive, or a 3-cycle. With a Condorcet winner it wins every agenda. In a cycle, the waiting letter always wins.

## Shared packet, Grades 2–5 (pp. 1–3): correct

- **Worked examples (pp. 1–2).**
  - On D vs E, V1 chooses D and V2, V3 choose E, so E wins 2–1. The tally boxes hold D: V1 and E: V2, V3.
  - In the knockout, E vs F gives F 2–1 (V1 and V3 choose F).
  - The cards on both pages read DFE, EFD, FED.
- **P1.** The cards are ABC, BCA, CAB. A beats B (V1, V3), B beats C (V1, V2) and C beats A (V2, V3), each 2–1. No letter beats both others, so the answer is no.
- **P2.** All three are possible, and the waiting letter always wins:
  - B/C first, then A wins;
  - C/A first, then B wins;
  - A/B first, then C wins.

  Swapping the order of the first pair changes nothing. The three answer rows have the boxes needed.
- **P3, first half.** Of the 20 sets of three different cards, 18 have one winner for every agenda, so there are many answers.
  - Three different cards cannot share a first choice, because only two rankings start with each letter.
- **P3, second half.** It is possible, but only in two ways; see item 1.
- **Diagrams.** The two blank sets of three cards are present.

## Line packet, Grades 3–5 (pp. 1–4): correct

- **Launch (p. 1).**
  - Favorites 0, 1, 5, 8, 10 sit on their own lanes, at ticks 0, 1, 5, 8 and 10 exactly. The X square is under 2 and the Y diamond under 8.
  - The table reads V1 2/8 → X, V2 1/7 → X, V3 3/3 → Tie, V4 6/0 → Y and V5 8/2 → Y. All five entries are right.
  - The tally boxes hold X: V1, V2; Y: V4, V5; and Tie: V3. "Tied vote: 2 to 2" is right.
- **P1.** The favorites are 0, 2, 4, 7, 10 as drawn. Location 4 is the unique location that beats every other, both among the ticks and among off-tick points.
- **P2.** The favorites read back as drawn: (0, 0, 0, 8, 10), then (1, 4, 4, 4, 9), then (0, 1, 6, 9, 10). The unique winners are 0, 4 and 6.
  - The page's "Voters sharing a favorite still get one vote each" matters. If the three voters at 0 counted once, the first set's answer would become 8.
  - Each "Winning location" blank sits above its own line, as the first one does.
- **P3.** Yes: the third favorite from the left always beats every other location. All 3,003 multisets were checked. The median always gets at least 3 strict votes, against ticks and against off-tick points.
  - "Count all five markers" rules out the third-distinct-place reading. That reading would fail in 1,485 sets, for example (0, 0, 0, 1, 2).
- **P4.** The favorites are 1, 3, 7, 9 as drawn. The ticks that never lose are exactly 3, 4, 5, 6, 7, and no location beats every other. With real locations, the never-losing set is exactly [3, 7].
  - The page's "Use only the numbered ticks" makes the tick answer the intended one.

## Upper packet, Grades 4–5 (pp. 1–2): correct

- **P1.** Set 1 is ABC, ACB, BAC. A beats B 2–1 and C 3–0, so A wins every agenda and the waiting letter cannot change the winner. Set 2 is ACB, CBA, BAC. B beats A, A beats C and C beats B, each 2–1, so the waiting letter always wins.
- **Worked conversion (p. 2).** The tiles are D at 0, E at 4 and F at 9, and the favorite V1 is at 1. The distances are 1, 3 and 8, so the card is DEF, as printed.
- **P2.** It is impossible, as intended. Any placement of distinct A, B, C produces at most 4 of the 6 strict rankings, never the two that put the middle letter last. No searched placement produced all three cards. Each card puts a different letter last, so whichever letter is in the middle is last on one card.

## Materials (pp. 1–5): sizes as stated

- **Page 1.** The scale bar is 100.0 mm. The three cards are 45 × 80 mm, the six option tiles (A, A, B, B, C, C) are 28 mm, and the five vote tokens are 18 mm.
- **Pages 2–3.** Each has one blank set of three cards and 18 slips (6 each of A, B, C). The slips are 21 mm, and each card slot is 23.3 mm tall.
- **Page 4, tally mat.** 170 × 90 mm, with three 54 mm wells. Each well has five 18 mm targets, with 2.00 mm boundary clearance and a 4.63 mm minimum gap. The two Option slots are 30 mm.
- **Page 4, knockout boxes.** Each holds the 28 mm tiles it needs. "Out" and "Winner" are 29 mm wide, so they leave only 0.5 mm a side. That is a physical-fit matter, not a mathematical one.
- **Page 5.** The lane pitch is 19 mm, the tick pitch 16 mm, and every lane tick lines up with the numbered line. The favorite markers are 13 mm. The X proposal is a 13 mm square and the Y proposal an 18 mm square diamond, so they fit on adjacent ticks. The tally labels are 23 mm.

## Facilitator guide (6 pp.): correct except item 1

- **Overview (p. 1).**
  - The ABC/BCA/CAB cycle, each 2–1. Any option wins by waiting. A Condorcet winner wins every knockout.
  - The median theorem, with its hypotheses stated: odd count, repeats counted, the median available. Uniqueness follows, because two universal winners would each have to beat the other.
  - Four voters: [3, 7], or 3–7 on the board.
  - The middle-candidate lemma.
- **Shared solutions (p. 3).**
  - P1's voter lists. The D/E/F example: V1 chooses D and V2/V3 choose E; then V1/V3 choose F and V2 chooses E.
  - P2's three agendas, and "These three choices exhaust all unordered first pairs."
  - P3's example ABC, ACB, BAC, with A beating B 2–1 and C 3–0.
- **Line solutions (p. 4).**
  - P1: against 0 and against 10 the count is 3–1 with one Tie (the voters at 2 and at 7 tie). Against 1, 2, 3, 5, 6, 7, 8, 9 it is 3–2.
  - P2: winners 0, 4, 6. The mean of 0, 1, 6, 9, 10 is 26/5 and the board's midpoint is 5.
  - P3: the proof, "3,003 arrangements" (C(15, 5)) and "55 pairs" (C(11, 2)).
- **Return investigations (p. 5).**
  - Line P4: the [3, 7] argument, and "the voters at 3,7,9" and "1,3,7" defending the ends.
  - Upper P1: B beats C 2–1 in set 1, and the set 2 cycle with its three agendas.
  - The 3-vertex tournament remark, with its caveat about larger menus.
  - Upper P2's proof, including favorites outside the candidates.
- **Materials figures (p. 2).** 170 × 90 mm, 54 mm wells, 2 mm clearance, "at least 4.6 mm" (actually 4.63) and 23 mm labels.

All of these are right.

## Problems found

1. **Guide p. 3, shared Problem 3: the agenda-dependent half has only two answers. The guide implies children can invent others.** Minor; guide only.
   - **Quoted:** "The cyclic profile of Problem 1 is already a valid three-distinct-card agenda-dependent example; children may reproduce or relabel it, or invent another and test their claim."
   - **Student page (shared p. 3):** "Make another set of three different cards where changing the waiting letter changes the winner."
   - **Evidence** (`check_math.py`, "Problem 3"):
     - Of the 20 sets of three different cards, exactly 2 make the waiting letter matter: {ABC, BCA, CAB}, which is Problem 1's set, and {ACB, CBA, BAC}, its mirror with B and C swapped.
     - Allowing repeated cards adds nothing. Every one of the 216 three-voter profiles with a cycle uses exactly one of these two sets.
     - The reason: each card agrees with at most two of the three cycle wins, because a card that agreed with all three would itself be a cycle. Each win needs two of the three cards, so 6 agreements are needed, from at most 2 per card. So each card supplies exactly two, and the cards must be the three rotations.
   - **Consequence:**
     - Copying Problem 1's cards (in any voter order) answers the second half, and the only other answer is the mirror.
     - An adult who reads "invent another" may send a child looking for a new pattern that does not exist.
     - The guide also misses a good, provable fact for a return question.
     - A related loose phrase on the same page: "The cards need not have identical first choices." In fact three different cards cannot share a first choice, since only two rankings start with each letter.
   - **Smallest fix (guide only):** replace "or invent another and test their claim." with:

     > "Every working set uses exactly the cards ABC, BCA, CAB or ACB, CBA, BAC, in some order. Each card can agree with at most two of the three winning pairs, and each pair needs two cards. 'Is there a different one?' makes a good return question."

     Optionally, change "The cards need not have identical first choices" to "Three different cards cannot all have the same first choice, since only two rankings start with each letter."
