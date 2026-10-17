# Week 94 revised student sources

Build with `python3 build.py OUTPUT_DIRECTORY`. Requires Python 3 and `pdflatex` on PATH, with TikZ, Latin Modern, fancyhdr and standard LaTeX packages. On macOS, add `/Library/TeX/texbin` to PATH if needed. No runtime download or private reference is used. The `.tex` files are the editable sources. `common.tex` holds the shared layout and drawings.

`python3 check_math.py` checks exact finite cases, attainable bounded-error extremes and the reference-separation calculation. The builder sets fixed dates and suppresses volatile PDF metadata. `.build/` under the chosen output is disposable.

Print single-sided on US Letter at 100%. Every drawn length unit is 12 mm. Prepare exactly one each of strips A, B, C, and D per pair from the first page's lower area, preferably from a spare copy. Keep the twelve-square row uncut. These pieces and the K–1 rulers match each other. Commercial cubes represent whole-unit lengths by count; no claim is made that commercial cubes fit the printed scale.

The K–1 packet is an intentionally short concrete entry, not a promised full hour. The upper packet's last page is a readiness-dependent return investigation. All work is unpiloted. Physical printing, cutting and game rehearsal remain untested.

Revision-stage checks and final visual QA are recorded in `../revision-response.md`.

Mathematical scope: the finite 21-rule game can sometimes identify a rule from one report. For unrestricted positive stretch and unrestricted shift, one exact reference leaves infinitely many possible rules. In the noisy design problem, separation D gives an untruncated possible-stretch interval of width 4/D. Restricting to positive stretches can shorten it and can leave an open endpoint at zero; the width remains meaningful even when no minimum is attained. The concrete Problem 6 intervals stay strictly positive and attain both extrema. Problem 7 asks for the smallest worst-case bound before reports arrive, not dominance for every realized pair of reports.
