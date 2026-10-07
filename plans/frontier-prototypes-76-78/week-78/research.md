# Week 78 mathematical design: Tropical lines, crossings, and hidden junctions

## Recommendation and scope

Use **three-arm tropical lines and point-line incidence**, with ordinary set intersection throughout. The week’s destination is a precise theorem children can investigate, repair with counterexamples, and prove geometrically:

> Two distinct tropical lines always meet. Usually they share exactly one point. They share an entire ray exactly when their junctions lie on the same horizontal, vertical, or rising 45-degree diagonal. If their junctions coincide, the lines are identical and share the whole three-arm figure.

A strong second destination is a genuine inverse-construction theorem:

> Two distinct points lie on exactly one tropical line unless they lie on the same horizontal, vertical, or rising 45-degree diagonal. In those exceptional cases infinitely many tropical lines pass through both points.

This offers real geometry, construction, classification, proof, and counterexample-making for Grades 4–5. Arithmetic only establishes why these particular three arms are a tropical line. Do not let the week become a min-plus arithmetic exercise, a nearest-site map, a cheapest-path problem, or a lesson in terminology. A physical “move the junction so the arms pass through targets” task gives younger children a meaningful entry.

**Do not add stable intersection to the child-facing core.** The literal infinite intersections are the mathematical discovery, not an inconvenience to erase. No assertion that two lines always have one intersection, no multiplicity counting, and no unqualified Bézout slogan.

## Source facts, with precise provenance

1. David Speyer and Bernd Sturmfels, *Tropical Mathematics* (2004), §1, printed pp. 1–2; §3, printed pp. 6–8 (PDF indices 5–7). https://www.claymath.org/wp-content/uploads/2022/03/Speyer.pdf
   - Uses min-plus: tropical addition is minimum and tropical multiplication is ordinary addition.
   - Defines a tropical hypersurface as the locus where the minimum is attained at least twice.
   - For min(a+x, b+y, c), the line has junction (c−a,c−b) and north, east, southwest arms.
   - Describes tropical plane curves and the connection to subdivisions, and states generic intersection/interpolation analogies with algebraic geometry.
   - Our implementation below stays in its degree-one case and proves all claims it asks children to use.

2. Ayush Kumar Tewari, *Point-Line Geometry in the Tropical Plane* (2020 preprint), §3, printed p. 3; §4, printed pp. 5–8. https://arxiv.org/pdf/2006.04425 ; record: https://arxiv.org/abs/2006.04425
   - Studies tropical point-line incidence, duality, and counting lines determined by points.
   - Explicitly separates ray intersections from stable intersections and discusses infinitely many lines through coaxial point pairs.
   - **Convention warning:** this paper uses max-plus and west, south, northeast arms. Reflect every coordinate through the origin to match the min-plus convention used here.

The detailed proofs, classroom designs, numerical examples, case table, and checking procedure below are independent derivations for this prototype. They are not copied exercises or claims of experimental educational validation.

## The exact object: one convention, no ambiguity

Write L(a,b) for the tropical line whose junction is (a,b). It is the union of these three **closed rays**, each including the junction:

- East: (a+t,b), t≥0.
- North: (a,b+t), t≥0.
- Southwest: (a−t,b−t), t≥0.

Directions stay fixed. A child may translate the figure, but may not rotate or reflect it while calling it the same min-plus family. A rising diagonal means slope +1; the actual arm from the junction points southwest.

For an all-nonnegative introductory scoring rule, use

    F(x,y) = min(x+b, y+a, a+b).

Mark a point only if at least two of these three scores are **jointly smallest**. The marked set is exactly L(a,b). The function’s graph would be a surface in three dimensions; the tropical line is the planar location of its creases, not the graph of F itself.

### Proof of the three-arm shape

All possible ties for the minimum fall into three cases:

- x+b = a+b ≤ y+a gives x=a and y≥b: the north ray.
- y+a = a+b ≤ x+b gives y=b and x≥a: the east ray.
- x+b = y+a ≤ a+b gives x−a=y−b≤0: the southwest ray.

At (a,b), all three tie. These cases exhaust the possibilities. A tie between the two larger scores does not qualify.

### Small exact seed

Use F(x,y)=min(x,y,4), giving L(4,4).

- (2,2): scores (2,2,4), qualifies; southwest arm.
- (4,8): scores (4,8,4), qualifies; north arm.
- (8,4): scores (8,4,4), qualifies; east arm.
- (4,4): scores (4,4,4), qualifies; junction.
- (6,6): scores (6,6,4), does **not** qualify despite a tie.
- (3,5): scores (3,5,4), does not qualify.

A movable-junction example without negative score values is min(x+3,y+5,8), which gives junction (5,3). Adding one common constant to all scores does not move the line; this follows because it preserves which scores tie for smallest.

## The main theorem: intersections, including every exception

Let A=(a,b) and B=(c,d) be the junctions.

1. If A=B, the lines are identical. Intersection = their entire three-ray union.
2. If a=c but b≠d, intersection = the north ray starting at the higher junction.
3. If b=d but a≠c, intersection = the east ray starting at the rightmost junction.
4. If a−b=c−d but A≠B, intersection = the southwest ray starting at the southwest junction.
5. Otherwise, the intersection consists of exactly one point.

For distinct junctions these three exceptional alignments are mutually exclusive. Thus two distinct lines never have zero common points, exactly two common points, a nonzero bounded common segment, or two common rays. The physical figure’s finite printed length is not the mathematical ray’s length.

### Recommended elementary proof: the rectangle between the junctions

Draw the axis-parallel rectangle having A and B as opposite corners. Children can reason with right/left, higher/lower, and equal grid steps; signed coordinates and slope formulas are unnecessary.

**Junctions in northwest/southeast positions.** The east arm from the northwest junction and the north arm from the southeast junction meet at the rectangle’s northeast corner. All other possible arm pairs either lie on different parallel lines or point away from one another, so there is no second meeting.

**Junctions in southwest/northeast positions.** Follow the northeast junction’s southwest diagonal until it first reaches the rectangle’s left or bottom edge. The left edge is on the southwest junction’s north arm; the bottom edge is on its east arm. If the rectangle is taller than wide, the diagonal first meets the left edge. If wider than tall, it first meets the bottom edge. In either case this is the only crossing: the northeast junction’s north/east arms cannot reach the southwest line, and the two southwest diagonals are distinct parallels.

**Equal width and height.** The northeast junction’s diagonal reaches the southwest junction itself, then continues along the southwest junction’s southwest arm forever. This is the diagonal shared-ray case.

**Zero width or zero height.** Junctions share a column or row. Their north or east rays respectively overlap, starting at the higher or rightmost junction. The other arms add no new common points. If both dimensions are zero, the two full lines coincide.

This proves existence, uniqueness in the ordinary cases, and all degeneracies. A useful independently derived refinement is that the two lines have exactly one common point inside the closed rectangle between their junctions, even in the shared-ray cases. For coincident junctions that rectangle is just one point. This refinement is not a claim that the full intersection is one point.

### Full algebraic teacher-audit table

Translate A to (0,0) and write B=(p,q). In the six open sectors:

| Conditions | Unique intersection |
| --- | --- |
| 0<p<q | (0,q−p) |
| 0<q<p | (p−q,0) |
| p<0<q | (0,q) |
| q<0<p | (p,0) |
| p<q<0 | (q,q) |
| q<p<0 | (p,p) |

Translate the result back by adding A. These six orders exhaust the possibilities when p, q, and 0 are distinct.

Boundaries:

- p=0, q≠0: north ray from (0,max(0,q)).
- q=0, p≠0: east ray from (max(0,p),0).
- p=q≠0: southwest ray from (min(0,p),min(0,p)).
- p=q=0: the whole line L(0,0).

### Checked numerical cases for six sectors and the boundaries

Keep A=(4,4):

| B | Full intersection |
| --- | --- |
| (6,8) | point (4,6) |
| (8,6) | point (6,4) |
| (2,7) | point (4,7) |
| (7,2) | point (7,4) |
| (1,2) | point (2,2) |
| (2,1) | point (2,2) |
| (7,4) | east ray starting (7,4) |
| (4,7) | north ray starting (4,7) |
| (6,6) | southwest ray starting (4,4) |
| (4,4) | entire L(4,4) |

Example score check at the first crossing: for A use min(x,y,4); for B=(6,8) use min(x+8,y+6,14). At (4,6), scores are (4,6,4) and (12,12,14), respectively. Both satisfy the two-minima condition.

## Inverse construction: find the junction from target points

A surprisingly productive child task is to fix a target P=(r,s), move the three-arm stencil so it contains P, and mark **every possible junction position**.

Those allowed junctions form a reversed three-arm figure:

- P on the east arm means junction (r−t,s): west from P.
- P on the north arm means junction (r,s−t): south from P.
- P on the southwest arm means junction (r+t,s+t): northeast from P.

Therefore a junction gives a line through both P and Q exactly when it belongs to the intersection of their two reversed figures. Reflecting the plane through the origin turns these reversed figures into ordinary min-plus line figures, so the proved intersection classification applies unchanged to their relative alignments.

Consequences for distinct P,Q:

- If not horizontally, vertically, or slope-1 aligned, there is exactly one junction and one line through them.
- Same row: all possible junctions lie on the west ray starting at the leftmost target.
- Same column: all possible junctions lie on the south ray starting at the lower target.
- Same rising diagonal: all possible junctions lie on the northeast ray starting at the northeast target.

Do not call the reflected junction-locus itself a min-plus tropical line of the original family: it has the opposite orientation. It is a construction tool, and an elementary version of point-line duality.

### Checked hidden-junction puzzles

- P=(2,2), Q=(7,5): unique junction (5,5). P is southwest, Q east.
- P=(2,2), Q=(5,7): unique junction (5,5). P is southwest, Q north.
- P=(2,7), Q=(6,3): unique junction (2,3). P is north, Q east.
- P=(2,4), Q=(7,4): every junction (a,4) with a≤2 works. There is no uniqueness.
- P=(4,2), Q=(4,7): every junction (4,b) with b≤2 works.
- P=(2,2), Q=(6,6): every junction (6+t,6+t), t≥0, works.

A three-point challenge with a checkable impossibility certificate:

- (2,2), (7,5), (5,8) all lie on L(5,5).
- (2,2), (7,5), (6,6) cannot lie on any one tropical line. The first two uniquely force junction (5,5), and (6,6) is not on that line (min(6,6,5) has only one smallest score).

If the two target points coincide, they impose only one condition: all junctions on the reversed three-arm figure through that point work. State “distinct points” in the joining theorem.

## Design possibilities considered before the writer stage

### 1. Make a line, and catch false ties

Children work on a large square grid with three score cards and colored counters. Start with min(x,y,4), sampling strategically rather than filling an entire large arithmetic table. They find the three arms and justify why the northeast diagonal is absent. Children choose a new junction, make a working three-score rule, and exchange it with a partner. The output is a geometric figure plus an explanation covering all points of each arm, not a completed table of sums.

### 2. Try to make two lines miss

Provide two transparent three-arm stencils with long arrowed arms and a square grid. Children can translate but not rotate them. They choose junctions to attempt zero, one, two, and infinitely many common points. They record the whole common set, distinguishing a crossing, a shared ray, and identical lines. Their failures at zero and two motivate a theorem; trials alone do not prove it.

### 3. Build and defend the crossing atlas

Children choose a fixed junction and draw the horizontal, vertical, and rising diagonal through it as **reference lines**. Those references divide possible positions of the other junction into six open regions plus boundary cases. Each group chooses representative pairs, predicts which arms meet, and explains using the junction rectangle. They deliberately test another group’s rule near a boundary. A completed atlas and repaired conjecture are substantial outputs. The six-case algebra table is for the teacher; the rectangle argument is the accessible proof.

### 4. Solve hidden-junction problems

Each child chooses two target points and moves the stencil to cover them. They must find all junctions, not stop at the first success. Constructing the reversed junction-locus for each target supplies a systematic method. Children create a unique-solution puzzle and a many-solution puzzle, then trade and check.

### 5. Invent a three-target challenge and publish a corrected theorem

Children create one possible and one impossible three-target placement, give a solution or impossibility certificate, and critique a false claim such as “different tropical lines share just one point.” They finish by stating the exact exceptions in their own diagram-supported language. A teacher can choose the joining theorem as the later/stretch destination if the full crossing proof already fills the available week.

The consequential child choices are where to place junctions and targets, what examples would refute a proposed theorem, how to classify boundary behavior, and how to certify uniqueness or impossibility. Avoid replacing those choices with only prescribed plotting.

## Meaningful younger entry

For younger children, use floor-grid tape, three colored straight strips with arrows, or a transparent template. The child chooses a target, moves the fixed-direction figure to cover it, and traces the junction’s possible locations. Then add a second target and compare “one place for the junction” with “lots of places.” They can also design a pair of lines sharing a whole arm and distinguish this from one crossing. This is genuine incidence and constrained motion without formal coordinates. Do not claim that manipulation alone establishes the all-configurations theorem.

## Practical and mathematical pitfalls

- A finite board can conceal ray continuation. Use arrowheads; tell children the arms continue. The rectangle argument guarantees a meeting within the box between the junctions, so keep that box visible.
- The points between grid dots count. Integer-junction examples have integer crossings here, but the geometry is not a set of grid dots only.
- Use a square grid so a one-right/one-up diagonal is unambiguous; do not refer to an arbitrary slanting arm.
- Minimum must be attained at least twice; any tied pair is insufficient.
- A single three-arm figure is one tropical line, not three independent ordinary lines.
- East, north, southwest is the min-plus convention. Max-plus pictures reverse all three directions.
- Distinct junctions exclude identical lines; distinct target points exclude repeated-point degeneracy.
- Never replace a shared ray with a single marked point while still calling it ordinary intersection.
- Do not interpret these as equal-angle Euclidean Y junctions or as three equal physical tensions. Tropical balancing concerns lattice-direction vectors (and weights for general curves), not equal-length unit vectors in three arbitrary directions.
- Generic incidence facts do not justify saying all tropical curves of given degrees meet in that many distinct points. That requires further machinery and is outside this prototype.
- The reverse-tripod construction should be named as a locus of possible junctions, not silently substituted for the original family of tropical lines.

## Research connection that earns its place

These are exactly the simplest tropical algebraic curves, and the child’s central problem is point-line incidence: which points lie on which lines, how lines intersect, and when point data determine a line. The shape originates in a minimum of affine functions. The reversal of “fixed line, varying point” into “fixed point, varying junction” gives an elementary instance of duality. Tewari’s paper shows that this incidence perspective genuinely leads to research questions about line configurations and counting, rather than merely attaching a fashionable label to arithmetic. The prototype does not ask children to prove the paper’s higher counting theorems.

## Research-stage verification reported

An independent exact-rational calculation intersected every pair of the three parameterized rays, rather than relying on plotting. It checked the six-sector formula for all 380 offsets (p,q) with −10≤p,q≤10 and p,q,0 pairwise distinct; each produced exactly the predicted singleton and no overlap. The ten listed numerical line pairs and all six hidden-junction examples above were also checked with the same ray-intersection calculation. The mathematical proof, not this finite check, establishes the theorem for all real junctions.


## Production status

This record supports an outline. Fresh student writer, independent adversarial and mathematical checks, revision, separate guide production, final page inspection and extracted-source reconstruction remain required. Research-stage computations check finite examples and do not replace independent verification of the eventual packet. Physical preparation and classroom piloting are unperformed.
