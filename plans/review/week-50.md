# Week 50: Staircases and lengths

**Verdict: keep.** No must: every band can be used as printed, and every answer checks. The should fixes cover the length proof printed in the worked example and the older bands' P2, a Grades 4–5 P5 that repeats P3, and some wording and timing repairs.

Reviewed October 10, 2026 by Claude with the math check in [week-50-math.md](week-50-math.md). I agree with its three findings and rate each a should. Its "not asked" remark that 16 turns is the minimum for the ±8 mm strip holds only on its lattices: 15 suffice, with corners at multiples of 32/3 mm (`check_card.py`). This matters only for fix 2. Packets: `week-50-k-1.pdf` (F50-K-v2, 5 pp., P1–6), `week-50-grades-2-3.pdf` (F50-23-v2, 5 pp., P1–5) and `week-50-grades-4-5.pdf` (F50-45-v2, 6 pp., P1–7). Adult guide: `week-50-facilitator.pdf` (4 pp.). Companions noticed but not reviewed: `week-50-bonus.pdf` (F50B-S, 3 pp.) and its guide. Status: unpiloted. The October 4 revision changed only the guide.

## The mathematics

Every right-and-up staircase across the 160 × 120 mm rectangle measures 280 mm, because its right pieces add up to the width and its up pieces to the height. Staircases in narrower strips come as close as you like to the 200 mm diagonal and stay 280 mm: curves can be close while their lengths are not (the "√2 = 2" paradox). In the ±15 mm strip a horizontal piece spans at most 40 mm, and an end piece at most 20 mm, so 8 turns are needed, and 8 suffice. With left moves a path measures 280 + 2L, where L is the total distance moved left. A mathematician would enjoy the paradox and the turn bound, which has a matching construction. "Essentially one fact" (themes.md) misses P4 and the 2L cost.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | An invariant, a classic paradox, and a turn optimum with a construction and a counting bound. |
| Problems | adequate | Before any explaining, P1–P3 contrast the child's own staircases, an L shape against two steps, and four steps against finer steps. P4 is the best task in every band. Thin: older P2 (fix 1) and 4–5 P5 (fix 2). |
| Student pages | adequate | Spec header and footer, a one-line rule, and true-scale boards with a 100 mm bar. The regrouping proof (fix 1) and P7's discovery (fix 3) are printed, and one label is misplaced (fix 5). |
| Concreteness | adequate | Pencil and string make each path and its length physical. A 4-minute whole-group launch runs string along an example that is not one of the problems. Nothing enforces right-and-up or the strip, but both are visible. |
| Correctness | strong | All answers check. |
| Adult guide | adequate | Theorem-first overview, full keys including the seven-turn proof, hints kept with the adults. Fixes 6, 7, 11. |
| Age fit, K–1 | adequate | No reading or arithmetic; P4 suits them. P3's sentence is long for one hearing (fix 8). Laying string along nine pieces is untested. |
| Age fit, grades 2–3 | strong | Addition up to 360. P4's proof and P5 come late, and the guide offers turns "as exploration before proof". |
| Age fit, grades 4–5 | adequate | Pages 1–4 are the 2–3 pages. New work: P4's proof and P6–7. P5 adds nothing new (fix 2). |

## Keep

- The P1 → P2 → P3 order. P2's dashed staircase looks closer to the diagonal than the solid one and has the same length. P3's printed staircase leaves the strip, so any staircase drawn inside the strip is closer.
- P4 with "Its pieces may follow the strip's boundary". Without that sentence the answer is 9.
- K–1 P5–6, 2–3 P5's two 360 mm paths, 4–5 P6's labelled route and P7.
- In the guide: the seven-turn proof (p. 2), Routes A and B, and the note on string error.

## Fix

1. **should**, all bands p. 1, and 2–3 and 4–5 P2. The example sorts the pieces into a 40 mm "right pieces" bar and a 30 mm "up pieces" bar beside a 40 × 30 outline. The guide holds this grouping back as a hint (p. 3). P2 then says "Find their exact lengths using the width and height", which leaves only 160 + 120. Fix: P2 ends "Find the exact length of each staircase." Draw the example as one 70 mm bar with the pieces in path order, relettered A–D.
2. **should**, 4–5 p. 5, P5: "Can the new staircase be shorter…?" asks for 280 a third time. Fix: in `make.py`, set `corridor=7.5` (half of P4's strip) and change the caption to 7.5 mm. Then ask: "Make a staircase inside this narrower strip with as few turns as you can. Is it shorter than your staircase in the wider strip? Explain your answer." Key: 16 turns, by the guide's U7.5, R20, U15, …, R20, U7.5. With 15 or fewer turns there are at most 8 horizontal pieces, and if there are 8, one is an end piece, so they cover at most 10 + 7 × 20 = 150 mm; fewer cover at most 140.
3. **should**, 4–5 p. 6, P7: "Explain which distances can shrink and which length stays the same" prints the band's discovery (guide p. 1). Fix: "Explain your answer."
4. **should**, 2–3 p. 5, P5: "Could such a path be shorter than 280 mm?" points back to the 360 mm paths, so the answer is a trivial no (math check 2). Fix: "Could a path with leftward pieces be shorter than 280 mm?"
5. **should**, all bands p. 1: "C: 20" sits on the gray outline, 8 mm from piece C (math check 1). Fix: in `make.py` `example()`, move the label from (17,45) to (31,46).
6. **should**, guide p. 1, Launch: "the horizontal strip … the vertical strip". The page shows two horizontal bars, and "strip" elsewhere means the gray corridor (math check 3). Fix: "the 'right pieces' bar … the 'up pieces' bar".
7. **should**, guide pp. 1 and 4: the two pages give different plans for the first visit. Page 1's "Flexible hour" has no run-around and an unexplained "walk an imagined right/up route". Page 4 stops first visits at P3. Fix: one plan following `context.md`: 0–5 run, 5–9 launch, 9–48 P1–P3 and then P4 for any pair that finishes, 48–55 share.
8. **could**, K–1 P3: "closer to the shortcut than this one reaches" calls the dotted line "the shortcut" while the caption calls it "the straight diagonal", and any staircase inside the strip is already closer. Fix: "Make a staircase inside the gray strip. Compare its length with this one using string." In the older bands, delete "with a smaller greatest vertical gap from the diagonal than this path".
9. **could**, delete "clipped by the rectangle" (older bands p. 4, 4–5 p. 5), "It goes left once" (4–5 P6) and "A straight diagonal is 200 mm long." (2–3 p. 5).
10. **could**, materials (untested): give K–1 a 30 cm pipe cleaner. It holds corners, and every staircase leaves about the same tail past F.
11. **could**, guide: state the eight-turn optimum in the overview.

## Overlaps

Week 26 uses the same projection for P ≥ 2(r + c). Weeks 67 and 69 rely on staircases being shortest grid routes, and Week 55 uses one as its certificate. Week 72's robot walks the same staircases, whose areas differ while their lengths agree, so the two weeks make a good return-visit pair. Only Week 50 has the paradox and the corridor bound. No merge.

## App fit

Change C to B, size S, for the turn optimum. On a grid every staircase visibly takes a + b steps, and the paradox is continuous, so neither makes a puzzle.

- **The puzzle.** The child drags a right/up path through a shaded corridor within a turn budget set at the optimum. Vary the slope, the width, and whether corners may touch the edge (here 8 turns against 9).
- **Certificate for "fewest".** Shade the windows. Each horizontal run fits in one window, and the end windows are half-width.
- **A second set.** Reach F in exactly a + b + 2L steps, two ways, with left steps allowed; bonus P1's priced diagonals fit beside it.
- **The board.** Memory robot's (Week 72), with the memory hidden.

Pitfalls: a live length readout as the goal, "predict the length" screens, and corridors whose optimum needs off-grid corners. Draw on P4, fix 2's strip, K–1 P5, 2–3 P5 and bonus P1.

**Decision, October 10, 2026.** Port, in Wave 9, as a short group on Memory robot's board with the memory hidden: drag a right-and-up path through a shaded corridor within a turn budget set at the optimum, with the shaded windows as the certificate for "fewest", then reach the finish in an exact number of steps with left steps allowed. The length invariant and the near-diagonal paradox stay on paper: on a grid the first is visible at a glance and the second is continuous. No live length readout. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The source README says the theme "remains **unpiloted**".
