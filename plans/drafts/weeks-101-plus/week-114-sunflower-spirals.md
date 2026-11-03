# Week 114 (draft plan): Sunflower spirals

**Strand:** number and dynamics (Numbers; Patterns and symmetry). **Deep-math field:** Diophantine approximation, mathematical biology. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Place seeds one at a time, each turned by a fixed fraction t of a full turn from the last, and each a little further out (Vogel's model, 1979: seed i at angle i·t and radius proportional to √i, so seeds cover equal areas). If t is a fraction p/q in lowest terms, seed i lands on the same ray as seed i + q, so the seeds line up on exactly q straight spokes with gaps between them (proved, and the same fact as hopping p around q dots). If t is irrational no two seeds share a ray. The golden turn t = 1 − 1/φ ≈ 0.382, about 137.5°, is the irrational hardest to approximate by fractions, so no spokes form at any scale, and the seed head packs evenly; nearby fractions such as 2/5 (144°), 3/8 (135°) and 5/13 (138.5°) give 5, 8 and 13 spokes. The spirals the eye sees join each seed to its nearest neighbours, and in the golden model those neighbours are i ± a Fibonacci number (checked here: across seeds 10 to 899 of a 1000-seed model, every nearest neighbour is 8, 13, 21, 34, 55 or 89 seeds away), which is why the two visible spiral families have consecutive Fibonacci counts that grow outward. That the golden angle is what plants produce is a separate, physical claim: Douady and Couder (Physical Review Letters, 1992) obtained phyllotactic patterns in a physical experiment with magnetic droplets, which is usually read as evidence that the pattern can come from simple growth dynamics; that interpretation is a hypothesis about plants, not a theorem. And the biology has exceptions: in the Turing's Sunflowers citizen-science study (Swinton, Ochu and consortium, Royal Society Open Science, 2016) 632 of 768 spiral counts (about 82%) had Fibonacci structure, and 136 did not. Children can discover spokes versus spirals, that spoke counts come from the fraction's denominator, and that real cones and flowers mostly, not always, show neighbouring Fibonacci counts.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Vogel Spiral](https://mathworld.wolfram.com/VogelSpiral.html) — MathWorld (Wolfram). The formula r = c√n, θ = n·α with the golden angle, and the reference H. Vogel, "A Better Way to Construct the Sunflower Head," Math. Biosci. 44 (1979) 179–189 (read November 3, 2026).
- [Golden Blossoms, Pi Flowers](https://mathtourist.blogspot.com/2020/04/golden-blossoms-pi-flowers.html) — Ivars Peterson, The Mathematical Tourist, 2020 (first posted 2002), summarising Michael Naylor's 2002 Mathematics Magazine article: a rational fraction of a turn gives distinct spokes, the golden angle gives no clumping (read November 3, 2026).
- [Novel Fibonacci and non-Fibonacci structure in the sunflower](https://pmc.ncbi.nlm.nih.gov/articles/PMC4892450) — Swinton, Ochu and the MSI Turing's Sunflower Consortium, Royal Society Open Science 3 (2016) 160091. 657 sunflowers, 768 parastichy counts, 565 Fibonacci plus 67 Fibonacci-structured, 136 without (read November 3, 2026).
- [Dynamical system approach to phyllotaxis](https://core.ac.uk/download/13733845.pdf) — d'Ovidio and Mosekilde, Physical Review E 61 (2000). Reports and cites Douady and Couder's magnetic-droplet experiment, Phys. Rev. Lett. 68, 2098 (1992) (read November 3, 2026).
- Prior use with children: [Fibonacci's Sunflowers](https://cdn.agclassroom.org/ks/kslesson/fibonaccis.pdf) — Kansas Foundation for Agriculture in the Classroom lesson by Amy Benz, grades 6–8, with real sunflower heads and optional pinecones (read November 3, 2026).

## A kid-friendly way in

A seed-placement sheet: a printed disc with numbered rays at angle i·t for i = 1 to 60 and faint guide circles at radius √i, one sheet per turn fraction (1/4, 2/5, 3/8 and golden). Children stick round sticker "seed" i on ray i at circle i, then compare finished sheets across the table: some make spokes, the golden one makes crossing spirals. A real pinecone (or sunflower head, or pineapple) per table for counting the two families of spirals, marking one spiral with a pipe cleaner or a dab of paint. Prep: print four sheet types (generated once by a script), sticker dots, collect pinecones; about 20 minutes once sheets exist. Launch (2–3 minutes): place seeds 1 to 8 on a big quarter-turn sheet together, ask where seed 9 will go, and hand out the other sheets.

## By band

- **K–1:** stick 30 seeds on a quarter-turn sheet (4 spokes, 8, 8, 7, 7 seeds) and on a golden sheet; describe the difference; count spirals on a pinecone with an adult marking the start.
- **2–3:** predict the number of spokes for 2/5 and 3/8 before placing; count both spiral families on pinecones and record them on a class chart; are the two numbers usually neighbours in 1, 2, 3, 5, 8, 13?
- **4–5:** why a fraction p/q gives q spokes (seed i and seed i + q share a ray); which fraction of a turn is closest to the golden one with small denominators (2/5, 3/8, 5/13, 8/21 get closer each time); compare the class chart with the citizen-science result that most but not all counts are Fibonacci.

## Checked facts

Computed in `check_number.py`, `check_week_114()`:

- golden angle 360(1 − 1/φ) = 137.5078° (to 4 places), equal to 360/φ²;
- turns 1/2, 1/3, 1/4, 2/5, 3/8, 5/13 give 2, 3, 4, 5, 8, 13 spokes;
- the Fibonacci fraction angles 180°, 120°, 144°, 135°, 138.5°, 137.1°, 137.6° approach the golden angle with strictly shrinking error;
- in a 1000-seed golden Vogel model, nearest neighbours of seeds 10 to 899 are 8, 13, 21, 34, 55 or 89 seeds away (all six occur);
- 30 seeds at a quarter turn sit 8, 8, 7, 7 on the four spokes;
- arithmetic on the cited 2016 counts: 565 + 67 = 632 of 768, about 82%, leaving 136.

Cited, not computed: the biological counts, Douady and Couder's experiment, Vogel's formula as published.

## Nearest existing themes

Week 4 (stars and wheels) is the rational half of this week: hopping p around q dots is a turn of p/q. Week 8 (rook race and Nim) meets the golden ratio through Wythoff pairs, and Week 110 (Fibonacci coins, draft) uses the same numbers as a number system. Year 1 used Fibonacci strips, and the grades 2–3 plan records that Fibonacci numbers were less engaging for most of that group; here the hook is the visible spokes-versus-spirals contrast and real pinecones, and Fibonacci counts arrive as an observation rather than as a sequence to extend. New here: irrational turning, best approximation, and a real-world claim with honest exceptions.

## App connection

Patterns and symmetry region, a "seed planter" family: the child sets a turn with a dial and watches seeds appear; puzzles: "make exactly 5 spokes", "make a head with no spokes up to 100 seeds", "how many spirals run clockwise in this picture?" Numbers region could carry the fraction-approximation side.

## Open questions

- Pinecone spiral counting is fiddly; whether 2–3 children can count reliably without an adult marking a start spiral is untested.
- The sheet generator does not exist yet; it is a small script for `lowell-math-circle-year-2/source/` when the week is built.
- Whether to include actual sunflower heads (seasonal) or photographs.
- Keep any claim about specific plants (pinecones usually 8 and 13, and so on) out of the guide unless a source is read for it.
