This is the preserved reviser report from [checkpoint 24a18cb0](https://github.com/jamesrp/math-circle-worksheets/blob/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-57-v1/reviser-report.md). Its inline `final/` paths and stage-status statements describe that historical run; live Markdown links below point to this package where applicable. The packaged guide is [k1-guide.pdf](k1-guide.pdf), its portable source is [guide-src/](guide-src/), and packaging checks are in [the packaging report](../../guide-packaging.md). Original writer/critic scripts, rendered-check records and other run evidence remain at [the pinned run](https://github.com/jamesrp/math-circle-worksheets/tree/24a18cb02a3f45c91311c90d5a85b65886450278/plans/guide-runs/k1-57-v1/). Existing companion-guide changes mentioned below remain **future work after organizer approval**; none is implemented here.

---

# Week 57 K–1 guide revision

Reviser stage only; student pages, existing guides/materials, draft source and independent review evidence remain unchanged. The section remains **untested with children and physically unrehearsed**. No packaging or integration is performed here.

## Finding dispositions

No must-fix findings were reported. All seven should-fix and all five minor findings were addressed; none was declined.

| Review item | Disposition and check |
|---|---|
| Should 1: demonstration | Build the same non-task 1-by-3 row from two squares and two halves, count “two, four, six halves”, contrast one tip-only extra half and remove it. Explicitly distinguish half counts from the shared launch's area units. Correct the between-corners wording; cover the older demo grid's question and I/B/area line. The input picture now shows the third square's diagonal. Row checked independently as (halves, outline, inside) = (6, 8, 0). |
| Should 2: overview explanation | Added the one-side and two-side-notch bookkeeping, including exactly how a newly enclosed dot changes both counts. Kept the general dot rule as adult knowledge while children notice contrasts. |
| Should 3: P1 picture descriptions | Corrected the wide triangle, rectangle and trapezoid intermediate dots and the unequal top-row paper amounts against the actual final PDF; retained all six correct answers. |
| Should 4: P2 catalog | Added four diagrams with actual half-piece divisions, four classes up to turns/flips, six when reflected copies count separately, all five outline dots. Reconstructed diagram triangle coordinates in the checker and proved their canonical set equals the complete three-half enumeration. |
| Should 5: kit capacity | Require trace/lift/reuse between constructions; extra pieces from the spare bag only for simultaneous comparisons. Explicitly note 20 halves hold five four-half shapes, and all six P5 shapes together require 12 squares (kit has 10). Pooled records are traced pictures. |
| Should 6: first-hour contrast | Default 38–50 minutes to P3's tilted-square contrast; remain with P2 only while joins/counts are insecure. |
| Should 7: P7 extra rule | Permit an intact square to stand for two halves, matching the student shared rules; ask for the half-paper count in the saved six-piece shape. Two shapes and all counts remain unchanged. |
| Minor 1: insertion notes | Named p. 1's K–1 pointer, both p. 2 print options, p. 3's 10–25 younger row and exact replaced K–1 paragraph. These existing-guide changes are instructions for later integration only. |
| Minor 2: printing | Named future `week-57-k-1.pdf` and current draft `k-1.pdf`; added spare pp. 2, 3, 5; stated the 10–15 minutes are additional to the week's 15–25-minute preparation/rehearsal estimate. |
| Minor 3: brevity | Removed repeated checker narration and board-quota disclaimers, preserving the adult catalogs and explanations. Clarified P3's 13-plus-one description and the six-square discussion's 12 halves without implying a nonexistent P6 record line. |
| Minor 4: quickest pair | Added eight-half records 10, 8, 6 alongside inside counts 0, 1, 2, explicitly connecting each newly enclosed dot to two fewer outline dots. |
| Minor 5: provenance | Added that the halves form, closing-in arguments and all instances were newly worked for these pages. |

## Student-page and material verification

Read the actual seven-page N57-K-v1 packet and rendered/inspected every page. P1–P7 each occupy the corresponding student page. P1 counts are (1,3), (2,4), (2,4), (2,4), (4,6), (4,6). P2/P3 boards have 3 by 4 dots; P4 5 by 5; P5 3 by 3; P6 6 by 5 with adjacent stars; P7 4 by 5. Workboards use 20 mm spacing. The p. 1 instruction explicitly counts a square as two halves; the P7 revision respects it.

Read the full ten-page W57-FAC-v4 base guide and visually inspected its p. 3 launch/route. Read and rendered both N57-M-v1 materials pages: 60 squares and 60 diagonal squares giving 120 halves. Five kits (10 squares, 20 halves) leave one kit's worth spare. Each shape fits its kit; simultaneous board filling requires the reuse convention now stated. No new material printable is needed.

No erroneous student-page statement was found. Operational issues remain: the p. 1 miniature example is not a 20 mm template; pieces hide dots, hand-cut cracks are not geometric tests, stars are targets, tip-only joins/pinched gaps are illegal, and the older spare grid carries text to cover. These are handled in the adult guide. Student PDF SHA-256 remains `3eb8603152b88bac06f94aa54f59ee39c7afb76cf94b31c4ca52f6baad7bc28f`.

## Mathematical verification

The final checker pins the actual student PDF and all seven problem/page labels. It recomputes P1 via polygon coordinates, checks the non-task row, exhausts all half shapes through eight (1, 3, 4, 14, 30, 107, 318, 1116), and checks all simple shapes against the dot relation without using it to obtain dot counts. P2's new diagram set is complete. P3 has 13 six-outline shapes plus the four-outline tilted square. P4's angle bound, P5's six rotation classes, P6's six-cell lower bound/16 constructions, and P7's two six-outline solutions all pass. New kit-capacity arithmetic and six rotation-only P2 classes also pass. No printed numerical answer changed.

Digital checks do not establish print fit, hand-cut piece handling, tracing feasibility, adult staffing, pacing or classroom readiness.

## Final build, layout and clean reconstruction

**Final: 5 US Letter pages, N57-K-FAC-v2.** The extra page gives the new P2 catalog and its P3 contrast their own readable spread; the former four-page layout would strand the catalog alone on an otherwise empty overflow page. Every final page was rendered with Poppler and inspected at readable size. The result has consistent headers/footers, clear piece divisions/dot marks, legible tables, no clipping or overlaps and no blank/diagram-only overflow page. The latest P3 cross-reference points to P5 on the following guide page.

`final/src/build.sh` completed with pdfTeX 1.40.29 and rejected neither errors nor overfull boxes; its final checker passed. The same unmodified source was copied outside the repository with only the unchanged student `k-1.pdf` beside it, and `src/build.sh` succeeded there. The clean and final guide PDFs are byte-identical and their `pdftotext -layout` output is identical. The source/checker uses relative lookup and no machine-specific paths.

Guide PDF SHA-256: `0687e7777b6f9bb4bcad889de88eeed577da6dc1e011298e230091584633646a`.

Remaining dependency: packaging is deferred to the coordinator after catalog integration; the base guide insertion notes are not applied at this stage. No blockers remain in this revision.
