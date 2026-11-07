# Week 53 return visit facilitator guide source

Writer-stage adult guide only. The student packets are unchanged.

## Rebuild

Requirements: Python 3 (standard library only), pdfLaTeX with Latin Modern,
geometry, amsmath, amssymb, array, booktabs, fancyhdr and TikZ; Poppler
`pdftotext` for input/version and final-page checks.

Place `k-1.pdf`, `grades-2-3.pdf` and `grades-4-5.pdf` in the directory above
this `src/` folder, then run:

```sh
cd src
sh build.sh
```

The build compiles twice, rejects errors/overfull boxes, writes
`../facilitator.pdf`, removes its temporary directory, then runs
`check_guide.py`. No downloaded reference or student builder is needed.
The checker first looks beside this source folder, then derives a repository
fallback `plans/return-visit-drafts/week-53` by walking ancestors; it contains
no machine-specific paths. This also supports later renaming `src/` to
`guide-src/` within the student draft folder.

## What the checker establishes

Final student PDFs are pinned by SHA-256 to the 7/6/10-page inputs personally
rendered and read by the writer. Their problem-to-page maps are checked by
text extraction. Independent graph data are transcribed here rather than
imported from the student code. Exhaustive link subsets and simple routes
recompute all finite answer sets, optional-place cases, price transformations,
threshold groups, complete route lists, and the one-change cost barrier.
Inverse-price formulas are compared with brute force for all 512 positive
triples from 1 through 8. Printed-map all-pair minimax and converse claims are
checked on every spanning tree; the guide's arguments, not finite tests, prove
the general statements. Eight final guide pages and recurring header/footer
are checked as well.

A passing script is not visual QA or physical rehearsal. The writer rendered
and inspected every final guide page. Timing, tape clearance, pawn handling,
price-invention conventions and age fit remain unpiloted and physically
unrehearsed. The next stage is an independent Claude critic, not revision here.
