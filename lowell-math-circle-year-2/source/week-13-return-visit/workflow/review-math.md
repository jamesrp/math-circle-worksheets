# Week 13 independent mathematics review

Reviewed the actual three-page `draft/return-visit.pdf`, its rendered pages, and `draft/src/return-visit.tex`. The three-file harness defaults do not apply to this shared return-visit collection. I did not read or use the writer's audit, check script, or claimed answers. No correctness defects were located in any band.

## K–1, page 1, Problem 1: checks out completely

The task asks for the largest simultaneous S-to-T packing on each map, first allowing shared middle dots and then allowing only one route per middle dot. The no-shared-arrow rule remains in force in both cases.

- **First map:** the four directed routes are S–A–H–C–T, S–A–H–D–T, S–B–H–C–T, and S–B–H–D–T. The answers are **2** with shared middle dots and **1** with one route per middle dot. For example, S–A–H–C–T and S–B–H–D–T share only H internally and use distinct arrows. Only two arrows leave S, and every route contains H.
- **Second map:** the extra arrow is A→C. The answers are **2** and **2**. S–A–C–T and S–B–H–D–T share no middle dot and no arrow. The two outgoing arrows from S still give the upper bound of two.

Independent exhaustive enumeration finds two optimal edge-disjoint packs on the first map and three on the second; the second has exactly one optimal internally vertex-disjoint pack. The smallest internal-dot deletion is {H} on the first map and has size two on the second. These checks distinguish internal dots from the common endpoints S and T. The printed arrowheads and labels match the two graphs, and the small U→V→W example correctly reserves only V.

## Grades 2–3, page 2, Problem 2: checks out completely

The task asks which specified pairings admit two simultaneous routes without a shared arrow, then asks for a feasible reassignment to two different finishes.

- **P→X and Q→Y fit.** P–A–X and Q–B–Y are a certificate. Enumeration gives three feasible packs: both direct routes, or either direct route together with the other route through C→D.
- **P→Y and Q→X are impossible together.** Individually their unique routes are P–A–C–D–Y and Q–B–C–D–X. Both require C→D. Sharing a dot is allowed, but sharing this arrow is forbidden.
- **Free assignment to the two finishes:** P→X and Q→Y works; the opposite assignment does not.

All three printed copies have the same nine directed arrows P→A, Q→B, A→X, B→Y, A→C, B→C, C→D, D→X, and D→Y. The simultaneous-reservation rule rules out sequential reuse of C→D. There are no unmarked geometric crossings that create an alternative reading.

## Grades 4–5, page 3, Problem 3: checks out completely

The task asks for a largest integral route packing with repeated routes allowed, followed by a set of crossed-out arrows that blocks every S-to-T route and whose capacities sum to the achieved packing size.

There are exactly three route types: S–A–T, S–A–C–T, and S–B–C–T. Let their multiplicities be x, y, z. The constraints are x≤1, y≤2, z≤2, x+y≤3, and y+z≤the printed C→T capacity.

- **C→T capacity 3:** the maximum is **4**. Both optimal multiplicity triples are (x,y,z)=(1,1,2) and (1,2,1). Crossing out A→T and C→T blocks every route and has sum 1+3=4. Exhaustive enumeration of all arrow-deletion sets finds this is the unique minimum-capacity cut.
- **C→T capacity 4:** the maximum is **5**, attained only by (x,y,z)=(1,2,2). Crossing out A→T and C→T has sum 1+4=5; crossing out S→A and S→B also has sum 3+2=5. Exhaustive deletion enumeration finds five minimum-capacity cuts, all of value five.

Every printed capacity is attached to its intended arrow. Both route counts fit the provided six rows. The U→V→W example has capacities 2 and 3 and correctly shows two simultaneous identical routes, using capacity two on each arrow. The task has a matching packing/cut certificate on both maps.

## Independent computation evidence

`math-independent-check.py` enumerates every directed simple route, every edge-disjoint and internally vertex-disjoint subset on the first two maps, both terminal assignments, every bounded route-multiplicity triple on the capacity maps, and every arrow/internal-vertex deletion subset used for the cut checks. Its full results are saved in `math-independent-check.json`. All task graphs are acyclic, so this route enumeration also covers every directed walk.

No source or PDF edits were made. Physical rehearsal and classroom suitability are outside this correctness-only review.
