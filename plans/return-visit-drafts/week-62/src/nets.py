"""Positions (mm, full size) for every network used in the packets."""
import math

def ring_pos(n, side, start=90, letters="ABCDEFGH"):
    R = side / (2 * math.sin(math.pi / n))
    return {letters[i]: (R * math.cos(math.radians(start - 360 * i / n)),
                         R * math.sin(math.radians(start - 360 * i / n))) for i in range(n)}

def star_pos(centre, leaves, radius, start=90):
    n = len(leaves)
    p = {centre: (0.0, 0.0)}
    for i, v in enumerate(leaves):
        a = math.radians(start - 360 * i / n)
        p[v] = (radius * math.cos(a), radius * math.sin(a))
    return p

NETS = {}

def add(name, lines, pos):
    NETS[name] = (lines, pos)

add("PATH2", "AB", {"A": (0, 0), "B": (36, 0)})
add("PATH3", "AB BC", {"A": (0, 0), "B": (36, 0), "C": (72, 0)})
add("PATH4", "AB BC CD", {"A": (0, 0), "B": (36, 0), "C": (72, 0), "D": (108, 0)})
add("TRI", "AB BC CA", {"A": (0, 31.18), "B": (-18, 0), "C": (18, 0)})
add("SQUARE", "AB BC CD DA", {"A": (0, 36), "B": (36, 36), "C": (36, 0), "D": (0, 0)})
add("STAR3", "AB AC AD", star_pos("A", "BCD", 36))
add("STAR5", "AB AC AD AE AF", star_pos("A", "BCDEF", 38))
add("K23", "AC AD AE BC BD BE", {"A": (0, 32), "B": (0, -32), "C": (-38, 0), "D": (0, 0), "E": (38, 0)})
add("K24", "AC AD AE AF BC BD BE BF", {"A": (0, 29), "B": (0, -29), "C": (-66, 0), "D": (-22, 0), "E": (22, 0), "F": (66, 0)})
add("RING4", "AB BC CD DA", ring_pos(4, 34, start=135))
add("RING5", "AB BC CD DE EA", ring_pos(5, 36))
add("RING6", "AB BC CD DE EF FA", ring_pos(6, 34, start=90))
add("RING7", "AB BC CD DE EF FG GA", ring_pos(7, 32))
_r5 = ring_pos(5, 36)
_r5["F"] = (_r5["A"][0], _r5["A"][1] + 31)
add("RING5LEAF", "AB BC CD DE EA AF", _r5)
_r6 = ring_pos(6, 34, start=120)
_r6["G"] = (_r6["A"][0] - 34, _r6["A"][1])
_r6["H"] = (_r6["D"][0] + 34, _r6["D"][1])
add("RING6LEAVES", "AB BC CD DE EF FA AG DH", _r6)
add("TREEB", "HA HB BC HD DE DF FG", {"A": (0, 32), "H": (0, 0), "B": (-34, 0), "C": (-68, 0),
                                      "D": (34, 0), "E": (34, -32), "F": (68, 0), "G": (68, 32)})
add("TREEA", "AB BC AD BE CF", {"A": (0, 34), "B": (36, 34), "C": (72, 34), "D": (0, 0), "E": (36, 0), "F": (72, 0)})
add("PAW", "AB BC CA CD", {"A": (0, 31.18), "B": (-18, 0), "C": (18, 0), "D": (54, 0)})

# arrow networks (lines are arrows u->v)
add("DEMOARR", "AB AC", {"A": (0, 0), "B": (36, 17), "C": (36, -17)})
add("I1", "AB BC CD EB FC GH", {"A": (0, 0), "B": (36, 0), "C": (72, 0), "D": (108, 0),
                                "E": (36, 34), "F": (72, 34), "G": (54, -33), "H": (90, -33)})
add("CIRC3", "AB BC CA", {"A": (0, 31.18), "B": (18, 0), "C": (-18, 0)})
add("CHAIN5", "AB BC CD DE", {"A": (0, 0), "B": (24, 24), "C": (48, 0), "D": (72, 24), "E": (96, 0)})
_layer = {"A": (0, 0), "B": (31, 0), "C": (62, 0), "D": (15.5, -31), "E": (46.5, -31), "F": (31, -62), "G": (31, -93)}
add("LAYC", "AD BD BE CE DF EF FG", _layer)
add("LAYD", "AD BD BE CE DF EF FG ED", _layer)
_i2 = {"H": (0, 34), "A": (34, 34), "C": (68, 34), "F": (102, 17), "G": (0, 0), "D": (34, 0), "E": (68, 0), "B": (68, 68)}
add("I3", "HA AC BC CF GD DE EF", _i2)
add("I2", "HA AC BC CF GD DE EF EC", _i2)
