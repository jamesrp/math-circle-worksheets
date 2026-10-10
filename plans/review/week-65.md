# Week 65: Hyperbolic octagon streets

**Verdict: keep.** Every answer and diagram checks, and nothing printed would stop a child or mislead an adult. The fixes concern depth: the turning problems stop one case short of their rule, P5 leaves the geometry, and K–1 has no route by design.

Reviewed October 10, 2026 by Claude, with the math check in [week-65-math.md](week-65-math.md). Packets: week-65-students.pdf, W65-S-v2, 6 pages, one shared Grades 3–5 packet (Problems 1–5 on pp. 1–5, P5's route sheet on p. 6). Adult guide: week-65-facilitator.pdf, W65-FAC-v2, 7 pages. Companions noticed but not reviewed: none. Status: unpiloted; restored and regenerated October 6, when the organizer authorized integration; the 10 mm arrow is unrehearsed on printed boards.

## The mathematics

The {8,4} tiling: right-angled octagons, four at each corner, in the Poincaré disk. Moving an edge and turning left brings a walker home after 8 moves, not 4 (P1–P2); the outside of two rooms takes 12 quarter-turns against 4 for two squares (P3). Both are cases of one rule: around n rooms, left minus right turns is 4 + 4n here and always 4 on squares (Gauss–Bonnet). P4 shows two complete streets through P both missing R. P5 counts walks among four rooms at a corner, as four squares would. A mathematician would enjoy a turtle on a hyperbolic floor; P1–P4 carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Turning excess and many parallels, reached by walking and tracing, with honest limits (guide p. 1). |
| Problems | adequate | P1 is an open search (2, 6, 54 routes); P3 and P4 set hyperbolic against Euclidean. P2's walk is forced by the drawing. Turning gets one room and two, so "each room adds four" stays a guess (fix 1). |
| Student pages | adequate | Format right, no slop. A non-task worked visual before each new action (pp. 1, 2, 5); large boards; the route sheet hides the counts. Faults: an attention hint (fix 3); p. 4 is nine sentences for one problem. |
| Concreteness | strong | The arrow holds position and heading, a partner checks, a coin holds the room. Guide p. 2: a three-minute launch of one move and one turn; the curved example comes with p. 2. Arrow fit is checked only digitally. |
| Correctness | strong | math.md: 110 checks in an independent Lorentz model, one minor label (fix 5). My spot checks agree; I disagree with none of its findings. |
| Adult guide | adequate | Theorem-first overview with limits and evidence levels; full keys, the 16 − 4 explanation, the three-choice completeness argument, a whole-line proof. Missing the rule that ties P2 to P3 (fix 1). |
| Age fit, K–1 | weak | No route, by design: "use a familiar tactile activity for that table" (guide p. 1). |
| Age fit, grades 2–3 | adequate | Third graders act and count to 12, an adult reading. P3 asks them to walk, count and mark at once; P4's Euclidean question is abstract but late. |
| Age fit, grades 4–5 | adequate | P4's explanation and P5's completeness are real work, but a quick fifth grader may run through P1–P3, and the turning conjecture has no third case. |

## Keep

- The worked panels on pp. 1 and 2 (move and turn, on squares and on a bending road); P1's open "Find routes of 4, 6, and 8 moves".
- P3: one walk on octagons and on squares, started at the shared wall's end so the last arrival goes straight.
- P4: streets drawn whole to the boundary; lines that "continue forever in both directions".
- P5: the C → D → E strip; "You may visit a room or use a door more than once"; the separate route sheet.
- Guide: overview, launch, the 16 − 4 explanation, the eight-route table, the whole-line proof, the 56 − 8 = 48 extension.

## Fix

1. **should**, guide pp. 1, 3–4. Item 1 says only "Local quarter-turns need not make a four-step loop"; p. 4: "A general formula for larger clusters is not required." Yet 8 and 12 are cases of left minus right = 4 + 4n (always 4 on squares), and the children's 16 − 4 argument extends to it: a room added along one wall brings 8 corners and the wall removes 4; a square brings 4 and loses 4. Fix: state the rule in item 1, naming Weeks 56 and 61 as its positive-curvature twins. In P3's section, give ready pairs a pencil trace around Home, A and ⋆ on p. 5 (17 left, 1 right; an L of three squares: 5 left, 1 right). In P2's, ask "Can you get back to A facing B in fewer than 8 moves?" (no: every return circles a whole room).
2. **should**, K–1, guide p. 1, "Younger access". Run for the whole circle, the parent volunteer's table has nothing, though P1, P2 and P5's two-door routes are object work. Fix: a route (launch; P1's 4- and 6-move loops; P2's left-turn walk; P5's two-door routes with a coin; adult reads and scribes), or a note in WEEKS-64-65-DRAFT.md that the week needs a K–1 companion. Whether K–1 can hold a heading on curved roads is a prediction.
3. **should**, p. 3, P3: "Mark dots where you go straight." It points at the junctions the 16 − 4 explanation rests on; the blank asks only for left turns. Cut it; guide p. 4's hints cover it.
4. **should**, p. 5, P5 has the same counts on four squares, as guide p. 1 admits. The hyperbolic payoff, 48 rooms two crossings from Home against 8 on squares, is only on guide p. 7. Fix: a late Problem 6: "Every room has 8 doors. How many rooms can you reach from Home in 2 door crossings but not fewer? How many on squares?" Key: 8 × 7 − 8 = 48; 4 × 3 − 4 = 8.
5. **could**, p. 4: the R label is nearer the v₂v₃ street (9.5 mm) than R (16.2 mm); move it to (−0.66, 0), as math.md says.
6. **could**, wording: p. 4's "two distinct ordinary straight lines" → "two different straight lines"; p. 2's "heading" → "facing the same way", as on p. 1.
7. **could**, p. 5: enlarge the ⋆ on the board.
8. **could**, pp. 5–6: the two "beside" sentences repeat; p. 6 is P5's only answer space, not "Extra workspace".
9. **could**, guide p. 3: let a child fit a card corner into a drawn corner, so right angles are checked, not told.

## Overlaps

Week 64 walks straight paths on a flat glued octagon; both guides keep them apart. Weeks 56 (720° defect) and 61 (spherical excess) are the same theorem with positive curvature; this is the only negative-curvature theme. Cross-reference the three; no merge.

## App fit

Proposed row: | 65 | Hyperbolic octagon streets | Walk an arrow around right-angled octagons; trace complete streets; list room routes | Shortest return 8 moves, not 4; around n rooms net turns 4 + 4n (Gauss–Bonnet); two streets through P miss R | No | B | A robot on a recentring octagon floor: come home in n moves, fence rooms on a turn budget, tap streets through P that miss R; a square floor beside it | L |

The child taps left, straight or right; the floor recentres so every room looks the same size, which paper cannot do. Solves: come home facing the same way in exactly 8 or 14 moves; fence a block with 12 left turns and no right turns. "Can't" goals: home in 4 or 6 moves (every return circles a whole room of 8 sides; my enumeration agrees), any odd length (two-colour the corners), two rooms with fewer than 12 left turns. Pitfalls: no "run this program, say where it ends" (P2 as printed), the kind children liked least; no "x of 8" counters; skip P5. L for a new disk renderer. Draw on P1–P4.

**Decision, October 10, 2026.** Port, in Wave 9, as its own family on a recentring octagon floor. The robot's position is kept as its exact sequence of moves (left, straight, right), so returns are checked exactly and the drawing only shows them. The solves are coming home facing the same way in exactly 8 or 14 moves and fencing a block on a turn budget, and the "can't" goals carry the mathematics: home in 4 or 6 moves, or in any odd number, and two rooms with fewer than 12 left turns. The large board is worth it because these impossibilities are where the hyperbolic floor differs from the square one, and a square floor sits beside it for contrast. No "run this program" screens. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. Unpiloted; the October 6 authorization covers integration only.
