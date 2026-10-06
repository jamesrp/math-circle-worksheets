# Adversarial review: Week 67, Meeting on shortest roads

## Verdict

**Mathematics and rendering pass; clarify two operational conventions before finalizing.** The correct single Grades 3–5 packet has four substantial pages. Preserve the simultaneous three-pair test and the counterexample maps. The requested changes are small rule clarifications, not a redesign or a demand for additional age bands.

## Scope and evidence

Read the actual repository `AGENTS.md`, `README.md`, this run's complete `PROMPT.md` and `CRITIC.md`, and the LaTeX/README/checker. Rendered and visually inspected every page of `draft/students.pdf` at 120 dpi (`critic-render/page-1.png` through `page-4.png`), with text extraction as a supplementary check. PDF SHA-256: `9977a0fbebe8a08a20a7c85900291d8f4066d63886f10d901850f893f887d70b`.

Ran the writer's checker successfully: all 2,300 distinct triples on the 5-by-5 vertex grid, all 56 cube triples, and the exact tree and cycles. Independently checked the actual diagrams by the interval condition d(A,M)+d(M,B)=d(A,B), and the grid/cube coordinate-median rule. The separate kernel and exact-instance audits corroborate these statements; their recorded PDF/source fingerprints match this draft. No student sources were edited. Counter use and classroom timing remain unpiloted.

## Changes to make

1. **Medium priority, shared rules and page 3 square:** Explicitly permit a meeting dot to be one of the homes. The current phrase “a shortest route through it” can be understood by a child as strictly passing through an intermediate stop, and the physical meeting counter may appear to need a vacant dot. The square in Problem 3 has exactly one correct answer: **home B itself**. A single sentence such as “The meeting dot may also be a home” closes this ambiguity without giving away that instance. This convention also matters to the invented triples in Problem 2 and the all-choices rule in Problem 5.
2. **Medium priority, shared color rule:** Explain how to record shared roads without losing one of the routes: draw the colors beside one another where they share a road. The text permits shared roads, which is mathematically right, but the task requires three checkable colored routes. In the tree each used branch belongs to two of the pairwise routes; overtracing a narrow road with another pencil can erase the evidence. This is a prospective usability concern, not an observed classroom failure. One short convention is enough; do not prescribe a route-finding method.

## Mathematical and page-by-page audit

- **Page 1 introduction:** The non-task P–M–Q example accurately shows 2+1=3 steps and a shortest path through M. It teaches a single pair check without revealing a three-home answer. “Each pair ... has a shortest route” correctly means some shortest route per pair, not every previously chosen shortest route. Keeping all homes and the candidate fixed is explicit and valuable.
- **Page 1, Problem 1:** Taking the lower-left vertex as (0,0), the left homes are (0,0), (4,1), (1,4), with unique meeting (1,1). The right homes are (0,3), (4,0), (4,4), with unique meeting (4,3). Both are available vertices on the actual diagrams. Shortest pairwise distances are respectively 5,5,6 and 7,5,4; the proposed meetings realize all three equalities.
- **Page 2, Problem 2:** Every placement of three different homes on the full rectangular grid has exactly one meeting. The four boards provide space for contrasting attempts, and the challenge retains the children's choice. Failure to find a no-meeting/multiple-meeting configuration is evidence to investigate, not proof by itself. The later adult guide should supply the coordinate-interval argument rather than treating four trials as certification. No additional mandatory proof prompt is needed on this student page.
- **Page 3, Problem 3:** The tree's meeting is the middle vertex of the horizontal spine, directly below C's two-edge branch. The triangle graph has no meeting: the third home is excluded from the one-edge shortest path between the other two. The four-cycle's meeting is B. This trio is purposeful: unique tree meeting, genuine failure, and a cycle that still works. The statement that every drawn edge has unit length handles the uneven geometry correctly.
- **Page 4, Problem 4:** Both cube drawings have the correct 12 edges and eight binary labels; every edge changes one coordinate. The meetings are **100** on the left and **011** on the right. Every pair of homes in either printed triple is two edges apart, and the meeting is one edge from each home. The crossed-road rule is explicit; unlabeled crossings are not extra vertices.
- **Page 4, Problem 5:** Coordinatewise majority is the correct rule for every triple of cube homes. For a coordinate shared by two homes, any shortest route between those two must preserve it; the three pair tests therefore force the majority coordinate. The resulting vertex lies in each pair's interval. This is a genuine late abstraction, not an arithmetic/binary-number exercise.

## Layout, depth, and operational fit

- All four US Letter pages have correct headers/footers and Problem 1–5 numbering. No text or figure clips, missing symbols, cramped label collisions, overflow, or unnecessary decorations were found. Grid lines are visible against the vertices, with substantial spaces for marking routes.
- Working grids have roughly 15.5–16 mm vertex spacing. Small home counters should fit; use appropriately small markers and set the meeting counter beside a home marker when the two coincide. Actual counter fit was not rehearsed. The cube labels are large enough to read and leave open road segments for color marks.
- The first two pages make one representation do enough work before trees/cycles and then the cube appear. Page 3 adds genuine contrast rather than a merely harder grid. Page 4 supplies a worked label-changing convention before use.
- Counting edges and maintaining three pairwise conditions are the main Grades 3–5 prerequisites. The cube/majority explanation is a later readiness gate, accurately stated in the source README. The pupil still chooses locations and routes; the adult can read aloud without operating the investigation for them.
- Page 2 supports sustained partner play, so a fast solver is not limited to the two supplied examples. Page 3's impossibility and page 4's all-triples rule give enough mathematical depth for flexible pacing. The four-page target is justified, not merely a quota.
- Problem 5 reuses a cube map already marked in Problem 4. This is workable with erasable marks or another copy; no extra page is required, but the adult preparation should anticipate reuse.

## Revision priority

Add the home/meeting coincidence and shared-color recording conventions, keep all instances, then render and inspect the updated four pages. Nothing in this review supports weakening the median question to minimum total travel or splitting it into sequential pair checks.
