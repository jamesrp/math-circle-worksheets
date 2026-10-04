Week 48 bonus: Inside and outside covers

Mathematical kernels

1. Changing a grid origin at the SAME cell size is not nested refinement and can improve or worsen inner/outer bounds. A unit square aligned to grid has exact bounds 1,1; shifted against grid may have 0,4. Shapes stay fixed while transparent grids move. Use polygons whose status is unambiguous and independently compute cover counts for each placement.

2. Two certified enclosures [L1,U1] and [L2,U2] for the SAME shape combine by intersection [max L,min U], and may be tighter than either alone. One need not refine every cell or average the estimates. Choose overlapping-grid certificates where each is better at one end, and include an impossible pair of claimed certificates. This is certificate combination, distinct from base grid refinement.

3. The same inside/partial/outside cell pattern can hide very different areas. Within partial cells a connected polygon may fill arbitrarily little or almost all of each cell while leaving every marked cell partial. Construct contrasting silhouettes consistent with a small mask; show why the mask provides bounds rather than an exact area. State whether holes and disconnected pieces are allowed, and give explicit verified witnesses rather than a pathological-set limit theorem.

Sources: Existing Week 48 outline, final base PDFs and facilitator mathematical bibliography, inventoried in tmp/bonus-weeks-35-51/base-week-48.txt. These are original extensions; identify precise source title/page if adapting a downloaded problem. Pedagogy: Math Circle by the Bay, printed pp. viii-x (PDF pp. 9-11), repeated themes and flexible depth; our chosen designs are inferences, not activities copied from that passage.

Suggested emphasis by level

K-1: Concrete material-based entries only where they genuinely work; spoken adult reading and optional adult recording. Do not force a K-1 version of all kernels.
Grades 2-3: Independent manipulation, drawing or a small finite outcome collection with counting; proofs can use pairings and examples.
Grades 4-5: New design, optimality, changed-rule tests or systematic completeness explanations through elementary models. No formal undergraduate prerequisites.

Materials

Reuse the base week materials where possible. Specify actual kit counts for one pair and for the eleven-child KK11 / 3333 / 445 group; three anchored adults. Add only realistic paper, counters, tracing sheets, rigid frames, string or cards. Print boards large enough for use, with at least 20-25 mm counter sites. Print at 100% on Letter. Digital diagrams are not physical pretests; any exact-fit or cutting procedure remains physically untested. Leave choice/wording of problems to the writer; require at least three genuinely distinct new investigations, not tiny variants of base problems.
