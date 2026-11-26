# Week 98 K–1 adult guide: writer-stage source

This is the writer-stage guide for the final nine-page K–1 draft, not a revised
student packet. It remains unpiloted and physically unrehearsed.

From this folder, run `./build.sh`. It writes `../k1-guide.pdf`, rejects TeX
errors and overfull boxes, removes temporary TeX products, then runs
`check_guide.py`. Requirements: Python 3.10+, Poppler (`pdftotext`), and a
configured pdfLaTeX installation with lmodern, geometry, amsmath, amssymb,
array, booktabs, fancyhdr, and TikZ. There are no external images, private
resources, network dependencies, or machine-specific paths.

For a portable clean rebuild, place the unchanged student `k-1.pdf` beside
this `src/` folder (or beside `guide-src/` after packaging). The checker tries
that first; if absent, it searches ancestor directories for the repository's
`plans/k1-drafts/week-98/k-1.pdf`. It deliberately fails on a different student
PDF fingerprint, so later student changes require a fresh visual/data check.

The checker independently enumerates seed sets and removal routes from
transcriptions of the final PDF, without importing the student checker.
It also checks all legal-order finishes and every legal perimeter change
on all 512 states of the 3-by-3 board. Its finite enumeration backs the small
instances; the guide's arguments establish the general facts. Human visual
inspection remains necessary for diagrams and layout.
