# Week 124 (draft plan): One straight cut

**Strand:** shape (Shapes and spaces). **Deep-math field:** computational origami, reflections and symmetry. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The fold-and-cut theorem: every drawing made of straight segments on a sheet of paper (any polygon, several polygons, nested or touching ones, even stray segments) can be folded flat so that one complete straight cut cuts along exactly the drawing and nothing else. It was proved by two methods around 1998: the straight-skeleton method of Erik Demaine, Martin Demaine and Anna Lubiw, and the disk-packing method of Marshall Bern, Erik Demaine, David Eppstein and Barry Hayes. The theorem idealises paper (zero thickness, any number of layers) and may need complicated, non-simple folds. Children work with the simple part of the idea, which is reflection: a fold maps one side of a crease onto the other, so after folding, the cut line touches every point that folds onto it. One fold and a cut always gives a shape with a mirror line; to cut out a polygon, the folds must stack every edge on one line and nothing else on it. With simple folds this is concrete and checkable: a square needs two folds (both diagonals), an equilateral triangle two (two of its mirror lines), and a rectangle that is not a square three (both mirror lines, then the bisector of a corner angle, which lays its two edges on one line). For a regular n-gon folded only along its own mirror lines, every fold at best halves the folded wedge, so ⌈log₂ n⌉ folds are needed and suffice: 2, 2, 3, 3, 3, 3, 4, 4 for n = 3 to 10 (checked here; whether non-mirror folds can ever do better I have not checked). History: the problem appears in a 1721 Japanese puzzle book (Kan Chu Sen); a legend credits Betsy Ross with a one-cut five-point star; Houdini's Paper Magic (1922) shows a star; Martin Gardner posed the general question. Proved: the theorem. Checked: the fold sequences above. Children can discover the role of mirror lines, the angle-bisector fold, and the fold-count pattern for regular shapes.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Fold-and-Cut](https://erikdemaine.org/foldcut/), Erik Demaine's page (read November 3, 2026). The theorem's statement, the two solution methods and their authors, the history (1721, Betsy Ross, Houdini, Gardner) and printable examples.
- [Fold-and-cut theorem: a vertical maths project around origami](https://ar5iv.labs.arxiv.org/html/2004.08683), Maria Luisa Spreafico and Eulalia Tramuns, arXiv 2004.08683, about 2020 (read November 3, 2026). About 150 pupils aged 8 to 10 and 27 aged 12: free cuts, cutting a square by symmetry axes, a triangle and rectangle at home, a pre-creased star; most found at least two folding sequences, and failures exposed weak understanding of symmetry axes.
- Prior use with children: [Fold and Cut, Week 6](https://sites.math.washington.edu/~mathcircle/circle/archive/2024-25/files/24au-week06.pdf), University of Washington Math Circle, autumn 2024 (read November 3, 2026): fewest folds for the regular triangle, square and 5- to 10-gons, a table, and the pattern behind it.
- Prior use with children: [Book 13: Fold-and-Cut Flag Puzzles](https://jrmf.org/wp-content/uploads/2022/08/Fold-And-Cut-Flag-Puzzles-Book-13-5.5-x-8.5-v13.pdf), Nancy Blachman and Skona Brittain, Julia Robinson Mathematics Festival (read November 3, 2026): square, rectangle, isosceles triangle, six- and five-point stars and a ring of 13 stars, each with one straight cut.

## A kid-friendly way in

Fold a sheet, make one straight cut, and predict what falls out. Materials: plenty of thin paper (printer paper cut into 15 cm squares; origami paper is easier), scissors, pencils, target cards with a shape drawn in the middle of a square sheet (square, rectangle, triangle, plus sign, five-point star, letters such as L, T and E). Prep: cut paper with a paper cutter and print target cards (20 minutes). Launch (2–3 minutes): fold a sheet in half, make one straight cut across the folded edge, and ask the group to predict the piece before unfolding; then show a target square drawn on a sheet and ask whether one cut can free exactly that square.

## By band

- **K–1:** Fold once and cut: predict and unfold, then match each result to the fold line (every shape has a mirror). Make a heart, a tree, a symmetric "person". Then try the square target with an adult showing the two diagonal folds.
- **2–3:** One-cut targets: square, rectangle, equilateral triangle, plus sign, letters. Find a folding for each and the fewest folds. Why does folding a corner in half put two edges on top of each other?
- **4–5:** Regular shapes from triangle to decagon: fewest folds, recorded in a table, and the pattern (the UW circle's question). Explain with the halving wedge why 8 sides need 3 folds. The five-point star (the Betsy Ross legend) and two separate shapes at once as extensions; the general theorem told as a story.

## Checked facts

In `check_shape_a.py`, `check_week_124()`: a simple-fold simulator applies each fold as a reflection and checks both directions (every edge point lands on the cut line, and every paper point landing on the line is an edge point) for the square with its two diagonal folds, the equilateral triangle with two mirror-line folds and the 4-by-2 rectangle with two halvings and a corner bisector; the rectangle's two halvings alone fail; the fewest mirror-line folds for regular n-gons are 2, 2, 3, 3, 3, 3, 4, 4 for n = 3 to 10, equal to ⌈log₂ n⌉. The theorem and history are cited to Demaine's page.

## Nearest existing themes

Week 28 (Flat folds) is the closest: crease patterns, Kawasaki's and Maekawa's conditions for folding flat. This week uses flat folding for a different goal (aligning edges) and needs only simple folds. Week 35 (Footprint borders), Week 37 (Mirror twins) and the reflection weeks 9 and 21 share mirror lines. The Year A summer plan's session 12, "Mirrors and folded shapes" (`plans/grades-2-3-year-a.md`), already proposes predicting cuts in folded paper and reversing the question; this draft is the deeper version of that idea for a return visit, and the two should not run close together. New here: designing folds to hit a target, the bisector fold, and a fold-count pattern with a halving explanation.

## App connection

Shapes and spaces. The Flat folds family (`creases`, Week 28) could carry a group: the child taps lines to fold a square sheet (the app animates the reflection), then drags one cut line; the app unfolds and shows what was cut out. A board is solved when the cut matches the target outline. Puzzles: "Cut out this square with one cut"; "Cut out a hexagon in 3 folds"; "Cut out two squares at once". The app should mark extra cut lines in red rather than refuse, so children see why a fold was missing.

## Open questions

- Paper thickness: three or four folds of printer paper are hard to cut through cleanly for K–1 and 2–3; test origami paper and scissor sizes.
- Fewest folds: the mirror-line count is checked, but whether other simple folds ever do better for a regular n-gon is not; the guide should present the table as "fewest we found" unless that is settled.
- How much of the five-point star to give: the classic star folds are not mirror-line folds of the star alone and may need a printed fold sheet (JRMF and Demaine give diagrams).
- Spacing from the Year A "Mirrors and folded shapes" session if both are used.
