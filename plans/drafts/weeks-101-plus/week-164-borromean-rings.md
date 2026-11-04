# Week 164 (draft plan): Three rings that hold together

**Strand:** shape (Shapes and spaces). **Deep-math field:** knot and link theory, Brunnian links, linking numbers. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The Borromean rings are three closed loops that cannot be pulled apart, although no two of them are linked: cut any one and the other two fall free. A link with this property for any number of loops (it is not an unlink, but removing any one loop leaves an unlink) is called Brunnian, after Hermann Brunn, whose 1892 paper "Über Verkettung" gave examples. Brunnian links exist for every number of loops from three up; one family is a ring of rubber bands, each looped around the next and the last around the first. The standard tool for "how linked are two loops" is the linking number: give each loop a direction, look at the crossings where one loop passes the other in a drawing, score each +1 or −1 by a right-hand rule, and halve the total. Equivalently, count the signed times one loop pierces a surface spanning the other (for a flat loop, its flat disk). Wiggling the loops without cutting never changes it. A Hopf pair (two hooked rings) has linking number ±1; every pair in the Borromean rings has linking number 0, so pairwise counts cannot see what holds the three together. Proving that the Borromean rings really are linked needs a three-way invariant (Milnor's invariants, 1954) or the fundamental group of the complement; children can only gather strong evidence by trying. A geometric surprise: the familiar picture with three round circles is an optical illusion. Freedman and Skora (1987) proved that a Brunnian link cannot be built from three round circles, and Lindström and Zetterström (1991) gave an independent proof; two circles and an ellipse arbitrarily close to round do work. Three rectangles with long side to short side above 1, placed in the three coordinate planes, do work, and for golden rectangles their twelve corners are the corners of a regular icosahedron. Matthew Cook conjectured that any three unknotted curves, unless all three are circles, can be moved into Borromean position; Howards (arXiv 2014) proved this for polygons (so, for example, three triangles), and the general case is still open as far as these sources say. In a flat drawing where each pair of rings overlaps like a Venn diagram, a pair is unhooked exactly when the same ring lies on top at both of its crossings; of the 8 such "who is on top" patterns, 6 are stacks that lift apart and 2 are cycles (red over blue, blue over yellow, yellow over red, and its mirror image), and those are the Borromean rings. Proved: Brunnian links for every n; no round Borromean rings; linking number invariance. Checked here: the 8 and 2, pairwise linking numbers in the models, the icosahedron. Open: Cook's conjecture for smooth curves.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [An infinite family of convex Brunnian links in ℝⁿ](https://arxiv.org/pdf/1101.4863), Bob Davis, Hugh Howards, Jonathan Newman and Jason Parsley, arXiv 1101.4863 (2011) (read November 4, 2026). Brunn's 1892 definition; Freedman and Skora's proof that at least one component must be non-circular and Lindström and Zetterström's independent proof; two circles and a nearly round ellipse suffice; no Brunnian link of round spheres.
- [Forming the Borromean rings out of arbitrary polygonal unknots](https://ar5iv.arxiv.org/html/1406.3370), Hugh Nelson Howards, arXiv 1406.3370 (2014) (read November 4, 2026). Cook's conjecture; any three polygonal unknots can be placed as Borromean rings by rigid motions and scaling, with no scaling needed when two are planar.
- [Brunnian link](https://en.wikipedia.org/wiki/Brunnian_link), Wikipedia, as a secondary pointer (read November 4, 2026). Rubber-band Brunnian links for every number of loops; Milnor's 1954 link-homotopy invariants.
- Prior use with children: [Folklore, the Borromean rings, the icosahedron, and three dimensions](https://arxiv.org/pdf/2009.09836), Dave Auckly, arXiv 2009.09836 (2020) (read November 4, 2026). Based on an activity at the Navajo Nation Math Circles summer camp: three golden rectangles make the Borromean rings and, with struts, an icosahedron "tent"; the rectangles cannot be assembled without breaking one; a proof that the rings are linked through the fundamental group.

## A kid-friendly way in

Pipe cleaners (chenille stems) in three colours, twisted closed into rings about 8 cm across; ends untwist to "cut" a ring. Index cards (3 by 5 inches, close to golden) with a long slot, plus tape. A printed recipe card with a three-ring Venn picture showing which colour is on top at each crossing. A 2 m loop of string per pair of children for the 4–5 chain. Prep about 20 minutes: twist a demonstration set and cut card slots. Launch (2–3 minutes): hold up three rings that hang together from one hand; ask a child to find two rings that are hooked (there are none); untwist one ring and let the other two drop to the table.

Suggested hour: 0–5 launch; 5–20 two-ring chains and the magic three from the recipe; 20–40 the eight Venn patterns (2–3) or arrows and crossing scores (4–5); 40–55 four-loop chain or card rectangles; 55–60 share which patterns held together.

## By band

- **K–1:** Hook two rings into a chain and pull to check. Then build the "magic three" from the recipe card with an adult (red lies on blue, blue on yellow, yellow on red) and test it: does it hang together? Untwist one ring: what happens to the others? Try untwisting each colour in turn.
- **2–3:** Lay three rings flat in a Venn pattern. Each pair crosses twice, and at each pair you choose which ring lies on top. Which choices hold together when lifted, and which fall apart or leave two rings hooked? Find every choice where no two rings are hooked; sort them into "lifts apart" and "holds together" (8 patterns, 2 hold). Extension: make the three rings from three slotted cards.
- **4–5:** Build a Brunnian chain of four (each loop folded round the next, the last round the first) and test that removing any one loop frees all. Put arrows on two rings and score crossings +1 or −1 with the hand rule: a hooked pair gives ±1, each Borromean pair 0. Discuss what a count of 0 does and does not prove. Story: why the round-circle picture is impossible, and the golden rectangles that make an icosahedron.

## Checked facts

In `check_shape_2.py`, `check_week_164()`: in the model with three ellipses (half-axes 2 and 1) in the three coordinate planes, ring 2 misses ring 1's flat disk and ring 3 pierces it twice with opposite signs, so both pairs have linking number 0 (the cyclic symmetry carries this to all pairs); a Hopf pair pierces once (±1); three rectangles with half-sides 1 and L give the same pattern for L = 1.2, 1.5, φ, 2 and 3; the 12 corners of three golden rectangles have 30 equal shortest distances, five at each corner (a regular icosahedron); in the Venn drawing, 64 over/under choices, 8 with every pair unhooked, 2 of them cyclic. The theorems (Freedman–Skora, Lindström–Zetterström, Howards, Brunn) are cited.

## Nearest existing themes

Week 40 (Loop colours) and atlas GA-26 are the library's knot weeks: three-colouring certifies that one knotted loop cannot become a plain loop. This week is about several loops, not one, and its central phenomenon (linked as a whole, unlinked in pairs) is new. Week 41 (Portals) and Week 75 (Twists on a cylinder) count signed crossings of a seam, which is the same bookkeeping as the linking number. Week 120 (draft, deltahedra) builds the icosahedron from triangles; here it appears as the corners of three rectangles. No week or draft covers links or Brunnian links.

## App connection

Shapes and spaces, near the Knot colours family (Week 40). Board: three coloured rings in a Venn layout; tapping a crossing swaps which ring is on top; a "lift" button animates whether the rings come apart, and a "cut" button removes one ring. Puzzles: "Make three rings that hold together but no two are hooked"; "Here are four loops; which single loop, when cut, frees everything?" A crossing-score view (+1 and −1 badges) supports the linking number. Knot colours could carry it if its diagram engine handles several components.

## Open questions

- Pipe-cleaner fit: rehearse the recipe so K–1 children can weave the third ring; pre-made pairs may be needed.
- The four-loop Brunnian chain: rehearse a pipe-cleaner or rubber-band recipe and print photos of each step; it is unrehearsed here.
- How to word "a count of 0 does not mean unlinked" for grades 4–5 without the three-way invariant.
- The card-rectangle model needs one card cut and taped; check whether 3 by 5 cards leave enough room.
