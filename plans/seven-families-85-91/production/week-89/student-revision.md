# Week 89 fresh revision stage

Addressed the critic’s R1 without removing or shortening any investigation. The shared K–5 readiness menu remains 20 consecutive problems across 11 student pages.

- Materials page 1 now supplies seven 25 × 25 mm input cards, with multiset 0,0,1,2,2,3,4. This deck supports the separate Problems 7, 11–13 visits.
- Materials page 2 now supplies six writable 50 × 25 mm total cards. No exhaustive deck of totals is required.
- Student page 4 now says to use supplied input cards and to use each shown input once. The latter distinguishes the five illustrated cards from the whole reusable seven-card deck.
- Both original boards and scale bars remain unchanged: 120 × 120 mm and 140 × 120 mm, with 20 mm cells. PDF vector measurement confirms all card dimensions to 0.001 mm and board dimensions within 0.002 mm. Actual printer scaling, cutting, piece fit and classroom use remain untested.

Rebuilt final/students.pdf (11 pages) and final/materials.pdf (2 pages) from matching final/src/build.py and TeX sources. Rendered and visually inspected every final page, including the revised page 4 and both card sheets. No overlap, clipping, overflow, LaTeX warning or misplaced card was found. All ten student pages other than page 4 render pixel-identically to the reviewed draft. All 20 problem numbers remain consecutive.

Copied the independent mathematical reviewer’s check_math.py byte-for-byte into final/src/check_math.py and ran it successfully; results are final/math-check-results.json. Mathematical tasks and worked diagrams are unchanged. The reviewer’s assumptions and guide requirements remain with the coordinator. Final guide review, portable source packaging and main publication are subsequent production steps.
