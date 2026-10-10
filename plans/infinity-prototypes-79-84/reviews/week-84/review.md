# Week 84 adversarial review

Reviewed 9 October 2026 as a fresh critic. This is the critic stage only; no student or guide sources were edited.

## Scope and evidence

I read PROMPT.md and CRITIC.md, including the explicit one-packet/selected-band override. I reviewed the eight-page `draft/students.pdf`, all three source files in `draft/src/`, and the separate five-page facilitator draft at `infinity-drafts/tmp/guide-drafts/week-84/facilitator.pdf` with its TeX source. I rendered every page with PyMuPDF and inspected all 13 pages. Critic renders are under `critic-render/students/` and `critic-render/guide/` in this run. A repeated-image display issue sometimes suppressed repeated headers in the inline tool view; PDF text positions and independent raster crops confirmed that the actual student headers/footers are present. That is not a document defect.

I independently enumerated all eight cafe deals and all eight three-headband worlds using a separate set-of-worlds calculation, rather than relying on the author's verifier. I checked the Hamkins October 2019 talk page, which links the slides and identifies the classic blue-eyed islanders/common-knowledge territory: https://jdh.hamkins.org/i-know-that-you-know-that-i-know-that-you-know-oxford-october-2019/ . I did not reread the private Rozhkovskaya passages claimed in the guide and do not certify that provenance detail here.

## Verdict

The mathematical core is correct and worth keeping. Problems 1–4 are substantial investigations with contrasting cases; the non-target two-person/two-doll worked visuals occur before first use; the cards use letters as well as colors; the guide opens with actual facts and hypotheses. The scope appropriately omits a forced K–1 edition and keeps the finite number grid adult-only. This draft needs revision before delivery because the shared-state implementation remains vulnerable to accidental information leaks, its main board cannot display the supplied initial card set, and the guide lacks several promised solutions. The guide also has one genuine clipped URL.

## Required student/material revisions

### 1. Page 8 does not physically accommodate the visible possibilities it is supposed to externalize

Each configuration card on pages 4–5 is 3.45 by 1.85 inches. Each page-8 “Still possible”/“Ruled out” rectangle is 3.45 by 5.7 inches, with its heading taking additional room. Even ignoring the heading, that box holds only three nonoverlapping cards vertically. The cafe starts with eight cards; the announced hats start with seven; Problem 4 starts with eight. A stack or heavy overlap hides most of the mathematical evidence. This is an exact dimensional contradiction, beyond the honest statement that physical rehearsal is untested.

Revise the board/card arrangement so the complete public set can remain visible and manipulable. Reasonable options include an explicitly tiled multi-sheet board, table-space headers instead of confining rectangles, or a deliberately sized compact configuration-card set. Preserve legible labels and sufficient handling size. State the intended print/assembly arrangement in the guide; do not claim a physical rehearsal occurred.

### 2. Make the distinction between permanent public deletion and temporary private-view filtering operational

The abstract rules on page 2 are correct: all three replies use the same pre-round shared set. But the only printed board is “Still possible / Ruled out,” and the guide launch says to show how one private observation “filters possibilities.” A likely implementation is to remove every card that does not match doll 1's view, then coach doll 2 from those survivors. That would leak private information and destroy the intended simultaneous-round result. Another likely error is to use the complete actual three-color deal as a doll's information, because spectators see it on the page.

The guide must explicitly say that matching a doll's private view does **not** remove anything from the shared set. Inspect or point to that doll's matching cards, make its choice face down, and return to the complete unchanged public set before coaching the next doll. Only the jointly revealed three-reply vector permits permanent deletion. Label the main set as shared/public if the revised board supports that distinction. No extra student proof procedure is needed, but a small private-view marker or masking arrangement may help enforce the rule.

Include a concrete adult check: in actual BBR with the initial seven public worlds, doll 1 must retain both BBR and RBR as private matches, doll 2 retains BBR and BRR, and doll 3 retains BBR and BBB. All three reply NOT YET on round 1. None of these three private two-card subsets is the next shared state. After that all-NOT-YET vector, the shared survivors are BBR, BRB, RBB, BBB.

## Required facilitator revisions

### 3. Add exact solutions matched to every numbered student problem

The guide gives YYN as an example and proves the one/two/three-blue theorem, but does not state the complete Problem 1 solution sets or the solutions to Problems 3 and 4. These omissions matter because these are the prompts most likely to produce mistaken public/private inference.

Problem 1, in displayed conversation order:

- Conversation 1: YYN, exactly one deal.
- Conversation 2: NYY, NYN, NNY, NNN, exactly four deals. After the first NO everybody knows the proposition “everyone wants a cup” is false, so later NO answers do not expose later preferences.
- Conversation 3: YNY, YNN, exactly two deals.
- Conversation 4: YYY, exactly one deal.

Problem 2: BRR gives (PROVE BLUE, NOT YET, NOT YET) at round 1; BBR gives all NOT YET at round 1 and (PROVE BLUE, PROVE BLUE, NOT YET) at round 2; BBB gives all NOT YET through rounds 1–2 and all PROVE BLUE at round 3. These must be computed from the pre-round state, and the red doll continues to say NOT YET even once it knows red.

Problem 3: round-1 grouping consists of singleton BRR, singleton RBR, singleton RRB, and one group of four {BBR, BRB, RBB, BBB} giving all NOT YET. Round 2 separates the four remaining arrangements: their reply vectors have blue in positions 1&2, 1&3, 2&3, or none, respectively. The last group is the singleton BBB even before it declares on round 3. Thus later replies do separate every group. Distinguish the audience's identification of BBB after round 2 from the dolls' own round-3 public declarations.

Problem 4: without the announcement, every doll has both own-color possibilities for every fixed pair of visible colors. All eight worlds produce the same all-NOT-YET vector. Deleting worlds inconsistent with that vector deletes none, so the state remains all eight. This is an unchanged-state argument covering arbitrarily many rounds, rather than an extrapolation from a few trials.

### 4. Repair the overlong source URL on guide page 5

The first Hamkins URL runs past the right edge and is visibly clipped. The LaTeX log reports an overfull hbox of 219.56764 pt at source lines 46–47. Use a short linked title or a deliberate URL-breaking package/layout, then re-render the final guide. The other inspected guide pages have no clipping/overlap problem.

## Readiness and workload recommendations

These are design judgments, not findings from a classroom pilot.

- Keep Grades 2–3's first route at the cafe and a coached one-blue example. For Grades 3–5, use the two-blue and three-blue worlds. Problems 3–4 are valuable readiness-dependent continuations; the visible all-worlds argument is their mathematical action, so do not eliminate them merely because they require adult reading.
- In the first route, use the teacher's ideal doll answers as checked results; actual children's hesitation, incorrect guesses, or uneven speed never become evidence. The current guide already says this clearly and should retain it.
- Add a print/use map: student task pages 1–3, cafe configurations 4, hat configurations 5, private preference/color cards 6, public response cards 7, shared display 8. Specify sets per table and any duplicates required by the repaired board. The adult should know whether previous cafe replies remain displayed or are adult-scribed; the lone extra YES/NO response cards on page 7 do not by themselves make three persistent reply displays.
- The guide's proposed common launch refers to a “worked non-target arrangement” without naming it. Point the adult to the actual two-doll BR worked example on student page 2, or supply the precise non-target launch. A normal launch should demonstrate legal coaching and one public update without revealing the target two-blue/three-blue timing.
- The guide covers theorem-first overview, assumptions, timing, concrete materials, first route, source/adaptation distinction, and observation record well. It currently has little optional hint support; one “which of these matching cards gives your doll red?” prompt would support the core without prescribing the whole investigation.
- The optional 0–6 grid is mathematically consistent with the bounded domain. It may remain a whiteboard encore, with no student grid added in this batch.

## Page-by-page visual check

- Student 1: header/footer, rules, non-target cafe example, all four transcripts legible; no overflow.
- Student 2: complete rules, private-view visual, three concrete deals legible; no overflow. Shared/private board issue is operational, not a typo in these rules.
- Student 3: Problems 3–4 have useful working space; no answers leaked.
- Student 4: all eight distinct cafe configuration cards present, numbered positions clear.
- Student 5: all eight distinct hat configurations present, positions/letters clear, RRR included correctly for the announcement and no-announcement comparison.
- Student 6: three YES, three NO, three B, three R private/prop cards; letters supplement color.
- Student 7: three PROVE BLUE and three NOT YET cards; two additional cafe YES/NO cards. Large clear type.
- Student 8: clear response slots, but possibility bins undersized for the complete supplied set.
- Guide 1: theorem-first overview and grade map; good layout.
- Guide 2: setup and timing readable; requires the explicit private/public handling repair.
- Guide 3: existing cafe example and headband explanations correct; add missing exact prompt solutions.
- Guide 4: bounded-grid encore correct and appropriately optional; good layout.
- Guide 5: source URL clipped; adaptation/unpiloted/physical-untested labels otherwise clear.

Digital mathematical checks establish the stated finite model only. Physical card fit, privacy masking, simultaneous reveal procedure and classroom pacing remain unrehearsed and unpiloted.
