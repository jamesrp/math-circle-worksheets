# Week 87 K–1 adult guide — reviser stage

Build from this folder with `./build.sh`. Requires pdfLaTeX with the standard
`geometry`, `lmodern`, `amsmath`, `amssymb`, `array`, `booktabs`, `fancyhdr` and
`tikz` packages, Python 3, and Poppler (`pdftotext`, `pdfinfo`). Output is
`../k1-guide.pdf`. Temporary LaTeX files are removed; the script ends with the
independent checker. No machine-specific TeX setup belongs in this portable
folder.

For an extracted/repackaged copy, place the final student `k-1.pdf` beside this
folder. The checker looks there first. In a repository worktree it can discover
`plans/k1-drafts/week-87/k-1.pdf` by walking ancestor directories. The PDF hash
intentionally locks the exact six-page student draft visually inspected here.
If student pages change, re-read/render them and re-derive the guide before
updating the checker's version binding.

`check_guide.py` reads the final student PDF's card rankings, target letters,
problem/page map and prescribed agendas; independently recomputes ballots,
knockouts and every single-card swap; exhaustively checks all 216 ordered
three-voter profiles, including every build for Problems 6–8. It additionally checks the cycle-or-fixed-winner dichotomy on all 216 profiles and the upward-moving winner and passed rival for all nine single swaps. It checks the guide's page count, references and construction strings. Manual visual review
is still required after layout changes.

This is the revised, branch-only guide (five pages, W87-K-FAC-v2). All three should-fix findings and eleven useful minors are addressed. The named repository fallback in minor 12 was already implemented and has been verified by running without a student PDF beside src/. Original writer/critic evidence is preserved outside this final folder. Packaging remains deferred.
Unpiloted and physically unrehearsed. The base replacement target is
`week-87-facilitator.pdf` W87-F-v2, page 1, “K–1 route (adult-led)”.
