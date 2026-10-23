# Week 87 student revision verification

All nine investigations retained: shared Problems 1–3 (Grades 2–5), line Problems 1–4 (Grades 3–5), upper Problems 1–2 (Grades 4–5). No independent K–1 packet.

Revisions address all three adversarial items and both independent mathematical material defects. Line page 1 now displays one unchanged five-voter comparison, every individual distance choice including a tie, and the complete aggregate. Materials page 5 supplies separate 23×23 mm X/Y tally labels. Materials page 4 has two 30×30 mm label slots, a 170×90 mm tally mat, and three 54×54 mm wells with five matching 18 mm targets each. Targets form a quincunx, with 2 mm minimum boundary clearance and 4.627 mm minimum token separation.

The independent check reads actual PDF vectors without importing the builder. It verifies all cut-card dimensions, 36 letter slips, 6 option tiles, 5 vote tokens, 5 favorite markers, 2 proposals, 2 tally labels, label slots, every tally target, 160 mm board span and 19 mm lane pitch. All material sizes and relevant clearances passed. A digital assembly used actual PDF crops to keep all five favorites and both proposals visible while the five vote tokens occupied their final wells and independent X/Y labels remained above them.

Rendered and visually inspected all 14 final pages individually: shared 1–3, line 1–4, upper 1–2, materials 1–5. Text and diagrams are legible, content is inside the page, and headers/footers/numbering are consistent. Latest changed tally page was re-rendered and inspected after enlargement. No Overfull or Missing character warnings. Numerical checks include the new 2–2/Tie example and every opponent for all 3,003 five-favorite multisets. Finite checks do not replace the general arguments.

Portable source ZIP contains only owned Python/README/QA sources and four matching reference PDFs. Clean extraction and rebuild produce byte-identical copies of all four final PDFs. See revision-audit/rebuild.json for hashes and counts and geometry.json for measurements. These stage evidence paths are outside the portable package; the package is independently rebuildable.

Physical cutting, placement, classroom procedure, timing and piloting remain untested. No facilitator guide was authored in this stage.

## Card fixes, October 23, 2026

Student pages changed from the review card: shared pp. 2–3; line pp. 1–4; upper pp. 1–2; materials p. 4 (wording, number-line stems, the third set's voter order, upper p. 2's work line and the knockout mat's Out and Winner boxes). Each changed page was rendered at 80 dpi and inspected; shared p. 1 and materials pp. 1–3 and 5 are pixel-identical to the previous build. `../review/check_pdf.py` reads every number line from the new PDFs: all favorite stems are 4 mm, labels stack 7 mm apart only where favorites coincide, and each voter's favorite matches the checked data. It also measures the knockout boxes: each is at least 5 mm wider and 11 mm taller than the 28 mm tiles it holds, inside the unchanged 175 × 100 mm mat. `../review/check_card_fixes_2026_10_23.py` checks the guide's new claims. Cutting, fit and use remain physically unrehearsed.
