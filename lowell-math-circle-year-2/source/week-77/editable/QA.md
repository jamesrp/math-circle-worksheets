# Verification and limits

## October 23, 2026 review-card fixes

The review card's shoulds 1–5 and coulds 6–8 (plans/review/week-77.md), made in the problem files, the guide and a new materials sheet. Checks run on the built PDFs and sources:

- `checks/independent_check.py` asserts the new Problem 2, 3 and 5 wording, the joined board's new C = (5.8, 1.4), that A, C, E and B, C, D are no longer collinear, that the triangles still meet only at C and that AB and DE stay 5.8 cm. The preserved `baseline_check.py` still checks the October 15 board's coordinates and is unchanged.
- `student/check_math.py` and `guide/check_math.py` add the new Problem 3 answer: on the joined board the first loop can be gone at stage 5 with either first edge; on the square only with AC first; all eight builds have counts 0, 1, 2, 1, 0.
- `review/verify_card_fixes_2026_10_23.py` reads the built PDFs: footers, wording, the bend at C (23.6 degrees each way), each printed tile's corners against the dots of its student board, each tile's name and edge names (each along the side whose corners it names), seven strips of the right lengths, 48 tokens with the stated labels and 8 stage cards, and the guide's new and removed passages.
- Student pages 1, 2 and 6 are pixel-identical to F77-45-v2 above the footer; pages 3–5 changed as intended. Every changed page was rendered at 80 dpi and inspected. A clean rebuild from the extracted source ZIP reproduces all three PDFs.

Physical rehearsal with the printed pieces and classroom piloting remain unperformed.

Critic follow-up, later on October 23, 2026 (F77-45-v4, F77-FAC-v4): Problem 3's square answer area is split into "Square, AC first:" and "Square, DA first:", and the guide gives Problem 3 about 8 minutes. Student page 4 changed above the footer; the other pages changed only their footer. A clean build from the extracted ZIP matches the print copies. Current hashes:

- week-77-students.pdf: 6 pages; SHA-256 5ae3ee7b1214a2d0353654b2990939ea114e3fd07872709f9fdcdc56a92bc489
- week-77-facilitator.pdf: 4 pages; SHA-256 6d88063412ffdd3bdffb71560bfe455a73a952b120b7c5f9447b3fcf32e4328b
- week-77-materials.pdf: 2 pages; SHA-256 42256b059d80b89a4f60a5b13b0210ccb8d7dfff81e65f79c971b111364cd4fe

## October 15, 2026 introduction revision

This is a user-directed revision of an existing reviewed packet, not a new worksheet-generation run. Student p1 adds the physical square progression (rim, diagonal, one filled half, both halves), explicitly retains all edges, and follows with a full triangular-loop token cancellation. Problems 1–6 remain on pp2–6. Student p2 retains its 6.2 cm working square. Guide pp1–4 update page references, the six launch tokens, 45 token cards, 17 tiles and 18 student-sheet preparation count. The student builder now initializes a private TeX format when the installed package tree lacks one, without writing to the home cache.

A fresh independent reviewer inspected all final student and guide pages, checked mathematics and guide/material consistency, and approved the PDFs after revision. The original independent, student and guide check suites all pass; new launch examples have explicit regression checks. All final pages were rendered at 100 dpi and visually inspected. The actual final portable ZIP was extracted to a clean directory and rebuilt with only packaged inputs; page text, counts, Letter dimensions and all rendered pixels matched the checked PDFs. Physical rehearsal and classroom piloting remain unperformed.

- week-77-students.pdf: 6 pages; SHA-256 9382c19f6c3281a0f0873c6c3c4735b9c7fa762edd20d69a58ff7e6a6c7b1867
- week-77-facilitator.pdf: 4 pages; SHA-256 61ef56e4679e6dd3862727854822c59d5eba6a70adf9c1ee15d3e864b73d5539

## Earlier review and continuing limits

The original packet completed fresh writer, adversarial critic, independent mathematical checker and reviser stages. The adult guide was separately authored and the pair independently reviewed. The mathematical checks distinguish finite computation from general proofs. Digital reconstruction does not validate physical tile/card handling, printing/tracing, timing, staffing or classroom age fit.

Production used installed TeX packages, with private temporary runtime format initialization on this minimal image. No generated format, cache, reference book, external font or network input is packaged or required on a normal TeX installation.
