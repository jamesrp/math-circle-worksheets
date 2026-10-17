# Independent mathematical answers — Week 88

Reviewed the eight-page shared Grades K–5 PDF (SHA-256 `699ffe43c5a4f0e9a43abe5dfb5981245f084ef5aaf6bb64d73299b0d7b53fa9`) and its source. All eight pages were freshly rendered into `math-render/` and visually inspected; the author's existing montage is an older version and was not used for final assessment. `check_math.py` is my independent, standard-library-only checker and has no runtime dependency on the draft or author's files. Run `python3 check_math.py`; recorded output is `math-check-results.json`. PDF geometry measurements are separately recorded in `pdf-geometry.json`.

## Problem-by-problem results

| Problem (page) | Task | Independently checked answer/outcome |
|---|---|---|
| 1 (1) | Biggest ring of diameter-40 disks about one diameter-40 disk | Six outside disks. Centers form a regular hexagon of circumradius 40 mm. |
| 2 (2) | Fit as many diameter-40 disks as the group can into 160 × 112 mm | Eleven have an explicit verified construction below. This is an open construction challenge, not a demand to establish the unrestricted packing optimum; no unrestricted maximum of eleven is asserted or certified. |
| 3 (3) | Diameter-40 outside, diameter-80 middle | Nine outside. A regular nonagon of center radius 60 mm realizes it. Ten are impossible. |
| 4 (3) | Diameter-80 outside, diameter-40 middle | Four outside. A square of center radius 60 mm realizes it. Five are impossible. |
| 5 (4) | Both sizes outside; try each middle size | Eight about an 80 mm middle; five about a 40 mm middle. Each is attained with one 80 mm outer disk and respectively seven or four 40 mm outer disks. |
| 6 (5) | Prove equal-size maximum and investigate neighbor contact | Six. Every cyclic angular gap is at least 60°; the six gaps sum to 360°, so every gap is exactly 60° and all neighboring disks touch. Seven would require at least 420°. |
| 7 (6) | Eleven disks, horizontal rows 4–3–4, 160 × 110 mm | Possible. Minimum necessary height is 109.2820323… mm, leaving 0.7179677… mm. |
| 8 (7) | Same row constraint in 160 × 108 mm | Impossible; the necessary height exceeds this by 1.2820323… mm. |
| 9 (7) | Smallest height for those rows, width 160 mm | Exactly 40 + 40√3 mm. This claim is confined to the specified straight horizontal 4–3–4 arrangement. |
| 10 (8) | Establish upper bounds for all the unequal/mixed rings | Uniform ring bounds and exhaustive mixed cyclic-order exclusion below establish 9, 4, 8, 5 respectively. |
| 11 (8) | Rule for arbitrary uniform outer size | For positive middle radius R and outer radius r, maximum is floor(π/arcsin(r/(R+r))). Equivalently use diameters D,d in floor(π/arcsin(d/(D+d))). This is the planar, nonoverlapping, externally touching setting; it assumes enough pieces and room. |

## Uniform and mixed ring proofs

For an outer radius r, its center is R+r from the middle center. Two outer radii r,s cannot overlap precisely when their center distance is at least r+s. The minimum angle between their radial segments is

`α(R;r,s) = arccos(((R+r)^2+(R+s)^2-(r+s)^2)/(2(R+r)(R+s)))`.

For equal outer radii this is `2 arcsin(r/(R+r))`. Every consecutive directed angular gap is at least this angle (even if one directed gap exceeds 180°); sum the gaps to bound the count. Uniformly spaced centers attain the bound, and the checker verifies every pair of disks, not just neighbors. Equal radii give 60°; the two unequal cases give 38.94244127…° and 83.62062979…°. Ten times the former and five times the latter exceed 360°.

For mixed disks about R=40 mm, the small-small, small-large, and large-large bounds are respectively `acos(7/9)`, `acos(2/3)`, and 60°. For R=20 mm they are 60°, `acos(1/3)`, and `acos(1/9)`. The checker enumerates all 510 binary cyclic words of length nine with both sizes for R=40, and all 62 words of length six for R=20. The smallest required angle sums are 368.97645909…° and 381.05755873…°, respectively, so every order is impossible. Any larger mixed ring could have disks deleted to leave one of these excluded counts while retaining both sizes; thus larger rings are excluded too.

Witness construction: begin with the sole large outer disk, then all small ones in cyclic order. Give each gap its pair-specific minimum plus an equal share of the remaining angle. The checker computes Cartesian coordinates and checks all pairwise distances, every central tangency, and containment within a centered 260 × 260 mm mat. Full center/radius triples are in `math-check-results.json`. The intended materials are sufficient for every witness. Numerical computations supplement the angular proof; forbidden sums have margins exceeding 8.97° and 21.05°, far from rounding uncertainty.

## Row construction and lower bound

Let `g = 20√3`. Use center coordinates in millimeters:

- Bottom: `(20,20), (60,20), (100,20), (140,20)`.
- Middle: `(40,20+g), (80,20+g), (120,20+g)`.
- Top: `(20,20+2g), (60,20+2g), (100,20+2g), (140,20+2g)`.

Adjacent rows have nearest horizontal displacement 20 and vertical displacement g, hence distance 40. The checker checks all 55 pairs, edges and heights. The same witness works for Problems 2 and 7.

For the lower bound, four diameter-40 disks on a straight horizontal row inside width 160 have centers forced to x=20,60,100,140: three gaps of at least 40 use all 120 mm of available center width. Any middle-row center has x in [20,140], hence lies at most 20 horizontally from one of these forced centers in each four-disk row. Each vertical row separation is therefore at least `sqrt(40²−20²)=20√3`. Add both separations and the bottom/top radii to get `40+40√3`. This remains valid if the middle row is not evenly spaced. It makes no claim about unrestricted or slanted arrangements.

## Diagram and physical-output checks

The final PDF has eight US Letter pages. The ring sketches on pages 3–4 correctly maintain the 2:1 diameter ratio and explicitly state they are sketches. The page-5 worked visual has three identical tangent pairs at half scale: radii 15 and 25 mm, collinear centers and contact point, and final center distance 40 mm. It does not pre-answer the ring count. Pages 1 and 5 have radius-20 mm middle disks at full scale. The four page-8 blank ring references have the correct size ratios and size labels.

The actual interior edges of the PDF's four filled tray-border strips give:

| Page | Intended interior | PDF interior measured in mm |
|---|---|---|
| 2 | 160 × 112 | 160.001229 × 112.000851 |
| 6 | 160 × 110 | 160.001229 × 110.000833 |
| 7 | 160 × 108 | 160.001229 × 108.000826 |

Differences below 0.002 mm reflect TeX/PDF unit conversion. All border ink lies outside the measured interior. No diagram has unequal x/y scaling. These digital checks do not establish printer accuracy, disk accuracy, physical rehearsal, or classroom readiness. The 110 mm construction remains physically untested.

## Fixed mixed witnesses used in the adult guide

The independent checker also verifies both specified reserved-plan witnesses, with angles measured from the middle center:

- R=40 mm: one radius-40 outer disk at 0°, seven radius-20 outer disks at 50°, 90°, 130°, 170°, 210°, 250°, 290°.
- R=20 mm: one radius-40 outer disk at 0°, four radius-20 outer disks at 80°, 140°, 200°, 260°.

Both pass all-pair nonoverlap, central tangency and 260 × 260 mm centered-mat containment checks. For the first, successive small-small gaps of 40° exceed 38.942…° and the two large-small gaps are 50° and 70°, exceeding 48.189…°. For the second, the small-small gaps are exactly 60° and the two large-small gaps are 80° and 100°, exceeding 70.528…°. The full Cartesian verification also checks non-neighbor pairs.
