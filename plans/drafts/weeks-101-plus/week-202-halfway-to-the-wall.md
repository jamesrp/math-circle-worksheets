# Week 202 (draft plan): Halfway to the wall

**Strand:** analysis, with number (app region "Shapes and spaces"). **Deep-math field:** geometric series, limits, picture proofs. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

For any ratio r with −1 < r < 1, the geometric series 1 + r + r² + … converges to 1/(1 − r): the partial sum of the first n + 1 terms is exactly (1 − r^(n+1))/(1 − r), and r^(n+1) shrinks below any tolerance. For |r| ≥ 1 the terms do not shrink and the series has no sum. Two cases carry the week. Halving: 1/2 + 1/4 + 1/8 + … = 1, because after n steps the part not yet covered is exactly 1/2^n, the size of the last step. Quartering: 1/4 + 1/16 + 1/64 + … = 1/3, by a square picture: take a unit square, cut it into four quarters and keep cutting the top-right quarter; at every level the L-shaped band just removed is three equal squares, one shaded, so the shaded part is exactly one third of everything removed so far, and in the limit one third of the whole square. Archimedes used this series (in the form 1 + 1/4 + 1/16 + … = 4/3) to find the area of a parabolic segment, though historians differ on whether he summed infinitely many terms or argued only with finite sums and a double reductio. "Converges" has a precise meaning: the partial sums come within any tolerance of the sum and stay there (the definition Huggett credits to Cauchy). Terms shrinking to zero is necessary but not enough: the harmonic series 1 + 1/2 + 1/3 + … diverges (draft 141), while the halving series starting at 1 never reaches 2. Zeno of Elea (born about 490 BC) argued that a runner must first reach the halfway point, then half the rest, and so on through infinitely many stages, so motion is impossible; Achilles can never catch the tortoise. The standard modern reply is that infinitely many distances (and times) can have a finite sum, so the run takes finite time. Philosophers still discuss whether that fully answers Zeno (whether an infinite sequence of acts can be completed, the "supertask" question), and the plan should present this honestly as history and philosophy, not as settled by the arithmetic. Proved: the partial-sum formula, convergence for |r| < 1, both picture proofs. Children can discover that halfway steps never reach the wall yet never pass it, that the pieces of a folded strip fill it exactly, that the shaded squares are one third, and, in grades 4–5, why each picture is a proof and why 0.999… = 1.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Zeno's Paradoxes](https://plato.stanford.edu/archives/spr2006/entries/paradox-zeno/). Nick Huggett, Stanford Encyclopedia of Philosophy (Spring 2006 edition). Zeno's birth about 490 BC; the Dichotomy (Aristotle, Physics 239b11) and Achilles (via Simplicius); the convergent-series "standard solution" and its limits, including supertasks and Aristotle's potential infinity (read November 4, 2026).
- [1/4 + 1/16 + 1/64 + 1/256 + ⋯](https://en.wikipedia.org/wiki/1/4_%2B_1/16_%2B_1/64_%2B_1/256_%2B_%E2%8B%AF). Wikipedia, secondary pointer. The square and triangle pictures (Ajose and Nelsen, Mathematics Magazine 1994; Nelsen and Alsina, Math Made Visual), Archimedes' Quadrature of the Parabola, Propositions 23–24, and the historians' disagreement about whether he summed the infinite series (read November 4, 2026).
- [Achilles and the Tortoise](https://undergroundmathematics.org/sequences/achilles-and-the-tortoise). Underground Mathematics, University of Cambridge. 100 m head start, speeds 100 and 1 m per minute, catch-up stages summing to about 101.01 m in about 1 minute 0.6 seconds (read November 4, 2026).
- Prior use with children: [Diminishing Returns](https://nrich.maths.org/6700). NRICH, ages 11 to 14. Shading squares to show 1/4 + 1/16 + … = 1/3 and a second pattern giving 2/3 (read November 4, 2026).
- Prior use with children: [CHAMP Solutions, Spring 2014 Lesson 6](https://champ-outreach.org/images/2014-Spring/Lesson6/CHAMP-Solutions.pdf). CHAMP math circle (University of Houston outreach for middle and high school students). A volunteer may only "walk half-way to the wall", then 1/2 + 1/4 + … by a shaded-square area model (read November 4, 2026). No K–5 circle handout was found.

## A kid-friendly way in

Materials: masking tape for a start line about 4 m from a wall, a "wall" of cardboard if the room lacks one, strips of paper (about 3 by 28 cm, two per child), squares of paper (15 cm, two per child), crayons, scissors. Prep: cut strips and squares, tape the line, about 15 minutes. Launch (3 minutes): one child stands at the line; the rule is "always walk exactly halfway to the wall". The group predicts, then counts steps; after a few steps the child is shuffling heel to toe. Then everyone folds a strip in half, colours one half, folds the uncoloured half in half, colours one part, and so on, to ask: does the coloured part ever fill the strip? Does it ever spill over?

Suggested hour: 0–5 the halfway walk; 5–20 strip folding (K–1 stop here with sorting and comparing); 20–40 the square picture; 40–55 Achilles story and the band questions; 55–60 Zeno as history.

## By band

- **K–1:** Walk halfway to the wall, then halfway again; do you ever touch it? Fold and colour a strip; lay coloured pieces end to end to rebuild it. Is every piece smaller than the one before? Is there always some white left?
- **2–3:** Fold and colour the square picture (cut a square into four, shade one, keep cutting the corner). How much of the square ends up shaded? Children can compare shaded and unshaded bands by cutting them out and stacking them.
- **4–5:** Explain why the shaded part is exactly a third, and why the halving strip adds to exactly 1 (the missing piece is always the size of the last one). Achilles and the tortoise: how far until Achilles catches up? Then 0.999… and 1/2 + 1/8 + 1/32 + …: what pictures show these sums?

## Checked facts

- `check_week_202()`: the halving partial sums are exactly 1 − 1/2^n; a 400 cm walk needs 9 halving steps to come within 1 cm (8 steps leave 1.5625 cm).
- `check_week_202()`: 1/4 + … + 1/4^n = (1 − 1/4^n)/3 < 1/3; at every level of the square picture the shaded area is exactly one third of the removed area.
- `check_week_202()`: the general formula (1 − r^(n+1))/(1 − r) for r = 1/2, 1/3, 1/4, 1/10, 2/3; ten nines give 1 − 10^(−10); 1/2 + 1/8 + 1/32 + … approaches 2/3 from below; 1/3 in binary is 0.0101….
- `check_week_202()`: Achilles catches the tortoise at 10000/99 ≈ 101.01 m after 100/99 minutes ≈ 60.6 s, both by the series and by solving 100t = 100 + t.
- `check_week_202()`: the halving series from 1 stays below 2, while 1 + 1/2 + 1/3 + 1/4 = 25/12 already exceeds 2.
- Zeno's dates and arguments, and the philosophical debate, are cited from Huggett; Archimedes' use of the series is cited through the Wikipedia pointer.

## Nearest existing themes

Week 80 (Midnight laboratory) already moves a counter halfway to END and contrasts it with Thomson's lamp, so the halfway walk on its own is not new; atlas GA-12 compares the halving and harmonic machines on fraction strips, and GA-03 uses widths ε/2, ε/4, … to cover all fractions. Draft 141 (Leaning towers) is the divergent partner; draft 174 halves a pile randomly; draft 175 keeps 3/4 of each triangle. Week 48 traps areas between inner and outer counts. What is genuinely new: a series that converges to a value other than 1 (1/3, 2/3, 4/3) found by a picture, picture proofs as proofs (the "three equal squares" argument), and Zeno as a historical argument children can debate. To avoid repeating Week 80, keep the walk to the two-minute launch and centre the hour on the square picture and other ratios. Year 1's paradoxes handout (Problem Set 11) was about self-reference (Protagoras, a list of sentences), not Zeno, so there is no overlap there.

## App connection

Region "Shapes and spaces", possible family "Shade the rest": a square or triangle board where the child chooses a piece to cut into k equal parts and shades some of them; the machine repeats the move and shows the running shaded fraction. Puzzle 1: "Make a pattern that shades exactly one third of the square forever." Puzzle 2: "Shade exactly 2/3 using only halvings." Week 48's "Area traps" family could host the same board with inside and outside counts.

## Open questions

- K–1 fit: is the strip folding meaningful after four or five folds, when pieces become hard to colour? A pre-printed strip with marked halves might work better.
- Does the halfway walk feel too much like Week 80 for returning children? If so, start with the strip.
- How much Zeno to include: a two-minute story, or a whole-group debate for grades 4–5? The supertask question is open in philosophy and should be framed that way.
- Is "0.999… = 1" a productive 4–5 question here or a distraction?
