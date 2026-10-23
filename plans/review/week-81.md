# Week 81: Buckets of Fish

**Verdict: keep.** No must. Every printed answer checks, the pages meet spec, and both theorems reach children through play. The fixes are a misworded guide sentence, a thin 4–5 rung before the termination question, the 4–5 route, and K–1, which has no route by design.

Reviewed October 17, 2026 by Claude, with math.md and card_appfit.py (new claims below). Packets: week-81-students.pdf (W81-S-draft-v1, 5 pp.: Grades 2–5 P1–P3 on pp. 1–4, with the board on p. 2 and cut cards on p. 3; Grades 4–5 P4–P5 on p. 5). Adult guide: week-81-facilitator.pdf (4 pp.). Companions noticed but not reviewed: the guide's p. 4 encore and return visit. Status: unpiloted. The organizer approved and promoted the packet on October 17 after its October 15 revision; that was review, not piloting. The card agrees with math.md's one finding and rates it a should.

## The mathematics

A move removes one counter and may refill only buckets to its left. The second player wins exactly when every bucket is even, whether refills are capped at one per bucket or not. A move from all-even always leaves an odd bucket. From anywhere else, take from the rightmost odd bucket and add one to each odd bucket on its left (P1–P3). Every play ends, because the rightmost bucket never refills, yet from (0, 1) a refill of M gives exactly M + 1 moves, so no bound holds (P4–P5). A mathematician would enjoy it: a one-line invariant in a game whose positions grow, and the gap between "every play is finite" and "every play is shorter than some N".

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Two real theorems, reached by playing. |
| Problems | adequate | P1–P3 give 4, 16 and 6 contrasting starts and move from play to sorting to a rule. P4 is one choice; P5 has one start (fix 2). |
| Student pages | strong | Spec header and footer, rules once, worked visuals before first use (pp. 1, 5), no hints or slop, large board, cut cards, answer boxes. |
| Concreteness | adequate | Counters on 56 × 139 mm buckets, plus Supply and Removed; cards for the sort; a three-minute whole-group launch (guide p. 2). Only the partner enforces "left only, one each". |
| Correctness | strong | Everything printed checks (math.md). One overview sentence misstates the repair move (fix 1). |
| Adult guide | adequate | Theorem-first overview with hypotheses; prerequisites, launch, route, keys, termination without notation, encore. Gaps: fixes 1, 3, 4, 7. |
| Age fit, K–1 | weak | No route, by design. |
| Age fit, grades 2–3 | strong | An adult reads the rule; at most 8 counters per bucket (math.md); the board holds the state; the rule (P3) comes last. |
| Age fit, grades 4–5 | adequate | P5's argument suits this table and the organizer, but P4 settles fast, P5 lacks a two-bucket case, and the route is unclear. |

## Keep

- p. 1: the three-sentence rule, with the cap stated once. The (1, 1, 2) → (1, 1, 1) → (2, 2, 1) visual rules out both misreadings (math.md).
- p. 2: the board, with Supply and Removed outside the buckets.
- P1's (0, 0, 1), won only by refilling nothing. P2's sixteen cards (every pair 0–3), where sorting is the mathematics. P3's open rule question. Its (3, 3, 1) is won only by refilling two buckets, and two of its starts have no winning move.
- p. 5: the cap lifted in plain words, the 12-to-11 visual, P4's 10, 30, 100 ladder, and P5's "Can you agree on moves that keep the game going forever?"
- Guide: "Finite refills and a fixed finite number of buckets are essential", the P1–P3 keys, and the warning not to apply the cap in P4.

## Fix

1. **should**, guide p. 1: "add 0 or 1 to each earlier odd bucket to restore all-even." Adding 0 leaves an odd bucket odd: from (1, 0, 1) it gives (1, 0, 0) (math.md item 1). Page 3 has it right. Fix: "add 1 to each earlier odd bucket (0 to each earlier even one)".
2. **should**, 4–5, p. 5. After P4's first move every move is forced (math.md), so the refill is the only choice. P5 then asks why every game ends, from one three-bucket start. No two-bucket game lets children try to go forever and fail. Fix: P5 says "Start from each picture." Show (0, 3), drawn like P4's picture, beside (1, 1, 1).
3. **should**, 4–5, guide pp. 1–2. Page 1's "termination/unbounded length, then parity" reverses the page order, and p. 2 never says whether this table plays P1–P2 first. Fix: "Grades 4–5: ten minutes of P1 and some P2 cards to learn the move, then P4–P5; P3 for a pair that finishes." Make p. 1 match.
4. **should**, K–1: no route. A should, as on the Week 79 card, because the 79–84 index says "No K–1 edition is forced." Fix, in the guide: after the launch, play P2's nine cards with at most two per bucket. Read the rule as "Take one. You may put one in bucket 1." Then sort the cards into two piles. That K–1 manages this is a prediction.
5. **could**, p. 1: "strictly to its left" and "each earlier bucket" name one idea two ways.
6. **could**, P5: "explain why even huge finite refills cannot prevent it" presumes the answer.
7. **could**, guide p. 2: "count card" wording survived the October 15 removal of the card page.
8. **could**: "draft" in the student footer id and the guide header.
9. **could**, guide p. 2: the launch does not show the one-per-bucket cap.
10. **could**, P3 repeats P1's (2, 2, 2); (2, 0, 2) would add a case.
11. **could**, return visit: with a cap of K the longest game is Σ a_i (K + 1)^i, which is 7 from (1, 1, 1) with a cap of one (card_appfit.py).

October 23, 2026: shoulds 1–4 and coulds 5–11 fixed in v2 (W81-S-v2), after the organizer's October 17 approval; the K–1 route is a guide paragraph on the existing cards. Checks in the package's `check_card_fixes.py`.

**Critic follow-up, October 23, 2026 (W81-S-v3, W81-FAC-v2):** an independent critic's two shoulds and a could are made. The K–1 rule read aloud is now "Take one. If you took it from bucket 2, you may put one in bucket 1." (the old "You may put one in bucket 1." allowed taking from bucket 1 and putting it back, so a game need not end); `editable/check_card_fixes.py` solves the nine cards under the new rule and the key stands. The guide's footer reads W81-FAC-v2. Problem 5's (0, 3) is drawn like (1, 1, 1). The band-view menu and a K–1 slice list pages 2–3. Not re-approved. Unpiloted.

## Overlaps

Weeks 7 and 8 share the game frame (second-player starts by working back) but not this invariant. Week 11 shares termination by a decreasing measure. Week 79's card names the same quantifier swap. No merge; Weeks 79–81 make a return sequence.

## App fit

I propose A: a group inside Pebble Duel (the base `nim` family, beside Menus and Star race), not a new family. themes.md has no row; it should read: | 81 | Buckets of Fish | Take one counter and refill only buckets to its left; find who wins and the winning move; make games long; ask whether one can go on forever | The second player wins exactly when every bucket is even, capped or not; every play ends since the rightmost bucket never refills, yet from (0, 1) a refill of M gives M + 1 moves | No | A | Pebble Duel group: tap a bucket to take one, tap left buckets to refill; duel, who starts, mark every second-player card. Termination stays on paper | S |

The capped game is a real on-screen solve, and the app beats paper here: its controls can offer refills only to the left, one each, which paper leaves to the partner. The substance is new to the family. Positions grow, yet the invariant is parity in each bucket. Without refills (1, 1) is a second-player start; with them it is a first-player start (card_appfit.py).

Draw on:
- **P1 and P3: duels.** Include (0, 0, 1), won by refilling nothing, and (3, 3, 1).
- **Who-starts rounds, three wins in a row.** Draw half the starts all-even; only 7 of the 63 nonempty three-bucket starts up to 3 are.
- **P2: Every start.** Use the 15 nonempty two-bucket cards. The answer is (0, 2), (2, 0) and (2, 2). That's all judges the whole set, and the app plays out a wrong mark, going first.
- **Every reply.** From (2, 2), which has three first moves.
- **Hard: the encore.** Take 1–3 and refill 0–3; multiples of four lose. The rule fails with refills below 3 (math.md).

Pitfalls:
- No title, How to play line or first hint says "even".
- A losing opponent leaves the fewest winning replies rather than moving at random.
- Undo treats a take and its refills as one move.
- The who-starts choice is final.
- Once found, the rule repeats, like the rook race's diagonal, so keep the group to six to eight puzzles.

P4–P5 do not port. "Last 100 moves" is one number typed into bucket 1. "Can a game go on forever?" is a claim about every play, which no finite board checks; that is Week 79's reason. A capped longest-game puzzle is no better: always refilling fully reaches the maximum, so the solve repeats, and "best" has no certificate to tap. Recommendation: port P1–P3 and the encore as a Pebble Duel group, and keep termination and the talk about infinity on paper.

**Decision, October 17, 2026.** Port the capped game (Problems 1–3) and the guide's take-1-to-3 encore as a group inside Pebble Duel, beside Menus and Star race. A move takes one counter from a bucket and refills buckets to its left, at most one each, and the controls offer only legal refills. The group has duels against a perfect opponent, who-starts rounds where the choice is final, every reply from (2, 2), and an Every start sort of the two-bucket cards judged as a whole with That's all. No title, How to play line or first hint says "even", and Undo takes back a take with its refills. Problems 4–5 stay on paper: the longest-game question comes down to one number, and whether a game can go on forever is a claim about every play that no finite board checks, Week 79's reason. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The organizer approved the packet on October 17 after reading its October 15 revision. No session has used it. Source README: "All activities are unpiloted; physical fit, actual-size printing, timing and classroom procedures have not been rehearsed."
