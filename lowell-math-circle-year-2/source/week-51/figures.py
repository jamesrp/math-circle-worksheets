"""Week 51 figures, carried over from the old builder
(archive-before-problem-files-2026-10-23/make.py and draw.py); the October 23 card
fixes changed launch() and nine_boards().

Coordinates are millimetres on the house 185 x 235 mm page canvas, y downward, so the
default page template in problem-files/canvas.py is the old builder's page. Problem
files call these functions by name in their `figure` sections; the wording lives in
the problem files.
"""
from canvas import BS, text, label, line, rect


# ---------------------------------------------------------------- shared pictures

def ruler(x, y, n=16, u=10, labels=True):
    s = line(x, y, x+n*u, y)
    for i in range(n+1):
        s += line(x+i*u, y-2, x+i*u, y+2)
        if labels: s += label(x+i*u, y+6, str(i), 9)
    return s


def band(x, y, L, U, name, n=16, u=10, ht=12):
    """A strip whose end is anywhere from L to U units, its name and range above, a ruler below."""
    s = rect(x, y, L*u, ht, 'fill=gray!8')+rect(x+L*u, y, (U-L)*u, ht, 'fill=gray!32')
    s += line(x, y-2, x, y+ht+2, 'line width=1.1pt')
    s += label(x+(L+U)*u/2, y+ht/2, '?', 12)
    s += text(x, y-10, f'{name}: {L} to {U} units', w=min(180-x, n*u+10), size=11)
    s += ruler(x, y+ht+6, n, u)
    return s


def joins(x, y, a, b, u=10):
    return rect(x, y, a*u, 9, 'fill=gray!12')+label(x+a*u/2, y+4.5, 'A', 9)+rect(x+a*u, y, b*u, 9, 'fill=gray!30')+label(x+(a+b/2)*u, y+4.5, 'B', 9)


def comparison(y, same=True):
    """A + 4 above, and the same A + 1 (same=True) or B + 1 below, from one start line."""
    s = line(12, y-3, 12, y+28, 'line width=1pt')
    for yy, length, l, extra in [(y, 50, 'A', 4), (y+16, 50 if same else 40, 'A' if same else 'B', 1)]:
        s += rect(12, yy, length, 11, 'fill=gray!25' if l == 'A' else 'fill=gray!8')
        s += label(12+length/2, yy+5.5, l, 11)
        s += rect(12+length, yy, extra*10, 11, 'fill=white,line width=1pt')
        s += label(12+length+extra*5, yy+5.5, str(extra), 11)
    s += label(6, y+12, '0', 10)
    s += text(118, y, 'Smallest gap: '+BS+'rule{12mm}{.3pt}'+BS+BS+'[4mm]Largest gap: '+BS+'rule{12mm}{.3pt}', w=65, size=11)
    return s


# ---------------------------------------------------------------- problem figures, by file

def launch():  # 00: A 2-3 and B 1-2 join to 3-5; one join from the ruler's 0, A 2 and B 2, ending at 4
    s = band(6, 37, 2, 3, 'A', 7, 10, 10)+band(6, 78, 1, 2, 'B', 7, 10, 10)
    s += line(81, 61, 96, 61, '-{Stealth[length=2mm]}')+band(104, 45, 3, 5, 'A + B', 7, 10, 10)
    s += joins(104, 80, 2, 2)+label(157, 84.5, '4', 10)
    return s


def printed_pairs():  # 02: three boxed pairs on 0-8 rulers
    s = ''
    for y, vs in [(49, [(4, 6, 'A'), (3, 4, 'B')]), (111, [(4, 5, 'C'), (4, 5, 'D')]), (173, [(6, 8, 'E'), (2, 4, 'F')])]:
        s += rect(0, y-15, 185, 51, 'rounded corners=2mm,gray!55')
        for x, (L, U, l) in zip([5, 101], vs): s += band(x, y, L, U, l, 8, 10, 12)
    return s


def k1_b_cards():  # 03, K-1: A and three printed cards for B
    s = band(12, 48, 3, 4, 'A')
    for y, L, U in [(99, 3, 4), (144, 4, 5), (189, 5, 6)]: s += band(12, y, L, U, 'B')
    return s


def target_card():  # 03, grades 2-3 and 4-5: an empty ruler for B's card and the 0-9 target with 7-9 shaded
    return ruler(12, 114)+rect(12, 145, 90, 14)+rect(82, 145, 20, 14, 'fill=gray!25')+label(12, 165, '0', 10)+label(82, 165, '7', 10)+label(102, 165, '9', 10)


def nine_boards():  # 09: four 9-unit boards for the three pairs, so the count is the child's to settle
    s = ''
    for y in [116, 146, 176, 206]:
        s += rect(12, y, 90, 13)+ruler(12, y+18, 9)
    return s
