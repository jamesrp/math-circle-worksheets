# Week 59 nominal mathematics and provenance

For a compact convex filled shape K, the width in unit direction u is
`max(x·u) − min(x·u)` over K: the perpendicular separation of the two parallel
supporting lines. A circle of diameter w and the exact Reuleaux triangle below
both have width w in every direction. An unequal-axis ellipse, square and
equilateral triangle do not. Finite ruler measurements provide experiments or
counterexamples; the all-direction statement requires an explanation. Total
width does not force a chosen interior point to remain halfway between the
supports. These are the worksheet's destinations; width is distinct from a
central chord, arbitrary vertex distance, arc radius and boundary length.

## Exact construction and universal support argument

Let A=(0,0), B=(w,0), C=(w/2, sqrt(3)w/2), w>0. The Reuleaux triangle is the
intersection of the three closed radius-w disks centered at these vertices.
Its boundary follows B→C around A at angles 0→60 degrees, C→A around B at
120→180 degrees, and A→B around C at 240→300 degrees. Every arc is the minor
60-degree arc; arbitrary rounded triangular outlines have no such guarantee.
The three closed disks are compact and convex, so their intersection is too.

Take a unit u whose angle lies between AB and AC. P=A+w*u lies on the BC arc:
its distances to B and C are at most w since each angular difference is at most
60 degrees. For x in K, its distance to A is at most w, so `x·u ≤ w`, with equality
at P. The line perpendicular to AP at P therefore encloses and touches K.

The opposite line through A must also enclose the **whole** shape. Membership
in the disks centered at B,C, together with |B|=|C|=w, implies
`x·B ≥ |x|²/2 ≥ 0` and `x·C ≥ |x|²/2 ≥ 0`. A u between B and C is a nonnegative
linear combination of B and C. Thus `x·u ≥ 0`, with equality at A. The opposite
support line exists and the gap is w. This checks the vertex contact rather
than assuming a radius alone is sufficient.

The corresponding sectors from B and C are 120–180 and 240–300 degrees.
Reversing a support direction leaves width unchanged; those three sectors and
their reversals cover every direction, including endpoints. This supplies the
all-turn content requested in Problem 4. Circle contact and perpendicular radius
are illustrated with a separate non-task circle before the task. The three
worksheet turns 7,37,83 degrees are illustrative instances, not the proof.

## Task-specific checks

1. Ideal width extrema in mm: disk [60,60]; ellipse [40,60]; square
   [60,60 sqrt(2)] ≈ [60,84.853]; equilateral triangle [30 sqrt(3),60] ≈
   [51.962,60]; Reuleaux [60,60]. The circle's radius is 30 while each Reuleaux
   arc's radius is 60. The non-task parallelogram has vertices (0,0),(38,0),
   (46,32),(8,32); its displayed horizontal support gap is 46, with a perpendicular
   arrow and a matching recorded sketch. It is drawn at 0.55 scale as a convention
   example; it is not a full-size model.
2. Between fixed 60 mm parallel edges, disk and Reuleaux can turn through all
   orientations and touch both edges. Ellipse and equilateral triangle can turn
   inside with translation, but lose one contact whenever width is below 60.
   The square has positions wider than 60 and cannot turn fully inside. This
   uses support width; no fixed-point rotation constraint is imposed. The student
   width rule is explicitly limited to measuring width, when both supports adjust
   into contact. Problem 2 explicitly keeps the parallel edges fixed 60 mm apart:
   it does not require contact at every fitting position. In a given orientation
   a freely translated piece fits iff its width is at most 60, and touches both
   iff its width equals 60. A continuous translation can center the continuous
   projection interval throughout a full turn. Clearance
   for physical cuts has not been tested.
3. The same construction with side/radius 40 gives width 40. Both 40 and 60 mm
   templates have exactly three equal sides. The before-use compass example has
   D=(0,0), E=(25,0), F=(0,25); opening DE at center D draws the 90-degree EF arc.
   It is deliberately a different construction instance from the target shape.
4. See the universal argument above. Experiments on any finite set of turns do
   not alone justify an assertion about every direction.
5. On the disk O is its center, so every O-to-support distance is 30. On the curved
   triangle O is the underlying equilateral centroid, not a circular center.
   `|O−vertex|=w/sqrt(3)` and its distance to the opposite arc midpoint is
   `w−w/sqrt(3)`: 34.641 and 25.359 at w=60. On a generating arc,
   `|A+w*u−O|²=|A−O|²+w²+2w(A−O)·u`; the arc's angle runs ±30 degrees about
   the direction opposite A−O. Distance is greatest at its endpoints and least
   at its midpoint. Hence no boundary point is farther from O than a vertex.
   The maximum support distance is the vertex distance; constant width makes the
   minimum its complement to w. These extrema are attained by the vertex/arc-midpoint
   support directions. The exact witnesses refute “constant width means constant
   marked-point height.” They do not assert smooth rolling or constant axle height.
   Before this task, an authored non-task rectangle with vertices (0,0),(44,0),
   (44,28),(0,28), in mm, carries the off-center mark O=(12,9). Its right support
   is x=44, enclosing the entire rectangle and touching its right side. The
   perpendicular from O ends at (44,9), has length 32 mm and is shown with a
   right-angle mark. Three panels show marked piece, the one touching edge plus
   measured segment, and a matching 32 mm record at display scale 0.6. This
   example shows one point-to-support distance, not the two-edge width (44 mm),
   an O-to-corner segment, or either target's extrema. O is a marked point, with
   no claim that it is every piece's center. The target orientations and extrema
   remain choices for the children.
6. Each boundary arc is one sixth of a radius-60 circle. The three arcs total
   half that circle's boundary. A radius-30 circle is a scale-1/2 copy, so its
   boundary is the same length. Equivalently both lengths are 60*pi ≈188.496 mm.
   This is a direct three-arc calculation; no general perimeter theorem is needed.
   The generating-circle panel uses six equal 60-degree sectors and the same
   0.63 display scale as both compared shapes.

## Source precedents and original adaptation

- ThinkMaths, [Shapes of constant width](https://think-maths.co.uk/resources/shapes-constant-width/),
  labels its material KS3,4,5. [Shapes of Constant Width](https://think-maths.co.uk/wp-content/uploads/2023/03/Shapes-of-Constant-Width_0.pdf),
  PDF p.1 Activities 1–2, supplies the parallel-edge experiment and contrasting
  constructions as precedents. [Constructing Shapes of Constant Width](https://think-maths.co.uk/wp-content/uploads/2023/03/Constructing-Shapes-of-Constant-Width.pdf),
  PDF p.1, supplies the equilateral three-arc construction. The writer used the
  repository's inspected Week 59 research record, not copied source figures or
  prose. Our square/ellipse control selection, record layouts, quarter-arc example,
  fixed-gap question, marked-point task, off-center measurement example and all
  diagrams/wording were authored here.
- Francis E. Su et al., [Reuleaux Wheel, Harvey Mudd College Math Fun Facts](https://math.hmc.edu/funfacts/reuleaux-wheel/),
  construction paragraph and “The Math Behind the Fact,” supports the established
  constant-width result. The support-sector proof here is an independent
  derivation, not a reproduced proof from that page. No exact square-hole claim
  is included.
- The repository's Week 59 research note records pedagogical evidence from
  Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 6 “At the
  lesson” (`OEBPS/part0016.xhtml`), and Givental et al., *Math Circle by the Bay*,
  Preface printed vii–ix (PDF pp.8–10). The former reports low child enthusiasm
  in an angle-cutting episode; its proposed explanation is a hypothesis. The
  latter supports deep themes, clear tasks and available manipulatives. Our
  inference is to offer substantial concrete comparisons before geometric proof;
  neither book validates this new route. The research note also reports the
  organizer's first-year Handouts 3 Problems 3.4–3.7 and Pattern Block Exercises
  p.1 as concrete shape-comparison and scale-check precedents, not prior use of
  this support-width investigation.

No text or assets from any referenced book, downloaded sheet, prior worksheet
or workflow exemplar were copied into the PDFs or lean source files. Source
attribution does not establish publication permission or elementary-age piloting.
Root REPUBLISHING.md was read and preserved.

## Verification limits

The independent verifier reads the actual generated arc center/radius/endpoints,
checks every polygon's convexity and the relevant regularity, and computes
linear extrema on circular arcs in 1,440 directions for every depicted Reuleaux
triangle. It also reads compiled PDF vectors and evaluates cubic Bezier extrema
rather than using their control-point bounding boxes. The greatest compiled
Reuleaux width deviation observed by the independent draft review and reproduced
by the final revision's rerun in 3,600 directions is 0.001631 mm. The nominal
60 mm disk's sampled compiled widths are
60.000456–60.016920 mm: checking only its coordinate axes conceals its cubic
approximation error. These are finite digital samples, not certified all-angle
error bounds or physical tolerances. Nominal geometry has the exact properties
proved above. All US Letter pages were rendered and visually inspected. Every copied
and ZIP-extracted source rebuild is checked for identical page text, dimensions
and rendered pixels. Physical print/cut/rail/compass trials, timing and classroom
piloting remain unperformed.
