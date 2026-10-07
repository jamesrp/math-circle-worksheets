# Week 77 adult guide: Persistent holes

Four-page adult guide for the five-page, six-problem Grades 4-5 prerequisite-led
student prototype (F77-45-v1). The adult guide is F77-FAC-v1. It opens with the
mathematical facts and limits, supplies one practical route for three children
and a mathematical adult, and gives complete solutions, ordered hints, exact
preparation counts, and a return-visit route for the fan-board problem.

## Build

Requires Python 3 and an installed TeX Live or MacTeX distribution with pdfLaTeX,
geometry, fancyhdr, array, amsmath, amssymb, and url. No Python packages are needed.

From this folder:

    python3 check_math.py
    python3 build.py --out output

The output is output/facilitator.pdf. The builder runs the checker first, refuses
overfull TeX boxes, and retains a build log in the chosen output directory.
If a minimal TeX installation has no initialized format or filename database,
the builder discovers the installed distribution with kpsewhich and builds its
format in a temporary directory. It does not download software or bundle fonts
or format dumps.

This guide source folder is self-contained: it can be renamed or moved, and does
not read the sibling student folder, the original run folder, or repository
research/review files. The student packet is needed only for classroom use, not
to rebuild or check the guide.

## Independent verification

check_math.py transcribes the final printed boards and schedules, then directly
enumerates edge subsets and filled-face subsets. It checks all answers in
Problems 1-6, all schedule alternatives, all four possible fan loops, all six
pairs and all 24 fan filling orders. Actual inclusion-map ranks, computed as
cosets of old cycles modulo later boundaries, independently check the printed
interval answers. The square formula is also checked on 84 finite schedules
including ties. These finite checks do not replace the guide's general proofs.

The code does not import student code, source comments, earlier reviewers'
answers, persistence libraries, or mathematical data outside this folder.

## Classroom limits and sources

The packet needs short-label reading, an unchanged saved edge list, and pair
cancellation. The guide does not supply a K-1 or separate Grades 2-3 edition.
Use one shared board at a time; Problems 1-3 form the first route. Problem 6 is
a readiness-dependent continuation. Physical handling, exact tile fit, pacing,
and classroom use remain unpiloted and must be rehearsed with real materials.

Background: Herbert Edelsbrunner, David Letscher and Afra Zomorodian,
*Topological Persistence and Simplification* (2002), Section 2 (PDF pages 2-3)
and Section 3 (PDF pages 4-6):
https://pub.ista.ac.at/~edels/Papers/2002-J-04-TopologicalPersistence.pdf

The square, joined-triangle and fan examples are independently devised. No
source papers, borrowed figures, external fonts, or runtime files are packaged.
