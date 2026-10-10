# Week 28 (single-vertex flat folding): math check

Scope: everything current in `lowell-math-circle-year-2/week-28/`, archive folders excluded:

- `week-28-k-1.pdf` (F28-K-v2, 6 pp., P1–P6)
- `week-28-grades-2-3.pdf` (F28-23-v2, 6 pp., P1–P6)
- `week-28-grades-4-5.pdf` (F28-45-v2, 6 pp., P1–P6)
- `week-28-facilitator.pdf` (18 pp.: an unnumbered overview, guide pp. 1–16, and a route-update page numbered 18)
- the bonus companion `week-28-bonus.pdf` (W28-BON-v1, 5 pp., P1–P5) and its guide `week-28-bonus-facilitator.pdf` (W28-BON-FAC-v1, 5 pp.)

Sources read: `source/week-28/editable/src/` (`k-1.tex`, `grades-2-3.tex`, `grades-4-5.tex`) and `source/week-28-bonus/student-src/bonus.tex`. By MD5, every delivered PDF is byte-identical to its reference copy in those source folders. I did not run or import the packet's own checkers (`facilitator-src/check_math.py`, `verify_*.py`, `student-src/check.py`, `math/independent-check.py`). I did not read its review or answer notes either. Checked October 10, 2026.

**Result:**
- **Mathematics:** every student problem in every band has the answer its page intends. Nothing asked for is impossible, and nothing claimed impossible can be done. Every count, table, witness, layer order and proof in both adult guides is correct, with the stated hypotheses.
- **Problems found:** 3, all minor, none a mathematical error:
  1. In bonus P1 case 4, the "impossible" answer holds only if the P half is the half that moves. The page conveys this only through the words "brings P onto Q" (wording).
  2. Grades 4–5 P6 asks "How many…?" and prints exactly 12 answer rows. The answer is 12, so the page gives the count away (page layout).
  3. K–1 P3 asks for "every" fold with ray 1 = M. It prints six disks, each already marked M, but there are only four such folds, and the guide never says two disks are spare (page layout).

## How it was checked

My scripts and their saved outputs are in this folder (to be committed as `checks/week-28/`). Each script finds the repository from its own location: four folders up from `plans/review/checks/week-28/`, or by walking upward from anywhere else. They need `pdfplumber`, which was already installed here.

- **`foldcheck.py`** is my own flat-folding oracle, written for this review.
  - **Method 1, a brute force over layer orders.** It flattens a single vertex by reflecting each sector in turn and tries every bottom-to-top order of the sectors. An order passes if it obeys three noncrossing rules:
    - no continuing layer lies between two layers joined at a crease;
    - two creases at the same spot on the same side do not interleave;
    - two creases at the same spot on opposite sides have disjoint height ranges.

    The script reads the M/V word off each legal order.
  - **Method 2, the crimp reduction** (Bern–Hayes/Hull), a separate theorem used only as a cross-check.
  - **Agreement:** the two methods agree on 400 random Kawasaki patterns of degree 4 and 6. Every pattern has a flat state, and every state obeys Maekawa. Eight 45° sectors give 112 valid words, as Hull's formula 2·C(8,3) predicts.
- **`pdf_geometry.py`** → `pdf_geometry.out` (362 checks, 0 failures) and `pdf_geometry.json`. It reads every diagram from the PDF vector drawings, not from the builders:
  - each disk's rays, as degrees clockwise from the top;
  - ray numbers, M/V labels, degree labels, shaded sectors and sector names;
  - the loose wedges and their radii, the half-turn template, the 30° ticks and the K–1 tab rows;
  - the guide's diagrams, including its dashed added rays.

  It compares each diagram with my own reading of the problem text. It also checks that every disk outline is a true circle, and that the TikZ sources give the same ray sets on every page.
- **`check_base.py`** → `check_base.out` (88 checks, 0 failures). It recomputes every base task and every guide claim with `foldcheck.py` and plain enumeration:
  - every routes count, tab stock, wedge subset, added ray (scanned every half degree) and six-angle order;
  - the guide's stack table, layer certificate and reading rule;
  - the guide's page cross-references.

  It quotes guide text from the PDF wherever it checks a printed claim.
- **`check_bonus.py`** → `check_bonus.out` (23 checks, 0 failures). It covers the bonus packet and its guide:
  - P1 points read from the PDF, with exact perpendicular bisectors and reflections;
  - P2–P3 strip orders, checked by enumeration with the stated bend rule;
  - P4–P5 hole centres read from the PDF, tested against reflection orbits, with clearances on a 15 cm square.

## K–1: no mathematical errors

All disks are four right angles, with rays 1–4 numbered clockwise from the top. By my brute force, the foldable words are exactly the eight 3:1 words. The other eight words have no legal stack.
- **P1:** asks for four different folds. Eight exist, so any four distinct words work.
- **P2:** the printed words are A MMMV, B MMMM, C MVVV, D MMVV, E MMVM and F MVMV, read from the PDF. Exactly A, C and E fold.
- **P3:** with ray 1 = M, exactly four words fold: MMMV, MMVM, MVMM and MVVV. The page prints six disks for them (finding 3).
- **P4:** the printed partial words are M?V?, MM?? and V?V? in every row. The tab rows read from the PDF are A = 2M 4V, B = 3M 3V and C = 4M 2V.
  - The left disk can be completed only as MMVM or MVVV, which uses 2 or 0 M tabs. The middle can be MMMV or MMVM, and the right VMVV or VVVM, each using 1 M tab.
  - So a row closes exactly when its stock has 2 or 4 M tabs. Rows A and C have 4 solutions each, and row B has none.
- **P5:** the answer is the eight words. Ten disks are printed, so two are spare.
- **P6:**
  - The A–H labels on the page are the eight valid words.
  - Two words differ in exactly two places, except the complementary pairs A–H, B–G, C–F and D–E, which differ in all four.
  - There are 240 routes from A to H and 248 from A to D, and each needs exactly the 6 blanks printed.

## Grades 2–3: no mathematical errors

- **P1:** the wedges measure A 30°, B 30°, C 60°, D 60°, E 90°, F 120° and G 150°, all with radius 2.25 cm. The half-turn template is a semicircle of the same radius. Exactly ten groups make 180°: AG, BG, CF, DF, ABF, ACE, ADE, BCE, BDE and ABCD. The page prints ten answer lines (see finding 2).
- **P2:** the drawn sectors are A 90/90/90/90, B 45/90/90/135, C 60/120/120/60 and D 30/60/150/120. Sectors 1 and 3 are shaded, and A1…D4 sit in sectors 1–4. In A, C and D the shaded and white pairs both make 180°. In B the shaded pair makes 135° and the white pair 225°.
- **P3:** these are the same four disks, with ray numbers. A, C and D fold, and B cannot. The brute-force valid words are:
  - A: all eight 3:1 words;
  - C: MMMV, MVMM, MVVV, VMMM, VMVV and VVVM;
  - D: MVMM, MVVV, VMMM and VMVV.
- **P4:** the given rays are {0, 90, 180}, {0, 60, 180}, {0, 30, 180} and {0, 120, 180}. Scanning every half degree, the only added ray that balances the alternating sums is 270°, 300°, 330° and 240° respectively, that is 360° − a. Each completed pattern folds as VVVM. The ticks are every 30°, so every answer lies on a tick.
- **P5:** the answer is the eight words, with 10 disks printed.
- **P6:** the wedges are A, A = 30°, B, B = 60° and C, C = 90°, with radius 2.4 cm, the same as the recording disks. There are 36 rooted orders, and every one puts one A, one B and one C in each alternating triple. Four are requested.

## Grades 4–5: no mathematical errors

- **P1:** these are the 2–3 P3 disks with degree labels, and each label sits in a sector of that size. A, C and D fold, and B cannot (135 ≠ 225).
- **P2:**
  - The three patterns are 120×3 (3 rays), 60/60/60/90/90 (5 rays) and 30/30/60/60/60/60/60 (7 rays). Each totals 360°.
  - Each has an odd number of rays, so none can fold.
- **P3:**
  - The alternating sums are A 135/225, B 180/180, C 150/210 and D 180/180, with the odd-position sectors shaded. The argument rules out A and C.
  - B and D do have flat states (brute force for B, crimp reduction for D).
- **P4:** the eight 3:1 words, with 10 disks printed.
- **P5:** none of MMMM, VVVV, MMVV and MVMV folds. Their rotations are exactly the eight non-foldable words, so P4 and P5 together cover all 16.
- **P6:** exactly 12 orders start with 30° (36 without that condition). The page prints 12 answer rows (finding 2).

## Adult guide (base): correct

- **Overview:** Kawasaki–Justin (unassigned, even degree, alternating sums 180°) and Maekawa (|M − V| = 2, necessary only) are stated with the right hypotheses. So is the scope: one interior vertex, ideal paper, every listed ray active. The claim that count plus angles does not certify a labelling is true: VVVM on D is the guide's own example, and my brute force confirms it fails.
- **pp. 3–4:**
  - **Constructions.** The two-book-fold construction gives VVVM, and its rotations and reversals give all eight words. Model C folds as VVVM.
  - **Model D certificate.** Rays 0°, 30°, −30°, 120°, sector intervals and the order S3, S4, S1, S2 are all correct. The order is legal and reads MVVV.
  - **D with VVVM.** Its joins force the order S1 < S4 < S3 < S2, the only one consistent with those labels, and that order crosses at the ray 2 crease (30°).
- **pp. 5–6:**
  - **Necessity proofs.** The orientation-parity proof is sound, and so is the proof that O − E lies strictly between −360° and 360°.
  - **Right-angle stack proof.** It is complete. Its survivor table (1234 VVMV, 1432 VVVM, 2143 VMMM, 2341 MMMV, 3214 VMVV, 3412 MVVV, 4123 MVMM, 4321 MMVM) is exactly the 8 legal orders of 24. Its height-reading rule reproduces every word.
- **pp. 7–16:**
  - **Answer tables.** Every table is correct: the catalog, P2 works/impossible, the P4 completion table and all eight triples, both routes and their changed-ray columns, the 240/248 counts, the ten groups with the largest-piece argument, the P2 sums, the witnesses, and the P4 table with its uniqueness proof. So are the 36 and 12 order counts and the 12-row list, and the 1/4/6/4/1 count.
  - **Extensions.** Exactly 2 and 4 M tabs work. The cycle A-B-C-D-F-E-H-G-A is legal. For every 0 < a < 180, the ray set 0, a, 180, 360 − a folds as VVVM.
- **Cross-references and page numbers.** Every page cross-reference lands on the content it names. The route-update page is numbered 18 after page 16, but that is not a mathematical issue and no reference is affected.

## Bonus companion and its guide: correct apart from finding 1

- **P1:** the points read from the PDF are P(1,1), Q(5,1), R(2,4), S(4,4); case 2 has R(1,4); T is (3,5) in case 3 and (2,5) in case 4.
  - In case 1 the fold x = 3 works. In case 2, P/Q force x = 3 but R/S force x = 2.5, so no fold works.
  - In case 3, T lies on the crease. In case 4, folding the P half sends T to (4,5). See finding 1.
- **P2:** all six orders of three panels are legal. With B face up, folding both outer panels toward the front gives ACB or CAB, and both toward the back gives BAC or BCA. Mixed directions give ABC or CBA.
- **P3:** 16 of the 24 orders obey the stated bend rule. The guide's lists of 16 valid and 8 excluded orders are exact.
- **P4:** the holes read from the PDF are (±1.7, ±0.9), (±1.2, ±1.2), and a third set with one hole moved to (−1.2, −0.9). The first two each come from one punch; the third cannot.
- **P5:** patterns 1 and 2 are the eight-point orbits of (1.7, 0.9) and (1.8, 0.7). Pattern 3 is the union of the four-point midline orbits of (1.7, 0.8) and (0.7, 1.4), and lacks (0.8, 1.7).
  - The picture folds along the diagonal through the original centre, as the guide's 0 ≤ q ≤ p assumes.
  - On a 15 cm square, each valid punch clears every fold and edge by at least 1.41 cm, and unfolded holes are at least 2.83 cm apart.
- **Bonus guide:** every stated fact, coordinate, count and limit is correct.

## Problems

### 1. Bonus P1 case 4: the answer depends on which half is folded (bonus p. 1; wording, minor)

- **Quoted text:** "Make one straight fold that brings P onto Q and R onto S at the same time. Where T is shown, T must stay in its original place. Draw a crease that works, or explain why none can."
- **The guide's answer:** case 4 has no answer: "T=(2,5) on the moving P side; the forced crease moves it to (4,5), so the demanded alignment and fixed T cannot coexist."
- **Evidence:** `check_bonus.py`.
  - P and Q force the crease x = 3, and so do R and S. T(2,5) lies on the P side.
  - If the P half moves, T goes to (4,5) and case 4 fails. If the child keeps the P half flat on the table and folds the Q half over, P and Q still meet, R and S still meet, and T stays exactly where it was. Case 4 then works.
  - The bonus guide itself says "A mark on the stationary Q half would stay fixed off the crease" and "The moving/stationary convention matters". So the student page settles the answer only through the word "brings".
- **Smallest fix:** in P1, add "Keep the Q side flat on the table and fold the P side over." Alternatively, put the same sentence in the guide's launch as a required demonstration.

### 2. Grades 4–5 P6 prints exactly as many answer rows as there are answers (4–5 p. 6; page layout, minor)

- **Quoted text:** "How many different orders start with 30° and have alternating totals of 180°? Explain why your count is complete."
- **Evidence:** `check_base.py` reads 12 rows of six blanks from the PDF. My enumeration finds exactly 12 orders. A child can read the count off the page and stop searching when the rows are full, which undercuts the completeness argument the problem asks for. Grades 2–3 P1 does the same, with ten answer lines for the ten half-turn groups. There the stakes are lower, because that problem asks only for "as many as you can".
- **Smallest fix:** print 14–16 rows on 4–5 P6, or open space with a few rows. Optionally, add one or two lines to 2–3 P1.

### 3. K–1 P3 prints six pre-marked disks for four answers (K–1 p. 3; page layout, minor)

- **Quoted text:** "Ray 1 must be a mountain. Find every flat fold with that label." There are six disks, each with M already printed on ray 1.
- **Evidence:** `check_base.py`: exactly four words fold with ray 1 = M (MMMV, MMVM, MVMM, MVVV). The page implies six. A K–1 child cannot prove completeness and may keep folding, or may record a non-foldable or repeated labelling to fill the last two disks. The guide says "All four answers" but never says that two disks are spare. K–1 P5 and 2–3 P5 (ten blank disks for eight answers) carry the same, weaker implication, since their disks are blank.
- **Smallest fix:** add to the guide's P3 entry: "Four answers; two of the six disks are spare." Alternatively, print four pre-marked disks plus two unmarked disks labelled as extra workspace.
