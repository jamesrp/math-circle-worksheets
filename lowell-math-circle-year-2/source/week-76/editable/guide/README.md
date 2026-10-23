# Week 76 substitution strips adult guide

Companion to the final four-page Grades 3–5 student packet F76-35-v1. This guide is F76-FAC-v1. It opens with exact theorems and limits, gives practical preparation for a three-child target table (and an optional four-child table), all seven solutions, complete enumeration answers, graduated hints, and an eventual-nonperiodicity proof.

## Rebuild

Use Python 3 (standard library only) and a normal TeX Live or MacTeX installation with pdfLaTeX, Latin Modern, geometry, fontenc, amsmath, amssymb, array, tabularx, fancyhdr, enumitem and url.

    python3 build.py --out /path/to/output

The builder runs `check_math.py` first and emits `facilitator.pdf`. It fails on TeX errors and overfull boxes. No downloaded papers, external fonts, generated TeX formats or binaries are bundled. In an intentionally minimal TeX environment, initialize pdfLaTeX's format and package database outside this source package, or pass the environment's documented TEXMF/TEXFORMATS values. Normal installations need no such workaround.

The independent checker transcribes all final student examples, generates the 16-tile answer, enumerates every permitted cropped pairing, checks whole-row histories, and builds the exact factor language through length 10 by a substitution-closure argument. Finite checks are not offered as a proof of the infinite theorem; that proof is written in the guide.

After rebuilding, render all four pages with `pdftoppm -r 120 -png facilitator.pdf guide` and inspect each one. Physical material rehearsal, feasibility judgments and classroom learning outcomes remain untested.

## Source lineage

Classical Thue–Morse substitution facts: Richard G. Swan, *The Morse Sequence*, Lemma 2.2, https://www.math.uchicago.edu/~swan/expo/Morse.pdf; Carl D. Offner, *Repetitions of Words and the Thue-Morse sequence*, §3, https://www.cs.umb.edu/~offner/files/thue.pdf; Jean-Paul Allouche and Jeffrey Shallit, *The ubiquitous Prouhet-Thue-Morse sequence*, §§2–4, https://cs.uwaterloo.ca/~shallit/Papers/ubiq15.pdf. Concrete packet examples and the adult presentation are independently arranged. This package contains original guide source, not copies of those references.
