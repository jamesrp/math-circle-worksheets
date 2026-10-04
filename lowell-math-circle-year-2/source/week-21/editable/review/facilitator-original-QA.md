# Week 21 adult guide verification

Date: 3 October 2026. Status: draft and unpiloted, ready for organizer review.

## Coverage

- Read repository AGENTS.md and relevant README background, Week 21 PROMPT.md, independent review, final student builder, and text extracted from all three final PDFs.
- Visually inspected every final student page in three seven-page contact sheets. Confirmed revised K-1 order: P1 equal routes, P2 guesses, P3 mirror, P4 unequal heights, P5 compare, P6 vertical, P7 inverse.
- Adult guide has 17 Letter pages. Its page finder names all 21 final numbered problems. Each problem has a matching solution, held hints, prerequisite information, and accessible reasoning. Shared configurations intentionally have one joint key.
- Added preparation, concrete common launch, hour menu, stopping points, extensions, source distinctions, and fidelity limits.

## Mathematics

- check_geometry.py passes with exact fractions and direct source comparison, without running the student builder.
- All assigned straightened crossings lie strictly inside the drawn permitted segment; all required reflected points fit the 16.8 by 18.2 cm working region.
- Mirror B/C equality holds at every shared contact; the opposite-side auxiliary route is identified correctly.
- Equal minima are checked by exact squared lengths, shared contact by exact crossing equality.
- The complete inverse answer is an open ray above the line, with two concrete legal examples.
- Restriction answers are yes/no/yes for C-D / E-F / C-F; no unjustified endpoint optimizer is supplied.
- Uniqueness follows from equality in the Euclidean triangle inequality and the single crossing of opposite half-planes.
- Sampling is identified as a sanity check rather than a proof.

## Visual review

- Rendered all 17 adult-guide pages with pdftoppm at 100 dpi and opened every page image.
- Reflowed dense concluding material onto separate readable pages.
- Split the vertical board into three separate solution views to avoid overlapping contact labels.
- Repositioned low reflected-point labels and masked label backgrounds to prevent collisions with paths or captions.
- Inspected the resulting pages again. No clipped body text, missing symbols, footer collisions, or overlapping labels remain.
- Final content uses embedded DejaVu fonts, 10.4 pt body text with 14.25 pt leading, consistent headings, and a draft/unpiloted footer on every page.
- Unchanged text-only pages retained the same layout; final guide page count and full extraction were checked.

## Preservation

The SHA-256 values of the three student PDFs match the initial audit. The adult scripts write only facilitator-guide.pdf and files in facilitator-src. No student files were edited.
