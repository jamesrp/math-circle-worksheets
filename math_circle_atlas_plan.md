# A research-to-play atlas of mathematics
## A plan for discovering, verifying, and mapping math-circle investigations

**Design principle:** map mathematical mechanisms with faithful child-accessible entrances, not advanced topic names with elementary worksheets attached.

The central object should be an **atlas**, not a curriculum and not an enormous list of lessons. A curriculum chooses a route through the atlas. A lesson instantiates one investigation. The atlas records the mathematical territory, the connections, the entrances that have been found, and the searches that remain unresolved.

This plan preserves the commissioner's existing approach: start with mathematics that is genuinely interesting at an undergraduate or research level, identify a mathematical mechanism worth thinking about, then find a concrete investigation that preserves it. Both the mathematical connection and the proposed learner access must be explicit.

The companion starter pack contains agent instructions, starter schemas, two structured prototypes, durable source references, and executable finite checks. It does not contain a populated exhaustive atlas. The prototypes are source-checked and computationally checked where specified, but are not independently reviewed or classroom-piloted.

## 1. Give “exhaustive” an auditable meaning

Use a pinned **Mathematics Subject Classification** snapshot as the research-coverage scaffold. The official MSC2020 description lists 63 top-level classifications and thousands of narrower categories, and offers downloadable forms. This provides an externally defined denominator rather than relying on an AI model to remember “all of math.” It is a research classification, not a developmental sequence. [S1]

Count nodes from the actual imported snapshot. Treat publication-format and other cross-cutting facets separately from substantive subject branches. Preserve their disposition rather than silently dropping them. The machine-readable MSC literature also cautions that classification granularity varies substantially across areas; raw counts should not be mistaken for equal amounts of mathematical territory. [S2]

Keep four coverage questions separate:

1. **Research coverage:** Did someone substantively investigate this area?
2. **Bridge coverage:** Was a faithful child-accessible entrance found to a specified idea?
3. **Design/review coverage:** Is there a mathematically checked, facilitatable investigation family?
4. **Classroom evidence:** Has that particular design been tried with a documented group?

A reviewed unsuccessful search is real research coverage. A clever puzzle linked to one theorem is not coverage of an entire discipline. A classroom success with one group is not a universal age guarantee.

### Coverage dispositions

Use explicit states: unvisited; screened; candidate bridge; faithful entry reviewed; blocked by an identified prerequisite; investigated but unresolved; delegated to a genuinely equivalent reviewed mechanism; and facet/out of scope with a stated reason.

Do not let “related to” fill a coverage cell. A symmetry puzzle may provide an exact example of a group action without covering representation theory, algebraic geometry, and category theory. Likewise, a solved parent-area puzzle does not mark all its descendant taxonomy codes reviewed.

The long-term completion criterion is **an individually justified disposition for every in-scope subject code**, not one lesson for every code. Maintain a search frontier for new mechanisms and intersections outside the current taxonomy. This makes the audit exhaustive against a known map while keeping the investigation of possible entrances open to revision.

## 2. Build three linked maps, not one tree

### The research map

Record areas, subareas, objects, constructions, theorem/problem anchors, sources, and conceptual relationships. Preserve the official taxonomy but permit multiple mathematical parents and cross-links.

### The bridge map

Record a chain such as:

**source-backed mathematical idea → structural mechanism → concrete representation → investigation family → variants**.

For tilings, “height functions” is an adult mathematical object; “change one arrangement into another by local moves” is an investigable question; small boards and manipulatives are representations. These should not be flattened into one topic label.

### The learner-access map

Record capabilities required by a particular representation and task. These can include matching, comparing, tracking a move, counting small collections, spatial rotation, recording cases, explaining an impossibility, fraction reasoning, or symbolic manipulation. Record alternative access routes rather than assuming one compulsory sequence.

Separate **enter, explore, solve, explain, and prove**. A child may participate meaningfully before being able to state or prove the general theorem. Proposed grades are useful search labels, but the capability profile and evidence should be authoritative.

Adult prerequisites must not automatically become child prerequisites. Knowing a formal definition of a group is not necessary to explore compositions of rotations. Conversely, little notation does not guarantee an easy entry. NRICH explicitly distinguishes mathematical prerequisites from the psychological difficulty of getting started. [S3]

### The essential family record

| Component | Required information |
|---|---|
| Mathematical core | Adult question; structural mechanism; exact claims and hypotheses; source locators |
| Bridge | What child objects, moves, and questions correspond to; what is preserved; what is omitted |
| Investigation | Opening challenge; meaningful decisions; possible discoveries; examples and counterexamples |
| Access | Capability prerequisites; representation alternatives; entry/solution/proof levels; grade hypotheses |
| Family | Parameters; branching questions; genuine extensions; related and duplicate mechanisms |
| Evidence | Proofs; computational checks; independent reviews; pilot records; provenance and rights |

Label bridge strength explicitly: **exact special case**, **faithful representation of a specified structure**, **shared mechanism/analogue**, or **motivation only**. The first two can justify a strong content-coverage claim, limited to the content actually established. The others may still support excellent activities, but should not impersonate stronger links.

The bridge test is concrete: can a reviewer identify the mathematical counterpart of each relevant child object and legal action, and explain why the child's question is genuinely about that structure?

## 3. Explore from several directions

A single flood fill starting from tilings will favor whatever is adjacent to tilings. Use several interacting searches.

**Top down:** start from the research taxonomy, subject surveys, and undergraduate course contents. Ask what each area studies and what its distinguishing mechanisms are.

**Bottom up:** start from successful activities, including the commissioner's existing weeks, and work backward to formal structures. JRMF and the MathCircles.org activity database provide useful comparison and discovery corpora. Their role is to suggest proven activity forms and overlooked mathematics, not to establish the age suitability of newly generated lessons. [S4, S5]

**Across proof mechanisms:** track invariance, monotonicity, recursion, induction, symmetry, double counting, extremal arguments, local-to-global reasoning, construction, approximation, randomness, and counterexamples. A familiar mechanism may supply an entrance to an unfamiliar subject.

**Across child actions:** investigate what can be done by arranging, connecting, rotating, folding, cutting, sharing, measuring, moving continuously, iterating, and communicating. Then ask which mathematical structures those actions genuinely realize.

**Against the current map:** commission adversarial searches for neglected areas, false equivalences, missing distinctions, and connections that only sound plausible.

### Seed exploration lenses

The following are proposed search directions, not claims that each area already has a validated kindergarten lesson. They supplement, rather than replace, the full taxonomy import.

| Territory | Candidate entrances to investigate |
|---|---|
| Logic, sets, foundations, infinity | Rules and consistency; sorting by properties; correspondence; finite versus infinite processes |
| Number theory | Remainders; repeated cycles; divisibility constructions; measuring with restricted tools |
| Enumerative and extremal combinatorics | Systematic construction; equivalent counting methods; unavoidable patterns |
| Graphs and networks | Routes; pairing; bottlenecks; local versus global constraints |
| Tilings, packing, discrete geometry | Possibility; local rearrangement; density; boundary effects |
| Groups, rings, fields | Compose and undo actions; investigate when order matters; finite arithmetic models |
| Linear algebra | Toggle systems; dependencies between moves; combining transformations; averaging |
| Euclidean, projective, and differential geometry | Construction; shortest routes; shadows and perspective; curved-surface experiments |
| Topology and knots | Allowed deformations; loops; gluing; holes; motion under constraints |
| Real analysis, measure, calculus | Continuous change; equality guarantees; area comparison; refinement and error bounds |
| Complex and harmonic analysis | Rotating-vector models; superposition; periodic patterns and decomposition |
| Dynamics, differential equations, PDE | Iteration; equilibria; spreading and averaging; discrete models with explicit limits |
| Probability, stochastic processes, statistics | Random walks; game fairness; sampling; inference from incomplete evidence |
| Optimization, variations, games, decisions | Best routes; fair division; constrained resources; strategic choices |
| Algorithms, complexity, information, coding | Sorting and search; state machines; communication; detecting errors |
| Mathematical physics, biology, and other applications | Conservation; balance; motion; flow; growth; comparing models with observations |
| Highly abstract structural branches | Test small genuine models and specific constructions before accepting or rejecting a bridge |

The last row is not a permission to collapse category theory, homological algebra, algebraic geometry, operator algebras, or other demanding areas into generic pattern play. Their actual branches still receive separate investigations and honest dispositions. A tiny example may realize a definition without preserving a sufficiently interesting question; that is a reason to continue searching, not to inflate coverage.

Continuous mathematics should be explored from the beginning, alongside discrete mathematics. Use a visual or physical interface where possible; introduce numerical and symbolic tools when they improve the investigation. Do not designate all continuity as a late-school subject merely because its formal development uses real analysis. Equally, distinguish a genuine infinitesimal from an ordinary small number or a repeated-halving limit. Every bridge must say which structure is actually present.

## 4. Organize the agents around evidence and artifacts

Do not ask a collection of agents to “brainstorm all mathematics” and merge their prose. Give each a bounded role, persistent state, and a checkable output.

### A. Coordinator and coverage auditor

Own the pinned taxonomy, task queue, provenance registry, canonical IDs, budgets, and coverage reports. Schedule neglected branches before allowing attractive areas to expand indefinitely. Keep research coverage, bridge quality, and classroom evidence separate.

Workers propose changes. Only a coordinating/editorial step merges records. Preserve failed attempts, disagreements, and references so work can be resumed without repeatedly rediscovering the same dead ends.

### B. Domain scouts

Begin with an accessible authoritative overview, then inspect authored texts or primary papers for the exact claims being used. Return a short mathematical dossier, not a lesson.

For a typical subarea, request three to five distinct mechanisms where available; exact theorem or construction anchors; important hypotheses; candidate concrete representations; adjacent mechanisms; and unresolved obstacles. The count is a work-budget target, not a demand to invent five results.

Use at least occasional independent scouting before sharing proposals. Different role names are not evidence of independent reasoning if every agent sees and repeats the same initial answer.

### C. Bridge designers

Work backward from a mechanism and forward from child actions. Try lower dimension, a finite case, a restricted family, one generator, a local move, a geometric encoding, or one part of a proof.

Every restriction requires rechecking the statement. A finite model can preserve an operation while losing the theorem's conclusion. The continuous example below makes this failure visible.

Require the following before polished storytelling: what the child can do first; what decisions remain open; what could be discovered; a small example; a counterexample or boundary case; and an explicit connection to the adult mathematics.

### D. Independent mathematical reviewers

Give the reviewer the child-facing rules before the proposed solution. Ask them to solve the task, challenge the hypotheses, and search for counterexamples. Review source claims and bridge fidelity, not merely the final answer.

Use exact finite enumeration, graph search, tiling solvers, rational arithmetic, or symbolic reasoning where suitable. Preserve witnesses, generators, seeds where randomness is used, and the precise domain checked. A hundred successful tests cannot justify an unrestricted theorem. A visual animation cannot establish exact equality.

### E. Facilitation and access reviewers

Review language, working-memory demands, spatial tracking, motor access, setup, group structure, hints, and the child's agency. An elementary educator's review is a different contribution from a mathematician's review. DREME's teacher and teacher-educator resources are useful sources of early-years expertise. [S6]

Ask whether a child can make productive progress without guessing the adult's intended trick. Design hints that reveal a useful observation or representation before giving the decisive idea. Permit directing a partner, manipulating large objects, drawing, explaining orally, and other participation modes.

An agent may hypothesize likely responses. It may not report simulated children as actual pilot evidence.

### F. Novelty reviewer and mathematical editor

Compare families by **objects, moves, questions, and reasoning**, not just textual similarity. Keep representational variants when they genuinely change access or insight, but do not count a new story as a new mathematical mechanism.

Apply two complementary tests: remove the famous theorem name and judge the activity; then remove the children's story and judge the mathematical connection. The commissioner's taste should calibrate the first test, while explicit structure and evidence govern the second.

Use hard gates for correctness, honest attribution, and bridge fidelity. Do not average a mathematical flaw away with high scores for engagement. Use softer ratings for agency, surprise, accessibility, extension depth, and practical reliability.

## 5. Make the iteration finite, reproducible, and informative

An initial round can proceed as follows:

**Scout → extract mechanisms → design alternative bridges → solve and attack → review access → merge or retain unresolved → update the frontier.**

Budget the loop. A reasonable initial management choice is two targeted repair attempts before a blocked candidate returns to the unresolved queue with a clear reason. Avoid both immediate rejection and endless agent debate.

A possible allocation is half the search effort for uncovered areas, one quarter for promising bridges, and the remainder for verification, repair, and adversarial or cross-field discovery. These are adjustable defaults, not empirically optimal percentages. Give demanding branches protected attention so low-effort output does not determine the shape of the atlas.

### Measure progress without rewarding padding

Report individually reviewed subject dispositions; distinct mathematical mechanisms; faithful entries at each capability level; independently verified families; unresolved questions; and actual pilot evidence. Break these down by area. Raw activity counts, citation counts, and the number of attached topic labels are poor stand-alone measures.

Maintain several independent audits: unseen syllabus topics; random subject-code checks; backward mapping of existing high-quality activities; and deliberate searches for missed continuous, applied, statistical, and abstract subjects. Keep the audit corpus separate from the corpus used to generate candidates where practical.

### Compare against the successful original prompt

Before scaling, run a deliberately diverse batch of perhaps twelve topics through both the original prompt and the new workflow under comparable budgets. Have the editor and an elementary facilitator compare anonymized outputs. Examine mathematical validity, fidelity, genuine child decisions, richness of extensions, and duplication. Pilot promising tasks rather than treating those ratings as evidence about real children.

The goal is not to replace an effective prompt with bureaucracy. It is to retain its taste while making breadth, reliability, and accumulated knowledge substantially better.

## 6. Worked example: domino flips and the topology of a configuration space

### Adult anchor

Thurston's *Conway's Tiling Groups* connects tilings with group-theoretic and height-function descriptions. Saldanha and Tomei's survey gives a useful precise anchor: for a tileable simply connected planar square-grid region, domino tilings are connected by elementary 2×2 flips. The survey also discusses the additional obstructions that can occur with holes. [S7, S8]

### Child-facing investigation

**“Can you change this floor into that floor without pulling the whole floor apart?”**

A move replaces two parallel dominoes filling a 2×2 square by the perpendicular pair. Begin with 2×2 and 2×3 boards, then 2×4. Let children choose targets and invent routes. Later, compare different routes, catalog floor plans, and ask whether every plan can reach every other plan.

Only after a reachability conjecture has become meaningful, introduce a 3×3 board with its center missing. It has two tilings, but neither has a legal flip: every possible 2×2 block includes the missing center square.

That is an accessible mathematical distinction: **having multiple solutions is different from being able to move between them under the allowed rule**.

### A complete elementary theorem inside the family

Every tiling of a 2×n rectangle can be changed into the all-vertical tiling. Examine the leftmost remaining column. It either contains a vertical domino, or its two cells belong to two horizontal dominoes covering the next column as well. In the second case, flip that pair to vertical. Fix the first column and repeat on the remaining rectangle. Each stage fixes another column, so the process ends. Reverse paths to connect any two tilings.

This proof is an algorithm and a recursive reduction; the child need not begin with formal induction terminology. The more general simply connected theorem remains an adult or later-student extension, rather than being falsely presented as proved by a few small boards.

### Proposed access ladder

K–1: build and perform legal moves. Grades 2–3: organize arrangements and routes. Grades 4–5: explain the narrow-board procedure and the frozen ring. Later: formulate a configuration graph, define height functions, examine extremal tilings and hole obstructions. These are design hypotheses, not classroom findings.

### Bridge audit and checks

A child's tiling is literally a vertex of the configuration graph; a legal flip is literally an edge. The reachability question is exactly graph connectivity. This is not just an analogy to advanced mathematics.

The included code enumerates the supplied boards and checks their flip graphs. It finds five 2×4 tilings in one connected component, 36 4×4 tilings in one connected component, and two isolated tilings for the 3×3 ring. These are exact finite checks, not the proof of the general theorem.

This family illustrates how one research source can open several distinct branches—tileability, reconfiguration, algorithms, heights, and topology—without treating all of them as one undifferentiated “tiling activity.”

## 7. Worked example: a continuous entrance to Borsuk–Ulam and numerical analysis

### Adult anchor

For a continuous real-valued height function on a circle, there is an opposite pair with equal heights. This is the circle case of the Borsuk–Ulam theorem, and it has a short intermediate-value proof. A university exercise with this exact statement and connection is listed in the sources. [S9]

### Child-facing investigation

**“Can you design a wavy circular fence so that opposite spots are NEVER at the same height?”**

Use an idealized fence with one height above each position on a circular base. Two markers stay above opposite base positions. The fence top can rise, fall, and have corners, but it cannot jump, and its seam joins continuously. A flat-strip version can support comparing the heights without the visibility problems of a cylinder.

For a younger entry, first use two markers sliding on parallel vertical tracks: exchange which one is higher without jumping. The circle model and universal claim are later steps, not prerequisites for participating in that warm-up.

### The mathematical discovery

After half a turn, the markers exchange starting positions. A marker that started higher ends lower, unless the two heights were already equal. Without a jump, they must pass through an equal-height moment.

For the adult proof, write positions as t modulo 1 and set

    g(t) = h(t) − h(t + 1/2).

Continuity of h makes g continuous, and periodicity gives g(1/2) = −g(0). If g(0) is zero, the desired pair is already found. Otherwise the endpoint signs differ, so the intermediate value theorem supplies a zero between them. [S9]

### The counterexample that protects fidelity

Now allow only six isolated posts with heights 0, 4, 1, 3, 0, 2 in circular order. No opposite posts match. Join the same posts by continuous straight ramps, and equalities must appear between posts. Thus discretizing the available positions can destroy the conclusion even while the picture looks similar.

A discontinuous profile also defeats the claim: height zero on the first half-open semicircle and one on the other. Opposite heights always differ. These are opportunities to discover why a theorem's assumptions matter, rather than merely to recite its conclusion.

### Genuine routes upward

Numerical learners can retain a bracket where the height difference changes sign and repeatedly halve it. Later, students can formalize error bounds and compare this bracketing method with Newton iteration on suitably smooth functions. Newton requires extra structure and need not converge from an arbitrary starting point; MIT's numerical-analysis material gives this as a substantive issue, not a footnote. [S10]

For a checked older-student counterexample, Newton's method on f(x)=x³−2x+2 starting at zero cycles 0→1→0. The supplied script verifies that calculation exactly. It also checks the antipodal equalities of 1,080 specified periodic piecewise-linear profiles using rational arithmetic. The universal circle theorem rests on the argument above, not on those tests.

The entry need not use numbers. The same family can later ask about proof, approximation, algorithms, and higher-dimensional topology. This is a meaningful continuous strand from the outset, not a disguised arithmetic worksheet.

## 8. Build in stages, with acceptance criteria

### First: establish taste and the minimal infrastructure

Ingest the commissioner's existing activities when supplied. Select accepted examples and deliberately rejected near misses. Establish the source registry, stable IDs, schemas, coverage ledger, task queue, and evidence vocabulary. Reproduce the included example checks. Keep the implementation in versioned files and a simple searchable index first.

### Second: make a breadth-first research map

Give every top-level field an actual dossier, including areas expected to be difficult. Follow with substantive subarea screening. Investigate a deliberately varied sample deeply enough to test the workflow: discrete, algebraic, geometric, continuous, probabilistic, applied, and abstract structural cases.

Publish the map and its unresolved frontier before generating a large lesson library. This makes neglected territory visible while it is still cheap to change course.

### Third: deepen, challenge, and pilot

Refine from subareas to individually justified leaf dispositions. Generate families only for worthwhile candidate mechanisms. Conduct independent review, trial a diverse subset with children, and revise capability labels, hints, and representations from real observations.

Pilot records should describe the setting, facilitator version, capabilities, independent actions, spontaneous observations, hints needed, and failures. Use the organizer's appropriate consent and privacy practices; do not collect identifying information unnecessarily. Repeated trials improve confidence without converting local evidence into universal claims.

### Fourth: assemble programs from the atlas

Only after the atlas is useful should a session or term planner choose paths through it. It can balance mathematical topics, reasoning mechanisms, physical formats, and prerequisite capabilities. Reuse a mechanism across different subjects when that creates transfer and new insight. Do not force a single accelerated school sequence on the atlas.

## 9. Handoff instruction

> Build a versioned research-to-play atlas, not a collection of worksheets. Use a pinned external mathematics taxonomy for coverage, and separate it from both the bridge graph and learner prerequisites. For every investigated mechanism, preserve a precise undergraduate or research anchor and its hypotheses; identify concrete objects, legal actions, and genuine child decisions; state what could be discovered and why the connection is faithful. Record examples, counterexamples, proof obligations, capability prerequisites, proposed grade bands, and explicit uncertainty. Independently solve and challenge candidate tasks before polishing them. Do not count a thematic analogy as content coverage, a finite test as a general proof, or a simulated child as classroom evidence. Preserve unsuccessful searches and revisit them when new representations become available. Begin with breadth, calibrate against the existing successful activities, and return an auditable frontier before mass-producing lessons.

The essential editorial question remains:

**What is the smallest honest mathematical world in which a child can encounter this idea, make choices, and discover something worth explaining?**

That question preserves the flavor of the original approach while allowing the search to scale across the discipline.

## Sources and locators

Sources were accessed on 25 September 2026. These references support the mathematical anchors, research scaffold, and pedagogical precedents; the architecture, workflows, proposed activities, budgets, and suggested age bands are design proposals.

- **S1 — MSC2020.** Mathematical Reviews and zbMATH, official classification information and downloads. https://msc2020.org/ . The official distribution specifies CC-BY-NC-SA; inspect terms before redistribution or incorporation into a product.
- **S2 — Arndt et al. (2021).** *10 Years Later: The Mathematics Subject Classification and Linked Open Data*. https://arxiv.org/abs/2107.13877 . Introduction and section 1.1.
- **S3 — NRICH, University of Cambridge.** *Low Threshold High Ceiling — An Introduction*. https://nrich.maths.org/articles/low-threshold-high-ceiling-introduction . Especially the distinction between mathematical and psychological thresholds.
- **S4 — Julia Robinson Mathematics Festival.** Puzzle library. https://jrmf.org/puzzle/?filter=recommended . Use as an activity-design and discovery corpus, with appropriate attribution and rights.
- **S5 — MathCircles.org.** Math Circle Activity Database. https://mathcircles.org/activities/ . Activity listings, mathematical topics, representations, and audience filters.
- **S6 — Stanford DREME Network.** Teacher and teacher-educator resources. https://dreme.stanford.edu/ . Source of early-years instructional expertise, not validation of these prototypes.
- **S7 — Thurston (1990).** *Conway's Tiling Groups*, American Mathematical Monthly 97(8), 757–773. https://www.ibr.cs.tu-bs.de/users/fekete/oldhp/Sem06/thurston.pdf . Relevant height-function material on printed pages 767–768; inspected as page images.
- **S8 — Saldanha and Tomei (1998).** *An overview of domino and lozenge tilings*. https://arxiv.org/abs/math/9801111 . Section 3, Theorem 3.1 and the hole/flow discussion; PDF pages 12–13 inspected.
- **S9 — Queen Mary University of London.** MTH5104 Convergence and Continuity (2012–13), exercise sheet 10 solutions, exercise 7 and comment, PDF page 3. https://maths.qmul.ac.uk/~sb/MTH5104/exercise_sheets/cc2012ex10sol.pdf . Exact circle statement and intermediate-value proof.
- **S10 — MIT OpenCourseWare (2013).** *Math, Numerics, and Programming (for Mechanical Engineers)*, Unit 6, section 29.2, especially 29.2.5 on Newton pathologies. https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-spring-2013/60af88c658ba3e83cdf7c43289aeb5b4_MIT2_086S13_Unit6_Textbook.pdf .
