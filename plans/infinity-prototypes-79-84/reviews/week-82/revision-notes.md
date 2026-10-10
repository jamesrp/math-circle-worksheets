# Week 82 revision stage

Read the writer instructions, selected-band scope override, adversarial review and independent mathematical review. Copied the writer sources into `final/src/` and changed only the student packet and its source README. No facilitator source, repository index, artifact marker, commit or remote was changed.

## Changes

- The shared definition now says that **any two customers** and their partners must appear in the same order. This fixes the universal-pair ambiguity identified by the mathematical reviewer.
- Problem 4 explicitly places the large reusable cutouts **on the table** and asks for **sketches** in the four compact boxes. The boxes are recording spaces, not fitted placement mats; the 16.3 cm by 2.65 cm continuing strips are no longer implicitly required to fit 16.1 cm by 2.0 cm boxes.
- Lowered the page-3 boundary sentence slightly to leave a visible gap below the red continuation label. Its meaning, and the two-block/pairs investigation, are unchanged.
- Preserved Grades 3–5 scope, the finite matching launch, the full-customer matching demand, explicit after-EVERY-customer conventions, and four consecutive problems. No discovery answer was added to a student board.

## Checks and evidence

`final/students.pdf` is seven pages: four task pages and three reusable-material pages. Both clean source builds pass the portable builder's overfull-layout rejection and produce byte-identical PDFs. SHA-256: `cf539148c46473b82ff29c113d05a03e2e04b2642bf9359f0e3a8fdf288d8719`.

Reran `independent-math-check.py`: all six finite bijections are checked exhaustively, only one keeps order, explicit inverse formulas are replayed through 10000, and the permitted finite row/star catalog has the expected six order types. These computations supplement the general inverse and obstruction arguments in `review-math.md`; finite replay is not an infinite proof. The revised wording agrees with the check of every pair. No map, card label, queue order, arithmetic operation or mathematical target was changed.

`final/check_final.py` checks seven pages, headers and footers in PDF text, consecutive Problems 1–4, the revised table/sketch rule, fresh-build identity and absence of text outside the page. Every final page was rendered with PyMuPDF, reopening the document for each page, and visually inspected. Every page was also independently rendered with Ghostscript 10.07.1 at 115 dpi and inspected. Evidence lives in `final/render-revision/`: `page-N.png`, `gs-page-N.png`, `QA.json`, extracted text and the every-page header/footer contact image.

Apparent missing repeated headers in sequential full-page image displays were checked with cropped header/footer images and pixel counts. All headers and footers are present in the actual PNGs from both renderers; no PDF content defect was found. The every-page cropped comparison was inspected separately.

## Limits and adult-guide follow-through

This remains an unpiloted draft. Physical cutting, yarn handling, material fit, timing and classroom procedures are untested. Digital dimensions clarify the intended tabletop/sketch roles but do not establish a successful physical rehearsal.

The integration agent owns the separate facilitator revision: supply the six finite matches, Problem 4 sample pairs, the distinction between printed identities and permissible partners, comparison-copy conventions, and a first route that leaves the two-block investigation available for a return visit. Those adult findings were deliberately not inserted as answers on student pages.
