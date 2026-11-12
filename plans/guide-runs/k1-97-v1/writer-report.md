# Week 97 K–1 guide: writer-stage report

## Deliverables and scope

- `draft/k1-guide.pdf`: **4 US Letter pages**, W97-K-FAC-v1, pdfLaTeX, model-guide sans-serif typography and density.
- `draft/src/`: `k1-guide.tex`, independently computed `answers.tex`, `check_guide.py`, `build.sh`, and build README. No TeX intermediates or machine-specific build paths.
- Writer stage only. No guide critic or reviser was run. Nothing was published or committed. All authored repository files are inside this run folder; student files are unchanged.

The theorem-first opening explains that square leftovers repeat when a side increases by the group size, so a finite complete cycle covers all square outputs; groups of 3 or 4 allow only 0 and 1, while groups of 6 allow 0, 1, 3 and 4. It distinguishes finite game completeness from universal explanation, names information lost by a leftover, and gives the odd-square ring destination for groups of 8. It refers the adult to the base overview for the older tables' prime/composite mathematics rather than repeating it.

## Exact replacement and inputs consulted

Once the student pages are approved, replace **“K–1 route (adult-led, no packet, about 15 minutes)” on page 2** of `lowell-math-circle-year-2/week-97/week-97-facilitator.pdf`, packet W97-FAC-v3. Retain that guide's shared launch, mathematical overview and older-table guidance. This draft does not edit the base guide's other now-stale “no K–1 packet” references; those are packaging/integration work, not a writer-stage change.

Read the root project guidance, week-guides brief and generated WRITER prompt; final K–1 PDF and source; K–1 outline; both student reviews; K–1 drafts README; base Week 97 guide, older student pages, source README and source notes; and Week 98 model guide/source. There was no `.agents/` skill directory in this worktree. The original scholarly and teaching PDFs referenced by the older authored material were not reopened; no new quotation or claim of direct source review is made.

## Final-packet alignment and independent mathematics

The student reviews describe the old **9-page** packet. The actual final packet has **13 pages**, Problems **1–11** on matching pages, the separate 6-by-6 workboard on p. 12, and side cards on p. 13. The guide uses only this final numbering and order, notably P3 rectangles **4×3, 3×2, 5×2, 5×3**, not the old review's order.

My `check_guide.py` does not import or execute the student checker. It uses explicit tile chunks and separately checks with `divmod`; it exhausts every allowed side card and computes all lists feeding the printed guide. It also verifies the final student SHA-256, PDF page/problem/group-size anchors, every guide problem/page heading, answer macros, guide headers/footers, and Letter size. It checks complete residue classes, repeat identities on finite instances, coordinate-counted rings through ring 50, the additional demonstration, optional-card extensions, and all printed arithmetic and material-count claims. Universal claims rely on the printed arguments, not the finite tests.

Final answers independently obtained:

| Problem | Answer |
|---|---|
| 1 | Sides 1–6, groups of 4: 1, 0, 1, 0, 1, 0; circle 0, 1. |
| 2 | Groups of 4, cards 1–5: 0 → {2,4}; 1 → {1,3,5}; no other leftover. |
| 3 | In printed order: 0, 2, 2, 3. Both 2 and 3 are possible. |
| 4 | Groups of 3: 1, 1, 0, 1, 1, 0; circle 0, 1. |
| 5 | Groups of 6: 1, 4, 3, 4, 1, 0; circle 0, 1, 3, 4. |
| 6 | Groups of 6, cards 1–6: 0 → {6}; 1 → {1,5}; 3 → {3}; 4 → {2,4}. |
| 7 | Groups of 2, sides 1–5: 1, 0, 1, 0, 1; odd side cards leave 1. |
| 8 | Side 9 leaves 1; side 10 leaves 0, in groups of 4. |
| 9 | Sides 1,3,5 each leave 1 in groups of 8; added rings hold 8 and 16. |
| 10 | Side 7 leaves 1; outer ring is 24, three groups of 8. |
| 11 | Groups of 8, cards 1–6: 0 → {4}; 1 → {1,3,5}; 4 → {2,6}. |

The revised packet's newly added early secret game, groups-of-2 page and groups-of-8 secret game (current P2/P7/P11) are included in this independent writer computation. This is not a substitute for the upcoming Claude guide critique.

## Visual, dimensions and rebuild evidence

- Personally rendered and inspected **all 13 final student pages**, including the repeated-removal strip, all game rows, the rings, board and six dot-picture cards. Render previews are in `tmp/student/`.
- Personally rendered and inspected **all 4 final guide pages after the last edit**, including the non-task worked visual, all answer lists, headers and footers. No overlap, clipping, missing glyph or split solution occurs. Previews are in `tmp/guide/`.
- The guide uses the same 11-point sans-serif / 0.7-inch Letter geometry as the Week 98 model, with no title rule. The solution pages are dense but legible and self-contained.
- Verified PDF drawing coordinates for 26 mm group-card cells (including both orientations of the six/eight cards) and the p. 12 board width of 156.001 mm (rounding to 156 mm). Source and rendered cut lines agree with six 58×74 mm side cards. These are digital geometry checks, not a physical fit test.
- Final `build.sh` compiled twice successfully, explicitly rejected TeX errors and overfull boxes, cleaned its temporary files, and finished with the checker passing.
- Copied `src/` and the unchanged student `k-1.pdf` to a directory outside the repository (`/tmp/w97-guide-clean-H534Vw`), with the student PDF beside `src/`. Built there successfully and confirmed both **identical extracted text and byte-identical PDF** against the delivered guide. No repository fallback was used there. Logs and comparison text are in this run's `tmp/`.
- The host's isolated TeX environment was sourced before compilation, as directed; that machine-specific setup is **not** embedded in `build.sh` or the portable source.
- Final guide SHA-256: `c6602443451a5f67788f3a303d7326787e94f841886973cab659646347903ad0`.
- Unchanged student SHA-256: `4905ded7fa316b912b7f2de7159f34192d11ff661e3026c322e41e72a430cc4d`.

## Student-page risks and preparation details

No mathematical error was found in the final student packet, and no student page was changed. Remaining operational concerns are hypotheses, not classroom findings:

- A child may treat the straight three-cell card as a rigid strip. The guide explicitly permits any tiles from any position and makes the card a count check.
- An incomplete final card can be mistaken for a removable group. The guide shows and names the partial group as the leftover wherever its tiles lie, and says it never goes in the cup.
- P4's side 6 requires 12 card-fills; repeated handling can consume the hour. The guide permits pooled cases and return visits, and protects time for the early game.
- Revealing an empty slot in the deck, spare tiles, the cup, residual positions or the number of removals can leak the secret. The guide hides all of these and shows only a rearranged leftover pile.
- P8 exceeds the 64-tile kit and is intentionally without building. P9 builds on the table. P10's optional 49-tile check fits the kit but not the six-wide board; the guide uses the table and borrows the printed group-of-8 card from p. 9.
- Print the workboard loose and cut only one card sheet per pair. The task pages already supply the needed group cards; no missing task-specific printable was found.

Objects not supplied by a week PDF are the ordinary 64 tiles, cup, folder, whiteboard/pen and scrap paper. The non-task table demonstration uses a temporary **five-space row drawn on the existing whiteboard**, each space at least 26 mm; it introduces no new deck or manufactured piece. Its side-3/groups-of-5 example is absent from every student task and gives away none of their answers. An optional later side-7 extension uses one hand-marked scrap card, explicitly identified as optional.

**Unpiloted and physically unrehearsed:** actual-size print/fit, cutting, screen concealment, child handling, staffing and timing are not verified by digital checks. No critic findings exist yet; none have been accepted, declined or claimed fixed in this writer stage.
