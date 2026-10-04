# Independent adversarial review: Week 12

## Verdict

The mathematical content is sound, the three PDFs render cleanly, and each band has six genuinely usable pages. I found no incorrect answer, malformed supplied pairing/path/tree, clipped text, or collision between printed elements. This is a strong draft, not a packet that needs to be rebuilt.

I recommend a targeted revision before printing, chiefly to make the physical-disc version work as clearly as the pencil version. The other concerns below are about essential definitions and the precision of a few prompts, not wrong mathematics. Preserve the open problems and the absence of supplied solution methods.

## Findings, in priority order

### 1. The intended endpoint discs cover the position labels, and several circle mats are marginal at the specified maximum disc size

**Where:** All K–1 pages; particularly the eight-dot circles on pages 3–4 and the ten-dot circle on page 5. Also the large six-dot working row on grades 2–3 page 1.

The supplied materials specify 15–20 mm diameter endpoint discs. In the source, the circle numbers sit only 4.3 mm radially beyond their endpoint centers. A centered disc has radius 7.5–10 mm and will cover those numbers, including the starting position 1. The numbers under the large line mat begin only 2.4 mm below the endpoint centers and are covered too. The circle arrows do not identify all the fixed positions, and parts of the arrows on the denser circles are also close to the discs.

The eight-dot circles of radius 27 mm have adjacent center separation 20.665 mm, leaving just 0.665 mm between 20 mm discs. The ten-dot circle of radius 33 mm leaves just 0.395 mm. These are not literal overlaps, and curved string routes remain possible, but they are barely separated physical endpoints for small hands. Straight connections between adjacent endpoint centers are almost completely hidden under the discs. That weakens the intended distinction between a changed pairing and a changed string shape, especially with 40 cm strings whose surplus must be managed.

**Revision:** Keep the compact circles for pencil records if desired, but provide a clearly usable larger physical working mat, with the start/position markings outside the maximum disc footprint. Alternatively, enlarge/rearrange the affected mats and move markings far enough from every endpoint. Check the result with actual 20 mm circles superimposed on the printout, not just bare dots. The existing grades 2–3 large row already has good 24 mm endpoint spacing and more than 90 mm of clear working height; it primarily needs its markings moved.

This is the most concrete print-readiness issue. It is an ergonomic/readability problem, not a claim that the diagrams have the wrong combinatorial objects.

### 2. Say what makes two pairings different

**Where:** The initial rules in K–1 and grades 2–3, affecting all collection/counting tasks.

“Keep the dots in place” and the numbering establish fixed positions well. However, neither packet explicitly says that only the partners matter. With flexible strings, a child can make two visibly different routes joining the same pairs, or can treat two rotated-looking patterns as the same. The mathematical count is finite only after the equivalence convention is clear. Grades 4–5 does state the corresponding convention for trees: “Only the branching and its order matter.”

**Revision:** Add one short essential rule, for example, “Pairings are different when a dot has a different partner.” This is a definition of the objects being counted, not a hint about how to enumerate them. It should remove the need for an adult to supply an extra counting convention midway through a problem.

### 3. The first tree problem assumes several new graph words before showing a connected example

**Where:** Grades 4–5 page 1, Problem 1 and its rules.

The opening introduces “root,” “parent,” “child,” “loops,” “branching,” and then “edges.” The only diagrams on that page are isolated filled dots. In particular, “edge” is never connected explicitly to a drawn line, and the parent/child relation is not pictured until page 2. A child who has not seen graph-theoretic trees can need an additional explanation just to know what objects to draw. That is at odds with the brief's preference for concrete objects and introducing terminology after using the idea.

**Revision:** Make the initial rules state concretely how dots and joining lines relate, or include a very small structural example that does not give an answer to the three-edge enumeration. Keep the root and left-to-right order explicit, and do not replace the task with arbitrary/unordered trees. This needs a small entry-point repair, not an extra lesson or worked three-edge example.

### 4. One height question admits correct answers that miss the intended invariant

**Where:** Grades 2–3 page 2, Problem 2: “What is always true about how high the path goes?”

For these three six-step cases, “it reaches at least one square,” “it never gets above three squares,” and “it goes up before it goes down” are reasonable answers. The intended common condition appears to be that the height never drops below the starting level. The current wording does not distinguish that from a question about maximum height. This is not a wrong question, but it can create avoidable redirection by the adult.

**Revision:** If the nonnegative-height observation is the goal here, ask about height relative to the starting level, without stating the answer. If the intention is deliberately broad discussion of several height features, retain it and recognize that it does not itself establish the Dyck-path condition. Page 4 correctly supplies that condition for its own task.

## Mathematical verification

I checked the source and independently enumerated every perfect matching on fixed ordered positions, then filtered out interleaving endpoint pairs. This did not call the author's Catalan-word generator. It gives the counts for 0 through 6 pairs as **1, 1, 2, 5, 14, 42, 132**.

- **K–1 Problem 1:** Two four-dot pairings exist, and four different six-dot pairings are available.
- **K–1 Problem 2:** There are exactly five six-dot pairings. Six recording circles do not disclose the answer.
- **K–1 Problem 3:** With eight dots, the fixed pair 1–4 has two completions; 1–6 has two; 1–3 and 1–5 have none. The duplicated 1–4 and 1–6 frames are sufficient to record both completions. All supplied chords have the correct endpoints.
- **K–1 Problem 4:** There are fourteen eight-dot pairings, so the open collection has substantial headroom beyond its six initial frames. The instruction permitting extra circles is explicit.
- **K–1 Problem 5:** The 3-, 5-, and 7-dot cases are impossible; the 4-, 6-, and 10-dot cases are possible. The ten-dot task asks only for one pairing, not the full collection of 42.
- **K–1 Problem 6:** The answer is no. Every noncrossing eight-dot pairing contains a pair of circular neighbors. One can see this by taking a pair with the fewest intervening points: if there were any intervening points, a pair wholly among them would give a smaller one. No forbidden hint or answer is printed.
- **Grades 2–3 Problem 2:** The three supplied pairings encode respectively as UUUDDD, UUDDUD, and UDUDUD. All supplied arcs are noncrossing, and the grids can contain the corresponding paths.
- **Grades 2–3 Problem 3:** The four drawn paths encode as UUDUDD, UDUUDD, UUDDUUDD, and UUUDUDDD. Their associated rows have the correct six or eight endpoints. Each has exactly one noncrossing inverse pairing.
- **Grades 2–3 Problem 4:** Exactly five paths satisfy the stated conditions. The use of six grids avoids giving away the count.
- **Grades 2–3 Problem 5:** UUUDDUDD and UUDUDUDD are valid. UDDUUDUD first goes negative at its third letter; UUUUDDUD ends at height 2. The invalid cases test different obstructions.
- **Grades 2–3 Problem 6:** Fourteen solutions fit in the sixteen supplied rows. This is a substantial extension.
- **Grades 4–5 Problems 1 and 5:** There are five three-edge and fourteen four-edge ordered rooted trees. The unlabeled drawings and explicit left-to-right convention preserve the intended class. The six and sixteen roots do not leak those totals.
- **Grades 4–5 Problem 2:** The four drawings have four edges each and encode as UUUUDDDD, UDUDUDUD, UUDUDDUD, and UDUUUDDD, matching the eight writing boxes per tree.
- **Grades 4–5 Problem 3:** All four codes are valid; UUDDUD and UDUUDD correctly distinguish the extra descendant on the left from the one on the right. The uniqueness question genuinely concerns the ordered-tree inverse.
- **Grades 4–5 Problem 4:** UUUUDDDD, UDUDUUDD, and UUUDUDDD are valid. UUDDDUUD and DUUUDDUD have negative prefixes; UUDUDUDU ends above zero. The request for general rules and reconstruction addresses existence as well as uniqueness. An empty code is also valid for the root-only tree, though no need to supply this answer on the student page.
- **Grades 4–5 Problem 6:** The requested counts are 42 and 132. A first-return/first-branch split gives a valid all-sizes recurrence, and the instruction asks for an exact count with justification rather than extrapolation from a pattern.

## Page-by-page visual and task audit

All eighteen pages were rendered from the actual deliverable PDFs at 90 dpi and individually inspected. All are single-page-size US Letter, 612 × 792 points, with consistent headers, unique band/version footer IDs, and page numbers 1–6. No supplied diagram is clipped or overlaps problem text, another diagram, or a footer.

- **K–1 page 1:** Clear two-case opening. The four-dot and six-dot frames match the task. Numerals between vertically adjacent circles are fairly close but do not collide.
- **K–1 page 2:** Six clean frames, with room for the complete set. Because page 1 already asks for four of the five solutions, much of the new work must be the completeness argument; this is a modest progression rather than an entirely new search.
- **K–1 page 3:** The contrasting possible/impossible partial configurations are a particularly good substantial problem. Printed chords are unambiguous.
- **K–1 page 4:** Clean open collection. It has fewer printed frames than possible answers, but the explicit continuation on blank paper is allowed by the brief's own examples.
- **K–1 page 5:** All six point counts are correct and distinguishable. The ten-point mat is larger than the others, but still tight for maximum-size discs as noted above.
- **K–1 page 6:** Larger circles give better working space. The impossibility question is real mathematics and a useful endpoint for faster children.
- **Grades 2–3 page 1:** The large blank region is purposeful manipulative space, not an accidental pagination gap. Six smaller drawing rows support a complete collection.
- **Grades 2–3 page 2:** Arc diagrams, writing boxes, and path grids align clearly. The forward code is given as the rule for the representation; it should not be removed as a prohibited solution hint.
- **Grades 2–3 page 3:** All four paths are legible, with corresponding workspaces for inverse pairings. There is enough vertical room for pencil arcs.
- **Grades 2–3 page 4:** The six large grids are appropriately spacious.
- **Grades 2–3 page 5:** Codes are readable and the valid/invalid cases are not visually marked as answers.
- **Grades 2–3 page 6:** Sixteen eight-dot drawing rows are dense but workable in pencil. Their approximately 10.5 mm spacing and roughly 20 mm usable arc height make them recording diagrams, not additional physical-string mats. Do not treat them as meeting the specification for object mats.
- **Grades 4–5 page 1:** Plenty of drawing space; the concern is the definition/entry point, not layout.
- **Grades 4–5 page 2:** The four tree diagrams preserve child order and show the root distinctly. There is adequate room to write the codes.
- **Grades 4–5 page 3:** Codes and root marks leave ample space for reconstruction and explanation.
- **Grades 4–5 page 4:** The six codes and broad blank area support classification plus the requested general argument.
- **Grades 4–5 page 5:** Sixteen root positions leave workable space for small four-edge trees; additional written organization can use the remaining lower area or blank paper supplied with the session.
- **Grades 4–5 page 6:** The mostly blank page is justified by a substantial counting/generalization problem. Counting six-edge trees is ambitious, but appropriate as surplus work at the end rather than a required finish.

## Organizer-standard assessment

The packet follows the requested register unusually well: only the prescribed header and problem labels function as headings; there are no motivational slogans, activity narration, themed characters, lettered solution steps, worked answers, or recurrence hints. Every K–1 problem has at most two sentences. Explanation requests chiefly concern completeness, impossibility, validity, or reversibility, where explanation is the actual mathematics.

The three bands have enough work, with flexible stopping points. K–1 receives genuine completeness and impossibility questions rather than merely easier counting. The older packet correctly chooses the tree–code route without forcing all three representations into the hour. The early completeness tasks and later inverse tasks form a reasonable mathematical progression.

The remaining improvements should be local. Do not add a facilitator guide, solution pages, a scripted discovery sequence, or a displayed counting recurrence to the student deliverable.
