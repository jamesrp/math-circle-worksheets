# Week 61 independent mathematical review

Reviewed October 4, 2026. This is the fresh math-review stage only. No student, guide, source, research or workflow files were changed. The actual deliverable is the combined six-page `draft/students.pdf`; the direct routing overrides the generic three-packet quotas. `research.md` is absent; the actual Week 61 research file is `plans/new-themes-52-63/week-61/research-notes.md`, which was read instead.

**Result: the numerical mathematics is correct, but revise the upper representations on pages 5–6 before release.** The critic's proposed repairs preserve a valid general six-lune argument. No impossible angle record, wrong area fraction, incorrect antipode, or wrong chosen lune was found. The current region map and first-use covering convention do not yet support a recoverable mathematical record. Do not remove the universal explanation or dilute it into fitting a formula to three examples.

Read: root `AGENTS.md`, `README.md`, `REPUBLISHING.md` unchanged; direct `STAGE-ROUTING.md`; this run's `PROMPT.md`, `CRITIC-MATH.md`, `review.md`; all seven `draft/src/` files; the actual research notes, research checker and output. The actual local primary text, Petrunin and Zamora Barrera, *What Is Differential Geometry? Curves and Surfaces*, v7, was checked at printed/PDF pp. 24–25, 119 and 178. Its distance, antipodal exception and six-slice excess argument match the claimed source references.

## Located findings and smallest repairs

### M1. Grades 4–5, page 5, Problem 5: the eight-region drawings omit visible region identities

The task asks, **“How many of the three pairs cover each of the eight regions?”** The front diagram labels regions 1, 2, 3, 5; the back labels 4, 6, 7, 8. These are correctly placed labels, but they are not a complete identification of the visible regions.

Independent half-space analysis of the actual camera gives:

| View | Cells with visible surface interior | Labels supplied | Unlabelled visible parts |
|---|---|---|---|
| Front | 1, 2, 3, 4, 5, 6, 7 | 1, 2, 3, 5 | 4, 6, 7 |
| Back | 2, 3, 4, 5, 6, 7, 8 | 4, 6, 7, 8 | 2, 3, 5 |

This is an exact visibility conclusion from the cell's three generating vertex rays, rather than a random sample. A cell has a visible interior patch when at least one ray has positive dot product with the eye direction. The author's centre-label test only labels four of those seven cells. The actual rendered page shows the omitted slivers. Dashed projections are hidden-surface arcs, not extra visible-surface region boundaries; they must not be counted as subdivisions of the front surface.

**Smallest repair:** label/call out every visible component with the same region ID across views, or use complementary hemisphere views normal to one side plane. For the octant, a pole-on view gives four complete quadrants per view. For the 80° triangle, using the oriented normal to side BC likewise gives exactly cells 1–4 on one hemisphere and 5–8 on the other, with unequal cells. This replacement is mathematically valid. It requires explicit labels at limb vertices (the existing strict `view.z(v)>0` label rule omits them) and omission of hidden arcs that project onto the same visible boundaries. Inspect the repaired rendered drawings; a valid camera alone is not a legibility check. Preserve one eight-entry record for the same ball.

### M2. Grades 4–5, page 5, shared lune-pair example and Problem 5: identify the two defining circles and the meaning of one count

The definition says, **“At each corner, choose the lune containing the triangle and the opposite lune. Together they are a lune pair.”** The finished example is captioned **“Pair at A: front of ball” / “Same pair: back of ball.”** It is geometrically correct: the blue set is precisely the lune bounded by circles AB and AC that contains the triangle, together with its antipodal lune. All three full circles currently have the same line style. No selected-two-circle intermediate or marked-patch count precedes the “Pairs covering it” row.

**Mathematical interpretation that must be shown:** at A, use the two side circles AB and AC, not BC. One selected pair contributes either 0 or 1 to any region interior. Its two opposite lunes have disjoint interiors; they do not give two contributions to the same patch. Counts at their common pole/boundary points are irrelevant to area and should not be used as the sample patch.

**Smallest repair:** keep the existing non-task 80° geometry and add the input triangle/corner A → selected full circles AB and AC → opposite-lune pair visual. Mark one interior patch and show its single-pair entry 1, explicitly for the one pair currently marked. Matching circle/patch labels should persist through the three views. This reveals a convention, not the main three-pair tally. Leave the remaining memberships to children. The construction is valid for both an acute and an obtuse interior corner under the shared rules; it must select the containing interior wedge, rather than automatically selecting whichever wedge looks narrower in projection.

### M3. Grades 4–5, page 6, Problem 6: supply the unequal-cell covering model before asking for the universal explanation

Problem 6 asks, **“Use the six lunes to find the fraction of the ball covered by each triangle. Find a rule using the sum of the three corners, and explain why it works for any triangle under our rules.”** The three exact angle records are correct and realizable. Their diagrams currently show only the target triangles. The preceding full covering task uses equal octants, so it does not by itself demonstrate why the count survives unequal cells.

**Proposed repair checked independently:** reuse the 80°/80°/80° full-circle arrangement as a genuine second covering investigation. All eight cells have positive area. Regions 1 and 8 each occupy 1/12 of the sphere; each of the other six occupies 5/36. Thus these cells are substantially unequal. Their pair-count record is still `[3,1,1,1,1,1,1,3]`. Each opposite-lune pair occupies 4/9, so all six counted lune areas total 4/3 spheres. Those values satisfy `4/3 = 1 + 4(1/12)`. The blue pair already printed on page 5 is the correct pair for this reuse; a recoverable map and counts still need to be added.

**Smallest repair:** provide the non-octant model with extended circles, antipodal copy, stable cell IDs and a single pair-membership record before the universal question. Keep the three exact angle records as applications. The general explanation must use the structural membership reason below and antipodal equality of area; unequal-cell experimental checking alone is not a proof. Update readiness notes to require counted overlapping area and the distinction between examples and a universal explanation. The proposed repair is mathematically sound but has not yet been authored or rendered in this stage.

### M4. Grades 2–5, page 3, shared meridian convention: endpoints alone do not imply the claimed right angle

The page says, **“A meridian goes from N to the opposite pole. Its corner with the equator is a right angle.”** The displayed meridian triangle and every intended calculation are correct. Read literally as an endpoints-only definition, however, a curved pole-to-pole path need not meet the equator at a right angle. For example, with colatitude t, the surface path `(sin t cos(kt), sin t sin(kt), cos t)` joins the poles, and at the equator its tangent has a nonzero component in the equatorial direction whenever k is nonzero.

**Smallest repair:** “A meridian is a great-circle semicircle from N to the opposite pole.” Its plane then contains the polar axis, so it meets the equator orthogonally. No new task or longer definition block is needed.

The page 2 positive-area condition could also be made explicit for agreement with the notes, but no counterexample satisfying all its existing rules was found: a distinct collinear triple in an open hemisphere has a 180° middle corner and is already excluded. Treat adding “encloses some surface area” as precision, not correction of a demonstrated false answer.

## Independent outcomes by actual page/band

| Page / band | Task and verified outcome |
|---|---|
| 1 / Grades 2–5 | Compare shortest routes for close, far nonopposite, and opposite marker pairs. Only the opposite pair admits different shortest routes; in fact it admits infinitely many great-circle semicircles of length πR. The worked P/Q arc spans 95°, rather than the complementary 265°, on their correct centre-plane circle. |
| 2 / Grades 2–5 | Maximize right corners. Three are possible: an octant has corners 90°,90°,90° and occupies 1/8. It lies strictly in the hemisphere centred on N+A+B, despite its vertices lying on the usual equator/pole reference. The first-use two-tangent example really has a 135° surface corner. |
| 3 / Grades 2–5 | Vary equator endpoints with N fixed. For the shorter gap θ in (0°,180°), corners are θ,90°,90° and area increases with θ; fraction θ/720. The displayed 110° example realizes those angles and selects the smaller region. Meridian wording needs M4. |
| 4 / Grades 3–5 | Find fractions for marked gaps 45°,72°,120°. Correct answers: 1/16,1/10,1/6. The worked 40° lune is 1/9, with nine equal rotational slices. Reflection in the equator gives a triangle half of its lune, not a whole lune. |
| 5 / Grades 4–5 | Count opposite-lune pairs for the octant. Correct record: 3,1,1,1,1,1,1,3; six lunes count 3/2 sphere areas; target fraction 1/8. Pair shading and antipodes are correct. M1–M2 concern mathematical recoverability of the diagram/record. |
| 6 / Grades 4–5 | Apply six-lune areas and explain the general rule. Records (60°,60°,90°), (80°,80°,80°), (100°,100°,100°) give 1/24,1/12,1/6. Each depicted coordinate triangle is unit-radius, positive-area, convex, minor-arc and strictly in an open hemisphere, with the named angles at the named vertices. M3 repairs the bridge to the valid universal argument. |

Grades 3–5 page 4 checks out completely mathematically. Grades 2–5 pages 1–3 have no wrong outcome or diagram, with the located meridian-definition ambiguity above. Grades 4–5 pages 5–6 preserve serious and correct upper mathematics, with the located representation repairs. No K–1 packet is claimed or required.

## Exact general covering proof and limits

Let T be a positive-area convex triangle with minor great-circle sides, distinct nonantipodal vertices A,B,C, strictly contained in an open hemisphere. The three vertices are linearly independent: otherwise their great-circle boundary would be degenerate. Orient the side normals n_A,n_B,n_C so that the hemisphere opposite side BC contains A, and similarly for the others. T is the intersection of these three positive hemispheres. Its antipodal copy T* is the intersection of the three negative hemispheres. The three independent centre planes divide the sphere into exactly eight cells. Every sign triple exists: a positive combination of s_A A, s_B B, s_C C has the desired signs against the normals, because n_i is zero on the other two vertex rays and positive on vertex i.

At A, the containing lune is `H_B ∩ H_C`; its opposite is `(-H_B) ∩ (-H_C)`. Thus a cell belongs to the pair at A exactly when its B and C signs agree. The analogous tests give the complete truth table:

| Region | Side signs | Pair at A | Pair at B | Pair at C | Total |
|---|---|---:|---:|---:|---:|
| 1 | +++ | 1 | 1 | 1 | 3 |
| 2 | ++− | 0 | 0 | 1 | 1 |
| 3 | +−+ | 0 | 1 | 0 | 1 |
| 4 | +−− | 1 | 0 | 0 | 1 |
| 5 | −++ | 1 | 0 | 0 | 1 |
| 6 | −+− | 0 | 1 | 0 | 1 |
| 7 | −−+ | 0 | 0 | 1 | 1 |
| 8 | −−− | 1 | 1 | 1 | 3 |

All equal signs give three agreements. For any other triple, exactly two signs agree, so exactly one pair covers it. This proves the multiplicity for every allowed triangle, independent of cell sizes or symmetry. Boundaries have zero surface area and do not affect the count. The antipodal map preserves surface area, so T and T* have equal area.

A lune of angle α radians has area `2αR²` by rotational proportionality about its polar axis. Opposite lunes are disjoint in their interiors. Hence the six counted lune areas total `4R²(α+β+γ)`. Counting the same set by multiplicity gives `4πR² + 4 area(T)`: one whole sphere plus two extra copies of each of T and T*. Equating yields `area(T)=R²(α+β+γ−π)`. In degrees the whole-sphere fraction is `(angle sum−180)/720`. Positive area gives a sum greater than 180°, and strict open-hemisphere containment gives area less than half the sphere. This is an exact proof; checking the octant, 80° model and three records merely illustrates it.

The scope excludes zero-area/collinear triples, antipodal side endpoints, long arcs, latitude edges, self-crossings and the complementary region. In the pole/equator family θ=0 degenerates, and θ=180 makes A and B antipodal. A triple of 60° corners cannot have positive area under these rules. Lunes intentionally use antipodal poles; this does not violate the triangle-side exclusion. Lengths scale by R and areas by R², so doubling radius doubles lengths and quadruples areas without changing angles or whole-sphere fractions.

## Evidence and limits of verification

`math-qa/check_independent.py` imports no writer/research geometry or verifier. It independently constructs the named spherical examples (including exact radicals for the 60°,60°,90° record), checks local tangent angles, determinant solid angles, minor sides, positive-area/open-hemisphere witnesses, all eight sign cells, each pair's area and the counted-area identity. It checks every displayed coordinate triangle and research meridian instance; the unused authored 75° triangle figure was also checked.

For the emitted TikZ schematics, it reconstructs every arc sample against the appropriate independently defined great-circle plane and the minor-arc interval where required, and checks 50,979 interior projection samples across all seven filled figures. The sampled fill checks avoid a 0.02 side-plane-dot boundary margin and the outermost 1% of the projected radius; they establish numerical agreement away from sampled/rounded boundaries, not an exact clipping proof. Emitted curves are polygonal samples, with visibility style switches allowed one sampling step across the horizon. The source's continuous clipping construction is mathematically consistent with convex hemisphere intersections. No wrong projected curve, shaded lune, target region or antipodal placement was found.

Results are in `math-qa/checks.json`. Every current PDF page was independently rendered at 108 dpi into `math-qa/page-01.png` through `page-06.png` and visually inspected. All actual grade headers, numbered problems, footers and Letter dimensions were checked; text extraction is `math-qa/student-text.txt`. Equal axis scale is retained. The page 5 slivers and missing bridge are visible in those current outputs. This stage does not claim to have inspected future repaired pages or to have done another portable ZIP rebuild; those remain revision/release checks.

The ball/string/marker/paper-corner/meridian/lune handling rehearsal and classroom pilot are **unperformed**. In particular, exact model marking, all three retained triangle sides, and stable overlapping-region records still require physical rehearsal. The analytic proof and digital checks do not validate those physical operations or children's independent use.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
