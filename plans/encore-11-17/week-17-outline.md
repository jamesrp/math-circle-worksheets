Week 17: Machine memory: patterns, combined memories and a limit

Mathematical kernels

1. A deterministic red/blue machine detecting whether RR has appeared anywhere needs exactly three states: no pending R, one pending R, and already seen RR. Start NO,NO,YES; R transitions 0→1→2→2, B transitions 0→0,1→0,2→2. Histories empty,R,RR are pairwise distinguishable: R separates first two, stopping separates RR from both. This is an absorbing occurrence detector, distinct from the base suffix RB machine.

2. To accept exactly when both red count and blue count are even, including no cards, four parity-pair states suffice and are necessary. R toggles the first coordinate, B the second; only even/even accepts. Histories empty,R,B,RB reach four different parity pairs; append the letters that bring one chosen pair to even/even to distinguish it from every other pair. Combining two memories is a new product construction with a concrete four-corner board entry.

3. No fixed finite-state red/blue machine can accept exactly rows with equal numbers of red and blue, for arbitrary length. For a machine with m states, the m+1 histories empty,R,...,R^m force two to share a state. If R^i and R^j share with i<j, append i blue cards: one balanced row must accept, the other must reject, but deterministic continuations from the same state agree. This is an elementary unbounded-memory obstruction. Let children test proposed small machines and find a pair of histories plus common ending; no pumping lemma or undergraduate prerequisites. Finite tests alone cannot certify all-length correctness.

Sources: Original local investigations and proofs from the familiar mathematical objects in the existing Week 17 guide. Existing guide references supply mathematical context, not copied exercises. Teaching sources consulted: Math Circle by the Bay, Preface pp. vii–x (PDF pp. 8–11); original year-1 Handouts 6, Problems 6.2–6.6, contrast representations of the same combinatorics. Specific teaching adaptations here are local planning choices, not source-reported outcomes.

Suggested emphasis by level: K–1/2–3: operate the RR detector with a partner, adult draws arrows. Grades 2–3/4–5: two parity memories. Grades 4–5: challenge any proposed fixed finite equal-count machine using histories and one common continuation.

Materials

For a pair, 12 R cards, 12 B cards labeled as well as colored, one marker, blank 4 cm state discs, pencils. Used cards hidden; current state is the whole memory. Exact one R and one B outgoing transition per state, fixed YES/NO, designated start. A stop signal adds no memory. Single-sided US Letter, actual size. Preparation counts are proposed, stock and physical procedures untested.

Scope and layout constraints

Create exactly three genuinely distinct new investigations, one per kernel, as a separate return-visit shared collection. At least one substantial numbered problem per investigation; normally one page each, add a second only if needed. Use band/readiness header per page, not three forced duplicate band packets. New output for this workflow is draft/return-visit.pdf (and final/return-visit.pdf after revision); this explicit delegated layout overrides the harness three-file default. Number problems consecutively. Do not print adult hints, theorem, solution or method. Give board/workspace where the child uses the page. Retain familiar shared conventions, show a small visual worked convention only where a representation is new. Existing base PDFs and Week 1 encore are read-only. This packet is draft/unpiloted review material; delivery is explicitly authorized.
