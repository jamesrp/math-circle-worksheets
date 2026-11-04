# Week 149 (draft plan): Racetrack

**Strand:** games (Games and choices), touching analysis and networks. **Deep-math field:** discrete motion, shortest paths in state graphs. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Racetrack is a pencil-and-paper game on squared paper, published by Martin Gardner in his Scientific American column in January 1973 (he learned it from Jürg Nievergelt; its origin is unknown). A car's move is an arrow from one grid point to another. Each turn the car repeats its last arrow and may then nudge the end by one square in any direction, so each coordinate of the velocity changes by at most 1 and there are 9 choices. A car that leaves the track crashes. This is Newton's first law with bounded acceleration made discrete: a car keeps moving unless something changes its velocity, and speed can only be gained or lost a little at a time. The key mathematical move is to change what "position" means. The state of a car is its point and its velocity together; the game is a walk on a finite graph of states, and the fastest race is a shortest path in that graph, found by breadth-first search (trying all 1-move states, then all 2-move states, and so on). Holzer and McKenzie (FUN 2010) showed that deciding whether a single car can reach the finish is NL-complete and that deciding whether a player has a winning strategy in the two-player game is P-complete; so unlike the NP-complete puzzles of draft 146, an optimal race can be computed efficiently. On a straight road the arithmetic is exact. From rest at full throttle a car is at 1, 3, 6, 10, 15 squares after 1 to 5 moves (triangular numbers). To park, landing on a square with a last move of length 1 so the car can stop, takes m moves for distances up to ⌊(m + 1)²/4⌋: 1, 2, 4, 6, 9, 12, 16, 20 squares for m = 1 to 8, because the best speed pattern rises and falls by one (1 + 2 + 3 + 2 + 1 = 9). So the braking must start about halfway, and doubling the distance multiplies the time by about √2, which is the discrete shadow of distance growing with the square of time under constant acceleration. On the U track used here (below), the fastest run from rest takes 13 moves, while a car that only speeds up crashes into the far wall on its sixth move. Proved: the state-graph method, the parking formula and the complexity classes. Checked here: every number above for the stated tracks. Children can discover that braking before a corner wins, that "how fast am I going" is part of where you are, and the 1-2-3-2-1 parking pattern.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Computational Complexity of RaceTrack](https://rd.springer.com/chapter/10.1007/978-3-642-13122-6_26) — Markus Holzer and Pierre McKenzie, Fun with Algorithms (FUN 2010), LNCS 6099 (read November 4, 2026). Reachability is NL-complete (or in L when the car may touch the edge); the single-player game is NL-complete; deciding a winning strategy in Gardner's two-player game is P-complete.
- [Racetrack (game)](https://en.wikipedia.org/wiki/Racetrack_(game)) — Wikipedia, secondary pointer (read November 4, 2026). The nine-choice rule; Gardner's January 1973 column, learned from Jürg Nievergelt; origin unknown, played by the 1960s.
- [Inertia Racetrack](https://www.transum.org/Maths/Game/Vectors/Default.asp?Level=6) — Transum Mathematics (read November 4, 2026). An online two-player version where each vector component changes by at most one per turn, with ten tracks and a solo fewest-moves mode; aimed at secondary vector work.
- Prior use with children: [How to Play Racetrack Game with a Paper and Pencil](https://teachbesideme.com/how-to-play-racetrack-game-with-a-paper-and-pencil/) — Karyn Tripp, Teach Beside Me (read November 4, 2026). The game for homeschooling families: oval tracks on graph paper, velocity changed by one square, crash rules and variations; no age range given. No math-circle handout was found (searched "racetrack game velocity vectors classroom activity").

## A kid-friendly way in

Start on the floor. A strip of tape squares (or floor tiles) is a road; a child is the car and holds a speed card. Each turn the car may add 1, keep or take away 1, then hops that many squares; the garage is a marked square where the car must land with speed 1. Then move to paper: tracks printed on 1 cm squared paper, a dot for the car, and a "ghost arrow" (copy the last arrow lightly, then choose its end or one of the 8 neighbours). Prep: tape one floor strip of 20 squares, print the U track and two oval tracks per pair, coloured pencils; about 15 minutes. Launch (3 minutes): on a projected track, drive three moves together, drawing each ghost arrow and the nine choices around its tip, then show a crash.

## By band

- **K–1:** The floor road. Park in the garage 4, 6 and 9 squares away with as few hops as you can; notice you must slow down before the garage. No reading; speed cards show dots.
- **2–3:** Paper races in pairs on oval tracks, then the solo U track: fewest moves from the start to the finish box. Record each move as an arrow; compare routes on a class chart.
- **4–5:** Explain the parking pattern (why 1 + 2 + 3 + 2 + 1 is best for 9) and find the most squares m moves can cover. Argue that a route is fastest: why can no route reach the finish in fewer moves? Meet the state idea: the same point at two speeds is two different places on the map of the game.

## Checked facts

All in `check_logic_games_2.py`, function `check_week_149()`:
- Nine choices per move.
- Full throttle from rest: 1, 3, 6, 10, 15 squares after 1 to 5 moves.
- Fewest moves to park d squares away (last move of length 1), d = 1 to 20: 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8; m moves reach at most ⌊(m + 1)²/4⌋ squares.
- The U track: grid points 0 ≤ x ≤ 20, 0 ≤ y ≤ 12, with a wall filling x < 15, 4 < y < 8 (a move's straight segment must stay on the track; touching the wall's edge is allowed). From rest at (2, 2) to any point with y ≥ 8 and x ≤ 2, the fastest run is 13 moves (breadth-first search). Full throttle to the right from (2, 2) crashes on move 6 (17 to 23).
- Cited, not computed: the complexity results (Holzer and McKenzie); Gardner's 1973 column (Wikipedia).

## Nearest existing themes

Week 67 (Meeting on shortest roads) finds shortest routes on a fixed map; here the map must be enlarged to include velocity before shortest paths make sense. Week 74 (Doubling elevators) is the closest relative: its states (x, h) add a hidden level to position in the same way. Week 89 and draft 111 (staircase numbers) meet triangular numbers and sums like 1 + 2 + 3 + 2 + 1. Week 47 (Gentle-step landscapes) also has neighbours that differ by at most 1. Week 86 (Pursuit and escape) is a two-player chase game. New: velocity as part of the state, bounded acceleration, and braking as a theorem about square growth.

## App connection

Games and choices region (or Maps and networks), possible family "Ghost-arrow racing": the board shows the car, its ghost arrow and the nine landing dots; the child taps one. Puzzles: "Park in the garage 9 squares away in 5 moves"; "Finish the U track in 13 moves"; "Beat the robot that never brakes". The app can compute the fastest route by breadth-first search and show it after a try.

## Open questions

- Floor version: do K–1 children keep track of their speed card while hopping? A partner holding the card may help.
- Crash rule for children: restart at speed 0 from the last safe point is gentle; skipping a turn is harsher. Choose one and print it.
- Does the 13-move U track feel achievable for 2–3? Rehearse; a wider track may suit them better.
- Whether to state the physics link (distance grows like time squared) to 4–5 or keep it for adults.
