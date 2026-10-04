# Week 13 return-visit critic review

## Scope and verdict

Reviewed the actual three-page `draft/return-visit.pdf`, Problems 1–3, against `PROMPT.md`, `CRITIC.md`, and `AGENTS.md`. The explicit shared-collection scope overrides the harness's three-band filenames and its usual four-pages-per-band expectation. This is a companion containing three investigations, not a replacement hour-long packet.

**Verdict: retain the investigations and make two local revisions.** The mathematics, non-task convention examples, page structure, and working space are strong. The definite physical-layout defect is that the permitted 15 mm occupancy markers cover parts of the middle-dot labels on page 1. A small wording change should also distinguish the routes retained within an attempt from resetting between attempts. Neither issue calls for new problems, a new representation, or extra worksheets.

## Minimum fixes

### R1 — Move occupied-dot labels outside the marker footprint (required)

**Page 1, both working maps:** `DotMap` places A/B/C/D labels 8 mm from their dots and H 8.5 mm away. In the actual PDF, the nearest text bounding boxes are only about 5.2–5.8 mm from the dot centers. A 15 mm marker has a 7.5 mm radius, so a centered marker overlaps these label areas. This is especially unhelpful at H, the meeting point whose reservation carries the investigation.

Move the labels so their nearest visible ink clears the 7.5 mm radius, preferably with at least 1 mm additional space. An offset around 11–12 mm from dot center is a reasonable starting point; expand the map bounding boxes as necessary and inspect the result. Keep both maps at their present useful working scale. The smaller U–V–W convention example already places V far enough away and does not need replacement. Check all five reservable dots on both working maps at actual size with the largest permitted marker.

This is a geometric PDF check, not a physical rehearsal: no actual markers were placed on printed sheets in this review.

### R2 — Make the boundary of an attempt explicit (small clarity revision)

**Page 1 shared rules:** “Keep all routes drawn at once” is the correct simultaneous model, but the problem then changes the sharing rule on the same working map. The intended action is to retain all routes of the current attempt, not carry the previous packing unchanged into the next rule test.

**Page 3 shared rules:** “Keep all earlier rows” correctly prevents treating capacities as successive travel, but can also sound like routes from abandoned trials may never be removed.

Use “Keep all routes in one attempt drawn at once” on page 1 and “Keep all rows for one attempt” on page 3, or equally brief wording. For page 1, make it clear that changing the rule begins a fresh attempt; erasing the routes or using the supplied spare paper is sufficient. Do not require children to maintain separate tallies while routing, or add a worked packing of either task graph. The counts already preserve the results of the two rule tests.

This is an unpiloted interpretation concern rather than observed classroom failure. A normal launch may resolve it, but the wording fix is cheap and keeps the distinction visible on the page.

## Page-by-page findings to preserve

### Page 1 / Problem 1 / K–1 entry

- The small U–V–W visual appears before the unfamiliar occupancy rule is used. It has a plain map, one dashed route, then the same route with its middle dot reserved. It demonstrates the action without revealing either task packing. The displayed reservation circle is 15 mm in diameter, consistent with the stated maximum marker size.
- Two full-width maps provide a purposeful contrast: the shared H obstruction, then the A–C bypass. The question preserves the child's choice of route and gives four distinct outcomes to test rather than a procedure for finding them.
- S and T remain common endpoints; the rule concerns middle dots. Arrow sharing remains forbidden when dot sharing is allowed. Both route styles remain visible, supporting simultaneous reservations rather than moving a single counter through and then freeing the route.
- The entry has real mathematical content and is plausible after an adult launch. Reading and numeral recording are adult-supported at this table; the child still chooses routes and encounters occupied dots. Maintaining solid/dashed route traces is a practical readiness demand to rehearse, not a reason to remove the investigation.
- The working maps are approximately 16 cm across, with well-separated dots and unobstructed road midsections. Two counts per map are a light record. Changing the sharing rule on one map does not require a new bookkeeping system, once R2 is clear.

### Page 2 / Problem 2 / Grades 2–3 entry

- The rules explicitly allow shared dots, prohibit shared arrows, and retain both routes at once. The printed paired destinations make the simultaneous condition concrete. A child cannot correctly answer the swapped case merely by finding each route in succession.
- The three large maps serve distinct roles: compatible prescribed pairs, incompatible prescribed pairs, then a choice of distinct finishes. The last case intentionally returns to a compatible assignment; it realizes the outline's reassignment comparison and should not be replaced merely because its graph repeats.
- All required arrows are present. The central C–D road is clear, and no geometric crossing creates an unstated meeting. P/Q, X/Y, and the two line styles are legible. The broad boards leave room to trace an attempted pair, including an overlap in an impossible attempt.
- “Fits / Impossible” supplies a compact decision record. An explanation of the obstruction can be handled by the adult without appending a routine proof demand. The printed task itself is sufficient to start independent attempts after the launch.

### Page 3 / Problem 3 / Grades 4–5 entry

- The U–V–W example explicitly bridges the map to a route row and then to two simultaneous reserved rows. Both rows remain visible, and repeated identical routes are shown. It does not require inferred counts from moving counters or interpreting a number as road length.
- Although page 1 forbids sharing an arrow under its rule, page 3 clearly introduces its own capacity rule and explicitly permits repeated routes. The example also visibly permits the middle dot V to be shared. These rules already communicate the changed model; do not add a separate ban on shared dots or restore the earlier one-route-per-arrow rule.
- The route rows are a recoverable record. Children can inspect each whole route to check arrow use; they are not asked to keep a concurrent tally at every road. Six adequately long rows accommodate the optimum of four and five routes on the respective maps.
- Crossed-out arrows remain readable alongside the route rows. The capacity numbers are close to the intended roads without overlapping them. The second map changes C–T from 3 to 4 while preserving the rest of the network.
- Finding a packing and an equally small blocking-arrow total is substantive work. The two contrasting capacities are enough for this companion investigation; the question preserves the child's choice of packing and blocking set. It does not print the min-cut theorem or give the intended answer.

## Mathematical sanity check

The rendered diagrams match their source edge lists. I ran `draft/src/check_math.py`; all assertions passed. I also checked the concrete witnesses and upper bounds against the pages:

- Problem 1: the first map admits the edge-disjoint routes S–A–H–C–T and S–B–H–D–T, but all routes use H, so only one fits under the middle-dot rule. On the second map, S–A–C–T and S–B–H–D–T fit under either rule. The two arrows out of S bound the maximum at two.
- Problem 2: P–A–X and Q–B–Y fit together. The swapped pair must both use C–D, so cannot fit together; each route exists individually. Free reassignment admits the first pair.
- Problem 3: for C–T capacity 3, one S–A–C–T, one S–A–T, and two S–B–C–T routes fit, giving four. Crossing out A–T and C–T blocks every route and totals four. With capacity 4, two S–A–C–T, one S–A–T, and two S–B–C–T routes give five, with the same blocking pair totaling five.

These are finite-instance checks, not a claim that the student pages establish a general theorem.

## Visual evidence and limits

Rendered every page directly from the draft PDF with PyMuPDF at 1.8× resolution (approximately 130 dpi) into `critic-render/page-1.png` through `page-3.png`, then inspected all three at readable size. Headers, footers, page numbers, consecutive problem numbering, arrows, capacity labels, examples, and answer areas are present. No clipped text, overflowing elements, unintended blank pages, or print-layout overlaps were seen; the marker-over-label defect arises when the intended physical materials are added.

No student source or PDF was edited or rebuilt. No facilitator guide, later workflow stage, upload, commit, or physical/classroom trial was performed. After the two local revisions, the reviser should render all three pages again and check the marker clearance on page 1. Classroom fit remains unpiloted.
