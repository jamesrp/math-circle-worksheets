# Week 125 (draft plan): One tile that never repeats

**Strand:** symmetry, with shape (app region "Patterns and symmetry"). **Deep-math field:** tiling theory, aperiodic order. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A tiling is periodic if some slide (translation) carries the whole tiling onto itself. Squares, equilateral triangles and regular hexagons tile periodically, and so do many other single shapes. A set of tiles is aperiodic if it tiles the plane but every tiling it admits is non-periodic. Berger (1966) built the first aperiodic set (20,426 Wang tiles), and Penrose's two-tile sets of the 1970s brought it down to two shapes with matching rules. Whether one shape could be aperiodic (an "einstein") stayed open until Smith, Myers, Kaplan and Goodman-Strauss (arXiv 2023, revised 2024 with a journal DOI) proved that the "hat", a polygon made of eight kites of the hexagon-kite grid, tiles the plane and admits only non-periodic tilings. Two limits matter for a facilitator. First, every hat tiling uses both the hat and its mirror image; reflected hats are sparse (in the Bridges group build, 49 of 392 tiles). Second, the same team's follow-up paper constructed the "Spectre", a curved-edge tile that is aperiodic using only rotated copies, with no reflections at all. Both proofs are hierarchical (tiles group into larger "metatiles" that substitute like bigger copies) and computer-assisted in part; nothing about aperiodicity can be seen from a finite patch, because every finite patch of a hat tiling can be extended in some way, and no finite check shows the absence of a period. A related open problem is Heesch's: if a shape does not tile, how many complete rings (coronas) of copies can surround it? The record known is 6 (Bašić), and which numbers are possible is open. What children can discover: the hat does fit together with copies of itself, it needs some flipped copies, and a slide that matches a square or hexagon floor never matches a hat floor they have built (an experiment on a patch, not a proof).

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [An aperiodic monotile](https://arxiv.org/abs/2303.10798) — David Smith, Joseph Samuel Myers, Craig S. Kaplan, Chaim Goodman-Strauss, arXiv 2303.10798 (2023, v3 2024; DOI 10.5070/C64163843). The hat is an eight-kite polykite; metatiles and substitution show it tiles; proofs that it admits only non-periodic tilings; reflected tiles are sparse and evenly spread; Berger's 20,426 Wang tiles; Heesch record 6 (read November 3, 2026).
- [A chiral aperiodic monotile](https://arxiv.org/abs/2305.17743) — same authors, arXiv 2305.17743 (2023, v2 2024). The equilateral member of the hat family tiles only non-periodically when reflections are forbidden; Spectres are strictly chiral aperiodic monotiles (read November 3, 2026).
- [A Group Activity to Make a Hat Tiling with Paper](https://archive.bridgesmathart.org/2024/bridges2024-393.pdf) — David Richeson, Chaim Goodman-Strauss, Linda Green, David Hall, Bridges 2024. A step-by-step group build for people with no mathematical training: 392 paper hats (343 one way, 49 reflected in a second colour), patches of eight with one reflected tile, taped arrows to align patches (read November 3, 2026).
- [Heesch Numbers of Unmarked Polyforms](https://isohedral.ca/?p=2377) — Craig S. Kaplan, blog post, May 23, 2021. Definition of Heesch number by coronas; Bašić's shape with Heesch number 6 (read November 3, 2026).
- Prior use with children: [MoMath Family Fridays: Build a Hat Tiling](https://flatironnomad.nyc/event/momath-family-fridays-build-a-hat-tiling-34326) — event listing for a family group build of a giant hat floor led by Chaim Goodman-Strauss at the National Museum of Mathematics; it describes a family audience of all ages but no child-specific tasks (read November 3, 2026). No elementary circle handout or NRICH task on the hat was found (searched "hat monotile activity for kids classroom tiling").

## A kid-friendly way in

Materials: card-stock hats printed in two colours (one colour for the reflected copies, as in the Bridges build), about 40 per table, plus a bag of square and hexagon tiles (pattern blocks), and one tracing-paper sheet per table. Prep: print and cut, or use a paper cutter; about 25 minutes with a guillotine for 160 hats. Launch (3 minutes): show a hexagon floor, lay a tracing of it on top, and slide the tracing until every outline matches again; then hold up one hat, show that it can be flipped over, and ask the room whether hats can make a floor with no gaps.

Suggested hour: 0–5 launch; 5–25 free building with hats and with squares or hexagons; 25–40 band tasks (one-colour challenge, slide test, kite grid, patch of eight); 40–55 join table patches into one floor on the carpet and hunt for a matching slide; 55–60 share what the flipped hats were doing.

## By band

- **K–1:** Build a hat floor on a table with no gaps or overlaps. Children notice and talk about the "flipped" hats (the other colour). Contrast: build a square floor and a hexagon floor and slide the tracing.
- **2–3:** Can you make a floor using only one colour (no flipped hats)? How big can you get before you are stuck? Then a slide test: trace your square floor and your hat floor and look for a slide that matches. Hats can also be drawn on a printed hexagon-kite grid (each hexagon cut into six kites): find which eight kites make a hat.
- **4–5:** Patch-of-eight build from the Bridges paper (seven hats around one reflected hat), then glue patches into a larger patch and compare it to the small one. Optional Heesch question: give a shape that does not tile (to be chosen; see open questions) and ask how many full rings of copies can surround it.

## Checked facts

- `check_week_125()`: the hat outline used for printing (13 vertices on the triangular lattice) has area exactly 8 kite areas, contains exactly 8 whole kites of the hexagon-kite grid, and has 13 straight sides (one of length 2, the rest 1 or √3). Kite angles 60, 90, 120, 90.
- `check_week_125()`: the Bridges build counts 343 + 49 = 392 = 49 × 8, so one tile in eight is reflected in that patch.
- Aperiodicity of the hat and the Spectre, and the Heesch record 6, are cited (Smith et al.; Kaplan), not computed.

## Nearest existing themes

Week 1 (Tiling lab: rhombus tilings and counting obstructions) and Week 76 (Substitution strips: the non-periodic Thue–Morse word in one dimension). The drafted Week 115 (wallpaper patterns) studies periodic symmetry. New here: a two-dimensional tile whose only tilings lack every slide symmetry, and the role of mirror images. The hierarchy idea links back to Week 76's substitution, so a facilitator can say "the same trick, now with shapes". No catalog week or atlas family covers aperiodic tilings.

## App connection

"Patterns and symmetry". A board where a child drags hats (with a flip button) onto a kite grid to extend a given patch; puzzles: "fill the outlined region with hats, using exactly one flipped hat" or "this patch has a hole; which hat orientation fits?" A slide-match tool (drag a ghost copy of the floor) gives a periodic-or-not experiment. No existing family carries free polygon placement; this would need a new tile-placement family.

## Open questions

- Material fit: are card-stock hats stiff enough, and do children of 5–6 manage the 12 orientations (six turns, two sides)? A home trial with 40 tiles would settle it.
- Do 2–3 children get stuck too early with random placement? The Bridges patch-of-eight method may be needed as a scaffold even for younger bands.
- Choose a concrete non-tiling shape with Heesch number 1 or 2 that children can surround with paper copies; not yet chosen or checked.
- Confirm print scale so a 40-tile patch fits a classroom table.
