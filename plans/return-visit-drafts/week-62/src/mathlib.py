"""Small standard-library helpers for checking Week 62 return-visit instances.

Networks are given as strings of two-letter lines, e.g. "AB BC".
"""
from itertools import product
from collections import deque


def parse(lines):
    edges = [tuple(e) for e in lines.split()]
    nodes = sorted({v for e in edges for v in e})
    return nodes, edges


def adj(nodes, edges):
    a = {v: set() for v in nodes}
    for u, v in edges:
        a[u].add(v)
        a[v].add(u)
    return a


def list_schedules(lines, lists, extra_nodes=""):
    """All schedules: each card in one of its own slots, no line same slot."""
    nodes, edges = parse(lines)
    nodes = sorted(set(nodes) | set(extra_nodes) | set(lists))
    out = []
    for choice in product(*[sorted(lists[v]) for v in nodes]):
        s = dict(zip(nodes, choice))
        if all(s[u] != s[v] for u, v in edges):
            out.append(s)
    return out


def all_schedules(lines, k):
    nodes, edges = parse(lines)
    return list_schedules(lines, {v: set(range(1, k + 1)) for v in nodes})


def key(s):
    return tuple(sorted(s.items()))


def moves_from(s, edges_adj, k):
    for v in s:
        for c in range(1, k + 1):
            if c != s[v] and all(s[w] != c for w in edges_adj[v]):
                t = dict(s)
                t[v] = c
                yield (v, c), t


def bfs_moves(lines, k, start, goal):
    """Fewest single moves from start to goal (dicts). Returns (n, path) or (None, None)."""
    nodes, edges = parse(lines)
    a = adj(nodes, edges)
    sk, gk = key(start), key(goal)
    prev = {sk: None}
    q = deque([start])
    while q:
        s = q.popleft()
        if key(s) == gk:
            path = []
            cur = gk
            while prev[cur] is not None:
                p, mv = prev[cur]
                path.append(mv)
                cur = p
            return len(path), list(reversed(path))
        for mv, t in moves_from(s, a, k):
            tk = key(t)
            if tk not in prev:
                prev[tk] = (key(s), mv)
                q.append(t)
    return None, None


def components(lines, k):
    nodes, edges = parse(lines)
    a = adj(nodes, edges)
    scheds = all_schedules(lines, k)
    seen = {}
    comps = []
    for s in scheds:
        if key(s) in seen:
            continue
        comp = [s]
        seen[key(s)] = len(comps)
        q = deque([s])
        while q:
            x = q.popleft()
            for _, t in moves_from(x, a, k):
                if key(t) not in seen:
                    seen[key(t)] = len(comps)
                    comp.append(t)
                    q.append(t)
        comps.append(comp)
    return comps


def stuck(lines, k):
    nodes, edges = parse(lines)
    a = adj(nodes, edges)
    return [s for s in all_schedules(lines, k) if not any(True for _ in moves_from(s, a, k))]


def parse_state(word):
    return {w[0]: int(w[1:]) for w in word.split()}


def ring_name(n):
    return " ".join("ABCDEFGH"[i] + "ABCDEFGH"[(i + 1) % n] for i in range(n))


# ---------- arrows ----------

def earliest(arrows, nodes):
    preds = {v: [] for v in nodes}
    for u, v in arrows:
        preds[v].append(u)
    slot = {}
    changed = True
    while len(slot) < len(nodes):
        progress = False
        for v in nodes:
            if v in slot:
                continue
            if all(p in slot for p in preds[v]):
                slot[v] = 1 + max([slot[p] for p in preds[v]], default=0)
                progress = True
        if not progress:
            return None  # circle
    return slot


def longest_path_cards(arrows, nodes):
    succ = {v: [] for v in nodes}
    for u, v in arrows:
        succ[u].append(v)
    best = {}

    def go(v, stack):
        if v in stack:
            raise ValueError("circle")
        if v in best:
            return best[v]
        r = 1 + max([go(w, stack | {v}) for w in succ[v]], default=0)
        best[v] = r
        return r
    try:
        return max(go(v, frozenset()) for v in nodes)
    except ValueError:
        return None


def fewest_slots_arrows(arrows, nodes, kmax=8):
    """Brute force the fewest slots for an arrow network (None if circle)."""
    for k in range(1, kmax + 1):
        for choice in product(range(1, k + 1), repeat=len(nodes)):
            s = dict(zip(nodes, choice))
            if all(s[u] < s[v] for u, v in arrows):
                return k
    return None


def orientation_min_longest(lines):
    nodes, edges = parse(lines)
    best = None
    dist = {}
    for bits in product([0, 1], repeat=len(edges)):
        arr = [(u, v) if b == 0 else (v, u) for (u, v), b in zip(edges, bits)]
        lp = longest_path_cards(arr, nodes)
        if lp is None:
            continue
        dist[lp] = dist.get(lp, 0) + 1
        if best is None or lp < best:
            best = lp
    return best, dist
