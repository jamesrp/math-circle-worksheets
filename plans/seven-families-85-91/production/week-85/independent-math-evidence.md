# Week 85 independent calculations and coverage

Run `independent-math-check.py` with a Python containing PyMuPDF. It does not import the writer's generator or checker. `independent-math-results.json` records the checked PDF hashes, coordinates, decompositions and measurements; `independent-math-check.log` is the successful run output. The draft was read-only.

## Governing theorem and its limit

Let O-X-Q be one straight rigid bar with OX=XQ=80 mm and Q-Y-P the other with QY=YP=80 mm. The short bars XT and TY also have length 80 mm. For the simple, nondegenerate quadrilateral X-Q-Y-T, equal sides imply that it is a parallelogram, so T=X+Y−Q. Since X=(O+Q)/2 and Y=(Q+P)/2, T=(O+P)/2. Therefore P=2T−O. Segments double, angle sizes and orientation are preserved, and area multiplies by four. Swapping tips solves this equation as T=(P+O)/2.

The simple-frame restriction is substantive: an overlapping configuration T=Q is also compatible with the raw bar lengths and does not enforce this equation. The adult assembly text on materials page 2 explicitly excludes that branch; upper page 1 repeats the restriction. The shared packet relies on that adult setup. Samples do not prove a theorem; the argument above supplies the general explanation.

## Every student task

| Packet/page/problem | Requested result | Independent outcome |
|---|---|---|
| Shared 1/1 | Trace A/B/C and compare | All corresponding segment lengths double. Right angles, triangle angles, orientation, relative proportions, open/closed status and number of corners survive. A's segments 35 and 20 mm become 70 and 40 mm. The three diagrams match their physical inserts. |
| Shared 2/2 | Visit D dots; trace E with P by moving T | D's inverse points are (115,125), (130,160), (155,150), (150,120), (125,140). Any order of straight joins stays in the convex T zone. E's inverse outline is (120,125),(150,125),(150,145),(135,157.5),(120,145), closing back to its start. |
| Shared 3/3 | Seek noncollinearity; a distance rule | Under the stipulated simple frame, no. T is the midpoint of OP; OT=TP and OP=2OT. All nine printed mechanism diagrams satisfy the midpoint, bar-length and output equations. |
| Shared 4/4 | Restrict output to F; largest tracer rectangle | Intended solid target yields x=130..150,y=132.5..147.5, a 20×15 mm rectangle. Outer-border alternative differs and crosses the T-zone boundary; see located issue. “Fill” is naturally interpreted as tracing the boundary in this path activity. |
| Upper 1/1 | Explain doubled anchor distance | The simple-rhombus/midpoint proof above supplies the theorem. All six marks are on the appropriate equal segments. |
| Upper 2/2 | Cover G/H/I originals and copies | G=4→16; H=4→16; I=4.5→18 unit squares. Exact decompositions exist with the supplied 10 mm squares and right-isosceles half-squares; see below. |
| Upper 3/3 | Reverse-trace J/K, find P rectangle for L | J becomes a 30×20 mm rectangle at x=120..150,y=125..145. K becomes the same arrow shape at half scale, vertices (115,137.5),(140,137.5),(140,132.5),(155,142.5),(140,152.5),(140,147.5),(115,147.5). L is x=125..155,y=130..150, so required P rectangle is x=210..270,y=120..160 (60×40 mm). |
| Upper 4/4 | Hold M fixed while moving anchor; restore output by moving M | O′=(60,140) is 20 mm right of O. Fixed M changes its copy from (220,110),(260,110),(240,160) to (200,110),(240,110),(220,160): 20 mm left. Move M 10 mm right to (140,125),(160,125),(150,150) to restore the original copy. All these vertices fit their working zones. |

## Area exact cover, not just equal area

G is a 2×2 block of unit squares; its copy is 4×4, requiring 20 whole pieces together. H consists of a 3×1 bottom strip plus a 1×1 upper square, and its copy is the corresponding strips of integer side lengths; together they need 20 whole pieces.

I is a right-isosceles triangle with 3-unit legs. Partition its lower-left-aligned 3×3 grid into three whole squares and three diagonal half-squares. The copy has 6-unit legs: fifteen whole squares and six half-squares. The pair uses 18 whole squares and 9 half-squares, within the 48+16 supply. Coordinates for every cell appear in the JSON. Triangle pieces may be rotated; no cutting beyond the supplied half-squares is required. The grid-phase error does not change these physical tilings.

## Materials and all rendered diagrams

- Materials page 1: two 182×18 mm strips and two 102×18 mm strips have 11 mm end margins around holes; each adjacent pair of centers is 80 mm apart. Long hole-center spans are 160 mm. The T label occurs at the correct shared short-bar hinge; X/Q/Y match the long-bar midpoints and endpoint joins.
- Page 2: topology has bars OQ, QP, XT and TY; T is the input hinge and P the output endpoint. Its instructions require coaxial tips, spacers and an uncrossed frame, while explicitly acknowledging untested hardware. The board is at least 450×400 mm.
- Pages 3–4: joined US Letter sheets give 431.8×279.4 mm; O=(40,140), O′=(60,140), input insert corners x=100..170,y=105..175, working T zone x=110..160,y=115..165, output corners x=180..290,y=90..190. The 100 mm calibration is correct.
- Page 5: bridge corresponds to mat x=194..238,y=70..215; its crosses at x=204/228,y=80/205 match both mat sheets outside the unprinted seam x=207.9..223.9. The bridge covers that seam. A and B have correct 70 mm cut borders.
- Pages 6–9: D/E/F/J/K output inserts have 110×100 mm borders; G/H/I/L/M/C input inserts have 70×70 mm borders. All labels A through M are present once. The colored physical paths match the student thumbnails. The small solid F box is 40×30 mm; L is 30×20 mm. G/H/I shapes are correctly sized despite their offset grids.
- Page 10: PDF vectors confirm 48 separate 10×10 mm squares. The additional row has eight 10×10 mm squares each divided along one diagonal, supplying 16 matching half-squares. Square and triangle assembly example in upper page 2 is geometrically valid.
- Shared page 1 and upper page 3 demonstrations show an unchanged anchor with a growing two-segment input/output path. Intermediate path endpoints coincide with their tips; forward and reverse arrow roles match the instructions.
- All 18 pages were visually inspected in the draft's rendered contact sheets alongside actual PDF text/vector inspection. Page sizes are US Letter, and source coordinates for all nine linkage drawings independently satisfy the required geometry. PDF hashes pin the checked versions.

## Reachability and limits

The intended zone is convex; every straight trace segment lies within it whenever its endpoints do. With O=(40,140), the T-zone radial distance ranges from 70 mm to sqrt(120²+25²)≈122.58 mm. With O′=(60,140), it ranges from 50 mm to sqrt(100²+25²)≈103.08 mm. Thus it is strictly between the folded and stretched singular distances 0 and 160 mm. An ideal noncollapsed branch exists continuously across either rectangle.

The independent checker additionally constructs 10,201 positions on each anchor's full T-zone grid by intersecting the two 80 mm circles about O and T. It checks all six equal lengths and tests rectangular 18 mm bar bodies with 11 mm end extensions against a centered minimum board. This is sampled digital support-envelope evidence, not a continuous collision proof or physical rehearsal. Output containment at O′ is checked for the actual M task and compensated M only: arbitrary full-zone traces under the moved anchor can leave the marked output zone and are not assigned by the worksheet. Real hand access, sleeves, vertical stack, line width tolerance, friction and branch guards still require adult rehearsal.
