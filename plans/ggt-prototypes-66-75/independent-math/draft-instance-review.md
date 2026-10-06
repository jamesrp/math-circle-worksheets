# Exact draft-instance review

All ten final writer-stage drafts were independently checked on 2026-10-06. The reviewed source and PDF fingerprints are in `draft-instance-check-results.json`; this does not certify later critic/reviser versions automatically. Tests import none of the writers' checking code.

`verify_draft_instances.py` is a standalone standard-library checker for the exact numerical/graph/geometric instances below. `bounce-unfolding-instance.json` is a small owned coordinate snapshot of the draft's two four-room unfolding diagrams, checked independently by reflection. With `--writer-root /path/to/parent`, the checker also fingerprints the available writer worktrees. Without that optional argument, no worktree or downloaded reference is required.

## Week 66: all five problems pass

- P1 A/B/C: minimum2,5,6 moves.
- P2 A/B/C: minimum9,11,9 moves. The final walker position really changes the answer.
- P3: minimum7.
- P4 L/R/F targets: all minimum6 from the original all-off origin.
- P5: therefore no, an extra legal move cannot always make a target harder to reach.

The source-defined lamp sets and final walker positions were read directly, since PDF text extraction alone cannot identify filled lamps.

## Week 67: all five problems pass

- P1 left/right medians: `(1,1)` and `(4,3)`.
- P2: every three-home placement on the full rectangular board has exactly one meeting vertex.
- P3: tree vertex `v=(2,0)`; triangle none; four-cycle B.
- P4 cube medians: `100` and `011`.
- P5: coordinatewise majority works universally.

Road length is the number of edges, not its length in the drawing. The cube convention explicitly excludes unlabeled crossing intersections.

## Week 68: all eight problems pass

- P1: maximum two infinite components for1,2 or4 blockers on the line.
- P2 example: blockers at −3,−1,0,2 trap exactly the two singleton pieces `{−2}` and `{1}`.
- P3: one blocked ladder vertex leaves it connected; two vertices on one rung separate its two infinite tails; two adjacent vertices on the same rail leave them joined.
- P4: four blockers cannot make three infinite ladder components.
- P5: block the four neighbors of a grid vertex to isolate it. The printed five-blocker vertical wall can be bypassed above or below; P-to-Q shortest length is10. Each grid still has one infinite component.
- P6: every finite deletion leaves just one infinite grid component; use the exterior-box proof.
- P7:3,6,12. P8:24, with doubling after each further blocked radius.

The drafts explicitly permit routes beyond the visible grid and identify the infinite continuation of each pattern.

## Week 69: all five problems pass

- P1: both drawn graphs are connected trees. All385 triples on the two actual graphs were checked; each used road belongs to exactly two pairwise paths, never just one.
- P2: choose AC via B for gap0 everywhere. Choose AC via `(0,4)` for a gap4 witness, satisfying the requested gap at least2.
- P3: exact largest achievable gaps on the2-,4-,6-unit boards are2,4,6. Every AC shortest path was enumerated:6,70,924 paths respectively. AB and BC are forced along the bottom and right.
- P4: pick integer n larger than the partner's number, and use the left/top AC route; its far corner has gap n.
- P5: no tree triangle has positive gap, by the tripod proof.

## Week 70: all four problems pass

P1 requires four shields already for its four disjoint diagonal interiors. P2/P3's16 target lifts have coordinates from `{−2,2,6,10}^2`. For each, the checker identifies its first target hit and verifies that this earlier segment meets one of the four universal midpoint shields. This includes the long diagonal shots to `(6,6)` and `(10,10)`, which first hit `(2,2)`. P4's four shields are both sufficient and minimal. Continuous point shields, first hits and portal seams are explicit.

## Week 71: all four problems pass

P1 has ample choices from its fixed center: six checked witnesses are ABC,ACA,ADC,BAD,CAC,DAB, with rational direction vectors in the results JSON. Their three crossings stay in the printed unfolding window and avoid corners. The checker found20 distinct center-start three-letter words; completeness of that20-word collection is not needed by the problem.

P2's square and rhombus unfolding diagrams contain the correct reflected labeled rooms; all eight polygons were independently reconstructed and compared to the authored coordinates within their decimal rounding tolerance. ABA is impossible in the square and feasible in the rhombus. P3 correctly distinguishes a proof of impossibility from unsuccessful trials. P4's horizontal stretch preserves the whole word language.

## Week 72: all four problems pass

P1's six memories are4,3,2,2,1,0. P2's24 orders of E/N/W/S yield memory−1 four times,0 sixteen times,+1 four times. P3's translated2-by-1 rectangles yield±2, and the six-vertex L outline yields±3. Translation of a closed loop preserves memory.

P4 witnesses: three positive unit loops followed by EENN give7; seven negative unit loops followed by EENN give−3. Arbitrarily many repeated unit loops establish every integer memory, and fit inside the displayed working board. The full path, not just its final position, determines memory.

## Week 73: all six problems pass after strict-interior clarification

The current source explicitly says O is inside, not on an edge. The fan maps are well-defined affine homeomorphisms on four glued triangles. Every original five-pin placement scores2, yet midpoint tests against O expose every off-center placement. The exact proof and legal-map assumptions are in `review-math.md`; finite sampled pin checks alone do not establish the all-pairs upper bound.

P3/P4 optimum2 is attained by `(x,y)->(x/2,2y)` in normalized rectangle coordinates. P5 target6-by-2 has optimum2; target2-by-3 has optimum3. P6 examples:6-by-1 or3-by-1.5, with general condition `max(W/4,H)=1.5`.

The independent finite check covers225 interior O placements and detects all224 off-center ones. The two-unit-disk argument supplies the universal conclusion.

## Week 74: all five problems pass

P1:3 costs3;7 costs6. P2:16 costs8, with multiple optimal words. P3 budget4–8 maxima:4,6,8,12,16. P4: no seven-move route can reach16 and return to ground. P5:9 costs7;15 costs9;17 costs9;23 costs10. Without left moves23 costs11, so the extra investigation genuinely distinguishes the move sets.

Both BFS searches are coordinate-unbounded and include all legal levels within their depth budgets. The human lower bound for23 and a minimum-coin proof for the no-left case are in `review-math.md`. The displayed board reaches24, enough for the10-move overshoot witness, and explicitly continues beyond the page and upward.

## Week 75: all seven problems pass

P1/P2 routes of the requested windings exist; the repeated-rectangle endpoints for+2 and−1 are `(2.5,1)` and `(−0.5,1)` when the start is `(0.5,0)`. P3's invariant is winding relative to fixed endpoints. P4 shortest twist-word length is the absolute signed sum. P5 requires three plus and three minus twists, in any order; there are20 such length-six words, e.g.+++---.

P6 minima for the listed winding pairs are0,1,2,1,2,1. P7:2 versus7 gives4;5 versus5 gives0. Adding the same twist preserves the winding difference, while twisting only one changes it. The printed rules exclude shared subarcs and non-crossing touches and exclude shared endpoints from the count, matching the proved intersection formula. Yarn must remain on the surface during allowed deformations.

## Review limits

All universal mathematics above is proved in `review-math.md`. Source attribution is separately checked in `sources.md`. The exact student-source geometry and PDF text were inspected; the Week 73 first page was additionally rendered for scale/geometry inspection. This is not a full typography or final-PDF visual audit. Cutting, yarn routing, physical manipulation, staffing and classroom suitability remain unpiloted; this review makes no physical-rehearsal claim.
