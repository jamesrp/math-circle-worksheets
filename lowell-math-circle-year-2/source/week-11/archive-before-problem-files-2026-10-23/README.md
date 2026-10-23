# Week 11 source before the problem-file conversion

On October 23, 2026 the Week 11 student packets were converted to problem files (`../week.toml`, `../figures.py`, `../problems/`), with no change to any wording or figure: the rebuilt LaTeX is byte-identical to this builder's, and the print PDFs match in pages and extracted text. Grades 2–3 and 4–5 match in 100-dpi pixels; K–1 page 6 differs by 100 pixels of glyph antialiasing, and this builder's own LaTeX compiled in the same TeX installation differs from the print copy in exactly the same way.

- `build_packets.py`: the student builder the problem files replaced. Its drawing code is carried over in `../figures.py`, its wording in `../problems/*.md`, and its numerical and order checks in `../editable/src/student_checks.py`.
- `chip-firing-week11-editable-source.zip`: the complete source package that contained it (the October 4 fresh-review release). Its PDFs are the same as the conversion's. SHA-256: `b0c85f41c37a6d4caa0b4382dc9432d293c52c0195c46b2843f7fed346a6dbb7`.
