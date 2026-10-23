# Week 42 source before the problem-file conversion

On October 23, 2026 the Week 42 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the generated LaTeX is byte-identical to this builder's.

- `write.py`: the student builder the problem files replaced. Its page-drawing helpers and the `Book` drawing methods from `common.py` are carried over in `../figures.py`, and its wording in `../problems/*.md`. `common.py` stays in `../editable/src/`, where its `build()` still compiles the three packets.
- `fair-results-lopsided-bag-week42-editable-source.zip`: the complete October 4 fresh-review source package that contained it. Its PDFs are the same as the current ones.

SHA-256 of the ZIP: `b78a317b66cc0ed46b6e1b4f11a45c011bdf0d440c1f6756f876595b525411dc`.
