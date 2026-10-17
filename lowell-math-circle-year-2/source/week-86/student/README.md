# Week 86 revised student sources

Build with Python 3 and pdfLaTeX/TikZ (TeX Live). No artwork or Python packages are needed for the build.

```sh
python3 build.py --out ../ --work ../build
python3 verify.py
```

The builder uses `PDFLATEX` if set, otherwise `pdflatex` on PATH, with `/Library/TeX/texbin/pdflatex` as a macOS fallback. Each PDF compiles twice; creation/modification dates and trailer IDs are suppressed. Sources are self-contained and may be copied or extracted into a fresh directory.

Outputs: `shared.pdf` (Grades 2–5, 4 pages), `upper.pdf` (Grades 4–5, 6 pages), and `materials.pdf` (3 pages). No standalone K–1 packet. Print single-sided US Letter at 100%. F1/F2 original and working copies remain visible together. Working dots are 22 mm diameter, except P7's 20 mm dots with 28 mm center spacing. Other working centers are at least 32 mm apart. Examples use 8 mm reference dots. Turn tiles are 35 mm square; cutout counters are 18 mm.

## Revision choices

- Paths specify the fewest C turns; staying consumes a turn.
- D1/D2 use regular six-dot layouts with no three centers collinear. Retained connected/all-six-dots/at-least-six-roads conditions.
- Fold Problem 4 retains the original and uses opaque removable covers on the printed working copy. No sleeve-erasure option. Materials page 3 specifies opaque paper/card rectangles (24 by 32 mm), strips about 5 mm wide, scissors, and removable tape; trim covers around surviving graph features. The original fold rule still compares accessible sets in one current graph and includes staying.
- Q6 starts both cops at a; exact solver checks its optimal three-turn guarantee. Q8 and the every-ring explanation retain their open placement and full depth. Stack cops sharing one dot.

Revised, digitally verified, and unpiloted. Physical printing, counter fit/stacking, turn-tile assembly and fold-cover procedure rehearsal are untested. No facilitator guide is part of this stage. See QA.md for the review and rebuild evidence.
