# Week 83 adversarial review

Reviewed 9 October 2026 as the fresh critic stage. No student, guide, builder, index, or repository edits were made.

## Verdict

The student packet is a strong usable draft. Retain its concrete game core, contrasting balance boards, and readiness-gated nursery. No mathematical error was found in its printed cases. Revision should fix the facilitator clipping and preparation mismatch, and supply the short concrete balance argument below. These are targeted fixes; do not replace the investigations with directed solution steps.

## Scope and evidence

Read PROMPT.md and CRITIC.md including the selected-band override; read actual student TeX/build.py and actual facilitator TeX. Independently rendered all seven student/material pages and all five guide pages at 1.4x with PyMuPDF, then viewed every PNG. Header strips were inspected separately to confirm matching headers on every page. Student pages 1–4 and 7 say Grades 2–5; pages 5–6 say Grades 4–5. All footer IDs/page numbers are present. Renders and extracted text are in `critic-renders/` and are review intermediates.

An independent recursive solver, written for this review without importing the author's code, checked legal cuts and both starting colors for every printed game. Results:

| Board | Outcome with optimal play |
|---|---|
| Problem 1 A | Blue wins with either starter |
| Problem 1 B | Red wins with either starter |
| Problem 1 C | Second player wins |
| Problem 1 D | Blue wins with either starter |
| Problem 2 A | Red wins with either starter |
| Problem 2 B | Second player wins |
| Problem 2 C | Blue wins with either starter |
| Problem 3 A | Red wins with either starter |
| Problem 3 B | Second player wins |
| Problem 3 C | Blue wins with either starter |

The source paper's standard normal-play game/number setting was also opened: Schleicher–Stoll, *An Introduction to Conway's Games and Numbers*, https://arxiv.org/html/math/0410026v2. The numeric, simplicity, and operation distinctions in the draft match that setting. This is a mathematical and digital review; no physical rehearsal or classroom trial took place.

## Required guide fixes

1. **Guide page 4: the Day 3 birthday list is clipped beyond the right page edge.** The line beginning “Day 3 introduces” is an unbreakable inline mathematical list. Its last visible text reaches the paper edge; PyMuPDF reports a slash span extending to x=616.34 on a 612-point-wide page. Break the day lists into separate lines or a short display/table. Rebuild and inspect this actual page, not only the source.

2. **Guide page 2: “supplied stalk cards” are not supplied.** The packet has large printed example boards and a blank ground-line workspace, plus number/birthday cutouts; it has no stalk cutout cards or removable red/blue strip sheet. The authorized erasable-board route is sufficient. Describe exactly that route: print the game boards and blank board, use a reusable sleeve/lamination and erasable red/blue marks, or separately provide removable segments. If magnetic segments are chosen, they remain externally prepared materials. Remove the nonexistent-card claim. In the optional nursery, specify printing/cutting page 6 separately so children do not have to sacrifice their active task sheet mid-investigation.

3. **Guide page 3: include an actual object-based argument for the central half balance.** Numerical addition and “children can enumerate” currently leave the adult to discover the complete reply strategy. Add the following concise proof for Problem 2 B, using the bottom-to-top convention and avoiding a mandatory response tree on the student page:

   - If Blue removes the base of one BR, Red removes the top R of the other BR. This leaves B+R with Blue to move; each takes their sole edge, so Red moves last.
   - If Red first removes the lone R, Blue removes one whole BR. Red must remove the remaining top R, then Blue removes its base and wins.
   - If Red first removes the top R of a BR, Blue removes the other whole BR. This leaves B+R with Red to move; Blue moves last.

   These cases cover every legal first move, up to exchanging identical stalks. They establish the printed balance by concrete play. Keep the theorem about equality in all game-sum contexts separate: this finite reply argument proves the selected board's outcome, while the standard number theorem establishes the half arithmetic.

## Recommended small guide clarifications

- Give a compact problem-to-board outcome key using the table above; this also supplies Problem 1 D and the two nonbalance quarter boards, currently only implicit in the adult prose.
- For optional Problem 6, say children can put a lower-bound card, selected card, and upper-bound card left-to-right on the table, reusing cards between attempts. The only printed mats currently have fixed bounds. A blank mat is optional; do not add a new representation demand.
- “Find a way” on Problem 3 properly asks for strategy. The guide should tell adults to use selected first-move counterexamples if children call one lucky play a guarantee, rather than ask every child to copy an exhaustive tree.

## Student page-by-page review

1. **Page 1: pass.** Shared rules state one stalk per move, disconnected material disappears, and no move loses. The BRB non-target visual contains input, marked removed R/intermediate detached top B, and the remaining grounded B. It reveals a legal action without revealing the balance. Ground and B/R labels are legible. Four starter-swapped boards provide concrete early play. The smallest drawn edge is 22 mm.
2. **Page 2: pass.** “Balances” is defined operationally as a second-player winning strategy for either starting color. The three contrasting boards are large and do not print the half value or correct answer. The answer is B; A and C have opposite winner classes. No extra bookkeeping is imposed.
3. **Page 3: pass.** All bottom-grounded BRR and RB diagrams have the correct colors/order. B is the balance; A is negative and C positive. There is enough working space and the aim is substantial.
4. **Page 4: pass.** Two large ground boards support making different balances with a nontrivial stalk. Children choose their own approach. Neither the target catalog nor a recipe is given away.
5. **Page 5: pass.** The bounds-to-candidates-to-oldest worked example (-2,2) is a non-task example. The {0|3} task genuinely distinguishes simplicity from midpoint insertion. Other answers are 0, 1/2, and 3/4. Strict inequality and reuse are explicit. This page needs the signed-number/fraction prerequisites already correctly gated in the guide.
6. **Page 6: pass with preparation clarification above.** All day 0–3 cards and birthdays are correct: 1+2+4+8=15 cards. Cutouts are 40 by 24 mm and match the center slot dimensions. Exact-size fit has zero design clearance and is digitally plausible, but physical cutting/placement is untested; retain that limitation. The problem asks for meaningful constraint design rather than arithmetic drills.
7. **Page 7: pass.** One large reusable grounded workspace, correctly labeled extra workspace. No duplicate numbered task or facilitation language.

## Facilitator strengths and limits

The guide opens theorem-first, states assumptions and the numeric destination, distinguishes experimentation from full-context equality, and maps concrete cutting versus nursery readiness. It keeps ordinary ordinal concatenation separate from commutative surreal addition and makes infinity an optional adult doorway. Timing, staffing, referee rotation, source attribution, unpiloted status and physical-fit limitations are present. The core works without fraction knowledge and can sustain a session; the nursery is correctly a return visit/choice, not forced on all Grades 2–5 children.

No student layout clipping, overlap, broken glyph, or inaccessible tiny diagram was found. The required changes are in the guide/preparation; guide repairs alone should not be claimed as student revisions. After any student change, inspect all seven actual final pages again. After guide changes, render and inspect all five actual final guide pages. Clean ZIP rebuild and delivered-version synchronization remain root/revision responsibilities.

## Reviewed PDF hashes

- students.pdf: `973527d26a184997193a4b9ebf9f4968fb764ba71f3f29c3820d9ace4dbcef94`
- facilitator.pdf: `57735772745dca401b12b8bef30e241894b3cde86143d06d466ee48a3f0a9779`
