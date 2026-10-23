# Week 40 review-card fixes, October 23, 2026 (version 3)

From the keep card [plans/review/week-40.md](../../../../../plans/review/week-40.md) (in the repository). The student packets were first converted to problem files with no wording change (byte-identical LaTeX, 0 differing pixels); these fixes were made afterwards in the problem files and the guide. The bonus was not changed.

| Card item | Change |
|---|---|
| 1 (should) | Grades 4–5 Problem 6 has its own page: before-and-after pictures with end dots for a curl (J, K) and a slide (T, U, V to X, Y, Z), with the arrow between "before" and "after", and "Check the curl and the slide the way you checked the move in Problem 5. Every way of moving a loop is made of curls, the move in Problem 5, and slides. Can the three-crossing loop become the plain loop?" The "Mathematicians have shown" sentence is gone. Guide p. 5 keys both moves (J=K; Y=U, Z=2U−T, X=2T−2U+V for all 27 inputs, shared out). |
| 2 (should) | Grades 4–5 Problem 7 has its own page with the figure-eight drawn 148 mm wide, arcs labelled 1–4, six four-arc records and a box: "Find every coloring of this loop. It cannot become a plain loop. What can equal coloring counts tell you about two loops?" The curve is (cos t − 1.5 cos 3t + 0.5 sin 2t, sin t + 0.5 sin 2t − 1.5 sin 3t), crossings at 59° or more, taken alternately over and under. Guide p. 5 gives its crossings and the argument that only RRRR, BBBB, GGGG work. |
| 3 (should) | Guide p. 2 launch: a partner, or in grades 4–5 a child referee, checks every crossing ("all same" or "all different") before a record is filled in; the adult colors one crossing wrongly (R over, R and B under) for children to catch. |
| 4 (should) | K–1 Problem 2 is the missing-color grid (was Problem 5); the trefoil, plain loop and cords are Problems 3–5. |
| 5 (should) | Problem 1 in every band: "How many whole arcs does this loop have?" on an unlabelled 70 mm figure-eight, with "arcs: ___". Keys: four, and a count of eight stops at overpasses. |
| 6 (should) | K–1 Problem 6: "color every arc of both strands"; "A strand may stop at an end dot in this picture. Use tracing paper for each try." sits above the picture; the six cases are numbered 1–6. |
| 7 (should) | The end dot R is S in every picture, in the table headers and in the guide ("(L,P,S,Q)", "S=L"). |
| 8 (should) | Grades 2–3 and 4–5 Problem 5: a nine-row table headed L, P, middle, S, Q; grades 4–5 also has an answer box. The 2–3 key lists the nine rows. |
| 9 (should) | Grades 2–3 Problem 4: "Which cords can you move into this plain loop shape?"; the follow-up "What can your attempts tell you, and what remains uncertain?" is in the guide's key. |
| 10 (should) | Guide p. 2: an overhand knot tied the other way round is the mirror image and cannot be laid out to match; retie it if every crossing comes out reversed. |
| 11 (should) | Guide p. 2: close each cord by overlapping its ends about 3 cm and taping them flat, never tying them; the pretest predictions are that a curl in a plain loop falls open when lifted and a taped slipped overhand knot is an unknot that keeps its knotted look. |
| 12 (should) | Guide p. 2: the 60-minute timetable is replaced by one route per band, a 5-minute launch and about 35 minutes at the tables: Problems 1–5 first in every band; K–1 and 2–3 Problem 6 and 4–5 Problems 6–7 on return. The K–1 trefoil (Problem 3) is now in the first route. The route note (p. 7) says the same. |
| 13 (could) | The arrow sits between "before" and "after" (2–3 and 4–5 Problem 5, 4–5 Problem 6). |
| 14 (could) | Page 1: the worked arc has no "input", "process" or "output"; "start" and "stop" sit below the strand, clear of it. |
| 15 (could) | No hyphenation on student pages (`\hyphenpenalty=10000`). |
| 16 (could) | K–1 Problem 5: cords A, B, C, D, each with "yes" and "no"; the guide tags them (A plain loop, B and D complicated unknots, C trefoil). |
| 17 (could) | Guide p. 1 opens with a plain sentence ("A knot is a closed loop of cord that may be moved and bent but never cut …") before the formal one. |

Footers F40-K-v3, F40-23-v3, F40-45-v3: K–1 five pages (Problems 1–6), grades 2–3 four (Problems 1–6), grades 4–5 six (Problems 1–7). The guide is still 6 pages plus the route note; its key alignment line names v3. The guide's own diagram of the worked arc was dropped (it repeated student page 1).

## Checks

- `review/verify_card_shoulds_2026_10_23.py reference-pdfs` (0 failures) reads every knot diagram back from the PDFs (cord pieces, end dots, and the strand through each gap) and recomputes: the figure-eight on Problem 1 in all bands and on 4–5 Problem 7 has 4 arcs, 4 crossings, 3 three-colorings (all one color) and 25 five-colorings; the 4–5 labels name four different arcs and the crossings match the guide's list; the trefoil in all bands has 9 colorings, 6 with more than one color, and the guide's crossing table; the two-crossing move gives one completion for each of the nine (L, P) before and after with S=L, Q=P; K–1 cases 1, 3, 5, 6 work and 2, 4 do not, and every disc's fill matches its letter; the curl keeps J=K; the slide gives X=2T−2U+V, Y=U, Z=2U−T for all 27 inputs before and after; the Type I–III identities for a*b=2b−a. It also checks the wording, page counts, footers, problem order, the S labels, the table, the arrow position, "start"/"stop" clearance, the absence of line-end hyphens, and the guide's sentences, route table, key alignment and route note. The v2 PDFs fail it.
- `src/check_math.py` and `verify_math.py` pass.
- Every page of the three packets and the guide was rendered at 80 dpi and inspected.
- A clean rebuild from the extracted ZIP reproduces the print PDFs; `verify_revision.py` and `verify.py` pass against the new reference PDFs (no font alternates are now allowed).
- `plans/review/checks/week-40/` now reads the archived v2 PDFs (the bonus PDFs are unchanged) and reproduces its stored results.

Deferred: none of the card's items. The taped cords A–D, the slipped-knot prediction, the 2.4 mm marker channel and the referee routine are physically unrehearsed; the week is unpiloted.
