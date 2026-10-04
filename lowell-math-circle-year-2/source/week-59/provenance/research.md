# Week 59 research: constant width beyond circles

Prepared 4 October 2026. New, unscheduled library theme; research and outline only. Digital calculations do not establish physical readiness. All cutout/ruler/compass pretests, timing and classroom piloting are unperformed.

## Mathematical destination

For a compact convex filled shape K and a unit direction u, width is the distance between two parallel lines, perpendicular to u, that enclose and touch K. In adult notation it is max(x·u)−min(x·u), over points x in K. The distance is measured perpendicular to the two lines. It is not a chord through a marked center, the distance between arbitrary boundary points, a radius, a bounding-box diagonal, or the boundary's length.

A circle of diameter w has width w in every direction. A noncircular Reuleaux triangle does too. An ellipse with unequal axes and an ordinary equilateral triangle provide contrasting controls. Several ruler measurements can suggest constancy or disprove it, but do not prove a statement about all orientations. The eventual adult guide must open with these facts and limits before individual solutions.

## Independently authored all-direction proof

Start with equilateral ABC of side w>0. Let K be the intersection of the three closed disks of radius w centered at A,B,C. Its boundary is three **minor 60-degree arcs**, each centered at the opposite vertex. It is convex because each disk is convex. This specifies the intended shape precisely; a casually rounded triangle need not have constant width.

Take coordinates A=(0,0), B=(w,0), C=(w/2,√3w/2). First let u point from A in any direction between AB and AC, inclusive. Put P=A+w u. It lies on the opposite arc BC: its distances to B and C are at most w, since its angle from each of AB and AC is at most 60 degrees. For every x in K, |x−A|≤w, so x·u≤w, with equality at P. This supplies the upper support line.

For the lower support, membership in the disks centered at B and C gives x·B≥|x|²/2≥0 and x·C≥|x|²/2≥0, by expanding their squared distances (|B|=|C|=w). A direction u between AB and AC is a nonnegative combination of B and C. Hence x·u≥0 for all x in K. Equality holds at A. The parallel line through A is therefore a support line, and the two support lines are w apart. Geometrically, the tangent constraints at A keep the whole shape on the correct side of that line; the opposite line is tangent to a radius-w arc, perpendicular to AP.

Repeat this argument at B and C. The directed sectors from a vertex toward its opposite arc cover angles [0,60], [120,180], [240,300] degrees. Their opposite directions cover the remaining three sectors. Width is unchanged by reversing direction, so every support-line orientation is covered, including endpoints. This proves constant width, rather than relying on a few symmetry positions. For children the radius/perpendicular picture is the explanation destination; coordinate expansion and sector coverage remain adult proof support.

The construction and theorem are supported by [Francis E. Su et al., Reuleaux Wheel, Harvey Mudd College Math Fun Facts](https://math.hmc.edu/funfacts/reuleaux-wheel/), the construction/constant-width paragraph and “The Math Behind the Fact.” That university page states the fact and suggests the investigation; it does not supply the full support-sector proof above. The proof here is an independently authored derivation, not a quoted university proof. A proposed Nebraska university page could not be fetched and is not cited as consulted.

## Controls, quantities and axle-height limit

For the proposed w=60 mm models:

* Circle radius 30 mm: every width is 60 mm.
* Ellipse semiaxes 30 and 20 mm: width in normal direction θ is 2√(900cos²θ+400sin²θ), ranging from 40 to 60 mm. Its two axis positions already disprove constant width. No trigonometry is needed for the physical entry.
* Ordinary equilateral triangle side 60 mm: support width ranges from altitude 30√3≈51.962 mm to 60 mm. Retain this control rather than assume children already know why the curved triangle is surprising.
* Reuleaux triangle width 60 mm: the construction arc radius is **60**, while the comparison circle radius is **30**. Confusing those radii is a common diagram error.

The centroid O of the underlying equilateral triangle is w/√3≈34.641 mm from a vertex, and w−w/√3≈25.359 mm from the midpoint of the opposite arc. These two radii are unequal. In two orientations resting against a horizontal support line, the marked centroid has those two heights above the line. Thus a wheel with a fixed axle at that point rises and falls; constant total support width does not imply constant axle height. By contrast, the separation of two parallel planes embracing an ideal cylinder of that cross-section stays w when orientation changes. This is an ideal roller geometry statement, not a claim that a thin cardboard cutout will roll smoothly or carry a platform. More generally, if a fixed point has the same distance to every support line in every direction, the convex shape's support function about it is constant, so the shape is a circle.

Optional adult/upper comparison: the three boundary arcs each subtend 60 degrees on a radius-w circle, so together they are half of that circle's circumference: perimeter 3·(πw/3)=πw. That matches the circumference of a circle of diameter w, about 188.496 mm at w=60. Width, radius and perimeter remain different quantities. The general Barbier theorem is additional source background; the three-arc calculation proves the equality needed here directly. Arc fractions are an optional readiness gate, not a Grade 2 entry demand. Area-minimization and arbitrary odd-polygon constructions are omitted.

No square-hole or fixed-center rotation claim is a worksheet kernel. The HMC source itself describes rounded corners in its square discussion; it does not justify promising an exact square hole. No mechanical demonstrations have been rehearsed.

## Independent digital audit

`verify_math.py` computes linear extrema on the actual circular arcs. For each direction it includes vertices and the radial maximum of each generating circle only if that point lies in all three disks. An arc's linear maximum occurs at such a point or an endpoint. This is stronger than measuring a sampled polygonal boundary, but the 1,440 tested orientations still constitute a finite check, not the universal proof.

`math-checks.json` records Reuleaux widths from 59.999999999999986 to 60.000000000000014 mm, maximum floating error 1.42×10⁻¹⁴ mm; ellipse 40–60 mm; triangle about 51.962–60 mm; sampled marked-centroid heights about 25.359–34.641 mm. The mathematical proof and two exact radial witnesses justify the claims, while the program catches construction/example mistakes. Future writer-selected diagrams/tasks require their own audit.

## Inspected primary resources and adaptation limits

* [ThinkMaths, Shapes of constant width](https://think-maths.co.uk/resources/shapes-constant-width/) labels the resource KS3,4,5. Its practical investigation uses parallel card edges; the page notes a construction-sheet correction uploaded 23 June 2018. Our proposed elementary route is an unpiloted simplification, not the source's validated age range.
* [Shapes of Constant Width, PDF p.1](https://think-maths.co.uk/wp-content/uploads/2023/03/Shapes-of-Constant-Width_0.pdf): Activity 1 compares the circle and equilateral triangle using two parallel straight edges; Activity 2 contrasts three flawed rounded constructions. These are actual source activities. We retain the mathematical idea of contrasting controls, not source prose or diagrams.
* [Constructing Shapes of Constant Width, PDF p.1](https://think-maths.co.uk/wp-content/uploads/2023/03/Constructing-Shapes-of-Constant-Width.pdf): three radius-side arcs from equilateral vertices. The two-page source also has extended odd-polygon constructions, which we do not assert for arbitrary polygons or ask young children to execute.
* Source cutout and triangle-construction PDFs were downloaded and visually inspected with the above pages. They remain external reference files; author-created compass templates, controls, arcs, labels and support lines must be drawn afresh. HMC university source was read and saved as HTML. All URLs and hashes are in `external-resources/new-themes-52-63/week58-59/manifest.json`.

Root `REPUBLISHING.md` was read. Borrowed figures, prose and downloaded references must not enter authored student pages or source ZIPs. The unchanged generated prompts include existing borrowed exemplars solely as local workflow records.

## Teaching evidence, then our inference

Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 6, “At the lesson,” “Experiments with triangles and quadrilaterals” (`OEBPS/part0016.xhtml`), reports children following angle-cutting experiments without much enthusiasm although parents enjoyed them. The author's explanation in terms of insufficient prior geometric comparisons is a **hypothesis**, not an observed causal fact. Our inference is to let children discover changing widths on the triangle/ellipse before the noncircular constant-width claim; do not make adult surprise the task.

Givental et al., *Math Circle by the Bay*, Preface printed vii–ix (PDF pp.8–10), describes deep themes, interaction, independent solutions, clear statements and available manipulatives. Our adaptation gives children the measurement/rotation choices and adult assistance with straight-edge parallelism, rather than requiring simultaneous angle notation, compass handling and a data table at entry.

First-year actual `Handouts 3.docx`, Problems 3.4–3.7, asks children to build/compare a hexagon and explore symmetry with tiles. `Pattern Block Exercises.pdf`, p.1 Problem 1, explicitly flags that the paper may not match the material scale. Those are precedents for handling/contrasting shapes and checking scale, not evidence that this session landed. The current workflow context's reported pattern-block success and lamp-rule difficulty support physically visible legal contact; that is an inference for this unpiloted route.

## Honest bands and physical constraints

One combined `draft/students.pdf` then `final/students.pdf`, under `../STAGE-ROUTING.md`. Physical measurement/rotation entry **Grades 2–5**; support-radius explanation and compass construction **Grades 3–5** when ready; perimeter fractions optional older continuation. No fabricated K–1 page. A younger child can handle a shape with an adult, but the ability to maintain parallel supporting edges and make a useful comparison is the mathematical gate. Adult reading alone cannot replace it. Millimeter subtraction, perpendicular gap, and an unfamiliar support-contact convention need an original non-task input → jaws touching both sides → measured gap visual before first use.

Five pair kits: each has pre-cut flat 0.5–1 mm stiff-card models of a 60 mm diameter circle, 60×40 mm ellipse, 60 mm-side equilateral triangle and 60 mm-width Reuleaux triangle; two straight 300 mm rulers or card rails with a 100 mm straight contacting edge; a 150 mm measuring ruler; a reusable 10 mm square-grid mat at least 200×200 mm; two movable right-angle guides to keep the rails parallel; pencil and blank paper. Mark the underlying triangle centroid on a second Reuleaux copy for the upper comparison; it is a marked point, not a circular center. Three tables each have one adult. The upper third child can referee contact and rotate roles. Provide six adjustable compasses and six 60 mm equilateral templates for optional construction; adults manage points/scissors and pre-cut lower models.

Print US Letter at 100% with a measured 100 mm bar; all geometry uses equal x/y scales and true circular arcs. A cutout is a separate material, not a compact worksheet picture. For measurements, allow translating the shape while it turns and adjusting both rails; do not pin its center. Edges must stay parallel, barely contact without squeezing, and enclose the whole shape. Measure the shortest/perpendicular gap, keeping one reference edge and units fixed. The grid/right-angle guides make this operational; an adult can assist alignment while children choose orientations. Nearest-millimeter records and cut-edge error are experimental limitations, not a certified instrument error bound. Exact fit requires an actual print/cut trial.

Unperformed physical pretests: printed 60/100 mm dimensions; cutout smoothness and visible contact; right-angle rail setup; whether a 60 mm Reuleaux model stays within an agreed ±1–2 mm trial tolerance across turns; ellipse/triangle contrast distinguishability; compass radius stability; younger retention of parallel-gap meaning; timing and piloting. No platform, axle or drill experiment is claimed tested. Keep useful upper proofs even if the first visit stops with measurements.
