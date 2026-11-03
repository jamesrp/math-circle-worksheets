# Week 121 (draft plan): Flat patterns that fold into a box

**Strand:** shape (Shapes and spaces). **Deep-math field:** polyhedra, spanning trees, unfolding (computational geometry). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Cutting a convex polyhedron along some of its edges so that it unfolds flat in one piece is an edge unfolding. The cut edges must form a spanning tree of the corners (V − 1 cuts: a loop of cuts would free a piece, and an uncut corner would not flatten), and the uncut edges, the hinges, form a spanning tree of the faces (F − 1 hinges). For the cube that is 7 cuts and 5 hinges. The cube's corner network has 384 spanning trees, which fall into exactly 11 classes under the cube's 48 symmetries, and every one of the 384 unfolds without overlap; so there are exactly 11 cube nets up to turning and flipping. Of the 35 hexominoes (six-square shapes), exactly those 11 fold into a cube. Half of the 24 failures can be spotted without folding: a 2-by-2 block would put four squares round one corner (a cube corner has three), and five in a row wraps onto itself; the other 12 fail only when folded. The research question behind this is Dürer's problem, formalised in 1975 and still open: does every convex polyhedron have at least one edge unfolding that does not overlap (a net)? Partial answers: Ghomi (Geometry and Topology, 2014) showed that every convex polyhedron becomes unfoldable after a suitable stretch, so every convex polyhedron is combinatorially equivalent to one with a net; a badly chosen cut tree can overlap even on a convex polyhedron, so the question is whether a good tree always exists; if cuts may cross faces, every convex polyhedron unfolds (O'Rourke's survey). For nonconvex polyhedra the answer is no: Bern, Demaine, Eppstein, Kuo, Mantler and Snoeyink gave polyhedra with 24 convex faces and with 36 triangular faces that cannot be edge-unfolded. Proved: the 11, the tree structure, the nonconvex counterexamples. Checked here: 384, 11, 35, the 12-and-12 split. Open: Dürer's problem.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Unfolding Polyhedra](https://ar5iv.arxiv.org/html/1908.07152), Joseph O'Rourke, arXiv 1908.07152 survey (read November 3, 2026). States Dürer's problem, that it remains open, and tabulates what is proved (any-cut unfoldings of convex polyhedra) and where counterexamples exist (nonconvex edge unfolding).
- [Ununfoldable Polyhedra with Convex Faces](https://arxiv.org/abs/cs/9908003), Bern, Demaine, Eppstein, Kuo, Mantler, Snoeyink, arXiv cs/9908003, 1999, revised 2001 (read November 3, 2026). Two nonconvex polyhedra (24 convex faces; 36 triangles) with no edge unfolding; they unfold if cuts may cross faces.
- [Affine Unfoldings of Convex Polyhedra: Progress on Dürer's Problem](https://ghomi.math.gatech.edu/Papers/durerPF.pdf), Mohammad Ghomi, 2015 summary of his Geometry and Topology 18 (2014) paper (read November 3, 2026). "The problem remains wide open"; every convex polyhedron becomes unfoldable after an affine stretch.
- Prior use with children: [Cube Nets, Task 31](https://mathematicscentre.com/taskcentre/031cuben.htm), Mathematics Centre (Australia), Years 2 to 10 (read November 3, 2026): find the 11 nets by guess and check, then by trying every case; extension asks how many hexominoes there are. Also [Christmas Boxes](https://nrich.maths.org/974/note?nomenu=1), NRICH, ages 11 to 14 (read November 3, 2026): find all six-square nets of a cube; answer 11 up to rotation and reflection.

## A kid-friendly way in

Cut open a real box and lay it flat, then hunt for other flat patterns of six squares that fold into the same box. Materials: one small cube box (or a Magna-Tiles cube) for the demonstration; 2 cm grid paper (or 1-inch); scissors; tape; a sorting mat with two areas, "folds into a box" and "does not". Prep: print grid paper and the mat (10 minutes). Launch (2–3 minutes): build a cube from six magnetic squares or unfold a box along edges, lay it flat, and show one six-square shape folding back up; then show a "plus" shape and ask whether it folds.

## By band

- **K–1:** Make six-square shapes from square tiles or cut-out squares, fold them around a cube block, and sort into "box" and "not a box". Tape hinges on one favourite and fold it shut.
- **2–3:** Find as many different nets as possible; decide when two are "the same" (turned or flipped). The class pools a checkable collection on the mat. Which non-nets can you rule out before folding?
- **4–5:** Why does every net have exactly 5 taped hinges and 7 cut edges? Is the collection complete (an organised search, for example by the longest row)? Extend: a net of a tetrahedron or octahedron from triangle paper, and the open question told as a story: nobody knows whether every convex solid has a net.

## Checked facts

In `check_shape_a.py`, `check_week_121()`: 216 fixed and 35 free hexominoes; a cube-rolling test finds exactly 11 that fold; the cube's 12-edge corner network has 384 spanning trees of 7 cuts, forming 11 classes under 48 symmetries; unfolding each of the 384 gives six different grid cells (no overlap) and always one of the 11 nets; none of the 11 has a 2-by-2 block or five in a row, and 12 of the 24 non-nets have one of these. Dürer's problem and the nonconvex counterexamples are cited.

## Nearest existing themes

Week 56 (Corners of a solid) builds its models from printed nets and its Problem 7 erases edges down to a tree; its review proposed an app "Unfold" board with the 11 cube nets, and the October 10 decision kept unfolding on paper. Week 53 (Cheapest connected networks) owns spanning trees. Week 26 (Same area, different boundaries) works with polyominoes and the boundary count (each net has boundary 14). Week 98 also uses grid shapes. New here: the classification of the 11 nets, the cut-tree and hinge-tree pairing seen in a solid, and an open research problem children can understand. The 11 nets themselves are a familiar school topic; the depth is in the trees and in Dürer's question.

## App connection

Shapes and spaces. A flat family "Box patterns": the child places six squares on a grid, presses Fold, and the app animates the fold or shows the two faces that collide; a checked "That's all" for the 11. A harder group gives a cube with some edges marked as cut and asks for the rest (exactly 7 cuts, no loop). This needs only a 2D grid and a short fold animation; the 3D turning solid stays off-screen as decided for Week 56.

## Open questions

- Is finding all 11 too long a search for one hour at 2–3? A pooled class collection may be the right shape.
- Fold accuracy on 2 cm squares for K–1 hands; magnetic squares may be better than paper.
- Whether the tree language (cuts never form a loop) lands at 4–5 without Week 53, or should wait until after it.
- A guide that tells the Dürer story should recheck the problem's status at the time of writing; recent preprints keep appearing.
