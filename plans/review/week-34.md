# Week 34: Hidden turns

**Verdict: keep.** No must. Every band reaches a real theorem with a surprise, that two kinds fail on 3 to 5 spots and succeed from 6, using counters and a tracing copy, and the math check found no wrong answer. The fixes are a launch figure without a flip, one goal phrased three ways, an unstated way to make the copy, and no odd ring for 4–5 P5.

Reviewed October 5, 2026 by Claude, with the math check in [week-34-math.md](week-34-math.md); I agree with its three findings. Spot checks: `card_checks.py` in [checks/week-34/](checks/week-34/). Packets: week-34-k-1.pdf (W34-k-1-v2, 5 pp., P1–6), week-34-grades-2-3.pdf (W34-grades-2-3-v2, 5 pp., P1–5), week-34-grades-4-5.pdf (W34-grades-4-5-v2, 5 pp., P1–5). Adult guide: week-34-facilitator.pdf (6 pp.). Companions noticed but not reviewed: week-34-bonus.pdf (W34-BON-v1) and its guide; the math check's items 1–2 are there, chiefly an undefined "change" in P3–P4 that alters the minima. Status: unpiloted (source README; guide footers). The organizer approved the October 4 revision's scope, not classroom use.

## The mathematics

A pattern colours the n spots of a regular ring; it is distinguishing when no turn or flip but the identity matches it. With two kinds on 3 to 5 spots, one kind has at most two spots and a flip keeps them, so three kinds are needed. From six spots, marking 0, 1, 3 gives gaps 1, 2, n − 3, all different, so two suffice; the smaller kind always needs three spots. A mathematician would enjoy this distinguishing number of a cycle (Albertson–Collins). K–1 P2, P4, P5, 2–3 P1–P4 and 4–5 P1–P4 carry the 3, 3, 3, then 2; 2–3 P5 and 4–5 P5 carry the minority bound and the construction for every n.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | An exact optimum, a provable lower bound, a construction for every n ≥ 6. |
| Problems | adequate | The order carries the development in every band. The three-ring problems are short; older P1–P3 ask one question at three sizes; 4–5 P5 has one test ring (fix 4). |
| Student pages | adequate | Correct header and footer, one plain problem per page, 28 mm spots on 140 mm rings, no slop. No flip in the figure; three goal phrases (fixes 1, 3). |
| Concreteness | adequate | Counters, a copy whose traced circles force legal positions, a partner tester, one launch (guide p. 2). Making the copy is never shown (fix 2). |
| Correctness | strong | The math check confirms every key, witness and proof. One key omission (fix 5). |
| Adult guide | adequate | Theorem-first overview with limits, keys for all 16 problems, child-sized arguments, proofs (p. 5), held hints. Fixes 2, 5, 10. |
| Age fit, K–1 | adequate | Short tasks, possible/impossible and fewest questions, the older bands' ideas. Prediction: 15 motions per eight-ring check (P6) need adult bookkeeping; "hide" is opaque on one hearing. |
| Age fit, grades 2–3 | strong | Little reading, no arithmetic; explanation after three rings (P3); the minority question late. |
| Age fit, grades 4–5 | strong | Small cases, a unified explanation (P3), then a proof for every n (P5) at the organizer's table. |

## Keep

- The 3, 3, 3, then 2 arc in every band. The overlay: turning and turning over one copy reaches all 2n − 1 motions; traced circles rule out half-way positions; the partner tests.
- The p. 1 non-task four-ring with a match and a near miss.
- K–1 P3's fragile and robust edits, K–1 P6, 2–3 P5's minority minimum, 4–5 P3's one explanation for three sizes, 4–5 P5.
- Guide p. 1's overview and limits; p. 3's "'no matching turn' is not enough" and "Do not give the 0, 1, 3 construction before exploration has a chance to work"; p. 5's gap proofs.

## Fix

1. **should**, all bands p. 1, figure and rules. The figure shows two turns and no flip, and the rules say "turn over" where every problem says "flip". Yet on 3- to 5-rings 48 of 50 mixed two-kind patterns have no matching turn (`card_checks.py`; only the alternating four-ring has one), so only flips defeat two kinds. A table that tests turns alone finds no match in K–1 P1 and answers "two" in K–1 P2, P4 and older P1–P3. Add a flip panel on the same four-ring with its axis drawn; write "Turn or flip (turn over) its tracing copy."
2. **should**, guide p. 2, materials and launch. Nothing says how to copy a counter pattern, what mark stands for each kind, or that each new or changed pattern needs a fresh copy (K–1 P1 and P3 ask for many). The launch uses a copy the adult prepared. Make one in the launch: lay paper on the ring, trace the spot circles, mark each with its counter's colour. Supply coloured pencils and about ten sheets per pair. Prediction: sliding paper over loose counters may move them; lift the copy and set it down.
3. **should**, K–1 pp. 2–5 and older pp. 1–5, the goal. K–1 says "allow a matching turn or flip" (P3), "no turn or flip can hide" (P2, P5, P6) and "stop every turn and flip" (P4); the older bands say "stop". Only "match" is shown, in the figure, and "Neighbors may match" (2–3, 4–5 P1) uses it for same-kind neighbours. Write "a pattern that no turn or flip can match" throughout and "Neighbors may be the same kind" once in the rules. The hiding story stays in the launch question.
4. **should**, 4–5 p. 5, P5: "on any ring with at least six spots? Test your idea on this eight-ring". The construction is tested only on even rings (6, 8); on odd rings every flip axis passes through exactly one spot. Guide p. 4 mentions "trying sizes 6, 7 and 8", but no seven-ring is printed. Add a seven- and a nine-ring as extra workspace (AABABBB and AABABBBBB work; `card_checks.py`).
5. **should**, guide p. 3, K–1 P6 key (math check item 3). Swapping kinds (BBABAAAA) or using another pair cannot match under the fixed-kind rule, and the key is silent. Accept it, then ask for a second arrangement with the same kinds and counts.
6. **could**, K–1 P1: give it a goal, "Can you make one your partner cannot match?"
7. **could**, 2–3 P1: drop "Use up to three kinds"; the kit says it and it bounds the answer.
8. **could**, p. 1 rules: "the direction of a symbol does not" is moot with coloured copies (fix 2).
9. **could**, p. 1 figure: the arrows chain start → turn 2 → turn 1; draw both from start.
10. **could**, guide p. 2: "For ten children" (context.md has eleven); the hour lacks the opening run and has an eleven-minute share.
11. **could**, guide p. 6 repeats p. 2's routes in another header style.

## Overlaps

Week 33 (prime-length necklaces) uses the same counter rings, face up and turns only; its "n distinct readouts" is this week's "no turn matches", and the encore's d | n flip count echoes its period theorem. Teach 33, then 34. Week 37 (mirror twins) asks the chirality question on tetrahedra. No other theme has the distinguishing number; no merge.

## App fit

B, size S, as the row says; a short set, which the encore can lengthen.

- **Build.** Tap spots to cycle at most k kinds. The app tests all 2n − 1 motions; on failure a ghost copy lands on the pattern by the matching motion.
- **Seek.** The child turns and flips the ghost of the app's pattern to find its one match (K–1 P1's partner role): clicking around, not predicting.
- **Can't.** For two kinds on 3 to 5 spots, or two or fewer of one kind, the child declares "impossible"; the certificate is the flip through the lone spot or between the pair.

Pitfalls: random two-kind rings are distinguishing 19% of the time at 6 spots, 38% at 8 and 74% at 12 (`card_checks.py`), so tapping until green works on big rings. Put the difficulty in fewest kinds, the minority of three, two patterns that cannot match each other, and the encore's fewest repairs, where each cycle of the motion lights up and must become one kind. The engine needs flips, unlike 33's, and no identity; the child, not an animation, moves the copy. Draw on K–1 P1, P2, P4, P6, 2–3 P1–P5, 4–5 P5 as a 6-to-12 ladder, and encore P1–P4.

## Classroom evidence

None reported. Unpiloted; overlay handling, counter fit on 28 mm spots and timing are untested (guide p. 1; source README).
