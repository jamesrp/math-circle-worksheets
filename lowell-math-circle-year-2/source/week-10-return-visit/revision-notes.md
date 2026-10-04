# Week 10 return-visit revision notes

The fresh REVISE stage is complete. The shared seven-page student companion is `return-visit.pdf`, identified on every footer as **F10-RV-v1**. The explicit shared-packet scope in `PROMPT.md` overrides the generic three-band filenames in the workflow harness. It contains exactly three numbered investigations, continued where needed.

Both `review.md` and `review-math.md` found no essential student-page correction. The student content, town edges, layout boxes, arrows, resets, band headers, convention examples, and problem/continuation wording are preserved. The final PDF differs from the approved draft only in its footer identifier. All seven pages have identical vector drawings to the draft; extracted page text is identical after that identifier substitution.

## Source changes

- Copied `draft/src/` to `final/src/`.
- Changed `F10-RV-draft` to `F10-RV-v1` in authoritative `src/generate.py`, then regenerated `src/return-visit.tex`. A rebuild therefore retains the final footer.
- Updated the optional `src/check_pdf.py` footer expectation to `F10-RV-v1`.
- Updated `src/README.md` to describe the revised review packet and both approved arrow conventions.
- Kept `src/towns.json`, `src/check_math.py`, and `src/build.sh` unchanged. The town data also matches the independent math review's bundled data exactly.

No facilitator, base packet, canonical source, combined packet, or global index was edited. The critic's adult-only history, layout-dimension, and conversion-example handoffs remain the coordinator's separate work.

## Final-page coverage

Every final page was rendered at 1.5 scale, read, and visually inspected individually. No clipping, overlap, missing arrow, incorrect start, or missing example was found.

| Pages | Actual band | Coverage and revision result |
| --- | --- | --- |
| 1 | K–5 | Problem 1; four small directed towns and the X → Y → Z action example. Already sufficient; final footer changed. |
| 2–3 | 2–5 | Problem 1 continued; four larger directed towns, including balanced disconnected Town 7. Already sufficient; final footer changed. |
| 4–5 | 2–5 | Problem 2 and continuation; four undirected starred towns with explicit reset rules. Already sufficient; final footer changed. |
| 6–7 | 4–5 | Problem 3 and continuation; linear and circular triple passwords with their non-task two-button examples. Already sufficient; final footer changed. |

## Verification

`src/build.sh` ran in two separate output directories, using `/Library/TeX/texbin/pdflatex`; each run regenerated TeX, ran the standard-library mathematical checker, and made two LaTeX passes. Both builds passed without LaTeX warnings or overfull/underfull boxes. Their page text and vector drawings agree.

The final PDF passed `src/check_pdf.py` using `tmp/example-edit-env/bin/python`. The fresh math review's independent checker was rerun against the actual final PDF and final town data. It checks all 12 rendered towns, 34 directed arrows, 0.75-inch counter footprints, stars, inch scaling, complete route searches, all binary row/circle candidates through the optimum lengths, and the convention examples. The smallest complete rendered arrow-to-counter gap is 0.0431 inch; the smallest arrow-to-island gap including strokes is 0.0619 inch. Active arrows retain position 0.86 and length 3 mm; demo arrows retain position 0.72 and length 2 mm.

The independent results retain the directed legal starts and safe first crossings from the reviews. Binary triples require at least 10 tiles in a row and 8 in a circle; the checked constructions attain those bounds. The source's mathematical report, the PDF checker, and the independent checker all pass.

`return-visit-source.zip` contains the seven files in `src/`. It was freshly extracted to `extracted-source/`, rebuilt without repository-relative imports, and checked again with both PDF and independent mathematics/vector checks. All seven rebuilt page texts, vector drawings, and 1.5-scale rendered images exactly match the delivered PDF. Generated TeX and all extracted source files match `final/src/`; the ZIP matches those files. PDF byte hashes differ between builds because of metadata, while content and renders agree.

Supporting evidence is in `validation.json`, `build/math-check.json`, `render/pdf-check.json`, and `verification/independent-check.json`, with the clean-package evidence under `extracted-source/`. All artifacts remain within this run.

Physical tabletop rehearsal and classroom piloting remain **untested**. This is a reviewable, digitally verified companion; actual-size material-fit rehearsal is still required before classroom use.
