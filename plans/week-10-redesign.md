# Week 10: Bridge puzzles, Euler trails, and the shortest delivery route

Redesigned September 19, 2026; review revisions September 20, 2026. Prepared, not taught. Use Week 1’s standard of an approachable experiment leading to a theorem, obstruction, optimization, or controlled mathematical question. Three core entry levels plus **one optional grades 6–7 page**. Full launch prompts, hints, checked solutions, and the 60-minute operating plan are in the [four-page facilitator guide](../lowell-math-circle-year-2/week-10/week-10-facilitator.pdf) and its [editable source](../lowell-math-circle-year-2/source/week-10/week-10-facilitator.tex).

## What changed

Replace the unconstrained mixed-kit workshop with a coherent route investigation. Puzzle design remains, now controlled by an existence theorem, an invariant, and explicit optimality certificates. K1 reasons about dead ends; middle proves odd-degree obstructions and repairs; upper constructs Euler trails and minimizes repeated unit roads; extra solves a weighted postman instance and tests greedy pairing.

## Entry points and mathematical work

Grade labels are approximate. Reading can always be supported by adult scribing/read-aloud; moving objects and giving an oral explanation count as mathematical work.

| ID suffix | Investigation | Student pages | Prerequisites: reading/arithmetic/reasoning | Main work |
| --- | --- | --- | --- | --- |
| K | Cross every bridge once / Dead ends | 2 | No reading; count small incident bridges and distinguish an island from a bridge. Track used edges and reason that a leaf needs an endpoint. | Triangle and triangle-with-branch; impossible three-leaf star; add one bridge between leaves and show a repaired route. |
| M | One-walk maps / Repair an impossible map | 2 | Count degrees to 4 and odd/even. Explain all possible starts, not only failed attempts. | Find a house Euler trail, prove its endpoints forced, show K4 impossible, add a duplicate bridge to repair, and design a two-odd-vertex puzzle. |
| U | When a walk exists / Shortest delivery / Algorithm | 3 | Route lists, edge counts, odd/even, lower and upper bounds. Follow constructive cycle-splicing and a pairing argument. | Prove the Euler criterion constructively, optimize closed K4 at 8 and open K4 at 7, then design a six-odd-vertex network attaining the three-extra-edge lower bound. |
| X | Cheapest pair first? | 1 | Addition through 23 and comparing three choices. Distinguish shortest connections from individual road costs; decompose repetitions into odd-endpoint paths. | Weighted K4: original 20, minimum augmentation 3, optimum 23; compare all pairings and reject an incautious greedy choice. |

The complete IDs are **F10-K/M/U/X-v2**. There is no extra packet for the lower groups; offer the next entry level when appropriate.

## Materials, launch, and hour

Seven moving counters, about 35 small used-edge markers, pencils, scrap paper, and two short paper strips for the upper loop splice. Optional strings/paper islands enlarge the models. Dots are junctions; line crossings without dots are not junctions. Every road joins two different dots (no self-loops); parallel roads are allowed. Print three K1 packets, three middle packets, and one upper packet: **15 core student sheets**, plus the single extra sheet if wanted. Print single-sided, US Letter; actual size is recommended but no physical fitting depends on calibration. Introduce one page at a time.

**Launch:** Can you cross every bridge once without teleporting? Let children freely walk and build first. Make revisiting an island legal and reusing a bridge illegal. Pair an arrival with a departure only after routes have been tried.

**Proposed hour:** 0–10 build and walk freely; 10–15 brief shared rules; 15–35 main investigation: try routes, pair arrivals/departures, and splice physical loops; 35–40 movement/reset; 40–55 continue with repairs, route optimization, or an optional proof; 55–60 share an explanation and tidy. The weighted route stays optional.

One parent stays mainly with K,K,1; the organizer alternates between 3,3,3 and the fifth grader, aiming for a return within five minutes and leaving a concrete next attempt. Roles rotate within triplets, preserving two opposing sides for games. The fifth grader needs actual adult mathematical conversation. The exact timetable and staffing are this project’s proposal, not a documented arrangement from the books.

**Hints and pacing:** first ask a child to demonstrate the rule and show their current attempt; next ask for a smaller example or counterexample; only then offer the organizing representation on the next page. The facilitator gives specific hint ladders. A corrected conjecture is valuable. Do not fill time with copying or require finishing every task.

## Stopping points and optional proof continuations

| Group | Satisfying stopping point | Optional proof continuation |
| --- | --- | --- |
| K–1 | Explain the three-leaf obstruction, add one bridge, and demonstrate the repaired route. | Explain why the remaining leaf and the center must be the endpoints. |
| 2–3 | Explain the house endpoints and repair K4 with a duplicate bridge and a complete route. | Generalize arrival/departure pairing to prove every odd vertex must be an endpoint. |
| 4–5 | Physically splice the two triangle loops and find a closed delivery route of length 8 with a matching lower bound. | Generalize splicing to any connected all-even map, then add/remove a temporary edge to prove the two-odd case. |

The full Euler criterion is established only when the construction and temporary-edge argument are explained. Otherwise record the physical splice, tested routes, and parity lower bound actually reached.

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

Independent Dijkstra search over (current vertex, visited-edge mask) verifies closed/open unit costs 8 and 7 and weighted cost 23. Route edge coverage is checked independently. The parity and pairing certificates prove the claims beyond the computation.

Run `python3 lowell-math-circle-year-2/source/week-10/verify.py`, then `sh lowell-math-circle-year-2/source/week-10/build.sh`. Builds write five PDFs in `lowell-math-circle-year-2/combined/`; LaTeX is editable in the week folder. The [print index](../lowell-math-circle-year-2/source/week-10/README.md) and [review record](../lowell-math-circle-year-2/source/week-10/REVIEW.md) describe the delivered files and visual checks.
