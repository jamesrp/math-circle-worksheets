# Week 67: Meeting on shortest roads

**Verdict: keep.** No must. Every answer checks, the guide is at the bar, and the grid, tree, triangle and cube reach a real theorem in order. The closest call is P5, whose cube maps P4 has already used; a child can reuse one, so it is a should.

Reviewed October 10, 2026 by Claude, with the math check in [week-67-math.md](week-67-math.md). Packets: week-67-students.pdf (GGT67-S-v1, 4 pp., one Grades 3–5 packet, Problems 1–5). Adult guide: week-67-facilitator.pdf (GGT67-FAC-v1, 2 pp.). Companions noticed but not reviewed: none exist. Status: unpiloted prototype awaiting organizer review. The source README says "physical preparation and handling have not been rehearsed."

## The mathematics

A meeting dot for three homes lies on some shortest route for each pair. On a full grid exactly one dot works: the middle x with the middle y. On a tree exactly one dot works, the centre of the three paths. On the cube it is the label with the majority digit in each place, and on a triangle no dot works. These are medians in median graphs (Druţu–Kapovich, Defs. 6.1–6.3, Ex. 6.19). A mathematician would enjoy it: uniqueness is proved one coordinate at a time, and existence fails on the triangle. P1–P2 carry the grid rule, P3 the contrast between networks, and P4–P5 the majority rule.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real theorem with honest limits: the full grid, "some" shortest route, and the triangle. |
| Problems | strong | P1: an interior meeting dot (1,1) and an edge one (4,3). P2's hunt for "none" and "more than one" builds the conjecture. P3: a three-junction tree, a triangle (none), a square (home B). P4 repeats one shape (fix 3). |
| Student pages | adequate | Spec header and footer, no Name/Date, no slop. Worked visuals come before the route and digit conventions. P5 lacks a clean cube (fix 1). |
| Concreteness | adequate | Counters hold homes and the proposal; a partner checks every length; the launch moves M on the printed example. Nothing physical enforces "shortest", and pp. 3–4 are paper only. |
| Correctness | strong | math.md: 40 checks, 0 failures, maps rebuilt from the PDF, every triple enumerated. I agree; fixes 3 and 7 checked in code. |
| Adult guide | strong | Theorem-first p. 1 with the full-grid limit, a warning against minimizing total travel and a band map; launch, a 25–30 minute route, keys with proofs, held hints. |
| Age fit, K–1 | weak | No pages, by design. Guide p. 1: "No K–1 adaptation or tested age-fit claim is intended." |
| Age fit, grades 2–3 | adequate | For third graders only. Children count and add within 8, and an adult reads p. 1's eight sentences. The load is holding one proposal through three coloured checks (prediction). |
| Age fit, grades 4–5 | strong | The whole packet, with the organizer: why P2 never finds a second dot, P3's impossibility, P5's proof. |

## Keep

- p. 1's rules ("each pair of homes has a shortest route through it", "The meeting dot may also be a home.", the fixed proposal, partner roles) and the P–M–Q example, which checks one pair without a three-home answer.
- P1's two boards and "every meeting dot"; P2's two impossible questions; P3's three maps with the tree's decoy branches.
- p. 4's 001 → 101 → 100 visual and crossed-roads rule; P5's open question.
- The guide's overview, the launch move of M, the P1 table and the P5 proof.

## Fix

1. **should**, p. 4, P5: "Choose three new homes on a cube map." Both cubes already carry P4's homes and coloured routes (math.md item 1), which coloured pencil won't erase cleanly. Fix: replace two answer rules with a blank `\cube` at 1.2 cm, or move P5 to a new p. 5 with two.
2. **should**, K–1, guide p. 1: no route, so the K–1 table spends the hour elsewhere. A should, as on the Week 60 and 62 cards, because the outline says "No forced K–1 or separate Grades 2–3 version". If taught to the current group, add a K–1 page: two 3×3 grids with two homes each ("Put a counter on every dot where the walk can stop and still be shortest."), then the P3 tree ("Where do all three walks meet?"), the adult scribing. That K–1 can do this is a prediction.
3. **should**, p. 4, P4. Each triple is the three neighbours of one label (000, 110, 101 around 100; 001, 010, 111 around 011), so a child can leave with "the dot next to all three". That fails for 000, 001, 111, whose meeting label 001 is not next to 111. Fix: use 000, 001, 111 on the right map (distances 1, 3, 2); key 001, routes 000→001, 000→001→011→111, 001→011→111.
4. **could**, p. 4: cut "Each dot on these maps has a three-digit label.", which describes the diagram.
5. **could**, p. 1 example: at 0.9 cm the M and Q circles touch and the thick M–Q road is a stub. Draw the example at the boards' 1.6 cm spacing.
6. **could**, p. 2: move "Keep a drawing of your attempts." to the guide.
7. **could**, P3 or guide: two crossroads each joined to A, B and C (two dots work) and a six-dot ring with alternate homes (none), so uniqueness visibly depends on the map too.
8. **could**, guide: the majority of three digits is their middle value, so P5 is P1's rule on a 2×2×2 grid; name median graphs.
9. **could**, guide launch: all six dots work for P and Q; two homes have many meeting dots, three have one.
10. **could**, guide: give a counter size (about 1.2 cm) for the 1.6 cm spacing, or enlarge P1's boards into p. 1's empty lower third.

## Overlaps

Week 69 (Thin and fat road triangles) shares the three homes, coloured pairwise routes, partner checks, trees and grids, and its P1 tree question is P3's tripod. Its theorem, thinness, differs, so teach 67 first and 69 as a return visit. Week 50's staircases are the grid fact behind P1. Weeks 18 and 46 count differing digits, which is cube distance. No merge.

## App fit

**A, size S** (proposed): the shared graph board already draws finger-traced coloured routes (flow, detours). The row should read:

| 67 | Meeting on shortest roads | Place a meeting counter for three homes; draw each pair's shortest route through it, on grids, a tree, a triangle, a square and a cube | Grids, trees and cubes have exactly one such dot (middle coordinates, tripod centre, majority label); a triangle has none | No (the shared graph board) | A | Tap a dot and trace three routes the app length-checks; "That's all"; place homes or cut a road so no dot, or two, work | S |

Solves: find the dot, with the three traced routes as certificate; "That's all" for find-every, with no count shown; design no meeting dot (a 3×3 grid missing its centre's roads, per math.md) or two (the crossroads map). For "none", the certificate is each dot with a pair it fails. Pitfalls: live per-pair lights make tapping all 25 dots a strategy, so require the routes; never score total travel, which gives away grid answers and is the wrong test elsewhere; put the difficulty in the maps, since grids are routine once the middle rule is known. Draw on P1, P3 and P4, moving P2's goals to maps where they succeed; P5's rule stays on paper.

**Decision, October 10, 2026.** Ported as **Meeting roads** on the shared graph board ([app PR #31](https://github.com/jamesrp/small-math-adventure/pull/31), `docs/meeting/`): three walkers meet on one dot, and any two walks together must make a shortest route between their homes, or the app draws a shorter one; one-answer maps, find-every maps with That's all (0, 1 or 2 answers), and closing a road so no dot works. Satchel only; not deployed and not yet played by children.

## Classroom evidence

None reported. The packet is an unpiloted prototype awaiting organizer review, and no use record mentions Week 67.
