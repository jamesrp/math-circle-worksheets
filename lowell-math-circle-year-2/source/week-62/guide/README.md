# Week 62 independently authored adult guide

The guide is for the actual final nine-page `students.pdf`: Problems 1–3 are headed Grades 2–5, and Problems 4–9 Grades 4–5. It does not change the student packet. Current staffing is eleven children at KK11 / 3333 / 445 fixed tables, with three anchored adults. The younger entry is optional and shallow, with a familiar accepted activity available when children do not retain endpoint conflicts.

The ten-page guide opens with the actual scheduling/coloring facts and their assumptions, then preparation, a common concrete launch, routes, all solutions, hints, optional extensions, and exact source references. No completion requirement is tied to one hour. Physical handling, kit preparation time and classroom piloting remain untested. A fresh reviewer must inspect the guide before release.

## Standalone build

```sh
python3 /absolute/path/to/guide/build.py --out /absolute/path/to/build-directory
```

The output directory must differ from the source directory. `build.py` copies the editable `facilitator.tex` there, runs the independent mathematical verifier, and compiles twice. The output is `facilitator.pdf`; all TeX intermediates and the finite-check report stay in the requested output directory. No student builder, repository-absolute path, third-party asset, or system font is required.

Build dependencies: Python 3 standard library, `pdflatex`, and standard TeX Live packages `geometry`, `fontenc`, `helvet`, `amsmath`, `amssymb`, `array`, `booktabs`, `tabularx`, `tikz` with `arrows.meta`, `fancyhdr`, `enumitem`, and `hyperref`. Helvetica/Nimbus Sans and standard TeX math fonts are embedded; no custom-font files are supplied.

## Independent mathematical checks

```sh
python3 /absolute/path/to/guide/verify.py --report /absolute/path/to/checks/math.json
```

`verify.py` independently transcribes 18 graphs from the visually inspected final student PDF. It reads no student/research answer data. Exhaustive assignment enumeration checks all listed minimum schedules, clique sizes, odd-cycle certificates, all minimal added-edge sets, and the named counts. It checks both legal intermediate path repairs, all 24 path orders and all 40,320 eight-vertex tree orders, and the worked launch states. Universal facts are justified by the written proofs and primary citations, not by finite computation. Source comments or earlier reviews are not answer evidence.

## Render and clean rebuild check

```sh
python3 /absolute/path/to/guide/qa.py /absolute/path/to/build/facilitator.pdf --out /absolute/path/to/qa
python3 /absolute/path/to/guide/qa.py /absolute/path/to/build/facilitator.pdf --out /absolute/path/to/qa --compare /absolute/path/to/clean-build/facilitator.pdf
```

QA requires PyMuPDF (`pymupdf`) in addition to the build dependencies. It checks ten US Letter pages, headers/footers, extracted text and span bounds; renders every page at 1.5x; and, with `--compare`, requires equal text, dimensions and rendered pixels for every clean-rebuilt page. Look at every generated PNG: numerical bounds do not detect every overlap. To test portability, copy only this source folder into a fresh directory and run its build command into a separate empty output directory. The repository QA interpreter is `tmp/bonus-35-51-venv/bin/python`; its absolute location is not required for portability.

## Provenance and package scope

Guide prose, launch drawing, solutions and check/build scripts are independently authored. Mathematical references: Lehman–Leighton–Meyer, *Mathematics for Computer Science* (2018), §§12.6.1–12.6.2, pp. 514–517, Theorem 12.6.3; Frieze D18, Theorem 1, pp. 8–10; MIT 18.310 Lecture 14, §1 following the clique definition; Pak/Redlich 18.315 Lecture 9, p. 1. Guide page 10 gives direct primary links and exact local teaching references.

Local pedagogy actually inspected: *Math Circle by the Bay*, Preface viii–x; Rozhkovskaya, Lessons 7–8, “At the lesson,” items 1 and 2 respectively; the organizer's 2025–26 Handouts 6 and 7. The guide distinguishes their reported lessons from our partner-checking and pacing inferences. Primary source downloads, broader research notes and prior-packet comparisons remain outside this folder.

Include only these original editable sources, scripts and README in a portable source bundle. Do not include prompts, exemplar blocks, books, downloaded reference PDFs, rendered previews or build intermediates. No remote upload, publication, or claim that existing remote copies are current is made.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
