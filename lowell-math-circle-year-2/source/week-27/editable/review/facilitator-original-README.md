# Week 27 stable pairings: portable facilitator source

Draft, unpiloted, unscheduled library slot. This folder builds the adult guide only; no student source or PDF is changed.

## Rebuild

Python 3 with `reportlab` is required. Fonts and their redistribution license are bundled in `fonts/`, so no system-font path is needed. The independent mathematical checker uses only Python's standard library.

Run from any directory:

```sh
python3 check_math.py
python3 build_guide.py
```

The guide is written to `../facilitator-guide.pdf` relative to this folder. The checker writes `math-checks.json` locally. It does not import the student generator or its answer code. It explicitly transcribes the preference profiles, exhausts all candidate matchings, checks all single-strip reversals and blank Y choices, audits both specific request logs, branches over every legal free-asker schedule for the older four-pair market, and exhausts 46,656 three-pair profiles (279,936 candidate matchings) for the last-choice bound.

For structural QA, install `pypdf` and `PyMuPDF`, then run `python3 verify_pdf.py`. It checks 17 pages, exact section starts, Letter size, text bounds, font embedding, hyperlinks, and unchanged student hashes when the PDFs are present alongside the folder. Human visual review remains required after content/layout edits; update the visual-review record honestly.

For fresh rendering, with Poppler installed:

```sh
mkdir -p qa
pdftoppm -scale-to 1200 -png ../facilitator-guide.pdf qa/guide
```

The included QA PNGs are the reviewed final render. All 17 pages were inspected. An isolated portable rebuild was also compared against every page of the reference render. The PDF contains four embedded Liberation Sans fonts. Build paths are relative; no absolute workspace paths or external images are required.

## Content map

- Guide pages 1-2: genuine prerequisite gate, materials at >=20 mm, compact recording-diagram distinction, short launch, flexible hour menu.
- Pages 3-5: K-1 Problems 1-6. The single-strip experiment resets before every change. K-1 is optional and requires demonstrated understanding of BOTH preferences.
- Pages 6-9: grades 2-3 Problems 1-5, exact solutions and completeness arguments.
- Pages 10-15: grades 4-5 Problems 1-6, exact legal logs, counterexample, finite completion and stability proofs, last-choice extremum.
- Page 16: optional proposer-optimality proof, extension and use-record prompts.
- Page 17: sources and fidelity limits.

`source-manifest.json` records references, supplied-file hashes, and the exact final packet versions. `qa-report.json` and `check-output.txt` record checks. No source manuscript scan is bundled; the guide includes verified public reference links. Bibliographic and pedagogy claims are explicitly limited to what was inspected, and no claim of classroom piloting is made.
