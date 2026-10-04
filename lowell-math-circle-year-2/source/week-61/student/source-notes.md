# Mathematical and source notes

Written October 4, 2026 for the Week 61 student packet and updated at the fresh revision stage. These are source and mathematical notes, not a facilitator guide.

## Precise scope

The model is an ideal round sphere of radius R. A great circle is its intersection with a plane through the center. For distinct nonantipodal endpoints, the shorter great-circle arc is the unique shortest surface route. Opposite (antipodal) endpoints have infinitely many shortest semicircles, all length pi R. Page 1 invites children to find that ambiguity. Page 2 explicitly excludes opposite corners from triangle sides.

Every later triangle is the nondegenerate smaller convex region bounded by three minor great-circle arcs and contained in an open hemisphere. All interior corners are in (0°,180°). Convexity and the open-hemisphere requirement select the intended interior. Corners are angles between inward side tangents on the actual sphere, not projected angles. A positive-area triangle under these rules has sum greater than 180° and surface-area fraction `(sum - 180)/720`. The complementary region, long-arc choices, self-crossings and latitude-edged shapes are excluded. Two distinct great circles meet at an antipodal pair; latitudes other than the equator are not great circles.

Page 1 experiments are evidence about handled models; exact shortest-path statements come from the ideal-sphere theorem. Paper-corner comparisons and sketches are experiments, not proofs of a universal angle sum. A meridian is a great-circle semicircle with the poles as endpoints; its center plane contains the polar axis, which gives the right-angle crossing with the equator. Page 4 supports an exact argument by equal rotations and reflection across the equator. Pages 5–6 support a conjecture from two checkable covering cases. Page 7 asks for an exact explanation of the general formula, not merely a formula fitted to three records.

For a lune with angle θ degrees, its whole-sphere surface fraction is θ/360. An opposite lune pair has fraction 2θ/360. The three pairs chosen at triangle corners have total fraction `2(sum)/360`. The triangle and its antipodal copy each belong to all three pairs; the other six regions belong to one pair. If the triangle's fraction is f, counted area is `1 + 4f`. Equating these quantities gives `f=(sum-180)/720`. The six-lune rule holds for all stated triangles; page 5 uses the checkable octant example, page 6 tests the unequal 80° cells, and page 7 asks for the universal explanation and its applications.

Page 4 chosen gaps: 45° gives 1/16, 72° gives 1/10, 120° gives 1/6. Page 5 octant angles are 90°,90°,90°; each lune covers 1/4 and all six counted together cover 3/2 spheres. Regions 1 and 8 have three pair coverings, the other six have one; the triangle covers 1/8. Page 6 has the existing 80°/80°/80° geometry as a genuine second covering investigation: regions 1 and 8 each occupy 1/12 of the sphere, and the other six each occupy 5/36. Pair counts remain 3,1,1,1,1,1,1,3. Each opposite pair occupies 4/9; all three pair areas total 4/3. This checks `4/3 = 1+4(1/12)` without assuming equal cells. Page 7 exact application records: (60°,60°,90°) gives 1/24; (80°,80°,80°) gives 1/12; (100°,100°,100°) gives 1/6. These records really exist; inverse spherical cosine-law coordinates and independent tangent/solid-angle checks verify them and their open-hemisphere containment. They are numerical applications, not directions to physically construct exact non-meridian models.

## Exact general explanation

Let T be any positive-area convex minor-arc triangle under the stated open-hemisphere rules, with vertices A,B,C. Its three center-plane side normals n_A,n_B,n_C can be oriented so n_A points toward A across side BC, and similarly for B,C. The vertices are linearly independent: a dependent triple would have a collinear great-circle boundary and zero area. The normals are correspondingly independent. T is the intersection of their three positive hemispheres; its antipodal copy T* is the intersection of their three negative hemispheres.

Every sign triple occurs. For signs s_A,s_B,s_C, normalize `s_A A+s_B B+s_C C`. Each normal is perpendicular to the other two vertex rays and positive on its own vertex, so the resulting point has exactly those signs. Thus there are eight cells, even when their shapes and areas differ. Boundaries have zero area and do not affect the area count.

The pair at A uses circles AB and AC, which have normals n_C and n_B. A cell belongs to that pair precisely when its B and C signs agree: both positive selects the containing lune; both negative selects the opposite lune. The corresponding tests hold at B and C. All-positive and all-negative sign cells have three agreements, so T and T* receive three coverings. Any other triple has exactly two equal signs, hence exactly one agreement and one covering. The complete checkable table is:

| Region | Side signs | Pair A | Pair B | Pair C | Total |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | +++ | 1 | 1 | 1 | 3 |
| 2 | ++− | 0 | 0 | 1 | 1 |
| 3 | +−+ | 0 | 1 | 0 | 1 |
| 4 | +−− | 1 | 0 | 0 | 1 |
| 5 | −++ | 1 | 0 | 0 | 1 |
| 6 | −+− | 0 | 1 | 0 | 1 |
| 7 | −−+ | 0 | 0 | 1 | 1 |
| 8 | −−− | 1 | 1 | 1 | 3 |

The antipodal map is an isometry of the sphere, so T and T* have equal areas. One lune of angle α radians has area `2αR²`, by equal rotational wedges around its antipodal poles. The six lune areas total `4R²(α+β+γ)`. The multiplicity count gives one sphere plus two additional copies each of T and T*, or `4πR²+4 area(T)`. Equating the two expressions gives `area(T)=R²(α+β+γ−π)`, or whole-sphere fraction `(angle sum in degrees−180)/720`. Positive area implies an angle sum above 180°, and the strict open-hemisphere scope gives an area below half the sphere. This exact structural argument is distinct from finite coordinate checks, sampled graphics, model measurements and the two example coverings.

## Original diagram conventions

`geometry.py` generates new TikZ figures from unit-sphere coordinates. All sphere silhouettes have equal horizontal/vertical scale. Great-circle curves are orthographic projections sampled on the actual circle. Earlier oblique views dash invisible portions; upper covering maps deliberately draw only the visible semicircles, with exact horizon endpoints, and use the silhouette for the side circle in the limb plane. Minor arcs use spherical interpolation. Shaded spherical regions are clipped against the visible hemisphere before projection. The first angle convention has two tangent directions at a front-center vertex separated by 135°, with a matching local-direction picture and record. The non-task 40° lune shows one lune, nine equal rotational strips, and a 1/9 record before area use. The first-use 80° example now shows corner A, the selected full circles AB/AC, the containing and opposite lunes on the same ball, and one interior patch X with the matching single-pair count 1. X is in sign cell +−−; it is not on a boundary or in the target triangle. No complete three-pair tally is supplied to students.

The eight region labels on pages 5–6 identify the signs of three oriented side half-spaces. In order they are +++, ++−, +−+, +−−, −++, −+−, −−+, −−−. Opposite region pairs are 1 and 8, 2 and 7, 3 and 6, 4 and 5. Front and back are views of the same ball. Both cameras are along the oriented normal to side BC (side AB for the N,A,B octant labelling). Four complete cells appear on each visible hemisphere: 1–4 in front, 5–8 in back. Every visible cell has its ID; limb points have explicit labels; no hidden arc introduces a projected subdivision. The non-task pair at A covers the cells whose B-side and C-side signs agree. `verify_math.py` checks each cell's area, the sphere total, each pair's area, and the 1/3 multiplicities.

## Credited mathematical sources and library overlap

Anton Petrunin and Sergio Zamora Barrera, *What Is Differential Geometry? Curves and Surfaces*, version 7, December 31, 2025, [primary text](https://arxiv.org/pdf/2012.11814v7): Observation 2.22, printed pp. 24–25 (distance); §14B, p. 119 (antipodal ambiguity); Lemma A.17, p. 178 (spherical excess/lune covering); Proposition 17.10, p. 143 (spherical Gauss–Bonnet setting). Local research previously verified this exact version at `external-resources/new-themes-52-63/week60-61/petrunin-zamora-differential-geometry-v7.pdf`. The reference's CC BY-SA 4.0 notice is source metadata; no source prose or figures are included in this packet.

The project atlas GA-23 already uses the octant and variable-longitude family for parallel transport, in `plans/atlas/families/geometry-analysis.md`. This packet develops a concrete shortest-arc, corner and area investigation. **The octant, lune relation and spherical excess theorem are established mathematics and prior library mathematics, not entirely new ideas.** No transported-arrow task is copied. The Week 41 flat torus is a different intrinsic metric; a physical ball is not its model. The scope of novelty here is newly authored wording, task sequence, recordings, source code and diagrams around credited mathematics.

## Credited pedagogical evidence and adaptation limits

The input research identifies the organizer's year-one *Pattern Block Exercises*, PDF p. 1: five minutes of free exploration before pairs/trios. Current `worksheet-workflow/context.md` reports tiling success and failure of the abstract paper-lamp rule. Adaptation: surface contact, fixed endpoints and corners become handled actions before formal area bookkeeping. This is an inference, not a reported sphere lesson.

Laura Givental, Maria Nemirovskaya and Ilya Zakharevich, *Math Circle by the Bay*, printed p. viii and pp. ix–x (PDF pp. 9–11), supplies deep-context, manipulative and flexible-depth precedents. Natasha Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 3 “At the lesson” item 1; Lesson 7 item 2; Lesson 8 item 2, supplies attempt-before-table and operational construction/recording evidence, as documented in the input research. Their observations do not validate our sphere adaptation. No source passage or illustration is copied.

Root `REPUBLISHING.md` was read unchanged. The portable source has only original source/build/verification files and authored notes. No borrowed exemplars, generated workflow prompts, third-party books, reference PDF duplicates, renders or build intermediates belong in the source ZIP. Attribution and these scoped overlap notes are not claims of publication clearance, an exhaustive rights audit, physical validation or classroom piloting.
