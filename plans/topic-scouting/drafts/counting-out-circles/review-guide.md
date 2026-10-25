# Review: Counting-out circles facilitator guide, draft v1

I reviewed `draft/facilitator.pdf` (6 pages) and its sources against the final student pages (K–1: 8 pages, grades 2–3: 7 pages, grades 4–5: 8 pages). I rendered and read every page. I also read the outline, the two page reviews and the Week 98 and Week 87 model guides. I did not edit the guide or the pages.

**How I checked.** `review-guide-check/verify.py` simulates the game literally: a fixed ring of spots, a chant said only to standing counters, and turns that carry on across laps. I wrote it without looking at the author's `check_guide.py`. It recomputes every number, list, sitting order and count the guide prints, plus the launch, the misreading, the spot gaps and the sheet and counter totals. Its output is in `review-guide-check/verify.out`. Results:

- Every printed value agrees with the simulation.
- The overview's theorems hold for n ≤ 1024, with the step rules checked for chants of 2 and 3.
- The compile log has no overfull or underfull boxes.

**Verdict.** This is a strong, correct guide. I found no must-fix items.

- The overview opens with real theorems and followable proofs, and its band map works.
- Every answer and every "find all" list is right, and each list comes with a completeness argument.
- Problem numbers, page numbers, mats and counts match the final PDFs, not the earlier draft. For example, it uses number 23 (not 21) in grades 4–5 Problem 6, the 12 → 9 binary example, checks of 14 and 20 or 14 and 21, and K–1 rings 7–10.
- The launch is a non-task instance (eleven people with a chant of four) and gives away no answer.

The should-fix items are about operations: carrying the launch over to the counters, and how the K–1 table actually runs.

## Must-fix

None found.

## Should-fix

### 1. The launch never shows children how the counters stand in for people, and its last instruction is unclear (p. 2, "Launch")

- **What the guide says:** After the human circle, the guide only *says* "on the mats a counter is a person, one side up for standing, flipped when that person sits". Then: "each table says its own, shorter chant once together, and looks for who is last in many circles".
- **What it leaves out:** Nobody shows flipping, skipping a flipped counter, or (at the older tables) the printed convention "put counters on spots 1 to 10 … and leave the other spots empty". AGENTS asks for explicit bridges between representations, and for a demonstration of a legal attempt on the actual materials. The Week 87 model launches on its real cards and tokens.
- **The unclear sentence:** "Says its own, shorter chant once together" does not tell the adult what to do.
- **Fix:** Replace that sentence with a 30-second replay on counters at each table, after the minute of handling. Each replay uses a chant of four, which no problem uses, so it is still a non-task instance. My simulation confirms both orders.
  - **Grades 2–3 and 4–5:** The adult puts 11 counters on spots 1–11 of the 16-spot mat (page 5 or 6) and replays the launch: 4 sits, 8 sits, then 9, 10 and 11 stand, the chant skips empty spots 12–16, and 1 sits. Reset.
  - **K–1:** On the ring of 7 (page 2), 4 sits, then 5, 6 and 7 stand and 1 sits. Reset. Use this ring rather than the 16-spot one, because the K–1 rule is "a counter on every spot".
  - **Then:** Say the table's own chant ("stand, sit") and what to record: a ring round the number in K–1, a table entry for the older bands.

### 2. How the K–1 table actually runs is not stated (pp. 2–3, "Materials", "Staffing", K–1 solutions)

This table is staffed by the parent who is not a mathematician, so these gaps matter most here.

- **Packets versus counters.** The guide prints "one 8-page packet per child" but gives "16 counters per pair". It never says whose page the pair plays on.
  - If each child plays every circle on their own page, the flips double. The 30-minute estimate for Problems 1–4 assumes one play per circle.
  - **Fix:** Say "the pair plays each circle once, on one child's page (take turns whose), and both children draw the ring on their own page". Alternatively, print one working packet per pair.
- **One ring at a time.** The K–1 rule says "Put a counter on every spot". Page 1 has 18 spots and page 3 has 19, more than the 16 counters.
  - **Fix:** Add "Play one ring at a time; move the counters to the next ring after drawing the ring round the last number."
- **Who writes the answers.** K–1 Problems 4, 5 and 8 ask for written answers or explanations, but the rings are not labelled with their sizes.
  - **Fix:** Add "Children point to the rings; the adult writes each circle's biggest number in the Problem 4 boxes and scribes spoken reasons for Problems 5 and 8." That is routine recording, not running the investigation.

## Minor

1. **Launch group sizes (p. 2).** The guide says "With fewer than eleven children, add adults to make 7 or 11". The chanting adult walks outside the circle, so only two of the three adults can join.
   - With 8 children, neither 7 nor 11 can be reached.
   - With 12 or more children, the guide gives no size.
   - **Fix:** "Any circle of 7, 11 or 15 works (one less than a multiple of 4), so 1 sits at the wrap; a child can be the chanter."
2. **Repetition (whole guide).** The guide runs 4,834 words, against 3,026 for Week 98 and 3,372 for Week 87. The restart misreading is explained seven times: in "Limits", Staffing, the launch twice, Hints, K–1 Problem 1 and Sources. Cuts that lose nothing:
   - the Staffing parenthetical "(the circle of 3 is the first where restarting at 1 changes the answer)";
   - the second half of the launch's last sentence ("and a circle of 8 never shows …");
   - the Sources sentence "The page reviews … identified the restart misreading, why a circle of 8 cannot show it, and the rival binary rules", which is process history, not help for a facilitator;
   - in grades 4–5 Problem 8, the restated step-rule proof: replace it with "the step rule's proof is in the overview; in children's terms, once 3 sits, 4 starts a circle of n − 1".
3. **Step-rule proof wording (p. 1).** "In a circle of n the first person to sit is 2 (or 3)" is false for a circle of 2 with the chant of three, where person 1 sits first. The parenthetical patches this afterwards.
   - **Fix:** "the first person to sit is the one who gets the last word of the chant: 2, or 3 (person 1 in a circle of 2)".
4. **K–1 Problem 4 (p. 3).**
   - The answers "3, 5 and 9" and "6 and 10" are complete only for the circles on the pages. Add "of the circles they played; bigger circles 17 and 33 also leave 3, and 18 and 34 leave 5" as a spoken extension.
   - The hint "Which circle comes just after a star?" points at a pattern rather than at the task. For a child who cannot find the circles, use "Where did you draw a ring round a 3?", and keep "just after a star" as the extension.
5. **K–1 Problem 3 (p. 3).** "Stars on the circles of 4 (page 1) and 8 (page 2)": add "and on the circle of 16 once it is played", since page 4 also asks for stars.
6. **K–1 Problem 2 hint (p. 3).** "Which circle you already played is most like this one?" is ungrammatical. Use "Which circle that you already played is most like this one?"
7. **"Grades 2–5 Problem 9" (p. 1, Every third person).** Write "grades 2–3 and 4–5 Problem 9".
8. **Band map, grades 2–3 "short reading" (p. 1).** The shared rules paragraph on page 1 is about 100 words. Write "an adult reads the opening rules; problems are one or two sentences".
9. **First-visit timings for the older bands (pp. 2–3).** Only K–1 gets an estimate. Grades 4–5 Problems 1–2 are 194 flips for one pair, about 15–20 minutes. Saying so makes "Problems 3–4" the honest first-visit reach and "5–6 if quick" believable. Give grades 2–3 a similar rough split.
10. **Grades 4–5 Problem 10 (p. 6).** "giving 2L + 1, Problem 4's answer": Problem 4 asks for 73 and 977, not a rule. Write "the rule behind Problem 4's answers".

## Checklist results

1. **Correctness:** all answers verified (see `verify.out`).
   - K–1: 3, 1, 3, 5 / 7, 1, 3, 5 / stars 4, 8 / 16 → 1 / {3, 5, 9}, {6, 10} / 2, 1, 4, 1, 4, 7 / circle of 9 → 1, sitting order 3, 6, 9, 4, 8, 5, 2, 7.
   - Grades 2–3: the 1–16 table; 9, 19, 1; even numbers; laps of 16; {12, 20, 36}, {1, 3, 7, 15, 31}; 37, 73; J₃ for 1–20; checks 2 and 20; 29.
   - Grades 4–5: {1, 2, 4, …, 64}; 73, 977; 41, 43; {27, 43, 75}, none; checks 2 and 2; 31, with 16 last to sit; the binary examples and the swap and reverse rivals.
   - Launch: sitting order 4, 8, 1, 6, 11, 7, 3, 2, 5, 10, with 9 last.
2. **Agreement with pages:** problem numbers, page numbers, mat pages (2–3 pages 5–7, 4–5 pages 6–8), sheet totals (32/22/18 = 72) and counters (128) all match. The spot-gap claim (about 2 mm on the rings of 9 and 10 and the 16-spot rings) matches the TikZ geometry (0.205–0.212 cm).
3. **Overview:** passes.
   - It states J(n) = 2L + 1 with assumptions: the chant carries past 1, counting starts at 1, empty spots are skipped.
   - It proves the step rules, doubling and the binary rotation.
   - It gives limits (the restart misreading and the circles that cannot reveal it).
   - It separates experiments, conjectures and explanations, and maps the bands before any solution.
4. **Launch:** brief, concrete, on a non-task instance, and free of the theorem and of every answer. It has a three-panel worked visual. The bridge to counters is missing (should-fix 1).
5. **Usability:**
   - Preparation (about 15 minutes plus printing) and staffing are realistic, and every band has a first route and a return route.
   - All hints are questions.
   - The K–1 table operations need the details in should-fix 2.
6. **Brevity:** no generic encouragement and no narration of the pages, but repetition (minor 2).

## What works and should be kept

- **The overview.** It is theorem-first with complete short proofs (step rule by renaming, 2L + 1 by "L sit, then a power of two starting with a stand", doubling, binary), plus the "Limits, and the one misreading that matters" paragraph. An adult learns the destination without reading the solutions.
- **The launch.** Eleven children, a chant of four, the pause at "who gets the next word?" after 9, 10 and 11, person 1 sitting at the wrap, and the stated reason for avoiding every-second circles.
- **Staffing.** The toucher-and-flipper roles that swap every circle, the 4–5 referee who watches the wrap, "the adult's main job is the wrap", and "if the adult is doing the counting, move to a smaller circle".
- **The K–1 plain-words key**, with "use the key to know when to ask for a replay, not to give answers".
- **The replay-not-correct hint** for entries that break a pattern, and the restart and sitting-counter hints.
- **Completeness arguments** for every "find all" problem: grades 2–3 Problem 5, grades 4–5 Problems 3 and 6, and grades 2–3 Problem 3 in both directions.
- **"Evidence, not yet a reason"** for K–1 Problem 5, and the discretionary "How do you know…?" follow-ups kept in the guide.
- **The informative-check notes** for grades 2–3 Problem 8 and grades 4–5 Problem 8 (14 and 21 test "drop to 1"), and the rival rules in grades 4–5 Problem 10 with the "try 8 and 16" hint.
- **The grades 2–3 split** of Problem 1 into 55 and 65 flips, with a pooled table and cross-replays.
- **The Status paragraph** naming exactly what is physically untested, the honest note that Concrete Mathematics was not consulted, and the record-after-session list.
