# Remaining eighty: author and reviewer contract

The user accepted the random-ten worksheet trial and requested the same treatment for the remaining eighty atlas families. The original ten and original atlas cards stay unchanged. Scope and batch assignments are in `scope.json`; each batch has eight original cards in `<batch>-originals.json`.

Read the root README, `plans/atlas/worksheet-trial/DESIGN-BRIEF.md`, the trial assessment, and relevant teaching notes in `plans/lesson-format-source-notes.md`. Use the revised Week 1 and random-ten sheets as the quality benchmark. A new family should produce a genuine investigation, not its atlas card placed in boxes.

## Design requirements

- Start with an exact, usable instance and a meaningful learner choice. Supply the board, diagram, data or construction the learner needs. For advanced topics a calculus or algebra choice is an appropriate concrete starting point.
- Develop toward an obstruction, optimal construction, complete classification, invariant, surprising representation or precise counterexample. Experiment first; useful proof or explanation after. Do not reveal the solution through titles, prefilled diagrams or conveniently truncated tables.
- Aim for 2–4 student pages per family, with room to work and staged handout. More is permitted when necessary. Page count is not an acceptance criterion. Do not force every page into one hour. No compulsory busywork table or arithmetic padding.
- Keep the actual prerequisite gate. In particular **GA-08 requires calculus** for the satisfying investigation. Distinguish an accessible warm-up from the real core. State reading, arithmetic and reasoning demands in the guide; mark advanced continuations on student pages.
- Every printed task must have a full checked answer, including all examples, impossible cases, general proof scope and extensions. Computation can verify finite instances; it cannot replace a needed general argument. State supplied theorems honestly. Keep scientific model assumptions explicit.
- Consult relevant source content for specialized claims. The original cards include inspected sources/locators; do not blindly copy them as evidence for new claims. Use official/primary sources if additional verification is needed. Record exact adaptation and scope.
- Keep prep realistic: reusable counters, rulers, string, graph paper, printouts. Provide diagrams rather than requiring an adult to invent them. Track prior-use overlaps against Weeks 1–10 and the first ten trials.
- Assess each family candidly: first-pilot candidate, promising with specific gates, or advanced/specialist. No classroom-test claims.

## Files owned by each author

For batch `ad1` (substitute your assigned batch):

- `plans/atlas/worksheet-expansion/ad1-data.json`: exactly the eight assigned families, structured below.
- `plans/atlas/worksheet-expansion/ad1-design.md`: brief design arc, substantive changes from atlas, source/prerequisite decisions and candid assessment for each family.
- `plans/atlas/worksheet-expansion/ad1-checks.py` and `ad1-checks-results.json`: meaningful exact finite calculations and identity/proof checks as appropriate. Code uses standard library where practical. Store all mathematical data here, not in builder paths.
- Later, after independent design review: `lowell-math-circle-year-2/source/atlas-remaining/ad1.py`: custom student renderer. Shared helpers and assembly are editor-owned. Do not edit other authors' files or shared files.
- Preview PDFs and PNGs only under `tmp/pdfs/atlas-remaining/ad1-preview/` (use a fresh suffixed folder after repairs). Final six PDFs are editor-owned.

**The editor has already run the PDF artifact-operation marker once for all six final outputs. Do not run it again.**

## Required data schema

Use a JSON object with `batch`, `status`, and `families` (list of eight). Each family has:

```
id, title, core_gate, extension_gate, reading, materials,
prep_minutes, timing, launch, satisfying_stop, prior_use,
assessment, mathematical_connection,
sources: [{title, url, locator, adaptation, checked}],
pages: [{title, gate, intro, prompts: [{id, text, solution, hints: [str]}]}],
extensions: [{prompt, solution, gate}],
figures: {... optional exact diagram data ...}
```

All prose fields above are strings except `prep_minutes` (number), lists and figures. Use prompt IDs `1`, `2`, ... within the family or `A1`, etc; family plus prompt is the key. Keep optional student questions in `pages` with an explicit gate. Guide-only extensions go in `extensions`, not as missing student tasks. Sources must contain checked locators and an honest evidence description, not merely URLs. Figures can have any appropriate structured form. Do not include answers inside student intros or diagram data rendered as a starting scaffold.

## Production API (after design review)

`from sheet import Book, DATA, ...` gives the same top-left-coordinate Letter drawing helpers as the random-ten trial. Body area x=44..568, y up to746; footer starts755. Use body type about11.5–12pt, not small print to force a fit. `book.c` is a normal ReportLab bottom-left canvas; convert `792-y` for direct graphics.

Your module exports `render_students(book, family_id)`. Load your data from `DATA/'ad1-data.json'`. The editor will provide `from common import start, question, blank, lines, family_data` for staged pages and tracked prompt IDs. Custom diagrams and layouts should be written specifically for the mathematics. Use the helpers for each prompt so assembly can verify actual printed-task coverage. A guide renderer is provided centrally from your complete data; optionally export `render_key_figures(book, family_id)` for worked diagrams that materially clarify a solution.

The author must inspect every student page at full size and all guide pages at least on contact sheets, with dense/diagram pages at full size. Independent reviewers then check the other batch's mathematics and PDFs. Send findings promptly, fix them in your own files, re-render changed pages under fresh paths, and record closure.

## Stage handoff

First complete design, data and mathematical checks. Report exactly what exists, the satisfying payoff and hard gate for each family, and any concerns. Stop before PDF rendering until the editor assigns cross-review and production. The editor is maintaining an eighty-family completion ledger; do not substitute a partial batch or silently drop a hard topic.
