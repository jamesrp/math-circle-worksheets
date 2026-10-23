# Archived base source: before the problem-file conversion, October 23, 2026

`build_packets.py` is the old student builder, with `examples.py`, the page 1 practice row it imported. It wrote the three band LaTeX files and the finite checks. The student pages are now stored as problem files one directory above (`week.toml`, `figures.py`, `problems/`); `figures.py` carries its drawing code and page template, `editable/src/regenerate.py` writes the LaTeX from the problem files, and `editable/src/check_math.py` keeps its finite checks unchanged.

`error-correcting-codebooks-week18-editable-source.zip` is the complete portable package it replaced: the October 4 fresh-review release. Neither file is current. The bonus companion is separate.

SHA-256 of the ZIP: `95ed006935a1480b138bd87d128474533ffec0c207191388fc6561877e886f83`.
