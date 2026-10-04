# Week 16 return-visit revised student companion

Four pages and four consecutive problems support exactly three investigations:

- Problems 1–2: a fourth interior letter, with an oral small-star entry followed by a free three-step mesh.
- Problem 3: boundary labels and changing the diagonal of a square.
- Problem 4: counterclockwise positive/negative rainbow triangles.

The fourth letter G is allowed only at interior dots in Problems 1–2. Problems 3–4 reset to R/B/Y only. The shared boundary rule on page 1 applies to page 2; offer those two pages together or retain the first page's rules during the second search. Every corner and side choice in Problem 4 is shown on its board. The draft does not print the discoveries, enumeration, minimum witness or proof route. Approximate bands are entries, not requirements.

Fresh writer, adversarial critic, independent mathematics reviewer and reviser stages have been completed for these student pages. It remains unpiloted. Printed material fit, timing and physical procedure have not been rehearsed. The parent coordinator creates and checks the separate adult guide. The revision defines counted triangles as cells with no subdivision lines inside and retains three pairs of signed totals. Four numbered problems still support exactly three investigations.

Requires Python 3 and pdfLaTeX with TikZ, fancyhdr and Latin Modern (ordinary TeX packages). No custom fonts, images or repository files are required.

```sh
sh build.sh
```

If pdfLaTeX is not on PATH, set `PDFLATEX` to its executable. The builder runs `generate.py`, compiles twice into `../build`, and writes `../return-visit.pdf`. `return-visit.tex` is portable and may also be edited and compiled directly; running the generator again replaces it from `generate.py`.

```sh
python3 check_math.py
```

The included writer check covers all 256 legal four-label mesh fillings, all 81 square corner patterns with both diagonals, all 192 ordinary mesh fillings, both signed convention examples, the small star and equilateral working-cell geometry. Its JSON is adult verification evidence, not student content. Exact general assumptions/proofs belong to the coordinator's adult guide.

Print US Letter, single-sided, Actual Size. Main mesh side: 4.5 inches; signed mesh side: 4.2 inches. Main dot spacing: 38.1 mm; signed spacing: 35.56 mm. Movable letter/color labels up to 12 mm or pencils are proposed. Digital dimensions do not establish physical readiness.
