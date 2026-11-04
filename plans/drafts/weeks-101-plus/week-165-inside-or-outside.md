# Week 165 (draft plan): Inside or outside?

**Strand:** shape (Shapes and spaces). **Deep-math field:** plane topology, the Jordan curve theorem, parity. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The Jordan curve theorem: a simple closed curve in the plane (a continuous loop that never touches itself) splits the rest of the plane into exactly two connected regions, a bounded inside and an unbounded outside, and every point of the curve borders both. For polygons there is a practical test and a short proof. Draw a straight ray from a point that avoids the polygon's corners and count how many times it crosses the polygon: odd means inside, even means outside. The count's parity is the same for every such ray, because sliding or turning the ray changes the count by 0 or 2, and it flips each time the point itself crosses the curve; walking alongside the curve shows there are at most two regions. Hales's formal-proof paper uses exactly this parity (the number of horizontal edges below a square of a grid polygon). For general continuous curves the theorem is much harder, because curves can be wild (Osgood's 1903 curve has positive area) and the polygon argument has to pass to a limit. Camille Jordan published a proof in his Cours d'analyse (1887); it was long called incomplete, Oswald Veblen's 1905 proof was regarded as the first rigorous one, and Thomas Hales has argued that Jordan's proof is essentially sound. Hales completed a computer-checked formal proof in HOL Light in January 2005 (138 definitions, 1381 lemmas, about 59,000 lines), and the Mizar team finished another in September 2005. Limits: the curve must not cross itself. For a self-crossing loop the crossing parity still colours the regions in two colours like a chessboard, but "inside" splits into degrees: the centre of a five-pointed star drawn in one stroke has even parity yet is wrapped twice (winding number 2). In space, a sphere still separates inside from outside, but the Alexander horned sphere shows the outside can be tangled. Proved: the theorem and the polygon parity test. Checked here: the floor-spiral example and the star. What children can discover: the crossing-count trick, that the direction of the ray never matters, where the trick breaks (through a corner, along an edge, a self-crossing loop), and why each crossing switches in and out.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Jordan curve theorem, formally and informally](https://cse-robotics.engr.tamu.edu/dshell/cs625/Hales-Jordan-Curve.pdf), Thomas C. Hales, American Mathematical Monthly 114 (December 2007), 882–894 (read November 4, 2026). Veblen 1905; the HOL Light proof of January 2005 and its size; the Mizar proof of September 2005; the parity function for grid polygons.
- [Jordan's proof of the Jordan curve theorem](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hales1.pdf), Thomas C. Hales, Studies in Logic, Grammar and Rhetoric 10(23), 2007 (read November 4, 2026). Jordan's proof is essentially sound; Veblen's proof and its reception; parity by counting crossings of a downward ray (Lemma 1).
- [Jordan curve theorem](https://en.wikipedia.org/wiki/Jordan_curve_theorem), Wikipedia, as a secondary pointer (read November 4, 2026). The 1887 date; the even-odd ray rule in computational geometry; Osgood's curve; Schoenflies; the Alexander horned sphere.
- Prior use with children: [Topology, section 5: Inside or Outside](https://teachersinstitute.yale.edu/curriculum/units/1980/7/80.07.08/7), Bhim Sain Kaeley, Yale-New Haven Teachers Institute unit 80.07.08 (1980) (read November 4, 2026). Students draw simple closed curves and find the rule: a line from the point to the outside crossing an odd number of times means inside.
- Prior use with children: [Colouring Curves Game](https://nrich.maths.org/7030), NRICH, ages 7 to 14 (read November 4, 2026). Self-crossing closed curves, a shading game on their regions, and the idea that all such curves can be coloured with two colours.

## A kid-friendly way in

A long rope or clothesline (10 to 15 m) laid on the floor as a twisting spiral; a stuffed animal; masking tape; printed "tangle" sheets (big simple closed curves with six bugs each), straightedges and stickers. Prep about 25 minutes: draw and print four tangle sheets of rising difficulty and practise laying the rope spiral. Launch (2–3 minutes): put the toy deep in the rope spiral and ask "inside or outside?" Take a vote, then have one child walk in a straight line from the toy to the wall, counting aloud each time they step over the rope; reveal by tracing the rope or flood-walking without stepping over it.

Suggested hour: 0–5 rope launch; 5–20 rope loops and jumping (K–1) or tangle sheets; 20–40 designing tricky loops for a partner; 40–55 corners, edges and self-crossing loops (4–5); 55–60 share the hardest loop and its count.

## By band

- **K–1:** Jump in and out of rope loops and count jumps: after 1 jump you are in, after 2 out. Colour the inside of simple loops on paper; place counters inside or outside a string loop and check by tracing a finger along a path that never crosses the line.
- **2–3:** Tangle sheets: decide quickly for each bug and check by colouring. Does the direction of your straight line change the answer? Draw a loop where a bug looks outside but is inside, and swap with a partner.
- **4–5:** Why does each crossing switch in and out, and why can two different rays never disagree? What goes wrong when the ray passes through a corner or along an edge, and how to fix it? Self-crossing loops (a figure eight, a star drawn in one stroke): the parity still two-colours the regions, but is the star's centre "inside"? Story: the theorem that took from 1887 to 2005 to check by computer.

## Checked facts

In `check_shape_2.py`, `check_week_165()`: a 16-corner spiral loop with outer box 12 by 12 is simple and encloses 52 of its 144 unit squares; for 3000 random points the four ray directions agree, and odd parity matches winding number ±1; a toy at the inner end of the corridor is crossed 5 times by a ray to the left and 3 times to the right; a point between corridor walls is crossed 4 times; for a bow-tie loop both lobes have odd parity and winding numbers +1 and −1; the centre of a one-stroke pentagram has winding number 2 and even parity, a star tip winding 1 and odd parity. The theorem, history and formal-proof sizes are cited above.

## Nearest existing themes

Week 48 (Inside and outside covers) takes "inside" for granted and traps area; this week asks what makes inside well defined. Draft 106 (Colouring maps) two-colours maps of whole lines and circles by the same parity of crossings; here parity decides a single point and the region count is the theorem. Draft 107 (Mazes) depends on whether walls connect to the outer wall; a hand-on-the-wall walk traces one side of a curve. The scouting draft on Hex uses the Jordan curve theorem for "no draws". Weeks 41 and 75 use signed crossings for winding. New here: the separation theorem itself, the ray-parity test and its failure cases, and parity against winding.

## App connection

Shapes and spaces, a possible new family "In or out": a long closed loop on a grid and several bugs; the child taps in or out, or drags a ray from a bug and the app counts the crossings as the ray grows. Puzzles: "Which bugs are inside? You may draw two rays"; "Add one wall segment so this bug is inside"; "Draw a loop whose ray from the bug crosses 7 times". Area traps (Week 48) could share the grid board.

## Open questions

- Floor space and rope length for a spiral with 5 or more crossings; rehearse in the school hall.
- Whether 2–3 children see "walk out without stepping on the rope" as the definition and the count as a shortcut, or confuse the two.
- How much of the self-crossing material to keep for 4–5: it overlaps draft 106 and leads to winding number (the Week 167 draft).
