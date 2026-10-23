# Archived base source: before the problem-file conversion, October 23, 2026

`build_packets.py` is the old student builder. It wrote the three band LaTeX files and checked every board (`geometry-checks.json`). The student pages are now stored as problem files one directory above (`week.toml`, `figures.py`, `problems/`); `editable/src/regenerate.py` writes the same LaTeX from them, line for line, and runs the same checks, giving the same `geometry-checks.json`.

`shortest-reflected-paths-week21-editable-source.zip` is the complete portable package it replaced: the October 4 fresh-review release. None of these files is current. Bonus companions are separate.

SHA-256 of the ZIP: `f7a4200c06e92f5a876177f9f3e319efc38fa2d0f625772b7259605b174d0f48`.
