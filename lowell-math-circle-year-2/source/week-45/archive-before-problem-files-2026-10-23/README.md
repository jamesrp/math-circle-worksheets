# Week 45 source before the problem-file conversion

On October 23, 2026 the Week 45 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical, and the rebuilt PDFs match the old LaTeX compiled in the same TeX installation in pages, extracted text and 100-dpi pixels. Against the print PDFs, page 1 of each band differs only by the line break of "identically", the hyphenation reflow already recorded in `../editable/review/rebuild-pixel-allowances.json`.

- `write.py`: the student builder the problem files replaced. Its drawing code is carried over in `../figures.py` and its wording in `../problems/*.md`.
- `visible-hidden-sides-week45-editable-source.zip`: the complete October 4 fresh-review source package that contained it. Its PDFs are the same as the current ones.
