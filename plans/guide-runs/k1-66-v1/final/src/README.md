# Week 66 K–1 adult guide — revised source

Rebuild from this directory with `./build.sh`. It writes `../k1-guide.pdf`, removes
its temporary TeX outputs and runs `check_guide.py` last. Requires Python 3,
Poppler (`pdftotext`), pdfLaTeX and its usual `lmodern`, `amsmath`, `amssymb`,
`array`, `booktabs`, `fancyhdr`, `geometry`, and `tikz` packages.

The checker first uses `../k-1.pdf`. While this folder is in a repository run,
it instead discovers `plans/k1-drafts/week-66/k-1.pdf` beneath an ancestor.
For a portable clean rebuild, copy this directory and the exact final student
PDF beside it; no repository, network, student Python source, or absolute path
is required. The PDF hash fixes the eight student pages against which the
writer manually transcribed and checked every target. If the student PDF is
changed, the checker deliberately stops pending fresh inspection.

The checker implements its own seven-position breadth-first search and compares
all 896 distances with the unrestricted-line covering-walk formula. It checks
all 24 guide answer-table rows directly from the TeX, including pictured lamp
positions, pawn positions, move words, step/flip decompositions and totals. It
enumerates the full shortest-word lists for Problem 5, the two tied Problem 4
home-ending words, and exact-length reachability for every Problem 8 candidate.
It verifies the P6/P7 neighbor diagrams, walking-order comparisons, parity,
non-task table demonstration, and guide/student page structure.

No student page is modified. This is the reviser-stage source following the preserved Claude review. All three should-fix and ten minor findings are addressed; see the run-level reviser report. Classroom use and physical setup remain untested.

The revised checker also verifies every neighboring pair among the 896 finite
states has distances differing by exactly one. The general explanation uses the
triangle inequality and evenness; finite enumeration does not prove the general theorem.
