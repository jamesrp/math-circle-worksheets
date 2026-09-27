# GA-01–08 maker PDF review

September 25, 2026. Maker review is complete; independent PDF review remains a separate release gate. Independent design review is closed in `review-ga1-design.md`.

## Current preview

The current preview is `tmp/pdfs/atlas-remaining/ga1-preview-v5/`:

- `atlas-ga1-student-worksheets.pdf`: 26 pages, including one contents page and all 25 planned student pages.
- `atlas-ga1-facilitator-guide.pdf`: 40 pages, including one contents page.
- `qa/student/` and `qa/facilitator/`: every page rendered at 100 dpi, extracted text, contact sheets, and build reports.

Student PDF SHA-256: `10ca7eb2a01f9cdd1f9802f59bc4c821127a1803e4f5a0346d708d0c172c9916`.

Guide PDF SHA-256: `73a31aaf01177d1b5a0d6b9b51cff2e0c670bbca81028a59396e3034d719a5a3`.

The custom source is `lowell-math-circle-year-2/source/atlas-remaining/ga1.py`. It uses `common.start` and `common.question`; all 55 student prompts are recorded and printed exactly once. The guide contains all 55 corresponding solutions/hint sets and all 13 solved optional extensions. No worked figures are added to the guide.

## Actual visual coverage

Every student page, 1–26, was inspected at full size in `ga1-preview`. The repaired pages 4, 5, 6, 11, 13, 20, 23 and 24 were then inspected at full size under the fresh `ga1-preview-v2` path. A byte comparison of all student PNGs confirms these are the only changed pages between those builds. Between v2 and v3, only student contents page 1 changed; it was inspected full size. Thus every final student page body is either the reviewed original or the reviewed repair, with byte identity checked rather than assumed.

All 42 v2 guide pages were inspected on five contact sheets. After the editor removed repetitive verification-only spill pages, all 40 v3 guide pages were inspected again on five new contact sheets. Current guide pages 1, 10, 13, 15, 18, 22, 29, 32, 34, 37, 38, 39 and 40 received additional full-size inspection for dense calculations, the complex-coordinate argument, composition identities, the complete calculus classification, source scope and the new contents layout. Apparent stale-image heading collisions were checked against saved paragraph bounds and fresh image paths; actual current paragraphs have their intended 7-point heading separation. No shared layout change was made on that basis.

The following mathematical diagram properties were checked against the data and prompts:

- GA-01: fixed room-axis labels, explicit directions of both quarter-turns, reset instructions, turn-card tracking and blank results; the face marks do not reveal the hidden-twist construction.
- GA-02: the repeated six-post height sequence, two sets of endpoint heights, three-spacings opposition, and a separately scaled three-spacings bracket over the blank design grid. The continuation pages delay the sign-exchange proof until after the learner's attempt.
- GA-03: illustrative point line, positive-width interval work, independent assigned-cost ledger and rational enumeration grid. Tiny late intervals are not falsely rendered to scale, and the rule rather than a finite picture must cover every index.
- GA-04: legal-root doubling rule; dials with no printed answer root; continuous and signed route records, including two route panels for the two requested routes. No branch-switching solution is pictured.
- GA-05: original path versus the added a–c edge, square fixed nodes versus round averaging nodes, and enough blank area for the attempted hidden-maximum network. The shortcut arch does not pass through b.
- GA-06: two separate labeled Argand grids for the two complex coordinates; the figure is not represented as a complete real planar picture of the solution set. Coordinate-change workspace remains blank.
- GA-07: correct unit-circle angle rays and input projection, the two-column input/output record and blank polynomial work. The trial angles are supplied tests, while the polynomial coefficients and composition proof remain for the learner.
- GA-08: prominent calculus prerequisites, labeled time/height axes with no answer curves, and separate left/right difference-quotient work areas. Waiting time, the derivative at its join, the forever-zero case and the full classification are retained in the prompts and guide.

## Repairs made and verified

1. Moved the top 90-degree labels inside the GA-01/04 dials and GA-07 unit circle to separate them from diagram titles.
2. Gave GA-02's blank fence grid its own opposition bracket at its actual physical scale.
3. Removed a facilitator-facing staging sentence from the GA-02 student introduction; staging remains in the guide.
4. Provided two signed-route records on the GA-04 continuation, as the prompt requests two routes, and removed an unrequested general-rule workspace label.
5. Added vertical space above the GA-08 axes on its first two pages.
6. Rebuilt after the editor moved the generic check/untested note onto the guide contents. The two near-empty verification-only pages disappeared; the current contents and all guide contact sheets were rechecked.

All repaired student pages were inspected under new output paths. Sources and solutions are confined to the guide. The student work areas are deliberately generous; several pages have room for a failed attempt and a repaired argument.

## Mechanical and mathematical evidence

The current build reports zero blank pages, zero out-of-page text characters and zero suspect glyphs in either book. Assigned-family validation, unique prompt IDs, complete keys, exactly-once prompt coverage, planned student page counts and stable contents pagination pass. Contents gates are readable, and GA-08 explicitly says calculus is required.

`python3 plans/atlas/worksheet-expansion/ga1-checks.py` passes: 8 families, 25 student pages, 55 keyed prompts, nine check groups. Those checks include finite rotation-word enumeration, exact affine crossing values, covering sums/enumeration, root-turn identities, rational averaging-network calculations, Gaussian-integer coordinates and factorization, polynomial identities, and the chosen calculus algebra/quotient instances. They support the written universal arguments; they are not claimed as substitutes for proof. The independent reviewer separately solved all 55 tasks and all 13 extensions.

The data status was updated after the build; that status field is not rendered. Final combined books have not been produced by this author. No extra artifact marker was run. Classroom engagement, timing and preparation remain unpiloted proposals. Independent PDF review and the editor's final assembly checks remain pending.

## Independent-review repair pass

The independent PDF reviewer found two small GA-04 issues after the maker pass: the prompt 6 workspace said “Three legal roots” before learners found their number, and the formal exponential in the no-switch proof silently assumed radians after degree-based student tasks. Removed “Three” and used `exp(iπθ(s)/360)`, explicitly keeping θ in degrees. Both repaired pages were maker-inspected at full size in fresh `ga1-preview-v5`. Byte comparison against v3 shows only student page 13 and guide page 18 changed; all other 64 page PNGs are identical. Counts and all mechanical checks still pass. The fresh preview and identity evidence were sent to the independent reviewer for closure.
