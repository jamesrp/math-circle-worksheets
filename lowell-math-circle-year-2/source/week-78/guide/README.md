# Week 78 adult guide: Three-armed lines

Original four-page facilitator guide for the single prerequisite-led Grades 4–5
student prototype (F78-S-v1). Intended staffing: one mathematician with three
children; this guide supplies no K–1 or separate Grades 2–3 activity.

## Build

Requires Python 3 (standard library only) and a normal TeX Live or MacTeX
installation with pdfLaTeX, Latin Modern, geometry, amsmath/amssymb, array,
tabularx, fancyhdr and url. No downloaded fonts, images or papers are needed.

    python3 build.py --out /path/to/output

This runs the independent exact-rational mathematical check, compiles twice and
writes `facilitator.pdf`. Build intermediates, including a generated format if a
minimal TeX installation lacks one, stay under the chosen output directory in
`.build-facilitator/`. The source folder can be copied and built on its own.

    python3 check_math.py

The checker independently encodes the final plotted coordinates, solves all nine
pairs of parameterized rays, checks full ray answers (rather than sampled grid
dots), checks all numerical answers and audits 6,561 rational junction pairs and
6,561 inverse target pairs. It imports no student source or checker. These finite
checks do not prove the all-real theorems; the guide gives geometric proofs.

## Print and use

Print single-sided Letter at 100%. The guide gives exact materials for three
children in two working pairs, with the adult as the fourth partner. Student
pages are shared per pair and handed out one page at a time. Problems 1–3 form
the core; 4–5 are readiness-based extensions and 6–7 can take a later session.
Physical preparation/handling rehearsal and classroom piloting are unperformed.

## Source lineage

- David Speyer and Bernd Sturmfels, *Tropical Mathematics* (2004), §§1 and 3:
  https://www.claymath.org/wp-content/uploads/2022/03/Speyer.pdf
- Ayush Kumar Tewari, *Point-Line Geometry in the Tropical Plane* (2020), §§3–4:
  https://arxiv.org/abs/2006.04425 (max-plus convention; reverse directions for
  this min-plus packet).

Definitions follow that mathematical framework. The final-case solutions,
rectangle argument, inverse construction and practical guide are independently
authored; no external text, figures, fonts or papers are packaged. The guide's
rendered pages were digitally inspected; that does not establish classroom fit.
