# Checks the route puzzles on ../2026-11-18-footprints.pdf (built by footprints.py).
# Rule: Pat never crosses the same bridge twice, but may stand on an island again.
# Each puzzle must have exactly one route, and dropping any one clue must leave more than one.
# The search covers every walk of 1 or more bridges in each town. Run: python3 footprints_check.py
# (The first version of this sheet, November 18 morning, had four forced-route puzzles; see git history.)
from footprints_puzzles import PUZZLES


def trails(edges):
    adj = {}
    for i, e in enumerate(edges):
        u, v = e[0], e[1]
        adj.setdefault(u, []).append((v, i))
        adj.setdefault(v, []).append((u, i))
    out = []

    def go(path, used):
        if used:
            out.append((tuple(path), tuple(used)))
        for v, i in adj[path[-1]]:
            if i not in used:
                go(path + [v], used + [i])

    for s in adj:
        go([s], [])
    return out


def count(walks, clues):
    return [w for w in walks if all(f(w) for _, f in clues)]


for p in PUZZLES:
    walks = trails(p["edges"])
    clues = p["checks"]
    sols = count(walks, clues)
    routes = ["-".join(w[0]) for w in sols]
    drops = [len(count(walks, clues[:i] + clues[i + 1:])) for i in range(len(clues))]
    print(f"Problem {p['n']}: {routes}; without each clue: {drops}; walks in town: {len(walks)}")
    assert routes == [p["answer"]], routes
    assert min(drops) > 1, drops
print("Every puzzle has exactly one route, and every clue is needed.")
