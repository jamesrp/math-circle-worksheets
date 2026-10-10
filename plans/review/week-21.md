# Week 21: Shortest reflected paths

**Verdict: keep.** No must: every answer checks, every board fits at true scale, and the pages are clean. The should items are a thin Grades 2–3 Problem 7 and four guide repairs, chief among them that string cannot find the best contact; only the fold can.

Reviewed October 10, 2026 by Claude, with the math check in [week-21-math.md](week-21-math.md); I agree with all of it and rate its one finding (p. 12 labels) a should. Packets: `week-21-k-1.pdf` (W21-K-v2), `week-21-grades-2-3.pdf` (W21-23-v2), `week-21-grades-4-5.pdf` (W21-45-v2), 7 pp. each, P1–P7. Adult guide: `week-21-facilitator.pdf` (19 pp.). Companions noticed but not reviewed: the bonus (W21-BON-v1) and its guide. Status: unpiloted (source README, guide footers); the October 4 revision changed only the guide.

## The mathematics

For A and B strictly on one side of a line, reflect B to B′. Every route A–M–B is as long as A–M–B′, hence at least AB′, with equality only where AB′ crosses the line: one best contact, unique, proved against routes nobody drew. The boards reach its consequences: mirrored finishes tie (K–1 P3, older P2); starts with a given best contact form a ray (K–1 P7, older P5); equal minima and shared contacts are independent (2–3 P6, 4–5 P4); fewer competitors cannot win (4–5 P6); no two contacts tie (4–5 P7). This is Heron's problem with its equality case and inverse, which a mathematician would enjoy; it is one theorem, and the bonus extends it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Bound, unique equality case, inverse ray, legality versus optimality, each on a board. |
| Problems | strong | Older bands go from a comparison whose 1.0 cm gap survives string error (P1) to the tie that is the proof's key step (P2) to the proof (P3); later boards each add a question. Thin: 2–3 P7 (fix 1). |
| Student pages | strong | Spec header and footer, rules once, one problem per page, 16.8 × 18.2 cm true-scale boards with room for every B′. No hints or narration; "Explain" only where a claim needs a reason. |
| Concreteness | adequate | Taut string on the printed line enforces the rules; the launch (guide p. 2) shows a legal bend, an illegal slide and pinch-and-compare. But string cannot locate the best contact (fix 2), so every "shortest" rests on the fold, a held hint; two strings per table are too few for pairs (fix 3). |
| Correctness | strong | No error in any band or key (math check); I re-derived the ten optima by brute force. Fix 5 is a label. |
| Adult guide | adequate | Theorem-first overview with hypotheses, the restricted-segment limit and a band map; every key; staged hints. Fixes 2–5. |
| Age fit, K–1 | adequate | No reading or arithmetic. P1–P3 and P5's comparison are string-and-fold work for a pair; P4, P6 and P7 need the fold and a straightedge, which the parent volunteer must bring in (prediction). |
| Age fit, grades 2–3 | strong | Short sentences, a ruler, a fold. P3's explanation is the proof; P6's exact tie needs matched right triangles (guide p. 11), late in the packet. |
| Age fit, grades 4–5 | strong | Every-contact proofs, the locus and uniqueness, each checkable with fold and straightedge, with the organizer at the table. |

## Keep

- Every band: the p. 1 route rules; full-size boards, one per page.
- 2–3 and 4–5: the P1 → P2 → P3 order; on P1, C is nearer A but needs 1.0 cm more string.
- K–1: P1's symmetric equal pair; P2's guesses, 0.71 and 1.25 cm over the best, so string can beat them; P3; P7.
- 2–3 P6 (equal minima, contacts 8 and 6.2) against 4–5 P4 (one contact, minima 16.14 and 15); 4–5 P5–P7.
- Guide: the overview, a launch that withholds reflection, the held hints, p. 3's "After the fold, every try still uses the same string. This one is straight.", and p. 13's caution against "use the nearest endpoint".

## Fix

1. **should**, 2–3 p. 7, P7: "In which cases is your shortest route still allowed? Explain." Once the route is drawn, this is reading whether its contact lies between two letters; why it stays shortest (fewer competitors cannot win) is asked only in 4–5. Fix: the 4–5 wording, "In which cases does the same route still give a shortest allowed route? Explain."
2. **should**, guide p. 7 ("Common mistake") and p. 1 ("Physical model"): the length is flat near the optimum. On every board a contact 1 cm from M* costs about 1 mm, and the contacts within 2 mm of the best span 2.7–4 cm (my check). K–1 P4's midpoint guess is 2.2 mm longer than the best, so an adult cannot show the "common mistake" with string. Fix, one sentence: "String settles differences of 5 mm or more (P2's guesses, P5's comparison), but any contact within about 1.5 cm of the best looks as good; then move to the fold."
3. **should**, guide p. 1: "Preparation for ten children … roughly 3 / 4 / 3 … two 60 cm non-stretch strings". The group is eleven at 4 / 4 / 3 (`context.md`), and comparing two routes needs two strings per pair (p. 4: "Two separate string pieces"). Fix: eleven children at 4 / 4 / 3; four strings per table; 77 pages per full set.
4. **should**, guide p. 1 and keys pp. 4–14: coordinates run "from the lower-left corner of the source working region, not the paper edge", a corner nobody can see, so an adult cannot check a child's contact with a ruler. Fix: also give each contact from the left (or bottom) end mark, x − 0.6: K–1 P4 5.7 cm; the restricted board 5.9 cm, C–D 3.9–7.6 cm.
5. **should**, guide p. 12 diagram: "C" sits above A's dot and "D′" between D′ and B′ (math check 1), so a reader can take the black A–B route for C's. Fix: in `facilitator-src/build_guide.py` line 214, drop 'C' from the `dx=-16` rule; put D′'s label below-left of its dot.
6. **could**, guide p. 2: "use a spare board" names none; say "a line and two dots on a blank sheet".
7. **could**, guide p. 2 timing: allow the five-minute run before the launch and shorten the 48–60 share.
8. **could**, guide: older explanations can go on a blank sheet or be told aloud, since B′ uses the space below the line.
9. **could**, guide pp. 1, 16–17: move production and rebuild notes to the source README; number the route update "18 / 18".

## Overlaps

Week 9 (bouncing paths) and Week 71 (billiard words) unfold reflections into straight lines but ask where a path goes, not which route is shortest. Weeks 41, 61 and 64 share only unfolding or the word "shortest". Only Week 21 has the optimality theorem, its uniqueness and its inverse ray. No merge.

## App fit

Change C to B, size M, as a group in Mirror Couriers beside Week 71's aiming group (wave 8). Dots and every best contact sit on grid points. The child taps a contact and claims "shortest"; the certificate is the fold, which flips B's leg across the river and shows the route straight or bent. Puzzles:

- Beat two drawn routes (K–1 P2); which finish needs less rope (2–3 P1).
- Tap every grid start whose best contact is P, then "That's all" (K–1 P7, 4–5 P5).
- Place a finish whose best route ties A–B's, or shares its contact (2–3 P6, 4–5 P4).
- Windows (4–5 P6); for Hard, two walls in a chosen order and a rectangle with a tie (bonus P1–P5).

The tie board (K–1 P3) suits a playground: drag the contact and both routes change together. Pitfalls: a live length readout (sliding to a minimum); length tolerances, since 1 mm accepts contacts across 2–3 cm; multiple-choice "predict the contact"; a fold the app makes before the child asks.

**Decision, October 10, 2026.** Port, in Wave 8, as a group in Mirror Couriers beside Week 71's aiming group: grid-point dots and contacts, the child taps a contact and claims "shortest", and the fold is the certificate. No live length readout and no length tolerance. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported; the source README, guide footers and themes.md mark it unpiloted. String handling, folding accuracy and K–1's reach to the fold are untested, so the age-fit notes are predictions.
