# Digital verification

Status: final student revision and independent final student/guide pair review passed. Unpiloted, organizer review pending, physical preparation and handling untested.

- Fresh writer, adversarial critic, independent mathematics checker and reviser were distinct agents in separate checkouts. Reviews are retained in `plans/new-families-92-97/week-94/` in the repository.
- Independent standard-library checker covers every student problem: finite machine cases, all report repairs, strip placements, two-point uniqueness, counterexamples to unrestricted extrapolation, and exact bounded-error endpoints.
- Coordinator kernel checker additionally passed 3,888 exact affine identification and interval-endpoint checks.
- Final student files have 2/4/5 pages; facilitator guide has 5 pages. Every one of these 16 final pages was rendered and visually inspected. No overlaps, clipping, extraneous pages, or illegible labels found. All text bounding boxes stay on US Letter pages.
- Rulers, cutout strips and unit rows share 12 mm units digitally. This is not a physical print-fit test.
- The package builder rejects errors and overfull TeX boxes and writes build intermediates outside sources when `--work` is given.

- The independent integration reviewer inspected all 16 final pages, checked every student/guide answer and the general proofs, reran the independent checker, and measured the 12 mm PDF vector geometry. Verdict: PASS; see the repository's `plans/new-families-92-97/week-94/final-pair-review.md`.
- A clean extraction of `week-94-source.zip` rebuilt all four delivered PDFs byte for byte; hashes and page counts are in the repository's `plans/new-families-92-97/week-94/rebuild.json`.

No unverified remote upload or main integration is claimed here.

## October 23, 2026: review-card fixes (v2)

- K–1 Problems 4–6 (two new pages), Grades 2–3 Problem 2, Grades 4–5 page 3 and Problem 7, and the guide changed; footers are now W94-K-v2, W94-M-v2, W94-U-v2 and W94-F-v2. The packets now have 4/4/5 pages and the guide 6.
- `check_math.py` now checks the K–1 tower answers and the guide's stretch-3 and B + C = 7 claims.
- Every changed page was rendered at 80 dpi and inspected. Against the v1 builds, the other student pages are unchanged above the footer at 100 dpi. The published band views match the packets pixel for pixel.
- Cube handling, the cover game and timings are unrehearsed.

## October 23, 2026: independent critic of the new K–1 pages (K–1 v3, guide v3)

- A fresh critic agent reviewed K–1 Problems 4–6 and the guide's K–1 page with `worksheet-workflow/stages/critic.md` (the repository's `plans/review/checks/week-94/k1-critic-2026-10-23/`). It found no must and four shoulds, all fixed: the rule says a machine always adds the same extra and P5 says P and Q went into the same machine (read with separate extras, outputs 4 and 6 fit 9 pairs); the keeper's extra waits behind the cover as a cube stick and P4 ends by lifting the cover; the P4 table asks only for towers given and the extra found; the guide says children "may" ask for several towers. One-line coulds were also taken; drawn outputs in the P6 panels and larger cells are deferred.
- Footers are now W94-K-v3 and W94-F-v3; the Grades 2–3 and 4–5 packets are byte-identical to v2. K–1 pp. 1–2 and guide pp. 1 and 4–6 are unchanged above the footer; K–1 pp. 3–4 and guide pp. 2–3 were rendered at 80 dpi and inspected. `check_math.py` adds the 9-pair count for separate extras, and the critic's own check passes on v3.
