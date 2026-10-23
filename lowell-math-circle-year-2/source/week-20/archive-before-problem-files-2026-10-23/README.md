# Archived base source: before the problem-file conversion, October 23, 2026

`build_packets.py` is the old student builder. It wrote the three band LaTeX files and solved every board with fixed values (with sympy) into `checked-values.txt`. The student pages are now stored as problem files one directory above (`week.toml`, `figures.py`, `problems/`); `editable/src/regenerate.py` writes the same LaTeX from them, line for line, and `editable/src/answer_checks.py` solves the same boards with exact fractions, giving the same `checked-values.txt`.

`averaging-maximum-principle-week20-editable-source.zip` is the complete portable package it replaced: the October 4 fresh-review release. None of these files is current. Bonus companions are separate.

SHA-256 of the ZIP: `13f08628acc77b1df004442a1c5a0d5f851df8cf1117018503f147e2840b4687`.
