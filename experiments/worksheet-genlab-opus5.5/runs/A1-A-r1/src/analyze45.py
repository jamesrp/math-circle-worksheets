from tri import *
from collections import deque
import itertools

def rtype(s):
    s = sorted(s)  # [('D',..),('U',..)]
    d = [t for t in s if t[0]=='D'][0]; u = [t for t in s if t[0]=='U'][0]
    if d[1]==u[1] and d[2]==u[2]: return 'L'
    if d[1]==u[1]-1 and d[2]==u[2]: return 'R'
    if d[1]==u[1] and d[2]==u[2]-1: return 'S'
    raise ValueError(s)

def ribbons(tiling, region):
    """list of ribbon words, from top edges left to right"""
    pieces = [s for _, s in tiling]
    # horizontal edge -> piece below it (piece containing edge as top edge)
    top = {}
    for s in pieces:
        t = rtype(s)
        if t == 'S': continue
        d = [x for x in s if x[0]=='D'][0]; u = [x for x in s if x[0]=='U'][0]
        # top edge of the rhombus is the top edge of D: P(i,j+1)-P(i+1,j+1); bottom edge is bottom edge of U
        k,i,j = d
        top[((i, j+1), (i+1, j+1))] = (s, t, u)
    ys = [v[1] for t in region for v in verts(t)]
    jmax = max(ys)
    starts = sorted([e for e in top if e[0][1]==jmax], key=lambda e: e[0][0])
    words = []
    for e in starts:
        w = ''
        while e in top:
            s, t, u = top[e]
            w += t
            k,i,j = u
            e = ((i, j), (i+1, j))
        words.append(w)
    return words

def flipgraph(region):
    T = tilings(region)
    keys = [frozenset(s for _, s in t) for t in T]
    adj = {k: [] for k in keys}
    for a, b in itertools.combinations(keys, 2):
        if len(a - b) == 3:
            tri_a = frozenset().union(*(a - b))
            if len(tri_a) == 6 and any(tri_a == hex_around(i, j) for (k, i, j) in tri_a for _ in [0]) :
                pass
            # check union is a unit hexagon
            ok = False
            for t in tri_a:
                for v in verts(t):
                    if hex_around(*v) == tri_a: ok = True
            if ok:
                adj[a].append(b); adj[b].append(a)
    return T, keys, adj

def dists(adj, src):
    d = {src: 0}; q = deque([src])
    while q:
        x = q.popleft()
        for y in adj[x]:
            if y not in d:
                d[y] = d[x] + 1; q.append(y)
    return d

if __name__ == '__main__':
    for abc in [(1,2,2),(1,2,3),(2,2,2),(1,3,1)]:
        R, poly = hexagon(*abc)
        T, keys, adj = flipgraph(R)
        words = [tuple(ribbons(t, R)) for t in T]
        print(abc, len(T), 'distinct ribbon tuples', len(set(words)))
        diam = 0
        for k in keys:
            dd = dists(adj, k); diam = max(diam, max(dd.values()))
        print(' diameter', diam, 'edges', sum(len(v) for v in adj.values())//2, 'degrees', sorted(len(v) for v in adj.values()))
        if abc == (1,2,2):
            for k, w in zip(keys, words):
                print('  ', w, [words[keys.index(n)] for n in adj[k]])
