# Week 91 K-1 adult guide: writer report

## Deliverable and scope

- `draft/k1-guide.pdf`: **4 US Letter pages**, F91-K-FAC-v1.
- `draft/src/`: `k1-guide.tex`, portable `build.sh`, independent `check_guide.py`, and rebuild README. No LaTeX intermediates are in the deliverable folder.
- Writer stage only. No critic or reviser stage has run, and no student or public week files were changed. The generated absolute-path stage prompts are not deliverables and must not be committed.
- The overview establishes one-switch alternation and pile difference at most one; four-exit equal-depth tree balance and return of every card after four counters; eight possible starts with distinct orders; opposite halves for the first two counters; and the difference between deterministic routing and independent coin choices. It separates experiment, conjecture and explanation, and points to the base guide for older-band mathematics rather than repeating the road theory.

## Exact replacement boundary

On approval, replace **“K–1 route, adult-read”** under **“Preparation, launch and visit choices”** on **page 2 of `lowell-math-circle-year-2/week-91/week-91-facilitator.pdf` (F91-FAC-v3)**, including that paragraph's final two lines at the top of page 3. Preserve the base guide's shared launch, older-table kit instructions, and the “First packet: operating and programming” section that follows it. The existing page-1 overview still says there is no independent K-1 packet; updating that sentence is a future integration consistency task, not an edit made at this writer stage.

## Inputs and page matching

Read the project instructions, brief, generated writer prompt, Week 91 K-1 outline, both student reviews, current K-1 drafts README, final student sources, base adult guide, materials and older student/return packets. Consulted the Week 98 adult guide and its source for format, tone and density.

Personally rendered and inspected **all seven final K-1 student pages**, including the revised diagrams, and the relevant materials pages 1, 2, 6 and 7. The final packet, not the earlier reviews' keys, controls the guide:

- P1 is ten counters, not the base route's twelve.
- P3 asks for five on either exit and two on the other, with six rows of seven boxes.
- P4's table order is 5, 8, 7, 4.
- P5 has nine recording trees; eight starts exist.
- P6 has six pictures, including the revised eight- and twelve-counter targets.
- P7/P8 are on student page 6; P9 is on page 7.

The checker binds these inspected pages to student PDF SHA-256 `bbf6588bb112f7eadc9f4c480e50315baa44615ad0b3da7c228d04e8082c68c8` and checks extracted problem/page mapping and revised wording.

## Mathematical verification

`draft/src/check_guide.py` is my own generic follow-then-flip graph simulator; it imports neither the student generator nor its checker. It checks the compiled guide's answer text as well as its independently computed results.

- Both switch starts, every prefix through 64 arrivals, the two ten-counter words, and all six P2 pile targets.
- All 128 seven-toss words: **42** achieve the revised five/two split; six independent trials miss it with probability **9.198794%** (guide rounds to 9.2%). The printed witness is valid.
- P4 predictions for both starts and all requested indices; all 256 eight-toss words verify the conditional one-half coin probabilities.
- All eight tree starts through 64 arrivals; the full distinct order key; **488** length-four windows with one visit per exit and return of the full state.
- Every successful start for every P6 target; P7 B-first-to-two starts LRL/LRR at counter 5 and B-last starts RLL/RLR at counter 8; P8's exact two starts RLL/RRL; all four P9 target pairs and impossibilities.
- The guide gives pairing, split-bundle and forced-route explanations for universal claims. Finite tests are regression evidence, not a claim to replace those proofs.

## Build, visual review and portability

- Two-pass pdfLaTeX build succeeded with **no errors, overfull boxes or missing-character warnings**. `build.sh` rejects these and cleans its temporary build directory before running the checker.
- Personally rendered and inspected **every final guide page at 130 dpi** after the last edit. Headers/footers, demonstration panels, tables, page breaks and all text are legible with no overlap or clipping. The one-departure demonstration has blank exits, a preserved spare card, visible intermediate state, and gives no numbered-task answer.
- Copied only `draft/src/` and the unchanged student `k-1.pdf` into a fresh directory **outside the repository**, with the student PDF beside `src/`. Rebuilt from inside that copied source folder. The checker passed without repository imports or absolute paths. The copied source folder remained free of build intermediates.
- Original and clean-copy `pdftotext -layout` outputs matched exactly; the PDFs were also byte-identical, SHA-256 **`a5ae5b4ab055a7e94b3bdaabd8f61ae68b7e7eb15bb24c05afedc2dc19d7f23a`**.
- Both builds used the supplied isolated TeX environment for this machine's broken global distribution configuration. No machine-specific environment or path is embedded in the portable script. This is a clean-source rebuild, not an independent-operating-system test.
- QA logs, text and renders are in this run's `tmp/` and are not deliverables. The checker first finds a sibling student PDF, then discovers `plans/k1-drafts/week-91` by walking repository ancestry.

## Student-page risks and remaining limits

No mathematical error was found in the final student pages. No student page was edited. The guide anticipates these remaining usability risks:

1. **Preserving starts:** P2/P6 drawing language still follows a trial in prose, but the revised shared rule requires copying spare cards first. The guide repeatedly says to copy the saved cards, never the changed working cards, and shows a non-task visual.
2. **Coin misses:** about one pair in eleven can miss the revised split even across all six rows. The guide distinguishes “did not occur” from impossibility and accepts a proposed face sequence, without misreporting it as an observed toss.
3. **Prediction row order:** P4 lists 5, 8, 7, 4. The guide makes all guesses first, then records actual arrivals in chronological order in the same unchanged trial.
4. **Spare frames:** P5 has one extra tree beyond its eight starts; P8 has a third frame although exactly two complete starts work. The guide explicitly says blank spare frames need not be filled and accepts “the unused card does not matter.”
5. **Writing and fine-motor load:** one adult can become a bottleneck when both pairs need a scribe. The guide suggests staggering tasks or one team, and distinguishes student recording miniatures from actual card boards.
6. **Integration note:** the base guide's “not an independent packet” overview sentence will need updating if these pages are approved, alongside replacement of the identified K-1 route.

All required printable cards/boards/strips are provided by the existing week kit. Counters, coins, pencils, scissors, glue and demonstration scrap paper are supplied objects, not printed files. Labeled cups are an optional supplied overflow aid already allowed by the base guide, not a new required printable.

**Unpiloted and physically unrehearsed.** Actual-size printing, card preparation and flipping, counter/card clearance, exit-pile handling, spare-card copying, adult recording load, timing and age fit were not physically tested or observed with children. The guide includes a 50 mm print check and an explicit rehearsal request. No classroom-readiness claim is made.
