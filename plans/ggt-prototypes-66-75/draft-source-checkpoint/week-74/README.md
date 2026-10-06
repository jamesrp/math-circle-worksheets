# Doubling elevators student prototype

Writer-stage draft, four US Letter student pages, Grades 4–5. Unpiloted; physical pawn/board rehearsal is untested. Reading simple move letters, locating a horizontal coordinate, doubling, and reasoning about a move budget are prerequisites. The third child can referee or rotate into either partner role.

Build with `python3 build.py --out /chosen/output` using Python 3 and a normal TeX Live installation with pdflatex, TikZ, geometry, fancyhdr, and Latin Modern. The source entrypoint is `students.tex`; the output is `students.pdf`. Run `python3 check_math.py` for exact route checks and the all-routes budget bound. The finite printed board is a working window, not a mathematical boundary.

Source lineage: Nicholas Touikan, *Introduction to Combinatorial and Geometric Group Theory*, section on HNN extensions and Baumslag–Solitar groups, https://ntouikan.ext.unb.ca/MATH6022/IntroCGGT/html_output/section-15.html (read October 6, 2026). The elevator game is an independently authored nonnegative-height exponential-shortcut model, not the full Cayley graph of BS(1,2). Outline also references Cornelia Druţu and Michael Kapovich, *Geometric Group Theory*, printed p.285 / PDF p.305, https://www.math.ucdavis.edu/~kapovich/EPR/ggt.pdf . No source text or downloaded reference is packaged.
