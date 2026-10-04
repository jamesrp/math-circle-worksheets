# Week 6 return visits: independent student-page critique

Reviewed `PROMPT.md`, `CRITIC.md`, current `AGENTS.md`, `draft/src/return-visit.tex`, and `draft/writer-notes.md`. The explicit outline overrides the harness's three-band filenames: the reviewed student deliverable is `draft/return-visit.pdf`, three pages, Problems 1–3, with genuine page-level bands 2–5, 4–5, and 2–5.

## Verdict

**Pass for revision/final checking. No blocking mathematical, layout, or independence defect found.** Keep the three substantial investigations and their current scope. The pages are a return-visit companion, so neither a fabricated K–1 packet nor four pages per band is required. Classroom and physical rehearsal remain untested.

## Located wording improvement

- **Low priority, page 3, Problem 3:** “explain why a row can only be read one way” can be read as a claim about every arbitrary R/Y row. Books 2 and 3 have invalid rows as well as uniquely decodable valid transmissions: for example, Y alone is invalid for both. Change this clause to “explain why a sent row can only be read one way.” This is a small precision edit; the preceding question already anchors the investigation in rows made from letter messages, so it does not currently invalidate the task. Keep the infinite-message-length explanation question: a finite search alone cannot settle uniqueness.

## Page-by-page assessment

1. **Page 1, heavy-card search (Grades 2–5).** The keeper fixes one secret, equal-size pan placements are required, and LEFT/RIGHT/BALANCED are mechanically specified. The visual shows the non-task input 10/11/12 with secret 12, placement 10 versus 12, and output RIGHT before first use. It does not expose the nine-card 3+3+3 strategy. Nine visible labels, two large pan areas, and a separate record area support repeated trials and constructing/checking a guaranteed plan. The “always” and hardest-secret questions supply depth beyond a lucky guess. A child can own the choice of grouping; no solution procedure is printed. This is readily five or more minutes of work. A real balance is not required by the stated keeper model.

2. **Page 2, unequal message batch (Grades 4–5).** The exact batch is four A, two B, one C, one D. The rules explicitly restart every message with all four possibilities, require the same plan, allow within-message adaptation, and stop at a singleton. These conventions successfully prevent a cross-message depletion strategy from changing the problem. Finding and evaluating several plans, then distinguishing total cost from the longest search, is a substantive elementary investigation. The printed record asks for four terminal costs and one batch total, avoiding eight separate tallies. The page uses ordinary counting and freely drawn plans, not an unfamiliar mandatory tree notation, so an additional worked tree would supply scaffolding rather than repair a missing convention. Band 4–5 is an honest choice for independent work.

3. **Page 3, joined counter words (Grades 2–5).** The M/N example explicitly shows message MN, separated counter words YR | R, then the joined output YRR. It demonstrates the recording conversion without exposing Book 1's collision. The three books create purposeful contrasts: an ambiguous code, a prefix-free code, and a uniquely decodable code that is not prefix-free. Repeated letters are permitted, so the investigation is not inadvertently limited to permutations or short messages. Building examples and searching for collisions offers a concrete 2–3 entry; explaining why all valid rows remain unique is a deeper continuation, appropriate for 4–5. The one collision book does not make the whole investigation a quick task because the two non-collision books require different explanations. No directed attention to prefixes or supplied decoding method gives away those discoveries.

## Independent mathematical checks

- Nine-card search: independently simulated actual LEFT/RIGHT/BALANCED responses for the 3-versus-3 first weighing and a 1-versus-1 second weighing within the remaining group. All nine secrets give distinct outcome pairs. One weighing has at most three outcomes, so two is the optimal guaranteed number under the stated fixed-secret, truthful-keeper model.
- Batch search: independently computed the optimal cost recursively over **every nontrivial subset split** of each remaining letter set, rather than assuming the writer's two tree shapes. The minimum is 14. The plan testing A, then B, then C has depths 1,2,3,3 and maximum 3; balanced depth 2 costs 16. The singleton stopping convention is necessary and is printed.
- Codebooks: independently checked unique decodability using the finite residual-word procedure (Sardinas–Patterson), obtaining Book 1 ambiguous, Books 2 and 3 uniquely decodable. Direct arguments agree: B and AC collide in Book 1; Book 2's initial R determines A and initial Y plus its next counter determines B/C; in Book 3 a final Y forces B=RY while a final R forces A=R, after which the remaining prefix is decoded in the same way. Invalid rows are not alternative decodings. The worked example MN gives YRR.

## Render inspection and format

Rendered the **current PDF** independently with Ghostscript at 110 dpi into `critic-render/page-01.png` through `page-03.png`, and visually inspected all three images. All three pages have consistent Week 6 headers, suitable band labels, footer `F06-RV-v1`, and consecutive problem/page numbers. No clipped text, collisions, overlaps, stray headings, Name/Date fields, generic encouragement, or directed substeps appeared. Printed cards, codebook labels, worked-example arrows, colour-letter counters, and recording lines are legible. The red/yellow circles include R/Y labels for grayscale interpretation. There are no polygons or calibrated physical templates to certify.

The source build and writer-stage extracted-source rebuild are documented, but I did not repeat source-package rebuilding in this critic-only stage. The later final-stage owner should verify its final revised output and final portable source package. No student PDF or source was edited during this review.
