# Week 95: Count the unseen

**Verdict: keep.** No must: every answer and proof checks, every problem has its objects and room, and the guide opens with the theorems. The fixes are the live game's set-up, a 4–5 problem that repeats an earlier one, no K–1 plan, and wording.

Reviewed October 23, 2026 by Claude, with math.md. Packets: week-95-grades-2-3.pdf (W95-23-v1, 4 pp.), week-95-grades-4-5.pdf (W95-45-v1, 4 pp.). Adult guide: week-95-facilitator.pdf (W95-F-v1, 5 pp.). Companions noticed but not reviewed: none. Status: unpiloted, organizer review pending; marks, mixing, resets and timing unrehearsed. No K–1 packet, by design.

## The mathematics

Mark a first catch of M, return it, catch n, and find R marked. Exactly M + n − R objects have been seen, so N ≥ M + n − R, sharply, with no upper bound. In a bag of N the overlap takes every value from max(0, M + n − N) to min(M, n), so big enough catches force a mark. Under uniform sampling E(R) = Mn/N, which suggests the guess Mn/R; it varies, is biased and fails at R = 0. With M + n fixed, equal catches maximize the expected overlap. A mathematician would enjoy the line between what a record proves and what a model suggests. 2–3 P2, P3, P6 and P7 carry the set facts, P4 the variability; 4–5 P2–P4 set bound against estimate, P6–P7 the design.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A sharp bound with no upper bound, a forced overlap, the expectation and the balancing theorem, each with its limits. |
| Problems | adequate | Experiment, bounds, estimate, variability, design, model failure, in order. 4–5 P5 repeats P2 (fix 2). |
| Student pages | adequate | Spec header, footer and numbering; a complete non-task demo before first use. Nine sentences of opening rules and small wording faults (fixes 4–9). |
| Concreteness | adequate | The bag hides the total, blind draws supply chance, letters make "the same object" physical; guide p. 2 launches on the demo. Letters undercut P1 (fix 1); erasable dots are untested. |
| Correctness | strong | math.md: 58 checks pass, no wrong answer, three minor findings. I agree, and rechecked 2–3 P4's per-round choices and the 1.76 ratio. |
| Adult guide | strong | Theorem-first p. 1 with limits and band map; every problem keyed, with held hints; kits, roles, route. Gaps: fixes 1, 3. |
| Age fit, K–1 | weak | "the K–1 table needs its own separately selected session activity" (guide p. 2), unnamed. |
| Age fit, grades 2–3 | adequate | Counting within 20 and matching letters; an adult reads the rules. A P1 round has many steps, carried by roles. P4 has no single answer, which the guide handles. |
| Age fit, grades 4–5 | strong | P3 needs equivalent fractions and supplies a worked bridge; P6–P8 come late, with the organizer. |

## Keep

- The p. 1 demo: the same A–F through catch, mark, return, mix and recapture, C circled as the overlap.
- Guide p. 2's "Keep sampling and existence separate".
- 2–3 P2 then P3, repeated against disjoint letters, with "Which of these totals are possible: 6, 7, 8, 12, 20?" and "Is there a largest possible bag if you have as many cards as you want?"
- 2–3 P4's six printed rounds, with no total marked right; P6's bags of 6, 8 and 12; P7's impossible-record puzzle.
- 4–5 P3's bridge (A•BC kept, D•EF added, guess 6) and ten-object counterexample; P4's five records that one bag of 18 fits; P8's letters-against-dots test.

## Fix

1. **should**, both bands p. 1, P1; guide p. 2. Kits carry "Permanent small identities A–X", and nothing says which objects the keeper hides. If they are the run A, B, C, …, the highest letter caught equals N with probability 0.74–0.98 over three rounds (math.md item 1); even shuffled, distinct letters across rounds bound N without the overlap. And the keeper, drawer and checker roles meet pairs at the 2–3 table: the keeper knows N, and the route allows one series, so two of four children never guess. Add to guide p. 2: "For Problem 1 the adult is the keeper. Fill each bag from the shuffled kit without showing the count, so every child draws and guesses. Distinct letters seen are also a correct lower bound; welcome that reasoning."
2. **should**, 4–5 p. 3, P5. "Does that rule out every finite bag? Build two different finite bags that could give this record." is P2's record B again, and "What would you change…" has the quick answer "catch more". The 4–5 band never meets the forced overlap of 2–3 P6. Replace the last three sentences with "The keeper says the bag holds at most 20. Which catch sizes make an overlap of 0 impossible? Explain." Key for guide p. 4: catches totalling 21 or more, each at most 12 to fit every allowed bag (12 + 9, 11 + 10).
3. **should**, K–1, guide p. 2. As on the Week 87 card, name the K–1 activity: Week 42's K–1 packet uses the same bags and counters, or an adult-led small 2–3 P6 (bag of 5, mark 3, catch 3: can the catch miss every dot?). That K–1 can do this is a prediction.
4. **could**, both p. 1: "use distinct objects in each catch" can read as "no shared objects" (math.md item 2); write "no object appears twice in one catch", also on guide p. 2.
5. **could**, both p. 1 demo: "catch 2" labels the arrow into "First catch" (math.md item 3); write "catch 2 objects" or drop it.
6. **could**, both p. 1 demo: "First catch: A, C" and "Second catch: C, D, F" head boxes holding the bag; head the boxes "Bag" and the rows beneath "Catch".
7. **could**, 4–5 p. 4, P6: the printed average is P3's rule turned round; ask children to explain it instead.
8. **could**, 4–5 p. 3, P4: cut "The fraction-matching rule gives these guesses." and "Each round begins again with unmarked objects".
9. **could**, 4–5 p. 2, P3: cut "Make a different possible bag to test your answer."; P2's bag of 10 already answers it.
10. **could**, guide p. 3, 2–3 P4: add the held hint "Make an 8-bag and a 16-bag and play a few rounds of each."
11. **could**, 2–3 p. 4, P6: centre the bag totals in their cells.
12. **could**, both p. 1: phrase the rules as actions, keeping every assumption the organizer asked for (outline, October 17).

Fixed October 23, 2026, after converting the week to problem files: shoulds 1–3 and coulds 4, 5 and 8–11 (Problem 5 key and letter leak checked in `source/week-95/review/check_card_fixes_2026_10_23.py`); coulds 6, 7 and 12 deferred.

## Overlaps

Week 42 draws from the same bags for fairness; Week 45 gets an exact chance from a clue; Week 94 recovers a hidden offset exactly. Week 51's bonus holds the fixed-sum product behind P6–P7. No other theme counts an unseen population. No merge.

## App fit

Not in themes.md. I propose Fit B, size M.

- **Arrange catches.** Given N lettered counters and catch sizes M and n, tap objects into each catch to hit a target overlap, or claim Can't. Certificate: only N − M objects are unmarked, so a catch of n holds at least n − (N − M) dots.
- **Every overlap.** Mark a bag's possible overlaps and declare done, with no visible count (2–3 P6).
- **Where the average comes from.** Sort all 20 catches of 3 from A–F, A and C marked, into overlap bins (4, 12, 4; mean 1 = 2 × 3 ÷ 6), on the list-and-sort engine of Weeks 24 and 42–45.
- **Pitfalls.** Guessing the total is predict-an-outcome, right only by luck; keep random catches to a playground. A budget split with the formula shown is a dozen guessable choices.

Draw on 2–3 P2, P3, P5–P7 and 4–5 P2–P4 (one bag fitting every record).

## Classroom evidence

None reported. Not yet taught.
