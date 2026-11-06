This is the preserved reviser report from [checkpoint 24a18cb0](https://github.com/jamesrp/math-circle-worksheets/blob/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-98-v1/reviser-report.md). Its inline `final/` paths and stage-status statements describe that historical run; live Markdown links below point to this package where applicable. The packaged guide is [k1-guide.pdf](k1-guide.pdf), its portable source is [guide-src/](guide-src/), and packaging checks are in [the packaging report](../../guide-packaging.md). Original writer/critic scripts, rendered-check records and other run evidence remain at [the pinned run](https://github.com/jamesrp/math-circle-worksheets/tree/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-98-v1/). Existing companion-guide changes mentioned below remain **future work after organizer approval**; none is implemented here.

---

# Week 98 K–1 guide revision

**Revisions ready; packaging deferred.** `final/k1-guide.pdf` is **5 US Letter pages**, identifier `W98-K-FAC-v2`. The source and portable checker are in `final/src/`; `final/verification.json` records hashes and checks. All **6 should-fix and 10 minor findings are addressed**; none was declined. No must-fix was reported. Original draft, writer report, independent review and review-check evidence are preserved. Student pages, existing guides, catalog and packaged draft folders are unchanged.

The extra page keeps the enlarged theorem-first overview, worked removal demonstration and complete adult keys at readable 11-point type; no text or table is stranded on a spill page. The section remains **untested with children and physically unrehearsed**.

## Finding dispositions

Numbers refer to the preserved `review-guide.md`.

| Finding | Revision and evidence |
|---|---|
| Should 1 | The opening now states the strip minimum for L≥2, the general rectangle fence lower bound and attained 3,3,4 values for the printed two-wide boards. It gives the four-middle-edge versus three-diagonal counterexample and P9's 3/4 endings before any key. The assumptions and proof limits remain explicit. |
| Should 2 | P6 now derives L≤2s−1 from s seeds and at most s−1 single gaps, forcing the stated 2,3,3,4 minima. The checker verifies these inequalities and exhausts every strip start as well as every optimal start. |
| Should 3 | Removed the unused optional twenty fence sticks per pair from this route's preparation list. The fence argument stays as adult background. The parent need not cut forty strips for an undescribed activity; the five-minute estimate now covers counters and the launch record/copy only. |
| Should 4 | Added a one-minute non-task return-visit removal demonstration, with three matching board pictures. Add a fourth seed at top right to the shared 2×3 start and fill it; clear growth, lift that seed and grow to a four-square stop; clear growth and restore the seed. The new checker asserts fill, stop and exact reset. It does not demonstrate the alternative removal that would answer P7. |
| Should 5 | P9 uses the visible seed-color counters as its current start, bare dots for removed seeds, and only the two endings on the two printed record boards. Children pool endings rather than running seed sketches. |
| Should 6 | The opening insertion note now names the p1 “No K–1 packet is claimed…” sentence and p2 “Per pair” and “Staffing” additions (one adult, two pairs, 6+20 counters per pair), alongside the exact replaced adult-led route. These are later integration instructions only. |
| Minor 1 | Corrected P2's middle-row explanation: each empty square touches one counter by a side and one or two at corners. |
| Minor 2 | Added the operational sign of an “exactly two” misreading: refusal of three/four neighbors, with P8's full starts then failing to fill. |
| Minor 3 | More-than-six seed guesses may be drawn on a record board. Running out of counters remains distinct from being stuck. |
| Minor 4 | Adult writes a child's P4/P5 guess beside the problem number before the hunt. |
| Minor 5 | Added all 14 three-seed fills on 3×3 in four families (2+4+4+4), and noted that straight rows/columns are stuck. The checker constructs the four rotated families and proves their union equals the complete optimal enumeration. |
| Minor 6 | P8's four full grows and fifteen deletion tests are split between the two pairs; reading-order tests avoid omissions, and ring totals 1,4,2,0 support comparison. |
| Minor 7 | Removed the board-letter process residue; simplified turned-copy wording and the growth-order question. Print note names eventual `week-98-k-1.pdf` as well as today's draft, without claiming it already exists. |
| Minor 8 | Removed repeated unsuccessful-search and one-board-at-a-time cautions, and generic celebration. Retained “let the child choose whether to seek fewer.” The overview now says “A few failed attempts…” to distinguish casual trials from a complete finite catalog. |
| Minor 9 | Bring the whole-group 2×3 board to K–1; if fixed to a whiteboard, draw a 30 mm-square copy. |
| Minor 10 | Close the first hour by asking for the next square-size prediction and save that conjecture for another visit. |

## Actual student pages, materials and mathematics

Read and rendered all **nine W98-K-v1 student pages**, all **five W98-FAC-v4 base-guide pages**, and the four-page writer guide. Poppler final renders confirm the page and board checks independently of text extraction. P1–P9 each occupy their matching student page. The original independent review's vector board parser was rerun on the current PDF; its geometry, seed locations, working/record classification and dimensions exactly reproduce the preserved `pages.json`.

The boards are: P1 2×2 with six records; P2 four 3×3 starts; P3–5 3×3,4×4,5×5; P6 lengths 3–6; P7 upright 3×2,4×2,5×2; P8 the L, corners, three-corners-and-center and middle-edge starts; P9 the top-row/left-column start with two record boards. Working squares are 30 mm, records 15–16 mm. Flat counters at most 25 mm leave grid lines visible. Per pair 6 seed +20 growth counters, table totals 12+40, serve one board at a time; five seeds plus twenty growth fill the largest board. No separate materials PDF prints these counters or the launch board. No unused stick kit remains.

All numerical keys are unchanged. `final/src/check_guide.py` checks:

- The exact student PDF hash, all nine problem/page labels and corrected “two or more” rule.
- P1's complete six starts/two diagonal fills; P2's 4,3,6,9 finishes.
- Complete minimum searches for 3×3,4×4,5×5 (3,4,5 seeds; 14,130,1615 optimal fillers), including every smaller start. It additionally verifies the newly printed four-family 14-start classification and six stuck rows/columns.
- Every strip start, exact optimal lists and the new strip lower-bound inequalities; P7's 3,3,4 minima and 10,8,48 optimal-start counts, with every displayed witness.
- All fifteen P8 deletions and P9's full removal tree with exactly the 3- and 4-seed endings.
- Every completed legal order and legal perimeter change on all 512 states of 3×3. These finite computations support the examples; the overview's arguments establish the general facts.
- Original launch, new non-task removal demonstration and exact restoration; kit arithmetic, physical dimensions and timing sum.

## Build, visual QA and clean rebuild

`bash final/src/build.sh` succeeds with real pdfLaTeX, ending with the checker. A separately retained TeX log contains **no errors, warnings or overfull boxes**. The guide has five Letter pages and repeated matching header/footer identifiers. Every final page was rendered with Poppler and inspected individually: type and math symbols are legible, all tables and both three-panel demonstrations are complete, and margins/footers have no clipping or overlap. Page 1 was re-rendered and reinspected after the last wording change; unchanged pages 2–5 retain their inspected output.

A new outside-repository `/tmp` directory contained only `final/src/` and the unchanged student `k-1.pdf` beside it. `src/build.sh` and its checker passed there. **PDF bytes and `pdftotext -layout` output matched exactly.** No network, private reference, absolute build path, student author code or other repository file was needed. Local render/log evidence is under `/tmp/k1-98-reviser-qa`, not in the deliverable sources.

- Final guide SHA-256: `5cc535e08d9fd95a673442f0f2b7515d974c06d2463c682e4aa020071f9a596a`.
- Unchanged student SHA-256: `804470c9ad7a0b88c393dda83e8e510796e0da749db79bab402328f50565f86a`.

## Student-page issues and remaining limits

No student page was edited. The guide works around: outside squares not explicitly excluded on the page; counter capacity for whole-page loading and guesses above six; clearing growth before every removal; P1 counting positions; P4/P5 overlap with older packets; and the need to separate successful constructions, casual failed trials and complete impossibility arguments. The six-counter cap is operational, not a restriction on mathematical guesses. The page's P8 instruction means restore each tested seed, while P9 keeps successful deletions; both now have concrete preparation.

The existing base guide's stale K–1 overview/kit/staffing notes are named for later integration. Its older-band page-reference drift, already identified by the writer/critic, remains out of scope. No private book or external paper was newly consulted or claimed reread. The source's elementary growth/fence arguments and small-instance enumeration supply this bounded revision.

Digital checks do not establish real print size, counter fit, two-finger checking, reset reliability, adult staffing, pacing or classroom readiness. **All guides remain untested with children and physically unrehearsed. Packaging remains a separate follow-up.**
