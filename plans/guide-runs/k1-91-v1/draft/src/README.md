# Week 91 K-1 adult guide: writer-stage source

Rebuild with `bash build.sh` from this folder (or invoke its path). Dependencies:
pdfLaTeX with the standard geometry, lmodern, amsmath/amssymb, array, booktabs,
fancyhdr and TikZ packages; Python 3; Poppler's `pdftotext` and `pdfinfo`.
The script compiles twice, rejects errors/overfull boxes/missing glyphs, removes
temporary LaTeX files and runs the independent checker. Output is
`../k1-guide.pdf`.

For a portable copy, put the unchanged final Week 91 student `k-1.pdf` beside
this folder. The checker first uses that sibling PDF; only if absent does it
walk upward looking for `plans/k1-drafts/week-91/k-1.pdf`. There are no absolute
paths or imports from the repository. The student SHA-256 deliberately binds
the key to the seven final rendered pages inspected for this writer stage.
Changing that PDF requires a fresh mathematical and visual review, not merely
changing the digest.

`check_guide.py` independently models a graph with alternating two-way rotors,
exhausts both switch starts and all eight tree starts, enumerates coin words,
checks every displayed answer against the compiled guide text, and verifies
student problem/page mapping. General claims are explained in the guide;
finite regression checks are not a substitute for those arguments.

Writer-stage only: no guide critic or reviser has run. Unpiloted and physically
unrehearsed. No student file is edited by the build or checker.
