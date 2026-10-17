# Week 79: approved facilitator hint correction, October 17, 2026

Scope: resolve only fix 1 in the Week 79 review card. Guide page 3 now scopes the finite-list hint to “Problem 4, smallest-card rule” and gives the Problem 3 contrast: after day 1, card 1 is in B under the smallest-card rule and in A under the changed rule, while counts remain equal. Other review proposals and Weeks 80–84 are untouched. Organizer promotion of October 15 and unpiloted status are unchanged.

## Independent mathematical check

The correction was checked from the two transfer rules, without importing the package checker. With the smallest-card rule, induction from empty bowls gives A = {n+1, …, 2n} and B = {1, …, n} after day n: adding the next pair makes n+1 the smallest, and transferring it gives the next instance. Thus card k transfers on day k and stays in B. Every nonempty fixed finite list is in B by its largest label's day (the empty list is vacuous). On every positive day N, card N+1 remains in A; day 0 has no cards in B.

With the larger-new-card rule, day n transfers only 2n. Every odd card stays in A from its arrival onward. Hence card 1 distinguishes the rules from day 1 onward. Both rules add two to A and transfer one to B each day, so both bowls have n cards after day n. These arguments establish the unbounded claims; computation alone does not.

A separate list-based replay checked both rules for 2,000 days: exact memberships, equal counts, the card-1 contrast, the N+1 witness for the smallest rule, and eventual inclusion of lists 1–6, 1–12 and {3,20,79,123}. All assertions passed. The existing portable checker also passed its 500-day replays during both builds.

## Output and package verification

- The published guide is still four pages. All four pages were rendered with PyMuPDF; page 3 was visually inspected at 108 dpi with clean text, spacing, header and footer. Pages 1, 2 and 4 are pixel-identical to the pre-correction guide.
- The builder completed without TeX errors or overfull boxes.
- Both the local build and a clean build from the newly extracted ZIP produced byte-identical PDFs. The ZIP contains exactly the documented six owned source files, each byte-identical to its editable counterpart; no generated or private files were added.
- Student PDF and source are unchanged. Student SHA-256: `b924d6631e3567547fab92a9b186c669c1671187d99cadeff6f513a3fe624493`.
- Corrected guide SHA-256: `a7a22397a0bb7e77790fa59c4e86b971f9669af2f77be792fd16c6ecfecab51c`.
- Current guide, editable source, portable ZIP, mathematical-check hash record and Week 79 reconstruction record are synchronized. No additional tracked Week 79 reference PDF or combined set exists. Historical review evidence remains historical; current review card, math review and index identify only fix 1 as resolved. No external Drive copy was accessed or updated.

Digital checks only. Physical printing, material fit, procedure rehearsal and classroom piloting remain untested.
