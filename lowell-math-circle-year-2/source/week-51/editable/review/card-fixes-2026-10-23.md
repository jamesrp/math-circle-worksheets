# Week 51: student-page fixes from the review card, October 23, 2026

The review card is `plans/review/week-51.md` in the project, with its math check `plans/review/week-51-math.md`. Its first must (the strip kit) was fixed earlier the same day; these fixes followed the problem-file conversion and were made in the problem files (`problem-files/problems/*.md`, `problem-files/figures.py`), the guide in `facilitator-src/content.json` and `facilitator-src/route-note.json`.

## What changed

- **Must (card fix 2), K–1 Problem 4, now Problem 6.** "Start at 0 and keep A unchanged within each comparison; B may vary separately." held A still in the bottom picture, where the key's gaps 1 and 5 need A = 4 and A = 6. It now reads "Start at 0. Both A's in the top picture are the same length. Each try may use new lengths." The guide key adds "The two extremes use different values of A, since each try may use new lengths."
- **Should (fix 3), all bands.** The gap page now comes before the shared-A page, so children meet the cross pairing (longest less shortest) alone before the bottom comparison needs it. K–1 Problems 5–6 become 4–5 and Problem 4 becomes 6; Grades 2–3 and 4–5 Problems 6–7 become 5–6 and Problem 5 becomes 7. The guide's keys are renumbered and reordered to match (gap keys on p. 2, shared and exact-total keys on p. 3), and the route note now gives K–1 P4–5, P6 and Grades 4–5 "after the dependency comparison in P7".
- **Should (fix 5), K–1 Problem 7 and Grades 2–3 Problem 8.** A's card is 3 to 7 units instead of 4 to 6, so A = 3 and A = 7 fail on B's card, and four boards are printed for the three pairs. The answers, (4,5), (5,4) and (6,3), are unchanged; the guide key says why 3 and 7 fail.
- **Should (fix 6), p. 1, all bands.** The launch picture drew the shortest and longest joins, which is older Problem 1's method, 2 mm right of the A + B ruler's 0. It now draws one join from the ruler's 0, A 2 and B 2, ending at 4 inside the band. The guide's launch asks for a shorter and a longer join.
- **Should (fix 7), K–1 Problem 3.** "Fitting within 9 includes ending at 9." is printed under the cards, as page 2 does for reaching 8.
- **Could (fix 9), K–1 Problem 5 (was 6).** Two rulers, one for each way to make a gap of 3; the prompt moved up to make room.
- **Could (fix 10), the shared-A page, all bands.** "One possible setting;" is cut; the line reads "The white pieces are exactly 4 and 1 units long."

- **Should (fix 8), guide p. 1, later the same day.** The "Flexible hour" planned about fifty minutes at the tables and two undescribed slots ("human strips", "exchange guarantees"). It now gives 0-5 arrival, 5-9 launch, 9-47 at the tables (P1-2 with partner tests, then P3, and P4 for older bands, or return pages), 47-53 sharing (each pair shows one guarantee and the two settings at its ends) and 53-60 reset, matching the group's 35 to 40 minutes at the tables. Only guide page 1 changed.

Deferred: should 4 (older Problem 6, the midpoint claim, which the two card runs agree repeats Problem 5's witnesses but would replace in different ways) and could 11 (simpler Grades 2–3 wording for "tightest guaranteed range", which would leave the phrase in Problem 7 and "neither bound" in Problem 5).

## Pages

- K–1: pp. 1 and 3–6 changed; p. 2 unchanged.
- Grades 2–3: pp. 1 and 4–6 changed. Pp. 2–3 have the same words and drawings, but this TeX Live breaks two lines without the old copies' hyphens ("reach-es", "with-in"), as recorded in `fresh-review-rebuild.md` for the old builder too.
- Grades 4–5: pp. 1 and 4–5 changed; pp. 2–3 as for Grades 2–3; p. 6 unchanged.
- Adult guide: all four pages (launch p. 1, reordered keys pp. 2–3, route note p. 4); the hour plan (fix 8) changed p. 1 again.
- The strip kit (`materials.pdf`) is unchanged: every changed build still uses whole lengths from one set.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` enumerates the changed problems on a quarter-unit grid (the launch join, K–1 Problem 3's card, the shared and separate gaps with A held at 5 for contrast, the two gaps of 3, the fill-9 pairs with A from 3 to 7). It then reads the reference PDFs: problem numbers and page order in every band, the new K–1 wording, no "One possible setting", the inclusive line, two 0–16 rulers under K–1 Problem 5, a launch join that starts at the ruler's 0 and ends at its 4 in every band, four 90 mm boards on the fill-9 pages, and the guide's labels, launch, fill-9 key and route note. Run on the earlier PDFs, it fails at the first page check.
- `materials/verify_materials.py` rebuilds every key's witnesses from one strip set, now including the printed launch join and A from 3 to 7.
- `problem-files/check_guide_copy.py` reports that every guide sentence and table row agrees with the problem files' keys.
- `facilitator-src/verify_pdfs.py` expected three guide pages, but the build appends the route note as a fourth, so `verify_math.py` failed on every clean build; it now expects four.
- The student packets built by the package match the problem-file tools' build in pages, text and 100-dpi pixels. Every changed page was rendered at 80 dpi and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify.py`, `verify_revision.py`, `verify_math.py` and this verifier. The student pixel allowances in `rebuild-pixel-allowances.json` are removed, since all three packets were rebuilt.

The theme remains unpiloted, and the changed pages have not been tried with strips on a table.
