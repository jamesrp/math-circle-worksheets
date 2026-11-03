# Weeks 101–142: draft plans toward a wider corpus

November 3, 2026. James reversed the pause on new weeks the same day: near-term circle content is covered, and new themes should keep growing in the background as draft markdown plans (see the [corpus plan's Decisions](../../corpus-plan.md#decisions)). This folder holds 42 of them. Each is one page: the deep idea stated theorem-first, linked sources that were opened and read, a hands-on way in, an entry for each band, checked facts, the nearest existing themes, an app idea and open questions. They follow [TEMPLATE.md](TEMPLATE.md).

**Status.** Plans only: no student pages, facilitator guide, review card or pilot. Nothing here has been reviewed by James or tried with children. A plan becomes a week through the [worksheet workflow](../../../worksheet-workflow/README.md) once someone picks it.

## How they were chosen

1. **Map the library.** [coverage.py](coverage.py) counts the 101 library themes, 90 atlas families and 12 scouted drafts by catalog area and by a coarse deep-math field. Shape (30 themes) and chance (17) are deep; games and logic have 7 each, counting and symmetry 9, number 10. By field, analysis and dynamics (9 weeks, though 33 atlas families), topology (8) and logic and computation (13) are thinnest in the weeks children actually use. 24 concepts in the concept map have no week, among them binomial counts, lattice paths, groups, equilibria, continuity and the diagonal argument.
2. **Choose gaps.** Topics were kept when they had a theorem or open problem a mathematician finds compelling, a cheap physical entry for K–1, room for grades 4–5, and something new against the library, the atlas, the [scouted drafts](../../topic-scouting/README.md) and the Year 1 handouts (figurate numbers, Fibonacci strips, Pascal recursion and knights and knaves were already used). Wythoff (Week 8), Stern–Brocot (Week 31's return visit), sorting networks (Week 23) and substitution words (Week 76) were ruled out as already present.
3. **Research and check.** Seven research passes, one per group below, read real sources (papers, survey and expository articles, circle handouts) and cite only pages they opened. Every small number a plan quotes is asserted in a standard-library script, one per group; all seven pass. I reviewed each group's report and spot-checked plans before they went to `main`.

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

By strand: counting 4, networks 3, number 7, symmetry 6, shape 9, chance 4, games 3 (plus 110 and 132), logic 4, analysis 2. By field, the plans add most where the weeks were thinnest: topology and analysis (106, 127, 128, 129, 141, 142), logic and computation (137–140) and groups (115–117). They give first weeks to binomial counts and lattice paths (101), groups (115–117), equilibria (135, 136), continuity and connectedness (129, 142) and computability (138).

## Strongest picks

1. **[One straight cut](week-124-fold-and-cut.md).** A research theorem (any straight-line drawing can be cut out with one cut after folding) that a kindergartner can test with paper and scissors, with a grade 4–5 question about how few folds each shape needs.
2. **[Gems made only of triangles](week-120-eight-deltahedra.md).** Magnetic triangle tiles, a classroom-wide hunt, and a complete answer: exactly eight convex shapes, and the missing 18 is a genuine surprise.
3. **[Hailstone numbers](week-108-hailstone-numbers.md).** An open problem children can run with counters, with Tao's 2019 theorem and computer checks as the honest story of what mathematicians know.
4. **[Tiny machines and the busy beaver](week-138-busy-beaver.md).** Children act as the machine; the record holders for 2, 3 and 4 states are checkable, and BB(5) was settled by an online collaboration in 2024. The age fit for grades 2–3 is the open question.
5. **[Leaning towers off the table](week-141-leaning-towers.md).** Blocks at a table edge make a divergent series physical: four blocks hang a whole block past the edge, and with enough blocks the overhang has no limit.

Close behind: [Proving without telling](week-140-proving-without-telling.md) (cups over a coloured map), [Splitting necklaces](week-128-splitting-necklaces.md) (a sliding-window proof children can follow) and [Peg jumps and Conway's soldiers](week-134-conways-soldiers.md), which answers the scouting set-aside with a K–1 entry.

## Overlaps and weak spots to settle in review

- **107 Mazes:** "a perfect maze is a tree" repeats Week 53 and atlas GA-25 and AD-05; the new parts are the wall-follower theorem and Wilson's fair random mazes.
- **102 Domino diamonds** shares Week 1's flip move and may fit better as a Week 1 return visit.
- **104 Sixteen-card square:** its 3×3 entry is near Week 36; a published "144 solutions" figure conflicts with the computed counts (6912 without diagonals; 1152 with, which is 144 up to the square's symmetries). The plan flags it.
- **117 Commutator puzzles** overlaps the scouting set-aside "sliding tokens"; build one, not both.
- **135 Trust game:** its one-round lesson repeats atlas AP-23; the repeated game and tournament are the new part.
- **110 and 114** lean on Fibonacci numbers, which the [grades 2–3 plan](../../grades-2-3-year-a.md) records as less engaging for most of last year's group.
- **111 Staircase numbers** shares rods with Week 89; **113 Magic squares** must stay a symmetry argument, not arithmetic practice.
- No prior use with K–5 children was found for 117, 120, 125, 128, 136 and 138; several have prior use only with grades 7 and up.
- Not confirmed from a page that was read, and flagged in each plan: the kidney-stone subgroup counts (133), the year of Goldwasser, Micali and Rackoff's paper (140), a direct source for the undecidability of Life (137), and some classic dates cited only through secondary sources (108, 109, 120, 122, 126).

## Next

James picks what, if anything, moves forward. A chosen plan goes through the worksheet workflow's outline, writer, critic and reviser stages, then a home pilot before the circle. Catalog draft records (`catalog/drafts/`) are not yet written for these plans, so they do not appear in the explorer.
