# Week 58 return visit adult guide source

This package builds `../facilitator.pdf`. It does not build or edit student pages.

## Build

Requires Python 3, Poppler `pdftotext`, and a working pdfLaTeX installation with
`geometry`, `fontenc`, `lmodern`, `amsmath`, `amssymb`, `array`, `booktabs`,
`fancyhdr`, `tikz` and `hyperref`.

From this folder run:

```sh
sh build.sh
```

The build first regenerates the mathematically checked tables, compiles twice
in an isolated temporary directory, rejects overfull boxes, copies the PDF to
the parent folder, removes TeX intermediates, and finishes by running the checker.

`check_guide.py` looks first for `k-1.pdf`, `grades-2-3.pdf` and `grades-4-5.pdf`
in the folder above this source folder. If absent, it searches ancestor folders
for `plans/return-visit-drafts/week-58/`. There are no machine-specific paths.
The exact final student PDFs are bound by SHA-256 and their problem/page map is
verified with `pdftotext`; changing the pages requires renewed visual review
and rederivation, not just replacing a hash.

For a portable rebuild, copy this entire folder and the three student PDFs into
a fresh directory outside the repository, with the PDFs beside the source folder,
then run its `build.sh`. No other repository files are required.

## Files

- `facilitator.tex`: adult prose, proofs and non-task convention visual.
- `checked-tables.tex`: generated train and marking-game keys, retained for review.
- `check_guide.py`: independent exact finite checks and table generator.
- `build.sh`: portable compile and validation entrypoint.

All claims of classroom usability and physical fit remain untested. The guide
is a writer-stage draft awaiting the separate critic and reviser stages.
