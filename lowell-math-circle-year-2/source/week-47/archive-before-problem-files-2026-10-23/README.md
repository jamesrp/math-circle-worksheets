# Week 47 source before the problem-file conversion

On October 23, 2026 the Week 47 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical to this builder's, and the PDFs built from it are pixel-identical to this builder's PDFs compiled on the same machine.

- `make.py`, `draw.py` and `examples.py`: the student builder the problem files replaced. Their drawing code is carried over in `../figures.py`, their wording in `../problems/*.md` and make.py's closing asserts in `../editable/src/check.py`.
- `gentle-step-landscapes-week47-editable-source.zip`: the complete portable package that contained them, the October 4 fresh-review release. Its PDFs are the current ones at the time of the conversion.

On the October 23 machine this package's own `build.py` reproduces its LaTeX but not its reference pixels exactly (pdftoppm at 100 dpi: 0, 48 and 21 differing pixels at most on any page of the K–1, 2–3 and 4–5 packets; text identical), so the conversion was proved against this builder compiled there rather than against the print PDFs' pixels alone.

SHA-256 of the ZIP: `ff54499c19ba6dc0751d68a5d9e586c165c32a3110662c80d690c973422eae63`.
