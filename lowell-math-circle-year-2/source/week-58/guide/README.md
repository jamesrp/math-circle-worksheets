# Week 58 facilitator guide source

This separate, original nine-page guide accompanies the final seven-page student packet and ten-page material packet, footer versions `W58-shared-v2` and `W58-materials-v2`. It does not edit or rebuild those PDFs. It contains the theorem-first overview, fixed KK11/3333/445 routes, actual stock and smaller print choices, all seven solutions, complete labeled counts, exact 100/200 mm cuts, replacement-only paper R3 instructions, return investigations and precise source notes. Physical pretests and classroom piloting are unperformed.

From any working directory:

```sh
sh /path/to/guide/build.sh /path/to/output
python3 /path/to/guide/verify_math.py /path/to/output/guide-math.json
python3 /path/to/guide/verify_pdf.py /path/to/output
```

The build produces `facilitator.pdf` and uses a temporary directory for all TeX intermediates. Requirements: standard TeX Live with `pdflatex`, `article`, `geometry`, `fontenc`, `helvet`, `amsmath`, `amssymb`, `array`, `booktabs`, `tabularx`, `fancyhdr`, `xcolor`, `TikZ`, `enumitem`, `url`. No external assets, custom fonts, shell escape or network are needed. Fixed compilation time makes visual builds stable.

The independently written mathematical verifier uses Python's standard library. It enumerates Problem 1's 16 allocations (4 pass), Problem 2's 16 (5 pass), Problem 5's 8 whole allocations (none pass) and 16 allocations of fixed halves (4 pass), and Problem 6's 27 allocations (1 envy-free, 2 proportional). Fractions verify strip values exactly. Finite profile checks supplement the algebraic universal proofs; they do not prove the theorems alone.

PDF verification needs Python 3 with PyMuPDF (`import pymupdf`); repository runtime: `tmp/bonus-35-51-venv/bin/python`. The verifier renders every page outside the source folder, checks Letter dimensions and text bounds, and independently rebuilds a copied source folder and a freshly ZIP-extracted source folder. It compares text, page dimensions, rotation and rendered pixels with the delivered guide. Inspect the rendered pages visually as well; automated text bounds do not establish absence of overlap.

The lean portable source is only these five files: `guide.tex`, `build.sh`, `verify_math.py`, `verify_pdf.py`, `README.md`. Do not add generated PDFs, renders, workflow prompts, borrowed exemplar blocks or third-party reference PDFs. Build and QA reports belong outside this directory.

Mathematical precedent: Ariel D. Procaccia, *Cake Cutting Algorithms*, §§13.2–13.3.1, author-hosted PDF pp. 1–4, <https://procaccia.info/wp-content/uploads/2020/03/cakechapter.pdf>; §13.3.3 pp. 5–6 is three-person background only. Pedagogical sources actually read: *Math Circle by the Bay*, Preface printed vii–ix (PDF 8–10); Rozhkovskaya, *Math Circles for Elementary School Students*, EPUB `part0010.xhtml` introduction, `part0011.xhtml` Lesson 1 “At the lesson,” `part0016.xhtml` Lesson 6 sausage discussion; organizer's *Handouts 8.docx*, Problems 8.1 and 8.5. Guide page 9 distinguishes source findings from design inferences. Source files remain in their repository reference folders and are not bundled.

Wording, figures, prompts and verifiers are authored for this project. Established mathematics is not claimed as new. Root `REPUBLISHING.md` was read. No borrowed reference passage or workflow writing example is reproduced in this bundle.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
