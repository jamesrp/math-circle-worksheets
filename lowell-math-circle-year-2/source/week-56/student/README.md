# Week 56 revised student packet: Corners of a solid

Fresh writer stage followed by independent critic, mathematics review and revision, October 4, 2026. `students.pdf` has nine original student pages; `materials.pdf` has four preparation pages. The material PDF is not a second student investigation. No facilitator guide was authored. All wording and TikZ figures were made for this packet, not copied from prior worksheets or source exemplars.

## Rebuild

From any directory:

```sh
sh /absolute/path/to/student/build.sh /absolute/path/to/output
```

Requires `pdflatex` and standard TeX Live packages: article, geometry, fontenc, helvet, tikz (arrows.meta, calc), array, tabularx, fancyhdr, amsmath. Both PDFs have US Letter pages and standard Helvetica-family fonts. The build uses a disposable directory for all TeX intermediates.

The five checked-in `*-net.tex` files are original editable TikZ assets. Regenerate them with `python3 make_assets.py` if changing model geometry. Python standard library only. `geometry-checks.json` records the asset checks. Generating nets is not required for an ordinary rebuild.

For render and mathematical QA, use `python3 verify.py OUTPUT_DIR QA_DIR`; requires PyMuPDF and Pillow. It checks all 28 actual PDF face polygons and all 16 fan cutouts for 30 mm edges, plus both 80 mm full-turn circles. Use `python3 audit_math.py OUTPUT_DIR QA_DIR` for the separate incidence/convex-hull/fan/subdivision/PDF-vector audit, which also checks actual PDF tab separation. Use `python3 clean_rebuild.py OUTPUT_DIR QA_DIR` for clean copied-source and extracted lean-ZIP builds, checking exact text, dimensions and rendered-pixel reproduction for both PDFs. QA output belongs outside the source package. Read every rendered page after an edit. Digital checks do not establish physical fit.

## Prerequisites and route

Pages 1–3, approximately Grades 2–5: adult-read short directions, counting to 24, identifying and preserving shared incidence on a closed physical surface, matching full-turn gaps to corner pieces. The concrete fan investigation on page 3 can be offered to younger children after the common adult demonstration, with adult reading and recording; no independent K–1 packet is claimed.

Pages 4–6, approximately Grades 2–5 with arithmetic support: multiples of 60 and 90 degrees, subtraction from 360, multiplication to total up equal gaps; keeping one unchanged assembled model as the reference. Page 5 introduces unequal gaps by vertex type. Page 6's zero-defect subdivision points are intentional; they are counted surface vertices, not new geometric corners of a convex body.

Pages 7–9, approximately Grades 4–5 with a mathematician and readiness for explanation: connected graphs, loops and trees, adding and subtracting V/E/F counts; triangle and polygon angle sums; multiplication/division, and using one mathematical rule to explain another. These are continuations and may require later visits. An observed numerical agreement is evidence for a conjecture; the edge/face cancellation and tree argument, followed by face-angle cancellation, explain the global facts. The first visit need not reach these pages.

## Concrete preparation

Prepare one closed cube, regular tetrahedron, regular octahedron, right equilateral triangular prism and square pyramid at each table: three identical five-solid sets. Print material pages 1–3 once per table on cardstock and page 4 for the circles/square pieces. Adult scissors cut nets and assemble them before class. The face edges are 30 mm, the tabs 6 mm deep with 4 mm tapered ends. All face polygons use equal x/y scaling. Net letters pair the cut edges; the small blue labels identify assembled vertices. Every face must be attached, including the hidden bottom faces. Reject any model whose seam labels or corner labels do not match. Check the 30 mm ruler before cutting.

For five pairs/groups, print the triangle strip on material page 3 and the squares/circles on page 4 once per pair/group. Each receives eight whole equilateral triangles, eight whole squares and two 80 mm circles. Use removable tape to build and unfold fans. For page 6, supply one additional cube per table, or place clear removable tape on the cube faces so children can draw and erase the three redrawings one at a time. Each redraw starts from the original cube; do not accumulate all three changes without recording it as a different case. A washable pen or removable marks can identify counted corners and edges.

Use the closed models in the shared launch. Let children handle them, then touch one face, one edge shared by two faces, and one assembled vertex. Demonstrate one fan using two triangle corners on a full-turn circle, then join a third corner so the free sides can meet when folded. The student conventions show separate sides → shared edge → a shared vertex, and loose triangle corners → one corner placed → a completed flat fan with gap. Do not count a net as an assembled solid or a bare wire frame as a face-covered solid.

The precise paper/tab fit, tape flexibility, assembly time, marker handling and session timing have **not been physically rehearsed**. All investigations are **unpiloted**. Matching computed lengths and checking absence of 2D overlap are digital checks only.

## Mathematical precedents and source scope

Use `plans/new-themes-52-63/week-56/research-notes.md` for the wider research record. Mathematical precedents: Keenan Crane, *Discrete Differential Geometry: An Applied Introduction*, Exercise 2.1 (printed p.22 / PDF p.23), Exercises 5.9–5.10 (printed pp.95–96 / PDF pp.96–97); Vicky Neale, NRICH, *Euler's Formula*, theorem and edge-removal proof; Thomas F. Banchoff, *Beyond the Third Dimension*, Chapter 5 section 2, regular polygon corners at a polyhedron vertex. Our particular tasks, model choices, paper nets and the elementary face-angle cancellation presentation are authored adaptations. Attribution does not imply that the adaptation has been classroom validated.

Urls: https://www.cs.cmu.edu/~kmcrane/Projects/DDG/paper.pdf ; https://nrich.maths.org/articles/eulers-formula ; https://www.math.brown.edu/tbanchof/Beyond3d/chapter5/section02.html

The assumptions are a finite closed convex polyhedron, or a sphere surface divided into polygonal disk faces meeting along whole edges. Every assembled edge meets two faces. The defects are planar face-angle gaps, not dihedral angles. Open surfaces are only used with the missing face explicitly omitted on page 7. Polygon subdivision creates zero defect at a new face-center or edge point. A local positive fan gap alone does not guarantee a globally assembled convex solid. Page 9's two specific cases exist as the regular icosahedron and dodecahedron, although building them is not part of the task.

## Revision and mathematical explanation

Revision v2 addresses the two fan-closure tests, compares the alternating count for all four Problem 1 models before the cube redrawings, scopes Problems 7–9 to polygon faces, and removes the unnecessary angle-measuring direction. The preparation PDF and exact net/fan geometry are unchanged. Student footer ID is N56-S-v2; unchanged materials retain N56-M-v1.

For the Euler reduction, remove one face and view the remaining connected surface graph in the plane through its opening. Delete an edge on a cycle, preserving connectivity and merging two regions, possibly including the unbounded outside region. The edge count and bounded-region count each decrease by one. A tree has E=V-1 and no bounded regions, so the opened count is V-E+F=1. Restoring the missing face adds one to obtain 2. No bridge is deleted; an open physical net has different incidence and is not this drawing.

The sum of the planar angles in an n-sided face is 180(n-2) degrees. Since every assembled edge belongs to two faces, all face-side incidences sum to 2E. Thus the angle total over all faces is 360(E-F), and the sum of vertex gaps is 360V-360(E-F)=360(V-E+F)=720 degrees. The square pyramid has a 120-degree apex gap and four 150-degree base gaps. A new vertex inside a face or along an unchanged edge has zero gap. Observed agreement among models suggests these claims; the tree reduction and angle-sum cancellation explain them.

The six tested fans have gaps 180,120,60,0,90,0 degrees in printed order. Every open fan can lie flat. Only the zero-gap fans close flat with no gap; the four positive-gap fans can close to a pointed convex corner without inward dents. Without the no-dents condition, a six-triangle fan can also make a nonconvex pointed cone. A positive local gap does not guarantee that an arbitrary set of fans assembles to a whole convex solid.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
