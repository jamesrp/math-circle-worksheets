# Final independent mathematical verification

## Verdict and reviewed version

**PASS.** Grades 4–5, all five final pages and Problems 1–6 check out mathematically. No mathematical correction is required. The new final problem is solvable as stated, including its requirement that the two unchanged edge lists permit either strict disappearance order after a reset.

Reviewed `week-77-reviser/tmp/worksheet-runs/week-77-v1/final/students.pdf`, `final/src/students.tex`, and `final/src/README.md`. The PDF was freshly rendered at 100 dpi and all five pages were inspected. Its SHA-256 is `e27735de07fee5b65d5f8ea1be06e260f4724a12ca039e10bd8b8d704a4d4787`. Source and README hashes are recorded in the results file.

`independent_check.py` was preserved unchanged. `final-independent-check.py` reruns that independent review for Problems 1–5 and adds a separately written integer-mask calculation and literal closed-trail enumeration for Problem 6. Neither the writer's nor the reviser's `check_math.py` was read, imported, or run. Full results are in `final-independent-results.json`.

## Existing problems and wording changes

1. **Page 1, Problem 1.** The task asks for a loop killed by one face and another surviving either one-face filling. The only nonempty loop edge sets on the printed square-with-diagonal are the two triangle boundaries and the outer rim. Either triangle boundary supplies the first answer; only the outer rim supplies the second. The rim XOR either filled triangle boundary is the other triangle boundary, still nonzero. Adding the diagonal when needed before a filling is permitted. The non-task XY/YZ demonstration correctly leaves XZ.

2. **Page 2, Problem 2.** The task asks for every schedule where the first saved loop dies at stage 8. There are four schedules, of which exactly three qualify:
   - DA at 2, AC at 4, ABC at 5, ACD at 8.
   - DA at 2, AC at 4, ACD at 5, ABC at 8.
   - AC at 2, DA at 4, ACD at 5, ABC at 8.
   The excluded schedule fills ABC at 5 after AC at 2: the saved ABC boundary then dies at 5. Every schedule has hole counts 0, 1, 2, 1, 0. Actual boundary membership and every inclusion-map rank were checked. The three qualifying schedules have intervals [2,8), [4,5); the excluded one has [2,5), [4,8). The shortened opening removes duplicate wording; the printed stage list retains all construction choices and constraints.

3. **Page 3, Problem 3.** The task asks for one first-loop death at 5 and another at 8 despite identical counts. If AB closes first, filling ABC first gives death 5; filling CDE first gives death 8. Interchanging the two lobes gives the other two schedules. Exactly two of the four schedules have each death time. The initial graph is a four-edge tree; the triangles share only the marked vertex C. The stated hole counts are correct, and inclusion calculations confirm they do not determine the lifetime of the first saved loop.

4. **Page 4, Problem 4.** The task asks whether the tied schedule ever has two holes at a finished stage and for every single-event move to stage 3 or 5 that makes this happen. The original finished-stage counts at 0, 2, 3, 4, 5, 8 are 0, 1, 1, 1, 1, 0. Exactly two changes work: move AC to 3, or move filling ABC to 5. Moving AC to 5 or ABC to 3 is illegal because the face would precede a boundary edge. The revised instruction to place the edge, then its tile, but check only after both are placed correctly implements one tied stage; there is no persistent stage-4-only short feature. The two successful changes create [3,4) or [4,5), respectively, while the original rim persists on [2,8).

5. **Page 4, Problem 5.** The answer is no. If a saved loop cancels against a particular set of filled triangle boundaries now, that exact set of triangles remains available at every later stage. The saved edge list and their boundaries are unchanged. The same cancellation remains a witness, regardless of later added pieces. This proves the statement for every legal growing board, rather than merely extrapolating finite examples. The original exhaustive checks cover 41 legal square subcomplexes and 81 joined-triangle subcomplexes, 1,742 inclusion pairs and 2,065 earlier-cycle tests.

The shared rule now checks that all three edges are “in place when a triangle is filled.” This preserves closure and is compatible with the clarified tied-stage procedure.

## Page 5, Problem 6: complete family and universal relation

The first task asks for two distinct edge loops which survive the already filled ABO and BCO, survive either possible next filling, and die only after both remaining triangles are filled.

Write X = ABO, Y = BCO, Z = CDO, W = ADO. Here “support” means the unique set of these faces whose combined boundary equals the saved edge loop. Each face has an outer edge found in no other face, so no nonempty face combination has zero boundary. Consequently every cycle has a unique face support. The direct enumeration finds 16 even edge chains and 15 nonempty closed-trail edge sets, all matching unique nonempty face supports.

Exactly four loops satisfy the first task:

| One closed walk | Saved edge set | Unique face support |
| --- | --- | --- |
| A–O–C–D–A | AO, CO, CD, AD | Z, W |
| A–B–O–C–D–A | AB, BO, CO, CD, AD | X, Z, W |
| A–O–B–C–D–A | AO, BO, BC, CD, AD | Y, Z, W |
| A–B–C–D–A | AB, BC, CD, AD | X, Y, Z, W |

Completeness follows directly: survival after either possible first remaining fill forces the unique support to include both Z and W. X and Y may independently be present or absent from the support. The code also independently enumerates all eight-edge closed walks with no repeated edge; thus it does not accidentally discard loops that revisit O. All four successful candidates happen to be simple loops.

**Universal relation:** every pair of these four loops differs by the boundary of a subset of the initially filled X and Y. They therefore represent the same nonzero class initially and after either single remaining fill, then vanish together after both. Distinct saved edge sets need not represent independent holes. The printed problem asks for distinct edge sets and makes no false independence claim.

## Page 5, Problem 6: either strict order after resetting

On the fresh all-edge board with no faces filled, a loop disappears exactly when all faces of its unique support have arrived. Its death position is therefore the latest filling position in its support.

For two supports, both strict death orders are possible exactly when neither contains the other. Of the six unordered pairs from the four valid candidates, only the two three-face supports are incomparable. Thus the unique reversible pair, ignoring traversal direction and the order in which the pair is named, is:

- L1: A–B–O–C–D–A, support X, Z, W.
- L2: A–O–B–C–D–A, support Y, Z, W.

Exact schedules:

- Fill CDO, ADO, ABO, BCO: L1 first disappears at filling 3; L2 at filling 4.
- Fill CDO, ADO, BCO, ABO: L2 first disappears at filling 3; L1 at filling 4.

All 24 face orders were checked against exact boundary membership for all 15 nonempty edge loops at every completed stage. For the reversible pair, six orders make L1 die first, six make L2 die first, and twelve give a tie. The initial equality of the two classes is not being carried across a forbidden removal step: the page explicitly resets to a fresh build, after which the previously filled triangles are absent and the two unchanged loops represent distinct classes.

## Diagrams and materials

- Pages 1, 2, and 4 show exactly the prescribed five square edge positions, with the prescribed initial solid edges where applicable. Page 3 has four initial edges and two dashed closing edges, with a real vertex at C.
- Page 5 has four outer edges and four spokes, totaling eight. O is a marked vertex, so the diagonals do not create an unmarked crossing. The four faces have disjoint interiors and cover the 8 cm square; each has area 16 square centimetres.
- The unshaded page-5 board is correctly usable for both starts because the task calls for placing removable opaque tiles. The README explicitly identifies the partly filled start, reset, separate tile set, and O-label marker.
- The material list covers every board edge, and three copies of each edge label suffice when testing one saved loop at a time: one saved-loop copy plus at most two incident-face copies. Launch tokens XY, YZ, XZ are now listed separately.
- Physical tile fit, handling, pacing, and classroom usability remain untested. This review establishes mathematical and digital consistency only.
