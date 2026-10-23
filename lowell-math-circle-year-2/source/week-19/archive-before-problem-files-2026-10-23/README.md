# Archived base source: before the problem-file conversion, October 23, 2026

`build_packets.py` is the old student builder. It wrote the three band LaTeX files and the answer checks. The student pages are now stored as problem files one directory above (`week.toml`, `figures.py`, `problems/`); `editable/src/regenerate.py` writes the same LaTeX from them, byte for byte, and `editable/src/answer_checks.py` holds the old builder's checks unchanged.

`subset-antichains-week19-editable-source.zip` is the complete portable package it replaced: the October 4 fresh-review release. None of these files is current. Bonus companions are separate.

SHA-256 of the ZIP: `f050e109b9cfbc8e08afd22ce74546c2d2908d333f5d62bb6d908de0dfbf7469`.
