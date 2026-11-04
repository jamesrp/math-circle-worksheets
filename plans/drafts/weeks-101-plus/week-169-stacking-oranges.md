# Week 169 (draft plan): Stacking oranges

**Strand:** shape (Shapes and spaces). **Deep-math field:** discrete geometry, sphere packing, computer-assisted and formal proof. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The Kepler conjecture, now a theorem: no packing of equal balls in space fills a larger fraction of space than π/√18 ≈ 0.7405, the density of the grocer's stack (the face-centred cubic packing). Kepler asserted it in 1611; Gauss proved in 1831 that it is the best lattice packing (balls arranged in a regular repeating grid); Hilbert included the general case in his 18th problem (1900); Thomas Hales announced a proof in 1998 relying heavily on computer calculations (interval arithmetic, linear programming, enumerating planar maps), published as "A proof of the Kepler conjecture" in the Annals of Mathematics 162 (2005). Because referees could not check every computer step, Hales led the Flyspeck project, a formal proof checked line by line in the HOL Light and Isabelle proof assistants, whose official account appeared on arXiv in 2015. The best density is not unique: the hexagonal close packing, which stacks the same triangular layers in a different order, is equally dense. Two facts children can see directly. First, a square pyramid of balls (layers 1, 4, 9, 16, ...) and a triangular pyramid (layers 1, 3, 6, 10, ...) are the same packing seen from different directions: in both, every ball inside the stack touches exactly 12 others, 4 in its own square layer, 4 above and 4 below. Second, stacking balls straight on top of each other in a cube grid is much worse, π/6 ≈ 0.524, and straight-up stacking of triangular layers gives π/(3√3) ≈ 0.605. Poured randomly into a jar, equal balls settle near 0.61, and repeated shaking raises this to about 0.64 (Scott and others), but "random close packing" is an experimental number, not a theorem. Counting the stacks: square pyramids hold 1, 5, 14, 30, 55, 91 balls; triangular pyramids 1, 4, 10, 20, 35, 56. Lucas's cannonball question: 1² + 2² + ... + 24² = 4900 = 70², a square pyramid that can be rearranged as a flat square, and G. N. Watson proved in 1918 that 24 is the only case above 1. Proved: Kepler (Hales, Flyspeck), Gauss's lattice case, Watson. Checked here: the counts, densities, the 12 contacts, the cannonball number up to a million. Experimental: the 0.64 of random packing.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [An overview of the Kepler conjecture](https://arxiv.org/pdf/math/9811071v1), Thomas C. Hales, arXiv math/9811071 (1998) (read November 4, 2026). Kepler 1611, Gauss 1831 for lattices, Hilbert's 18th problem, the density π/√18 ≈ 0.74048, hexagonal close packing as equally good, the computer's roles in the proof. The journal version is recorded as Annals of Mathematics 162 (2005), 1065–1185.
- [A formal proof of the Kepler conjecture](https://arxiv.org/abs/1501.02155), Thomas Hales and 21 coauthors, arXiv 1501.02155 (January 2015) (read November 4, 2026). The Flyspeck project's official account of the formal proof in HOL Light and Isabelle.
- [Random close packing of granular matter](https://arxiv.org/pdf/0710.2463), Charles Radin, arXiv 0710.2463 (2007) (read November 4, 2026). Poured balls near 0.61, shaken to about 0.64 (Scott and Kilgour 0.6366), the maximum π/√18 ≈ 0.74.
- [Square pyramidal numbers, A000330](https://oeis.org/A000330), OEIS (read November 4, 2026). 1, 5, 14, 30, 55, 91, ...; the only square above 1 is 4900 (Watson 1918; Lucas's problem).
- Prior use with children: [Cannon balls](https://meaningfulmaths.nt.edu.au/mmws/nz/resource/cannon-balls.html), NZ Maths problem (Level Two of the NZ curriculum), hosted by Meaningful Maths (read November 4, 2026). Stack tennis balls or oranges, count the layers of a triangular pyramid (10, 6, 3, 1, total 20) and extend the pattern.

## A kid-friendly way in

A bag of oranges for the launch; per table, 60 to 100 ping-pong balls (bulk packs) or large marbles, a square frame (four rulers or a shallow box lid, 4 or 5 balls wide), a triangular frame (three rulers taped), a clear plastic box about 4 balls by 4 balls by 6 balls high, and squares of non-slip drawer liner. Prep about 20 minutes: count balls into tubs, tape frames, check the box size. Launch (2–3 minutes): build a three-layer orange pyramid on a tray while the group watches (9, then 4 in the hollows, then 1), and ask: could the oranges sit straight on top of each other instead? Which way uses less room?

Suggested hour: 0–5 orange launch; 5–25 square and triangular pyramids; 25–40 the box filled two ways; 40–55 counting contacts and the cannonball puzzle (4–5); 55–60 share counts and the better box.

## By band

- **K–1:** Build square and triangular pyramids in the frames; count each layer and the whole stack. Try to make a ball sit straight on top of another (it rolls into a hollow). Which pyramid is taller with the same number of layers?
- **2–3:** Pyramid counts: predict how many balls a 5-layer square pyramid needs (55) and a 5-layer triangle (35) before building. Fill the clear box two ways, layers straight on top and layers in the hollows, and count: which holds more? Hold one ball and count how many it touches in the middle of a big stack.
- **4–5:** Show that the square pyramid is a tilted triangular pyramid: find the triangular layers on its slanted faces. Explain why every inside ball touches 12. The cannonball puzzle: which square pyramid can be laid flat as a square? (Use a table of the counts; 4900 needs 24 layers.) Story: Kepler's claim, the 1998 computer proof and the formal check reported in 2015.

## Checked facts

In `check_shape_2.py`, `check_week_169()`: square-pyramid counts 1, 5, 14, 30, 55, 91, 140 and triangular 1, 4, 10, 20, 35, 56, 84, with the closed formula; n = 24 is the only n from 2 to 1,000,000 with a square total (4900 = 70²); π/√18 ≈ 0.74048, π/6 ≈ 0.5236, π/(3√3) ≈ 0.6046; a 6-layer square pyramid of 91 unit balls has no overlaps; in the offset square-layer packing each ball touches 12 (4 beside, 4 above, 4 below), and those 12 map exactly onto the 12 nearest points of the face-centred cubic lattice; in a box 4 by 4 balls, height 4 holds 64 straight against 66 offset, height 6 holds 96 against 100. Kepler's theorem, Gauss, Watson and the 0.64 are cited.

## Nearest existing themes

Week 88 (Packing and kissing circles) is the flat version: six disks around one, and its plan explicitly left out three dimensions and Kepler's density, so this week is its natural sequel. Year 1 used figurate numbers, so the pyramid counts are partly familiar; here they serve the packing question, and the cannonball 4900 is new. Week 56 (Corners of a solid) and draft 120 (deltahedra) are other three-dimensional builds. New here: density as a fraction of space, the identity of the two pyramids, and the story of a computer-checked proof.

## App connection

Shapes and spaces. A 3D stacking board: the child drops balls into a frame layer by layer, and the app snaps each ball into a hollow or on top, with a counter and a "fill" meter for the box. Puzzles: "Fill this box with as many balls as you can"; "How many balls make a 6-layer triangle pyramid?"; "Turn the square pyramid until you see triangles". No existing family carries 3D stacking; this would be new, and Week 88's flat packing could share its counters.

## Open questions

- Ping-pong balls roll; test drawer liner and a frame so a 4-layer pyramid stands for K–1 hands.
- The box comparison gives a small difference (64 against 66); decide whether it is convincing or whether a taller box is needed.
- Whether the "square pyramid is a triangular pyramid" claim can be seen physically by grades 4–5 without a model to rotate.
