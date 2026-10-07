# Week 77 mathematical design: persistent homology through repairable loop films

Research date: 2026-10-07. Pre-production source and mathematical design record; this is not a final student packet or answer key. Recommended range: grades 4–5, with an adult handling formal homology and verification.

## Recommendation and mathematical destination

Use a growing planar patchwork of dots, edge strips, and solid triangular tiles. Children control the arrival schedule and pursue an actual design problem: **Can you fill the first-born loop while leaving a newer loop alive? When is that possible, and what makes it impossible?**

Compare two triangles that touch only at one vertex with a square subdivided by a diagonal. Their films can have exactly the same hole counts at every time, but different persistence. The decisive operation is adding tile boundaries with a “two copies cancel” rule. Barcodes record the conclusion after the construction and proof; they are not the activity itself.

The theorem-level destinations are:

1. **Counts do not determine persistence.** Two valid filtrations can have equal first Betti numbers at every time and the same final complex, yet their inclusion maps and interval multisets differ. The two-chamber example below is an exact counterexample.
2. **The two-tile square theorem.** Begin with the three-edge path AB–BC–CD. Close the rim with AD at time b, add diagonal AC at s, and add the two triangular faces at u and v, where b < s <= min(u,v). Its H1 persistence intervals are [b,max(u,v)) and [s,min(u,v)), omitting an interval if its endpoints agree. In particular, exchanging the two face times does not change the barcode. The original rim survives the first filling.
3. **A finite, provable perturbation result.** Within this explicitly restricted square family, moving each of b,s,u,v by at most epsilon, while preserving the stated schedule inequalities, moves each endpoint of those two matched intervals by at most epsilon and changes each lifespan by at most 2 epsilon. A lifespan greater than 2 epsilon cannot become zero. This is a small classroom theorem, not a claim that children have proved general persistence stability.

This is genuinely different from an MST/connected-components activity. All core examples remain connected from time 0. Their informative changes are in H1, and 2-dimensional filled faces change which loops count. No clustering or merge-tree interpretation is needed.

## Source record and exact source scope

### Primary source

Herbert Edelsbrunner, David Letscher, and Afra Zomorodian, **Topological Persistence and Simplification** (2002):
https://pub.ista.ac.at/~edels/Papers/2002-J-04-TopologicalPersistence.pdf

Use PDF pages 2–3, Section 2, for simplicial complexes, mod-2 chains/boundaries, and age filters; PDF pages 4–6, Section 3, for persistence, inclusion-induced maps, simplex pairing, and interval visualization. PDF page 5 distinguishes time-based from index-based persistence. These establish the mathematical setting. The child constructions and proofs below are independently designed finite examples, not examples copied from the paper. Do not present the paper's three-dimensional alpha-complex machinery or general pairing algorithm as grade-school content.

### Optional adult extension, not required for the classroom proof

David Cohen-Steiner, Herbert Edelsbrunner, and John Harer, **Stability of Persistence Diagrams**:
https://pub.ista.ac.at/~edels/Papers/2007-01-StabilityPersistenceDiagrams.pdf

The linked PDF is the nine-page conference-version text; its first page says SCG ’05, although the author's publication list associates this filename with the 2007 journal publication. Cite the version accurately. PDF page 1 states the bottleneck bound; Sections 2 and 3 (including 3.2 and 3.3) give assumptions and proof. This supplies context for the restricted perturbation experiment; it does not license unqualified assertions about arbitrary changes to drawings, point clouds, or schedules.

No complete papers or excerpts are needed in the prototype bundle. Links plus the original classroom mathematics suffice.

## Exact finite mathematical model

Choose a fixed, noncrossing straight-line triangulation in the plane. Only its listed vertices, edges, and triangular faces are allowable pieces. Intersections must be common faces: crossing edges without a vertex, overlapping triangle interiors, and a line passing through a triangle's interior are not allowed. A tile is the whole closed triangle, not merely its outline.

Assign an arrival time f(sigma) to each piece. Every vertex arrives no later than its incident edges, and each of a triangle's three edges arrives no later than that face. Define K_t to contain exactly the pieces with f(sigma) <= t. Then every K_t is a simplicial complex and K_t is contained in K_t' whenever t <= t'. Pieces never leave during one run. Rearranging cards is allowed when designing a new run; physically removing a piece mid-film is not an ordinary filtration.

At a tied time, place vertices first, then edges, then faces. Take the recorded frame only after the complete tied-time batch. Such an ordering is legal but does not create positive-duration bars from its temporary intermediate states. The default examples avoid positive-feature birth/death ties. The perturbation experiment may deliberately create a zero-duration interval, which is omitted from the barcode.

Use time-based intervals [birth,death), with lifespan death minus birth. A frame at death is already filled. Do not mix this convention with the source's separate index-gap convention.

All exact homology below is over the field F2. An edge chain is a subset of edges. Adding chains means symmetric difference: an edge used twice cancels. A cycle is an edge subset with an even number of selected incident edges at every vertex. A boundary is a symmetric difference of boundaries of available filled triangles. Two cycles represent the same H1 class if their symmetric difference is such a boundary. For t <= t', the inclusion map sends a cycle's class at t to the class of the very same edge chain at t'. It may become zero or become equal to another class because new tiles have arrived.

For a finite planar subcomplex, the number of independent unfilled holes is beta1 = E - V + C - F, where F counts filled triangular faces and C counts connected components. This gives an independent count check, not a pairing rule. A graph cycle that surrounds available tiles can represent zero homology; counting all visibly closed walks is incorrect.

## Materials and substantial child agency

A laminated sheet with allowable dotted edges, removable edge strips, two-color triangular cardstock tiles, small edge tokens (two tokens on one edge cancel), integer time cards, and a phone/photo storyboard if convenient. No computer is needed. A pencil grid and tracing paper are sufficient.

Use a few boards, not an enormous triangulation:

- Two triangular chambers touching at a vertex.
- One square with one diagonal.
- Two or three such blocks connected by a tree of edges or meeting at isolated vertices. This adds design choices without introducing unchecked cross-block dependencies.

Children control meaningful decisions: which boundary closes first, when to add the divider, which half to fill first, whether a target repair order is possible, and which legal one-step timing changes defeat or preserve their design. They must give a witnessed construction or an impossibility argument. Pair exchanges can ask one team to replay and challenge another's plan. The tile-boundary cancellation is the evidence that explains the film, rather than a tally sheet attached afterward.

A coherent sustained investigation can move through:

1. Build two legal films of the same two-chamber board, with identical hole counts but different answers to “does the first loop survive to time 4?”
2. Attempt the same repair order on the subdivided square. Discover that one half-tile cannot fill its original four-edge rim.
3. Show why using edge-token cancellation, then state the square theorem in ordinary language.
4. Design a board and legal schedule for two prescribed lifespans, trade with a partner, and verify using tiles. Include a request that is impossible on one board and possible on the other.
5. Allow every chosen arrival time to move by at most one. Test which survival promises are guaranteed, then prove the elementary bound.

The task need not teach all five stages in one sitting. The design/counterexample/proof spine matters more than covering many barcode conventions.

## Checked example A: same counts and final board, different persistence

Use A=(0,0), B=(-2,0), C=(-1,2), D=(2,0), E=(1,2). The closed triangles ABC and ADE meet only at A. At time 0 put all five vertices and AB, AC, AD, AE. This is a connected tree. Add BC at time 1 and DE at time 2.

Film A: add face ADE at 3, then face ABC at 5.

Film B: add face ABC at 3, then face ADE at 5.

Both films have beta1 values 0 at time 0, 1 at time 1, 2 at time 2, 1 at time 3, and 0 at time 5. They have the identical final filled two-triangle board. The numerical tuples (V,E,F,C,beta1) are:

- t=0: (5,4,0,1,0)
- t=1: (5,5,0,1,1)
- t=2: (5,6,0,1,2)
- t=3: (5,6,1,1,1)
- t=5: (5,6,2,1,0)

Let P=AB+BC+AC and Q=AD+DE+AE. The classes are independent because they have disjoint edge supports. Each filled face adds exactly its own boundary relation. Thus:

- Film A has H1 intervals [1,5) and [2,3), lengths 4 and 1. The inclusion H1(K_1)->H1(K_4) has rank 1.
- Film B has H1 intervals [1,3) and [2,5), lengths 2 and 3. The same inclusion has rank 0.

This proves that identical Betti counts do not specify persistence. It also refutes “a filling always kills the newest loop anywhere on the board”: Film B legitimately kills the older independent class while the newer one survives.

For a direct comparison with the next square example, simply relabel arrival times 1,2,3,5 as 2,4,5,8. The two-chamber options become [2,8),[4,5) or [2,5),[4,8), while the square below permits only the former under its construction constraints.

## Checked example B: the shared-diagonal square

Let A=(0,0), B=(2,0), C=(2,2), D=(0,2). At time 0 use all vertices and AB, BC, CD. Add AD at 2, AC at 4, face ABC at 5, and face ACD at 8. This is legal: every face's three boundary edges already exist.

The tuples (V,E,F,C,beta1) are:

- t=0: (4,3,0,1,0)
- t=2: (4,4,0,1,1)
- t=4: (4,5,0,1,2)
- t=5: (4,5,1,1,1)
- t=8: (4,5,2,1,0)

Define the edge chains:

- O=AB+BC+CD+DA, the original outer rim.
- P=AB+BC+AC, the rim of ABC.
- Q=AC+CD+DA, the rim of ACD.

The exact cancellation identity is O=P+Q. The diagonal AC appears twice on the right and cancels.

Before time 2, H1=0. From 2 to 4, O is a basis. From 4 to 5, O and P form a basis (equivalently P and Q do). At 5 the new available face imposes P=0 in homology. Hence [O]=[Q], and this class remains nonzero because Q cannot be the boundary of the sole available tile ABC. At 8, Q is also a boundary and H1=0.

The inclusion maps therefore retain the original O class until 8. The new independent direction created at 4 ends at 5. The barcode is exactly [2,8), [4,5). Swapping the two face arrival times gives the same answer, using the basis O,Q before the first filling.

Useful map checks, independent of visual naming:

- rank(H1(K_2)->H1(K_4))=1
- rank(H1(K_2)->H1(K_5))=1
- rank(H1(K_4)->H1(K_5))=1
- rank(H1(K_2)->H1(K_8))=0

Children can verify the chain identity with edge tokens or by laying the two triangle outlines on top of the board and cancelling the doubled diagonal. Saying “the old hole picked the left/right descendant” would be an unnecessary and potentially false geometric story. What survives is the class represented by O, and after a tile appears another rim represents that same class.

## Proofs for the restricted classroom theorems

### Square theorem

Before b the board is a tree. Between b and s, O spans H1. Between s and min(u,v), H1 has basis O,P or O,Q. The first face makes one of P,Q zero; since O=P+Q, the remaining triangle rim represents the image of O and is nonzero. The second face makes it zero. Thus the old summand has support [b,max(u,v)), and the other summand has support [s,min(u,v)). This proves the interval formula through the actual maps. It is not inferred from the dimension sequence alone.

The equality cases s=min(u,v) give a zero-duration new interval. If u=v both independent directions end at that time. Using b<s keeps the classroom discussion of the first-born rim unambiguous.

### Why tiling the interior is a valid witness

For a simple closed edge loop in this planar triangulation, summing the boundaries of all interior triangular faces cancels every interior edge twice and leaves exactly the outer loop. If all those faces are available, the loop is a boundary. In these finite planar boards the filling 2-chain, if it exists, is unique: a nonempty finite selection of planar triangles always has some exposed boundary edge, so no nonempty 2-chain has zero boundary. Consequently the simple loop cannot be a boundary until every required interior triangle is present.

This is a useful substantial child task: exhibit the required tile collection and its exposed edges; show why one missing tile leaves an uncancelled edge. However, the time at which an arbitrary drawn loop first exists is not automatically the birth of an interval generator. It might already be homologous to an earlier loop or represent a sum of classes. The theorem above identifies the original square loop's birth separately. Do not generalize “take any outline's first appearance and final filling time” into a universal barcode algorithm.

### Restricted timing stability

For the square theorem, match old interval to old interval and new to new. If each of b,s,u,v changes by at most epsilon, then min(u,v) and max(u,v) each change by at most epsilon: every changed input is trapped between its original value minus epsilon and plus epsilon. The other two endpoints have the same bound directly. The difference between lifespans is therefore at most 2 epsilon by the triangle inequality. The new schedule must still be legal and obey b'<s'<=min(u',v'); otherwise it is outside this elementary theorem's stated family.

For isolated triangular chambers there is an even simpler version: birth is the maximum of the three rim-edge arrival times and death is the face time. The same max argument gives the same endpoint and lifespan bounds when both schedules are legal. A [2,3) interval can disappear under allowed one-unit edits by moving its last edge to 3 while leaving its fill at 3. A length-4 interval cannot disappear under one-unit endpoint errors, since its new length is at least 2.

A long interval is evidence of robustness to this specific timing-error model. It is not automatically a scientifically important structure. An arbitrary schedule can make a tiny geometric triangle live longer than a huge region.

## Research-stage computational check

A fresh small Python checker was run on 2026-10-07, separate from the hand proofs. It sorted simplices by (arrival time, dimension, vertex labels), checked every face precedes its coface, formed each boundary column as a set of codimension-one faces, and reduced columns by symmetric difference using the latest pivot. It had no persistence-library dependency. A separate union-find plus V/E/F count produced the tuples above.

The reduced H1 birth/death simplex pairs were:

- Square, ABC filled first: AC -> ABC gives (4,5); AD -> ACD gives (2,8).
- Square, ACD filled first: AC -> ACD gives (4,5); AD -> ABC gives (2,8).
- Two-chamber Film A: DE -> ADE gives (2,3); BC -> ABC gives (1,5).
- Two-chamber Film B: BC -> ABC gives (1,3); DE -> ADE gives (2,5).

There were no unpaired positive H1 columns in any final board. This verifies these finite examples, not arbitrary classroom boards.

## Child/adult boundary and nonnegotiable pitfalls

Child-accessible: legal arrival rules; replaying schedules; detecting an empty region; distinguishing an outline from a solid tile; double-edge cancellation; preserving a chosen original rim; designing and refuting repair schedules; time differences; the maximum/minimum argument with concrete cards.

Adult-only: chain groups and quotient vector spaces; formal inclusion maps and ranks; proving general interval decomposition; arbitrary persistence pairing; boundary-matrix reduction; bottleneck matchings and general stability. The adult can use those to validate the child models without putting the notation in the activity.

Important limitations:

- An unfilled graph triangle is a cycle; a filled triangular face makes that particular cycle a boundary. Three mutually joined vertices do not force a filled triangle in this model.
- These are deliberately weighted simplicial filtrations on a fixed planar board, not automatically Vietoris–Rips or Cech complexes of point data. A distance-based model would require its own exact rules and verification.
- Children must not add arbitrary crossing edges or overlapping faces and keep using planar hole counts.
- Adding edges can split visible empty regions; the resulting visual regions are not canonical identities of persistent classes. Use boundary cancellation and inclusion maps for pairing.
- “Kill the youngest” is only valid among the classes involved in the relevant boundary relation; it is false as a global visual heuristic. The two-chamber counterexample exposes that error.
- In the planar setting, a newly filled legal triangular face kills one H1 direction; in general higher-dimensional complexes a face can instead create H2. Do not export the planar statement without qualification.
- Use actual timestamps, not the number of printed frames, for lifespan. Tied-time microsteps do not contribute positive persistence.
- Moving dots without changing incidence or timestamps leaves this combinatorial filtration unchanged; it is not a meaningful experimental demonstration of metric stability.
- Repairing a schedule before replay is valid. Deleting material mid-run requires a different theory, such as zigzag persistence, and is outside this prototype.
- Measuring only the number of holes per frame cannot certify a barcode. Require at least one survival/cancellation witness across time.


## Production status

This record supports an outline. Fresh student writer, independent adversarial and mathematical checks, revision, separate guide production, final page inspection and extracted-source reconstruction remain required. Research-stage computations check finite examples and do not replace independent verification of the eventual packet. Physical preparation and classroom piloting are unperformed.
