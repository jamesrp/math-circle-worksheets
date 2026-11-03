# Week 107 (draft plan): Mazes, walls and random trees

**Strand:** networks (Maps and networks), with logic (Codes and logic). **Deep-math field:** graph theory (trees, graph search), probability (random spanning trees). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Model a grid maze as rooms (dots) and open doorways (links). A perfect maze, with exactly one route between any two rooms, is a spanning tree of the grid: an m-by-n maze has mn − 1 doorways, and of the (m − 1)n + m(n − 1) inner walls exactly (m − 1)(n − 1) stay standing (9 of 24 on 4-by-4). Three facts about solving. (1) Hand on the wall: if every wall is connected to the outer wall (the maze has no free-standing island of wall), keeping one hand on the wall from the entrance traces round the single wall and must reach every doorway on that wall, including the exit, though not by the shortest route. In a perfect maze the walker passes every doorway exactly twice and visits every room before returning (checked here on random 4-by-4 mazes). If the wall has islands, the rule can circle forever: in an open 3-by-3 block, a right-hand walker starting in the centre loops round the four rooms by one post and never reaches the far corner. (2) Trémaux's method (19th century, published by Lucas in 1891) marks each passage as it is used, turns back on reaching an already-visited junction by a new passage, and never uses a passage a third time; it solves every finite maze and is the ancestor of depth-first search. (3) Making mazes: the number of perfect mazes is the number of spanning trees (4, 15, 192, 2415, 100352 for 2-by-2, 2-by-3, 3-by-3, 3-by-4, 4-by-4, by Kirchhoff's matrix-tree theorem). Wilson's algorithm (David Wilson, mid-1990s; analysed in Propp and Wilson's 1998 journal paper) produces every perfect maze with equal chance: from a room not yet in the maze, take a random walk, erase any loop it makes, and add the loop-free path when it hits the maze; the result is uniform whatever order the starting rooms are taken in. A natural-seeming method, knocking down walls in a random order and skipping any that would make a loop, is not fair: on 2-by-3, six mazes come out with chance 5/84 and nine with 1/14. A recent result (Gladkov and Pak, 2024) shows that a randomised exploration of a maze with one entrance and two exits leaves by each exit with probability 1/2. Children can discover the doorway count, when hand-on-wall works and when it fails, Trémaux marking, and Wilson's loop erasure as a physical procedure.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Maths aMazes](https://plus.maths.org/maths-amazes) — Chris Budd and Chris Sangwin, Plus Magazine issue 14, March 2001. Mazes as networks, hand-on-hedge working only sometimes, Trémaux's marking method (from Rouse Ball) with each path used at most twice, Hampton Court (read November 3, 2026).
- [Exploring Mazes at Random](https://www.math.ucla.edu/~pak/papers/maze21.pdf) — Nikita Gladkov and Igor Pak, preprint dated July 25, 2024. Right- and left-hand-on-wall rules, Trémaux credited via Lucas 1891, the equal-exit theorem for randomised depth-first search, tree mazes (read November 3, 2026).
- [How to Get a Perfectly Random Sample from a Generic Markov Chain and Generate a Random Spanning Tree of a Directed Graph](https://www2.stat.duke.edu/~scs/Projects/Trees/Theory/ProppWilson1998.pdf) — James G. Propp and David B. Wilson, Journal of Algorithms 27 (1998), 170–217. Cycle popping via loop-erased random walk returns a uniformly random spanning tree (Theorem 13), independent of popping order (read November 3, 2026).
- [Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm) — Wikipedia, secondary pointer. Mazes as random spanning trees; Wilson's algorithm as the unbiased method and Aldous–Broder as a slower uniform one (read November 3, 2026).
- Prior use with children: [A-maze-ing Math](https://mathmidway.org/Training/amazeing.php) — Math Midway, Museum of Mathematics. A walk-through exhibit maze with a turning rule, linked to graph theory; young children play, older ones study the structure (read November 3, 2026). No K–5 circle handout on wall-following or random mazes was found on NRICH or JRMF.

## A kid-friendly way in

A floor or tabletop maze: a 4-by-4 grid of rooms (paper squares or a printed board with 5 cm rooms) and wall strips or blocks along the grid lines. Children build a maze by placing walls, then a partner solves it walking a token with a "hand" (a sticky arrow pointing at the wall on the right). For the random-maze station: arrow cards, one per room, and a four-sided die or spinner (N, E, S, W; re-roll into the outer wall). Prep: print boards, cut wall strips (24 inner positions), make arrow cards; about 25 minutes. Launch (2–3 minutes): walk a token through a small printed maze on the board with a hand on the right wall, narrating "right if I can, else straight, else left, else back".

## By band

- **K–1:** solve printed and floor mazes by hand on the wall; build a maze and let a friend try. Find a maze where the hand rule goes round and round (a wall island).
- **2–3:** build perfect mazes on 3-by-3 or 4-by-4 (every room reachable, one route only) and count the doorways (always one fewer than rooms) and the standing inner walls; solve an island maze with chalk or counter marks by Trémaux's rule.
- **4–5:** Wilson's algorithm with the die and arrow cards on a 3-by-3 board: start with one room in the maze; from another room roll and step, turning that room's arrow to point the way you left (later visits overwrite it, which erases loops); when you hit the maze, follow the arrows from the start and open those doorways. Compare with knocking down walls at random: on 2-by-3 there are 15 perfect mazes, and the class can tally which come up.

## Checked facts

Computed in `check_counting_networks.py`, `check_week_107()`:

- (m − 1)(n − 1) standing inner walls, 24 inner walls on 4-by-4; spanning tree counts 4, 15, 192, 2415, 100352;
- random wall knocking on 2-by-3 over all 5040 orders: six mazes 300 times (5/84), nine 360 times (1/14);
- Wilson's algorithm on 2-by-3: all 15 mazes within one percentage point of 1/15 in 30,000 seeded trials;
- right-hand walker in 20 random 4-by-4 perfect mazes: back at the entrance after 30 steps, every doorway twice, every room visited; the open 3-by-3 loop that never reaches the corner;
- Trémaux on an open 5-by-5 grid from 50 seeds: always reaches the goal, no passage used more than twice.

Cited, not computed: uniformity of Wilson's algorithm in general, Kirchhoff's theorem, Gladkov–Pak.

## Nearest existing themes

AD-05 lists the spanning trees of a small network (and Kirchhoff's determinant), GA-25 closes roads until no loop survives and proves the count E − V + 1, which is exactly this week's (m − 1)(n − 1) standing walls, and Week 53 finds the cheapest spanning tree; so "a perfect maze is a tree" duplicates existing material and should be a quick bridge, not the centre. Week 91's rotor-router cards are physically similar to Wilson's arrow cards; Week 10 counts odd islands (Budd and Sangwin use Euler's theorem on mazes). New here: solving rules and when they fail (wall islands), Trémaux's search, and fair random generation by loop erasure against an unfair intuitive method.

## App connection

Maps and networks: a "maze maker" family. The child places walls on a grid; the app checks for one route between every pair of rooms; puzzles ask "build a maze where the right-hand rule fails", "remove the fewest walls so every room is reachable", or "run Wilson's walk: tap where the die sends you". A solving mode replays the hand-on-wall walker so children can predict its path.

## Open questions

- Whether a die-driven Wilson walk on 3-by-3 finishes in reasonable time at a table; walks can wander, so a 2-by-3 board may be the realistic size.
- Whether K–1 children can keep a consistent hand side when turning a token on paper; a floor maze with real walking may work better.
- Whether to tie this to Week 91 (rotors) as a return visit rather than a new theme.
