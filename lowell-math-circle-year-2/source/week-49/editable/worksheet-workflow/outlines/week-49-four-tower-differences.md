Week 49: Four towers and their differences

Mathematical kernels

1. Put four nonnegative whole-number heights in a cyclic order. Replace them simultaneously by the absolute differences of adjacent heights, including the last-first pair. Every integer four-tuple eventually becomes (0,0,0,0). Example: (1,4,2,0) → (3,2,2,1) → (1,0,1,2) → (1,1,1,1) → (0,0,0,0). The largest height never increases, but need not decrease every round. A complete proof uses parity: after four difference rounds all entries are even. Repeat the same fact after factoring out two; after 4k rounds the entries are multiples of 2^k while still bounded by the original maximum, so they must eventually vanish. The four-round parity fact can be established with a small two-color model; it must not be replaced by a claim that several examples prove termination.

2. Number of sites matters: with three sites, (1,0,0) leads to (1,0,1) → (1,1,0) → (0,1,1) → (1,0,1), a nonzero cycle. Four sites, values 0–5, include a seven-round example (0,1,2,4). The central investigation is dynamical termination and counterexamples, not arithmetic drill. Give an explicit paired old/new ring diagram with matching edges and outputs; all new values must use the old ring, not values overwritten mid-round. Do not generalize the integer termination claim to arbitrary real starting heights.

Sources: Daniel Shapiro, The Four-Number Game (2005), three-page explanation and parity proof: https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/d/5402/files/2014/08/4NumbersGame-18ok6xx.pdf. Local verification checked all 1,296 four-tuples with values 0–5 and the three-site cycle. This is distinct from chip-firing redistribution, averaging consensus and deterministic permutation cycles.

Suggested emphasis by level:

K–1: make adjacent tower gaps with matched blocks, replay short four-tower transformations, and seek interesting starts.
Grades 2–3: compare terminating and repeating small rings; explain why the maximum cannot increase.
Grades 4–5: investigate the parity shadow and the boundedness/divisibility termination argument; full proof is a readiness-based continuation.

Materials

Each child: two four-station ring mats with stations at least 40 mm wide, a reusable clockwise edge-to-output guide, and either at least 32 identical snap cubes for heights up to four on both mats or reusable small number cards plus an erasable surface. For the three youngest, reserve 96 cubes so each child can work independently. Older groups may use number cards; larger chosen values must not be restricted merely by block supply. Supply a separate three-station mat for the changed-rule investigation. Keep old and new states visible simultaneously. A short strip of two-color parity markers is optional; no long subtraction table is required.
