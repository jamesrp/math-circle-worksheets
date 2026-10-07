# Week 75 adult guide source

This independently authored companion matches the final four-page GGT75-S-v1 student prototype. It contains no student source, downloaded reference, cache, or machine-specific dependency.

Requires Python 3 and pdflatex with the standard LaTeX packages listed in facilitator.tex (including Latin Modern, amsmath, amssymb, fancyhdr and hyperref).

Run `python3 check_math.py` from any working directory with the path to the script, or run `python3 build.py --out PATH`. The builder runs the checker and writes PATH/facilitator.pdf. Without --out, it writes beside guide-src. All checking code uses only the Python standard library and imports no student or prior review checker.

The source includes human proofs; finite checking supports the printed instances and does not replace those proofs. Final output was rendered and visually inspected. Physical setup and classroom use are unpiloted and unrehearsed.
