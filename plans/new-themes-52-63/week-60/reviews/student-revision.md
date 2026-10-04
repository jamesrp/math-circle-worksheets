# Week 60 student revision v2

Fresh revision stage, October 4, 2026. Current review deliverable:
`students.pdf`, seven US Letter pages, Problems 1-9, footer `W60-S-v2`.
Editable sources are the six authored files in `src/`. The draft and both
reviews remain separate. No guide, workflow, other week, global index or remote
copy was edited. Physical handling and classroom piloting remain unperformed.

## Review disposition

| Review point | Revision/evidence |
|---|---|
| M1, both critics: counter timing | Page 1 now states the compulsory one-counter condition before "Remove one turn counter after deciding on each offer." The practice visual remains intact. Actual PDF text-order and simulated two-offer deadline checks pass. |
| L1: short Problem 2 bridge | Problem 2 now asks whether the same fixed rules can give opposite winners in two six-round matches, asks for possible offers for both, then asks whether either match settles the long-run average. This constructive sample task preserves open methods and consecutive numbering. Constant full-word offers give legal opposite samples for any fixed policies; independently checked. No supplied optimal strategy or extra calculation recipe was added. |
| L2: accessible page 6 route | `src/README.md` explicitly identifies pages 1-3 and 6 as the Grades 3-5 core; pages 4-5 and 7 are readiness-dependent/later visits. No proof-page completion gate. Actual bands retained on every final page. Separate guide author receives this route through source notes. |
| L3: score reuse and four-point difference | Complete recoverable words and one score line remain. README specifies scoring one plan, saving its labelled total, clearing all score areas, then scoring the other; shared sets and adult addition retain children's decisions. Physical card/eraser/overlay rehearsal remains an explicit outstanding pretest, not claimed solved by rendering. |
| L4: average arithmetic gate | README retains exact prerequisites, including fractions or equal-sized concrete batches on page 4 and fractional continuation values on page 7. A brief non-target average example is conditional on an unfamiliar prerequisite. Upper mathematical depth remains, without printing the target method. |
| Mathematical critic: retain global optimality/generalization | Problems 5,6,8,9 remain intact. Independent full history-policy audits cover two/three offers for all three bags; four-offer verification distinguishes 512 turn/current-score policies from the induction bounding every legal history policy. No all-2^39 enumeration claim. |

## Final verification

- Ran independently authored revision-stage `src/check_math.py`: all 8
  two-offer and 4,096 three-offer history policies per bag; Plan A/B totals
  130/134; optima 40,36,44 on the nine-word collections; 0/4/6 values
  10/3,40/9,134/27; 0/5/6 values 11/3,44/9,143/27,448/81; revised sample task;
  practice conventions; 125 bags including duplicate/negative tickets through
  six horizons. Evidence: `math-checks.json`, with theorem/scope in
  `src/mathematics.md`.
- Audited actual PDF paths/text: complete equally sized ordered collections
  9+27+9+9, including unseen tails; four-sided rectangular cards, nonoverlap;
  counter circles equal in both axes, diameter about 17.28 pt, two versus three.
  Pair cards about 154.80 x 63.36 pt; triples about 154.80 x 50.40 pt.
- Rendered and visually inspected **every final page 1-7** at 1.7 scale,
  including bands, practice input/intermediate/output visuals, cards, workspace,
  all headers/footers and page numbers. A non-deduplicated header/footer montage
  confirms regions omitted by repeated-image display. No clipping, overlaps or
  overfull TeX warnings. Evidence: `qa/render/`, `qa/headers-footers.png` and
  `qa/verification.json`.
- Built from a separate clean source copy and from a newly created/extracted
  six-file source ZIP. Both reproduce all seven pages' extracted text,
  dimensions and rendered pixels exactly. All build/render/ZIP intermediates
  stay outside `src/`. `build.py` rejects an output directory inside source.
- Lean sources contain only original LaTeX/TikZ, build/check scripts, README
  and mathematical notes. Precise Ferguson, organizer, Givental et al. and
  Rozhkovskaya provenance is stated; relevant local source passages were read.
  No prompt, style-exemplar block, book content, reference PDF or render is
  bundled. These precedents do not validate the adaptation or physical handling.

Remaining operational checks: actual mixing/display handling, irreversible
passes, counter enforcement, score reuse, role rotation, staffing and classroom
independence. They require a physical rehearsal and pilot; none was performed.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
