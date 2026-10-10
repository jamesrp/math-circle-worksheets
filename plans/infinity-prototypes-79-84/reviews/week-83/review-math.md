# Week 83 independent mathematical review

Reviewed 2026-10-09. This is the fresh CRITIC-MATH stage, not the writer's check or a revision. Read `PROMPT.md` with the selected-band scope override and `CRITIC-MATH.md`, then independently solved every printed board and bound task. Drafts were not edited.

## Located correction

### Facilitator, page 3, two-BR-plus-R response proof

**Location:** `infinity-drafts/lowell-math-circle-year-2/source/week-83/guide/facilitator.tex`, section “Exact game reasoning and solution methods,” paragraph beginning “For the balance.”

**Quoted text:** “To make the argument tangible, children can enumerate legal first cuts and exhibit a reply leaving a zero position or a position their color wins. A response strategy must cover every opponent move; one successful play is evidence only.”

**Finding:** This is correct mathematics, but the paragraph does not supply the concrete exhaustive reply proof expressly required in the task handoff. The numerical equality is not a substitute for this requested adult solution. There are exactly two equivalent Blue openings and three Red openings in two equivalent types. The independent game-tree solver checks all of them.

**Smallest fix:** Add this paragraph to the adult solution; no student change is needed:

> If Blue starts, Blue must cut the base of one BR stalk. Red cuts the top R of the remaining BR, leaving B+R with Blue to move; Blue takes B and Red takes R. If Red starts by taking the separate R, Blue removes one whole BR; Red must take the top R of the remaining stalk and Blue then takes its B. If Red instead starts by cutting the top R of a stalk, Blue removes the other whole BR, leaving B+R with Red to move; Red takes R and Blue takes B. In each opening case the second player makes the last move. The two identical stalks make the listed cases exhaustive.

This is an adult solution-completeness issue, not a counterexample to the printed balance or a suggestion to print the strategy on student boards.

## Student packet: all selected bands check out

Grades 2–5 task pages 1–4 and auxiliary page 7 are mathematically correct. Optional Grades 4–5 pages 5–6 are mathematically correct. No K–1 packet is required or claimed. Every one of the seven actual PDF pages was independently rendered, viewed, and compared with the source declarations. No incorrect diagram, missing grounded segment, reversed stalk order, overlap hiding a rule, or illegible bound was located.

| Page / problem | Asked task | Independent result |
|---|---|---|
| 1 / Problem 1 | Play four boards with each starter; determine whether a fixed color can always win. | A=B: Blue wins either starter. B=R: Red wins either starter. C=B+R: second player wins. D=BB+R: Blue wins either starter. |
| 2 / Problem 2 | Find the second-player-win balances among three boards. | A=BR+R has value −1/2 and favors Red. B=2BR+R is zero and balances. C=3BR+R has value 1/2 and favors Blue. |
| 3 / Problem 3 | Find quarter balances and strategies for every other board. | A=BRR+RB has value −1/4 and favors Red. B=2BRR+RB is zero and balances. C=3BRR+RB has value 1/4 and favors Blue. Exhaustive legal-cut recursion checks both starters and all replies. |
| 4 / Problem 4 | Invent two different balanced boards, each containing a stalk of at least two segments. | Satisfiable, for example BR+RB and BB+RR. Each has value zero and is second-player-win by the independent tree check. Other solutions are allowed; this is not a finite enumeration request. |
| 5 / Problem 5 | Choose the earliest-born card satisfying each pair of strict bounds. | (0,3) chooses 1; (−1,1) chooses 0; (0,1) chooses 1/2; (1/2,1) chooses 3/4. The non-task visual (−2,2) correctly demonstrates 0. |
| 6 / Problem 6 | Invent two distinct bound pairs choosing the same card and a pair choosing a card younger than both bounds. | (−1,1) and (−2,2) both choose 0. (0,1) chooses day-2 card 1/2, later than days 0 and 1. All 15 supplied cards and their first birthdays agree with an independently generated day-0–3 dyadic catalog. |
| 7 / auxiliary | Reusable empty grounded board. | Correctly has a ground line and no numbered duplicate task or pre-revealed value. |

The worked cut on page 1 is the non-target stalk BRB: Red cuts its middle R, the upper B falls, and the base B remains. It is legal and consistent with one-stalk-per-turn semantics. Printed stalk strings are read bottom to top in this report. Actual PDF vector edges on pages 1–3 are 22 mm: 14, 15, and 24 colored segments respectively, including the worked visual on page 1.

For Problem 6, exhaustive checking of the 105 distinct ordered lower/upper pairs from the 15 supplied cards gives 91 with a unique earliest supplied answer and 14 with no card strictly between the bounds. Eight pairs choose a card later than both bounds. The student task asks children to find valid pairs, so the no-answer pairs do not make it incorrect. The guide's instruction to say “not in this catalog” for a missing answer is correct; for example (1/4,1/2) would first admit 3/8 on day 4, which is absent here.

## Facilitator mathematical claims

Apart from the located response-proof omission, the guide's theorem-first opening and ensuing mathematics check out:

- Normal-play rules, one-component moves, collapse above cuts, starter-dependent outcome classes, and finite termination agree with the game trees.
- B=1, R=−1, BR=1/2, BRR=1/4, RB=−1/2 follow directly from recursive cuts. In particular BRR's Red options are 1 and 1/2; its effective upper bound is 1/2, so the simplest allowed number is 1/4.
- A zero number game is a second-player win, not a draw. Positive/negative number games favor Blue/Red for either starter.
- Equality in arbitrary disjunctive-sum contexts is explicitly distinguished from finite selected-board evidence. The independent finite solver checks these boards; it does not establish the full context theorem or confuse game forms with their canonical values.
- The birthday catalog records first births correctly. The simplicity cuts are strict; {0|3}=1 is deliberately not midpoint 3/2, and {−1|1}=0 reuses an older number.
- The infinite-cut doorway is adult-only and does not claim an actual infinite construction was physically carried out. Ordinary ordinal queue concatenation's 1+ω=ω is kept distinct from commutative surreal addition's 1+ω=ω+1.
- The green-edge encore is correctly described as first-player-win star, not zero, and is absent from the core student tasks.

## Reproducible evidence and boundaries

`verify_math.py` uses only Python's standard library. It parses the actual diagram declarations and supplied cards, implements all legal cuts independently, solves both starting turns by minimax, and separately computes simplest rational values recursively without assuming board additivity. It checks 61 winner-state/turn entries and 65 numeric-cut states, all ten printed boards, both invention witnesses, all four cuts, all 15 cards, all 105 possible supplied bound pairs, and the three complete response paths. Run `python3 verify_math.py`; an optional first argument supplies another `students.tex` path for a later revision.

`verify_math_results.json` records the source digest, exact values, legal opening witnesses, bound-pair coverage and response paths. `math-render-checks.json` records the reviewed PDF digest, seven US Letter pages, actual 22 mm segment counts, and every-page visual inspection. Independent render images are in `math-renders/`.

No physical fit, magnetic adhesion, marker erasure, printer color legibility or classroom rehearsal was performed. These remain explicitly untested. This review does not certify age fit, priority of teaching examples, infinite game behavior, or Lean formalization. The guide's reference-pedagogy attribution was not re-audited against the private source book as part of this mathematical stage.
