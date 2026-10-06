# Week 66 writer prototype

One shared four-page Grades 3–5 packet. Prerequisites: order signed positions on a line, count moves, preserve both lamp and walker state, compare short move words. No group notation. This is an unpiloted writer draft, not an adult guide or final revision.

Build: `python3 build.py` or `python3 build.py --out PATH`. Produces `students.pdf` and `build.log`. Requirements: Python 3, TeX Live with TikZ, fancyhdr, amssymb. No repository imports, absolute paths, external images, or downloaded texts.

Check: `python3 check_math.py`. The checks compare BFS on all 4,608 finite-street states with the extremal-visit line formula. Removing excursions outside the endpoint/required-lamp interval cannot hurt, so the finite boundary does not alter these target distances.

Sources for the mathematical brief: Druţu–Kapovich, Geometric Group Theory, Exercise 7.82, printed p.233 / PDF p.253, https://www.math.ucdavis.edu/~kapovich/EPR/ggt.pdf ; Cleary–Taback, Dead end words in lamplighter groups and other wreath products, PDF p.9, https://arxiv.org/pdf/math/0309344 . The worksheet wording and diagrams are newly authored. Digital checks do not establish physical rehearsal or classroom readiness.
