# Week 86 independent final-pair review

**PASS — 2026-10-17.** Independently reviewed the complete final student/material/guide set. No required corrections remain. All activities remain unpiloted and physically unrehearsed.

## Complete page coverage

Rendered and visually inspected shared pp.1–4, upper pp.1–6, materials pp.1–3 and facilitator pp.1–6: **19 pages**. Read all guide explanations against the printed boards and task numbering. The path launch shows one unchanged graph, C moving one road, then R staying, with the turn explicitly changing. Fold guidance shows the original neighborhoods, their inclusion and the resulting reduced graph. The fold test uses the current uncovered graph while preserving an original reference. Removable opaque covers correctly replace the earlier impractical idea of erasing printed roads through a sleeve.

Working diagrams have readable labels, separate dots and large counter spaces. Shared triangle/square/five-/six-cycle boards supply meaningful contrasts. The design boards avoid accidental collinear-dot ambiguity. Two-cop rules allow one move or stay per cop and the six-cycle starts both cops at a, preserving a real coordination question. The eight-cycle/general question is retained for a deeper visit. All pages are unclipped and legible.

A provisional concern about the upper circles on materials pp.1–2 was **retracted** after original-detail page viewing, enlarged crops and the reviser's separate renderer confirmed complete circles in the same unchanged PDF (hash below). No unnecessary geometry change was made.

## Mathematics and guide agreement

Checked the guide's assumptions: finite connected undirected graphs, visible positions, cop placement and first move, allowed stays, immediate capture. The tree proof shrinks the robber's component rather than incorrectly asserting distance decreases every round. The cycle strategy accounts for both a cop stay and either move; finite experimental survival is distinguished from perpetual evasion.

Checked path starts and worst-case counts (5 vertices →2 cop moves;7 →3); both tree starts c; triangle/square contrast; minimum square/pentagon added chords1/2; the one-chord pentagon's retraction onto a square; triangle-with-tail versus bare six-cycle examples; exact F1 fold sequence and only F2 initial folds b→a or b→c. Verified both directions of fold preservation and the no-dominated-vertex evasion argument underlying the full classification. The two-cop blocker-and-sweep argument applies to arbitrary finite cycles and does not claim all graphs need only two cops.

An independently written finite game solver (no author-code imports) verified cycles3–9 with one and two cops, every square/pentagon chord subset and the printed fold claims. The separate portable checker passed55 graph cases and verified that the common-entry Q6 two-cop minimax is3, whereas free optimal placement would trivialize it to1. General proofs remain in the guide; these computations are supporting checks.

The theorem-first guide includes concrete launch, prerequisites, realistic older-table staffing, preparation, first route, later visits, hints, complete solutions and source limits. No independent K–1 packet is claimed. The six-road design restriction has a mathematical purpose: exclude the already-understood tree answer and challenge the false claim that any cycle guarantees evasion.

## Clean-source reconstruction

Copied the source into a separate review directory and ran only that copy's `build.py --out ... --work ...`, with no private inputs or network. All four output PDFs were byte-identical to the reviewed finals. Full ZIP extraction remains the coordinator's following release step.

| PDF | Pages | SHA-256 |
|---|---:|---|
| week-86-shared.pdf |4|f20f41ba2817745e0c7821d63718122fb35b5ed9624e00324d13b6f4987c1fbd|
| week-86-upper.pdf |6|d98525f8fc2e7335e1ec4dea8d623d4d99ebcd0ac791e1f6c92273472d07a3bf|
| week-86-materials.pdf |3|040cd4c03ceb15bdd957b2a6acdb0718612551842075f0854f2592f0cce9b96b|
| week-86-facilitator.pdf |6|172d0a6cbd94b01f6e23c8bddcea7bd5e686191b8340464c44fc53641d5557ca|

Physical printing, token fit, cover handling, preparation time and classroom use have not been tested. The guide says so directly and makes rehearsal a separate practical check.
