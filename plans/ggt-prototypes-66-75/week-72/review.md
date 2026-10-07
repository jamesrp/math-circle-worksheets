# Week 72 adversarial student-packet review

## Verdict

**Retain the four-page mathematical design; make the memory apparatus continuous across the later tasks.** This is a strong concrete entry into order-dependent motion and signed area memory. All printed examples and requested outcomes are correct. The chief revision is practical: the packet relies on a movable memory marker, but its two different printed number lines do not provide one consistent signed-memory workspace for the final task. Signed arithmetic and the final all-integer construction must remain honest readiness gates.

Reviewed the authorized shared Grades 4–5 `draft/students.pdf`, all four pages. I read `PROMPT.md`, its scope addendum, `CRITIC.md`, repository `AGENTS.md` and `README.md`, student source, source README and checker. Fresh renders at 105 dpi are in `critic-render/`; every page was inspected visually. PDF SHA-256: `196c6763bf0e2f1104d3012281263eee89c60706281b5f08c3301a97b515e512`. No draft or student-source edits were made.

## Revision priorities

### 1. Pages 2–4: supply one usable signed-memory marker surface

The rule explicitly gives one partner a movable memory marker. Page 1 supplies a line from 0 to 8, while Page 2 replaces it with a line from −6 to 6. Pages 3 and 4 supply no line. Page 4 requires memory 7 and then −3, so neither earlier line, on its own, supports the whole task. The 7 is present on Page 1: this is not an impossible numerical task or a wholly absent resource. It is an avoidable page/material switch at exactly the point where the state should stay easy to recover. Intermediate values can also leave a printed range on a child's legitimate exploratory route.

Provide one reusable bidirectional memory strip, or explicitly supply the permitted equivalent counter tray, with a clear way to extend beyond its printed ends. A range covering at least the concrete tasks is enough; a paper line need not depict every integer in the final general question. Reusing a loose strip across all pages would avoid crowding and make the partner's job stable. Keep this as an apparatus convention, not an arithmetic hint or a suggested route.

The later adult materials list must also make E/W/N/S cards real rather than assumed: prepare enough for exploratory routes, plus a simple option to record longer words on paper. The shared instruction to keep all cards in order is valuable; it should not silently require an unlimited stock of cards in Problem 4.

### 2. Minor language precision on Page 4

“Any whole-number memory, positive, zero or negative” states the intended set clearly, but “whole number” is often taught as excluding negatives. Use “any integer memory” if that vocabulary is part of the prerequisite gate, or simply “any memory number, including negative numbers.” Do not alter the intended all-integer construction.

## Page-by-page findings

- **Page 1 / Problem 1:** The movement arrows, column-based update rule and division of partner roles are clear. The non-task EENE visual shows the initial state, an intermediate horizontal run, the N update and a later unchanged memory. Its arithmetic is correct. The 3-by-3 mat has generous working space, the target ring is clearly at `(2,2)`, and the route/final-memory record is recoverable. Seven blank rows are harmless even though there are six distinct routes; they do not tell the children the answer. The task is substantial enough to involve enumeration and equal-memory comparisons without requiring a method.
- **Page 2 / Problem 2:** All four cards necessarily return the robot to O; different orders produce memories −1, 0 and 1. Asking whether any other value can occur makes completeness the central question rather than an automatic “explain” after arithmetic. The large signed-column mat and memory line are useful. Moving west before moving north and subtracting a negative column are genuine new arithmetic demands; this is an appropriate stopping gate for children who have only done Page 1. The source README already states that gate honestly.
- **Page 3 / Problem 3:** The three congruent rectangles at columns 0, 2 and −3 isolate translation from area. The L-shaped boundary adds a purposeful nonrectangular case. Each has an explicit start, correctly numbered columns and sufficient room for a robot counter. Asking children to add direction arrows makes the two recorded values interpretable. The final question is a conjecture-generating task, not a printed theorem. The eight oriented trials have more than enough substance. A reusable memory strip would make this page operational without reaching back to another worksheet.
- **Page 4 / Problem 4:** Reaching one position with two specified memories and then with an arbitrary memory extends the central idea rather than merely changing numbers. The printed grid is large enough for valid examples and for repeated unit loops, so the all-integer result does not require walking beyond the mat. The two route lines and explanation space are adequate for concise route records. The final construction is readiness-dependent and may be a return visit rather than a compulsory finish within one hour.

## Independent mathematical checks

The supplied checker passes the EENE example, all six monotone routes, all 24 four-card loops, translated rectangles, the L-shaped loop and signed-memory constructions. I separately recomputed memories from the geometric line sum `sum x·Δy` over successive path vertices rather than reusing the checker's mutable-counter implementation.

- The six monotone words give `EENN:4`, `ENEN:3`, `ENNE:2`, `NEEN:2`, `NENE:1`, `NNEE:0`.
- Among the 24 orders of ENWS, four yield −1, sixteen yield 0, and four yield 1. Thus the three possible memories in Problem 2 are complete.
- Counterclockwise traversal of each displayed rectangle gives +2, including the translated negative-column rectangle; reversal gives −2. The L-shaped loop gives +3, or −3 in reverse.
- Concrete Page 4 witnesses within the drawn grid include `EEEENWNW` for memory 7 and `NNNENESS` for memory −3. Both finish at `(2,2)` after eight moves. This is existence evidence; the student is not asked to minimize length.
- For every positive integer k, perform the unit loop ENWS k times at O and then NNEE; the final state is `(2,2,k)`. For a negative integer use NESW the corresponding number of times, followed by NNEE. For zero use NNEE. This gives the general plan while keeping all motion within the displayed mat, and it does not rely on passing through the target before the final arrival.

The independent kernel report verifies the stronger destination: on a closed simple loop the memory is signed area, positive for counterclockwise orientation. Translation adds the horizontal shift times total vertical displacement, which is zero for a closed loop. Arbitrary repeated or self-crossing walks instead record algebraic area with multiplicity, not the unsigned area of their union. The Page 3 examples are simple outlines, so they correctly support the first statement. The later adult guide must preserve this distinction when responding to children's more general claims.

The integral memory convention also remains separate from the symmetric height `z−xy/2` used in the cited Heisenberg source. No student prompt incorrectly calls an open path's raw memory its Euclidean enclosed area. The group formula need not appear on the student sheet for the noncommuting-motion idea to be substantive.

## Visual, scope and readiness checks

All four pages have consistent headers, footers, page numbers and consecutive problem numbering. Grids have equal horizontal and vertical scales. Columns, dots, rings, route lines and arrows are legible; no clipping, overlapping labels, missing symbols or insufficient writing area was found. The worked-example panels are small but readable, and their black point identifies the current position.

The four-page shared Grades 4–5 scope matches the addendum; the lack of K–1/Grades 2–3 outputs and the separate adult guide is not a defect. Sources are editable and include no borrowed reference text. The material and arithmetic risks above are digitally identified, not classroom observations. Before use, rehearse a negative-column move with the actual marker system and check that the checking partner can update memory without the adult running the state. Preserve the concrete Page 1 entry even for children not ready for the signed-arithmetic continuation.

## Independent exact-instance cross-check

Before closing this review I read the completed independent `draft-instance-review.md`. Its Week 72 result is PASS for all four problems. I verified that its PDF and student-source SHA-256 fingerprints match this reviewed draft. Its findings agree with this review; the proposed revisions above concern task selection, conventions or physical usability rather than a failed mathematical instance.
