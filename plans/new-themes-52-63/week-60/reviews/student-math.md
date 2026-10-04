# Week 60 independent mathematical review

Reviewed October 4, 2026 in a fresh mathematical-review agent. Scope: the actual seven-page `draft/students.pdf`, its sources and source notes, `review.md`, the Week 60 research, `PROMPT.md`, `CRITIC-MATH.md`, project guidance and stage routing. No draft or prompt was edited.

**Verdict: the task mathematics, exact examples, enumerations and actual diagrams check out. Make the one shared-rule clarification below before release. Preserve the Grades 4–5 optimality and generalization tasks.**

## M1 — Counter timing can change the stopping horizon

**Location:** Grades 3–5, page 1, shared rules before Problems 1–2; these rules also govern the upper pages.

**Exact text:** “Remove one turn counter after each offer. With one counter left, you must take the offer, even if it is 0.”

**Evidence:** Start a two-offer round with two counters and reveal 0. If the partner removes a counter immediately after revealing the offer, there is now one left and the next sentence requires taking that same 0. The intended two-offer model permits passing this first 0 and makes only the second offer compulsory. Applied consistently, that reading collapses a two-offer round to one offer: the best expected score becomes `10/3`, rather than the independently enumerated `40/9`. The page-1 practice visual and source README show the intended order, so the defect is a consequential ambiguity in the shared wording, not an error in the intended theorem.

**Smallest fix:** Change “after each offer” to “after deciding on each offer.” Prefer putting the compulsory-last-offer sentence before that removal sentence, so the child checks the current counter count while deciding. Update only the common rule, retaining the practice visual and the later “including this one” position convention.

## Coverage and evidence

All Grades 3–5 tasks and all Grades 4–5 tasks are mathematically correct under the intended counter timing. There is no K–1 variant, as expressly allowed by stage routing. The four actual PDF card collections contain exactly **9, 27, 9 and 9** equal-size complete ordered words; neither repeated accepted scores nor unseen tails were omitted. All seven rendered pages and the two/three-counter positions were inspected. A clean build from a separate source copy reproduces every page's text, dimensions and rendered pixels. Draft/source hashes are unchanged.

Reproducible, independently authored checks and the compact task-by-task mathematical evidence are in [review-math-assets/evidence.md](../../../../tmp/worksheet-runs/week-60-new-v1/review-math-assets/evidence.md), [independent_check.py](../../../../tmp/worksheet-runs/week-60-new-v1/review-math-assets/independent_check.py), and [independent-evidence.json](../../../../tmp/worksheet-runs/week-60-new-v1/review-math-assets/independent-evidence.json). The check enumerates every deterministic history-dependent policy at horizons two and three, and explicitly distinguishes the restricted horizon-four policy enumeration from the induction proving optimality over every legal policy.

Physical mixing, display-copy handling, irreversible passes, counter enforcement, card scoring/erasing, role rotation, actual staffing and classroom fit remain **unrehearsed and unpiloted**. Digital verification does not establish those properties.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
