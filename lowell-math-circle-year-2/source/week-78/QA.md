# Verification and limits

## October 23, 2026 review-card fixes (v3)

The review card's shoulds and coulds 5, 6 and 9 were made after the organizer's October 17 approval: see README.md. `checks/check_card_fixes.py` recomputes every changed claim with exact fractions over a quarter grid. The claims are: the falling-diagonal pair meets only at (6,6); Problem 4's junction is still (2,2); one dot allows many junctions; Problem 5's same-row pair allows exactly the row to the left of P; Q is off the line; and a 12 cm arm crosses every printed board. All checks in build-manifest.json pass. The packet was rebuilt from the extracted ZIP. Changed pages were rendered at 80 dpi and inspected: students pp. 1, 3 and 4, and guide pp. 1–3; the other pages changed only in the footer id. The traced shape and the younger entry are unrehearsed; the week is unpiloted.


## October 15, 2026 introduction revision

This is a user-directed revision of an existing reviewed packet, not a new worksheet-generation run. Student p1 retains the minimum-tie definition and adds U=(1,4), V=(4,2), whose unique crossing is (4,4). Blue solid and orange dashed lines remain distinguishable in monochrome. Student p2 explicitly asks for one single-point meeting and one whole-stretch overlap. Problems 1–7 remain on pp2–5. Guide launch, student-page references and 15-sheet allocation are synchronized. Independent review caught an orphan phrase creating a fifth guide page; shortening only the launch restored the four-page guide and its proof references.

A fresh independent reviewer inspected all final student and guide pages, checked mathematics and guide/material consistency, and approved the PDFs after revision. The original independent, student and guide check suites all pass; new launch examples have explicit regression checks. All final pages were rendered at 100 dpi and visually inspected. The actual final portable ZIP was extracted to a clean directory and rebuilt with only packaged inputs; page text, counts, Letter dimensions and all rendered pixels matched the checked PDFs. Physical rehearsal and classroom piloting remain unperformed.

- week-78-students.pdf: 5 pages; SHA-256 d981cc7557ec477bb61cb5ef4a5f424260d4a235e5ce8a14227e9ef338e12a89
- week-78-facilitator.pdf: 4 pages; SHA-256 02b2fc713f1de0fa035b12c879dc48bebee9aeab33774f3090e5922997cf66b7

## Earlier review and continuing limits

The original packet completed fresh writer, adversarial critic, independent mathematical checker and reviser stages. The adult guide was separately authored and the pair independently reviewed. The mathematical checks distinguish finite computation from general proofs. Digital reconstruction does not validate physical tile/card handling, printing/tracing, timing, staffing or classroom age fit.

Production used installed TeX packages, with private temporary runtime format initialization on this minimal image. No generated format, cache, reference book, external font or network input is packaged or required on a normal TeX installation.

Organizer promotion: October 17, 2026. Status/metadata only; accepted student and facilitator PDFs unchanged. Unpiloted; physical rehearsal remains untested.
