"""Random search for clear tangled straight-line drawings of the networks.

Positions live on an integer grid; prints the best candidates for each network
so the chosen ones can be copied into nets.py by hand."""
import itertools
import random
import sys

import networkx as nx

from geom import clarity


def E(s):
    return [tuple(x) for x in s.split()]


NETS = {
    # K-1
    "k_diamond": ("ABCD", E("AB AC BC BD CD")),
    "k_fan5": ("ABCDE", E("AB BC CD EA EB EC ED")),
    "k_c6": ("ABCDEF", E("AB BC CD DE EF FA")),
    "k_prism": ("ABCDEF", E("AB BC CA DE EF FD AD BE CF")),
    "k_k5": ("ABCDE", E("AB AC AD AE BC BD BE CD CE DE")),
    # 2-3 and 4-5
    "n1": ("ABCDE", E("AB BC CD DE EA AC AD")),
    "n_k5": ("ABCDE", E("AB AC AD AE BC BD BE CD CE DE")),
    "n_k5e": ("ABCDE", E("AB AC AD AE BC BD BE CD CE")),
    "n_prism": ("ABCDEF", E("AB BC CA DE EF FD AD BE CF")),
    "n_k33": ("ABCDEF", E("AD AE AF BD BE BF CD CE CF")),
    "n_oct": ("ABCDEF", E("AB AC AD AE BC CD DE EB FB FC FD FE")),
}


def search(name, lo, hi, W=6, H=5, trials=20000, seed=1):
    verts, edges = NETS[name]
    rnd = random.Random(seed)
    grid = [(x, y) for x in range(W + 1) for y in range(H + 1)]
    best = []
    for _ in range(trials):
        pts = rnd.sample(grid, len(verts))
        pos = dict(zip(verts, pts))
        c = clarity(pos, edges)
        if not (lo <= c["n_cross"] <= hi):
            continue
        if c["vdist"] < 0.45 or c["cv"] < 0.45 or c["cc"] < 0.3 or c["ang"] < 20 or c["vangle"] < 14:
            continue
        score = min(c["vdist"], c["cv"] * 0.9, c["cc"] * 1.3) + 0.01 * c["ang"]
        best.append((score, pos, c))
    best.sort(key=lambda t: -t[0])
    return best[:5]


if __name__ == "__main__":
    for name in sys.argv[1:]:
        name, lo, hi = name.split(":")
        verts, edges = NETS[name]
        G = nx.Graph(edges)
        print(name, "planar" if nx.check_planarity(G)[0] else "NONPLANAR", len(verts), "dots", len(edges), "links")
        for score, pos, c in search(name, int(lo), int(hi)):
            print(f"  {score:.2f}", {k: v for k, v in pos.items()}, c)
