# Week 151 (draft plan): Instant Insanity

**Strand:** networks (Maps and networks). **Deep-math field:** graph theory (2-factors of multigraphs), search and complexity. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Four cubes have their faces coloured with four colours; the task is to stack them so that each of the four long sides of the tower shows all four colours. The trick is to forget positions and record only opposite faces: draw one dot per colour, and for each cube draw three links, one joining the colours of each opposite pair (a loop if both faces match), labelled with the cube's number. In a solved tower the front and back faces of the four cubes use one opposite pair from each cube, and every colour appears once in front and once at the back, so those four links form a subgraph using each cube once in which every colour dot meets exactly two link ends; the left and right sides give a second such subgraph, sharing no link with the first. Conversely, two such disjoint subgraphs can always be turned into a tower, by walking round each subgraph's loops to decide which face goes in front. So the puzzle is solvable exactly when this pair exists, and the search shrinks from 41,472 positions (24 orientations per cube, divided by the tower's 8 turnings and flips) to 81 choices of one pair per cube. The method appeared in 1947 in the Cambridge student magazine Eureka under the pseudonym F. de Carteblanche, for the earlier puzzle sold as the Great Tantalizer; Parker Brothers sold the puzzle as Instant Insanity from 1967. For the commercial colouring recorded on Jaap's Puzzle Page the solution is unique up to turning and flipping the tower, and the computer check here confirms that: exactly one disjoint pair, out of three "every colour twice" choices. With n cubes and n colours the question is NP-complete (Robertson and Munro, 1978), so the graph trick is a huge saving for four cubes, not a fast method for every size. Children can discover that the ladder of goals gets steep (front only is easy, all four sides is rare), that a cube with one colour on four faces makes the puzzle impossible, and, in grades 4–5, why the two-subgraph test works.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Instant Insanity](https://www.jaapsch.net/puzzles/insanity.htm) — Jaap Scherphuis, Jaap's Puzzle Page. Nets of the four commercial cubes, the count 24^4/8 = 41,472, uniqueness of the solution, and the graph method step by step (read November 4, 2026).
- [The Mutando of Insanity](https://ar5iv.labs.arxiv.org/html/1610.09371) — Érika B. Roldán Roa, arXiv 1610.09371, 2016. History: the 1947 Eureka paper by Cambridge undergraduates writing as F. De Carteblanche, the 1967 Parker Brothers puzzle, T. A. Brown's 1968 note (read November 4, 2026).
- [Variations on Instant Insanity](https://erikdemaine.org/papers/InstantInsanity_Ianfest2013/paper.pdf) — Erik D. Demaine, Martin L. Demaine, Sarah Eisenstat, Thomas D. Morgan, Ryuhei Uehara, about 2013. Robertson and Munro (1978): n cubes with n colours is NP-complete; complexity of prism variants (read November 4, 2026).
- Prior use with children: [Coloured Cubes](https://mathematicscentre.com/taskcentre/185colcu.htm) — Mathematics Centre task 185, for Years 2 to 10, "hard to solve but easy to start", fine to leave and return; credits Carteblanche (1947) and suggests building the cubes from nets (read November 4, 2026). Also [Instant Insanity](https://gems.education.purdue.edu/wp-content/uploads/2019/02/Instantinsanity.pdf) — Purdue GEMS club challenge for grades 3–8, with card-stock cubes from enlarged handouts (read November 4, 2026).

## A kid-friendly way in

Each pair folds a set of four paper cubes from printed nets (card stock, colours printed or coloured in), or uses wooden cubes with dot stickers. A large "tower mat" with four side windows helps children check sides. Prep: print and cut nets for six sets, or sticker 24 wooden cubes; about 25 minutes if printed, more if coloured by hand (have children colour their own nets from a key as a first activity if time allows). Launch (2–3 minutes): with a non-task set of two cubes, show a legal stack, turn one cube, and walk once round the tower naming the colours on each side.

## By band

- **K–1:** the ladder of goals: make the front show four different colours, then the front and the back. Then a three-cube, three-colour warm-up set where every side can show all three colours.
- **2–3:** the full puzzle by trial, recording which goals are reached; then a "broken" set where one cube has one colour on four faces, and explain why no stacking can work.
- **4–5:** draw the opposite-face graph for each cube on one four-dot picture, find the two "every colour twice" subgraphs, and build the tower from them; then explain why the two subgraphs must exist in any solution.

## Checked facts

Computed in `check_networks_counting_2.py`, `check_week_151()`:

- 24 rotations of a cube; 24^4 = 331,776 placements, 41,472 up to turning and flipping;
- Jaap's colouring (red on 7 faces, green and yellow 6, blue 5): placements with front all different 33,280; front and back 1,536; three sides 172; all four sides 8, which is one tower up to its 8 turnings and flips;
- graph method on that colouring: 3 "every colour twice" choices, exactly 1 disjoint pair; 81 choices to search;
- warm-up: cubes with opposite pairs (red–yellow, yellow–blue, blue–red), (red–red, yellow–blue, red–blue), (yellow–yellow, red–blue, red–yellow): 24 towers, 3 up to turning and flipping;
- a set where one cube shows red on four faces has no solution.

Cited, not computed: the history and NP-completeness for n cubes.

## Nearest existing themes

Week 37 (mirror twins) also turns physical solids and counts orientations, but its question is chirality of labelled tetrahedra; there is no graph and no stacking goal, so overlap is in handling skills only. Week 5 (tower cities) and draft Week 104 ask for every symbol once in each row or column, a Latin condition close to "every colour once on each side". Week 62 colours conflict networks. New here: replacing a spatial search by a graph built from opposite pairs, and 2-factors (every dot meeting two link ends) as the hidden structure.

## App connection

Maps and networks, or a crossover with Shapes and spaces: a tower of four cubes the child turns by tapping arrows, with each side's colours shown as a strip below; puzzles climb the ladder (one side, two sides, all four). A second mode shows the colour graph and asks the child to pick two disjoint "every colour twice" sets of links, then the app builds the tower from them.

## Open questions

- Whether paper cubes are sturdy enough for repeated turning; wooden cubes with stickers may be worth the cost.
- Whether K–1 can track four sides at once; the tower mat or a mirror behind the tower might help.
- Whether the graph step lands in grades 4–5 without a long explanation, or needs its own return visit.
