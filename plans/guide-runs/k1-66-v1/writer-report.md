# Writer report — Week 66 K–1 adult guide

## Delivered

- `draft/k1-guide.pdf`: **4 US Letter pages**, pdfLaTeX; required header, footer and packet id `GGT66-K-FAC-v1` on every page.
- Portable `draft/src/`: `k1-guide.tex`, executable `build.sh`, independent `check_guide.py`, and `README.md`. No TeX intermediates, generated workflow prompts or student source are included in the deliverable.
- Writer stage only. No critic/reviser stage was run, no student page was edited, and nothing was committed or published. Ready for Claude's guide critique.

## Mathematical destination and replacement

The opening overview proves the decomposition into required flips plus the shortest covering walk, distinguishes a shortest construction from a lower-bound explanation, introduces the concrete 9-to-8 dead end, and explains why exact route lengths are the minimum plus an even number. It separates K–1 experimental/conjectural work from the optional evenness explanation and refers to the base guide for the older bands' general dead-end classification.

After approval, this section replaces **only the paragraph headed “K–1 tables.” under “Materials and preparation,” page 1 of `lowell-math-circle-year-2/week-66/week-66-facilitator.pdf` (GGT66-FAC-v2)**. The common launch and older-band material remain in place. Student problem and page numbers are 1–8 respectively, matching the final eight-page K–1 packet.

## Verification

- Personally rendered and visually inspected all **8 final K–1 student pages**, all **5 current older-band student pages**, the Week 98 model's opening page, and all **4 final guide pages**. Student targets were transcribed from the final pictures; revisions to the student records/wording were observed rather than assuming the older review text described the final layout.
- Independent checker imports no student code. BFS covers all **896** seven-lamp states and agrees with the unrestricted-line covering-walk formula and parity. It parses and verifies every one of the guide's **24 answer-table rows**, including lamps, walker, route replay, steps, flips and total; checks P3/P4 visiting orders; enumerates the complete **2 and 4** shortest-word lists for P5 and both tied home-ending P4 words; verifies each P6/P7 neighbor; and computes exact-length reachability for every P8 tower (working counts **1/3**, **2/4**, **4/6**). P5 completeness is also explained with the objects, not left as a code assertion.
- The checker binds the hand-transcribed targets to the final student PDF's SHA-256 `24badb0fc7c0be2a0df035c5ccae1a15595a21ad93b293719422a14307c83bef` and checks the eight problem/page labels. Independent PDF-vector measurement confirms seven **20 mm** work lamps on **24 mm** centers and **17 mm** pawn spots; these agree with the printed source and guide. Physical fit is not claimed.
- Table demonstration starts with all lamps off and the pawn at the rightmost lamp, then F, L. Neither intermediate/output is a printed K–1 target; it supplies no target minimum. The guide explicitly resets all-off/home afterward. It shows input, intermediate and output with matching dot/left-arrow records.
- `build.sh` succeeds and runs its checker after removing temporary TeX outputs. An additional retained QA compile log contains **no errors, LaTeX warnings or overfull boxes**. Every guide page was checked for typography, table fit, header/footer placement, and diagram legibility; no clipping/overlap was found.
- Clean rebuild outside the repository with only `src/` plus the final `k-1.pdf` beside it passed the checker. Extracted `pdftotext -layout` output is identical; the PDF is also byte-identical. Final guide SHA-256: `a59bb1233c3b40386db2fcac340a54f9b295a3b9fdc8d2ef030bf4a6f3762136`.
- The checker looks beside `src/` first, then discovers the repo-relative student path from ancestors. No machine-specific path is embedded in portable sources. The local TeX environment workaround was sourced externally for each compile, not added to `build.sh`.

QA renders, logs and clean-build evidence are in this run's `tmp/`, not in `draft/`.

## Student-page risks and limits

No mathematical error was found on the final student pages. The guide explicitly handles the remaining operational risks: on P6/P7 the connecting arrows depict changes between targets rather than walking directions; every target must be rebuilt from all-off/home; all four pictures (including the left one) participate in “most”; P7's four standing towers would require **33 cubes**, so the pair records and dismantles each tower while reusing its roughly **24 cubes**. It also warns that twelve shaded boxes are recording capacity rather than a limit, and that the fifth P5 row does not signal five answers.

P5 is readiness-dependent: adults may record requested symbols but children must retain the ability to replay/compare routes, rather than the adult doing the investigation. The adult may offer the parity explanation without requiring it for K–1 success. The suggested first visit stops at selected P3/P4 targets; completing the packet is not the goal.

The week's files do not print counters, a pawn, or cubes: those real objects must be supplied, as in the existing kit. No additional specialist object is required. Counters no wider than 17 mm and a pawn base fitting the 17 mm spot are specified. **The guide is unpiloted and physically unrehearsed**: actual-size printing/handling, counter stability, pawn fit, nine-high cube towers, recording demands, pacing, and success with two pairs and one adult remain untested. No missing private reference was needed for the assigned bounded guide-writing task; mathematical claims were independently checked against the supplied owned material rather than claiming fresh consultation of external books.
