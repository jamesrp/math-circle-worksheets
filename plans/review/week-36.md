# Week 36: Making threes

**Verdict: keep.** No must. Every answer checks, the pages are clean, and every band reaches unique completion, the four splits and the four-tile maximum with real tiles. The fixes are guide repairs and two 4–5 page details.

Reviewed October 10, 2026 by Claude, with the math check in [week-36-math.md](week-36-math.md); I agree with it and rate its one finding a could. My spot checks: `card_checks.py`. Packets: week-36-k-1.pdf (W36-k-1-v2, 4 pp., Problems 1–4), week-36-grades-2-3.pdf (W36-grades-2-3-v2, 4 pp., Problems 1–5), week-36-grades-4-5.pdf (W36-grades-4-5-v2, 5 pp., Problems 1–5). Adult guide: week-36-facilitator.pdf (6 pp.; p. 6 is the October 4 route note). Companions noticed but not reviewed: week-36-bonus.pdf (W36-BONUS-v1, 3 pp.) and its guide. Status: unpiloted (source README, guide footers); readiness check, tile handling and timing untested.

## The mathematics

The nine tiles are the plane over the integers mod 3; the allowed threes are its 12 lines. Two tiles have exactly one completion, so threes share at most one tile, four pass through each tile, and the twelve fall into four families of disjoint threes, the only four splits. At most 4 tiles avoid a three (five tiles have ten pairs, completed among four leftover tiles at most two each), and every legal three extends in exactly three ways, so maximal equals maximum and the adding game always lasts four moves. A mathematician would enjoy it: the smallest cap set, with proofs children can act out. Every band meets completion, splits, the cap and threes through a tile in P1–P4; 2–3 P5 and 4–5 P5 carry the forced length.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Incidence in a finite plane, a counting proof of the cap bound, maximal = maximum, limits stated (guide p. 1). |
| Problems | strong | Each is a search with a definite answer: four contrasting pairs, every split, the most tiles, all threes through a tile, a game whose length can't change. Completion opens every band; the game or the stuck question closes 2–3 and 4–5. |
| Student pages | strong | Header, footer, rules once, a worked check before first use, 60 mm mats for tiles, 22 mm record boards, no do-not-list items. Fixes 3, 4. |
| Concreteness | adequate | Real tiles; one launch bends a valid three off a line (guide p. 2). A partner checks P1 and the 2–3 game; elsewhere the rule is checked by eye. No tile sheet (fix 1). |
| Correctness | strong | All 370 math-check tests pass; no error on a student page or in the base guide. |
| Adult guide | strong | Theorem-first overview with assumptions, limits and band map; keys for every problem; the dish proof; sources with sections. Fixes 1, 2, 5. |
| Age fit, K–1 | adequate | No reading or arithmetic, short tasks, the same four ideas as older bands. The demand is judging two attributes at once; the guide gates the packet on an untried check (fix 5). Checking a five-tile attempt is adult work. |
| Age fit, grades 2–3 | strong | Short sentences, no arithmetic, explanation only where it is the point (P4); the opponent enforces P5. |
| Age fit, grades 4–5 | strong | Five proofs, each after concrete work, with the organizer at the table. |

## Keep

- Page 1 in every band: the five-sentence rule, then an allowed three bent off a line with an arrow to its completing tile, and a near miss, each with shape and fill rows ending "all different" or "two the same". Its pair is not a P1 pair.
- The four P1 pairs (same shape, same fill, two all-different); K–1's "give your partner new pairs"; 2–3's open "can any pair have two different answers?"
- The cap at three depths, then 2–3 P5's "Can your choices change how many moves the game lasts?" and 4–5 P5's "get stuck early".
- Guide: "Do not announce the largest legal collection"; ten pair markers in four dishes (p. 5); the 3 + 3 + 6 count and parallel-class key (p. 4).

## Fix

1. **should**, all bands, guide p. 2: "prepare one set of nine large tiles per child… 20-35 minutes to print or draw, cut and sort". Every problem uses the tiles and nothing prints them. Not a must (compare Week 23): each packet already prints all nine tiles in 60 mm cells (K–1 p. 3, 2–3 p. 3, 4–5 p. 2). Write: "Print K–1 p. 3 on card stock once per child, plus one, and cut on the grey lines: nine 60 mm tiles that fit the mats' cells." Drop "45 mm".
2. **should**, guide p. 1 or 3: the record boards (2–3 p. 4, 4–5 pp. 3–4) use the tic-tac-toe layout, on which all eight straight lines are allowed threes and four are bent: {CO, TF, SH}, {CH, TO, SF}, {CH, TF, SO}, {CF, TO, SH}. Reading lines off the board gives four threes through the centre, three through a corner, two through an edge tile, so a child can "explain why you have them all" with the wrong count (prediction). The guide says the grid is "not a rule about straightness" and "a straight row of physical tiles can fail", but neither fact. Add both.
3. **should**, 4–5 p. 4, P4: "Find every split, and explain why your list is complete" sits above four boards, and there are exactly four splits. Print six, three rows of two, cells about 18 mm.
4. **should**, 4–5 p. 1, P1: "Explain why any two different tiles have exactly one tile that completes an allowed three" prints the conclusion; the 2–3 page asks it openly. Write "Complete the pairs. Can two different tiles have two completing tiles, or none? Explain."
5. **should**, guide p. 2: "If the gate fails, sort or complete triples using only three shapes while holding fill fixed." One fill gives three tiles and one three, a minute of work for a K–1 table. Write: judge shapes only with all nine tiles; P2 and P3 still work, and the most is again four (two each of two shapes); then add fills with the printed near miss.
6. **could**, guide p. 2: "For ten children", an 8-minute launch, a group break at 23–27 and work to minute 57 ignore context.md's eleven children and 35–40 table minutes.
7. **could**, guide pp. 2 and 6: "the youngest adult" means the K–1 table's adult; say so.
8. **could**, 2–3 p. 3, P3: "Can you change one chosen tile and then add another?" names one test; "How do you know you cannot keep more?" is open.
9. **could**, WEEKS-11-51.md and the source README say "A nine-point world"; the packets say "Making threes".
10. **could**, bonus guide p. 2, P3 extension: use the math check's replacement; "may create cross-layer triples" sends an adult hunting for a triple that usually isn't there.

## Overlaps

Week 19 (antichains) shows maximal is not maximum; here they coincide, worth a cross-reference. Week 62 compares two and three colours for pairwise conflicts, bonus P2 for threes; Week 62's notes separate them. The two mixed splits are the orthogonal Latin squares of order 3, near the app's Symbol Orchard. Nothing else has this plane or a cap set: no merge.

## App fit

A, confirmed, size M rather than S. Tap to complete a pair, drag tiles into trays, select a three-free collection; the app checks every three. Pitfalls: at nine tiles every stuck collection has four tiles, so "make the largest" has no wrong path; the forced-length game is predict-an-outcome, which children enjoyed less.

- Nine tiles: P1 as tutorial; all four splits, the child declaring "that's all", no "2 of 4" counter (4–5 P4); threes through a tile (4–5 P3); four is most by a five-set's ten pairs in four dishes (guide p. 5).
- 27 cards (bonus P3's numbers): random greedy stalls at 8 in 13,752 of 20,000 runs and the maximum is 9, so "reach 9" is a real solve; lighting each unchosen card with the pair that blocks it certifies "stuck".
- Bonus P1's avoidance game against the computer (the first player wins by centre and opposites); bonus P2's three-colouring, with 9 > 4 + 4 against two colours.
- Shuffle tile positions so board lines don't stand in for the rule. 81 cards (maximum 20; 9 of 5,000 greedy runs) is a playground.

**Decision, October 10, 2026.** Port, in Wave 7 (sets and numbers), at size M: the nine tiles as the tutorial and the find-every-split set, then the 27-card layer where "reach 9" is a real solve and each unchosen card lights with the pair that blocks it, plus the bonus avoidance game and three-colour puzzle. Tile positions are shuffled so board lines don't stand in for the rule. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The source README says the theme is unpiloted; the October 4 record says the organizer approved the revision scope, not classroom effectiveness.
