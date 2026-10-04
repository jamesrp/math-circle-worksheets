# Week 54 fresh adversarial student-page review

Reviewed October 4, 2026. **Recommendation: revise one consequential wording ambiguity, then retain the packet's mathematical substance.** This is a design review of the actual nine-page `draft/students.pdf`, not of the three nonexistent per-band files named by the generic harness. The direct combined-packet routing in `plans/new-themes-52-63/STAGE-ROUTING.md` controls.

I read `PROMPT.md`, `CRITIC.md`, the routing override, the Week 54 research record, the repository README and REPUBLISHING.md, and the draft's TeX, source README and checker. I rendered all nine US Letter pages with the requested Python environment and inspected each full-page image, as well as a contact sheet. Evidence is in `review-assets/page-01.png` through `page-09.png`, `contact.png`, `extracted.txt` and `spot-checks.json`. I edited neither the draft nor its sources. The independent mathematical reviewer remains responsible for the separate full mathematical audit.

## Required revision

**R1 — Page 6, Problem 6: specify completed joining routes. Priority: high for mathematical interpretation; small edit.**

The prompt says, “Try different legal joining routes. Can the routes end with different collections?” It never says to continue both routes until no equal-size pair remains. Pages 3 and 4 put that stopping condition inside their respective numbered problems; it is not an activity-wide rule that automatically governs Problem 6. “Legal” describes individual joins and does not require a route to be maximal.

Under the literal wording, the answer can be yes: from four 3-unit strips and six 1-unit strips, a route that stops after joining two 3s ends at `6+3+3+1+1+1+1+1+1`, while a route that stops after joining two 1s ends at `3+3+3+3+2+1+1+1+1`. Both contain only legal moves, preserve 18 units, and end differently. The intended terminal collection is `12+4+2` in both completed routes. Thus this ambiguity changes the answer to the question intended to establish independence of merge order.

Add the terminal condition directly to the task, for example: “Try different legal joining routes, continuing each until all sizes are different.” Keep the open question and the general all-odd claim. This supplies an essential rule without giving away either the conclusion or the explanation.

## Page coverage and design findings

| Actual page | Task and rendered evidence | Assessment |
|---|---|---|
| 1 / Problem 1 / Grades 2–5 | Complete unordered catalogs for totals 4 and 5; first-use record `2+1` shown as loose strips → longest-first rows → sizes. | Substantial child-owned search with a clear fixed total, positive parts and no order distinction. The example uses total 3, outside both target catalogs. Enough room for rows or size records; no answer enumeration is printed. |
| 2 / Problem 2 / Grades 2–5 | Choose total 6 or 7; build odd-only and different-size catalogs separately. | Both restrictions are introduced clearly and remain separate, so “odd” is not silently changed to “odd and distinct.” This is a genuinely new classification question, not a padded grade variant. The two catalogs externalize the comparison. |
| 3 / Problem 3 / Grades 2–5 | Worked total-10 input → one actual join → terminal `6+4`; then nine ones, `5+5+3+3+3+1+1`, and `5+3+1`. | The physical action is introduced before use with a meaningful intermediate state. Cases contrast repeated carrying, two odd families with a retained 3, and a collection requiring no join. These differences justify the three cases; they are not arbitrary number substitutions. Units and labels are visible at the printed scale. |
| 4 / Problem 4 / Grades 2–5 | Worked `4+3+2` → `3+2+2+2` → `3+1+1+1+1+1+1`; three distinct inputs are split and rebuilt. | Concrete inverse testing has adequate contrasting work: a mixed 24-unit collection, the shared odd core of `12+6+3`, and an all-odd fixed point. All starting sizes differ. The original state remains printed for checking the return; children need not remember it. The small pictures are usable records beside manipulatives. |
| 5 / Problem 5 / Grades 2–5 | Find every matching odd/distinct pair for total 8 and record sizes in paired rows. | A substantial synthesis after the actions are familiar. The six true pairs are not supplied to children. The two-way arrows have a clear matching role. Numerical records are appropriate here and much lighter than repeated full drawings. |
| 6 / Problem 6 / Grades 4–5 | Eighteen-unit starting collection; two route spaces and a large general-reasoning space. | Rich order-independence investigation with real choices both within families and between families. Preserve the general question. Required fix R1 makes the mathematical destination unambiguous. No unfamiliar route code is imposed, so no additional code demonstration is needed. |
| 7 / Problem 7 / Grades 4–5 | Worked `5,3,3,1` → column lengths `4,3,3,1,1` → rebuilt rows; twice-exchange trials `5,2,1`, `4,4`, `3,3,1,1`. | Input, actual column reading and output precede first use. The example has total 12 and does not solve the total-8 target trials/catalog. Trials contrast uneven rows, a rectangular diagram, and repeated short rows. Square axes are equally scaled; each six-by-six output grid can hold its required diagram. |
| 8 / Problem 8 / Grades 4–5 | All total-8 collections with at most 3 strips, transformed and classified; asks for a rule for any total. | A real restricted-catalog and correspondence problem. Ten true input collections fit the twelve-row table. Sizes are explicitly requested, so the one-row cells are workable even for the eight-ones output. The largest-part bound is left for children to discover. |
| 9 / Problem 9 / Grades 4–5 | General odd/distinct equality through joining and splitting, with large explanation space. | Retains the actual theorem and the need for a general explanation. The prompt does not substitute another finite experiment or print a binary grouping recipe. Oral reasoning, objects and drawings can support this page. Its full-page workspace is justified by the explanation, not by a decorative variant. |

Every rendered page has the consistent week/topic/grade header, footer identifier and page number. Problems run consecutively 1–9. I found no clipping, overlap, unintended second title, Name/Date field, generic encouragement, optional hint, or “go further” label. Shared conventions appear where needed instead of being repeated after every task. All displayed unit squares have equal horizontal/vertical scaling; the physical diagrams' visible row lengths match the printed labels and source cases. No polygon/arc variants or additional grade packets exist to inspect in this draft.

## Mathematical spot checks relevant to design

My separate small enumeration found 5 partitions of 4 and 7 of 5; the odd/distinct counts are 4/4 for total 6, 5/5 for total 7, and 6/6 for total 8. The total-8, at-most-three-strip catalog has 10 members. The three Problem 4 inputs return under splitting then terminal joining, and their totals are 24, 21 and 11. The displayed row/column examples conjugate as drawn and return on the second exchange. These results are recorded in `review-assets/spot-checks.json`; they do not prove the all-total theorem or replace the fresh mathematical audit.

No mathematical error was found in the printed examples. R1 is an essential assumption/wording issue rather than an incorrect diagram. The general explanations must ultimately distinguish finite evidence from the reversible correspondence, including termination, independence of legal join order, and both inverse identities. The research record contains that substance; keep it for the later separately authored adult guide.

## Operational concerns to test, not automatic redesign requirements

**Catalog workload and records, especially pages 5 and 8.** A pair's 24-unit kit cannot retain all six 8-unit collections simultaneously. The packet already provides a recoverable size record for each collection and its partner, and Problem 8 explicitly uses size records. This satisfies the immediate bookkeeping need; I do not recommend printing the intended catalog or a catalog-making algorithm. In a pilot, watch whether children use the records to check duplicates/completeness or instead spend their effort recopying collections. If matching or rearranging the accumulated records becomes the mathematics, offer blank movable record cards or let pairs pool their own discovered cards, as the project guidance recommends. That is an operational option, not evidence that these modest catalogs presently need replacement by supplied solution cards.

**Page 4's dense intermediate record.** The 24-unit input splits to `7+5+5` and seven ones, so the middle cell may require ten drawn rows. A sizes record is much lighter and fits. The source notes allow adult recording while children make choices. Rehearse this with the actual pieces and a typical child-sized written record; do not infer physical readiness from this render. If the cell becomes a barrier, a minimal local clarification of record mode or adult recording is preferable to losing this useful mixed case.

**The approximate Grades 2–5 header on pages 1–5 needs the stated prerequisite gate.** Counting/adding through 24, comparing group sizes, recognizing odd/even and retaining a reversible rule are meaningful requirements. The source README names them and explicitly permits adult reading/recording. The physical entry is credible for the four third graders with the anchored mathematician, but independent completion of all catalogs or all inverse checks is untested. The Grade 4–5 pages add whole-catalog comparison and general reversibility arguments rather than simply larger arithmetic. This is an honest omission of a full K–1 route under the routing override, not a defect to repair by manufacturing one.

**Several visits are reasonable.** There is considerably more than one hour of good work here. A first grouping/classification/rebuilding visit and a later route/involution/general-explanation visit are credible options. These are my planning inferences, not a reported classroom outcome or a fixed timetable. The later adult guide should offer a manageable first route and readiness-dependent continuations, retain pages 6, 8 and 9's full explanations, and state that finishing every page is not the goal. It must also supply the brief common launch with children handling pieces first. The source README already records that launch intention; a separate guide is outside this writer-stage deliverable and is not missing work to demand from the student writer.

I reread *Math Circle by the Bay*, Preface printed pp. viii–ix (PDF pp. 9–10), on deep themes, manipulative use, independent work/dialogue and clear statements, and *A Decade of the Berkeley Math Circle*, §3.6 printed pp. 113–114 (PDF pp. 133–134), on the difference between extensive evidence and explanation. Those actual source lessons support keeping the packet's depth and fixing R1's ambiguity. They do not validate this adaptation's age fit, pacing or material handling.

**Minor optional typography:** page 8 splits “total” as “to- / tal” in the task. It is legible and mathematically harmless, but disabling this one automatic word break would improve a short read-aloud task. This is not a release blocker.

## Revision boundary

Make R1 explicit and re-render the changed page. Preserve the child-owned unordered catalogs, all three purposeful join/split contrasts, the concrete row/column involution work, and the general proof questions. No restart, new band variants, completed catalog on student pages, or reduction of the upper theorem is justified by this review. Physical fit, rule retention and classroom pacing remain untested.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
