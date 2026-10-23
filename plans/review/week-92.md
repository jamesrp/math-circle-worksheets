# Week 92: Fold-and-stretch predictions

**Verdict: keep.** No must: every answer and diagram is right, the problems reach a real theorem in a good order, and the guide is at the bar. The missing K–1 route and P3's answer-sized boards are shoulds.

Reviewed October 23, 2026 by Claude, with the math check in [week-92-math.md](week-92-math.md). Packets: week-92-students.pdf (W92-S-v2, 7 pp.; pp. 1–3 Grades 2–3, P1–P3; pp. 4–7 Grades 4–5, P4–P9); band slices 2–3: pp. 1–3, 4–5: pp. 1–2, 4–7. Adult guide: week-92-facilitator.pdf, 5 pp. Companions noticed but not reviewed: none. Status: unpiloted, physical rehearsal untested (README, QA.md).

## The mathematics

A marker on the continuous track [0, 16] moves to twice its distance from the nearer end: the tent map. Mirror pairs merge (P1), yet no band gets narrower: across 8 its width becomes twice the longer half, equal only when symmetric, and endpoint images miss the turn at 8 (P2, P4, P5). For any named n the band [0, 2/2ⁿ] stays in [0, 2] for n moves, but no band works forever (P6–P7). Each dyadic piece of width 16/2ⁿ fills the track after n moves, so every band with width eventually does (P8–P9). A mathematician would enjoy sensitive dependence made exact, with a quantifier swap at its centre.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Exact interval images, a width inequality with its equality case, the horizon 2/2ⁿ, the dyadic induction, with honest limits (singletons, the fixed point 32/3). |
| Problems | strong | P2: left half, right half (reversed), asymmetric crossing (ends give 10–12, truth 10–16), symmetric crossing (ends give 4, truth 4–16). P3: [1, 2] against the wider [7, 9], both four moves. Thin spots: P3's boards (fix 2); P8's fourteen records all end as the whole track. |
| Student pages | adequate | Spec header and footer, no slop or extra headings. Non-task visuals first: 13 → 3 → 6 (p. 1), the band 5–10 through 8 (p. 2), one ½ in both scales (p. 5). Faults: fixes 2, 3, 5–7. |
| Concreteness | adequate | Guide p. 2 launches everyone on the printed 13 → 6 with markers, ruler and map; a partner checks each move, and the map makes any band image readable. But bands are pencil shading, the strips are undefined (fix 8), and nothing folds ("No physical stretching of paper is required"). |
| Correctness | strong | math.md: all correct, with general proofs; one guide slip (fix 4). My exact recomputation of P1–P4, P6 and P8 agrees. |
| Adult guide | strong | Theorem-first p. 1 with assumptions, limits and band map; launch, route, full keys and proofs. Gaps: fixes 1, 4, 8, 10. |
| Age fit, K–1 | weak | No pages, by design. Guide p. 2 offers "an oral token-and-fold demonstration" it never describes. |
| Age fit, grades 2–3 | adequate | Doubling distances up to 8, gaps from 16, adult reading. The demands are the continuum, shown on p. 2, and a two-scale graph. Three pages (fix 3). |
| Age fit, grades 4–5 | strong | P4–P5 start from moving bands. P6 halves to 1/32 on an unmarked line; P8's 34 band moves split among three; P7 and P9 are late proofs for the organizer's table. |

## Keep

- p. 1: the V map (output left, nearer-end distance right) with the dashed 13 reading; P1's "Find every pair that meets after one move."
- p. 2: the 5–10 band with dots at 5, 8, 10 and both axis highlights; P2's four bands in order.
- P3's two bands; P4's [6, 10] and "Find two more starting bands …"; P5; p. 5's scale bridge and P6's unmarked 0–1 lines; P7; P8's pieces A–N with separate result tracks; P9's "Include bands whose ends lie between ticks".
- Guide: the p. 1 overview, the p. 2 launch and band demonstration, solutions 5, 6, 8, 9.

## Fix

1. **should**, K–1, guide p. 2: "an oral token-and-fold demonstration or a different familiar activity" names a demonstration it never describes. SCOPE.md authorizes leaving out K–1, so a should, as on Weeks 60 and 62. Fix: describe a route on a spare p. 1 track. Fold it at 8: which starts touch? Then hop whole-number starts, laying the nearer-end gap twice from 0: "Does every start get to 0? Which take the most moves?" (all do; odd starts take five). That K–1 can lay a gap of 7 twice is a prediction.
2. **should**, 2–3, p. 3, P3: each band has exactly four tracks, "After 1 move" to "After 4 moves", and both first fill on move 4. The board answers "How many moves does each need?" (math.md calls the count a fit) and spoils the surprise that the wider [7, 9] is no faster. Fix: six after-tracks per band, about 14 mm apart.
3. **should**, headers and `band-views/week-92/`: the 2–3 slice is three pages (spec: four or more), though P4–P5 need only P2's band work, and the 4–5 slice opens with two pages headed "Grades 2–3". Fix: head pp. 1–2 and 4 "Grades 2–5", add p. 4 to the 2–3 slice and menu, rebuild the views. That a quick 2–3 table runs out is a prediction.
4. **could**, guide p. 3, P1: doubling "preserves their difference" is false, it doubles it (math.md); write "keeps them different (it doubles the gap)", and "grows for three successive moves" → "four moves: 1, 2, 4, 8, 16".
5. **could**, p. 2: cut "One marker follows the rule from its unknown start; it is never placed at a fresh start."; no answer depends on it, and guide p. 1 tells the adult.
6. **could**, P4: cut "Is 12 the only possible next place?", which p. 2's example answers.
7. **could**, p. 4, P5: replace the lone grey rule with two Start/After track pairs.
8. **could**, guide p. 2: specify the "translucent strips" (a 5 cm tracing-paper strip per pair) or say pencil shading suffices.
9. **could**, week-92/README.md "Use the guide's exact duplicate-sheet instructions" and the source README's "duplicated cutting/card sheets": none exist; delete.
10. **could**, guide p. 2: the first route times only P1–P3; give the upper table's hour (P1 briefly, P2's crossing bands, P4–P5, P6 if ready).

## Overlaps

Atlas GA-10 (Geometry and Analysis pp. 33–36) uses the same tent map for periodic programs and cycle counts: same object, different theorems (guide p. 5). Week 51's ranges are the prerequisite; Weeks 93 and 46 contrast; Weeks 80 and 81 share the "every n, not forever" swap. None iterates interval images. No merge.

## App fit

B, size M; themes.md has no row for 92, so add one. Ruler strips (Week 51) already has bands, Break and Widen modes and two-pin certificates; add the tent move as a group there:

- **Break** (P2, P4): an endpoint-only claim ("every start from 6 to 11 lands in 10 to 12"). The child drags a marker inside the band and the app moves it; a landing outside breaks the claim. Can't: pin the lowest and highest landings.
- **Widest** (P6): a band from 0, window 0 to 2, three, four or six moves, on a zoomed 0–1 ruler; the app shows an escaping start while one exists, and the certificate is the right end landing exactly on 2.
- **Fill on move k** (P3): place a width-2 band so the whole track first becomes possible on move 3, then on move 4.

Pitfalls: no typed or predicted band ends, no band animation to watch as the task, a grid fine enough for 1/32, no "x of 8" counter on P1's pairs. P7–P9 stay on paper.

## Classroom evidence

None reported. README and QA.md: "Unpiloted; physical rehearsal untested." No use record or organizer report mentions Week 92; the app's decisions.md row says it waits on organizer review.
