# Archived base source: before the problem-file conversion, October 23, 2026

`build_packets.py` is the old student builder and `examples.py` the K–1 worked example it imported. It wrote the three band LaTeX files and checked every printed set of counts by exhaustion. The student pages are now stored as problem files one directory above (`week.toml`, `figures.py`, `problems/`); `editable/src/regenerate.py` writes the LaTeX from them and `editable/src/check_answers.py` carries over the checks unchanged.

`discrete-tomography-week25-editable-source.zip` is the complete portable package it replaced: the October 4 fresh-review release with the October 23 guide corrections. None of these files is current. Bonus companions are separate.

SHA-256 of the ZIP: `7eb8f6f49915d845a53fe34d280f96d13320fdde64281f411dc81cc318d7860c`.
