This is the preserved reviser report from [checkpoint 24a18cb0](https://github.com/jamesrp/math-circle-worksheets/blob/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-66-v1/reviser-report.md). Its inline `final/` paths and stage-status statements describe that historical run; live Markdown links below point to this package where applicable. The packaged guide is [k1-guide.pdf](k1-guide.pdf), its portable source is [guide-src/](guide-src/), and packaging checks are in [the packaging report](../../guide-packaging.md). Original writer/critic scripts, rendered-check records and other run evidence remain at [the pinned run](https://github.com/jamesrp/math-circle-worksheets/tree/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-66-v1/). Existing companion-guide changes mentioned below remain **future work after organizer approval**; none is implemented here.

---

# Reviser report: Week 66 K–1, Lamplighter streets

**Revisions ready; packaging deferred.** `final/k1-guide.pdf` has **4 US Letter pages**, identifier `GGT66-K-FAC-v2`. Portable source and checker are in `final/src/`; `final/verification.json` records hashes and results. The original draft, writer report, Claude review and review-check evidence are preserved. No student page, existing guide, catalog or packaged draft folder was changed.

## Finding dispositions

No must-fix findings were reported. **All three should-fix and all ten minor findings are addressed; none declined.** Numbers below refer to the preserved `review-guide.md`.

| Finding | Revision and evidence |
|---|---|
| Should 1 | Guide p. 2 practises the first-hour cube-to-square record on the same non-task F,L try. The visual shows input, one cube after a flip, two cubes after a step, and matching 0/1/2 shaded squares. Pawn is explicitly in its spot above the rightmost lamp. Dot/arrow notation is deferred to P5. |
| Should 2 | Guide p. 1 now states the two end-visiting orders and their dependence on the finish; why repeated lamp visits create P5's alternative shortest words; and why triangle inequality plus parity makes each one-move neighbor exactly one easier or harder. The destination names the first-hour discoveries. |
| Should 3 | P5's sorting instruction is replaced by a question about when home is lit. The leave-it-off question is explicitly a later hint; completeness stays in the solution. |
| Minor 1 | Preparation says dark side up means on; reset means every counter light side up. |
| Minor 2 | P5 notes that its printed FR example begins one top-picture answer; replay beside the targets and stop after two moves. The page itself is unchanged. |
| Minor 3 | Point-before-flip is the pair's legality check; the adult spot-checks and watches resets rather than claiming simultaneous observation of both streets. |
| Minor 4 | A single stroke per square is sufficient; the adult can erase surplus marks. The initial demonstration still matches the student's colouring rule. |
| Minor 5 | P4 asks which lit lamp to visit first and what happens with the other first. P7 explains that the three right-hand counts alone tie at 8. |
| Minor 6 | P3 now says the wrong order walks out to the finishing end and back again, rather than retracing the whole street. |
| Minor 7 | The demonstration uses a pawn silhouette and house outline matching the student conventions, replacing triangle/“home” glyphs. |
| Minor 8 | The print note distinguishes today's draft `k-1.pdf` from the proposed approved `week-66-k-1.pdf`. The insertion note names the future full path and the additional sentence needed in the base guide's page-1 “What children discover” paragraph. This is a later integration instruction, not a claim that the approved file exists. |
| Minor 9 | Removed the adult-guide announcement and repeated recording/dead-end explanations; replaced “workstreet,” “attains that lower bound” and “completeness support” with plain language. Space supports the expanded overview. |
| Minor 10 | P5 word lists have spaces after commas; the checker trims whitespace while still testing the exact complete lists. |

## Mathematics and actual-page verification

I rendered and read all **8 final student pages**, all **3 base-guide pages**, all **4 original draft pages**, and all **4 revised guide pages**. I checked student pictures against the adult tables: P1–P8 are on student pages 1–8; TL/TR/BL/BR ordering, P6/P7 left and three right-hand pictures, move labels and P8 tower counts match. No keyed answer changed.

`final/src/check_guide.py` passes. It replays all 24 answer-table rows, verifies their pictured lamp/walker states, steps-plus-flips splits and shortest counts; enumerates P5's complete **2 and 4** shortest-word lists and P4's two tied home-ending words; checks P6's **5 → 4,6,4**, P7's **9 → 8,8,8**, and all P8 candidates (**1/3**, **2/4**, **4/6** work). Its BFS covers **896** seven-lamp states and agrees with the unrestricted-line formula and parity. I added the every-edge check that neighboring minima differ by exactly one. The general overview's explanation uses reversible moves and parity; enumeration is supporting finite evidence, not its general proof. The non-home-start demonstration F,L reaches a non-task picture; it is not a minimum-search answer.

I also reran the preserved independent critic's vector-reading checker without altering it or its original output. It recovered all **29 framed pictures and 12 towers** from the final student PDF and passed every recomputed comparison. The printed working lamps are **20 mm** across on **24 mm** centers, with **17 mm** pawn spots. Per pair the guide correctly uses **7** of the kit's **9** counters (two spare), one pawn and about **24 cubes**. P7's four standing towers would need **33 cubes**, so recorded counts permit cube reuse. No counters, pawn or cubes are supplied as printables. Physical fit remains untested.

## Build, visual QA and clean rebuild

`bash final/src/build.sh` compiled the final guide and ended by running its checker. A separate retained pdfLaTeX log has **no errors, warnings or overfull boxes**. All four final pages were rendered and inspected for readable type, table fit, mathematical symbols, matching pawn/house/cube/square demonstration, margins and repeated header/footer identifiers. No clipping or overlap was found. Page 2 was re-rendered and re-inspected after the last small spacing/text edit; unchanged pages 1, 3 and 4 retain their inspected output.

I copied only `final/src/` and the unchanged `k-1.pdf` into a new `/tmp` directory outside the repository and ran `src/build.sh` there. Its checker passed. Both **PDF bytes and `pdftotext -layout` output were identical** to the final in-repository build. No network, repository files, student Python or absolute input path was needed. Temporary rendering/log/clean-build evidence is under this run's ignored `tmp/revise/`.

- Final guide SHA-256: `1f9ca900b28fecd0ab62f24b9102dda4484f0469ca2ba38105397f6e8cf518b1`.
- Unchanged student SHA-256: `24badb0fc7c0be2a0df035c5ccae1a15595a21ad93b293719422a14307c83bef`.

## Student-page issues and remaining limits

No mathematical student-page error was found. The guide works around P5's example being an answer prefix, its fifth blank row not promising five answers, the twelve-square capacity not promising a minimum or limiting a trial, P6/P7's arrows showing differences rather than routes, and “most” including the left picture. All target attempts start again all-off/home. The P5 representation remains readiness-dependent; P6–P8 are later routes, not required first-hour completion.

Packaging must later replace the stale “There is no K–1 packet” paragraph in base guide page 1 and add the overview band-map sentence specified in the final guide. These existing files were deliberately left untouched. **The guides remain untested with children and physically unrehearsed**: handling, reset reliability, fit, tower stability, pencil erasure, two-pair staffing and pacing have only digital/planning checks. No private external source was required or newly consulted for this bounded reviser stage. No packaging, main integration or release was performed.
