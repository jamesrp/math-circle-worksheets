# Week 44 source before the problem-file conversion

On October 23, 2026 the Week 44 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the generated LaTeX is byte-identical to this builder's.

- `write.py`: the student builder the problem files replaced. Its page-drawing helpers and the `Book` drawing methods from `common.py` are carried over in `../figures.py`, and its wording in `../problems/*.md`. `common.py` stays in `../editable/src/`, where its `build()` still compiles the three packets.
- `copying-bag-week44-editable-source.zip`: the complete October 4 fresh-review source package that contained it. Its PDFs are the same as the current ones.

SHA-256 of the ZIP: `9a779beecb2d418ad9f820a3db89714a90c07a9e25828c30a4ad84143b3bb96b`.
