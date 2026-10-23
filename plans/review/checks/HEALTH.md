# Review check health

Health sweep of every script under `plans/review/checks/`, October 23, 2026, after the day's card fixes, critic follow-ups, problem-file conversions and footer bumps. Each script was run on a clean checkout of `origin/main` (at 389d252) with these repairs, and the folders repaired after that run were run again.

**How to run.** Run each command from the script's own folder (`cd plans/review/checks/<week>`). Extraction scripts (`extract*.py`, `pdf_geometry.py`, `pdfgeom.py`) write the JSON the other checks read, so run them first, as the commands show. In plain alphabetical order several checks read a stale JSON and pass or fail for the wrong reason. A `> file` in the command is the committed output the script prints to standard output; the other scripts write their own output files.

**Status.**
- *pass*: passes unchanged.
- *pass; re-pointed*: the script deliberately checks the version that was reviewed. It now reads the archived copy explicitly (`archive-before-*` print folders or source ZIPs, each MD5-identical to the reviewed copy) and says so in a comment naming the commits that changed the week and the check that covers the current pages.
- *pass; updated*: a revision moved or reshaped what the script reads, so its expectations follow the change, with a comment naming the commit. What it checks is kept.
- *pass; finding paired*: a review finding that printed FAIL by design is confirmed on the archived copy as reviewed. A second check confirms the correction in the current copy.
- *pass; needs input*: the script needs an argument or module that is not in the repository.
- *FAIL: packet error*: a real error in the current packet. The packet was not changed.
- *FAIL: open finding*: a reviewed finding that is still open in the current packet.

**Result.** 394 scripts (plus 69 helper modules). 244 pass unchanged, 68 re-pointed, 53 updated, 21 with a finding paired, 5 need input. 2 fail on real packet errors and 1 on an open finding.

**Real packet errors (not fixed here).**
- Week 5 return-visit guide, p. 3, order-3 impossibility argument: "The bottom corners are forced to be b, a." With the top corners a (left) and b (right), the diagonals force bottom-left a and bottom-right b, so the bottom corners are a, b. The contradiction still follows. Check: `week-05/check_return_visit.py`.
- Week 28 guide, p. 2: "(the sector lists on page 10)". The sector table is on printed p. 11, since the 2-3 Problems 2 and 3 swap (799a994); the pp. 10 and 13 references were updated, this one was not. It is still present after c6c73f2. Check: `week-28/check_base.py`.

**Open finding.** Week 41 bonus, pp. 1-2: the portal boards mark only the left and right seams, though the rule wraps columns too (math review problem 1; the bonus was not on the card). Check: `week-41/check_diagrams.py`.

**Other findings.** Several checks had been passing for the wrong reason. Week 94's `rebuild_compare.py` rebuilt nothing, since `build.py` had moved, and still exited 0; it now exits 1 when a PDF is not rebuilt. When the scripts run in alphabetical order, the checks in Weeks 5, 18, 20, 22, 25, 27, 29, 30, 34, 35, 43 and 61 read a JSON extracted from older PDFs. The Week 9 app checks need the pre-redesign app data, `git -C <small-math-adventure> show 0769bac~1:dist/puzzles.json > puzzles-reviewed.json`, because the app's billiard family was redesigned in 0769bac. Week 4's `check_codes.py` needs `pip install wordfreq english-words`. Week 43's typo "The27-story" is already fixed in the current guide. Weeks 98-100 and 83-85 may still change in other lanes.

| Week | Script | Command | Status | Note |
|---|---|---|---|---|
| 01 | check_pdf_geometry.py | `python3 check_pdf_geometry.py` | pass |  |
| 01 | check_k1.py | `python3 check_pdf_geometry.py && python3 check_k1.py` | pass |  |
| 01 | check_k1_witness.py | `python3 check_pdf_geometry.py && python3 check_k1_witness.py` | pass |  |
| 01 | check_middle.py | `python3 check_pdf_geometry.py && python3 check_middle.py` | pass |  |
| 01 | check_symmetry.py | `python3 check_pdf_geometry.py && python3 check_symmetry.py` | pass |  |
| 01 | check_upper.py | `python3 check_pdf_geometry.py && python3 check_upper.py` | pass |  |
| 01e | big_games.py | `python3 big_games.py 4x4` | pass; needs input | takes a board name and an optional bound: 4x4 (default) or hex333 600; writes big_games_<board>.out |
| 01e | boards.py | `python3 boards.py` | pass |  |
| 01e | check_cross.py | `python3 check_cross.py` | pass |  |
| 01e | check_extra.py | `python3 check_extra.py` | pass |  |
| 01e | check_guide.py | `python3 check_guide.py` | pass |  |
| 01e | check_k1.py | `python3 check_k1.py` | pass |  |
| 01e | check_middle.py | `python3 check_middle.py` | pass |  |
| 01e | check_upper.py | `python3 check_upper.py` | pass |  |
| 01e | pdfpaths.py | `python3 pdfpaths.py` | pass |  |
| 02 | extract.py | `python3 extract.py` | pass |  |
| 02 | check_json.py | `python3 extract.py && python3 check_json.py` | pass |  |
| 02 | edge_cases.py | `python3 extract.py && python3 edge_cases.py` | pass |  |
| 02 | solve.py | `python3 extract.py && python3 solve.py` | pass |  |
| 02 | verify_diagrams.py | `python3 extract.py && python3 verify_diagrams.py` | pass |  |
| 03 | check_week03.py | `python3 check_week03.py` | pass |  |
| 03 | dump_mats.py | `python3 dump_mats.py` | pass |  |
| 03 | guide_rows.py | `python3 guide_rows.py` | pass |  |
| 04 | extract_pdf.py | `python3 extract_pdf.py` | pass |  |
| 04 | check_codes.py | `python3 extract_pdf.py && python3 check_codes.py` | pass; needs input | needs the word lists: pip install wordfreq english-words |
| 04 | check_pictures.py | `python3 extract_pdf.py && python3 check_pictures.py` | pass |  |
| 04 | check_rings.py | `python3 extract_pdf.py && python3 check_rings.py` | pass |  |
| 04 | check_theory.py | `python3 extract_pdf.py && python3 check_theory.py` | pass |  |
| 04 | check_times.py | `python3 extract_pdf.py && python3 check_times.py` | pass |  |
| 04 | edge_cases.py | `python3 extract_pdf.py && python3 edge_cases.py` | pass |  |
| 05 | extract_pdf.py | `python3 extract_pdf.py > extract_pdf.out` | pass |  |
| 05 | check_return_visit.py | `python3 extract_pdf.py && python3 check_return_visit.py > check_return_visit.out` | FAIL: packet error | return-visit guide p. 3: "The bottom corners are forced to be b, a"; they are a, b (left, right) |
| 05 | check_week05.py | `python3 extract_pdf.py && python3 check_week05.py > check_week05.out` | pass; updated | guide grids taken by reading order: could 7 (d04ef8f, F05-FAC-v6) moved the 4-5 ladder to p. 7 and the P6 example to p. 8 |
| 05 | edge_cases.py | `python3 extract_pdf.py && python3 edge_cases.py > edge_cases.out` | pass |  |
| 05 | geometry.py | `python3 extract_pdf.py && python3 geometry.py > geometry.out` | pass |  |
| 05 | guide_towers.py | `python3 extract_pdf.py && python3 guide_towers.py > guide_towers.out` | pass |  |
| 05 | source_vs_pdf.py | `python3 extract_pdf.py && python3 source_vs_pdf.py > source_vs_pdf.out` | pass; updated | student LaTeX generated from the problem files (problem_tex.band_tex) |
| 06 | extract_pdf.py | `python3 extract_pdf.py > extract_pdf.out` | pass |  |
| 06 | check_answers.py | `python3 extract_pdf.py && python3 check_answers.py > check_answers.out` | pass; finding paired | quotes the card fixes corrected are confirmed in the archived guide as reviewed (F06-FAC-v4) |
| 06 | source_vs_pdf.py | `python3 extract_pdf.py && python3 source_vs_pdf.py > source_vs_pdf.out` | pass; updated | band_tex; the 4-5 rules paragraph follows Problem 1 on p. 2 since the intro follow-up |
| 07 | extract_pdf.py | `python3 extract_pdf.py` | pass |  |
| 07 | check_answers.py | `python3 extract_pdf.py && python3 check_answers.py > check_answers.out` | pass |  |
| 07 | misere_and_periodicity.py | `python3 extract_pdf.py && python3 misere_and_periodicity.py > misere_and_periodicity.out` | pass |  |
| 07 | source_vs_pdf.py | `python3 extract_pdf.py && python3 source_vs_pdf.py > source_vs_pdf.out` | pass; updated | band_tex; corrected guide quotes located in the archived guide |
| 08 | extract_pdf.py | `python3 extract_pdf.py` | pass |  |
| 08 | check_answers.py | `python3 extract_pdf.py && python3 check_answers.py` | pass; updated | corrected guide sentences located in the archived guides (repo.py) |
| 08 | guide_figs_pdf.py | `python3 extract_pdf.py && python3 guide_figs_pdf.py` | pass |  |
| 08 | return_visit.py | `python3 extract_pdf.py && python3 return_visit.py` | pass; updated | corrected RV-guide sentences located in the archived guide (repo.py) |
| 08 | source_vs_pdf.py | `python3 extract_pdf.py && python3 source_vs_pdf.py` | pass; updated | band_tex (packets are problem files) |
| 09 | extract.py | `python3 extract.py > extract.out` | pass |  |
| 09 | pdfgeom.py | `python3 pdfgeom.py > pdfgeom.out` | pass |  |
| 09 | app_check.py | `python3 app_check.py puzzles-reviewed.json` | pass; needs input | reads the app data as reviewed: git -C <app> show 0769bac~1:dist/puzzles.json; app 0769bac redesigned the billiard family, so the current file stops at KeyError component_min (documented in the docstring) |
| 09 | app_family_check.py | `python3 app_family_check.py puzzles-reviewed.json` | pass; needs input | as app_check.py; output identical to the committed .out on the pre-redesign data |
| 09 | billiards.py | `python3 extract.py && python3 pdfgeom.py && python3 billiards.py > billiards.out` | pass |  |
| 09 | check_answers.py | `python3 extract.py && python3 pdfgeom.py && python3 check_answers.py > check_answers.out` | pass; updated | corrected quotes checked in the archived guide; guide thumbnails matched across pp. 4-5 (card fixes); long (about 4 min) |
| 09 | rv_check.py | `python3 extract.py && python3 pdfgeom.py && python3 rv_check.py > rv_check.out` | pass |  |
| 09 | source_vs_pdf.py | `python3 extract.py && python3 pdfgeom.py && python3 source_vs_pdf.py > source_vs_pdf.out` | pass; updated | band_tex |
| 10 | card_app_check.py | `python3 card_app_check.py <small-math-adventure>/dist/puzzles.json` | pass; needs input | needs the app data; passes on small-math-adventure dist/puzzles.json |
| 10 | check_geometry.py | `python3 check_geometry.py > check_geometry.out` | pass; updated | Grades 2-3 has 13 pages since the card fixes |
| 10 | check_guide_figs.py | `python3 check_guide_figs.py > check_guide_figs.out` | pass |  |
| 10 | check_koenigsberg.py | `python3 check_koenigsberg.py > check_koenigsberg.out` | pass |  |
| 10 | check_pictures.py | `python3 check_pictures.py > check_pictures.out` | pass; updated | 2-3 Problems 6-7 moved to pp. 9-10 (card fixes, 9a65bef); passes after 1bea664 "continued" labels |
| 10 | check_rv.py | `python3 check_rv.py > check_rv.out` | pass; finding paired | two reviewed guide statements have counterexamples (archived wording); current guides carry the corrected hypotheses |
| 10 | check_sources.py | `python3 check_sources.py > check_sources.out` | pass; updated | band_tex |
| 10 | check_theory.py | `python3 check_theory.py > check_theory.out` | pass | long (3-8 min) |
| 10 | check_towns.py | `python3 check_towns.py > check_towns.out` | pass; updated | reviewed p. 12 is p. 13 since the card fixes |
| 11 | extract_pdf.py | `python3 extract_pdf.py` | pass |  |
| 11 | check_answers.py | `python3 extract_pdf.py && python3 check_answers.py` | pass; updated | K-1 P1/P3 print each start twice and P4 has ten rows (5acb95e, F11-K-v4) |
| 11 | source_vs_pdf.py | `python3 extract_pdf.py && python3 source_vs_pdf.py` | pass; updated | problem statements read from the problem files (band_parts) |
| 12 | catalan.py | `python3 catalan.py` | pass |  |
| 12 | check_23.py | `python3 check_23.py` | pass |  |
| 12 | check_45.py | `python3 check_45.py` | pass |  |
| 12 | check_files.py | `python3 check_files.py` | pass |  |
| 12 | check_guide.py | `python3 check_guide.py` | pass |  |
| 12 | check_k1.py | `python3 check_k1.py` | pass; re-pointed | K-1 as reviewed (archive-before-card-fixes); current K-1 checked by editable/review/verify_card_fixes_2026_10_23.py |
| 12 | check_rv.py | `python3 check_rv.py` | pass |  |
| 13 | extract_graphs.py | `python3 extract_graphs.py` | pass; updated | graphs.py: K-1 P5 has 11 bowtie copies (45eb31c); 4-5 p. 7 reprints P1 boards, bottleneck on p. 8 (b696120) |
| 13 | check_critic_fixes.py | `python3 extract_graphs.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 13 | solve.py | `python3 extract_graphs.py && python3 solve.py` | pass; updated | reads the updated graphs.py board lists |
| 13 | theorem_check.py | `python3 extract_graphs.py && python3 theorem_check.py` | pass |  |
| 14 | extract_figures.py | `python3 extract_figures.py` | pass; updated | reads the updated expected.py (gray starts on the recording copies) |
| 14 | check_guide_map.py | `python3 extract_figures.py && python3 check_guide_map.py` | pass |  |
| 14 | check_text.py | `python3 extract_figures.py && python3 check_text.py` | pass |  |
| 14 | rv_check.py | `python3 extract_figures.py && python3 rv_check.py` | pass |  |
| 14 | solve.py | `python3 extract_figures.py && python3 solve.py` | pass; updated | expected.py: recording copies print the start in light gray (0be5284) |
| 15 | extract_crosses.py | `python3 extract_crosses.py` | pass |  |
| 15 | extract_pdf_geometry.py | `python3 extract_pdf_geometry.py` | pass |  |
| 15 | check_all.py | `python3 extract_crosses.py && python3 extract_pdf_geometry.py && python3 check_all.py` | pass |  |
| 15 | search_placements.py | `python3 extract_crosses.py && python3 extract_pdf_geometry.py && python3 search_placements.py` | pass |  |
| 16 | check_diagrams.py | `python3 check_diagrams.py` | pass; updated | split-tint blank side dots (bd86bf0) left to the package verifier |
| 16 | check_math.py | `python3 check_math.py` | pass |  |
| 16 | check_return_visit.py | `python3 check_return_visit.py` | pass |  |
| 17 | extract_pdf.py | `python3 extract_pdf.py` | pass |  |
| 17 | check_math.py | `python3 extract_pdf.py && python3 check_math.py` | pass; updated | reworded guide quotes located in the archived guide; both pairs-page layouts read (750c916) |
| 17 | check_return_visit.py | `python3 extract_pdf.py && python3 check_return_visit.py` | pass; finding paired | "in a row" confirmed on the reviewed RV; current says "next to each other" (750c916) |
| 18 | extract_pdf.py | `python3 extract_pdf.py > out_extract_pdf.txt` | pass |  |
| 18 | check_math.py | `python3 extract_pdf.py && python3 check_math.py > out_check_math.txt` | pass; updated | archived-guide quotes; K-1 P5 two square rows per triangle (64dbf65) |
| 18 | check_rebuild.py | `python3 extract_pdf.py && python3 check_rebuild.py > out_check_rebuild.txt` | pass |  |
| 19 | extract_pdf.py | `python3 extract_pdf.py > out_extract_pdf.txt` | pass |  |
| 19 | check_critic_fixes.py | `python3 extract_pdf.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 19 | check_math.py | `python3 extract_pdf.py && python3 check_math.py > out_check_math.txt` | pass; updated | archived-guide quotes; current guide rows with arrows |
| 19 | check_rebuild.py | `python3 extract_pdf.py && python3 check_rebuild.py > out_check_rebuild.txt` | pass; re-pointed | reviewed builder rerun from the archived pre-conversion ZIP; current ZIP compared with editable/ plus problem files (tools drift reported as NOTE) |
| 20 | extract_boards.py | `python3 extract_boards.py` | pass; re-pointed | reads the archive-before-card-fixes packets (repo.py); bonus current |
| 20 | check_bonus.py | `python3 extract_boards.py && python3 check_bonus.py` | pass |  |
| 20 | check_math.py | `python3 extract_boards.py && python3 check_math.py` | pass; re-pointed | base packets and guide as reviewed (repo.py REVIEWED; d19c46b reshaped them); stale page-3 cross-references confirmed there and page 4 checked in the current guide |
| 21 | extract_geometry.py | `python3 extract_geometry.py` | pass |  |
| 21 | check_base.py | `python3 extract_geometry.py && python3 check_base.py` | pass |  |
| 21 | check_bonus.py | `python3 extract_geometry.py && python3 check_bonus.py` | pass |  |
| 21 | check_guide_diagrams.py | `python3 extract_geometry.py && python3 check_guide_diagrams.py` | pass |  |
| 22 | extract.py | `python3 extract.py` | pass; re-pointed | student PDFs as reviewed (archive-before-intro-followup) against the TeX in that archive's ZIP; check_critic_fixes.py covers the current pages |
| 22 | card_app_check.py | `python3 extract.py && python3 card_app_check.py` | pass |  |
| 22 | check_bonus.py | `python3 extract.py && python3 check_bonus.py` | pass |  |
| 22 | check_critic_fixes.py | `python3 extract.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 22 | check_guide.py | `python3 extract.py && python3 check_guide.py` | pass |  |
| 22 | check_students.py | `python3 extract.py && python3 check_students.py` | pass; re-pointed | via extract.py |
| 22 | check_theorem.py | `python3 extract.py && python3 check_theorem.py` | pass |  |
| 23 | extract_networks.py | `python3 extract_networks.py` | pass |  |
| 23 | check_math.py | `python3 extract_networks.py && python3 check_math.py` | pass; finding paired | "1110 finishes 1101" on the reviewed guide; current prints 1011 (f7a0b21) |
| 24 | extract_decks.py | `python3 extract_decks.py` | pass |  |
| 24 | best_cycle.py | `python3 extract_decks.py && python3 best_cycle.py > best_cycle.out` | pass |  |
| 24 | card_checks.py | `python3 extract_decks.py && python3 card_checks.py > out_card_checks.txt` | pass |  |
| 24 | check_bonus.py | `python3 extract_decks.py && python3 check_bonus.py` | pass |  |
| 24 | check_critic_fixes.py | `python3 extract_decks.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 24 | check_math.py | `python3 extract_decks.py && python3 check_math.py` | pass; finding paired | unqualified gate sentence confirmed on the archived guide; current wording checked |
| 24 | reconcile_checks.py | `python3 extract_decks.py && python3 reconcile_checks.py > out_reconcile_checks.txt` | pass |  |
| 25 | extract.py | `python3 extract.py > extract.out` | pass |  |
| 25 | check_bonus.py | `python3 extract.py && python3 check_bonus.py` | pass |  |
| 25 | check_guide.py | `python3 extract.py && python3 check_guide.py` | pass; updated | launch picture A1, A2, B1 (bc911cb) |
| 25 | check_students.py | `python3 extract.py && python3 check_students.py` | pass; updated | 4-5 P1 prints eight grids for six pictures (c668ca3); long (about 7 min) |
| 25 | second_forcing.py | `python3 extract.py && python3 second_forcing.py > second_forcing.out` | pass |  |
| 25 | second_spot.py | `python3 extract.py && python3 second_spot.py > second_spot.out` | pass |  |
| 25 | second_twomove.py | `python3 extract.py && python3 second_twomove.py > second_twomove.out` | pass | long (about 2 min) |
| 26 | extract.py | `python3 extract.py` | pass |  |
| 26 | check_bonus.py | `python3 extract.py && python3 check_bonus.py` | pass |  |
| 26 | check_guide.py | `python3 extract.py && python3 check_guide.py` | pass; updated | captions "37 tiles" (acb3820); p. 1 12-tile row length (fb262ee) |
| 26 | check_students.py | `python3 extract.py && python3 check_students.py` | pass; updated | third shape boundary 20 (acb3820); long (2-10 min) |
| 27 | extract.py | `python3 extract.py` | pass |  |
| 27 | check_bonus.py | `python3 extract.py && python3 check_bonus.py` | pass |  |
| 27 | check_guide.py | `python3 extract.py && python3 check_guide.py` | pass; finding paired | two reworded sentences confirmed in the archived guide; current wording checked (34082e7) |
| 27 | check_students.py | `python3 extract.py && python3 check_students.py` | pass; updated | 2-3 Problem 4 prints six boards (34082e7, W27-23-v4) |
| 28 | pdf_geometry.py | `python3 pdf_geometry.py > pdf_geometry.out` | pass; updated | 2-3 P2/P3 swapped (799a994); K-1 P3 six M disks again (c6c73f2, F28-K-v4) |
| 28 | check_base.py | `python3 pdf_geometry.py && python3 check_base.py > check_base.out` | FAIL: packet error | guide p. 2 still says "(the sector lists on page 10)"; the table is on printed p. 11. P6 rows finding paired (799a994) |
| 28 | check_bonus.py | `python3 pdf_geometry.py && python3 check_bonus.py > check_bonus.out` | pass |  |
| 28 | kit_crosscheck.py | `python3 pdf_geometry.py && python3 kit_crosscheck.py > kit_crosscheck.out` | pass |  |
| 29 | pdf_geometry.py | `python3 pdf_geometry.py` | pass; updated | target boxes and strips (69100ef); run before check_base.py and check_bonus.py |
| 29 | check_base.py | `python3 pdf_geometry.py && python3 check_base.py` | pass; finding paired | reviewed-guide findings confirmed in the archive, current wording checked; K-1 P6 one target row per pair (69100ef) |
| 29 | check_bonus.py | `python3 pdf_geometry.py && python3 check_bonus.py` | pass |  |
| 30 | extract.py | `python3 extract.py` | pass; re-pointed | reads common.REVIEWED_PDF (the packets as reviewed) |
| 30 | check_bonus.py | `python3 extract.py && python3 check_bonus.py` | pass; finding paired | "how the conclusion changes" confirmed in the archived bonus guide; current asks whether (9d14e21) |
| 30 | check_critic_fixes.py | `python3 extract.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 30 | check_guide.py | `python3 extract.py && python3 check_guide.py` | pass; updated | launch example target 5, weights 2 and 7 (9d14e21) |
| 30 | check_students.py | `python3 extract.py && python3 check_students.py` | pass; re-pointed | extract.py reads the packets as reviewed (common.REVIEWED_PDF; 9d14e21, 7c7712b redrew them) |
| 31 | bonus_layout31.py | `python3 bonus_layout31.py` | pass |  |
| 31 | check_guides31.py | `python3 check_guides31.py` | pass; updated | reworded quotes located in the archived guide (bc911cb, f21417c) |
| 31 | check_students31.py | `python3 check_students31.py` | pass |  |
| 32 | check_card_fixes.py | `python3 check_card_fixes.py` | pass |  |
| 32 | check_guides32.py | `python3 check_guides32.py` | pass; finding paired | false claims in the archived guide confirmed as findings; current guide checked (b2a20e1) |
| 32 | check_students32.py | `python3 check_students32.py` | pass; updated | board B 9 by 6; P6 on its own page (b2a20e1) |
| 33 | pdf_extract.py | `python3 pdf_extract.py` | pass |  |
| 33 | card_checks.py | `python3 pdf_extract.py && python3 card_checks.py > card_checks.out` | pass |  |
| 33 | check_base.py | `python3 pdf_extract.py && python3 check_base.py` | pass |  |
| 33 | check_bonus.py | `python3 pdf_extract.py && python3 check_bonus.py` | pass |  |
| 33 | check_card_fixes.py | `python3 pdf_extract.py && python3 check_card_fixes.py` | pass; updated | follows the critic follow-up v4 (e33eed1) |
| 33 | check_critic_fixes.py | `python3 pdf_extract.py && python3 check_critic_fixes.py` | pass |  |
| 34 | extract.py | `python3 extract.py > out_extract.txt` | pass; re-pointed | base packets and guide from common.REVIEWED; bonus current |
| 34 | card_checks.py | `python3 extract.py && python3 card_checks.py > card_checks.out` | pass |  |
| 34 | check.py | `python3 extract.py && python3 check.py` | pass; re-pointed | extract.py reads base packets and guide as reviewed (archive-before-card-fixes; f708ade); bonus current |
| 34 | check_card_fixes.py | `python3 extract.py && python3 check_card_fixes.py` | pass |  |
| 34 | compare_source.py | `python3 extract.py && python3 compare_source.py > out_compare_source.txt` | pass; re-pointed | reviewed TeX from the pre-conversion ZIP against the reviewed PDFs |
| 35 | extract.py | `python3 extract.py` | pass; re-pointed | reads common.STUDENT and GUIDES (copies as reviewed) |
| 35 | check.py | `python3 extract.py && python3 check.py` | pass; re-pointed | packets and guide as reviewed: K-1 archive-before-card-shoulds, 2-3/4-5/guide archive-before-intro-followup (aa01c74, 70a26ca, 36a239b) |
| 35 | compare_source.py | `python3 extract.py && python3 compare_source.py` | pass; re-pointed | reviewed TeX from the intro-followup ZIP; reference hashes on the current copies |
| 36 | extract_pdf.py | `python3 extract_pdf.py > out_extract_pdf.txt` | pass |  |
| 36 | card_checks.py | `python3 extract_pdf.py && python3 card_checks.py > out_card_checks.txt` | pass |  |
| 36 | check_bonus.py | `python3 extract_pdf.py && python3 check_bonus.py > out_check_bonus.txt` | pass |  |
| 36 | check_critic_fixes.py | `python3 extract_pdf.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 36 | check_guide_text.py | `python3 extract_pdf.py && python3 check_guide_text.py > out_check_guide_text.txt` | pass; updated | reworded claims looked up in the archived guide (1105082) |
| 36 | check_math.py | `python3 extract_pdf.py && python3 check_math.py > out_check_math.txt` | pass |  |
| 36 | check_pages.py | `python3 extract_pdf.py && python3 check_pages.py > out_check_pages.txt` | pass |  |
| 36 | common.py | `python3 extract_pdf.py && python3 common.py` | pass |  |
| 36 | compare_source.py | `python3 extract_pdf.py && python3 compare_source.py > out_compare_source.txt` | pass |  |
| 37 | check_bonus.py | `python3 check_bonus.py` | pass |  |
| 37 | check_math.py | `python3 check_math.py` | pass; updated | letter-cap markers; the B-D finding is fixed (8e92570, 799a994) |
| 38 | check_bonus.py | `python3 check_bonus.py > out_check_bonus.txt` | pass; finding paired | R-row pairing confirmed on the archived bonus; current bonus v2 joins dot to square (8a253a9) |
| 38 | check_diagrams.py | `python3 check_diagrams.py > out_check_diagrams.txt` | pass |  |
| 38 | check_math.py | `python3 check_math.py > out_check_math.txt` | pass |  |
| 38 | common.py | `python3 common.py` | pass |  |
| 39 | extract.py | `python3 extract.py > out_extract.txt` | pass |  |
| 39 | bonus_check.py | `python3 extract.py && python3 bonus_check.py` | pass |  |
| 39 | check.py | `python3 extract.py && python3 check.py` | pass; updated | worked-example routes and P4 route ABCBCDABA (89149a6); K-1 footer finding paired: current F39-K-v5/F39-23-v4/F39-45-v3 match the guide |
| 39 | compare_source.py | `python3 extract.py && python3 compare_source.py` | pass; re-pointed | reviewed make_packets.py against the reviewed PDFs |
| 40 | check_bonus.py | `python3 check_bonus.py` | pass |  |
| 40 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass |  |
| 40 | check_main.py | `python3 check_main.py` | pass |  |
| 40 | diag.py | `python3 diag.py` | pass |  |
| 41 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 41 | check_diagrams.py | `python3 check_diagrams.py` | FAIL: open finding | base slide example follows v3 (6e5b742, plus backtrack picture); the reviewed bonus finding stands: bonus pp. 1-2 boards mark only the left/right seams |
| 41 | check_math.py | `python3 check_math.py` | pass; updated | v3 pages: 2-3 P4 adds RRRDDD, 4-5 P2/P3 swapped, P5 on its own page (6e5b742) |
| 42 | appfit_counts.py | `python3 appfit_counts.py > out_appfit_counts.txt` | pass |  |
| 42 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 42 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | base packets as reviewed (d307721 redrew them); bonus current |
| 42 | check_math.py | `python3 check_math.py` | pass; updated | reworded phrases located in the archived guide |
| 43 | extract.py | `python3 extract.py` | pass; re-pointed | reads common.PDFS (archived); reference-copy hashes on DELIVERED |
| 43 | check_base.py | `python3 extract.py && python3 check_base.py` | pass; re-pointed | base packets and guide as reviewed (6cd8fe9, 3b64f1a, 599c24a); the "The27-story" typo is fixed in the current guide |
| 43 | check_bonus.py | `python3 extract.py && python3 check_bonus.py` | pass |  |
| 43 | common.py | `python3 extract.py && python3 common.py` | pass |  |
| 44 | extract.py | `python3 extract.py > out_extract.txt` | pass |  |
| 44 | appfit_check.py | `python3 extract.py && python3 appfit_check.py` | pass |  |
| 44 | check.py | `python3 extract.py && python3 check.py > out_check.txt` | pass; updated | P3 page 10 rows of 4 (142693b); bonus marks start at 1 (3e5ac6e, W44-BONUS-v2) |
| 44 | check_critic_fixes.py | `python3 extract.py && python3 check_critic_fixes.py` | pass |  |
| 45 | pdf_extract.py | `python3 pdf_extract.py` | pass; re-pointed | common.PDFS = copies as reviewed; DELIVERED for reference hashes |
| 45 | check_appfit.py | `python3 pdf_extract.py && python3 check_appfit.py > check_appfit.out` | pass |  |
| 45 | check_base.py | `python3 pdf_extract.py && python3 check_base.py` | pass; re-pointed | via common.PDFS (copies as reviewed; de045a5, aa01c74) |
| 45 | check_bonus.py | `python3 pdf_extract.py && python3 check_bonus.py` | pass; finding paired | "322=12" confirmed on the archived bonus guide; current "3 x 2 x 2 = 12" (de045a5) |
| 45 | check_card_shoulds.py | `python3 pdf_extract.py && python3 check_card_shoulds.py > out_check_card_shoulds.txt` | pass |  |
| 45 | check_critic_fixes.py | `python3 pdf_extract.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 46 | extract_diagrams.py | `python3 extract_diagrams.py > extract_diagrams.out` | pass; re-pointed | common.PDFS and reviewed TeX from the archived ZIP (5c127cb) |
| 46 | check_base.py | `python3 extract_diagrams.py && python3 check_base.py > check_base.out` | pass; re-pointed | via common.PDFS and TEX (5c127cb) |
| 46 | check_bonus.py | `python3 extract_diagrams.py && python3 check_bonus.py > check_bonus.out` | pass; re-pointed | via common.PDFS (the bonus is unchanged) |
| 46 | check_card_shoulds.py | `python3 extract_diagrams.py && python3 check_card_shoulds.py > out_check_card_shoulds.txt` | pass |  |
| 46 | check_critic_fixes.py | `python3 extract_diagrams.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 47 | pdf_extract.py | `python3 pdf_extract.py` | pass; re-pointed | common.PDFS archived; DELIVERED for reference hashes |
| 47 | card_checks.py | `python3 pdf_extract.py && python3 card_checks.py > card_checks.out` | pass |  |
| 47 | check_base.py | `python3 pdf_extract.py && python3 check_base.py` | pass; finding paired | forcing-example finding confirmed on the archive; fixed by K-1 P7's own board (34e1dae) |
| 47 | check_bonus.py | `python3 pdf_extract.py && python3 check_bonus.py` | pass; re-pointed | via common.PDFS (34e1dae, 98601c9, 55acd79) |
| 47 | check_bonus_fixes.py | `python3 pdf_extract.py && python3 check_bonus_fixes.py > out_check_bonus_fixes.txt` | pass |  |
| 47 | check_card_shoulds.py | `python3 pdf_extract.py && python3 check_card_shoulds.py > out_check_card_shoulds.txt` | pass |  |
| 47 | check_critic_fixes.py | `python3 pdf_extract.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 47 | compare_source.py | `python3 pdf_extract.py && python3 compare_source.py` | pass; re-pointed | reviewed TeX from the archived ZIP; bonus ring moved (98601c9) |
| 48 | pdf_extract.py | `python3 pdf_extract.py` | pass; re-pointed | via common.PDFS; reference hashes on DELIVERED |
| 48 | card_checks.py | `python3 pdf_extract.py && python3 card_checks.py > card_checks.out` | pass |  |
| 48 | check_base.py | `python3 pdf_extract.py && python3 check_base.py` | pass; finding paired | 2 findings confirmed on the reviewed guide; current guide: 48 small tiles, "Up to eight could change this way" |
| 48 | check_bonus.py | `python3 pdf_extract.py && python3 check_bonus.py` | pass; finding paired | labelled witness grids confirmed on the reviewed bonus; current bonus v2 captions both grids "Pair:" |
| 48 | check_bonus_fixes.py | `python3 pdf_extract.py && python3 check_bonus_fixes.py > out_check_bonus_fixes.txt` | pass |  |
| 48 | check_critic_fixes.py | `python3 pdf_extract.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 48 | compare_source.py | `python3 pdf_extract.py && python3 compare_source.py` | pass; re-pointed | reviewed TeX (archived ZIP) against the reviewed PDFs; reference hashes on DELIVERED |
| 49 | pdf_extract.py | `python3 pdf_extract.py` | pass |  |
| 49 | check_base.py | `python3 pdf_extract.py && python3 check_base.py` | pass; finding paired | base PDFs from archive-before-card-fixes (6f116d5); should 1 confirmed there, current rings (0,2,1,4),(0,1,4,2) last 4 moves |
| 49 | check_bonus.py | `python3 pdf_extract.py && python3 check_bonus.py` | pass |  |
| 49 | check_bonus_fixes.py | `python3 pdf_extract.py && python3 check_bonus_fixes.py > out_check_bonus_fixes.txt` | pass |  |
| 49 | common.py | `python3 pdf_extract.py && python3 common.py` | pass |  |
| 50 | check_card.py | `python3 check_card.py` | pass |  |
| 50 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass |  |
| 50 | check_diagrams.py | `python3 check_diagrams.py` | pass |  |
| 50 | check_math.py | `python3 check_math.py` | pass |  |
| 51 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | base packets from archive-before-card-fixes; bonus and reference hashes current |
| 51 | check_math.py | `python3 check_math.py` | pass |  |
| 52 | check_card_fixes.py | `python3 check_card_fixes.py` | pass |  |
| 52 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass |  |
| 52 | check_diagrams.py | `python3 check_diagrams.py` | pass; updated | P14 has two blank 4x4 boards (c1f3431) |
| 52 | check_math.py | `python3 check_math.py` | pass |  |
| 53 | pdfgeom.py | `python3 pdfgeom.py` | pass |  |
| 53 | check_card_fixes.py | `python3 pdfgeom.py && python3 check_card_fixes.py` | pass |  |
| 53 | check_diagrams.py | `python3 pdfgeom.py && python3 check_diagrams.py` | pass; re-pointed | archived PDF and networks.json from the archived ZIP (problem-file conversion removed it) |
| 53 | check_label_fix.py | `python3 pdfgeom.py && python3 check_label_fix.py` | pass |  |
| 53 | check_math.py | `python3 pdfgeom.py && python3 check_math.py` | pass |  |
| 54 | pdfgeom.py | `python3 pdfgeom.py` | pass |  |
| 54 | check_diagrams.py | `python3 pdfgeom.py && python3 check_diagrams.py > out_check_diagrams.txt` | pass |  |
| 54 | check_guide_text.py | `python3 pdfgeom.py && python3 check_guide_text.py > out_check_guide_text.txt` | pass |  |
| 54 | check_math.py | `python3 pdfgeom.py && python3 check_math.py > out_check_math.txt` | pass |  |
| 55 | check_diagrams.py | `python3 check_diagrams.py` | pass; finding paired | draw-order finding confirmed on the archived p. 8; current dots clean (could 3, 79172d1) |
| 55 | check_math.py | `python3 check_math.py` | pass; updated | TeX from problem files; rule wording paired; K-1 route adult-led (guide p. 2) |
| 56 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass |  |
| 56 | check_diagrams.py | `python3 check_diagrams.py` | pass; updated | students.tex from problem files; materials in editable/student/; headers K-5 (84e3253); footer N56-S-v4 (7e78880) |
| 56 | check_k1_route.py | `python3 check_k1_route.py` | pass |  |
| 56 | check_math.py | `python3 check_math.py` | pass |  |
| 56 | check_nets.py | `python3 check_nets.py` | pass; updated | net sources moved to editable/student/ |
| 57 | check_diagrams.py | `python3 check_diagrams.py` | pass |  |
| 57 | check_math.py | `python3 check_math.py` | pass; updated | guide prints the P5 sum as 3/5+24/5+3/5 = 6 (bc1b3ee); long (about 4 min) |
| 58 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 58 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (materials pages rebuilt) |
| 58 | check_math.py | `python3 check_math.py` | pass; finding paired | PDFs and sources as reviewed (6ea89c0 rebuilt the strips); Visit A tie finding paired |
| 59 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 59 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | via w59common (226e7eb, 94ea196); check_critic_fixes.py covers current |
| 59 | check_math.py | `python3 check_math.py` | pass; re-pointed | via w59common (student and guide as reviewed) |
| 60 | card-appfit-check.py | `python3 card-appfit-check.py` | pass |  |
| 60 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 60 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | via w60common (c27d1c5, daea5a2) |
| 60 | check_math.py | `python3 check_math.py` | pass; finding paired | only-tie claim and "15 purple trapezoids" confirmed on the reviewed guide; current guide checked |
| 61 | extract.py | `python3 extract.py > out_extract.txt` | pass |  |
| 61 | check_card_fixes.py | `python3 extract.py && python3 check_card_fixes.py` | pass |  |
| 61 | check_critic_fixes.py | `python3 extract.py && python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 61 | check_diagrams.py | `python3 extract.py && python3 check_diagrams.py > out_check_diagrams.txt` | pass; updated | p. 5 example is a 70-70-70 triangle (3e0a91b should 5) |
| 61 | check_math.py | `python3 extract.py && python3 check_math.py > out_check_math.txt` | pass |  |
| 62 | extract.py | `python3 extract.py` | pass |  |
| 62 | check.py | `python3 extract.py && python3 check.py` | pass |  |
| 62 | check_card_fixes.py | `python3 extract.py && python3 check_card_fixes.py` | pass |  |
| 62 | compare_source.py | `python3 extract.py && python3 compare_source.py` | pass |  |
| 63 | check_diagrams.py | `python3 check_diagrams.py` | pass |  |
| 63 | check_k1_route.py | `python3 check_k1_route.py` | pass |  |
| 63 | check_math.py | `python3 check_math.py` | pass |  |
| 64 | check_card_fixes.py | `python3 check_card_fixes.py` | pass |  |
| 64 | geom64.py | `python3 geom64.py` | pass |  |
| 64 | math64.py | `python3 math64.py` | pass |  |
| 65 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 65 | check_math.py | `python3 check_math.py` | pass |  |
| 65 | check_pdf.py | `python3 check_pdf.py` | pass; updated | footer W65-S-v4 (385be6b); five packets of 7 pages (43a1008) |
| 66 | check_diagrams.py | `python3 check_diagrams.py > check_diagrams.py.out` | pass |  |
| 66 | check_math.py | `python3 check_math.py > check_math.py.out` | pass |  |
| 67 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 67 | check_math67.py | `python3 check_math67.py > check_math67.out` | pass; re-pointed | pdfgraph67.py names the archived copies (f877598, 04f2054) |
| 68 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass |  |
| 68 | check_diagrams.py | `python3 check_diagrams.py` | pass |  |
| 68 | check_math.py | `python3 check_math.py` | pass |  |
| 69 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 69 | check_pdf_diagrams.py | `python3 check_pdf_diagrams.py > check_pdf_diagrams.py.out` | pass |  |
| 69 | check_week69.py | `python3 check_week69.py > check_week69.py.out` | pass; re-pointed | TeX as reviewed from source/archive-before-intro-followup/week-69-source.zip |
| 70 | check_critic_fixes.py | `python3 check_critic_fixes.py > out_check_critic_fixes.txt` | pass |  |
| 70 | check_week70.py | `python3 check_week70.py` | pass; re-pointed | students.tex as reviewed from the pre-conversion ZIP (e8e24b1, 5ee7a5a) |
| 71 | check_card_fixes.py | `python3 check_card_fixes.py` | pass |  |
| 71 | check_week71.py | `python3 check_week71.py > check_week71.py.out` | pass; updated | window macros from the problem-file LaTeX (b882c12); output unchanged |
| 72 | check_card_fixes.py | `python3 check_card_fixes.py` | pass |  |
| 72 | check_diagrams.py | `python3 check_diagrams.py > check_diagrams.py.out` | pass; updated | P3 fifth board, the 2-by-2 square (f21adb9) |
| 72 | check_math.py | `python3 check_math.py > check_math.py.out` | pass |  |
| 73 | check_card_fixes.py | `python3 check_card_fixes.py` | pass |  |
| 73 | check_diagrams.py | `python3 check_diagrams.py` | pass; updated | P5 second target 8 by 1 (a21e008) |
| 73 | check_math.py | `python3 check_math.py` | pass |  |
| 74 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (b49dd73, dd839c9) |
| 74 | check_math.py | `python3 check_math.py` | pass; re-pointed | as check_diagrams.py |
| 75 | check_week75.py | `python3 check_week75.py` | pass |  |
| 76 | check_math.py | `python3 check_math.py` | pass; re-pointed | archived PDFs and students.tex (c06e3cc, 5629111, 42f72b9) |
| 77 | check_diagrams.py | `python3 check_diagrams.py` | pass; updated | written for an F77-45-v1 never committed; now checks the current 6-page F77-45-v4 |
| 77 | check_math.py | `python3 check_math.py` | pass; re-pointed | students.tex and guide as first committed (F77-45-v2) |
| 78 | check_diagrams.py | `python3 check_diagrams.py` | pass; updated | written for an F78-S-v1 never committed; checks current F78-S-v3 (d9f7472) |
| 78 | check_math.py | `python3 check_math.py` | pass |  |
| 79 | card2_chosen_moves.py | `python3 card2_chosen_moves.py > card2_chosen_moves.py.out` | pass |  |
| 79 | card_choose_move.py | `python3 card_choose_move.py > card_choose_move.py.out` | pass |  |
| 79 | card_targets.py | `python3 card_targets.py > card_targets.py.out` | pass |  |
| 79 | check_diagrams.py | `python3 check_diagrams.py` | pass; finding paired | reads the organizer-approved archive; checks the corrected "Problem 5, smallest-card rule" in the current guide |
| 79 | check_math.py | `python3 check_math.py` | pass |  |
| 80 | card_checks.py | `python3 card_checks.py > card_checks.py.out` | pass |  |
| 80 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (bad980d, 65fb9bc) |
| 80 | check_math.py | `python3 check_math.py` | pass; re-pointed | reviewed students.tex of Weeks 80 and 79 (a7cb913) |
| 81 | card_appfit.py | `python3 card_appfit.py > card_appfit.py.out` | pass |  |
| 81 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (dddd8f3, 810b365, 49c93a9) |
| 81 | check_math.py | `python3 check_math.py` | pass; re-pointed | reviewed students.tex |
| 82 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | reviewed W82-Q-draft-v1 (e8ee578, abf6c2f) |
| 82 | check_math.py | `python3 check_math.py` | pass |  |
| 83 | card_checks.py | `python3 card_checks.py > card_checks.py.out` | pass |  |
| 83 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (8e59b53, ff74daa) |
| 83 | check_math.py | `python3 check_math.py` | pass; re-pointed | reviewed students.tex |
| 83 | check_rebuild.py | `python3 check_rebuild.py` | pass; re-pointed | rebuilds the reviewed TeX from the archived ZIP against the archived PDFs |
| 84 | pdf_extract.py | `python3 pdf_extract.py` | pass; re-pointed | via common.PDFS (archive-before-card-fixes) |
| 84 | check_math.py | `python3 pdf_extract.py && python3 check_math.py` | pass; finding paired | PDFs as reviewed (3c1af9b, f9d1bc1); reply-card shortfall paired with the current guide sentence |
| 84 | second_card_checks.py | `python3 pdf_extract.py && python3 second_card_checks.py > second_card_checks.py.out` | pass |  |
| 85 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass |  |
| 85 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | reviewed PDFs, generate.py and TeX (2d9c473, 48976ba, bc8c507); current print copies vs reference-pdfs |
| 85 | check_math.py | `python3 check_math.py` | pass; re-pointed | reviewed generate.py |
| 86 | card_arms.py | `python3 card_arms.py > card_arms.py.out` | pass |  |
| 86 | card_spot.py | `python3 card_spot.py > card_spot.py.out` | pass |  |
| 86 | check_math.py | `python3 check_math.py` | pass | long (over 10 min) |
| 86 | check_pdf.py | `python3 check_pdf.py` | pass; re-pointed | archive-before-card-fixes (69e8099, dfbc5e4) |
| 87 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (79d58c1, dfbc5e4) |
| 87 | check_math.py | `python3 check_math.py` | pass |  |
| 88 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (5180cb7, 7cd6bda, dfbc5e4) |
| 88 | check_math.py | `python3 check_math.py` | pass; re-pointed | reviewed TeX from the archived ZIP |
| 88 | check_packing.py | `python3 check_packing.py` | pass |  |
| 89 | card_appfit.py | `python3 card_appfit.py > card_appfit.py.out` | pass |  |
| 89 | check_diagrams.py | `python3 check_diagrams.py > check_diagrams.py.out` | pass; re-pointed | pages and guide from archive-before-card-fixes (37507d4, dfbc5e4); cube-pile checks read the current students.tex |
| 89 | check_math.py | `python3 check_math.py > check_math.py.out` | pass |  |
| 90 | check_math.py | `python3 check_math.py` | pass |  |
| 90 | check_scale.py | `python3 check_scale.py` | pass |  |
| 91 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (c619ef2, dfbc5e4) |
| 91 | check_math.py | `python3 check_math.py` | pass |  |
| 92 | check_diagrams.py | `python3 check_diagrams.py` | pass |  |
| 92 | check_math.py | `python3 check_math.py` | pass |  |
| 93 | check_math93.py | `python3 check_math93.py` | pass; re-pointed | via repo_path.py (archived copies) |
| 93 | check_pdf93.py | `python3 check_pdf93.py > check_pdf93.out` | pass; re-pointed | repo_path.py names the archived copies; reviewed guide TeX from the ZIP (215e5ae, 2aa59b1) |
| 93 | rebuild_compare.py | `python3 rebuild_compare.py > rebuild_compare.out` | pass; re-pointed | rebuilds the archived reviewed ZIP against the archived PDFs |
| 94 | check_math.py | `python3 check_math.py` | pass; re-pointed | reviewed TeX from the archived ZIP, PDFs from archive-before-card-fixes (c23f192, a4b598d, a10728d, f192b3c) |
| 94 | rebuild_compare.py | `python3 rebuild_compare.py` | pass; re-pointed | rebuilds the archived ZIP (source/week-94/build.py moved) and now exits 1 on a missing rebuild; it had passed silently with nothing rebuilt |
| 95 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (1e29ee4, dfbc5e4); review/check_card_fixes_2026_10_23.py covers current |
| 95 | check_math.py | `python3 check_math.py` | pass |  |
| 96 | check_diagrams.py | `python3 check_diagrams.py` | pass |  |
| 96 | check_math.py | `python3 check_math.py` | pass |  |
| 97 | card_checks.py | `python3 card_checks.py > card_checks.py.out` | pass |  |
| 97 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archived PDFs; rebuild from the pre-conversion ZIP (c3f3bbb, dfbc5e4, 842a570) |
| 97 | check_math.py | `python3 check_math.py` | pass |  |
| 98 | card_appfit.py | `python3 card_appfit.py > card_appfit.py.out` | pass |  |
| 98 | card_appfit2.py | `python3 card_appfit2.py > card_appfit2.py.out` | pass |  |
| 98 | card_appfit3.py | `python3 card_appfit3.py > card_appfit3.py.out` | pass |  |
| 98 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass; re-pointed | checks the v3 critic version in archive-before-small-coulds (6c3e6ba made the guide v4) |
| 98 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archive-before-card-fixes (b3ad940, 27b8dd5, 6c3e6ba) |
| 98 | check_math.py | `python3 check_math.py` | pass |  |
| 99 | card_checks.py | `python3 card_checks.py > card_checks.py.out` | pass |  |
| 99 | check_diagrams.py | `python3 check_diagrams.py` | pass; re-pointed | archived PDFs and per-page TeX (0842f62 removed them; 8a555d1, f9d1bc1) |
| 99 | check_math.py | `python3 check_math.py` | pass |  |
| 100 | check_critic_fixes.py | `python3 check_critic_fixes.py` | pass |  |
| 100 | check_diagrams.py | `python3 check_diagrams.py` | pass; finding paired | sentences the card fixes rewrote are located in the archived guide/packet |
| 100 | check_math.py | `python3 check_math.py` | pass | long |
| bonus-labels | check_bonus_labels.py | `python3 check_bonus_labels.py > check_bonus_labels.out` | pass; updated | Week 44's label-fix copy is read from archive-before-small-coulds (its bonus guide is v4 since 3e5ac6e) |
| critic-j | check_critic_j.py | `python3 check_critic_j.py` | pass |  |
| critic-m | check_critic_m.py | `python3 check_critic_m.py` | pass |  |
| roster-labels | check_roster_labels.py | `python3 check_roster_labels.py` | pass |  |

## Package verifiers

The package's own dated verifiers (`*2026_10_23*`, card, critic and guide-copy checks) for the weeks revised on October 23, run from the repository root. 80 pass. 14 read a fresh build in `editable/build/` (or `editable/*.pdf`) and need the package build first. That build was not run here, so they are not counted as failures.

| Verifier | Command | Status | Note |
|---|---|---|---|
| week-100/checks/card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-100/checks/card_fixes_2026_10_23.py` | pass |  |
| week-11/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-11/check_guide_copy.py` | pass |  |
| week-12/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-12/check_guide_copy.py` | pass |  |
| week-12/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-12/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-12/editable/review/verify_student_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-12/editable/review/verify_student_fixes_2026_10_23.py` | pass |  |
| week-13/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-13/check_guide_copy.py` | pass |  |
| week-14/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-14/check_guide_copy.py` | pass |  |
| week-16/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-16/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-17/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-17/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-18/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-18/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-19/editable/review/check_card_fixes.py | `python3 lowell-math-circle-year-2/source/week-19/editable/review/check_card_fixes.py` | pass |  |
| week-20/editable/review/check_card_fixes.py | `python3 lowell-math-circle-year-2/source/week-20/editable/review/check_card_fixes.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-21/editable/review/check_card_fixes.py | `python3 lowell-math-circle-year-2/source/week-21/editable/review/check_card_fixes.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-22-bonus/review/verify_card_fix_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-22-bonus/review/verify_card_fix_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-22/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-22/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-23/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-23/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-23/editable/review/verify_sorts_rule_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-23/editable/review/verify_sorts_rule_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-24/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-24/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-25/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-25/check_guide_copy.py` | pass |  |
| week-25/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-25/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-25/editable/review/verify_small_coulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-25/editable/review/verify_small_coulds_2026_10_23.py` | pass |  |
| week-25/editable/review/verify_student_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-25/editable/review/verify_student_fixes_2026_10_23.py` | pass |  |
| week-26/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-26/check_guide_copy.py` | pass |  |
| week-26/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-26/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-26/editable/review/verify_student_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-26/editable/review/verify_student_fixes_2026_10_23.py` | pass |  |
| week-27/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-27/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-28/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-28/check_guide_copy.py` | pass |  |
| week-29/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-29/check_guide_copy.py` | pass |  |
| week-29/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-29/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-29/editable/review/verify_student_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-29/editable/review/verify_student_fixes_2026_10_23.py` | pass |  |
| week-30/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-30/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-31/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-31/check_guide_copy.py` | pass |  |
| week-31/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-31/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-31/editable/review/verify_student_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-31/editable/review/verify_student_fixes_2026_10_23.py` | pass |  |
| week-35/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-35/editable/review/verify_card_fixes_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-35/editable/review/verify_critic_coulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-35/editable/review/verify_critic_coulds_2026_10_23.py` | needs a build | reads a fresh build (run the package build first); not a packet failure |
| week-36/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-36/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-37/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-37/check_guide_copy.py` | pass |  |
| week-38/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-38/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-39/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-39/check_guide_copy.py` | pass |  |
| week-39/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-39/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-39/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-39/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-40/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-40/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-41/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-41/check_guide_copy.py` | pass |  |
| week-41/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-41/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-42/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-42/check_guide_copy.py` | pass |  |
| week-42/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-42/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-43/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-43/check_guide_copy.py` | pass |  |
| week-43/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-43/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-43/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-43/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-44/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-44/check_guide_copy.py` | pass |  |
| week-44/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-44/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-45/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-45/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-46/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-46/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-47/editable/review/verify_card_shoulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-47/editable/review/verify_card_shoulds_2026_10_23.py` | pass |  |
| week-48/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-48/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-49/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-49/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-50/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-50/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-51/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-51/check_guide_copy.py` | pass |  |
| week-51/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-51/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-54/editable/review/check_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-54/editable/review/check_card_fixes_2026_10_23.py` | pass |  |
| week-55/editable/review/check_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-55/editable/review/check_card_fixes_2026_10_23.py` | pass |  |
| week-57/editable/review/check_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-57/editable/review/check_card_fixes_2026_10_23.py` | pass |  |
| week-65/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-65/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-66/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-66/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-67/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-67/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-74/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-74/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-75/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-75/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-75/editable/review/verify_minus_signs_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-75/editable/review/verify_minus_signs_2026_10_23.py` | pass |  |
| week-76/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-76/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-77/editable/checks/baseline_check.py | `python3 lowell-math-circle-year-2/source/week-77/editable/checks/baseline_check.py` | pass |  |
| week-77/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-77/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-78/checks/check_card_fixes.py | `python3 lowell-math-circle-year-2/source/week-78/checks/check_card_fixes.py` | pass |  |
| week-80/editable/check_card_fixes.py | `python3 lowell-math-circle-year-2/source/week-80/editable/check_card_fixes.py` | pass |  |
| week-81/editable/check_card_fixes.py | `python3 lowell-math-circle-year-2/source/week-81/editable/check_card_fixes.py` | pass |  |
| week-82/editable/check_card_fixes.py | `python3 lowell-math-circle-year-2/source/week-82/editable/check_card_fixes.py` | pass |  |
| week-86/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-86/check_guide_copy.py` | pass |  |
| week-86/editable/review/check_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-86/editable/review/check_card_fixes_2026_10_23.py` | pass |  |
| week-87/check_guide_copy.py | `python3 lowell-math-circle-year-2/source/week-87/check_guide_copy.py` | pass |  |
| week-87/editable/review/check_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-87/editable/review/check_card_fixes_2026_10_23.py` | pass |  |
| week-88/editable/review/check_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-88/editable/review/check_card_fixes_2026_10_23.py` | pass |  |
| week-88/editable/review/check_ring_rule_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-88/editable/review/check_ring_rule_2026_10_23.py` | pass |  |
| week-89/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-89/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-90/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-90/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-91/editable/review/verify_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-91/editable/review/verify_card_fixes_2026_10_23.py` | pass |  |
| week-95/review/check_card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-95/review/check_card_fixes_2026_10_23.py` | pass |  |
| week-96/checks/card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-96/checks/card_fixes_2026_10_23.py` | pass |  |
| week-97/checks/card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-97/checks/card_fixes_2026_10_23.py` | pass |  |
| week-98/checks/card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-98/checks/card_fixes_2026_10_23.py` | pass |  |
| week-98/checks/small_coulds_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-98/checks/small_coulds_2026_10_23.py` | pass |  |
| week-99/checks/card_fixes_2026_10_23.py | `python3 lowell-math-circle-year-2/source/week-99/checks/card_fixes_2026_10_23.py` | pass |  |
| week-77/editable/checks/baseline_check.py | `cd lowell-math-circle-year-2/source/week-77/editable && python3 checks/baseline_check.py` | pass | an unchanged copy of the original review, hard-coded to the pre-fix Problems 1-5 by design |
| week-77/editable/checks/independent_check.py | `cd lowell-math-circle-year-2/source/week-77/editable && python3 checks/independent_check.py --source-dir student --verify-only --pdf ../../../week-77/week-77-students.pdf` | pass | |
| week-94 K-1 critic (plans/review/checks/week-94/k1-critic-2026-10-23/scripts/k1_check.py) | `python3 plans/review/checks/week-94/k1-critic-2026-10-23/scripts/k1_check.py lowell-math-circle-year-2/source/week-94/problems` | pass | output identical to k1_check.out on the current problem files |
