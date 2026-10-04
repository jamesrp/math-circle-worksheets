Week 36: Three-in-a-line in a nine-point world

Mathematical kernels

1. The nine points of the affine plane over the three-element field can be represented concretely by all nine combinations of three shapes and three fills. A line is a triple for which each attribute is either all the same or all different. Any two distinct points have a unique third point completing a line: keep a common attribute, otherwise use its missing third value. This is an exact finite geometry, not an arbitrary set of puzzle restrictions. The 3-by-3 array has 12 lines: three rows, three columns, and six wraparound diagonals. Ordinary tic-tac-toe has only eight lines, so the two must never be confused. Coordinates modulo three and affine terminology belong to adult explanation, not entry requirements.

2. The largest subset with no complete line has four points. Four corners of a 2-by-2 subarray are a witness. A short exact upper bound avoids a tedious 126-case list: suppose five chosen points contain no line. Their ten pairs each demand a missing completion among the four unchosen points. One unchosen point can complete at most two of those pairs: pairs completed by the same point are disjoint, since a pair sharing a chosen endpoint would violate unique completion. Four unchosen points can therefore account for at most eight pairs, fewer than ten. This is a small cap-set problem. Do not print the optimum before exploration. Finite verification independently found 12 lines, 54 four-point caps, and no five-point caps; see /workspace/shared/new-domain-expansion/symmetry-topology-checks.json. No claim is made that testing the cases proves a general cap-set theorem.

Sources: Julia Carney, SET and Finite Affine Geometry, University of Chicago REU (2021), §§1,3,5, https://www.math.uchicago.edu/~may/REU2021/REUPapers/Carney.pdf ; Tanya Khovanova's original SET Tic-Tac-Toe investigation, https://blog.tanyakhovanova.com/2020/06/set-tic-tac-toe/ . The elementary ten-pairs/eight-capacity proof above is supplied independently. Use original shape/fill art, not commercial card artwork.

Suggested emphasis by level:
K–1: Optional only after the child can apply both attributes independently; use large physical pieces to find a missing third and play cooperative three-making. If the two-attribute gate fails, use a one-attribute preparation without claiming it realizes the nine-point theorem.
Grades 2–3: Play on the nine-piece world, invent line-free collections, and try to enlarge them; avoid copying catalogs.
Grades 4–5: Seek a maximum line-free collection and explain the exact upper bound with physical pair markers or a drawing; 3-by-3 wrap diagrams are an optional second representation.

Materials

Per child: one complete set of nine 45 mm square tiles, showing one large circle/triangle/square in open/striped/solid fill; six 20 mm selection counters; one 180 mm square 3-by-3 parking mat with cells at least 55 mm. Per table: ten spare pair markers and four dishes for an optional upper proof; three blank 3-by-3 mats; one large demonstration set. Colors may supplement but never carry the two attributes alone. No commercial SET deck needed. Give an explicit example of two tiles and their unique completing tile, displaying each attribute separately with matching labels; add a near-miss example using exactly two equal fills. These clarify the rule without revealing the four-point optimum. Do not introduce the wraparound grid until children know the triple rule; its first example must show one broken-looking diagonal continuing at the opposite edge. Keeping pieces movable makes this a game/construction, not a card-classification worksheet.

Novelty and readiness: Beyond the atlas; different from Week 5 Latin-square reconstruction, existing antichains, and error-correcting codebooks. It uses affine incidence/unique completion and caps, not Hamming separation. Draft and unpiloted; youngest band conditional.
