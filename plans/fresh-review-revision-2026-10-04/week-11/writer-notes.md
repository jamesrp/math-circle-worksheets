# Week 11 writer stage: chronological firing records

Scope: targeted recording revision only, in the copied `week-11` package. This is a draft for independent review, not a release. All three student packets remain six pages, with Problems 1–6 consecutive.

## Changed files

- `week-11/src/build_packets.py`: student-only generator, updated to `F11-K-v3`, `F11-23-v3`, and `F11-45-v3`.
- `week-11/src/k-1.tex`, `week-11/src/grades-2-3.tex`, `week-11/src/grades-4-5.tex`: regenerated consistently from that generator.
- Student PDFs in `week-11/build/`, copied to `student-stages/week-11/draft/k-1.pdf`, `grades-2-3.pdf`, and `grades-4-5.pdf`.

## Recording decisions

- Shared rules define the chronological sharing word and recording the final piles after stopping.
- A small non-task recording convention on page 1 of each packet shows the spoken action order “A, then B, then A” becoming `A → AB → ABA`. It is a notation example, with no supplied starting piles or solution to a numbered task. The older packets also show counting the two A letters and one B letter after stopping.
- K–1 Problems 1, 3, 5 have one sharing-word field plus final-pile fields. Their original final-state questions are unchanged. No sharing-count tallies were introduced.
- Grades 2–3 Problems 1, 2, 4 and Grades 4–5 Problems 1, 4 replace all per-circle concurrent tally columns with one wide chronological word field. Their prompts explicitly defer counting letters until after stopping.
- Tasks needing only final-state collections or successive stable states retain their original recording format; this revision does not add separate firing counts to them.
- The 44 mm working circles, 60 mm square sinks, every board coordinate, and every edge are exactly unchanged on every student page.

## Preserved mathematical tasks

- K–1: all six original problem descriptions are byte-for-byte unchanged, including all four paired starts, all four square starts, all six staged-addition rows, the complete stable-state collection, and eleven repeated-addition rows.
- Grades 2–3: all original starts and repeated trials remain. Problems 3, 5, 6 are verbatim: all six-chip starting configurations leading to `(1,1)`, staged addition, and the two twelve-addition reachable-state collections. Problems 1, 2, 4 retain their comparisons of final states and firing counts.
- Grades 4–5: all original investigations and cases remain. Problems 2, 3, 5, 6 are verbatim: two staged-addition examples in all three timings, all four starting states under repeated addition, the three twelve-chip termination experiments and general explanation, and the eight-chip order-independence explanation. Problems 1 and 4 retain every start, repeated trial, and question about firing counts and the diagonal edge.

## Checks performed

- Read the current generator, TeX, and all current student PDF text; inspected all 18 current rendered pages.
- Regenerated student sources and ran their numerical checks: 20 randomized legal orders per authored start, exhaustive legal-choice comparison on all assigned starts, repeated-addition cycles, and staged-addition identity checks all pass.
- Original and revised `checks.json` are byte-for-byte identical. Thus no numerical reference result changed.
- Independently replayed 31 chronological sharing words, checked legality at each move, final piles and sink totals, and derived each sharing count from the completed word. Results: `week-11/writer-qa/recording-checks.json`.
- Programmatically compared every generated board node and edge against the copied baseline; positions and material dimensions are identical on all 18 pages.
- Built each student PDF directly with two `pdflatex` passes. No top-level builder or adult generator was run. No LaTeX overfull/underfull warnings appeared.
- Rendered and visually inspected all 18 final pages in `week-11/writer-qa/draft/`, including individual first-page checks. Headers, footers, word examples, tables, writing space and boards are clear, with no overlaps or clipping.
- Re-running the student generator produces identical hashes for the generated TeX.

Baseline copied student sources are preserved under `week-11/writer-qa/baseline-src/` for reviewer comparison. No facilitator sources, adult guides, AGENTS, indexes, released files, reference PDFs, source ZIPs, or bonus files were edited. The parent release path owns packaging and final extracted-ZIP checks. Physical material rehearsal and classroom piloting remain unperformed.
