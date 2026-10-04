# Independent adversarial review: Week 11 chip-firing packet

## Verdict

**Revise before printing, chiefly for two consequential ambiguities.** The mathematical examples, graph drawings, and physical board sizes are sound. All three PDFs have six US Letter pages, and I found no clipping, overlaps, missing glyphs, or incorrect edges in the 18 rendered pages. This does not need a wholesale redesign. The main risks are children solving a different problem from the one intended, and a few places where the recording layout does less than the task asks.

I read `PROMPT.md`, freshly rendered all three delivered PDFs at 90 dpi, visually inspected every page, checked the authoring source for exact dimensions and wording, and independently enumerated legal continuations for the numerical starting positions. I did not edit the draft.

## Required revisions

### 1. Make the total and the freedom to redistribute explicit

**K–1, page 2, Problem 2; also grades 2–3, page 3, Problem 3.**

K–1 currently says: “Put 4 chips on A and B, then share until you must stop. Find every finish; do the same with 5 chips.”

There are two separate problems:

- “4 chips on A and B” can mean four altogether or four on each circle. The page does not disambiguate this with pictured starting piles.
- The preceding problem changes the sharing order while keeping a given start. This problem needs children to change the starting distribution, but never says that they may. A child following the established pattern can try several orders from one chosen distribution, find the same finish, and reasonably regard the problem as done. That turns a substantial search into one short run.

A minimal two-sentence repair is: “Put 4 chips altogether on A and B in any way, and share until you must stop. Find every finish; then try 5 chips.” This supplies the missing objects/constraint, not a method for organizing the search.

Grades 2–3 Problem 3 similarly begins “Put exactly 6 chips on A and B.” Add “altogether.” Its following request to find every start helps convey redistribution, but the total should still be explicit. The intended seven possible starts have total six, not six chips at each vertex.

**Why this matters mathematically:** distributing four chips produces three distinct finishes, `(1,1)`, `(1,0)`, and `(0,1)`. Five chips also produce those three finishes. If the K–1 instruction is read as four at each circle followed by five at each circle, both trials instead finish at `(1,1)` and the central search disappears. For grades 2–3, the successful total-six starts are exactly `(0,6)`, `(3,3)`, and `(6,0)`.

### 2. Scope the sharing-count question to one fixed starting position

**Grades 4–5, page 1, Problem 1.**

The last sentence asks: “Can the final piles agree while the sharing counts differ?”

As written, there are two defensible answers. Across two orders **from the same start**, the answer is no. Across the different starts printed in this very table, the answer is yes:

- `(2,2)` finishes at `(1,1)` with sharing counts `(1,1)`.
- `(3,3)` finishes at `(1,1)` with sharing counts `(2,2)`.

Thus a correct observation from the displayed data can look like a counterexample to the intended order-independence statement. Add the missing scope, for example: “For the same start, can the final piles agree while the sharing counts differ?” If comparing different starts is intentionally part of the task, ask that separately and explicitly. Do not treat an unqualified “yes” as an error.

## Recording and usability revisions to consider

These are smaller concerns, not mathematical failures.

### 3. Match the space to the requested record

- **Grades 2–3, page 4:** the problem asks for another order and a comparison of both final piles and sharing counts, but supplies only one results row per start. Other order-comparison pages supply duplicate rows. The 12 mm-high rows could be divided into two trial rows without changing the board or adding a procedural hint. As printed, children must decide how to put two records into one cell or retain the first result from memory.
- **Grades 4–5, page 3:** “Draw the routes of pairs you get” is followed by a tightly defined “After 1” through “After 4” table and only one writing line. The table can hold the successive pairs, but there is little obvious open space for a separate route drawing or for showing the shared three-state cycle. Either make the requested product a record of successive pairs, or give actual drawing room. Do not print the cycle or its arrows as a hint.
- **Grades 2–3, page 3:** the exhaustive-start table is useful, but the explicit completeness explanation gets only one ruled line. An oral explanation with the adult is possible in this setting; if a written explanation is expected, give it more space.

### 4. Distinguish initial emptiness from a later reachable state

**Grades 2–3, page 6, Problem 6.** “Which pairs of final piles can each rule reach?” follows an instruction to begin empty, while the table begins after one addition. Both repeated-addition rules visit the same three nonempty stable pairs after additions; the empty pair exists only at time zero. “After at least one addition, which pairs of final piles can each rule reach?” would remove this small boundary ambiguity. This is optional, but useful given the next band's explicit transient-versus-cycle problem.

## Mathematical audit

The underlying student problems are otherwise correct. I independently checked all listed numerical configurations on the triangle, four-cycle, and four-cycle with diagonal, including all distributions of totals four, five, and six on the triangle. Exhaustive branching over available legal moves produced exactly one terminal configuration and one sharing-count vector for each checked start. These checks were independent of the author's `checks.json`; reviewer output is in `review-render/independent-checks.json`.

Key results relevant to the tasks:

- Triangle reference cases `(2,2)`, `(4,0)`, and `(3,3)` give the stated outline results. `(4,0)` has only one complete legal order, so the “if possible” qualification in the first problems of both older packets is necessary and correctly present.
- Four-cycle `(0,4,0)` finishes at `(1,0,1)`, with counts `(1,3,1)`. The grades 2–3 page 2 starts do allow different complete orders.
- The diagonal board has degrees three at A and C and two at B, exactly as drawn. Its examples are legal with the common rule. In particular, `(3,0,3)` finishes at `(2,0,2)`, so the added line supplies a genuine change in stable-pile sizes rather than merely another picture of the degree-two game.
- K–1 Problem 4 has eight stable assignments, all three coordinates independently zero or one. Four chips cannot be stable on that board. The task is mathematically substantial and appropriate to concrete enumeration.
- The triangle batches `(3,0)+(0,3)` and `(2,0)+(0,4)` finish at `(1,1)` and `(1,0)` respectively, under all three tested timing choices. The four-cycle batches `(2,0,0)+(0,4,0)` and `(3,0,0)+(0,0,3)` finish at `(1,1,1)` and `(1,0,1)` respectively.
- Adding one chip at A on the triangle gives `(0,0) → (1,0) → (0,1) → (1,1) → (1,0)`. The empty state is outside the three-state cycle. The two different starts `(0,0)` and `(1,1)` both map to `(1,0)`, so grades 4–5 Problem 3 correctly exposes non-reversibility. The packet does not make the false claim that every stable state belongs to a group or returns to itself.
- The final four-cycle start `(0,8,0)` finishes at `(1,0,1)` with counts `(3,7,3)`, totaling 13 sharing moves. It does offer different legal orders.
- The termination and uniqueness explanation questions in grades 4–5 are valid for the finite connected sink boards shown. They are substantial ending problems. Their general explanations are demanding, but the adult-led setting and the instruction to supply more than most children finish make that an acceptable challenge, not a reason to add a proof recipe to the student pages.

## Physical and presentation audit

- All delivered PDFs are exactly six pages at 612 × 792 points (US Letter).
- The source specifies 44 mm working circles, satisfying the minimum 40 mm clear working-region requirement, and a 60 × 60 mm sink on every board. The board edges terminate at boundaries and remain outside the chip-placement regions. These are pile regions, not one slot per counter. Larger piles may need stacking, which the brief allows.
- There is one sink per diagram, plainly labeled, and the common rules state that it retains chips and never shares. No ambiguous duplicated sink is present.
- Numerical tasks fit the 24-counter allowance. The largest explicitly prescribed initial total is 12, and the longest fixed cumulative addition trial uses 12 chips.
- Headers give the correct week, topic, and band. Footers have the required organization/week/packet identifier and page number. All problem labels use “Problem N:”.
- Fonts are embedded, and no missing-character or overfull warnings appeared in the logs. The rendered pages are legible, with clear lines and no text touching a board or footer.
- The pages avoid mascots, manufactured excitement, extra activity headings, worked answers, formal algebraic vocabulary, and lettered procedures. K–1 problems stay within two sentences, with dot-based starts where useful.
- Six pages per band and the later enumeration, cycling, and general-explanation tasks provide a credible reserve of work for the hour. K–1 receives genuine mathematical questions rather than a shortened arithmetic worksheet.

## Recommended revision order

1. Repair the shared-total/distribution wording on K–1 page 2 and grades 2–3 page 3.
2. Add “for the same start” to grades 4–5 page 1.
3. Improve the recording fit where convenient, especially the second-order record on grades 2–3 page 4.
4. Re-render after edits and recheck the affected pages. Preserve the large boards, concrete examples, spare register, and substantive final problems.
