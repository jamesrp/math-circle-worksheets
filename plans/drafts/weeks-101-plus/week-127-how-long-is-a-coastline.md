# Week 127 (draft plan): How long is a coastline?

**Strand:** shape, with analysis (app region "Shapes and spaces"). **Deep-math field:** fractal geometry, measurement, limits. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

For a smooth curve, measuring with shorter and shorter rulers gives totals that settle down to a length. For a coastline they do not: Lewis Fry Richardson's measurements, analysed by Mandelbrot ("How long is the coast of Britain? Statistical self-similarity and fractional dimension", Science 1967), fit the empirical law L(G) ≈ M·G^(1−D), where G is the ruler length and D is a constant at least 1. Mandelbrot reported D ≈ 1.25 for the west coast of Britain, 1.13 for Australia, 1.14 for the Spain–Portugal border and 1.02 for South Africa. This is an empirical fit over a range of scales, not a theorem about real coasts, which stop being self-similar at the scale of grains of sand. The exact model is the Koch curve: each stage replaces every segment by four segments one third as long, so the length is multiplied by 4/3 each stage and grows without bound, while the curve itself stays inside a bounded region. Its similarity dimension is log 4 / log 3 ≈ 1.262, since it is made of N = 4 copies scaled by r = 1/3 and D = log N / log(1/r). Box-counting gives the same number for the limit curve: with boxes of side ε, the number N(ε) of boxes touched grows like ε^(−D); a segment doubles its count when ε halves (D = 1), a filled square quadruples (D = 2), and the Koch curve multiplies by about 4 when ε is divided by 3. What children can discover: shorter rulers always give a longer answer for a wiggly coast, the answer for a straight edge does not change, and counting boxes at two grid sizes gives a growth factor that tells "line-like" from "area-like" from "in between".

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [How Long Is the Coast of Britain? Statistical Self-Similarity and Fractional Dimension](https://gis.humboldt.edu/olm/courses/gsp_510/Articles/Mandelbrot1967.pdf) — Benoit Mandelbrot, Science 156 (1967), p. 636 onward. Richardson's relation L(G) ~ G^(1−D) and the values D = 1.25 (west coast of Britain), 1.13, 1.14, 1.02 (read November 3, 2026). Bibliographic record: [ADS abstract](https://ui.adsabs.harvard.edu/abs/1967Sci...156..636M/abstract) (read November 3, 2026).
- [5 Fractal Geometry](https://webapps.math.uci.edu/~ndonalds/math161/fractals.html) — Neil Donaldson, UC Irvine Math 161 course notes. Self-similar dimension log N / log(1/r); Koch curve D = log 4 / log 3 ≈ 1.2619 and stage lengths (4/3)^n; box-counting definition; empirical coastline method (read November 3, 2026).
- Prior use with children: [Coastline (teacher notes)](https://meaningfulmaths.nt.edu.au/mmws/nz/sites/default/files/images/Coastline_Teacher.pdf) — New Zealand curriculum Level 4 task hosted by Meaningful Maths NT: measure a coastline with a centimetre ruler and with string on maps at several scales and compare (read November 3, 2026).
- Prior use (older students): [Fractals: Measuring a Coastline](https://serc.carleton.edu/spaceboston/2011activities/57516.html) — SERC Carleton, high-school activity measuring a printed Koch snowflake with sticks of 1, 5, 10 and 20 cm (read November 3, 2026).

## A kid-friendly way in

Materials: an enlarged printed outline of a local shoreline (for example Bellingham Bay and Lummi Island from a public map), printed Koch curves of stages 1, 2 and 3 on a base of 27 cm, card strips of 9, 3 and 1 cm (or pairs of dividers for older children), string, and transparent grids at 2 cm and 1 cm. Prep: print and cut strips, about 20 minutes. Launch (3 minutes): walk a long strip along the shoreline on the board, end to end, counting steps; then do the same with a short strip for one bay and ask what will happen to the total.

Suggested hour: 0–5 launch; 5–30 strip-walking on the coast and the Koch drawings with a shared table of results; 30–45 box counting (4–5) or string comparisons (K–1); 45–60 put every table's totals on one board and ask what the coast's "real" length is.

## By band

- **K–1:** Lay string along a wiggly edge and along a straight edge of the same span, then straighten both strings and compare. Walk a long and a short strip along a printed coast and count steps with stickers.
- **2–3:** Measure the shoreline with 9 cm, 3 cm and 1 cm strips and record steps × strip length. Does the total settle down? Do the same on printed Koch stages on a 27 cm base, where each strip matches one stage's segments and the answers are exact: 36 cm (stage 1, 9 cm strip), 48 cm (stage 2, 3 cm strip), 64 cm (stage 3, 1 cm strip).
- **4–5:** Box counting: lay the 2 cm and 1 cm grids over a straight line, a filled shape and the coastline, count touched boxes, and compare the growth factors. Explain why the Koch curve's length grows by 4/3 each stage, and why its box count grows by about 4 when boxes shrink by 3.

## Checked facts

- `check_week_127()`: Koch stage lengths on a base of 1 are 1, 4/3, 16/9, 64/27; stage n has 4^n segments, so a ruler of length 3^(−k) takes exactly 4^k steps on stage k. On an 81 cm base the stage lengths are 81, 108, 144, 192, 256 cm (a 27 cm base gives 27, 36, 48, 64).
- `check_week_127()`: log 4 / log 3 ≈ 1.26186. With D = 1.25, halving the ruler multiplies the measured length by 2^0.25 ≈ 1.189, and four halvings double it.
- `check_week_127()`: box counts for a segment double when the box side halves; for a filled square they quadruple. For Koch stage 5 on a unit base, a computed count gives 16 boxes of side 1/9 and 68 of side 1/27, a factor of 4.25 (close to 4; real grid counts wobble).
- Coast dimensions (1.25 and others) are cited from Mandelbrot 1967, not computed.

## Nearest existing themes

Week 50 (Staircases and lengths) shows nearby curves can have very different lengths; Week 51 (Honest measurement ranges) treats measurement error; atlas GA-29 (Cantor set) removes length to leave a dust. New here: length that grows without limit as the ruler shrinks, and a fractional dimension measured by box counting. The Koch construction is close to Week 76's substitution idea but applied to a curve.

## App connection

"Shapes and spaces". A board with a ruler of selectable length that the child "walks" along a coast (snapping each step to the curve) while the app keeps the tally; puzzles: "predict the total with the 1-unit ruler" or "which of three coasts gives the same answer for every ruler?" A box-counting overlay with two grid sizes could be a second puzzle type. Likely a new family.

## Open questions

- Which local shoreline map can be printed without licensing issues (public-domain USGS or NOAA chart)? Not yet checked.
- Strip-walking on a printed coast is imprecise; do children get a clear increasing trend with only three rulers?
- Is box counting with transparent grids practical for 4–5, or should the grids be printed under the coast?
- The 2–3 exact Koch numbers depend on rulers matching stage segment lengths; confirm the printed sizes.
