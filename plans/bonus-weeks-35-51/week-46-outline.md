Week 46 bonus: Boards that forget

Mathematical kernels

1. A shared COPY instruction (slot j receives the current color of slot i on each board) transports dependencies instead of overwriting with a new color. With only copies, all-red and all-blue starts can never match. One shared color reset followed by copies can synchronize every start. Each slot depends on one original slot or a reset constant; keep a live dependency record using arrows/markers. New instruction must have explicit old/new paired-board visual.

2. Uniform independent position draws on three slots cover all slots in exactly three draws in 6 of 27 histories; by four draws they have covered all in 36 of 81. The first complete coverage may take arbitrarily long. Drawing all three positions without replacement guarantees coverage in three draws while independent fair new colors still produce uniform final boards. Choose an exact waiting-time/chooser comparison, beyond base a fixed covering story.

3. A rotating/shift memory device can combine RESET the left slot and cyclic ROTATE the whole row. Reset+rotate may erase all starts even though only one physical slot ever receives a new color. Shortest universal reset words for three slots involve three resets and suitable rotations; dependency tracing proves optimality. This changes the forgetting mechanism from fixed-coordinate overwrite and offers a concrete code-design challenge distinct from copy propagation. Verify minimal lengths by exhaustive transition search.

Sources: Existing Week 46 outline, final base PDFs and facilitator mathematical bibliography, inventoried in tmp/bonus-weeks-35-51/base-week-46.txt. These are original extensions; identify precise source title/page if adapting a downloaded problem. Pedagogy: Math Circle by the Bay, printed pp. viii-x (PDF pp. 9-11), repeated themes and flexible depth; our chosen designs are inferences, not activities copied from that passage.

Suggested emphasis by level

K-1: Concrete material-based entries only where they genuinely work; spoken adult reading and optional adult recording. Do not force a K-1 version of all kernels.
Grades 2-3: Independent manipulation, drawing or a small finite outcome collection with counting; proofs can use pairings and examples.
Grades 4-5: New design, optimality, changed-rule tests or systematic completeness explanations through elementary models. No formal undergraduate prerequisites.

Materials

Reuse the base week materials where possible. Specify actual kit counts for one pair and for the eleven-child KK11 / 3333 / 445 group; three anchored adults. Add only realistic paper, counters, tracing sheets, rigid frames, string or cards. Print boards large enough for use, with at least 20-25 mm counter sites. Print at 100% on Letter. Digital diagrams are not physical pretests; any exact-fit or cutting procedure remains physically untested. Leave choice/wording of problems to the writer; require at least three genuinely distinct new investigations, not tiny variants of base problems.
