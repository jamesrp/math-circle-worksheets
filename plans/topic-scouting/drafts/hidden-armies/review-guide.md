# Review of the Hidden armies facilitator guide (HA-FAC-v1)

Reviewer: guide critic. I did not write the guide, and I did not edit it or the student pages.

## What I checked

- **Pages.** I rendered and read all 6 guide pages and all 17 student pages: K–1 has 6, Grades 2–3 has 5 and Grades 4–5 has 6.
- **Background.** I read the outline, both page reviews, the drafts README entry, `worksheet-workflow/context.md` and the Week 98 model guide.
- **Build.** I rebuilt the guide from `draft/src/` in `review-guide-check/build/`. The log is clean (no overfull or underfull boxes, no warnings), and the text is identical to `draft/facilitator.pdf`.
- **Answers.** I recomputed every printed answer with my own script, `review-guide-check/verify.py`, which does not use the author's `check_guide.py`. All 89 checks pass. They cover:
  - Theorems 1 and 2 for every N up to 12, 15 and 30 respectively.
  - The equal-hill tie rule.
  - The 28 × 28 table: the beat counts by type, the total of 210, ties of 13 and "beats + beaten by = 15".
  - The 180 three-plan circles, the 12 circles through 2-2-2, and which plans lie on any circle.
  - Every complete list on the K–1 pages (P2, P3, P4, P6 and P7).
  - Every counter-plan in 2–3 P3 and 4–5 P2.
  - Every fewest-cubes answer, including 40-30-30 needing 62.
  - Both parts of 4–5 P7, including the attack used in the "proof for 9" and the case where the partner may use fewer cubes.
  - Ben's and Mia's tables, including that the arrangements of 3-3-0 are the only plans that do better than break even against Ben.
  - The launch claim that every 5-cube type appears on the K–1 pages and no 7-cube launch type appears on any page.
- **Page agreement.** Every problem number, page number, board or strip count (K–1 P7: 4 and 8 boards; 2–3 P6: 6 and 20 strips), packet length, packet id and picture description matches the final PDFs. This includes the row order in K–1 P5 and the arrow direction in 2–3 P5.

**Verdict:** I found no must-fix problems. The answers, the page references and the overview are all sound. The fixes below are about the launch, what the K–1 adult does next, one hint, and some precision and brevity.

---

## Must fix

None.

---

## Should fix

### S1. Page 2, Launch Game 2 demonstrates the counter-plan

B says "I saw your plan, and I'll try to beat it" and builds 2-1-4 against A's previous plan, 5-0-2.

- 2-1-4 does beat 5-0-2. It gives up the tallest hill and puts more cubes than A on each of the other two. That is exactly Theorem 2's counter-plan shape.
- It is also the intended discovery of K–1 P2–P3, Grades 2–3 P3 and Grades 4–5 P2.
- Children who check B's attempt against A's old plan see the construction modelled by an adult before the tables start.
- AGENTS.md asks that the launch not reveal the main theorem.

**Fix:** have B build 2-3-2, or 2-0-5, instead.

- Each still ties A's new 2-5-0 through the equal hill 1, so Game 2 keeps its point.
- Against 5-0-2 each would only have tied (verified), so neither shows a way to win.
- Alternatively, keep 2-1-4 and drop B's sentence. Use "B tries something new" instead.

### S2. Page 2, Staffing, and page 3, K–1 Problems 2 and 4: no next step after a false "safe plan" claim

The guide tells the parent volunteer:

- not to say whether a plan can be beaten;
- to ask the partner to try;
- that "the keys below tell you the truth".

It gives no next move when the partner fails and the hint ("Which hill could you let your partner have?") does not help. That outcome is likely:

- With 5 cubes, 2-2-1 is beaten only by 3-0-2 and 0-3-2.
- With 4 cubes, 2-1-1 is beaten only by 0-2-2.

The first route ends at K–1 P3, so the table can leave believing in a safe plan.

**Fix:** add one sentence giving an escalation in order:

1. Ask the second pair at the table to try.
2. The adult may take one turn as challenger and build the beating plan. This is a legal move in the game, and the children check it hill by hill; it is not a verdict.
3. Otherwise, take the claim to the sharing minutes or leave it open for the return visit, and record it.

### S3. Page 6, Grades 4–5 Problem 8: the hint gives away Ben's answer

The hint "Does it matter which arrangement of 3-3-0 you test?" names 3-3-0. A plan from the 3-3-0 family is the whole answer for Ben, and the hint is given before the child has necessarily found it.

**Fix:** "Against Mia, does it matter which arrangement of a plan you test?"

### S4. Page 1, Theorem 3: "ties exactly 13" is stated without its easy proof

The guide gives "every plan ties exactly 13 of the 28, itself included" as a computed fact. It is also the basis of the Grades 4–5 P4 check that beats plus beaten-by equals 15. The fact has a two-line proof that holds for every N:

1. A game ties exactly when some hill is equal.
2. The number of plans q with q_i = p_i on hill i is N + 1 − p_i. Summed over the three hills, that gives 2N + 3.
3. Each pair of hills that are both equal forces q = p, so subtract 3 and add 1 back for the triple.
4. The total is 2N + 1, which is 13 for N = 6. I verified this for N = 1 to 9.

**Fix:** add that clause. The overview is supposed to carry proof ideas, and an adult can then explain the "15" check rather than just quote it.

### S5. Page 2, Seating and comparing: where the folder stands

Partners sit side by side. A folder stood in front of each child does not hide a plan from a partner sitting beside them. The page says only "stood open as a screen".

**Fix:** stand one opened folder upright between the two partners' mats, like a wall. At the reveal, slide one mat directly above the other, hill 1 above hill 1, as in the K–1 rules picture.

Also say that folders are only needed for hidden games:

- K–1 P1;
- Grades 2–3 P1;
- the opening games of Grades 4–5 P1.

From K–1 P2, Grades 2–3 P2 and Grades 4–5 P1's testing onward, plans are shown openly.

---

## Minor

1. **Page 4 (Grades 2–3 P2) and page 5 (Grades 4–5 P6): predictions read as observations.** "Children often settle on 2-2-2" and "Children tend to skip its second case" describe material that has never been piloted. Use "Expect…", as K–1 P2 already does.
2. **Page 1, Theorem 3: ambiguous wording.** "Plans beaten, by type: 6-0-0 none, …" can be read as "beaten by". Use "Number of plans each beats, by type: …".
3. **Page 1, Theorem 4: counting convention.** For "180 circles", say that each circle is counted once, not once per starting plan.
4. **Page 1, Unpredictability: "guarantees an even score" overstates it.** The die guarantees at least an even score on average. Against 6-0-0 it wins on average; it does not tie every game.
5. **Page 1, The game: a missing case.** "The other two hills then hold equal totals and split one each" omits the case where both are also equal. Use "split one each, or both tie".
6. **Page 6, Grades 4–5 P7, proof for 9: an unstated step.** "Your two smaller hills total at most 5" needs its one-line reason: a total of 6 within at most 9 cubes forces every hill to hold 3, which is 3-3-3.
7. **Page 4, K–1 P7: completeness for 3-1-1 is asserted.** The guide says a winner "needs at least 2 cubes on each of hills 2 and 3" without saying why. Give the reason as for 4-0-1: winning hill 1 costs 4 and leaves 1 cube, and winning one hill while tying two costs 6.
8. **Page 2, Prerequisites: two cross-band claims.**
   - "A quick K–1 child can try Grades 2–3 Problem 6" points to 15 written three-number strips plus a written completeness argument. The matching task for K–1 is K–1 P7. Either drop the claim or say an adult writes the strips.
   - "Grades 2–3 Problem 7 is the same question as Grades 4–5 Problem 6" should say "the same kind of question". The 4–5 version adds 40-30-30 and asks why the rule works.
9. **Page 2, Materials: two small inconsistencies.**
   - "Plans of 10, 20 or 100 cubes are written, not built." But 10 cubes per child let a pair build the 10-cube rows: 2–3 P3 (4-4-2 and 2-5-3), 2–3 P7 (8-1-1 and 5-3-2) and 4–5 P2 (1-8-1). Say "20 or 100".
   - The folder count is one per child, but the two launch adults need folders too.
10. **Page 2, Launch: designer reasoning.** The parenthetical "(Not 5: …)" explains a design choice the adult running the launch does not need. Cut it to "(7, so that no launch plan appears on a page)".
11. **Page 3, K–1 P2: narration.** "In each row the left board is the plan shown and the right board the plan that beat it" repeats the column labels printed on the page. Delete it.
12. **Repeated arguments.**
    - The 1-1-1 argument appears four times: in the overview, K–1 P4, 2–3 P4 and 4–5 P3.
    - "6-0-0 beats nothing" appears three times.
    - Theorem 1 is restated in K–1 P6, 2–3 P7 ("Why: …") and 4–5 P6.

    Where a band entry restates the argument, cite the theorem instead.
13. **Page 3, Pacing: no timings for the older bands.** K–1 gets minutes for each problem, but Grades 2–3 and 4–5 get none. Add rough minutes, for example 2–3: P1 about 10, P2 about 10–15, P3 about 15.
14. **A continuation for quick Grades 4–5 children.** The guide offers none beyond P8. Here is one I verified: with 4 or 5 hills (same rules), a plan nobody can beat exists exactly when the number of cubes is at most the number of hills, that is, when no hill holds more than 1. I checked this for 4 hills up to 12 cubes and 5 hills up to 10 cubes. The same counter idea proves it: give up the biggest hill, top two other hills by one cube each and match the rest, at a cost of N − a + 2. It extends Problem 3 without new materials. Script: `review-guide-check/hills.py`.
15. **Page 6, Sources: one source not verified.** I could not reach the Competitive Kids page from this environment (the proxy returned 403). The guide's quote "the only protection is unpredictability" and its "3, 5 or 7 fronts" are not in the outline, which says "3 to 7 fronts" and was accessed October 24. The reviser should confirm the October 25 consultation actually happened, or attribute these details to the outline.
16. **Page 3, launch figure: missing labels.** The output strips have no A/B labels. The rows line up, but adding "A" and "B" would make the labels match across all three panels.
17. **Recording conventions for K–1.** The launch shows strips for the older tables but does not show how K–1 children record. The rules picture on K–1 page 1 does show towers on hills, so this is minor. One line telling the K–1 adult to point to that picture when Problem 2's boards first come up would close the gap.

---

## What works and should be kept

- **The overview is genuinely theorem-first.**
  - "Cheapest win = b + c + 2" comes with a complete case proof.
  - "Safe iff no hill above 1" comes with the counter-plan and the exact list of exceptions (1, 2 and 3 cubes).
  - The 6-cube ranking and the circles are labelled as exhaustive checks.
  - The limits are explicit: three hills, majority of hills, equal hill to nobody.
  - Experiment, conjecture and explanation are kept apart.
  - The band map is short and useful.
  - The remark on mixed strategies is correct, including the optimality argument for Mia's die, and it is tied to one problem.
- **Every answer is right and keyed to the final pages.**
  - The "find all" answers come with completeness arguments a child could give (K–1 P7, 2–3 P6).
  - The K–1 lists give a non-mathematician parent the truth to check against.
- **The launch** uses non-task 7-cube plans. It has a clear input / tokens / strips figure, shows an empty hill and an equal-hill tie, and says "both may change" once.
- **The staffing lines are good.** For example: "do not choose plans or say whether a plan can be beaten"; "if the adult is choosing the plans, return to building with cubes".
- **Honest status.** The physically untested points are named, and the preparation time is marked as untested.
- **First routes and return visits for every band**, including the note that the shared table can fill most of a session.
- **Sources state honestly what was and was not consulted.** The after-session record list is concrete.
