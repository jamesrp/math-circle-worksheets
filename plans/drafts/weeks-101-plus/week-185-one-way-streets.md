# Week 185 (draft plan): Making every street one-way

**Strand:** networks (Maps and networks). **Deep-math field:** graph theory (strong orientations, 2-edge-connectivity). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Robbins' theorem (Herbert Robbins, "A theorem on graphs, with an application to a problem of traffic control", *American Mathematical Monthly*, 1939): the roads of a connected town can all be made one-way so that every place can still be reached from every other place exactly when no single road is a lifeline, that is, no road whose closure would cut the town into two pieces (in graph language, the graph is connected and has no bridge). One direction is immediate: a lifeline road can carry traffic only one way, so the side it points away from can never be reached back. The other direction is the theorem. Robbins' proof builds the town as a loop with "ears" added one at a time (a path that leaves the part already built and comes back to it); turn the first loop into a one-way circuit and each ear into a one-way path, and everything stays mutually reachable. A quick test children can use: a one-way town works exactly when, starting from one chosen place, you can reach every place and every place can reach you. Proved for all finite towns; good orientations can be found in linear time by depth-first search; it extends to towns where some streets are already one-way (Boesch and Tindell 1980) and to streets that must keep one direction along their whole length (Aamand, Hjuler, Holm and Rotenberg 2017). Checked here: on every town with 3, 4 or 5 places, a good one-way plan exists exactly when there is no lifeline; a ring of roads has exactly 2 good plans; a town of 3-by-3 crossings (12 roads) has 78 good plans among 4096; the Manhattan rule (neighbouring streets alternate) works on 4-by-4 crossings but never on 3-by-3, where a corner always becomes a dead end or a place nobody can enter. Children can discover lifeline roads, find good plans, and see why a lifeline ruins every plan.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Robbins Theorem](https://mathworld.wolfram.com/RobbinsTheorem.html) — Wolfram MathWorld. Statement (a strongly connected orientation exists iff the graph is connected with no bridges) and the 1939 *Monthly* reference, 46, 281–283 (read November 4, 2026).
- [One-Way Trail Orientations](https://arxiv.org/pdf/1708.07389v1.pdf) — Anders Aamand, Niklas Hjuler, Jacob Holm and Eva Rotenberg, arXiv 1708.07389, 2017. The mayor's one-way-streets motivation, Robbins' theorem as 2-edge-connectivity, and its extension when each street is a trail of several road pieces that must all point the same way (read November 4, 2026).
- [Robbins' theorem](https://en.wikipedia.org/wiki/Robbins%27_theorem) — Wikipedia, as a secondary pointer only: the ear-decomposition proof, the linear-time depth-first algorithm, and Boesch and Tindell's 1980 mixed-graph version (read November 4, 2026).
- Prior use with children: none found for one-way orientations (searched math circle, NRICH and JRMF pages for one-way streets and Robbins). The nearest is the [CMI Math Circle junior session of August 16, 2026](https://www.cmi.ac.in/~mathcircle/synopsis/aug16_junior.pdf), which teaches a bridge as a line whose removal splits the drawing, inside Fleury's algorithm ("don't burn your bridges") (read November 4, 2026).

## A kid-friendly way in

A floor or table town. Printed town maps (about A3) with places drawn as houses and roads as wide strips, a pile of paper arrow cards that fit on a road, and one toy car. Children put an arrow on every road, then test: drive the car from the school to every house along arrows, and from every house back to the school. A red "road closed" card tests for lifelines. Prep: print five maps (a ring, two rings joined by one road, the same joined by two roads, a 3-by-3 crossing grid, a town with a dead-end lane) and cut arrow cards; about 25 minutes. Launch (2–3 minutes): a four-house ring on the board; make it one-way all the way round and drive the car; then flip one arrow and show a house that can be left but never re-entered.

## By band

- **K–1:** ring towns and a town with a dead-end lane. Make every road one-way so the car can visit every house and come home; find the road that spoils every try (the lane), and the "road closed" card that cuts the town in two.
- **2–3:** the 3-by-3 crossing town: find a good plan, then try the Manhattan rule (neighbouring streets opposite) and see it fail at a corner. Which maps can be fixed, and which never? Mark every lifeline road on each map.
- **4–5:** explain why a lifeline always ruins every plan; build a good plan for a lifeline-free town loop by loop (a one-way ring, then each added path one-way); find why alternating streets need an even number of streets each way.

## Checked facts

Computed in `check_networks_3.py`, `check_week_185()`:

- on every graph with 3, 4 and 5 places and at least one road: a good orientation exists exactly when the graph is connected with no lifeline road;
- a ring of k roads (k = 3 to 8) has exactly 2 good orientations;
- the 3-by-3 crossing town: 12 roads, 78 good orientations out of 4096;
- alternating rows and columns on r-by-c crossings (r, c from 2 to 5) work exactly when r and c are both even, and then for 2 of the 4 phase choices;
- in the 3-by-3 town, if every row runs east no choice of column directions works;
- two triangles joined by one road: 0 good plans; joined by two roads: 18 of 256.

Cited, not computed: Robbins' theorem for all towns, the linear-time algorithm, Boesch–Tindell and the trail version.

## Nearest existing themes

Week 10's return visit "One-way streets" is about directed Euler walks (each island balanced in and out), a different theorem on the same kind of map; Week 10 itself is undirected Euler walks. Week 13 (Route packing) uses one-way maps and cuts; Week 68 counts closures that split infinite maps; the scouting draft "Who beat whom" orients a complete network (tournaments). Draft 152 needs strongly connected networks. Warning: Week 10 calls every road a "bridge", while Robbins' theorem uses "bridge" for a cut road, so this plan says "lifeline road". New: choosing directions to keep a town connected, and the cut-road certificate.

## App connection

Maps and networks: a "one-way town" family. The child taps each road to cycle its arrow; a "test drive" button floods reachability from the town hall forward and backward and highlights any house that cannot get out or cannot be reached. Puzzles: make a given town work; find the one road that makes a town impossible; fix the Manhattan grid with as few reversed streets as possible. Could share the road-map engine with Week 10's family.

## Open questions

- Whether the two-way test (out from the school and back) is too much to track with one car at K–1; two cars (one leaving, one returning) may help.
- The 3-by-3 grid has 12 roads; check that 2–3 can find a good plan without an adult's ear hint.
- Terminology with Week 10 must be settled before student pages: lifeline road, only road or cut road.
