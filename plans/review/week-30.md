# Week 30: Two-pan weight kits

**Verdict: keep.** The mathematics, problems and answers are right in every band, and nothing as printed leaves a child or adult stuck. The fixes are should and could items, led by the board count that gives away 2–3 Problem 4.

Reviewed October 5, 2026 by Claude. Packets: week-30-k-1.pdf (F30-K-v2, 5 pp.), week-30-grades-2-3.pdf (F30-23-v2, 5 pp.), week-30-grades-4-5.pdf (F30-45-v2, 5 pp.). Adult guide: week-30-facilitator.pdf (5 pp.). Companions noticed but not reviewed: week-30-bonus.pdf (W30-BON-v1, 4 pp.) and its guide. Status: unpiloted (October 4 revision; the organizer approved its scope, not its classroom use).

## The mathematics

Each weight goes beside the target, opposite it or off. The kit 1, 3, 9, … balances every target up to (3^m − 1)/2 in exactly one way, and no m weights balance more, even with gaps: the 3^m placements pair into positives and negatives around the all-off zero. Children find the step themselves: to a kit with total S, add 2S + 1, since heavier leaves a gap and lighter falls short. A mathematician would enjoy it. K–1 P4–P5, 2–3 P2–P6 and 4–5 P1–P7 carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Existence, uniqueness and a sharp bound; every band meets "can't", "every" and "best". |
| Problems | strong | Contrasting kits (1,2 / 1,3 / 1,4; third weight 8 / 9 / 10; 1,3,8 against 1,3,9), each a five-minute task, ordered from two weights to five. |
| Student pages | adequate | Clean headers, footers and rules, no slop. 2–3 P4 prints the answer count; K–1 P3 and 2–3 P3 lack a strip per kit. |
| Concreteness | adequate | The launch shows the shared action, and dealing only the current kit enforces one copy of each weight. Paper cards "stand for amounts" (guide p. 1), so balancing is checked by arithmetic alone. |
| Correctness | strong | math.md checked every answer, count and board; one dot on the K–1 "10" card touches the border. |
| Adult guide | strong | Theorem-first overview with hypotheses, band map, keys and proofs for all bands, cited theorem. Materials and timeline have gaps. |
| Age fit, K–1 | adequate | One- or two-sentence problems, totals to 6 until P5; P2's impossible boards and P3's tie are real mathematics. P3 wants two kits' results on one strip. |
| Age fit, grades 2–3 | adequate | Sums to 13, then 40; P5's counting argument is adult-led per the guide. P3 tracks 14 targets for three kits on ruled lines. |
| Age fit, grades 4–5 | strong | Uniqueness, the universal bound and the 121 construction, with the organizer at the table. |

## Keep

The four-sentence rules and the launch example. K–1 P2's boards for the impossible targets 4 and 5. K–1 P3's tie: 1, 4 and 1, 3 each balance four of 1–6, but only one has no gap. The unique answer {1, 3} in K–1 P4 and 4–5 P1. The open choice of a third weight (2–3 P2) before the 8 / 9 / 10 comparison (2–3 P3); reversed, P3 would answer P2. The duplicate-versus-unique contrast in 2–3 P4. The impossibility questions (2–3 P5, 4–5 P4) and the fourth and fifth weights. In the guide: the overview, the small-kit key, the off / opposite / beside hint, the 4–5 proofs, and dealing only the current kit.

## Fix

1. **should**, 2–3 p. 4, P4: two boards under "1, 3, 8" and one under "1, 3, 9" tell the child there are exactly two ways and one. Knowing you have them all is the problem; math.md calls this an observation, I rate it higher. Draw three boards under each kit with `pan(..., scale=.7)` and drop the ruled lines.
2. **should**, 4–5 p. 4, P5: "Can another kit balance more, even if there are gaps?" A child who chose 1, 2, 3 answers "yes, 1, 3, 9" and stops short of the bound the guide expects (13). Replace it with "What is the most any three-weight kit can balance, even with gaps? Explain why none can do better."
3. **should**, K–1 p. 3, P3: one 1–6 strip serves both kits, so a child cannot record two results to compare. Use two labeled strips, "1 and 4" and "1 and 3", as in 2–3 P1, and drop the ruled lines.
4. **should**, 2–3 p. 3, P3: only ruled lines under each kit, though a first miss means tracking up to 14 targets. Replace each kit's lines with `targets(range(1,15), y, 7)`.
5. **should**, guide p. 1, Materials: paper cards give no check that pans balance, the target has no object, no card or mat template is supplied, and a child who picks 5, 6, 7 or 11 (2–3 P2, 4–5 P1, P2, P5) has no card. The week's outline asked for unit bundles. List linking-cube sticks (or Week 29's rods) of 1, 2, 3, 4, 8, 9 and 10, a target stick in another colour, and a mat where each pan's sticks lie end to end in a row; equal lengths balance. Keep cards for 27, 81 and big targets, plus blanks. Untested; rehearse the fit.
6. **should**, 2–3 p. 2, P2: the boards print 5, 8 and 13; 5 and 13 are the targets that rule out 10 and 8, which is the guide's hint. Leave the target boxes blank (`blanks(p,['','',''],9)`).
7. **should**, bonus guide p. 1 (companion): "every surviving pair cannot be that kit" is false as written; use math.md's wording, "the three pairs left by the three possible removals cannot all be {1,3}".
8. **could**, K–1 p. 5, P5: the "10" card's tenth dot sits on the border; change the row step from .38 to .33 in `weights()`.
9. **could**, all bands p. 1: the launch example (target 3, kit 1 and 4) is a cell of K–1 P3 and 2–3 P1; use target 5 with weights 2 and 7, and drop the arrow that points at text.
10. **could**, 2–3 p. 2, P2: delete "Test your choice."; the goal already requires it.
11. **could**, guide p. 2: the 0–60 timeline and "trade … with another pair" assume an hour of work and two pairs per table; fit it to 35–40 minutes and the 4–5 trio.
12. **could**, bonus guide p. 2: reword the equal-cards question per math.md item 2.

## Overlaps

Week 29 (two-length builders) also builds targets from a kit, but with unlimited copies and addition only; its theorem is the Frobenius gap, and its rods could supply this week's weights. Week 6 (code breaking) uses the same counting move (k answers separate at most 2^k), which the bonus's search problems repeat. None reaches balanced ternary; no merge.

## App fit

Fit B, confirmed: a new mechanic in the odd-pebble balance's art. The child drags weights beside the target, opposite it or back to the tray, and the beam tips, giving the check the paper lacks. Solves: balance each target 1–N with a given kit; pick a third weight from a small tray so the kit covers 1–13, the app naming the first miss; find every balance of 4 with 1, 3, 8, declaring "done" with no visible count. Certificate for "best" at two weights: a 3 × 3 grid of all nine placements shows at most four positive targets. For "can't": a total too small, or the off / opposite / beside split. Pitfalls: free number entry invites guessing 1, 3, 9 by pattern; no predict-the-tip questions. Draw on K–1 P2–P5, 2–3 P1–P4 and P6, 4–5 P1–P2 and P6–P7, and the bonus's kits that survive losing a weight.

## Classroom evidence

None reported. The theme is unpiloted; physical fit, demonstrations and timing are untested (source README).
