# Week 166 (draft plan): You can't comb a hairy ball

**Strand:** shape (Shapes and spaces). **Deep-math field:** topology of surfaces, vector fields, Poincaré–Hopf. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The hairy ball theorem: every continuous field of arrows tangent to a sphere has at least one point where the arrow is zero. Poincaré proved it for the ordinary sphere (1885) and Brouwer extended it to all even-dimensional spheres (1912). So a hairy ball cannot be combed flat without a tuft, a parting or a crown, and (idealising wind as a flow along the surface) somewhere on Earth there is always a calm spot. Shapes that bend into a sphere (a cube, a stuffed animal) are covered too; a torus (a ring doughnut) is not: arrows running round the ring never vanish. The sharp version counts the calm spots with signs. Walk once around a small circle about an isolated calm spot and count how many times the arrow turns: this is the index. A spring (arrows out), a drain (arrows in) and a whirl each have index +1, a saddle (in from two sides, out to two) has −1, a "dipole" (the pattern of a steady breeze seen from the far side) has +2. The Poincaré–Hopf theorem says that for any field with finitely many calm spots, the indices add up to the Euler characteristic V − E + F of the surface: 2 for a sphere, 0 for a torus. So a ball can have one spring and one drain (north-to-south flow), or two springs, two drains and two saddles, or a single calm spot of index 2, but never none; on a torus the total is 0 and none is possible. A neat bridge to Euler's formula: put a spring at every corner of a cube, a saddle at every edge midpoint and a drain at every face centre; the indices add to 8 − 12 + 6 = 2. Limits: the theorem needs continuity (no jumps) and arrows tangent to the surface; it says a calm spot exists, not where. One dimension down, arrows round a circle can avoid zero, while arrows on a segment pointing out at both ends must vanish somewhere (the intermediate value theorem). Proved: both theorems. Checked here: the indices of the six standard calm spots, the dipole, and the cube total. What children can discover: you can comb the ring but not the ball; the kinds of calm spot; "spring plus drain" and other combinations that are always possible on a ball; in grades 4–5, that the total is always 2.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Hairy balls, cyclones and computer graphics](https://chalkdustmagazine.com/blog/hairy-balls-cyclones-computer-graphics/), Rudolf Kohulák, Chalkdust magazine blog, September 2, 2016 (read November 4, 2026). Statement, sources and sinks +1, saddles −1, the index sum equals the Euler characteristic, combinations totalling 2, the calm spot as the eye of a cyclone.
- [Hairy Ball Theorem](https://math.hmc.edu/funfacts/?p=438), Francis Su and others, Math Fun Facts, Harvey Mudd College (read November 4, 2026). Statement; the torus has Euler number 0 and so carries a field with no problem points; indices add to the Euler characteristic; presentation suggestions for a classroom.
- [Hairy ball theorem](https://en.wikipedia.org/wiki/Hairy_ball_theorem), Wikipedia, as a secondary pointer (read November 4, 2026). Poincaré 1885, Brouwer 1912, the Poincaré–Hopf connection, combing a hairy doughnut, the cyclone corollary and its meteorological caveat.
- [Math's 'hairy ball theorem' has surprising implications](https://www.scientificamerican.com/article/maths-hairy-ball-theorem-has-surprising-implications/), Scientific American (no byline shown on the page read) (read November 4, 2026). Hairy cubes and stuffed animals count as spheres, a doughnut can be combed, a spinning ball has a still point, tokamaks are doughnut-shaped for this reason.
- Prior use with children: none found. Searched "hairy ball theorem activity kids math circle comb tennis ball wind map calm point" and NRICH; the Harvey Mudd page is aimed at college classes.

## A kid-friendly way in

Inflatable beach balls and inflatable swim rings (a few dollars each), sheets of small arrow stickers (or dot stickers and markers), fluffy pompoms or a scrap of faux fur, a fine comb, and printed cube nets with a dot at each corner, edge midpoint and face centre. Prep about 20 minutes: inflate, cut sticker sheets, print nets. Launch (2–3 minutes): comb a pompom or fur ball in front of everyone and ask whether anyone could comb it with no tuft or parting; then show the rule for the arrow game: cover the ball with arrows so that neighbouring arrows point almost the same way, and look for a "calm spot" where the arrows spread out, come together, swirl or split.

Suggested hour: 0–5 combing launch; 5–20 swim ring then beach ball; 20–35 sorting and listing calm spots; 35–55 scoring calm spots and the cube net (4–5); 55–60 compare totals across tables.

## By band

- **K–1:** Stick arrows all round the swim ring so every arrow follows its neighbour: easy, no calm spot. Now the beach ball: where did the calm spot appear? Sort pictures of calm spots into spring, drain, whirl, split.
- **2–3:** On the beach ball, try for exactly one calm spot, then for two. Which kinds can you get together (a spring and a drain; two whirls; a spring, a drain and ...)? Record each ball as a list of calm spots. Then the swim ring: can you put exactly one calm spot on it?
- **4–5:** Score each calm spot: walk a small circle around it with a pointer that copies the arrows and count its turns (+1, −1, +2). What is the total on every ball? On every ring? Fold a cube net with springs at corners, saddles at edge midpoints and drains at face centres, and connect the total to V − E + F from Week 56.

## Checked facts

In `check_shape_2.py`, `check_week_166()`: numerical turning counts on a small circle give index +1 for spring, drain and whirl, −1 for the saddle, +2 for the dipole, −2 for the monkey saddle; the steady breeze on the plane becomes −w² at the far point of the sphere (index 2); spring plus drain totals 2, as do two springs, two drains and two saddles; V − E + F = 2 for the five Platonic solids and the "pillow" (two squares sewn together), 0 for 3-by-3 and 4-by-5 torus grids; the cube's corner-edge-face field totals 8 − 12 + 6 = 2. The theorems are cited.

## Nearest existing themes

Week 56 (Corners of a solid) proves V − E + F = 2 and Descartes' 720°; here the same number appears as a sum of calm-spot indices. Draft 129 (Wobbly table and crumpled map) is another "something must exist, we can't say where" result (intermediate values, Brouwer's fixed point theorem); draft 106 contrasts the sphere and the torus for map colouring. Atlas GA-04 follows an arrow around a dial (winding). Week 41 (Portals) makes the torus a board. New here: fields of arrows, the index of a zero, and a theorem whose answer depends on the shape of the surface.

## App connection

Shapes and spaces. A rotatable ball and a ring covered with a grid of arrow tiles; the child turns arrows, and the app shades any tile whose arrow differs from a neighbour's by more than 45° and marks calm spots with their type. Puzzles: "Make the ring with no calm spot"; "Give this ball exactly one calm spot"; "This ball has two springs and a whirl; what else must it have?" The Corners family (Week 56) could host the cube version.

## Open questions

- Whether arrow stickers on a beach ball give a clear enough sense of "neighbours almost the same" for K–1; a printed ball net with pre-placed dots may be steadier.
- The pointer-walk for the index is new to children; it should be rehearsed and perhaps taught first in the Week 167 draft (turning).
- Keep wind as a story only: real wind also blows up and down, so the cyclone claim is an idealisation (as Wikipedia notes).
