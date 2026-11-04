# Week 205 (draft plan): Pi from polygons

**Strand:** analysis, with shape (app region "Shapes and spaces"). **Deep-math field:** limits, squeezing between bounds, Archimedes' method. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Every circle's circumference is the same multiple of its diameter, π, and its area is half the circumference times the radius, so A = πr². Archimedes' Measurement of a Circle states the area result as Proposition 1 ("every circle is equal to a right-angled triangle" with one leg the radius and the other the circumference) and proves it by double reductio: if the circle were bigger than the triangle, a fine enough inscribed polygon would be bigger too, and if smaller, a circumscribed one would be smaller, and both contradict the polygon's area being half its perimeter times its apothem. Proposition 3 gives 3 10/71 < π < 3 1/7, that is 223/71 < π < 22/7, by starting from hexagons and doubling the number of sides four times to 96. Perimeter over diameter is n sin(π/n) for the inscribed n-gon and n tan(π/n) for the circumscribed one: 3 and 3.464 for hexagons, 3.1410 and 3.1427 for 96-gons, and each doubling cuts the gap between the bounds by about 4. Archimedes needed square roots by hand along the way and used 265/153 < √3 < 1351/780. The wedge picture makes the area formula concrete: cut a disc into many equal wedges and lay them alternately up and down; they form a near-parallelogram with base half the circumference (πr) and height r, and the more wedges, the closer it comes to a rectangle of area πr². The honest limit statement matters: the rearranged wedges always have exactly the disc's area, and what needs an argument is that the shape tends to a rectangle; replacing each wedge by its triangle gives the inscribed polygon's area (m/2)r² sin(2π/m), half its perimeter times its apothem, which tends to half the circumference times the radius. "Looks more and more like a rectangle" is not by itself a proof, since Week 50 shows staircases can approach a diagonal while their length stays fixed. Convexity is what makes the polygon perimeters behave. Proved: Propositions 1 and 3, and the convergence of both bounds. Children can discover that circumference over diameter is a bit more than 3 for every round object, that the hexagon proves "more than 3", that the wedge strip is about πr long and r high, and in grades 4–5 why inscribed and circumscribed polygons trap π.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Archimedes Measurement of the Circle: Proposition 1](https://legacy-www.math.harvard.edu/archive/archimedes09/pdf/Measurement.of.the.Circle.pdf). Seminar notes, Harvard Mathematics archive, February 6, 2009. Mark's literal translation of Proposition 1 (the circle equals a right triangle with legs the radius and the circumference) and its structure as an argument by contradiction from both sides with inscribed and circumscribed polygons (read November 4, 2026).
- [Archimedes and Pi](https://www.cs.miami.edu/home/burt/manuscripts/archimedes/archimedes_pi.html). Burton Rosenberg, University of Miami, 2003. Proposition 3's 223/71 < π < 22/7, the doubling from hexagon to 96-gon, the ratios 265 : 153 and 1351 : 780 in Archimedes' steps, and an error estimate for n-gons (read November 4, 2026).
- Prior use with children: [Relating Area to Circumference](https://im.kendallhunt.com/MS/teachers/2/3/8/index.html). Illustrative Mathematics, Grade 7, Unit 3, Lesson 8. Students cut a circle into wedges, rearrange them into a near-parallelogram, and reason that area is half the circumference times the radius (read November 4, 2026).
- Prior use with children: [Cutting Pi](https://www.howtosmile.org/resource/cutting-pi). Exploratorium (listed on howtosmile.org), ages 11 to adult. Wrap string around a round object, cut it, and count how many diameters fit along it (read November 4, 2026).
- [Circles Lesson 1: The Ratio of Circumference to Diameter](https://nctm.org/Classroom-Resources/ARCs/Measures-of-Circles/Circles-Lesson-1). NCTM, grade 7. Measuring round objects with string to find the ratio (read November 4, 2026). No K–5 math-circle handout was found.

## A kid-friendly way in

Materials per table: a collection of round things (cans, lids, plates, a bucket, tape rolls), string or yarn, scissors, masking tape, a printed sheet with a circle and its inscribed and circumscribed hexagons, paper plates or card discs pre-marked into 8 and 16 wedges, glue sticks, a 1 cm grid sheet with a 10 cm radius circle. Prep: gather objects, print sheets, mark plates, about 25 minutes. Launch (3 minutes): wrap a string once around a big can, cut it, then lay the can's width along the string again and again; the group counts "three and a bit". Ask whether a bucket or a coin would give a different count.

Suggested hour: 0–5 launch; 5–20 measure many round things, lay the cut strings on a big "diameters" chart; 20–40 band tasks; 40–55 wedge strips; 55–60 compare everyone's "three and a bit".

## By band

- **K–1:** Cut a string as long as the way around, then mark off the across lengths with a crayon. Is it always three and a bit? Make a circle "into a strip" by cutting a plate into 8 wedges and laying them up and down.
- **2–3:** Measure five round objects and list the "times around over across" results. Then the hexagon sheet: why is the circle's way around longer than 3 across, and shorter than the outside hexagon? Count grid squares inside and touching the 10 cm circle and compare with the wedge strip's rectangle.
- **4–5:** Double the hexagon to a 12-gon by folding or by drawing on the printed circle, and measure both polygons' perimeters; how close can you trap π? Explain the wedge rectangle's base and height, and why more wedges make the area estimate better. Then Archimedes' 96-gon and 22/7: which is closer to the measured value from string?

## Checked facts

- `check_week_205()`: inscribed and circumscribed perimeter over diameter for n = 6, 12, 24, 48, 96: 3.0000 and 3.4641, 3.1058 and 3.2154, 3.1326 and 3.1597, 3.1394 and 3.1461, 3.1410 and 3.1427; 223/71 = 3.140845 and 22/7 = 3.142857 lie outside the 96-gon bounds; each doubling divides the gap by about 4 (between 4.00 and 4.24).
- `check_week_205()`: (265/153)² < 3 < (1351/780)².
- `check_week_205()`: the inscribed m-gon areas for m = 8, 16, 32, 64 are 2.83, 3.06, 3.12, 3.14 times r².
- `check_week_205()`: on a 1 cm grid a 10 cm radius circle has 276 squares wholly inside and 344 touched, around 100π ≈ 314.16; radius 5 gives 60 and 88 around 78.54.
- `check_week_205()`: a 10 cm can has circumference about 31.42 cm; a 1 mm error in a 7 cm diameter shifts the ratio by about 1.4%.
- Propositions 1 and 3 are cited from the sources; the irrationality of π is not claimed here.

## Nearest existing themes

Week 26 (Same area, different boundaries) is about polyomino perimeters, not circles, so it does not overlap. Week 48 (Inside and outside covers) traps an area between inner and outer counts, the same squeeze in grid form; the 2–3 grid count above is a direct callback. Week 50 (Staircases and lengths) is the warning that converging shapes need not have converging lengths. Week 59 (Constant-width shapes) already uses π for the Reuleaux triangle's perimeter (Barbier), and Week 88 uses angles around a circle; draft 130 finds π by dropping needles and draft 126 cuts and rearranges polygons. No library week measures circumference or derives πr². New here: π as a constant children measure, Archimedes' two-sided squeeze, and the wedge argument for area.

## App connection

Region "Shapes and spaces", possible family "Trap the circle": a circle with a slider for the number of sides; the child sees inside and outside polygons and their perimeters as bars, and must reach a target gap. Puzzle 1: "Trap the circle between bars less than 0.1 apart." Puzzle 2: "Rearrange 16 wedges into a strip and read its length and height." Week 48's "Area traps" family could host the grid version.

## Open questions

- String measurement error for small objects: rehearse whether 2–3 children get "three and a bit" reliably, or whether larger objects (buckets, hoops) are needed.
- Is folding a 12-gon from a printed hexagon practical, or should both polygons be printed?
- π is a standard middle-school topic; returning children may already "know 3.14". Keep the focus on why it is the same for every circle and how to trap it.
- Wedge cutting with 16 pieces may be fiddly for K–1; pre-cut wedges in two colours may help.
