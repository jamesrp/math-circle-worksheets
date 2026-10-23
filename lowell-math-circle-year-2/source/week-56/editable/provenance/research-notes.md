# Week 56 research: Corners of a solid

Research/outline stage, October 4, 2026. This is a new theme, not a scheduled meeting or a piloted activity. Student problems are left to the fresh writer. Read [the outline](../../../../plans/new-themes-52-63/week-56/outline.md) and [direct stage routing](../../../../plans/new-themes-52-63/STAGE-ROUTING.md) together. README, AGENTS.md, workflow README/template/context/generator, both current theme indexes and REPUBLISHING.md were read. No earlier packet or prompt block was edited.

## Mathematical destination and limits

For a finite convex polyhedron, the boundary is a sphere and **V-E+F=2**. More generally the same result holds for a finite cell decomposition of a topological sphere with disk faces, whole-edge attachments and manifold neighborhoods. Each ordinary closed-surface edge is incident to two faces. The numbers refer to the assembled object, not to the separated cut edges of a net, the number of polygon corners before assembly, or a projection's crossing points. A genuine convex vertex has positive defect **360 degrees minus its incident planar face-angle sum**; subdivision points lying in a face or along an edge can have zero defect. Summing all defects gives **720 degrees**. Planar turning, 3D dihedral angles and angular defect are different quantities.

An open box is a disk (alternating count 1). A cylinder band and Möbius band have boundary and do not inherit the closed-sphere formula. A torus has count 0 and total signed defect 0, but no arbitrary donut drawing or bent band establishes a valid face-edge-vertex cellulation. The proposed core needs only checked closed convex solids. For general closed polygonal surfaces, sum(defect)=360(V-E+F) follows by the same face-angle sum argument; concave vertices can have negative defect. These generalizations are adult limits, not a reason to add a difficult torus construction to the first visit. A local fan with positive deficit need not be globally completable into a convex polyhedron.

Children should discover shared incidences and an invariant under changing/subdividing a surface, then connect the folded corner gaps to a fixed global total. The discovery is new to this collection even though Euler's formula and discrete Gauss-Bonnet are established mathematics. Numerical checks are experiments; a pattern inferred from them is a conjecture; the reductions below explain the general result.

## Proofs and independent small checks

Remove one face from a convex polyhedron and use a Schlegel projection through that face to view the remaining surface as a disk. Its graph is connected and planar. Delete edges on cycles, each time merging two regions (one may be the unbounded outside region); E and the number of bounded faces both decrease by 1. Stop at a tree, whose E=V-1 and bounded-face count is 0. Thus V-E+F_disk=1. Replacing the removed face adds one face and gives 2. No bridge is deleted in the cycle step. This is a reduction argument, not a claim that simply flattening any physical paper net preserves the assembled incidences.

An n-gon has planar angle sum 180(n-2), as a triangulation into n-2 triangles shows. Across all faces, the side incidences total 2E. Thus all face-angle contributions total 180(2E-2F)=360(E-F). Subtracting them from 360 once at each vertex leaves 360(V-E+F)=720. Cutting a polygon face by a diagonal preserves the angle sum at old corners while adding E and F together. Inserting a vertex inside a face splits its full turn among the new faces and creates zero defect; inserting one along an edge similarly has total incident angle 360.

| Model | V | E | F | Defect distribution, degrees |
|---|---:|---:|---:|---|
| Regular tetrahedron | 4 | 6 | 4 | 4 vertices at 180 |
| Cube | 8 | 12 | 6 | 8 at 90 |
| Regular octahedron | 6 | 12 | 8 | 6 at 120 |
| Right equilateral triangular prism | 6 | 9 | 5 | 6 at 120 |
| Square pyramid with equilateral side faces | 5 | 8 | 5 | 4 base vertices at 150; apex at 120 |
| Cube, every square divided by one diagonal | 8 | 18 | 12 | 8 at 90; no new curvature |

The square pyramid may be realized with unit base edges and apex height sqrt(1/2); base face angle 90 plus two triangle angles 60 gives defect 150. The apex has four 60-degree angles and defect 120. This is a useful check that defects need not all be equal. With regular polygons as faces and the same q faces at every genuine convex vertex, q*180(n-2)/n<360 restricts candidates to (n,q)=(3,3),(3,4),(3,5),(4,3),(5,3). Explicit models establish existence; the inequality alone does not.

[verify-kernels.py](../../../../plans/new-themes-52-63/week-56/verify-kernels.py) reconstructs edges from face cycles, checks that each appears twice, computes each incident face angle from 3D coordinates using dot products, and checks the total. [kernel-checks.json](../../../../plans/new-themes-52-63/week-56/kernel-checks.json) records the results. This checks example geometry independently of substituting the known total; it is not a classroom rehearsal or a proof for all surfaces.

## Sources and provenance

1. **Keenan Crane, Discrete Differential Geometry: An Applied Introduction**, [author's CMU page](https://www.cs.cmu.edu/~kmcrane/Projects/DDG/) and [notes](https://www.cs.cmu.edu/~kmcrane/Projects/DDG/paper.pdf), downloaded October 4. Exercise 2.1, printed p.22/PDF p.23, explicitly contrasts disk count 1, sphere count 2 and genus. Exercises 5.9-5.10, printed pp.95-96/PDF pp.96-97, define defect and state the discrete Gauss-Bonnet identity. Relevant PDF pages were extracted and visually inspected. The elementary polygon-angle proof above is our derivation. We explicitly require no boundary for this defect formula; Exercise 5.10's abbreviated statement does not spell out that requirement.
2. **Vicky Neale, NRICH, Euler's Formula**, [original Cambridge article](https://nrich.maths.org/articles/eulers-formula), published February 1, 2011. The connected planar graph theorem counts the outside face; its edge-removal proof and final polyhedron discussion were read. The final rubber-stretching picture is identified by the author as intuition, not a proof. We retain the precise convex/sphere assumptions rather than treating its informal “polyhedra” wording as universal.
3. **Thomas F. Banchoff, Beyond the Third Dimension**, [Chapter 5 section 2](https://www.math.brown.edu/tbanchof/Beyond3d/chapter5/section02.html), author's Brown-hosted book. It compares triangles/squares/pentagons around corners and explains why a full flat turn cannot form a convex corner. This is the precedent for a physical local fan entry; our exact solids, wording and future figures are new adaptations. Chapter 6 section 3, [Schlegel diagrams](https://www.math.brown.edu/tbanchof/Beyond3d/chapter6/section03.html), was also read as projection context.

Downloaded sources and URL/hash metadata are in `external-resources/new-themes-52-63/week56-57/`. No third-party book or workflow exemplar should enter the deliverable ZIP. Attribution identifies a precedent; it does not imply permission to republish downloaded originals or validate our adaptation.

## Novelty against inspected current material

Both WEEKS-11-51.md and BONUS-AND-RETURN-VISITS.md were searched and read for neighboring themes. Current PDFs, not archive copies, were text-extracted; all pages of relevant upper and bonus packets were rendered as contact sheets in `tmp/new-themes-52-63-research/week56-57/` and inspected.

- **Week 26 bonus p.2, Problem 3**, and adult p.3: outward/inward planar corners obey C-R=4(1-H), with a no-diagonal-pinch restriction. Bonus pp.3-4 concerns exposed cube area from footprints and height differences. Week 56 uses closed polyhedral surface incidence and 3D corner defect, not another planar turning count or cube-surface optimization.
- **Week 37 upper pp.1-5** studies labeled tetrahedra, rotation/mirror equivalence and 12 rotations; **bonus p.2, Problem 2** studies two-color tetrahedral edges, and p.3 colored right-angle arms. The same convenient solid may recur as a manipulative, but Week 56's face-edge-vertex relation and total curvature are different questions. No chirality classification or rotational enumeration is repeated.
- **Week 38 upper pp.1-6** and bonus pp.1-3 trace boundary components, cuts and seam reversal in bands. Week 56 restricts the core to closed sphere surfaces and explicitly contrasts boundary surfaces. It does not recast seam tracing as an Euler calculation.
- **Week 31** and **Week 48** were inspected for the paired Week 57 investigation; none of their examined tasks supplies a closed-polyhedron defect investigation.

This is a specific novelty comparison with the closest released themes, not a claim that the classical mathematics was invented here. Actual attendance/use is still unknown beyond the use records; library numbering does not establish previous child exposure.

## Pedagogy and operational fit

**Direct source evidence.** Givental, Nemirovskaya and Zakharevich, *Math Circle by the Bay*, printed pp.viii-x (PDF pp.9-11), read locally, advocate themes that extend into deeper mathematics, a bag of manipulatives, repeated chances to improve explanations and different pace/depth with shared themes; they decline universal duration estimates. Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 7, “At the lesson,” item 2 (`OEBPS/part0017.xhtml`), read from the local EPUB, reports enthusiastic free polygon construction with K'nex. This is evidence for handling/construction time, not for successful polyhedron-defect teaching. Item 1 distinguishes an observed game result from a rule/strategy explanation and reports the group was not ready for a triangulation argument.

**First-year precedent.** The organizer's *Handouts 4.docx*, Problems 4.2-4.5, was read: physical tiling followed by obstruction and symmetry classes. Its note about approximate print fit warns us to state dimensions and physically check cutouts. *Handouts 1.docx* includes figurate arrays and scaling triangular tiles. Neither is evidence that these children have learned Euler/defect. README and current workflow context report successful block handling and failed paper-only lamp rules; those are organizer-reported observations. Avoid placing the legal incidence convention only in a child's memory.

**Our proposed adaptation.** Keep one adult at each fixed table. Children first handle whole solids, mark what they have counted, and build corner fans whose edges/tape visibly preserve face incidence. A whole-group launch touches an actual shared edge and vertex before diagrams appear. K-1 may make choices among flat and folded fans with adult recording; if the adult has to make every comparison, this is not an independent younger investigation. Main Grades 2-5 entry needs short adult-read directions, counting to roughly 20, and preserving one model while checking it. The 720-degree route needs whole/half turns, multiples of 60/90 and subtraction, or physical paper sectors with adult arithmetic. Symbolic Euler reduction and arbitrary n-gon sums are upper continuations.

An initial 20-35 minutes on models or fans is a planning estimate; a later visit can pursue why the global sums agree. Count sheets should be recoverable from sticker-marked models, and participants should not maintain three live tallies while folding. Prepare three sets of four small solids and five fan sets; provide cut assets rather than a shopping requirement. Exact material fit, preparation duration, tape stiffness, hidden-face recognition, staffing success and classroom timing remain **unrehearsed and unpiloted**. Record what a child touched/built/said separately from interpretations about readiness, and save where each pair wants to resume.

Independent-review correction (October 4, 2026): deleting a boundary cycle edge can merge a bounded face with the outside region. The reduction and bounded-face decrement remain valid; the former wording incorrectly required both merged regions to be bounded.
