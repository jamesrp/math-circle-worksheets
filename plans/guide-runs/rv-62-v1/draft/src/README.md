# Week 62 return-visit adult guide, writer stage

Rebuild from inside this folder with `./build.sh` (or `sh build.sh`). Requires
Python 3, pdfLaTeX with geometry, fontenc, lmodern, amsmath, amssymb, array,
booktabs, fancyhdr, hyperref and tikz, plus Poppler's `pdftotext`.
The script compiles twice into a temporary folder, rejects overfull boxes,
copies `../facilitator.pdf`, cleans its LaTeX intermediates, and ends by running
`check_guide.py`. The exhaustive tree-list check can take roughly a minute.
No machine-specific environment setup is embedded in the builder.

## Portable layout

```
week-62/
  k-1.pdf
  grades-2-3.pdf
  grades-4-5.pdf
  facilitator.pdf       # output
  guide-src/            # this folder (src/ works too)
    build.sh
    facilitator.tex
    check_guide.py
    student-edition.json
    README.md
    SOURCES.md
```

The checker first finds student PDFs one directory above itself. In a repository
run it may instead locate `plans/return-visit-drafts/week-62` under an ancestor.
There is no absolute path fallback or dependency on the student's Python sources.
`student-edition.json` pins the three final PDF hashes and the final printed
problem/page map. An intentional student revision requires new visual inspection,
updated instance data, and updated hashes; a mismatch should not be ignored.

## Mathematical checks

The independently written verifier transcribes the final inspected boards, not
an earlier review answer key. It uses product enumeration for list completions,
breadth-first search for shortest move routes, replay of every guide move word,
longest-path layering plus exhaustive smaller-slot schedules for arrows, all
list assignments for the two invented-list tasks (including the eight-card tree),
all legal 3/4-color states for rings of sizes 3–8, and all orientations of both
final conflict boards. It checks the launch examples and the printed orientation
witnesses. Universal theorems are proved in the guide; the finite computations
are not offered as universal proofs.

A writer report and render/clean-copy QA are retained in the run folder, not in
this portable source package. The guide and student activities remain unpiloted
and physically unrehearsed. Student PDFs were not changed.
