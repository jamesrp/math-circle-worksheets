# Archived base source: before the problem-file conversion, October 23, 2026

`build_packets.py` is the old student builder and `examples.py` the K–1 and Grades 2–3 worked example it imported. They wrote the three band LaTeX files from `src/math_checks.json`. The student pages are now stored as problem files one directory above (`week.toml`, `figures.py`, `problems/`); `editable/src/regenerate.py` writes the LaTeX from them, and the builder's one check (the hold/release example) moved into `figures.py`.

`stable-matching-week27-editable-source.zip` is the complete portable package it replaced: the October 4 fresh-review release with the October 23 table kit. None of these files is current. Bonus companions are separate.

SHA-256 of the ZIP: `f019e81c3009ec6d288c59c4fe6c5629a15d7f3294334ab1dddccfd463ac2db6`.
