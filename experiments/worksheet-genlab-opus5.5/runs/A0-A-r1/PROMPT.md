Make an activity PDF for each of three grade levels (K–1, grades 2–3, and grades 4–5) targeting a 1-hour math circle where the kids will get to work with each other and also with professional mathematicians guiding them. High-level activity outline is below.


=== Activity outline ===

Week 1: Tiling with pattern blocks

Mathematical kernels

1. Coloring obstructions and best possible packings. On the triangular grid every small triangle points up or down, and every blue rhombus covers exactly one up-triangle and one down-triangle. So a region with more up-triangles than down-triangles cannot be tiled by blue rhombi, even when its area is even, and the difference between the two counts is a lower bound on how many triangles must stay uncovered. This is the triangular-grid version of the mutilated-checkerboard argument (dominoes cannot tile a chessboard with two opposite corners removed). A triangle with n small edges on each side has n more up-triangles than down-triangles, so blue rhombi always leave at least n triangles uncovered, and n can be achieved. A piece made of two blue rhombi (the purple chevron) can never do better than blue rhombi alone, because each chevron splits into two blues.

2. Rhombus tilings of a hexagon, and flips. A hexagon on the triangular grid can usually be tiled by blue rhombi in several ways. Any two tilings are connected by flips: wherever three rhombi form a small hexagon, rotate them into the hexagon's other filling. The tilings and flips form a graph worth exploring (shortest flip routes between tilings; whether you can return to a tiling in an odd number of flips). Rhombus tilings correspond to stacks of cubes and to lattice paths: following the chain of rhombi that crosses the hexagon from one side to the opposite side traces a path ("ribbon") of left and right steps. Ribbons can be used to count all tilings and to prove facts about flips; for example each flip swaps an adjacent left/right pair in a ribbon, so every round trip takes an even number of flips. Sources: Thurston, "Conway's tiling groups" (1990); Saldanha and Tomei, "An overview of domino and lozenge tilings"; MIT 18.312 lectures on rhombus tilings and plane partitions.

Suggested emphasis by level: grades 2–3 work with possible and impossible boards and fewest-gap packings (kernel 1); grades 4–5 explore the tilings of a small hexagon, flips between them, and ribbons (kernel 2); K–1 works with the same pieces at an entry point suited to them.

Materials

21st Century Pattern Blocks, plenty for ten children: green triangle (each edge 1 inch), blue rhombus (two triangles), red trapezoid (three triangles), yellow hexagon (six triangles), purple chevron (a concave six-sided piece equal in area to two blue rhombi, and exactly coverable by two blues), plus pink right triangles, teal kites, and gray darts. There are no orange squares or tan thin rhombi. Upscale pattern blocks at 2× and 3× size are also available. Paper, pencils, and small whiteboards.

Any board on which children place physical blocks must be printed at actual size: the small triangle's edge is 1 inch (2.54 cm).


=== Session context ===

The Bellingham Math Circle is an elementary-school math circle that meets weekly for one hour. Its purpose is enjoyment, curiosity, and real mathematical thinking rather than school arithmetic practice.

Children at this session: ten. Two kindergartners and one first grader; four third graders; two fourth graders and one fifth grader. Grade bands (K–1, 2–3, 4–5) are rough entry points, and a child may work from another band's pages.

Adults: three. The organizer (a research mathematician), a second mathematician, and one parent volunteer who is not a mathematician. Each adult stays mainly with one band's group.

Shape of the hour: a few minutes of free handling of the materials; a short whole-group demonstration of the concrete action everyone will use; about forty minutes of work in the three groups, where children work together and talk with their adult; a few minutes of sharing at the end.

Pages are printed single-sided on US Letter paper at 100% scale.


Technical instructions

Your working directory is runs/A0-A-r1. Keep all your files inside it: LaTeX sources in runs/A0-A-r1/src/ and the three finished PDFs at exactly these paths:

  runs/A0-A-r1/final/k-1.pdf
  runs/A0-A-r1/final/grades-2-3.pdf
  runs/A0-A-r1/final/grades-4-5.pdf

The deliverable is the student pages only. There is no separate facilitator guide.

Tools available: pdflatex, xelatex, lualatex (TeX Live with TikZ and texlive-fonts-extra), python3, pdftoppm, pdftotext. Draw diagrams with TikZ or with Python-generated TikZ. Before you finish, compile each PDF, render its pages to PNG (for example `pdftoppm -r 60 -png file.pdf prefix`), and look at every page with the Read tool to check that the diagrams are correct and nothing overflows or overlaps. Fix what you find.

Isolation: this is a controlled experiment. Use only the information in these instructions. Do not read any file outside runs/A0-A-r1 (in particular nothing elsewhere under /home/claude/genlab and nothing under /mnt/user-data), do not use web search or web fetch, and do not use any remote-device, computer, or browser tools.

When you are done, reply with the three PDF paths and their page counts, in under 80 words.
