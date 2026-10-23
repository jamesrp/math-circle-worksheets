# Week 69 source before the problem-file conversion

On October 23, 2026 the Week 69 student packet was converted to problem files (`../week.toml`, `../template.tex`, `../problems/`), with no change to any wording or figure: the generated LaTeX differs from the old source only by blank lines between sections. Rebuilt here, the old source and the problem files give pixel-identical packets; both differ from the print PDF made on October 16 by at most 123 pixels a page at 100 dpi with identical text, which is the difference between TeX installations, not between sources.

- `students.tex`: the hand-written student source the problem files replaced. Its preamble is carried over in `../template.tex` and its wording and figures in `../problems/*.md`.
- `week-69-source.zip`: the complete source package that contained it.
