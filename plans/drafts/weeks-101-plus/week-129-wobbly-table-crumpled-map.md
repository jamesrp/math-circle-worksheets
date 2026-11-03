# Week 129 (draft plan): The wobbly table and the crumpled map

**Strand:** shape, with analysis (app region "Shapes and spaces"). **Deep-math field:** topology, intermediate value theorem, fixed points. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Wobbly table theorem: a square table with four equal legs, standing on continuous ground that is not too steep, can be turned on the spot, by at most a quarter turn, to a position where all four feet touch the ground. The idea: rotate the table and keep two diagonally opposite feet on the ground; measure how far the other pair is above (positive) or below (negative) the ground. After a quarter turn the two diagonals have swapped roles, so the sign has changed, and since nothing jumps, the intermediate value theorem gives an angle in between where it is zero. In the simplest model, with the feet at the corners of a square of fixed horizontal position, the four feet are level-compatible exactly when h1 + h3 = h2 + h4, and g(θ) = h1 + h3 − h2 − h4 satisfies g(θ + 90°) = −g(θ). Making this rigorous for real ground is harder: André Martin (arXiv 2005–06, later in a journal) proved it for slopes up to 15°; Baritompa, Löwen, Polster and Ross ("Mathematical table turning revisited", 2005) proved it for ground with slope at most about 35° (Lipschitz constant 1/√2) and legs long enough, and showed that a rectangular table may need up to a half turn. Limits: the legs must be equal, the ground continuous (no steps), and the result says nothing about the table top being level. A three-legged stool never wobbles at all, because three points always lie in one plane. The same no-jump idea gives the hiking monk puzzle (a monk walking up one day and down the next is at the same place at the same time on both days) and, in two dimensions, Brouwer's fixed point theorem (1912): every continuous map of a disk to itself fixes some point. So a smaller or crumpled copy of a map laid entirely on top of the same map has a point lying directly above the place it shows. All of these are existence results that do not say where the point is. What children can discover: turning a four-legged stool always seems to find a steady spot within a quarter turn; a three-legged stool is always steady; a half-size map laid on a map has exactly one "you are here" point.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Mathematical table turning revisited](https://arxiv.org/pdf/math/0511490) — Bill Baritompa, Rainer Löwen, Burkard Polster, Marty Ross, arXiv math/0511490 (2005). The intermediate value argument; Lipschitz bound 1/√2 (about 35.26°) and leg-length condition; square tables need about a quarter turn, rectangles up to a half turn (read November 3, 2026).
- [On the stability of four legged tables](https://arxiv.org/abs/math-ph/0510065) — André Martin, arXiv math-ph/0510065 (2005–06), DOI 10.1016/j.physleta.2006.08.053. Square table on ground with slope at most 15° balances after a rotation of less than 90° (read November 3, 2026).
- [Brouwer's Fixed-Point Theorem](https://thatsmaths.com/2015/04/30/brouwers-fixed-point-theorem/) — ThatsMaths blog, April 30, 2015. Brouwer 1912; disk statement; the one-dimensional interval case; a map laid on the ground has a "you are here" point (read November 3, 2026).
- [Brouwer Fixed Point Theorem](https://math.hmc.edu/funfacts/?p=389) — Harvey Mudd Math Fun Facts (Francis Su et al.). Crumpled sheet over an identical sheet has a point above its original; the stirred-coffee version (read November 3, 2026).
- Prior use with children: [To Be or Not to Be, too](https://www.qedcat.com/mathsnacks/mathsnacks07_existence2.pdf) — Burkard Polster and Marty Ross, MathSnacks column, Vinculum 42(3), September 2005: the monk puzzle and the egg-cutting (ham sandwich style) existence argument. Also [The wobbly table problem](https://spark.iop.org/wobbly-table-problem), Institute of Physics Spark story for ages 11–16 (no activity given) (both read November 3, 2026). No elementary circle handout on table turning was found (searched "wobbly table rotate fix" and "monk climbing mountain math circle").

## A kid-friendly way in

Materials: one or two small square four-legged stools or step stools with equal legs (or a square of plywood with four equal dowel feet), one three-legged stool, a tray of damp sand or a lumpy doormat for uneven ground, a strip of tape marking quarter turns on the stool, letter-size copies of a school map plus half-size copies, and pins. Prep: about 20 minutes, mostly making the half-size copies and checking the stool wobbles somewhere. Launch (3 minutes): put the four-legged stool on the bumpy tray so it rocks, ask children to predict whether turning it can fix the rock, and turn it slowly while everyone watches the rocking pair of feet.

Suggested hour: 0–5 launch; 5–25 stool stations (four-legged and three-legged) with turn records; 25–35 monk puzzle with figures; 35–55 map on map; 55–60 share where the steady spots were and why a quarter turn is enough.

## By band

- **K–1:** Turn the stool until it stops rocking; mark the spot with a sticker. Try the three-legged stool: can anyone make it rock? Lay a small map copy on a big map and hunt for a spot that sits over itself.
- **2–3:** Record, for each eighth of a turn, which diagonal pair rocks. Does the rocking pair switch by the quarter-turn mark? Monk puzzle with two toy figures on a drawn mountain path, one walking up and one down at the same time.
- **4–5:** Explain why a quarter turn swaps the roles of the two diagonals and why that forces a steady spot in between. Map on map: find the fixed point of a half-size, quarter-turned copy by repeatedly asking "where is this spot shown on the copy?" and watching the guesses close in. Discuss: does the argument work on stairs (a jump)?

## Checked facts

- `check_week_129()`: for 200 random smooth grounds, g(θ) = h1 + h3 − h2 − h4 satisfies g(θ + 90°) = −g(θ) and bisection finds a zero in [0°, 90°]; four corners of a tilted plane satisfy h1 + h3 = h2 + h4. This checks the simplified model only; the real-ground theorems are cited.
- `check_week_129()`: on a 28 × 21.6 cm map, a half-size copy turned a quarter turn counterclockwise, placed so the map's lower-left corner is shown at (16, 4) cm, lies inside the map (x from 5.2 to 16, y from 4 to 18) and has exactly one fixed point, at (11.2, 9.6) cm; repeated look-ups converge to it.
- `check_week_129()`: random up and down schedules of the monk always cross (checked on 200 random monotone schedules).
- Brouwer's theorem and the slope conditions are cited.

## Nearest existing themes

Week 16 (Sperner, the discrete cousin of Brouwer), atlas GA-02 (one-dimensional Borsuk–Ulam: an opposite pair at equal height on a loop, the same diagonal-swap structure as the table) and GA-36 (fixed points of a machine on [0, 1], and iteration that may not find them). New here: a physical object (the stool) whose behaviour is the theorem, and the two-dimensional fixed point of a map on a map. Overlap with GA-02 is real: the table's g(θ + 90°) = −g(θ) is the same sign-swap move, so this week works best as the hands-on companion to GA-02 rather than a separate theme.

## App connection

"Shapes and spaces". A rotating square table on a height-coloured landscape; the child turns it and sees two feet glow when they touch, and a dial shows which diagonal is lifted. Puzzles: "find a steady angle within this quarter turn" and "design ground where the table must turn more than 45°". A map-on-map board where dragging a half-size copy updates the "you are here" point. Could extend the GA-02 board if one is built.

## Open questions

- Physical fit: does a real stool on a sand tray behave like the model, or does sand give way? A home rehearsal with two stools is needed.
- Many stools have unequal legs from wear; the theorem needs equal legs, so check the stool on a flat floor first.
- Is the half-size map fixed-point search too fiddly with pins for 2–3?
- Decide whether to present the crumpled (not just scaled) map, where the fixed point need not be unique.
