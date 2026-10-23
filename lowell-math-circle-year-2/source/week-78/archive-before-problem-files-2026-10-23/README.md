# Week 78 source before the problem-file conversion

On October 23, 2026 the Week 78 student packet, organizer-approved and promoted on October 17, was converted to problem files (`../week.toml`, `../template.tex`, `../figures.py`, `../problems/`), with no change to any wording or figure.

- `students.tex`: the hand-written student LaTeX the problem files replaced. Its preamble is `../template.tex`; its pages are in `../problems/*.md`.
- `build.py`: the old student builder, which wrote the boards' TikZ into `cases.tex`; `../figures.py` now draws them with the same `boards()` code.
- `week-78-source.zip`: the source package that contained them, current from the October 17 promotion. Its PDFs are still the current print copies.

SHA-256 of the ZIP: `d094917849b83035d526437a2fc24fc98e3f73c28f5a1bcc31aa6c22e5e47fd1`.
