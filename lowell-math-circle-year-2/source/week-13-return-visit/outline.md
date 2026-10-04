Week 13: Routes: what changes when sharing rules change?

Mathematical kernels

1. Edge-disjoint routes may share an internal vertex. On S→A,B→H→C,D→T (meaning edges S-A,S-B,A-H,B-H,H-C,H-D,C-T,D-T), two edge-disjoint routes fit but only one route fits if internal vertices cannot be shared. Adding A→C permits two internally vertex-disjoint routes. Internally vertex-disjoint route packing is controlled by removable internal vertices (when no direct S-T edge), not by the old edge cut. New rule must be visible with a counter occupying each reserved internal vertex.

2. Max-flow/min-cut for one start and finish does not settle specified terminal pairs. Use sources P,Q, finishes X,Y, and arrows P-A,Q-B,A-X,B-Y,A-C,B-C,C-D,D-X,D-Y. P-X and Q-Y fit simultaneously. P-Y and Q-X each exist alone but both require C-D, so cannot fit together. If endpoints may be reassigned two routes still fit. This supplies a concrete two-pair obstruction distinct from maximizing one-start routes. Keep both routes simultaneously reserved, rather than sequential travel.

3. Integer road capacities allow that many simultaneous routes to use an arrow. A capacity c may be represented by c separate lanes; the cut upper bound sums capacities, and integral packing attains a minimum cut. On S-A(3),S-B(2),A-C(2),B-C(2),C-T(3),A-T(1), the optimum is 4, bounded by the incoming capacity at T. Increasing C-T by one allows 5. The capacity model is a different mathematical direction, not changing the length of a road or sending successive counters.

Sources: Original local investigations and proofs from the familiar mathematical objects in the existing Week 13 guide. Existing guide references supply mathematical context, not copied exercises. Teaching sources consulted: Math Circle by the Bay, Preface pp. vii–x (PDF pp. 8–11); original year-1 Handouts 6, Problems 6.2–6.6, contrast representations of the same combinatorics. Specific teaching adaptations here are local planning choices, not source-reported outcomes.

Suggested emphasis by level: K–1: compare meeting at a dot versus sharing a road with adult-controlled reservations. Grades 2–3: two prescribed terminal pairs. Grades 4–5: capacities and matching cut certificates.

Materials

For a pair, pencils in two line styles, 16 closure/occupancy markers at most 15 mm, spare paper. Graph arrows have unobstructed midsections; capacities written beside arrows and represented by lane boxes if helpful. No geometric crossing is a meeting without a vertex dot. Single-sided US Letter, actual size. Preparation counts are proposed, stock and physical procedures untested.

Scope and layout constraints

Create exactly three genuinely distinct new investigations, one per kernel, as a separate return-visit shared collection. At least one substantial numbered problem per investigation; normally one page each, add a second only if needed. Use band/readiness header per page, not three forced duplicate band packets. New output for this workflow is draft/return-visit.pdf (and final/return-visit.pdf after revision); this explicit delegated layout overrides the harness three-file default. Number problems consecutively. Do not print adult hints, theorem, solution or method. Give board/workspace where the child uses the page. Retain familiar shared conventions, show a small visual worked convention only where a representation is new. Existing base PDFs and Week 1 encore are read-only. This packet is draft/unpiloted review material; delivery is explicitly authorized.
