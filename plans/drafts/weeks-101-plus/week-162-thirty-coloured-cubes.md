# Week 162 (draft plan): Thirty coloured cubes

**Strand:** symmetry (Patterns and symmetry). **Deep-math field:** group actions, orbit counting, the rotation group of the cube. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Paint the six faces of a cube with six different colours. There are 6! = 720 ways to place the colours on fixed faces, but turning the cube makes many of them the same cube. The cube has exactly 24 rotations (any of 6 faces can go on top, then any of 4 sides to the front), and no rotation except doing nothing keeps a six-colour cube looking the same, so the 720 paintings fall into groups of exactly 24 and there are 720 / 24 = 30 different cubes. A child-sized count gives the same answer: hold red on top; 5 colours can go on the bottom; the remaining four colours go round the sides in 4! = 24 orders, but turning the cube about its vertical axis makes groups of 4 the same, leaving 6; so 5 × 6 = 30. The mirror image of a six-colour cube is never the same cube, so the 30 come in 15 mirror pairs. The 24 rotations shuffle the cube's four long diagonals in all 4! = 24 possible ways, so the rotation group is a copy of the symmetric group S4. With repeated colours the groups are not all of size 24 and the count needs Burnside's lemma: painting faces red or blue gives 10 different cubes, and three colours each on two faces gives 6. MacMahon (New Mathematical Pastimes, 1921) built puzzles on the set of 30: pick one cube as a model and build a double-size 2 × 2 × 2 copy of it from eight of the other 29, with touching inner faces the same colour. For every model exactly one set of eight cubes works, in exactly two arrangements when the model is held still (checked here by exhaustive search; Conway's 6 × 6 tableau organises the answer). Johnson and Roldán (2024) count solutions when inner faces need not match, and find nine new minimal sets of 12 cubes from which all 30 can be built. Everything is proved; the remaining questions here are counting, not open problems. Children can discover that "same" means "same after turning", find a system that lists all 30, and (grades 4–5) solve one MacMahon puzzle.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Solution Numbers for Eight Blocks to Madness Puzzle](https://arxiv.org/abs/2407.13208) — Inga Johnson and Érika Roldán, arXiv 2407.13208, 2024 (authors from the [HTML version](https://arxiv.org/html/2407.13208v1)). 720 placements, 24 rotations, exactly 30 MacMahon cubes; MacMahon's 1921 New Mathematical Pastimes and the interior-matching puzzle; Conway's 6 × 6 tableau; one set of eight cubes arranged in exactly two ways; up to five targets per set when inner faces need not match; nine new minimal universal sets of 12 (read November 4, 2026).
- [MacMahon's Coloured Cubes](https://mathematische-basteleien.de/macmahon.htm) — Mathematische Basteleien (German recreational-mathematics site; the page read does not name its author). The 30 cubes, the 2 × 2 × 2 copy puzzle worked for one cube with a second symmetric solution, variants, and how to make the cubes at home (read November 4, 2026).
- [The Thirty Color Cubes Problem](https://g4gexchangearchive.omeka.net/items/show/1718) — Margaret Kepner, Gathering for Gardner 15 exchange gift: supplies for making the set with colour stickers and labels (read November 4, 2026).
- Prior use with children: none found for the 30-cube set with K–5 children; I searched for MacMahon cubes and the thirty coloured cubes with "math circle", "classroom" and "children". Nearest: NRICH [Four Colours](https://nrich.maths.org/1087/note?nomenu=1) (ages 5–11), arranging eight multilink cubes so each colour shows once on each face of the big cube (read November 4, 2026).

## A kid-friendly way in

Blank wooden or foam cubes and round stickers in six colours. Each child paints (stickers) one cube with six different colours, any way they like, then meets a partner: are your cubes the same? Turn them to check. The class goal is a museum of all 30 different cubes on a shelf with a sorting card for each ("red on top, ___ on the bottom"); duplicates go in a "twins" box and new children are asked to make a cube the museum is missing. Prep: 40 blank 2–3 cm cubes, 6 sticker colours (about 250 stickers), 30 sorting cards; about 15 minutes. Launch (2–3 minutes): show two stickered cubes that look different from where the room sits, turn one slowly until they match, and say that these count as the same cube; then show a pair that can never be turned to match.

## By band

- **K–1:** cubes with only red and blue stickers: make as many different cubes as the table can (one red face, two red faces, …), check by turning, and line them up; the table finds there are 10. Matching a mystery cube to the shelf is the core skill.
- **2–3:** six-colour cubes for the class museum; find a system that guarantees no missing cube (fix red on top, choose the bottom, then the order round the sides); predict the total and see whether the museum reaches it.
- **4–5:** explain 30 two ways (5 × 6, and 720 ÷ 24 by counting the cube's turns); find each cube's mirror twin in the museum; then MacMahon's puzzle: choose a model cube and find the eight cubes that build its double-size copy with matching inner faces.

## Checked facts

Computed in `check_number_symmetry_2.py`, `check_week_162()`:

- the rotation group generated by two quarter turns has 24 elements and permutes the four long diagonals in all 24 ways;
- 720 six-colour paintings form 30 classes; 4! / 4 = 6 side orders and 5 × 6 = 30; every six-colour cube differs from its mirror image (15 pairs);
- two colours: 64 paintings, 10 cubes (1, 1, 2, 2, 2, 1, 1 with 0 to 6 red faces); three colours on two faces each: 90 paintings, 6 cubes;
- MacMahon's puzzle: for each of the 30 models, an exhaustive search over the eight corner cubes (outer faces matching the model, touching inner faces equal, eight different cubes, model excluded) finds exactly two arrangements, both using the same set of eight.

## Nearest existing themes

Week 37 (mirror twins) counts the 24 labellings of a tetrahedron as two classes of 12 under its 12 rotations, the same orbit-counting move on a smaller group; Week 34 (hidden turns) colours rings so no turn or flip fixes them; Week 33 (prime-length necklaces) counts rings up to turning; atlas AD-24 (two-colour necklaces) tests why dividing by the number of turns fails, which the K–1 two-colour cubes illustrate in three dimensions; Week 1e stacks cubes but is not about colouring. The Week 151 draft (Instant Insanity, written in parallel) also uses cubes with coloured faces, but its mathematics is a graph of opposite faces for a stacking puzzle; the two could share stickered cubes and should be scheduled apart. New: the cube's group of 24, a complete class collection, chirality without labels, and MacMahon's matching puzzle.

## App connection

Patterns and symmetry region, a "colour cube museum" family: a 3D cube the child turns by dragging; puzzles: "is this cube already in the museum?", "make a cube the museum is missing", "build the double-size copy of this cube" with eight draggable small cubes. The 3D turning interface is the main build cost; an existing family with cube turning could carry it if one exists.

## Open questions

- Telling cubes apart by turning is hard for some children; the sorting card ("red on top, which colour below, then read the sides clockwise from ___") may be needed earlier than planned. Untested.
- The MacMahon puzzle needs the full set of 30 on the shelf, so it depends on the museum being complete and correct.
- Confirm MacMahon's 1921 title and date beyond Johnson and Roldán's statement before the guide states them.
