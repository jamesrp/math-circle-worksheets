# Week 78: Three-armed lines

Original four-page shared student prototype for Grades 4–5, by prerequisites.
No separate younger-band packet or facilitator guide is included in this student
packet. Problems move from choosing and drawing junctions to intersections,
constructing lines through points, and all-case explanations.

## Prerequisites and use limits

Children should be able to follow horizontal, vertical, and 45-degree diagonal
rays on an equal-scale square grid and compare small whole numbers. An adult may
read the text. The opening minimum-tie example uses nonnegative numbers; signed
arithmetic is not required for the drawing tasks. Later explanations require
reasoning beyond a finite drawing and beyond integer grid points.

Print on US Letter paper, single-sided, at 100% scale. Each pair needs two
contrasting pencils and a ruler or straightedge. Large square-grid working boards
and two movable junction counters can support further trials; tracing paper is
optional. The printed packet can be used with ordinary paper and pencil. Physical
printing, manipulation, timing, and classroom use have not been tested.

## Build and checks

Requires Python 3 (standard library only), pdfLaTeX, TikZ/PGF, Latin Modern,
geometry, and fancyhdr. From this directory:

    python3 check_math.py
    python3 build.py --out /absolute/path/to/output

The result is `students.pdf`. Build intermediates stay in the output directory's
`.build/` folder. The builder checks the mathematics first, then runs pdfLaTeX
twice. If a minimal TeX installation has packages but no search databases or
format, the builder uses read-only file lookup and generates a private format
inside `.build/`; it does not change the system TeX installation.

For visual review with Poppler:

    pdfinfo /absolute/path/to/output/students.pdf
    pdftoppm -r 90 -png /absolute/path/to/output/students.pdf /absolute/path/to/output/page

All diagram coordinates are original. `data.py` supplies the task cases;
`build.py` writes their TikZ definitions. `check_math.py` uses exact rational
ray intersection calculations to check every supplied finite case, including
whole shared rays. It also checks 2,401 ordered integer-junction pairs against an
independent rectangle formula, verifies inverse constructions, and checks the
minimum-tie convention at half-grid points. The fixed opening trials include both
unequal-width/height southwest/northeast arrangements. Problem 6 includes a pair
whose intersection is outside the printed 0--8 grid. Every finite expectation
list is length-checked, so an added case cannot be silently skipped. A finite regression is not an
all-real proof or evidence of classroom readiness.

## Mathematical source relationship

David Speyer and Bernd Sturmfels, *Tropical Mathematics*, Sections 1 and 3,
printed pages 1–2 and 6–8:
https://www.claymath.org/wp-content/uploads/2022/03/Speyer.pdf

The source supplies min-plus arithmetic, the corner-locus definition (the
minimum is attained at least twice), the north/east/southwest orientation of a
tropical line, and generic intersection and interpolation statements. For a
junction `(a,b)`, this packet uses the corner locus of
`min(x-a, y-b, 0)`. Its opening example `min(x,y,2)` has junction `(2,2)`;
subtracting 2 from all terms gives the same corner locus. Equal larger terms
alone do not put a point on the line.

The precise elementary ray classifications, inverse-locus classifications,
rectangle calculation, coordinates, tasks, diagrams, and verification code were
independently derived for this prototype. The checks and tasks concern ordinary
set intersections; they do not replace an overlap by a stable intersection or
introduce multiplicity. No source text, external diagrams, papers, workflow
prompts, or downloaded resources are packaged here.
