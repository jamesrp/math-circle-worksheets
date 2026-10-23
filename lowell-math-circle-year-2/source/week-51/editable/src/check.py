#!/usr/bin/env python3
"""Endpoint checks carried over from the old student builder (make.py, archived in the
repository's source/week-51/archive-before-problem-files-2026-10-23/). They are
deterministic interval bounds, not probabilities. verify_math.py runs this file;
checks.txt, which make.py wrote, records the same results."""
assert (4+3,6+4)==(7,10)
assert (13-12,15-10)==(1,5)
assert (7-6,9-5)==(1,4)
assert (4+4-(6+1),6+4-(4+1))==(1,5)
assert min(a-(12-a) for a in [7,9])==2 and max(a-(12-a) for a in [7,9])==6
assert [(a,9-a) for a in range(4,7) if 3<=9-a<=5]==[(4,5),(5,4),(6,3)]
print('PASS student endpoint checks (joins 7..10; shared gap 3, separate 1..5; long minus short 1..5; total 12 gap 2..6; fill 9: three pairs).')
