# Week 175 (draft plan): The chaos game

**Strand:** analysis and dynamics, with chance (app region "Chance and machines", or "Shapes and spaces"). **Deep-math field:** iterated function systems, contraction, fractals. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Mark the three corners of a triangle. From any starting dot, roll a die to choose a corner at random and put a new dot halfway between the current dot and that corner; repeat. The dots fill in the Sierpiński triangle, whatever the start. The mathematics behind it: each move is one of three maps f_i(p) = (p + v_i)/2 that halve all distances. Hutchinson's theorem (1981) says any finite set of such shrinking maps has exactly one nonempty compact set A with A = f₁(A) ∪ f₂(A) ∪ f₃(A), its attractor; here A is the Sierpiński triangle, three half-size copies of itself. Since each copy f_i(A) lies inside A, every move at least halves a dot's distance to A, so after k moves any start is within 2^(−k) of the triangle's size from A (eight moves on a 25 cm triangle leave less than 1 mm), which is why the first few dots are thrown away and why the start does not matter. That the random dots come arbitrarily close to *every* point of A, with probability 1, is the chaos-game theorem: Barnsley popularised the method (*Fractals Everywhere*, 1988), Elton (1987) proved an ergodic theorem for contractive systems, and Barnsley and Vince (arXiv 2010) proved it for general systems without contraction. There is an exact discrete picture too: starting at a corner, after k moves the dot can be at exactly 3^k places, (a, b)/2^k with a and b sharing no binary 1, which are the odd entries of Pascal's triangle (by Kummer's and Lucas's theorems; this links to draft 101). Each level keeps 3 of every 4 smaller triangles, so the area tends to 0 while the set has dimension log 3/log 2 ≈ 1.585. Changing the rule changes the picture, and some of it is provable: a square with halfway jumps reaches every one of its 4^k small squares and fills in evenly; a square where the same corner may not be chosen twice in a row keeps only 4·3^(k−1) of them, so it thins into a fractal; a triangle with jumps one third of the way fills the whole triangle (the three two-thirds-size copies overlap and cover it), while halfway jumps leave the middle open (the centre point is in no half-size corner copy). Many other rules are worth exploring experimentally; what they produce is observation unless someone proves it. Children can discover the empty middle triangle and its smaller copies, that the start does not matter after a few jumps, and, in grades 4–5, why no dot can land in the middle.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Chaos Game on a General Iterated Function System](https://arxiv.org/pdf/1005.0322). Michael F. Barnsley and Andrew Vince, arXiv 1005.0322 (2010). Random orbits converge to the attractor with probability one when each map is chosen with probability bounded below, without contraction; history from Hutchinson (1981), Barnsley (1988) and Elton (1987) (read November 4, 2026).
- [Chaos in the Classroom, chaos game section](https://math.bu.edu/DYSYS/chaos-game/node3.html). Robert L. Devaney, Boston University, 1995. A dot in a removed middle triangle is sent into ever smaller removed triangles, so the orbit appears to lie on the attractor (read November 4, 2026).
- [The Chaos Game](https://beltoforion.de/en/recreational_mathematics/chaos_game.php). beltoforion.de (a personal recreational-mathematics site). Variations: a square with halfway jumps gives an evenly filled area, not a fractal; rules forbidding the same corner twice in a row; other jump fractions (read November 4, 2026).
- Prior use with children: [Math Explorers' Club, lesson 4](https://pi.math.cornell.edu/~lipa/mec/lesson4.html). Cornell University; students roll a die with each of three colours on two faces, do 7 to 10 warm-up rolls, plot 20 to 30 points each on a transparency, and the teacher stacks the transparencies to reveal the triangle; it notes that hundreds of points are needed (read November 4, 2026). The page gives no grade level; its later questions (dimension, fern rules) suggest middle school and up.

## A kid-friendly way in

Materials per table: a printed equilateral triangle, side about 25 cm, with corners coloured red, blue and green; a die with two stickers of each colour (or the rule 1–2 red, 3–4 blue, 5–6 green); a ruler for 2–5; for K–1, a "halfway band", a rubber band cut open with its midpoint marked, stretched between the dot and the corner; a fine marker; one transparency sheet per table with the same triangle printed on it, laid over the paper so dots go on the transparency. Prep: print paper triangles and transparencies, sticker dice, mark bands, about 25 minutes.

Launch (3 minutes): on a large triangle on the board, a child picks a starting dot anywhere; roll, find halfway to that corner, dot; do four or five jumps. Say once that the first five dots are drawn faintly and do not count. Ask: "If every table makes 30 dots, what will the stack of all our sheets look like?" At the end, stack the transparencies on a window or projector.

## By band

- **K–1:** Make dots with the halfway band and stickers or a marker, 10 to 15 each. Before the stack: is there a place where no dot has landed yet? After the stack: point to the empty triangles, big and small.
- **2–3:** Measure halfway with a ruler. Start a dot inside the big empty middle triangle on purpose: where does the next dot go? Where does it go after two jumps? Find empty triangles of three sizes in the stacked picture and count how many of each size.
- **4–5:** Why can a dot, after its first jump, never land in the middle triangle? (Halfway from any point of the triangle to the red corner lands in the red corner's half-size triangle.) How many small triangles can hold the dot after two jumps, three jumps? Extension: try a square with halfway jumps, and a square where the same corner is never chosen twice in a row, and compare the pictures; or colour the odd numbers in Pascal's triangle and lay it beside the stack.

## Checked facts

- `check_week_175()`: starting at a corner, the points reachable after k halfway jumps (k ≤ 8) are exactly the 3^k grid points (a, b)/2^k with a AND b = 0, and each has C(a + b, a) odd.
- `check_week_175()`: 250 mm/2⁸ < 1 mm; level counts 3, 9, 27, 81; log 3/log 2 ≈ 1.585; a seeded run of 3,000 dots after 8 warm-up jumps never enters the open middle triangle.
- `check_week_175()`: square with halfway jumps reaches all 4^k cells; with "never the same corner twice" exactly 4·3^(k−1) cells (k ≤ 6); halfway copies miss the centroid, two-thirds-size copies cover every point of a fine grid.
- `check_week_175()`: with 27 equally likely level-3 triangles, a dot in each needs on average 27·H₂₇ ≈ 105 dots, so a class should pool well over 100 counted dots before the third-level holes are fully outlined.

## Nearest existing themes

Draft 101 (Bead machines and the odd triangle) reaches the same Sierpiński picture by parity in Pascal's triangle; this week reaches it by random jumps, and the checked fact above shows they are literally the same set of points, a natural return visit. Draft 127 (How long is a coastline?) measures fractal dimension of the Koch curve; atlas GA-29 (Cantor set) removes length to leave a dust. Week 92 (Fold-and-stretch predictions) has maps that *double* distances, so uncertainty spreads; here maps *halve* distances, so randomness produces a fixed shape. Week 80 (Midnight laboratory) moves a counter halfway to one end deterministically. New here: random iteration of contractions, independence of the start, and attractors as fixed points of a set of maps.

## App connection

Region "Chance and machines" (or "Shapes and spaces"), possible family "Dot machine": a child picks corners, a jump fraction and an optional rule (no repeats), and the machine plots 5,000 dots. Puzzle 1: "Which rule made this picture?" (match three pictures to three rules). Puzzle 2: "Choose a jump fraction for the triangle that leaves no holes." Puzzle 3: "Place a starting dot so the next dot lands in the blue corner's small triangle."

## Open questions

- Accuracy: do children's halfway marks stay accurate enough over 30 jumps for holes to show in a stack of 8 to 10 transparencies, and does the halving band work in K–1 hands? Untested.
- Transparency printing and a window or projector for stacking; a plain-paper fallback (one shared large sheet passed around) should be designed.
- Whether 2–3 children can stay engaged through 30 measured jumps, or whether 15 per child with more children per sheet is better.
- The beltoforion page is a personal site; a reviewer may want a second source for the square variations, which are checked here by computation.
