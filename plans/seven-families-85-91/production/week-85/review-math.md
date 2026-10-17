# Week 85 independent mathematical review

Reviewed `draft/shared.pdf` (4 pages, Grades 2–5), `draft/upper.pdf` (4 pages, Grades 4–5), and `draft/materials.pdf` (10 pages). These are the actual packets; the generic three-band names in the stage prompt do not exist. No draft files were changed. Mathematical evidence is in `independent-math-check.py`, `independent-math-results.json`, and `independent-math-evidence.md`; the checker is independent of the writer's checker.

## 1. Shared, page 4, Problem 4: “box F” has two different possible boundaries

**Exact text:** “Make different paths for T whose copies stay inside box F. What is the largest rectangle T can trace whose copy fills the box?”

**Located diagram:** The F label appears beside an outer dashed 110 × 100 mm rectangle enclosing an unlabeled solid 40 × 30 mm rectangle. The same arrangement is on materials page 7, insert F.

**Evidence:** Taking the intended solid rectangle gives a 20 × 15 mm tracer rectangle, at mat x=130..150, y=132.5..147.5. Taking the dashed rectangle gives a 55 × 50 mm tracer rectangle, at x=110..165, y=115..165. These are different answers, and the latter extends 5 mm beyond the marked T zone x=110..160. The latter interpretation is particularly plausible because F labels the outer insert border, while “box” is not qualified. The mapping used here follows independently from the linkage, P=2T−O with O=(40,140).

**Smallest fix:** Change the first sentence to “Make different paths for T whose copies stay inside the small solid box on insert F.” Retain the second sentence. Alternatively, move F immediately beside the solid box in both diagrams and make clear that the dashed border is the insert edge.

## 2. Materials pages 7–8, G/H/I for upper page 2, Problem 2: unit grids are offset from the shape lattice

**Exact task:** “Use inserts G, H and I with the square and triangle pieces. How many square units cover each original and its copy?”

**Located diagrams:** The faint 10 mm grids behind G and H on materials page 7 and I on page 8.

**Evidence from PDF vector coordinates, measured from each page's lower-left corner:**

- G's square corners are (42,52), (62,52), (62,72), (42,72), while grid lines lie at x=40,50,60,… and y=50,60,70,…: a 2 mm offset in each direction.
- H's corners use x=141,151,171 and y=52,62,72, while grid lines use x=140,150,160,… and y=50,60,70,…: offsets of 1 mm and 2 mm.
- I's vertices are (42,153), (72,153), (42,183), while grid lines use x=40,50,60,… and y=150,160,170,…: offsets of 2 mm and 3 mm.

The printed grid therefore does not show the intended unit-square/half-square partitions. This is a diagram accuracy issue, not an impossibility: the physical pieces still tile G/H/I exactly, with areas 4, 4, and 4.5 square units; their copies have areas 16, 16, and 18.

**Smallest fix:** Remove the three optional faint grids. If retaining them, shift a local TikZ scope to each insert's (x+10,y+10), and draw `grid (50,50)` from local (0,0), so the grid phase follows the insert rather than the global page origin.

## Coverage and limits

The shared packet's other tasks check out under the adult material-page instruction to keep the frame simple and noncrossed. All four upper tasks check out mathematically; its area materials have the grid issue above. All specified targets and the intended inverse targets fit their assigned zones. The 20 mm anchor translation and 10 mm compensation are correct. The six equal-length constraints and all nine printed mechanism poses check out. Exact area-piece decompositions fit the supplied 48 squares and 16 triangles, for one original/copy pair at a time. The bar templates, mat registration, bridge, and cutout inventory were checked digitally. Physical stack, coaxial tips, motion, clearance, support, branch retention and handling remain untested, as the packet correctly states.
