# Week 94 independent mathematics review

Reviewed the actual draft PDFs: K–1 (2 pages, Problems 1–3), Grades 2–3 (4 pages, Problems 1–7), and Grades 4–5 (5 pages, Problems 1–7). Extracted their text and independently rendered and visually inspected all 11 pages. Inspected diagram coordinates in `draft/src/common.tex` and the student sources. Did not read `review.md` or the author's checking script before completing verification. No student sources were edited.

## Located issue

**K–1, page 2, Problem 2 — small boundary ambiguity, not an incorrect length.**

Exact text: “Find every place each strip can go with one end at 7. Draw its two ends on a ruler.” The four displayed rulers run from 2 to 14. Strip D is 6 units long.

The intended answer, if both ends must lie on the printed ruler, is A: (5,7) and (7,9); B: (4,7) and (7,10); C: (3,7) and (7,11); D: (7,13) only. However, if the strip may overhang the ruler, D also has the legal length-6 placement (1,7). Children can physically place it that way, but the second endpoint is outside the supplied numbered scale. Thus “every place” has one or two answers for D depending on an unstated boundary convention. The diagram strongly suggests the intended convention, so this is a minor clarification rather than a substantive mathematical failure.

Smallest fix: replace the first sentence with “Find every place each strip fits entirely on the printed ruler with one end at 7.” Retain the current rulers and strip sizes.

No other K–1 mathematical problems found. Problem 1 has lengths A=2, B=3, C=4, D=6, invariant under translation. Problem 3 has the single unordered solution A+C=D when using the four supplied strips once each; reversing A and C does not give a new length combination. The ruler, twelve-square row, and supplied strips use the same nominal 12 mm unit in the PDF source and visually agree in the actual PDFs.

## Clean bands

**Grades 2–3 checks out completely, all four pages and seven problems.** All six offset choices produce positive feasible hidden lengths. In Problem 2 the full list is (6,9), (5,8), (4,7), (3,6), (2,5), (1,4); Problem 3's difference is always 3. Problem 4's hidden lengths are (5,8), (7,10), and (3,6). In Problem 6, I needs its last report changed from 10 to 9; II is consistent with offset 6; III needs its middle report changed from 6 to 5. The open games in Problems 1, 5, and 7 admit the stated checking/reveal procedures. All printed cases and diagrams agree with those calculations.

**Grades 4–5 checks out completely, all five pages and seven problems.** Independently checked all 21 finite machines, the three candidates after 2 reports 6, the exact two-point calibrations, all three one-report repairs, the non-affine counterexample, and the error bounds. In particular:

- Problems 1–2 deliberately permit one-report identification for some finite machines; this is correct. A 6-unit request identifies 17 of the 21 machines immediately, with ambiguity only at reports 12 and 18. Any two distinct supplied lengths identify every machine. If a 7-unit reference is constructed, its single report identifies all 21 machines. These facts do not contradict the later continuous stretch-and-shift model.
- Problem 4 has exactly three repairs: change the report at length 2 to 6, at length 4 to 11.5, or at length 6 to 15. Every resulting stretch is positive.
- Problem 5 explicitly removes the stretch-and-shift promise. Rules can agree at every input below 8 and still disagree at 8, so no number of such tests forces its report without additional assumptions.
- Problem 6 gives stretch ranges [1,3] and [7/4,9/4]. Achieving rules (shift,stretch) are (7,1), (1,3), (11/2,7/4), and (5/2,9/4), respectively.
- Problem 7's strongest worst-case choice is 1 and 10, giving possible-slope width at most 4/9, attained when the positive-slope restriction does not truncate the interval. Ten repeats at one reference cannot bound the slope: any positive slope can be offset to give the same repeated report. The worst-case interpretation matters; no averaging assumption is used.

## Independent evidence and limits

`check_math_independent.py` is a portable standard-library Python check, independent of all draft code. It records a solution or verification for every problem and passes when run with `python3 check_math_independent.py`. Exhaustive finite searches and exact rational arithmetic support the results above; the script also records the algebraic reason behind the continuum conclusions. Fresh rendered pages are in `math-review-renders/`.

This is a mathematics review of the draft, not a claim of classroom piloting or a physical cutting/measurement rehearsal. No need to change correct mathematical content in the two older bands.
