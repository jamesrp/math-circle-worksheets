# Mathematical destination and limits

Let mu(A)=AB and mu(B)=BA. The A-grown words are nested prefixes, so they define one infinite word T. True replacement pairs always contain unlike letters. This establishes the absence of AAA and BBB: every three consecutive positions contain one whole pair.

ABABA and BABAB are also impossible. If an alternating five-letter piece started on the first position of a pair, its first, third and fifth letters would be three equal consecutive parent letters. If it started on the second position, the corresponding three parent letters would be their complements. Both contradict the no-triple fact. A genuine five-letter crop therefore contains equal neighbors. Such neighbors must cross a pair boundary, fixing the alignment. In a crop, at most one tile at each end may be an incomplete pair; discarding those ends does not reveal their missing parent letters or the crop's original absolute position.

Whole-row ancestry and occurrence as a crop are different tests. ABBAABBA is not a whole A-grown row, yet it occurs inside a later genuine row. The revised AABB crop has alignment A | AB | B and keeps parent A. The periodic ABBA strip passes the simplest local bans but contains ABBAABBAAB, whose forced pairs decode to forbidden ABABA. This rejects that periodic impostor without claiming a finite search proves aperiodicity.

The infinite T has no eventual period. Every aligned four-letter block is ABBA or BAAB, producing equal neighbors arbitrarily far out. Equal neighbors begin at odd indices when indexing starts at zero. An odd eventual period would shift them inside an unlike-letter replacement pair, impossible. An even eventual period 2q gives period q after retaining every even-indexed letter, which recovers T itself. Repeated halving of a positive integer reaches an odd number, giving a contradiction. The argument covers every proposed period and every finite discarded prefix; finite printed rows alone do not.

The student and adult checkers compute the exact finite language using a justified bounded construction, independently of the infinite proof. `checks/independent_check.py` gives a binary-digit-parity model with a two-superblock completeness argument and compares all displayed strips with the final source. The adult guide contains all seven final answers and the readiness-dependent proof route.

This is labeled one-dimensional substitution mathematics, not a proof that a geometric tile set is aperiodic. Physical material handling and classroom learning remain untested.
