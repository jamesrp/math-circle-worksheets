# Week 91 source before the problem-file conversion

On October 23, 2026 the Week 91 student packet was converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the generated LaTeX is the old generator's, byte for byte, apart from a final newline.

- `generate.py`: the generator that wrote all three student-facing packets. Its drawing helpers are carried over in `../figures.py` and its student-packet wording in `../problems/*.md`; the current `../editable/student/generate.py` still writes the return-visit packet and the materials.
- `week-91-source.zip`: the October 17 source package that contained it. Its PDFs are the same as the current ones.

SHA-256 of the ZIP: `b2c55d82eea7b0811dd735a49efafd40ca6ed7f7f99c29f2fbf2754190481f18`.
