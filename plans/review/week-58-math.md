# Week 58 (fair division): math check

Scope:
- `lowell-math-circle-year-2/week-58/week-58-students.pdf`: one combined packet of 7 US Letter portrait pages, Problems 1–7, footer `W58-shared-v2`. Pages 1–3 and 5 are headed Grades 2–5. Pages 4, 6 and 7 are headed Grades 3–5. There is no other band; the guide says K–1 has an oral entry only.
- `week-58-materials.pdf`: 10 pages, footer `W58-materials-v2`. Pages 2–5 are rotated landscape.
- `week-58-facilitator.pdf`: 9 pages, footer `W58-guide-v1`.

Sources read: `source/week-58/student/students.tex`, `common.tex`, `materials.tex`, the student and guide READMEs, `guide/guide.tex` and `provenance/research.md`. I did not run or import the packet's own `verify_math.py` or `verify_pdf.py`. pdfLaTeX and PyMuPDF are not installed here, so I could not rebuild anything. I read every value from the delivered PDFs (with `pdftotext`, and from 254 dpi renders) and cross-checked it against the source. My scripts and their outputs are in this folder. Checked October 10, 2026.

**Result: every answer, count, cut position, table and theorem in the student packet and the guide is correct, and every diagram and material matches its text. I found 4 problems, all minor:**
- **one guide sentence** that puts the Problem 1 tie on the wrong partition;
- **one student wording** whose other reading changes Problem 2's "find every" count from 5 to 3;
- **two trivial points:** an overview example that does not fit its own sentence, and the page-3 launch picture, which draws the output pieces shorter than the halves they come from.

## How it was checked

- **`check_math.py`** (output `out_check_math.txt`; 84 checks, 1 failure, which is Problem 1 below):
  - **Inputs:** reads the printed inputs from the TeX and confirms that the delivered PDFs print the same ones. These are A = (red 3, blue 1) and B = (1, 3), the goods of Problems 1, 2 and 5, U = V = 1, and the X/Y/Z observer rows (4,8,0), (0,4,8), (8,0,4). The same values appear on the student pages, the material cards and the student p. 6 table.
  - **Problems 1 and 2:** enumerates all 16 labelled allocations of each with exact fractions. It also enumerates every two-tray partition under divide-and-choose, for each divider and each tie-break.
  - **Problem 3:** solves the equal-value cut exactly for each cutter and confirms by a whole-millimetre scan that the cut is unique.
  - **Problem 4:** checks the cut-and-choose guarantee on 4,554 piecewise-constant strip profiles and tie-breaks, and checks the join-cut trial.
  - **Problem 5:** enumerates all 8 whole-card allocations and the 16 fixed-half allocations. It also scans paper shares p in steps of 1/120.
  - **Problem 6:** enumerates all 27 panel allocations.
  - **Problem 7:** checks the two-person equivalence on 32,768 allocations (values 0–3), and again with negative values. It checks "envy-free ⇒ proportional" for three people on 531,441 allocations (values 0–2), where it also finds 11,172 proportional but not envy-free cases.
  - **Guide:** compares every table row, count and formula in the delivered guide text with these results.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`; 74 checks, 0 failures). It uses 254 dpi renders (10 px/mm) and `pdftotext -bbox`. It confirms:
  - all ten 100 mm check bars measure 100.00 mm, tick centre to tick centre;
  - the six 25 mm cards, including the paper R3, are 25.00 × 25.00 mm;
  - the seven preference and observer cards are 100.00 × 150.00 mm;
  - the X/Y/Z panels are 50.00 × 40.00 mm;
  - all 20 strip halves are 150 × 40 mm, and strips 1–10 each have one red and one blue half;
  - every value-dot row on student pp. 1–3 and 5 and on materials pp. 2–5 has as many dots as its printed number, every 0 has none, and no dot is left over;
  - the red and blue panels of each p. 3 and p. 4 sketch are equal (90.00 mm each), and the p. 4 dashed cut sits exactly on the join;
  - the p. 3 launch's dashed line halves its panel;
  - the p. 1 launch counters are 3 → trays 2 | 1 → chooser 2 | remainder 1, inside the drawn trays.

## Student packet (pp. 1–7): the mathematics checks out (see Problems 2 and 4 for two minor points)

- **Launch (p. 1):** a non-task picture: three neutral counters, then trays 2 | 1, then the chooser takes the 2-tray and the divider takes the remainder. This matches the text and gives away no answer.
- **P1 (R1, R2, R3, B1):**
  - A's total is 10 and B's is 6. Keeping your tray (envy-free) needs A ≥ 5 and B ≥ 3.
  - Exactly 4 of 16 allocations work: A gets any two reds (3 ways; A sees 6 vs 4, B sees 4 vs 2), or A gets all three reds (A sees 9 vs 1, B sees 3 vs 3).
  - These are 4 different partitions too, so the count is 4 whichever way "division" is read. Four record boxes are printed.
  - Divide-and-choose:
    - Every two-red / red-plus-blue partition succeeds whichever person divides, and both choices are strict.
    - In the all-red / blue partition, the only tie in the problem occurs when A divides: B sees 3 vs 3. One tie-break succeeds and the other fails A.
    - When B divides, every partition with a successful outcome succeeds.
- **P2 (R1, R2, B1, B2):**
  - Both totals are 8 and half is 4.
  - Exactly 5 of 16 labelled allocations are envy-free for both: A gets R1,R2, or A gets one red and one blue (4 ways).
  - The proportional-for-both allocations are the same 5, so the answer to "Which … are proportional for both people?" is all of them.
  - The saved-table rows are (6, 2, 8, 4) for the colour split and (4, 4, 8, 4) for a mixed split.
  - Six record boxes for five answers; the guide calls the sixth spare.
- **P3 (300 mm strip, red 0–150, blue 150–300):**
  - A's equal-value cut is at exactly 100 mm. A sees (2, 2) and B sees (2/3, 10/3), so B takes the right piece.
  - B's cut is at exactly 200 mm. B sees (2, 2) and A sees (10/3, 2/3), so A takes the left piece.
  - Both cuts are unique, and each person gets at least 2 of their own total of 4.
  - The launch example is correct (75 mm of a 150 mm panel worth 2 is worth 1). It is a non-task value, since no task panel is worth 2.
- **P4:**
  - Both answers are yes. The cutter gets exactly half, the chooser's piece is at least the average of the two, and the chooser does not envy.
  - The join-cut trial with both people using A's values fails: the chooser takes red (3), and the cutter gets blue (1), which is less than 2 and less than 3. It does not contradict the first part, because the join cut is not equal-value for the cutter.
- **P5:**
  - No whole-card allocation is envy-free. In every allocation one tray holds fewer cards, so its owner envies.
  - After replacing R3 with the paper copy, an envy-free division exists. In fact it is envy-free exactly when each person gets one whole card and exactly half the paper's area. With fixed halves, 4 of 16 allocations work.
- **P6:**
  - Each total is 12 and one third is 4. The initial A:X, B:Y, C:Z gives every person 4, so it is proportional.
  - It is envy-free for nobody: A envies B, B envies C and C envies A.
  - The only envy-free allocation of all 27 is A:Y, B:Z, C:X. Exactly 2 of the 27 are proportional.
- **P7:**
  - Two people: no and no. The conditions are equivalent, and this holds even without nonnegativity.
  - Three people: yes (the initial P6 allocation is an example) and no (envy-free implies proportional).

### 1. Guide p. 8, "Visit A": the tie is placed on the wrong partition

- **Text (guide p. 8, "Visit A"):** "The two-red / red-plus-blue partition from Problem 1 leads to a separate question about which divider/chooser roles make success certain and why a tie matters."
- **Evidence:** in every two-red / red-plus-blue partition, both possible choosers choose strictly. If A divides, B sees 2 vs 4. If B divides, A sees 6 vs 4. So that partition succeeds for either divider and has no tie. The guide's own p. 4 says the same. The only tie in Problem 1 is in the **all-red / blue** partition when A divides: B sees 3 vs 3, and choosing the reds leaves A with 1 vs 9. That is the partition where the roles matter. (`out_check_math.txt`, "divide-and-choose" lines and the FAIL line.)
- **Smallest fix:** change "The two-red / red-plus-blue partition" to "The all-red / blue partition". Or write "Comparing the two-red / red-plus-blue partition with the all-red / blue partition leads to …".

### 2. Student p. 2, Problem 2: "Find every complete division" counts 5 only if swapping the two trays counts as different

- **Text (p. 2):** "Find every complete division that is envy-free for both people. … Different card labels count as different cards."
- **Intended answer (guide p. 4):** 5 labelled allocations, A ← {R1,R2}, {R1,B1}, {R1,B2}, {R2,B1} or {R2,B2}.
- **Other reading:** on p. 1 "divide" means making two trays before anyone owns them ("Divide these cards into two trays; your partner chooses a tray first"). A child who counts divisions in that sense finds the colour split and two mixed partitions, {R1,B1 | R2,B2} and {R1,B2 | R2,B1}: **3** answers. For each mixed partition both owner assignments work, and the label sentence does not say whether the swapped one is another division. (`out_check_math.txt`: "counted as unordered partitions … only 3".) In Problem 1 the two readings agree (4 and 4), so the difference first shows up here.
- **Mitigation:** the record boxes have A and B sides, and the guide says that exchanged labels give "distinct valid records".
- **Smallest fix:** "Find every way to give all four cards to A and B that is envy-free for both people." Or add: "Giving the same two trays to the other people counts as a different division."

### 3. (Trivial) Guide p. 1 overview: "above one third" does not fit the cited example

- **Text (guide p. 1, "Why the relationships hold"):** "With three people, being above one third of the total need not make the own bundle largest. Problem 6 supplies a complete example with own value 4, competing values 8 and 0, and total 12."
- **Evidence:** 4 is exactly one third of 12, not above it. The sentence is true, but the example only shows "at least one third".
- **Smallest fix:** "being at least one third of the total".

### 4. (Trivial) Student p. 3 launch picture: the output pieces are drawn shorter than the halves

- **Diagram (p. 3, above Problem 3):** "Two equal lengths" shows a 48.9 mm panel cut at its centre into two 24.4 mm halves labelled 75 mm. The "Output: value 1 each" pieces are drawn 20.9 mm wide, about 86% of a half. (`out_check_diagrams.txt`, "p.3 launch" note; `students.tex` draws them at x = 136–157 and 164–185.)
- **Why it matters:** the page's rule is "value follows length". The two output pieces are equal, so the value labels stay right, but the picture shows the cut pieces shrinking.
- **Smallest fix:** draw each output piece 24.5 mm wide. For example, move the second arrow to 120–129 and draw the pieces at 132–156.5 and 160.5–185.

## Materials (pp. 1–10): check out

- **Values:** the card values and dots match the student pages. A/B are (3, 1) and (1, 3), U/V are 1, and the X/Y/Z observer cards match the p. 6 table.
- **Sizes:** all sizes are as stated (25 mm cards, 100 × 150 mm cards, 50 × 40 mm panels, 150 × 40 mm halves, 100 mm bars).
- **Strips and counts:** strips 1–10 each have one red and one blue half. The guide's print arithmetic is right: 42 sheets give 100 halves, which is 50 strips or 10 per pair; 27 sheets give 4 strips per pair; there are 19 student sheets.

## Adult guide (pp. 1–9): correct apart from Problems 1 and 3 above

- **Overview:** the statements are true with the stated hypotheses (complete allocation, additive values, nonatomic and divisible for the cut theorem). Envy-free implies proportional. The two-person equivalence holds. Three people can be proportional while everyone envies. Whole items can block both conditions. A single interval cut exists by continuity. Cut-three-and-choose does not inherit the guarantee.
- **P1 and P2:** the tables are exactly right (4 and 5 rows with the printed own/other values), and so are the counting arguments (A needs 3r + b ≥ 5 and r + 3b ≤ 3; then 3r + b ≥ 4 and r + 3b ≤ 4). The divide-and-choose paragraph on p. 4 is right, including the A-divides tie. The "useful failed trial" (A sees 4 vs 6) is right.
- **P3 and P4:** the 100/200 mm cuts, the value table, the uniqueness claim, the proof of both "yes" answers and the join-cut analysis are all right.
- **P5:** right: the 1, 3, 3, 1 count histogram, the impossibility, the characterization (one whole card each plus exactly half the area), and 4 assignments for fixed halves. The odd-count return question is also right.
- **P6 and P7:** the observer table, the envy cycle, the unique repair, "2 of 27 proportional", the 3³ exhaustion argument and both proofs are right.
- **Cutting-error extension:** (2 + e/50, 2 − e/50) holds for both cutters, because the relevant density is 3/150 in each case.

The guide is correct apart from the Visit A sentence and the overview wording above.
