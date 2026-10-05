"""Recheck every count the reconciled card's App fit and fix list give."""
from itertools import combinations, product
from fractions import Fraction as F

# face ticket -> (card, showing, hidden)
FACE = {1: ('RR', 'R', 'R'), 2: ('RR', 'R', 'R'), 3: ('RB', 'R', 'B'),
        4: ('RB', 'B', 'R'), 5: ('BB', 'B', 'B'), 6: ('BB', 'B', 'B')}
CARDS = {'RR': (1, 2), 'RB': (3, 4), 'BB': (5, 6)}

def red_bins(cup):
    """(hidden red, hidden blue) among the cup's red-showing faces."""
    hr = sum(1 for t in cup if FACE[t][1] == 'R' and FACE[t][2] == 'R')
    hb = sum(1 for t in cup if FACE[t][1] == 'R' and FACE[t][2] == 'B')
    return hr, hb

def fair(cup):
    hr, hb = red_bins(cup)
    return hr == hb and hr > 0

subsets = [s for k in range(7) for s in combinations(range(1, 7), k)]
print('subsets of six tickets:', len(subsets))
fair_all = [s for s in subsets if fair(s)]
print('fair cups (4-5 P6):', len(fair_all))
# the engine's evenGroups is true for two empty bins: cups with no red face
print('cups with both bins empty (evenGroups true, no red clue):',
      sum(1 for s in subsets if red_bins(s) == (0, 0)))
print('two-ticket fair cups (K-1 P7, 2-3 P6):', [s for s in fair_all if len(s) == 2])
alw_blue3 = [s for s in combinations(range(1, 7), 3) if red_bins(s)[1] > 0 and red_bins(s)[0] == 0]
print('three-ticket cups, red sometimes, always hides blue (K-1 P5):', alw_blue3)

# K-1 P5 under the p.3 "show its red face" reading: ticket 4 shows red face 3
def red_face_bins(cup):
    hr = hb = 0
    for t in cup:
        card = FACE[t][0]
        if card == 'RR': hr += 1
        elif card == 'RB': hb += 1   # its red face is 3, hiding blue
    return hr, hb
alt = [s for s in combinations(range(1, 7), 3) if red_face_bins(s)[1] > 0 and red_face_bins(s)[0] == 0]
print('K-1 P5 under the red-face reading:', alt)
# K-1 P4 under the red-face reading, adding 4 to {1,3}
print('K-1 P4 add 4, red-face reading (hidden red, hidden blue):', red_face_bins((1, 3, 4)))
print('K-1 P4 add 4, own-face reading:', red_bins((1, 3, 4)))

# K-1 P2: one-ticket removals that tie a red clue
print('K-1 P2 tying removals:', [t for t in range(1, 7) if fair(tuple(x for x in range(1, 7) if x != t))])
# K-1 P1 pairs: same showing color, different hidden
print('K-1 P1 pairs:', [p for p in combinations(range(1, 7), 2)
                        if FACE[p[0]][1] == FACE[p[1]][1] and FACE[p[0]][2] != FACE[p[1]][2]])

# whole-card selections
sels = [c for k in range(1, 4) for c in combinations(CARDS, k)]
print('non-empty whole-card selections:', len(sels))
for c in sels:
    cup = tuple(t for card in c for t in CARDS[card])
    print('  ', '+'.join(c), red_bins(cup), 'fair' if fair(cup) else '')
print('hidden-red bin values over whole cards:', sorted({red_bins(tuple(t for card in c for t in CARDS[card]))[0] for c in sels}))
print('hidden-blue bin values over whole cards:', sorted({red_bins(tuple(t for card in c for t in CARDS[card]))[1] for c in sels}))

# copies of whole cards: a RR, b RB; hidden red 2a of 2a+b red faces
print('copies, fair (2a = b) smallest:', min((a, b) for a in range(1, 6) for b in range(1, 6) if 2 * a == b))
print('copies, hidden red 3/4 smallest:', min((a, b) for a in range(1, 6) for b in range(1, 6) if F(2 * a, 2 * a + b) == F(3, 4)))

# 4-5 P3 partial information after a red clue (tickets 1,2,3)
for name, test in [('odd', lambda t: t % 2), ('even', lambda t: t % 2 == 0), ('3 or less', lambda t: t <= 3)]:
    surv = [t for t in (1, 2, 3) if test(t)]
    print('4-5 P3', name, '->', surv, red_bins(surv))

# bonus P1: card x L/R x L/R, red then red
hist = list(product(CARDS, 'LR', 'LR'))
rr = [h for h in hist if FACE[CARDS[h[0]]['LR'.index(h[1])]][1] == 'R' and FACE[CARDS[h[0]]['LR'.index(h[2])]][1] == 'R']
print('bonus histories:', len(hist), 'red-red:', len(rr), 'of which RR:', sum(1 for h in rr if h[0] == 'RR'))
# bonus P3: four tickets, h honest; blue report hidden weights h (blue) and 3(4-h) (red)
print('bonus P3 tie at h =', [h for h in range(5) if h == 3 * (4 - h)])
