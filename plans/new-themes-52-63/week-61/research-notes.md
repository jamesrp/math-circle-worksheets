# Week 61 research: Triangles on a ball

Prepared October 4, 2026. Research and outline only; a fresh writer chooses student problems. Proposed theme, unpiloted. Actual ball/string/angle handling has not been rehearsed.

## Mathematical overview and limits

The mathematical surface is an ideal round sphere of radius R, with all routes restricted to its surface. A great circle is cut out by a plane through the center. Its arcs are the locally straight surface paths. Between two distinct nonantipodal points, the shorter great-circle arc is the unique shortest route. Antipodal endpoints admit infinitely many shortest semicircles, each of length pi R. A complete great circle or an arc longer than half its circumference is not a shortest route between its endpoints. Distinct great circles meet at two antipodal points, so complete great circles do not supply parallel lines. Latitude circles except the equator are small circles.

For a nondegenerate convex triangle contained in an open hemisphere, using the shorter great-circle arcs for its three sides, let alpha, beta, gamma be the smaller interior surface angles. With angles in radians,

`area = R^2 (alpha + beta + gamma - pi)`.

The positive area implies an angle sum greater than 180 degrees. If E_deg is the sum minus 180 in degrees, its fraction of the whole sphere is `E_deg/720`. The region chosen here has area less than a hemisphere. We exclude degenerate triangles, antipodal side endpoints, complementary regions, long-arc ambiguities, and self-crossing boundaries. A latitude-edged region is not a triangle for this theorem. An apparent angle in a flat perspective picture is not the actual angle between tangent directions on the sphere.

Petrunin and Zamora Barrera's *What Is Differential Geometry? Curves and Surfaces*, version 7, gives the spherical distance in Observation 2.22, printed/PDF pp. 24-25, antipodal shortest-path nonuniqueness in section 14B, printed/PDF p. 119, and the spherical excess proof in Lemma A.17, printed/PDF p. 178. Proposition 17.10, printed/PDF p. 143, places the formula in the spherical Gauss-Bonnet setting. [Primary scholarly reference, v7](https://arxiv.org/pdf/2012.11814v7). A preferred Berkeley course anchor was not located; this verified primary substitute is used with the coordinator's approval. No Berkeley teaching claim is inferred from it.

Children can experiment with physical strings and corners and conjecture the angle-sum contrast. The exact mathematical explanation uses center planes and an area covering argument. Measurement error or a convincing ball model alone does not prove the universal statement. General differential geometry, calculus, and parallel transport are later connections, not claimed prerequisites or results of the entry activity.

## Lunes and an explanation available to adults

A lune bounded by two great-circle semicircles meeting at angle alpha has area `2 alpha R^2`. Its fraction of the sphere is alpha/(2 pi), or alpha_deg/360: equal angular wedges between fixed poles have equal areas by rotation. This is a two-corner region with antipodal endpoints, not one of our three-corner triangles.

Extend the triangle's three sides to full great circles. At each pair of antipodal vertices select the two opposite lunes that contain the triangle and its antipodal copy. Their six areas total `4 R^2 (alpha+beta+gamma)`. Every other region of the sphere is covered once, while the triangle and antipodal triangle are each covered three times. Thus the same total is `4 pi R^2 + 4 area(triangle)`, proving the formula. The covering argument and its source are credited; any worksheet or guide diagram must be newly drawn and show the counted regions accurately. The argument is established mathematics, not a claim of an original theorem.

For a child-accessible special family, fix the north pole and two equator points separated by theta degrees along the shorter equator arc, with 0 < theta < 180. Its meridian corners at the equator are right angles; the north-pole angle is theta. The triangle is the northern half of a theta-degree lune, so its whole-sphere area fraction is theta/720. This directly verifies the excess formula in that family without formal radians or general six-lune bookkeeping. A general proof is a readiness-dependent adult conversation after enough concrete examples.

## Independently checked examples

Use theta = 30, 60, 90 or 120 only as checked background instances; the writer chooses tasks and examples. At theta = 0 the construction degenerates; at 180 the equator vertices are antipodal and the shorter side is no longer unique.

| Meridian gap | Triangle angles | Sum | Excess | Fraction of sphere |
|---:|---|---:|---:|---:|
| 30 degrees | 90, 90, 30 | 210 | 30 | 1/24 |
| 60 degrees | 90, 90, 60 | 240 | 60 | 1/12 |
| 90 degrees | 90, 90, 90 | 270 | 90 | 1/8 |
| 120 degrees | 90, 90, 120 | 300 | 120 | 1/6 |

On the unit sphere take N=(0,0,1), A=(1,0,0), B=(cos theta,sin theta,0). The tangent directions are projections of the other vertex vectors into the tangent plane. `check_examples.py` computes all three corner angles independently and checks the solid angle using `2 atan2(|det(N,A,B)|,1+N.A+A.B+B.N)`. The positive dot products with the vector (cos(theta/2),sin(theta/2),1) check that each tested triangle lies in an open hemisphere; convexity puts the shorter arcs and interior there too. Exact fraction results are stored alongside numerical coordinate checks in `math-checks.json`.

Equal-angle figures have the same fraction of spheres of different radii. Doubling R multiplies lengths by two and area by four. Keep fraction of a sphere distinct from an absolute area. A three-right-angle triangle exists here and has positive area; a proposed positive-area great-circle triangle with three 60-degree angles cannot satisfy the theorem under our conventions.

## Readiness and suggested page-band menu

Recommend one combined `students.pdf`: Grades 2-5 physical route/corner entry, followed by Grades 3-5 for concrete lune or sphere-fraction comparison where appropriate, and Grades 4-5 for the general excess-area explanation or an investigation using it. The writer may choose a different page count and grouping; this is not a task sequence. Do not promise K-1 theorem work merely because a child can handle a ball.

- Reading: adult can read labels and rules; children must keep both endpoints fixed and stay on the surface. The selected region and side convention need a visual reference.
- Arithmetic at entry: recognizing right angles, counting three corners, and comparing routes can suffice. Exact sums require addition through at least 300; degree labels require knowing 90 as a right angle. A corner made from paper is a comparison tool, not a reliable angle meter on every curved patch.
- Area continuation: equal slices and fractions of one whole sphere; subtraction of 180 and comparison with 720 if using the degree formula. Adults can record while children choose and check constructions. Radians, pi and R^2 can stay with adults unless children are ready.
- Reasoning: distinguish a curved view in space from a local surface path, complete circle from arc, and actual corner from its projected picture. Build several examples before interpreting a table or theorem.

For the current 3333 table provide two ball kits; for 445 use one kit with rotating builder/checker/recorder. All three children should manipulate and make mathematical choices. The parent-led KK11 table needs another suitable existing activity or supported exploration explicitly outside the claimed core; the organizer should decide the session arrangement. The current eleven-child roster and three anchored adults come from `worksheet-workflow/context.md`, not the older seven/ten-child plan snapshots.

## Launch, materials and physical gate

After the customary movement time, let children explore a ball and string briefly. A short demonstration fixes two practice points, shows a string touching the surface between them, changes the surface route while keeping endpoints fixed, and distinguishes a lifted chord. Show how a paper corner compares tangent directions at a marked intersection on the actual model. This is a legal-action/convention launch, not a demonstration of the three-right-angle discovery. Use a non-task worked visual before any unfamiliar sphere-to-record conversion; diagrams should match the ball's labels and visible/hidden arcs.

The outline specifies balls about 15-20 cm in diameter, stable supports, 80 cm flexible strings, removable markers and a paper right angle. A globe or model with an accurately marked equator and meridians can support exact intended configurations. On a plain ball, an elastic loop that seems taut may be held by friction or slip into a smaller circle. A string pulled between points may lift into a chord; a flat protractor laid over the ball does not automatically read a surface corner. These are operational constraints, not reasons to remove the mathematics.

Before use, rehearse with the actual kit: stable ball handling, fixed-point string contact, keeping the shorter arc, crossing markers, showing hidden arcs, comparing one known right angle, and marking two meridians at a known separation. For a lune demonstration check that the same poles and chosen smaller wedge stay fixed. Test removal of marks. **All of these pretests remain unperformed.** Digital coordinate checks cannot establish physical fit or a child's independent control.

Proposed pacing: five minutes of movement, four-five minutes of material action, 20-30 minutes of constructing/comparing surface figures, and an optional 15-20 minute area continuation or closing share. Ball-route work and excess-area work can be separate visits. Preparation is about 15-20 minutes only if the ball and angular reference are already suitable; sourcing or calibrating a model may take longer. This estimate is untested.

## Overlap and novelty boundary

Current `WEEKS-11-51.md` and `BONUS-AND-RETURN-VISITS.md` were read. Current Week 41 upper student PDF pp. 1-5 and facilitator pp. 1-2 were inspected for the actual portal and lift model; bonus pp. 1-3 extend orbits, tours and shortest periodic-grid routes. The square is glued by translations into a flat quotient torus. Its planar lifts classify winding, with no claim of a length-preserving paper torus in space. Week 61 instead studies the intrinsic geometry of a positively curved round sphere, actual surface shortest arcs and angle-dependent area. A ball is not a physical implementation of the Week 41 flat metric.

The atlas already has a curved-geometry strand: GA-23 in `plans/atlas/families/geometry-analysis.md`, “What changes when an arrow travels around a sphere?”, uses the octant triangle and variable-longitude family for parallel transport. Its checked 90-degree route has area pi/2, and the source is the same Petrunin/Zamora text. **The octant and lune relation are therefore prior library mathematics.** Week 61 is a new elementary theme development centered on shortest arcs, triangles and excess area, not a claim that spherical geometry has never appeared in the repository. It should not duplicate the transported-arrow investigation or import its executive demands into the entry page. Weeks 38 seams/cuts and 39 road detours provide further surface/path context; they do not establish the spherical metric theorem.

Year-one DOCX handouts include plane billiards (Handouts 10, Problems 10.2-10.7; Handouts 11, Problems 11.4-11.5), and the pattern-block handout compares area and perimeter. These are concrete geometry precedents, not spherical triangle evidence. No spherical route or excess problem was located in the extracted eleven-handout text. That is a scoped text comparison; file presence does not establish which returning children used a task.

## Pedagogy evidence and proposed adaptation

The organizer's first-year materials and README support handling materials and learning by doing. *Pattern Block Exercises - Google Docs*, PDF p. 1, gives five minutes of free play before pairs/trios. The current context reports successful tiling and the paper-lamp rule failure. **Our inference:** children should see and enact “stay on the surface,” fixed endpoints, and actual corners before interpreting a perspective drawing or formula. This inference is not an observed result from a sphere lesson.

*Math Circle by the Bay*, printed p. viii / PDF p. 9, explicitly chooses themes with deep mathematical context; pp. ix-x / PDF pp. 10-11 report manipulatives, independent attempts, changes of pace/depth, and extra challenges. **Our adaptation:** a concrete route entry can grow into a serious area theorem over more than one visit; all children need not finish a covering proof.

Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 3, “At the lesson,” item 1 (`OEBPS/part0013.xhtml`), describes children's attempts and explanations before an organizing table. Lesson 7, “At the lesson,” item 2 (`part0017.xhtml`), records enthusiastic K'nex polygon construction and that an earlier triangle experiment was not recalled. Lesson 8, item 2 (`part0018.xhtml`), records writing/coloring delays. **Our adaptation:** let the ball work create the question, keep optional notation with adults, and provide records rather than lengthy copying. The book does not validate this spherical model; its triangle anecdote is a particular observation, not a general ban on triangle investigations.

## Provenance and workflow

Reference: `external-resources/new-themes-52-63/week60-61/petrunin-zamora-differential-geometry-v7.pdf`, from the URL above; manifest records version and checksum. No source figures or prose are copied into deliverables. Statements, checked coordinate examples, proposed materials and future graphics are newly authored around established mathematics and credited library precedents. The source's CC BY-SA 4.0 notice is recorded as source metadata; no copied source asset is planned.

Root `REPUBLISHING.md` was read without change. Future portable packages omit workflow prompts, borrowed exemplars, downloaded texts, render caches and reference-PDF duplicates. A source citation or this limited comparison is not a publication clearance or exhaustive independence audit.

Outline: `outline.md`. Run: `tmp/worksheet-runs/week-61-new-v1/`. Follow root `STAGE-ROUTING.md` for one combined packet, honest page bands, and fresh writer/critic/math/reviser stages with unchanged generator. The independent math reviewer should check every depicted arc, chosen region, triangle assumptions, area fraction and meaning of its angles. Subsequent guides must open with the actual mathematical facts, conventions, limits and band map before individual solutions. Research-stage checks do not constitute student-PDF rendering, source-ZIP rebuild, a physical rehearsal, or a pilot.
