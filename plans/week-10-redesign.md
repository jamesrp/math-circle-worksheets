# Week 10: Bridge puzzles, Euler trails, and the shortest delivery route

Revised September 27, 2026 in response to the [Week 1 classroom review](week-01-classroom-review.md) and the adopted AGENTS.md guidance. **F10-K/M/U/X-v3 are prepared, unpiloted revisions.** No observations about a Week 10 session have been supplied. The previous v2 source and PDFs are preserved separately in the weekly `archive-before-classroom-guidance-2026-09/` directories.

## What changed, and why

Children now try several maps and starting points before counting degrees. Fresh maps support two distinct repairs and a later closed-route repair. Upper work performs two loop insertions at different vertices before a general proof; delivery gets two route trials before pairing roads. Two six-odd-vertex maps contrast a sharp lower bound with one that cannot be attained. The extra separates actual weighted routes, shortest connections, the three pairings and a checked greedy counterexample.

These changes infer what may help from the organizer's reported Week 1 experience: sufficient contrasting work, explicit actions, and records introduced for a purpose. They are proposals, not claims that these new sequences succeeded with children. Formal generalizations, hints and discretionary proof follow-ups are in the [six-page facilitator guide](../lowell-math-circle-year-2/week-10/week-10-facilitator.pdf); numbered student problems state concrete actions with the space/diagrams needed to perform them.

## Entry points and mathematical work

Grades are approximate. Choose by prerequisites; read aloud, scribe and accept oral or drawn explanations. The additional pages provide flexible continuations, not a one-hour completion quota.

| ID | Pages | Prerequisites | Concrete sequence |
| --- | --- | --- | --- |
| F10-K-v3 | 3 | Adult reads; track a moving counter and used bridges; compare leaves and endpoints. | Triangle/branch and two-leaf/three-leaf contrasts; two separate repairs; a child-created town. |
| F10-M-v3 | 4 | Count degrees to 4 and distinguish odd/even; oral route records can be scribed. | Multiple starts before parity; house, branch and K4; two repairs then closed repair; constrained map design. |
| F10-U-v3 | 5 | Route lists, edge counts and parity; optional general proof uses finite construction and matching lower bounds. | Two concrete loop insertions; two closed delivery attempts; three pair repairs; open route; prism versus five-leaf star. |
| F10-X-v3 | 3 | Add lengths through 24 and compare three choices; shortest connection may involve several roads. | Actual routes; six shortest-connection trials; all pairings; two route certificates; cheapest-first tie counterexample. |

## Materials, launch, and flexible hour

Seven moving counters, about 35 used-edge markers, pencils and paper strips for loop insertion. Optional string and paper islands enlarge the models. Keep earlier maps for comparison; a crossing without a dot is not a junction. Parallel bridges are allowed; each road joins two different dots.

**Print a starting set:** page 1 of the appropriate level for each child (3 K–1 + 3 middle + 1 upper = **7 starting sheets**), with one master of each continuation and the optional three-page extra. Copy additional pages as needed and offer one at a time. The complete core packet lengths are 3/4/5 pages; the full roster set would be 26 sheets, but is not the default print instruction. Use US Letter, single-sided, actual size. No activity depends on physical scale calibration.

**Whole-group launch:** Let children freely build or walk small maps, then gather at a triangle. Walk A–B–C–A, mark each used bridge, and demonstrate the visited-island record. Invite another start. State that islands may be revisited but bridges are used once. Add a branch and begin an attempt before distributing starting tasks. Introduce parity only after contrasting walks.

**Proposed hour:** 0–10 handle materials; 10–15 short common action-and-record demonstration; 15–35 concrete attempts; 35–40 movement/reset; 40–55 revisit, compare or continue at the child's current stage; 55–60 share one result and tidy. Change this rhythm to fit actual exploration. Parent mainly supports K–1; organizer alternates middle/upper about every five minutes and leaves a specific next attempt. The upper child receives actual adult mathematical conversation. Roles rotate so each child acts.

## Stopping points and proof continuations

| Group | Satisfying stop | Optional facilitator continuation |
| --- | --- | --- |
| K–1 | Two-leaf versus three-leaf attempts and one demonstrated repair. | Explain why leaves force endpoints and why the unjoined leaf remains special. |
| 2–3 | Identify house endpoints or demonstrate a repaired K4 route. | Pair arrivals/departures at repeated visits to prove the odd-endpoint necessity. |
| 4–5 | Two actual loop splices, or an eight-step delivery route with its parity lower bound. | Constructive all-even Euler proof and temporary-edge argument; full route/pairing optimality reasoning. |

Do not require every table cell, map or page. Demonstrate each unfamiliar record once with the real objects. When a representation is causing copying rather than helping compare attempts, scribe or return to objects. Preserve both construction and explanation; the guide keeps complete arguments so they are available when children are ready.

## Observation plan and reuse

After the session record which exact pages/instances children attempted, what they tried, what needed adult rescue, what they explained and what they wanted to continue. Label adult hypotheses separately from observed behavior. Distinguish a child's explanation from a supplied theorem. Unused stages remain prepared reserves; do not mark a whole printed packet as taught. The existing use log records actual use; this revision makes no new teaching claims.

## Verified mathematical backbone

An Euler trail uses every edge exactly once; an ordinary trail may omit edges. For a finite connected undirected network with at least one edge, a closed Euler trail exists exactly when every degree is even, and an open Euler trail exactly when precisely two degrees are odd. Pair arrivals and departures to prove necessity. Begin the construction concretely with triangles ABC and ADE sharing A. Walk A-B-C-A and mark its edges; write each triangle loop on a paper strip, then insert A-D-E-A at a visit to A to get A-D-E-A-B-C-A. Check all six edges physically. For sufficiency in the all-even case, follow unused edges to a closed walk, start another closed walk at an on-route vertex with unused edges, and splice; connectedness and finitely many edges ensure completion. Add and later remove a temporary edge to handle the two-odd case.

K1 triangle ABC closes. Add AD: D-A-B-C-A uses every edge once. The three-leaf star needs three endpoints, impossible; add BC between leaves and D-A-B-C-A is the repaired trail.

House edges AB,BC,CD,DA,DE,EC have odd vertices C,D. Trail D-A-B-C-D-E-C proves feasibility. K4 (outer triangle ABC and center D) has all four degrees 3, impossible without repeats. A second AB edge leaves C,D odd; C-A-B-D-A-B-C-D is an Euler trail using both AB copies.

Upper delivery counts all six unit roads at least once and requires return to A. Four odd vertices require at least two repeated crossings, since each extra copy changes parity at only its two endpoints. Route A-B-C-D-A-C-D-B-A repeats AB and CD and attains 8. Pairings AB+CD,AC+BD,AD+BC each add 2 and all work. Allowing different finish leaves at most two odd vertices, so at least one repeat is necessary; A-B-C-A-D-C-D-B attains 7.

For a six-odd-vertex design with exactly 3 extra crossings, a triangular prism works: two triangles plus three matching cross-edges gives six degrees 3. Duplicate the three cross-edges, making all degrees 4. A five-leaf star also has six odd vertices but cannot attain 3 extra crossings; an odd-count lower bound alone need not be sharp.

Extra lengths AB=2, BC=3, AC=7, AD=1, BD=6, CD=1 total 20. Shortest connection costs are AB: 2, AC: 2 (via D), AD: 1, BC: 3, BD: 3 (via A), CD: 1. Pairings cost 3, 5, 4 respectively. Repeating AB and CD gives 23, attained by the same closed route as above. Choosing AD first (cost 1) forces BC (cost 3) and is worse. AC and BD still must each be serviced once despite shorter alternative connections.

Every closed covering walk, after removing one required copy per road, leaves an augmentation graph odd exactly at the original odd vertices. Its edges decompose into paths pairing those vertices and nonnegative-cost cycles. Each path costs at least its shortest connection; therefore minimum pairing cost is a lower bound. Duplicating shortest connections for a minimizing pairing makes all degrees even and attains the bound via Euler. This proves optimality rather than merely proposing a short walk.

## Sources and boundary between class and research

- Cornell CS 2800 Spring 2017, [Lecture 36: Paths](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec36-graphs2.html), Eulerian paths section: even-degree criterion and constructive cycle-splicing proof. This is an actual undergraduate discrete mathematics topic.
- Jack Edmonds and Ellis L. Johnson, *Matching, Euler tours and the Chinese postman*, *Mathematical Programming* 5 (1973), pp. 88–124. [IBM publication record](https://research.ibm.com/publications/matching-euler-tours-and-the-chinese-postman); [primary paper hosted at Michigan](https://web.eecs.umich.edu/~pettie/matching/Edmonds-Johnson-chinese-postman.pdf). Introduction describes the route problem and matching reduction; §4 concerns the matching algorithm and §5 Euler tours. The page explores the exact four-odd-vertex case, not the general blossom algorithm or polyhedral proof.
- Rozhkovskaya, *Math Circles for Elementary School Students*, M.4.1 “Make your own problem,” EPUB `OEBPS/part0031.xhtml`, motivates creation under constraints. Its original animal/figure/number prompt is different from these graph briefs.

Research connection: efficient weighted matching turns exponentially many pairing choices into a practical route-inspection algorithm. We point to a historical solved paper, with no claim that the child-sized optimization is an open problem.

For pedagogy, re-read *Math Circle by the Bay*, preface printed pp. viii–x (PDF 9–11): common themes with varying depth, manipulatives, explanations, and reserve challenges. Also re-read Rozhkovskaya, Lesson 3 “At the lesson” (`part0013.xhtml`) for attempts before an organizing display; Lesson 7 (`part0017.xhtml`) for verifying legal-move understanding; and Lesson 8 (`part0018.xhtml`) for unequal copying pace. Our preprinted material, adult rotations, and particular task sequence are adaptations, not arrangements reported by those sources. See [lesson-format-source-notes.md](lesson-format-source-notes.md).

## Returning children and future branches

Lowell Handout 10 has a shortest-password-window task tied to directed Euler/deBruijn constructions. This week uses undirected road maps, odd-degree impossibility, and minimum repeats; do not call all graph traversal new. Week 1 flip graphs concerned states and local moves, whereas these edges must all be serviced. Generic old workshop activities remain future reserves. Archive each child-created map with a route, claim, and reason. Update the [use log](fall-k-5-year-a-use-log.md) after teaching, recording exactly which packet pages and instances each child encountered; prepared reserves stay untaught. Preserve an oral explanation as a brief adult note when writing is a barrier.

## Verification and outputs

Independent Dijkstra search verifies closed/open unit K4 optima 8/7, weighted optimum 23, prism optimum 12 and five-leaf star optimum 10. Added assertions check the second K4 repair, every printed pairing route, third-loop insertion and the 24-cost greedy comparison. Finite checks support the printed cases; general proofs remain in the facilitator guide.

Run `python3 lowell-math-circle-year-2/source/week-10/verify.py`, then `sh lowell-math-circle-year-2/source/week-10/build.sh`. The five PDFs are written to `lowell-math-circle-year-2/week-10/`; editable TeX sources remain in the weekly source folder and intermediates in `tmp/pdfs/`. The [print index](../lowell-math-circle-year-2/source/week-10/README.md) and [review record](../lowell-math-circle-year-2/source/week-10/REVIEW.md) record final page counts and checks.
