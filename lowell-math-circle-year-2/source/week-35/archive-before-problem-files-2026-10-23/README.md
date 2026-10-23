# Archived base source: before the problem-file conversion, October 23, 2026

`build_packets.py` is the old student builder. It wrote the three band LaTeX files and, at its end, checked the footprint motif and wrote `src/mathematical-checks.json`. The student pages are now stored as problem files one directory above (`week.toml`, `figures.py`, `problems/`); `editable/src/regenerate.py` writes the LaTeX from them, and the motif check moved unchanged into `editable/src/check_motif.py`.

`glide-borders-week35-editable-source.zip` is the complete portable package it replaced: the October 4 fresh-review release with the October 3 introduction follow-up and the October 23 table kit. None of these files is current. Bonus companions are separate.

SHA-256 of the ZIP: `5aca08daa208b13a5ed675ba24adeef4aad9c9420797d54b0880e148c457f40c`.
