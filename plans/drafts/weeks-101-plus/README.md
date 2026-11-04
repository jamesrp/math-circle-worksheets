# Weeks 101–208: draft plans toward a wider corpus

November 3, 2026. James reversed the pause on new weeks the same day: near-term circle content is covered, and new themes should keep growing in the background as draft markdown plans (see the [corpus plan's Decisions](../../corpus-plan.md#decisions)). This folder holds 108 of them: Weeks 101–142 from November 3, then Weeks 143–175 and Weeks 176–208 from November 4, each time after James asked for more. Each is one page: the deep idea stated theorem-first, linked sources that were opened and read, a hands-on way in, an entry for each band, checked facts, the nearest existing themes, an app idea and open questions. They follow [TEMPLATE.md](TEMPLATE.md).

**Status.** Plans only: no student pages, facilitator guide, review card or pilot. Nothing here has been reviewed by James or tried with children. A plan becomes a week through the [worksheet workflow](../../../worksheet-workflow/README.md) once someone picks it.

## How they were chosen

1. **Map the library.** [coverage.py](coverage.py) counts the 101 library themes, 90 atlas families and 12 scouted drafts by catalog area and by a coarse deep-math field. Shape (30 themes) and chance (17) are deep; games and logic have 7 each, counting and symmetry 9, number 10. By field, analysis and dynamics (9 weeks, though 33 atlas families), topology (8) and logic and computation (13) are thinnest in the weeks children actually use. 24 concepts in the concept map have no week, among them binomial counts, lattice paths, groups, equilibria, continuity and the diagonal argument.
2. **Choose gaps.** Topics were kept when they had a theorem or open problem a mathematician finds compelling, a cheap physical entry for K–1, room for grades 4–5, and something new against the library, the atlas, the [scouted drafts](../../topic-scouting/README.md) and the Year 1 handouts (figurate numbers, Fibonacci strips, Pascal recursion and knights and knaves were already used). Wythoff (Week 8), Stern–Brocot (Week 31's return visit), sorting networks (Week 23) and substitution words (Week 76) were ruled out as already present; for the second batch, de Bruijn sequences were dropped too (Week 10's return visit and Week 33's bonus use them). The second batch leaned again on the thinnest strands (logic, games, networks, counting, symmetry) and on topology and analysis. The third batch went to games, networks, logic and analysis, the strands still thinnest after Week 175; Sprouts and Colonel Blotto (scouted drafts), matching cards with one shared symbol (Week 36), distinguishing colourings (Week 34), the liar's guessing game (Week 18), Tchoukaillon and Dots and Boxes (scouting set-asides) and 4×4 sudoku (near Week 5) were ruled out.
3. **Research and check.** Seventeen research passes (seven for the first batch, five each for the second and third), one per group, read real sources (papers, survey and expository articles, circle handouts) and cite only pages they opened. Every small number a plan quotes is asserted in a standard-library script, one per group; all seventeen pass. I reviewed each group's report and spot-checked plans before they went to `main`.

```sh
for f in plans/drafts/weeks-101-plus/check_*.py; do python3 "$f"; done
```

## The plans

| Week | Plan | Strand (app region) | Deep-math field | K–1 way in |
|---|---|---|---|---|
| 101 | [Bead machines and the odd triangle](week-101-galton-and-odd-pascal.md) | counting | binomial counts, Lucas's theorem mod 2 | colour odd numbers in Pascal's rows; drop beads by coin flips |
| 102 | [Domino diamonds](week-102-aztec-diamond.md) | counting | perfect matchings, the arctic circle | tile small Aztec diamonds; flip a 2×2 block |
| 103 | [Tower maps and one-switch codes](week-103-hanoi-maps-and-gray-codes.md) | counting | state graphs, Gray codes | walk a floor map of two-cup tower positions |
| 104 | [The sixteen-card square](week-104-sixteen-card-squares.md) | counting | orthogonal Latin squares, 36 officers | nine shape cards on a 3×3 mat |
| 105 | [Knight's tours on small boards](week-105-knights-tours.md) | networks | Hamiltonian cycles, Schwenk's theorem | hop a knight on 3×3 and lay counters |
| 106 | [Colouring maps](week-106-map-colouring.md) | networks | planar colouring, seven colours on a torus | two-crayon maps of whole lines and circles |
| 107 | [Mazes, walls and random trees](week-107-mazes.md) | networks | graph search, uniform spanning trees | hand-on-the-wall mazes; find a wall island |
| 108 | [Hailstone numbers](week-108-hailstone-numbers.md) | number | the open Collatz problem | a halving-and-tripling counter machine |
| 109 | [Sharing loaves the Egyptian way](week-109-egyptian-fractions.md) | number | unit fractions, a greedy monovariant | fold and share 2 loaves among 3 |
| 110 | [Fibonacci coins](week-110-fibonacci-coins.md) | number, games | Zeckendorf's theorem, Fibonacci Nim | pay amounts with no two neighbouring coins |
| 111 | [Staircase numbers](week-111-staircase-numbers.md) | number | consecutive sums and odd divisors | build cube staircases; find unbuildable totals |
| 112 | [Spreading claps around a circle](week-112-euclidean-rhythms.md) | number | Euclidean rhythms, even distributions | clap 3 beats on 8 plates |
| 113 | [One magic square](week-113-magic-squares.md) | number, symmetry | uniqueness up to the square's 8 symmetries | split 1–9 into rows of 15 |
| 114 | [Sunflower spirals](week-114-sunflower-spirals.md) | number | the golden angle, Diophantine approximation | seed stickers at a quarter turn and a golden turn |
| 115 | [Wallpaper patterns](week-115-wallpaper-patterns.md) | symmetry | the 17 plane groups, Conway's orbifolds | sticker each spin point in a pattern |
| 116 | [Kaleidoscopes](week-116-kaleidoscopes.md) | symmetry | dihedral groups, Leonardo's theorem | count copies in hinged mirrors |
| 117 | [Commutator puzzles](week-117-commutator-puzzles.md) | symmetry | commutators, parity, permutation groups | two rings of animal tokens: do, do, undo, undo |
| 118 | [Card magic](week-118-card-magic.md) | symmetry, logic | Gilbreath's principle, the five-card trick | perform the colour-pairs trick and try to break it |
| 119 | [Juggling patterns](week-119-juggling-patterns.md) | symmetry | siteswaps, the average theorem | colour-strip throw patterns; spot crashes |
| 120 | [Gems made only of triangles](week-120-eight-deltahedra.md) | shape | the eight convex deltahedra | magnetic triangle tiles; count faces |
| 121 | [Flat patterns that fold into a box](week-121-cube-nets.md) | shape | the 11 cube nets, Dürer's open problem | fold six-square shapes around a cube |
| 122 | [Tangram shapes with no dents](week-122-convex-tangrams.md) | shape | the 13 convex tangrams | fill convex outlines |
| 123 | [Guards in a gallery](week-123-gallery-guards.md) | shape | Chvátal's theorem, Fisk's colouring proof | can one guard see the whole tape room? |
| 124 | [One straight cut](week-124-fold-and-cut.md) | shape | the fold-and-cut theorem | fold once, cut once, predict the shape |
| 125 | [One tile that never repeats](week-125-one-tile-never-repeats.md) | symmetry, shape | the hat and spectre monotiles (2023) | build a floor of hat tiles |
| 126 | [Cut and rearrange](week-126-cut-and-rearrange.md) | shape | Wallace–Bolyai–Gerwien, Dehn's invariant | remake a cut square as other shapes |
| 127 | [How long is a coastline?](week-127-how-long-is-a-coastline.md) | shape, analysis | fractal dimension | string along a wiggly coast |
| 128 | [Splitting necklaces](week-128-splitting-necklaces.md) | shape | necklace splitting, Borsuk–Ulam | share a two-colour bead strip with few cuts |
| 129 | [The wobbly table and the crumpled map](week-129-wobbly-table-crumpled-map.md) | shape | intermediate values, Brouwer's fixed point | turn a stool until it stops rocking |
| 130 | [Dropping sticks and noodles on lines](week-130-buffons-needle-and-noodle.md) | chance | Buffon and Barbier, expectation | drop toothpicks; sort touching and not |
| 131 | [Collecting every sticker](week-131-collecting-every-sticker.md) | chance | the coupon collector, harmonic numbers | roll until every face appears |
| 132 | [Coin-pattern races](week-132-penneys-game.md) | chance, games | Penney's game, nontransitivity | race two colour patterns |
| 133 | [Better in both, worse together](week-133-simpsons-paradox.md) | chance | Simpson's paradox | pick the better bag, then pour them together |
| 134 | [Peg jumps and Conway's soldiers](week-134-conways-soldiers.md) | games | colouring invariants, golden-ratio weights | small peg-jump puzzles with colour stickers |
| 135 | [The trust game](week-135-trust-game.md) | games | Nash equilibrium, repeated games | share-or-keep bean game |
| 136 | [Sealed-bid auctions](week-136-sealed-bid-auctions.md) | games | Vickrey auctions, truthful bidding | bid cube towers behind a folder |
| 137 | [The Game of Life](week-137-game-of-life.md) | logic | cellular automata, Garden of Eden | run three-counter starts on a grid |
| 138 | [Tiny machines and the busy beaver](week-138-busy-beaver.md) | logic | computability; BB(5) proved in 2024 | be the machine head on a row of cups |
| 139 | [Secret messages and two padlocks](week-139-secret-messages.md) | logic | frequency analysis, key exchange | act out the two-padlock box |
| 140 | [Proving without telling](week-140-proving-without-telling.md) | logic | zero-knowledge proofs, secret sharing | the cave game: catch a bluffer |
| 141 | [Leaning towers off the table](week-141-leaning-towers.md) | analysis (shape) | the harmonic series diverges | how far can one block stick out? |
| 142 | [A path through every point](week-142-space-filling-curves.md) | analysis (shape) | Hilbert's space-filling curve | walk a floor path through every square |
| 143 | [Domino computers](week-143-domino-computers.md) | logic | Boolean circuits, NAND is universal | build wires, forks and merges; predict which pushes knock the cup |
| 144 | [The MU puzzle](week-144-mu-puzzle.md) | logic | formal systems, an invariant mod 3 | a cube pile you may double or take 3 from: which piles appear? |
| 145 | [The fake coin and the balance](week-145-fake-coin-balance.md) | logic | information bounds, Dyson's 12 coins | find the heavy one among 3, 4 and 9 containers |
| 146 | [Easy to check, hard to find](week-146-easy-to-check-hard-to-find.md) | logic | certificates, P versus NP | split stick bags into two equal rows; check a friend's |
| 147 | [Pairing strategies](week-147-pairing-strategies.md) | games | positional games, pairing blocks | the strip game: dominoes stop three in a row |
| 148 | [Guess two-thirds of the average](week-148-guess-two-thirds.md) | games | iterated dominance, equilibrium | tower rounds aiming at half the level |
| 149 | [Racetrack](week-149-racetrack.md) | games | shortest paths in a state graph | park a floor car in 4, 6 and 9 squares |
| 150 | [Same network or different?](week-150-same-network-or-different.md) | networks | graph isomorphism, invariants | rearrange a bead network to match a drawing |
| 151 | [Instant Insanity](week-151-instant-insanity.md) | networks | 2-factors of the opposite-face graph | four colours on the front of a cube tower |
| 152 | [Who is most important?](week-152-who-is-most-important.md) | networks, chance | stationary distributions, PageRank | walk the room dropping counters; compare cups |
| 153 | [Soap-film shortcuts](week-153-soap-film-shortcuts.md) | networks, shape | Steiner trees, the Steiner ratio (open) | dip peg frames; compare string lengths |
| 154 | [Bulgarian solitaire](week-154-bulgarian-solitaire.md) | counting | partitions, a staircase every start reaches | six counters: do the move until something happens |
| 155 | [Weird dice](week-155-weird-dice.md) | counting, number | generating functions, Sicherman dice | race sums with the weird pair and ordinary dice |
| 156 | [Lining up by height](week-156-lining-up-by-height.md) | counting | Erdős–Szekeres, pigeonhole labels | can five children avoid three up or three down? |
| 157 | [Remainders that repeat](week-157-remainders-that-repeat.md) | number | periods of 1/p, Artin's conjecture (open) | deal counters onto 7 plates; watch leftovers repeat |
| 158 | [Squares from two squares](week-158-squares-from-two-squares.md) | number | Fermat's two-squares theorem, Zagier's proof | add pairs of tile squares; find unmakeable totals |
| 159 | [Rectangles of a number](week-159-rectangles-of-a-number.md) | number | divisor sums, perfect numbers (odd ones open) | every rectangle from 6, 7, 8 and 12 tiles |
| 160 | [Times tables on a circle](week-160-times-tables-on-a-circle.md) | number (shape) | envelopes, epicycloids, multiplicative order | yarn times 2 on a 10-notch plate |
| 161 | [Flexagons](week-161-flexagons.md) | symmetry | state graphs of flexing | sticker each new face of a trihexaflexagon |
| 162 | [Thirty coloured cubes](week-162-thirty-coloured-cubes.md) | symmetry | orbit counting, the cube's rotation group | how many red-and-blue cubes are different? (10) |
| 163 | [Arrow multiplication](week-163-arrow-multiplication.md) | symmetry | complex numbers, Gaussian primes | quarter turns and half turns on a floor mat |
| 164 | [Three rings that hold together](week-164-borromean-rings.md) | shape | Brunnian links; no round Borromean rings | build the magic three from a recipe card |
| 165 | [Inside or outside?](week-165-inside-or-outside.md) | shape | the Jordan curve theorem, ray parity | jump in and out of rope loops |
| 166 | [You can't comb a hairy ball](week-166-hairy-ball.md) | shape | Poincaré–Hopf, Euler characteristic | arrow stickers on a swim ring and a beach ball |
| 167 | [Walking a loop](week-167-walking-a-loop.md) | shape | turning number, Whitney–Graustein | walk tape paths counting left and right turns |
| 168 | [Folding beats the compass](week-168-folding-beats-the-compass.md) | shape | origami constructions, trisection | fold thirds by eye, then by the magic fold |
| 169 | [Stacking oranges](week-169-stacking-oranges.md) | shape | Kepler's conjecture, Hales and Flyspeck | build square and triangular ball pyramids |
| 170 | [Shapes that build bigger copies of themselves](week-170-rep-tiles.md) | shape | rep-tiles, substitution tilings | pattern-block doubles; a big L from four Ls |
| 171 | [Shared birthdays](week-171-shared-birthdays.md) | chance | the birthday problem, counting pairs | teddy parties on a 6-box calendar |
| 172 | [First digits](week-172-first-digits.md) | chance, number | Benford's law | sort a powers-of-2 deck by first digit |
| 173 | [How long does Snakes and Ladders last?](week-173-snakes-and-ladders.md) | chance | Markov chains, expected game length | play a 20-square board and line up the roll towers |
| 174 | [Shrinking piles](week-174-shrinking-piles.md) | chance (analysis) | exponential decay, maxima of waiting times | pour off heads; build a falling staircase |
| 175 | [The chaos game](week-175-chaos-game.md) | analysis (chance) | iterated function systems, Sierpiński | halfway-jump dots, then stack everyone's sheets |
| 176 | [Hide and seek with unequal prizes](week-176-hide-and-seek.md) | games | zero-sum games, the minimax theorem | hide a bean in one hand; prizes 1 and 2 |
| 177 | [Pirates share the gold](week-177-pirates-share-the-gold.md) | games | backward induction with voting | act out two, then three pirates splitting coins |
| 178 | [Bidding for turns](week-178-bidding-for-turns.md) | games | Richman games, random-turn games | bid chips for each move in a short race |
| 179 | [Sharing the taxi fare](week-179-sharing-the-taxi-fare.md) | games | the Shapley value, the airport rule | share a ride along a floor road with three stops |
| 180 | [Who holds the power?](week-180-who-holds-the-power.md) | games | weighted voting, power indices | vote with stacks of cubes; who can swing it? |
| 181 | [A new road makes traffic worse](week-181-a-new-road-makes-traffic-worse.md) | games (networks) | Braess's paradox, price of anarchy | drive four cars on a floor map, then add a road |
| 182 | [Passing secrets by phone](week-182-gossip-calls.md) | networks | the gossip problem, 2n − 4 calls | pass secret cards in pairs until everyone knows all |
| 183 | [Can everyone get a partner?](week-183-dance-partners.md) | networks | Hall's theorem, König's theorem | pair children with cards they accept; find the stuck group |
| 184 | [Your friends have more friends](week-184-your-friends-have-more-friends.md) | networks (chance) | the friendship paradox, sums of squares | a yarn friendship web with sticky-note counts |
| 185 | [Making every street one-way](week-185-one-way-streets.md) | networks | Robbins' theorem, lifeline roads | put arrows on a town map and test every trip |
| 186 | [How many trees on numbered pegs?](week-186-counting-trees.md) | networks (counting) | Cayley's formula, Prüfer codes | join 3 and 4 pegs with string, no loops |
| 187 | [Can the fire cross the forest?](week-187-crossing-the-forest.md) | networks (chance) | percolation, crossing chance 1/2 | colour a hexagon board by coin flips |
| 188 | [A few shortcuts make a small world](week-188-small-worlds.md) | networks (chance) | small-world networks, graph distance | pass a note round a ring, then add yarn shortcuts |
| 189 | [Guessing your own hat](week-189-guessing-your-hat.md) | logic | hat games, Hamming codes | three-player hat game with sticker dots |
| 190 | [Follow the loop to find your card](week-190-hundred-prisoners.md) | logic | permutation loops, the 100 prisoners | four cups, two looks each, follow the loop |
| 191 | [Say what you see](week-191-look-and-say.md) | logic | look-and-say, Conway's cosmological theorem | read rows of counters aloud to build the next |
| 192 | [Short codes for common letters](week-192-shortest-codes.md) | logic | Huffman codes, the Kraft budget | build a code tree for a short message |
| 193 | [The ant that builds a highway](week-193-langtons-ant.md) | logic | Langton's ant, an open problem | be the ant on a floor grid of flip cards |
| 194 | [The endless hotel and the strip nobody listed](week-194-hilberts-hotel.md) | logic | infinite sets, Cantor's diagonal | move along a line of rooms; the 3-by-3 diagonal game |
| 195 | [Ordering stones with a balance](week-195-ordering-stones.md) | logic | comparison sorting, log2 n! bound | order three, then four stones with a balance |
| 196 | [Ringing every order of the bells](week-196-change-ringing.md) | symmetry | change ringing, Hamiltonian cycles, cosets | stand in a row and swap neighbours to a beat |
| 197 | [Star patterns from crossing lines](week-197-star-patterns.md) | symmetry | Hankin's method, star polygons | extend lines from edge midpoints on a dot grid |
| 198 | [Nibble a tile](week-198-nibble-a-tile.md) | symmetry (shape) | tiling by translation, Beauquier–Nivat | nibble a card square and tape the bite opposite |
| 199 | [Steering a card with perfect shuffles](week-199-perfect-shuffles.md) | symmetry, number | faro shuffles, multiplicative order | perfect-shuffle eight cards and track one |
| 200 | [Kaprekar's sorting machine](week-200-kaprekars-routine.md) | number | Kaprekar's routine, proof by cases | sort digit cards big-first and small-first |
| 201 | [Two prime towers make every even tower?](week-201-prime-pairs.md) | number | Goldbach's conjecture (open) | build even towers from two prime towers |
| 202 | [Halfway to the wall](week-202-halfway-to-the-wall.md) | analysis | geometric series, picture proofs | fold and cut halves of a sheet |
| 203 | [Press it again](week-203-press-it-again.md) | analysis | fixed points, contraction mappings | a halfway-between ribbon rule, again and again |
| 204 | [The fastest slide](week-204-fastest-slide.md) | analysis (shape) | the brachistochrone, the cycloid | race marbles on straight and curved ramps |
| 205 | [Pi from polygons](week-205-pi-from-polygons.md) | analysis (shape) | Archimedes' bounds, limits | wrap string round cans and lids |
| 206 | [Folding the square root of two](week-206-folding-the-square-root-of-two.md) | number (analysis) | √2 is irrational, Theon's ladder | cut the biggest squares off a sheet of paper |
| 207 | [Random walks home](week-207-random-walks-home.md) | chance | Pólya's recurrence theorem | walk a floor number line by coin flips |
| 208 | [Long runs](week-208-long-runs.md) | chance | longest runs, the log n law | make one real and one fake coin list |

By main strand, Weeks 101–142: counting 4, networks 3, number 7, symmetry 6, shape 9, chance 4, games 3 (plus 110 and 132), logic 4, analysis 2. Weeks 143–175: logic 4, games 3, networks 4, counting 3, number 4, symmetry 3, shape 7, chance 4, analysis 1. Weeks 176–208: games 6, networks 7, logic 7, symmetry 4, number 3, analysis 4, chance 2 (no counting or shape, which were already deeper). Together: counting 7, networks 14, number 14, symmetry 13, shape 16, chance 10, games 12, logic 15, analysis 7. By field, the plans add most where the weeks were thinnest: topology and analysis (106, 127, 128, 129, 141, 142), logic and computation (137–140) and groups (115–117). They give first weeks to binomial counts and lattice paths (101), groups (115–117), equilibria (135, 136), continuity and connectedness (129, 142) and computability (138). The second batch adds topology (164–167), computation and complexity (143, 144, 146), equilibria and positional games (147, 148), Markov chains (152, 173) and group actions (162). The third adds cooperative and zero-sum game theory (176, 179, 180), selfish routing (181), matching duality (183), percolation (187), infinite sets and the diagonal argument (194), information theory (192) and calculus-flavoured analysis (202–205).

## Strongest picks

From Weeks 101–142:

1. **[One straight cut](week-124-fold-and-cut.md).** A research theorem (any straight-line drawing can be cut out with one cut after folding) that a kindergartner can test with paper and scissors, with a grade 4–5 question about how few folds each shape needs.
2. **[Gems made only of triangles](week-120-eight-deltahedra.md).** Magnetic triangle tiles, a classroom-wide hunt, and a complete answer: exactly eight convex shapes, and the missing 18 is a genuine surprise.
3. **[Hailstone numbers](week-108-hailstone-numbers.md).** An open problem children can run with counters, with Tao's 2019 theorem and computer checks as the honest story of what mathematicians know.
4. **[Tiny machines and the busy beaver](week-138-busy-beaver.md).** Children act as the machine; the record holders for 2, 3 and 4 states are checkable, and BB(5) was settled by an online collaboration in 2024. The age fit for grades 2–3 is the open question.
5. **[Leaning towers off the table](week-141-leaning-towers.md).** Blocks at a table edge make a divergent series physical: four blocks hang a whole block past the edge, and with enough blocks the overhang has no limit.

Close behind: [Proving without telling](week-140-proving-without-telling.md) (cups over a coloured map), [Splitting necklaces](week-128-splitting-necklaces.md) (a sliding-window proof children can follow) and [Peg jumps and Conway's soldiers](week-134-conways-soldiers.md), which answers the scouting set-aside with a K–1 entry.

From Weeks 143–175:

1. **[Lining up by height](week-156-lining-up-by-height.md).** Children are the material: five in a line always hide three going up or three going down, and grades 4–5 can follow the pair-label proof that 10 people force 4. A theorem from 1935 with a sharp bound children can build (3 2 1 6 5 4 9 8 7).
2. **[How long does Snakes and Ladders last?](week-173-snakes-and-ladders.md).** A game every child knows, an exact answer worked backward from the finish, and a computed surprise: adding a ladder can make the game longer.
3. **[Three rings that hold together](week-164-borromean-rings.md).** Three rings that fall apart if any one is cut, built from a recipe card; the deep fact (they cannot all be flat circles) is a 1987 theorem.
4. **[Domino computers](week-143-domino-computers.md).** Falling dominoes become logic gates; NAND alone builds everything, and finding the fewest gates for each job is a real search grades 4–5 can run.
5. **[The chaos game](week-175-chaos-game.md).** Random halfway jumps from a shared sheet fill in the Sierpiński triangle, and the reachable points match the odd numbers of Pascal's triangle from draft 101.

Close behind: [Guess two-thirds of the average](week-148-guess-two-thirds.md) (a whole-room game with published data from real players), [The MU puzzle](week-144-mu-puzzle.md) (a K–1 cube-pile version of a famous impossibility) and [Thirty coloured cubes](week-162-thirty-coloured-cubes.md).

From Weeks 176–208:

1. **[Follow the loop to find your card](week-190-hundred-prisoners.md).** A strategy that looks impossible works a third of the time, and the reason is the loops children already met in Week 3; with four cups the whole answer (5/12) is a count they can finish.
2. **[A new road makes traffic worse](week-181-a-new-road-makes-traffic-worse.md).** Four toy cars on a floor map, each choosing the quickest road, all get slower when a shortcut opens. A real surprise with arithmetic K–1 can follow.
3. **[The fastest slide](week-204-fastest-slide.md).** Marbles race down straight and curved ramps; the curve wins, and the best curve is a 1696 challenge problem with computed race times.
4. **[Pirates share the gold](week-177-pirates-share-the-gold.md).** Acting out two, three, then five pirates makes backward induction a story, and the lopsided answer (98, 0, 1, 0, 1) is memorable.
5. **[Guessing your own hat](week-189-guessing-your-hat.md).** A team game where passing is allowed and the best strategy wins 3 times in 4, because wrong guesses pile up together.

Close behind: [Ringing every order of the bells](week-196-change-ringing.md) (children are the bells), [Can the fire cross the forest?](week-187-crossing-the-forest.md) (after Hex) and [Bidding for turns](week-178-bidding-for-turns.md).

## Overlaps and weak spots to settle in review

Weeks 101–142:

- **107 Mazes (settled November 4).** Stays a new week, centred on when the hand-on-the-wall rule works (no wall islands), Trémaux's method and Wilson's fair random mazes. "A perfect maze is a tree" repeats Week 53 and atlas GA-25 and AD-05, so it is now a two-minute bridge, not a task. Run it after Week 91, whose rotor cards double as Wilson's arrow cards.
- **102 Domino diamonds (settled November 4).** Stays a new week, not a Week 1 return visit: the count 2^(n(n+1)/2), the complete-list argument and the arctic circle are new; only the flip move is shared. Schedule it after Week 1 and reuse Week 1's flip launch.
- **104 Sixteen-card square:** its 3×3 entry is near Week 36; a published "144 solutions" figure conflicts with the computed counts (6912 without diagonals; 1152 with, which is 144 up to the square's symmetries). The plan flags it.
- **117 Commutator puzzles** overlaps the scouting set-aside "sliding tokens"; build one, not both.
- **135 Trust game:** its one-round lesson repeats atlas AP-23; the repeated game and tournament are the new part.
- **110 and 114** lean on Fibonacci numbers, which the [grades 2–3 plan](../../grades-2-3-year-a.md) records as less engaging for most of last year's group.
- **111 Staircase numbers** shares rods with Week 89; **113 Magic squares** must stay a symmetry argument, not arithmetic practice.
- No prior use with K–5 children was found for 117, 120, 125, 128, 136 and 138; several have prior use only with grades 7 and up.
- Not confirmed from a page that was read, and flagged in each plan: the kidney-stone subgroup counts (133), the year of Goldwasser, Micali and Rackoff's paper (140), a direct source for the undecidability of Life (137), and some classic dates cited only through secondary sources (108, 109, 120, 122, 126).

Weeks 143–175:

- **145 Fake coin** largely duplicates the planned Year 3 return visit rv-6 (weighing with three outcomes); keep its heavy-or-light case as the distinct part, or fold it into rv-6.
- **159 Rectangles of a number** repeats Week 96's rectangle picture and Year 1's divisor toggling; divisor sums and perfect numbers are new. A return visit may suit it better than a week.
- **151 Instant Insanity and 162 Thirty coloured cubes** both use coloured cubes with different mathematics; schedule them apart.
- **153 Soap-film shortcuts** is exactly the move Week 53 forbids (new junctions), so frame it as Week 53's pair. **150** shares its drag-the-dots action with the scouted untangling draft, and **156** could serve as the Ramsey scouting draft's return visit.
- **167 Walking a loop** overlaps Week 65's "left minus right is 4"; the plan centres figure eights, stars and the turtle rule. **169**'s pyramid counts repeat Year 1's figurate numbers; **165** shares its parity trick with 106; **144** uses the same invariant move as Week 2 and atlas AP-25.
- **161 Flexagons (checked November 4):** a strip-folding simulation corrected two outer labels in the hexahexaflexagon face map and confirms 6 faces, 9 states, 12 flex links and the 12-flex Tuckerman traverse. A real folded flexagon is still the last check.
- No prior use with K–5 children was found for 143, 144, 145, 147, 149, 150, 162, 163, 166, 173 and 174.
- Not confirmed from a page that was read, and flagged in each plan: Drensky's "exactly k(k−1) moves" (the check shows it is only the maximum; 154), the best proven Steiner-ratio bound (sources differ; 153), the Beardon paper beyond its abstract (160), a recent odd-perfect-number bound (159), the board size in Allis's gomoku result (147), a real-data Benford table (172), and some classic dates (157, 158, 159, 164).

Weeks 176–208:

- **Better as return visits than weeks:** 186 counting trees (atlas AD-04 and AD-05 already have Prüfer codes and the 16 trees; fold into draft 150 or a return visit), 199 perfect shuffles (Week 3's grades 4–5 problems already reach 8 out-shuffles for 52 cards; a Week 3 encore), 195 ordering stones (Week 23's counting bound) and 197 star patterns (Week 4's star polygons, draft 115's symmetry).
- **Atlas families without a K–1 entry:** 176 (AP-22, same 2/3 numbers, and Week 24's bonus), 192 (AP-29) and 194 (AD-02 and Week 82) each propose to be that family's full-band week rather than run beside it. 181's Pigou part repeats AP-23.
- **203 Press it again** overlaps Week 93 (the same averaging fractions), atlas GA-36 and draft 168's pinch game; the plan proposes sorting calculator machines by convergence speed instead. **206** shares √2 material with Week 93, AD-10 and draft 170; the irrationality proof is the new part. **202** keeps Week 80's halfway walk to a two-minute launch.
- **200 Kaprekar** replaces draft 108's Kaprekar side station if both are built. **183** is near Week 13 (König's theorem is a case of max-flow min-cut). **187** should come after the Hex scouting draft. **189**'s seven-player step repeats Week 18's code.
- No prior use with K–5 children was found for most of Weeks 176–208; exceptions are a Princeton Friends School sheet (176), a Waterloo CEMC grades 7–8 handout (177), a Wellesley grade 7 module (180) and JRMF's gossip sheet (182), all for older children.
- Not confirmed from a page that was read, and flagged in each plan: Stewart's 1999 pirate column (177), Shapley 1953 and Banzhaf 1965 (cited through later texts; 179, 180), Huffman 1952 beyond its title page (192), who first proved the ant's path unbounded (sources disagree; 193), White 1983 beyond its abstract (196), and the Cayley, Borchardt and Prüfer dates (186).

## Next

James picks what, if anything, moves forward. A chosen plan goes through the worksheet workflow's outline, writer, critic and reviser stages, then a home pilot before the circle. Catalog draft records (`catalog/drafts/`) are not yet written for these plans, so they do not appear in the explorer.
