# Week 123 (draft plan): Guards in a gallery

**Strand:** shape, with networks (Shapes and spaces). **Deep-math field:** combinatorial geometry, visibility, graph colouring. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A gallery is a simple polygon (one closed wall, no holes) with n corners, and a guard sees every point joined to it by a straight segment inside the gallery. Chvátal's art gallery theorem (1975, answering Klee): ⌊n/3⌋ guards always suffice, and for every n some galleries, the combs, need that many. Fisk's proof (1978) is short enough for children to act out: cut the gallery into triangles with diagonals between corners (always possible, giving n − 2 triangles, as in Week 14), colour the corners with three colours so every triangle has all three (always possible, by adding triangles one at a time), then put a guard at every corner of the least-used colour; there are at most ⌊n/3⌋ of them, and every triangle has one, which sees the whole triangle. The lower bound uses a comb: no point sees the tips of two different teeth, so k teeth need k guards. For galleries whose walls all meet at right angles (orthogonal polygons, which always have an even number of corners, n = 2r + 4 with r inward corners), ⌊n/4⌋ guards suffice and are sometimes needed (Kahn, Klawe and Kleitman, 1983; Urrutia's note counts six proofs). Limits: these are worst-case bounds over all galleries with n corners; a particular gallery may need far fewer (a convex room needs one), and Fisk's choice depends on the triangulation, so it is a guarantee, not an optimum. Galleries with holes (pillars) need more guards and are a different theorem (Malkevitch lists them among open directions). Children can discover that dents create hiding places, design rooms that need two or three guards with as few walls as possible, and with the colouring see why n/3 is always enough.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Guards in Galleries](https://annalindeberg.github.io/assets/pdfs/gallery.pdf), Anna Lindeberg, expository article, November 11, 2024 (read November 3, 2026). States Chvátal's n/3 theorem with his 1975 paper and gives Fisk's triangulate-and-colour proof.
- [Research Resources for High School Students Related to Art Gallery Theorems](https://web.york.cuny.edu/~malk/high-school-research/artgalleryresearch.html), Joseph Malkevitch, York College (CUNY) (read November 3, 2026). Klee's question, Chvátal's ⌊n/3⌋, Fisk's colouring proof, orthogonal galleries as a conjecture to discover, and open variants (holes, equilateral polygons).
- [Sixth proof of the Orthogonal Art Gallery Theorem](https://www.matem.unam.mx/~urrutia/online_papers/IllumOrt.pdf), Jorge Urrutia, 1997 (read November 3, 2026). Any orthogonal polygon with n vertices can be guarded by ⌊n/4⌋ guards, first proved by Kahn, Klawe and Kleitman (SIAM J. Algebraic and Discrete Methods, 1983).
- Prior use with children: [The Art Gallery and the Fortress Problem](https://static.idm314.org/resources/activities/idm-art-gallery-en.pdf), Christiane Rousseau, International Day of Mathematics activity, 2023, ages 10–12 and up (read November 3, 2026). Participants place cameras at corners, triangulate and colour; orthogonal galleries; a fortress (guarding the outside) variant.

## A kid-friendly way in

Play hide-and-seek in a taped room. Materials: masking tape for one large floor outline with two or three dents (about 8 to 10 corners), printed gallery floor plans on letter paper (8 to 12 plans, from a 4-sided convex room to a 3-tooth comb), counters or toy figures as guards, string or a ruler for sight lines, three colours of dot stickers or crayons. Prep: draw the plans on grid paper and copy them (20 minutes), tape the floor outline at the start. Launch (2–3 minutes): one child stands as the guard in the tape room; others try to stand where the guard cannot see them without crossing a wall (check with string). Then show a paper plan, a guard counter and a string sight line.

## By band

- **K–1:** In the tape room and on large plans: can one guard see everywhere? Find a hiding place and move the guard to fix it. Build a room where one guard is not enough.
- **2–3:** For each plan, find the fewest guards and record where they stand. Draw a room that needs 2 guards with as few corners as possible, then 3. Is there a room with 6 corners that needs 3 guards?
- **4–5:** Fisk's method on paper: draw diagonals to cut the room into triangles, colour corners so each triangle has three colours, and put guards on the least-used colour. Why does every triangle get a guard, and why are there at most n/3 of them? Build a comb that really needs that many. Extension: rooms with only right angles (count corners, test n/4), and a pillar in the middle.

## Checked facts

In `check_shape_a.py`, `check_week_123()`: for triangular-tooth combs with k = 2 and 3 teeth (n = 3k + 2 corners, ⌊n/3⌋ = k), no point on a 0.25-step sample grid sees two tooth tips, and k guards below the teeth see every sample point (a sampled check, backed by the disjoint-cone argument); ear-clipping triangulates four test galleries into n − 2 triangles, Fisk's colouring gives every triangle three colours and a least class of at most ⌊n/3⌋; on a convex 9-gon a fan gives classes 1, 4, 4 and a zigzag 3, 3, 3, so the method's count depends on the triangulation; orthogonal combs with n = 4k corners satisfy n = 2r + 4 and need and are guarded by k guards (sampled). The general theorems are cited.

## Nearest existing themes

Week 14 (Polygon triangulations and flips) supplies the n − 2 triangles; here they become a tool. Week 62 (Conflict networks and scheduling) owns colouring; this is a forced three-colouring with a counting payoff. Week 31 (Hidden orchard) and Weeks 9, 21 and 71 use sight lines and reflection, but on lattices and in billiards, not polygon interiors. Week 15 (Nearest-site regions) assigns regions to sites by distance, not by sight. New here: visibility inside a nonconvex room, a worst-case bound with a matching construction, and a proof by colouring.

## App connection

Shapes and spaces (or Maps and networks). A new family, "Gallery guards": the child taps to place guards on a floor plan and the app shades what each guard sees; a board is solved when the floor is fully shaded with the target number of guards. A second group shows a triangulated plan and asks for a three-colouring of the corners, then lights the guards on the least colour. Puzzles: the 3-tooth comb (3 guards), an L-shaped room (1 guard, from the inner corner) and a right-angle comb with two teeth and 8 corners (2 guards), and "design a room that needs 2 guards with 6 corners". The Mirror Couriers or Sight lines boards have ray drawing that could be reused.

## Open questions

- Sight-line checking with string on letter-size plans: are the plans big enough for small hands, and do children accept "the string must not cross a wall" without arguing about corners?
- Guards at corners only (as in Fisk's proof) or anywhere (as in the hide-and-seek)? Both bounds are the same; decide which the student pages state.
- K–1 reading: the floor game needs none, but the paper plans need a picture rule.
- Rehearse the taped room in the actual space before relying on it.
