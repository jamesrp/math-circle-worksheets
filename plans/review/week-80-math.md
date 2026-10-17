# Week 80 (Midnight laboratory): math check

Scope:
- `lowell-math-circle-year-2/week-80/week-80-students.pdf`: one selected-band packet, 5 pages.
  - pp. 1–2 (Grades 2–5): the light story, the fold worked visual, Problems 1–2.
  - pp. 3–4 (Grades 4–5): Problems 3–5.
  - p. 5 (Grades 2–5): cut-out time strip, position strip, ON and OFF panels.
- `week-80-facilitator.pdf`: 4 pages.

Sources read: `source/week-80/student/students.tex`, `guide/facilitator.tex`, `README.md`, `QA.md`, `SOURCES.md` and `build.py`, plus the outline `worksheet-workflow/outlines/week-80-midnight-laboratory.md` for intent. I rendered every student and guide page and read them. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-80/`. Checked October 17, 2026, against the organizer-approved PDFs of October 16.

**Result: every printed fact, answer and diagram is mathematically correct. I found 2 problems, both minor and neither a wrong statement. (1) Problem 4 invites "extra rules" such as "flip once more at midnight" or "stay as it was", which cannot be carried out at all, and the guide does not tell the adult this. (2) The p. 3 MIDNIGHT box is smaller than the ON/OFF card it seems meant to hold.** A few non-mathematical inconsistencies are listed at the end for the card stage.

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures):
  - Reads the opening rule from `students.tex`. Builds the switch times by replaying "halfway from the previous switching time to midnight" from the given 11:30 and 11:45, for 200 switches, in exact fractions. The closed form 1 − 2⁻ⁿ is only compared with the replay.
  - Clock times and positions on the 180 mm line:

    | Switch | Clock | Mark from 11:00 | Gap to MIDNIGHT |
    |---|---|---|---|
    | 1 | 11:30 | 90 mm | 90 mm |
    | 2 | 11:45 | 135 mm | 45 mm |
    | 3 | 11:52:30 | 157.5 mm | 22.5 mm |
    | 4 | 11:56:15 | 168.75 mm | 11.25 mm |

  - Replays the card from OFF and confirms the states ON, OFF, ON, OFF. After switch n the card is ON exactly when n is odd.
  - For ε = 2⁻ᵏ (k < 150), the interval (1 − ε, 1) contains both an ON time and an OFF time. So neither endpoint value is a left limit.
  - Builds the ON and OFF endpoint extensions. Both satisfy every constraint of the printed rule, all of which concern times before midnight, and they differ at midnight.
  - Replays the counter's halving moves: the gap halves each move, never reaches 0, and falls below any tested tolerance at a computed N.
  - Checks the guide's averages remark and the 45-minute first route.
  - Replays the Week 79 rule from its own `students.tex` to test the encore sentence.
  - Physical numbers (counter sizes, fold error on the cut strip) for the notes below.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures; `FINDING` lines are the observations reported here):
  - Reads the delivered student PDF with pdfplumber: page size, headers, footers and band labels, and problem numbers 1–5 in order.
  - Every timeline and strip (pp. 1, 2, 3, 5) is exactly 180.00 mm between its end ticks, with its end labels inside the ticks.
  - p. 1 worked visual: three equal 52 × 18 mm strips. The crease and the unfold mark are at the exact midpoints. The folded half is 26 mm, and the fold arrowhead is over the 11:30 end. Labels: 11:30 and MIDNIGHT at the Input ends, and 11:45 centred under the mark.
  - p. 2: the counter circle is 6.00 × 6.00 mm, centred on the START tick.
  - p. 5: two 184 × 36 mm cut rectangles with the ticks 2 mm in from each edge, and equal 76 × 54 mm ON and OFF panels.
  - p. 3: box size compared with the card. p. 4: the two "At midnight:" boxes.
  - Uses pdftotext to confirm the guide sentences quoted here.

The infinite statements are proved by hand; the replays only corroborate them:
- **Switch times.** t₁ = 1/2, and t_{n+1} = (t_n + 1)/2 gives t_n = 1 − 2⁻ⁿ by induction.
- **No last switch.** If t < 1, then (t + 1)/2 − t = (1 − t)/2 > 0 and 1 − (t + 1)/2 = (1 − t)/2 > 0. So every switch has a later one before midnight.
- **No limit for the card.** By induction from OFF, the state after switch n is ON exactly when n is odd. Given ε > 0, choose n with 2⁻ⁿ < ε. Then t_n and t_{n+1} both lie in (1 − ε, 1) and show different states. So the state has no left limit at midnight, and no endpoint value makes it continuous there.
- **Endpoint not determined.** The rule fixes the state only at times t < 1 (OFF at 11:00, a flip at each t_n). Setting midnight to ON, or to OFF, satisfies all of it. The two extensions differ, so the rule alone does not decide.
- **Counter.** Its position is p_n = 1 − 2⁻ⁿ < 1, and the gap 2⁻ⁿ falls below ε once n > log₂(1/ε). So the left limit at midnight is END.

## Student packet, Grades 2–5 pages (pp. 1–2, 5): checks out

- **Opening and worked visual (p. 1):** the given switches fit the rule. 11:45 is halfway from 11:30 to midnight, and 11:30 is halfway from the 11:00 start. The fold demonstration (MIDNIGHT meets 11:30, crease = 11:45) is geometrically exact.
- **P1:** no last switching mark, by the step above. The four requested marks are at 90, 135, 157.5 and 168.75 mm, leaving an 11.25 mm gap. After four flips the card shows OFF.
- **P2:**
  - The card never settles: ON after odd switches, OFF after even ones.
  - The counter approaches END and never reaches it.
  - On the equal 180 mm lines the counter's positions coincide with the time marks. This is the intended parallel, not a shortcut that answers the card question.
- **Materials (p. 5):** both strips are 180 mm between ticks, and the ON and OFF panels are the same size for gluing back-to-back.

## Student packet, Grades 4–5 pages (pp. 3–4): correct; problems 1 and 2 below

- **P3:** the rule alone says nothing about midnight, since both endpoint extensions satisfy it. Support from the card and marks: both states occur after any mark, however late.
- **P4:** ON and OFF are both consistent extra rules, and neither follows. See item 1 for rules that refer to the state just before midnight.
- **P5:** the limit rule assigns END to the counter and nothing to the card.

## Adult guide: correct, except the gap in item 1

The overview checks out:
- the switch times, including 11:52:30, and t_n = 1 − 2⁻ⁿ;
- the post-switch states, "no limit", and "both states occur arbitrarily close to midnight";
- "no last switch";
- "the instructions for t < 1 alone do not determine the state at t = 1";
- ON or OFF appended as an endpoint is consistent, and requiring continuity at 1 is impossible;
- the counter's convergence to 1.

Hypotheses are stated: two distinct states, the rule covers only t < 1, and the post-switch convention.

The answers are also correct:
- P1: a further halfway mark always exists.
- P2 and P5: the counter's gap halves, and every tolerance is eventually beaten.
- P5: the odd and even subsequences are constant and different, so the states have no limit.
- The averages remark: the running averages tend to 1/2, which is a different question.
- The encore sentence on Week 79: under its smallest-card rule, label k is in B from day k on, so each label settles, while |A| = n grows and the limit of A is empty.

The first route totals 45 minutes after the movement break.

### 1. Student p. 4, Problem 4, and guide p. 3 (minor): some natural "extra rules" cannot be carried out, and the guide only covers ON, OFF and "undefined"

- **Quoted text.**
  - Student: "Keep every switch before midnight. Make two different extra rules for the card at midnight. Decide whether either extra rule follows from the original switching rule."
  - Guide p. 3: "Problems 3–4: if a child predicts ON at midnight, invite an OFF group to identify a different additional assumption. Ask whether either is forced by the earlier moves. If a child says undefined, ask what is specified before midnight…"
- **Evidence.** The light "keeps switching", so a likely child rule is "at midnight it flips once more". Another is "at midnight it stays the way it was". Both need a state just before midnight, which means a last switch or a left limit. Neither exists: `check_math.py.out`, Card and Endpoint blocks, and the proof above. So these rules do not choose a side at all. That differs from ON or OFF, which are consistent but not forced.
  - The guide's only coverage is the overview's "Requiring continuity at 1 is impossible", which covers "stays the way it was" in technical terms. Nothing covers "flip once more".
  - An adult following the p. 3 moves ("Ask whether either is forced") may accept such a rule as a third consistent choice. The child's answer to "Decide whether…" would then be incomplete.
  - The same fact is the heart of Problem 5, so the link is worth giving the adult.
- **Smallest fix.** Add one sentence to the guide's "Problems 3–4" paragraph: "A rule such as 'flip once more at midnight' or 'stay as it was' needs a last state before midnight, and there is none, so it does not choose a side; this is the same obstacle Problem 5 meets."

### 2. Student p. 3, Problem 3 (minor, fit): the MIDNIGHT box is smaller than the card

- **Diagram.** Below the timeline is a rounded box labelled "MIDNIGHT", 66 × 53 mm. The ON/OFF card cut from p. 5 is 76 × 54 mm (`check_diagrams.py.out`, p. 3 and p. 5 blocks). Problem 3 says "Use the card and switching marks to support your answer", so the box reads as the place to set the card, or to leave empty, for midnight. The card overhangs it by 10 mm across and 1 mm down. Neither the page nor the guide says what the box is for.
- **Effect.** No answer changes. A child who puts the card there covers the box completely, and the MIDNIGHT label above it stays visible. This is cosmetic, but the sizes were plainly meant to match.
- **Smallest fix.** Draw the box at least 80 × 58 mm. In `students.tex`, line 122 becomes `(52,10) rectangle (132,68)`, with the line-123 label moved to y = 73 and the line-121 bounding box raised to height 78. Or, if the box is meant for writing, say so in the guide.

## Outside the mathematics (for the card stage; not counted)

- **Band labels.** pp. 3–4 are headed "Grades 4–5". Guide p. 2 says "Problems 3–5 are a Grades 3–5 continuation", and the index and README say "Grades 3–5 endpoint discussion". Guide p. 1 says "Grades 4–5 can separate an endpoint convention from a consequence".
- **"Six drawings".** Guide p. 3 says "This is not a proof from six drawings". The packet and guide p. 2 use four marks ("Work on the first four halves only"); six is the outline's figure. The argument is unaffected.
- **First-route wording.** Guide p. 2 says "for Grades 2–3 use Problems 1–2 only", but its timing then includes "five minutes considering extra endpoint rules", which is Problem 4's content.
- **Fold demo against the cut strip.** The p. 1 demo draws the end ticks at the paper's edge. On the p. 5 strips the ticks are 2 mm in from each cut edge. A child who folds the paper edge, not the MIDNIGHT tick, onto the last mark gets marks off by 0, 1, 1.5 and 1.75 mm. That is at most 35 seconds of clock time, and the first fold is exact either way. Negligible.
- **Counter size.** The guide says only "one counter". The END tick stays uncovered through move 4 for counters up to about 22 mm across: a 19 mm counter leaves a 1.75 mm gap, while a 25 mm counter covers END at move 4. The guide's "stop physical moves before counter size hides the gap" handles it. Naming a counter of 15 mm or less would avoid the question.
- **Not checked:** the page references for Thomson (pp. 5–6) and Benacerraf (pp. 768–770), which are bibliographic.
