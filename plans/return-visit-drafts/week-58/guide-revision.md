This is the preserved reviser report from [checkpoint 24a18cb0](https://github.com/jamesrp/math-circle-worksheets/blob/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/rv-58-v1/reviser-report.md). Its inline `final/` paths and stage-status statements describe that historical run; live Markdown links below point to this package where applicable. The packaged guide is [facilitator.pdf](facilitator.pdf), its portable source is [guide-src/](guide-src/), and packaging checks are in [the packaging report](../../guide-packaging.md). Original writer/critic scripts, rendered-check records and other run evidence remain at [the pinned run](https://github.com/jamesrp/math-circle-worksheets/tree/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/rv-58-v1/). Existing companion-guide changes mentioned below remain **future work after organizer approval**; none is implemented here.

---

# Week 58 return-visit guide: reviser report

## Deliverable

`final/facilitator.pdf`: **8 US Letter pages**, footer `W58-RV-FAC-v2`.
Portable sources and checker are in `final/src/`. Drafts, writer report and critic evidence are preserved. No student page, base guide, base material file or packaged draft was edited. Packaging remains a separate stage.

**Untested with children and physically unrehearsed.** Preparation time, print fit, cutting and handling, staffing, pacing and child independence remain estimates or open checks.

## Finding disposition

There were no must-fix findings. All seven should-fix findings and six minor findings were addressed; none was declined.

| Critic finding | Revision and location |
|---|---|
| Should 1: continuous two-taste fact and three-taste bound | Guide p. 1 adds the continuous half-value window with nonatomic/nonnegative/additive assumptions and a zero-density limiting qualification. The train proof remains explicit. The X/Y/Z fact now points to adding/comparing the three equations. The general k-cut result is labelled literature background, not a page task or a result established by finite checks. Grades 4–5 P3 distinguishes the general bound from the fixed 60/180 mm positions. |
| Should 2: band discoveries and demands | P. 1 now states each band's intended discoveries, separates experiment/conjecture from explanation, and identifies adult reading/scribing, millimetres, half/quarter-panel work and fixed-observer comparisons. |
| Should 3: launch goal/recording | P. 3 has two children build/split the non-task train, draw the bar on a sketch, and hear the fewest-places goal. The two-cut trick is withheld. |
| Should 4: timing and one additions list | P. 2 gives estimated per-problem first routes, a two-column first-hour/later additions table, an explicit warning that routes can continue on another visit, and a lower-consumable option using unmarked actual-size rows or tracing overlays. The 20–30 minute estimate is explicitly for first-hour additions to a ready base kit. |
| Should 5: panel run sheet and actual scale | P. 5 has a five-step marking-game run sheet, cited on p. 7. P. 2 distinguishes schematic strips from 150 mm panel rows and the 125 mm goods row. The four-child grades 2–3 group stops pair work together for three recipients/referee. |
| Should 6: repeated band labels | Every solution heading has K–1, Grades 2–3 or Grades 4–5; prose replaces the ambiguous middle/upper labels. |
| Should 7: length | Removed revision history, author-process notes, repeated explanations, the K–1 1/16/16/1 and 790-train census from teaching prose, redundant determinant and table commentary, and the base kit size table. Essential computations stay in the checker. The revised PDF is 4,350 whitespace-delimited words including tables/headers, versus the critic's approximately 4,709-word draft count, despite the new theorem, run sheet, print table and demands. It remains eight pages. |
| Minor 1: already-printed challenge | K–1 P3 now says P2 row 5 already supplies such a train, and asks a copier for a different challenge. |
| Minor 2: row versus separate halves | Grades 4–5 P4 states that the three row cut positions and alternating trays are forced up to tray exchange, whereas separate panels allow any choice of one half of each per tray. |
| Minor 3: excessive uniformity assumption | Grades 4–5 P6 permits nonnegative additive divisible values with no value stuck at a point. Uniform panel density remains the printed numerical model. |
| Minor 4: instruction-like hint/reset | P. 5 asks which card is used across the trays and names the fallback: redo the printed Y-panel example with a real panel. |
| Minor 5: upper pair/trio | P. 2 says three children use one pair kit with rotating referee for train work; all three are recipients in panel games and the adult referees. |
| Minor 6: provenance | P. 8 cites Procaccia through the base guide's consulted range and explicitly makes no claim of newly rereading the chapter. Other background bibliography is also labelled not newly consulted. |

## Mathematical and reference checks

All numerical answers remain unchanged. The final checker passes the original exact tests: all printed trains and minimum gaps, 70 four-red/four-blue orders, all 790 kit-bounded trains, 10,922 even-count trains through length 14, strip equations and 80/160/60/180 mm cuts, the X/Y/Z half system, every mark/taker/observer value/envy comparison for six games, all 120 labelled five-card orders, and the two-red obstruction/cut positions. It additionally solves 729 two-observer continuous-window examples exactly, with unequal panel widths and zero or nonuniform densities. These examples exercise the added explanation; they do not prove the general continuous or k-cut theorem. Material arithmetic is checked as well.

I rendered and personally inspected all **17 final student pages** (K–1 5; Grades 2–3 6; Grades 4–5 6), all eight material pages, the nine-page base guide, the eight-page writer draft and all eight revised guide pages. I checked the printed train words, problem/page map, card values and panel conventions against the guide. The final student SHA-256 pins still pass:

- K–1: `e2f7b33390031a2dd21d842d3c4536be969a0cf85cdb20c6722377cb0b06b11c`
- Grades 2–3: `c355af82ef03fc15a32837b9d4d0cb2bc27214abc7cad0ce27a49d9e81cf7e5e`
- Grades 4–5: `9a05f73c4fcd48c704f6ebeac740664019e74ff102602a086d1bd3abb7e09a32`

Material counts match the actual base PDF: materials p. 1 has three sturdy reds/two blues plus the separate replacement R3; combining only the base five and the extra five gives six reds/four blues per pair. The extra paper R3 is set aside. Material p. 5 supplies one three-panel set and C; p. 4 supplies A/B. There are three strips on each of pp. 6–8. The print list distinguishes disposable replacements from mounted cards and reduced-cutting page-row games.

## Build and visual QA

`final/src/build.sh` ran with real pdfLaTeX twice per build and passed its no-error/no-overfull gate and terminal checker. Every final page was rendered at 105 dpi and inspected: text/tables legible; no clipping, overlaps, overflow, broken figures or footer collision. All pages are Letter size. Source has no absolute build paths or generated prompts.

A clean outside-repository directory contained only `final/src/` plus the three unchanged student PDFs alongside it. `src/build.sh` succeeded there, including its checker. `pdftotext -layout` matched exactly; the PDFs were byte-identical. Final/rebuilt SHA-256:

`83717d2fc83334d71b2df4c96d3a764b07a9ab5d4e83c2fc26b9c31196a7d25d`

Local scratch evidence lives under this run's ignored `tmp/` (renders, extracted text, build/clean-build logs and `verification.json`). No TeX intermediates are included in `final/src/`.

## Student-page issues and workarounds

Student pages are unchanged. The guide retains the writer's eight page issues, with the critic's clarifications:

1. Grades 4–5 P6's “whatever values” follows a rule aiming at 4. The guide requires each person's own original total divided by three when card values change; total 24 needs target 8, not 4.
2. Grades 2–3 P5–6 non-takers still need a 112.5 mm quarter-panel mark. The adult may scribe or establish it lies beyond 75 mm; half-panel teaching alone is insufficient.
3. K–1 P3's seven record rows do not promise seven answers or require the all-34 catalogue; record successful partner challenges actually played.
4. Grades 2–3 P1 has eight rows for six colour orders; unused rows are spare.
5. Student red/blue strip diagrams are schematic; cut the real 240 mm material strip. Panel rows and the goods row are actual size when printed at 100%.
6. Two-person A/B and three-person A/B/C repeat letters with different values. Put the first set away and retain one observer across tray comparisons.
7. Grades 4–5 P4 has three observers judging two trays, not three own shares. Row-cut uniqueness differs from arranging separated panel halves.
8. Twelve-slot open train records do not require twelve physical cards; the ten-card kit serves fixed trains and larger inventions may be sketched.

No new student-page defect was found. Private source books and Procaccia were not newly accessed or claimed reread. Digital checks do not establish actual material fit or successful classroom use.
