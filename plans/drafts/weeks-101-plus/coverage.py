"""Count library themes, atlas families and drafts by catalog area and by deep-math field.

Run: python3 plans/drafts/weeks-101-plus/coverage.py
Fields are a coarse hand mapping of each concept in catalog/concepts.toml; a theme
counts once per field among its concepts. Weeks 101+ drafts are read from the
"Deep-math field" line of each draft plan.
"""
import collections, glob, os, re, tomllib

ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")
FIELD = {
    # combinatorics and counting
    **dict.fromkeys("listing-cases multiplying-choices subsets binomial recurrence bijection catalan lattice-paths inclusion-exclusion derangements partitions posets tableaux words ramsey finite-geometry polyominoes substitution tilings matchings sumsets".split(), "Combinatorics"),
    # graph theory
    **dict.fromkeys("graphs euler-trails trees graph-colouring bipartite stable-matching flows-cuts euler-formula rigidity graph-distance infinite-graphs chip-firing rotor-routing cops-and-robbers cheapest-networks series-parallel".split(), "Graph theory"),
    # number theory
    **dict.fromkeys("parity place-value balanced-ternary divisibility primes prime-factorization remainders gcd lcm euclid frobenius fermat square-remainders differences-sums diophantine-equations".split(), "Number theory"),
    # algebra and groups
    **dict.fromkeys("symmetry permutations permutation-cycles composition groups group-actions frieze-patterns chirality free-groups cayley-graphs linear-algebra-f2 linear-maps quotients finite-fields polynomials complex-numbers".split(), "Algebra and groups"),
    # geometry
    **dict.fromkeys("area length angles dissection pick area-bounds convexity nearest-regions reflection polyhedra spherical-geometry hyperbolic-geometry constant-width folding packing scaling coordinates distance-rules tropical-geometry thin-triangles stretch-maps curvature".split(), "Geometry"),
    # topology
    **dict.fromkeys("surfaces torus mobius winding knots holes persistence sperner connectedness".split(), "Topology"),
    # probability and statistics
    **dict.fromkeys("equally-likely conditional-probability expected-value fair-randomness urns nontransitive coupling random-walks inference measurement-error percolation averaging".split(), "Probability and statistics"),
    # analysis and dynamics
    **dict.fromkeys("optimal-stopping iteration chaos infinite-processes limits slope-limits continuity derivatives integrals differential-equations fourier function-distance measure-zero balance-laws".split(), "Analysis and dynamics"),
    # logic and computation
    **dict.fromkeys("deduction latin-squares information codes automata common-knowledge tomography algorithms sorting diagonal-argument ordinals infinite-games".split(), "Logic and computation"),
    # game theory and optimization
    **dict.fromkeys("backward-induction take-away-games nim copying-strategies partizan-games strategy-stealing game-length optimization fair-division voting optimal-transport equilibria".split(), "Games and optimization"),
}

def load(pattern):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, pattern))):
        with open(f, "rb") as fh:
            out.append(tomllib.load(fh))
    return out

def main():
    with open(os.path.join(ROOT, "catalog/concepts.toml"), "rb") as fh:
        concepts = tomllib.load(fh)["concepts"]
    missing = sorted(set(concepts) - set(FIELD))
    assert not missing, f"concepts without a field: {missing}"
    weeks, atlas, drafts = load("catalog/weeks/*.toml"), load("catalog/atlas/*.toml"), load("catalog/drafts/*.toml")
    area = collections.Counter(concepts[w["concepts"][0]]["area"] for w in weeks)
    print("Library themes by area of first concept:", dict(area.most_common()))
    table = collections.defaultdict(collections.Counter)
    for name, rows in (("weeks", weeks), ("atlas", atlas), ("drafts", drafts)):
        for r in rows:
            for fld in {FIELD[c] for c in r["concepts"]}:
                table[fld][name] += 1
    new = collections.Counter()
    for f in glob.glob(os.path.join(os.path.dirname(__file__), "week-1*.md")):
        m = re.search(r"\*\*Deep-math field:\*\*\s*([^.]+)\.", open(f).read())
        if m:
            new[m.group(1).strip()] += 1
    print("\n| Field | Weeks 1-100 | Atlas families | Scouted drafts |")
    print("|---|---|---|---|")
    for fld in sorted(table, key=lambda k: -table[k]["weeks"]):
        t = table[fld]
        print(f"| {fld} | {t['weeks']} | {t['atlas']} | {t['drafts']} |")
    used = collections.Counter(c for r in weeks for c in r["concepts"])
    print("\nConcepts no library week is about:", ", ".join(k for k in concepts if not used[k]))
    if new:
        print("\nWeeks 101+ drafts by stated field:", dict(new.most_common()))

if __name__ == "__main__":
    main()
