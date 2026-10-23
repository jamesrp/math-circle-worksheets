# Week 34 source before the problem-file conversion

On October 23, 2026 the Week 34 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the generated LaTeX is byte-identical to this builder's.

- `build_packets.py`: the student builder the problem files replaced. Its drawing code and page template are carried over in `../figures.py`, its wording in `../problems/*.md`, and its finite checks, unchanged, in `../editable/src/check_distinguishing.py`.
- `symmetry-breaking-week34-editable-source.zip`: the complete October 4 fresh-review source package that contained it. Its PDFs are the same as the current ones.

SHA-256 of the ZIP: `810c6dff065626080ff85b745ddd43a6d8078d23a3d416dc641c4ba5b4bae7ca`.
