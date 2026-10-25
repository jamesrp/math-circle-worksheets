"""Recompute every answer the facilitator guide prints, against the final student pages.

Run:  python3 check_guide.py          (needs networkx, pdflatex, pdftotext)

1. Rebuilds the student figures from a temporary copy of the pages' sources and checks that
   the copied data in netdata.py (pictures, link lists, portal boards, game boards) matches
   what was printed; reads the final PDFs' text for link lists and problem/page numbers, and
   checks the guide's "Problem N, page P" headings against them.
2. Recomputes the mathematics: network types, untangled drawings and region counts, fewest
   crossings, the impossibility arguments, the link game, and the portal-board drawings.
3. Revision checks, read back from the generated figures: the bent launch link (C-D round B),
   the K-1 key's fewest-crossing drawings, the numbered exits on the portal drawings, the
   Grades 2-3 split, and the first-hour time budget.
"""
import collections
import itertools
import math
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile

import networkx as nx

import netdata as N

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.dirname(HERE)
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.append(s)


def check(cond, msg):
    if not cond:
        say("FAIL:", msg)
        raise SystemExit(1)


# ====================================================================== 1. agreement with the pages
def rebuild_student_figures():
    tmp = tempfile.mkdtemp(prefix="un-pages-")
    for f in os.listdir(os.path.join(PAGES, "src")):
        shutil.copy(os.path.join(PAGES, "src", f), tmp)
    subprocess.run([sys.executable, "nets.py"], cwd=tmp, check=True, stdout=subprocess.DEVNULL)
    return tmp


NUM = r"(-?\d+\.\d+)"


def parse_picture(path):
    txt = open(path).read()
    segs = [((float(a), float(b)), (float(c), float(d))) for a, b, c, d in
            re.findall(r"\\draw\[line width=[\d.]+pt\] \(" + NUM + "," + NUM + r"\) -- \(" + NUM + "," + NUM + r"\);", txt)]
    nodes = {lab: (float(x), float(y)) for x, y, lab in re.findall(r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{([A-G])\};", txt)}
    links = set()
    for p, q in segs:
        a = min(nodes, key=lambda v: math.dist(nodes[v], p))
        b = min(nodes, key=lambda v: math.dist(nodes[v], q))
        check(math.dist(nodes[a], p) < 0.15 and math.dist(nodes[b], q) < 0.15, f"segment end off a dot in {path}")
        links.add(frozenset((a, b)))
    return links, nodes


def parse_list(path):
    return {frozenset(m) for m in re.findall(r"([A-G])\\,--\\,([A-G])", open(path).read())}


def parse_circles(path, radius=None):
    out = []
    for x, y, r in re.findall(r"\(" + NUM + "," + NUM + r"\) circle \(" + NUM + r"\)", open(path).read()):
        if radius is None or abs(float(r) - radius) < 1e-6:
            out.append((float(x), float(y)))
    return out


def page_texts(band):
    out = subprocess.run(["pdftotext", "-layout", os.path.join(PAGES, band + ".pdf"), "-"],
                         capture_output=True, text=True, check=True).stdout
    return out.split("\f")[:-1]


def check_pages(tmp):
    say("== 1. agreement with the final pages ==")
    gen = os.path.join(tmp, "gen")
    for nm, (links, where) in N.PAGE_NETS.items():
        if nm.startswith("k_hw"):
            continue
        drawn, nodes = parse_picture(os.path.join(gen, f"pic_{nm}.tex"))
        listed = parse_list(os.path.join(gen, f"list_{nm}.tex"))
        mine = {frozenset(e) for e in links}
        check(drawn == mine == listed, f"{nm}: picture, list and guide data differ")
        # positions: same shape up to the printed scale
        pos = N.PAGE_POS[nm]
        a, b = ("D", "E") if nm == "n5" else sorted(pos)[:2]
        k = math.dist(nodes[a], nodes[b]) / math.dist(pos[a], pos[b])
        for v in pos:
            if nm == "n5" and v in "ABC":
                continue  # house labels sit a little below the house centre
            check(abs(math.dist(nodes[a], nodes[v]) - k * math.dist(pos[a], pos[v])) < 0.02, f"{nm}: position of {v}")
    say("pictures: all 13 tangled pictures match their printed link lists and the guide's data")

    # link lists in the PDF text, page by page (multisets of 'X–Y' tokens)
    expect = {
        ("k-1", 0): ["k_bowtie", "k_kite", "k_k4"], ("k-1", 2): ["k_star", "k_fan", "k_prism"], ("k-1", 3): ["k_k5"],
        ("grades-2-3", 0): ["n1", "n2", "n3"], ("grades-2-3", 1): ["n4", "n5", "n6"],
        ("grades-4-5", 0): ["n1", "n2", "n3"], ("grades-4-5", 1): ["n4", "n5", "n6"],
    }
    for (band, pg), nets in expect.items():
        toks = collections.Counter(frozenset(m) for m in re.findall(r"\b([A-G])–([A-G])\b", page_texts(band)[pg]))
        want = collections.Counter(frozenset(e) for nm in nets for e in N.PAGE_NETS[nm][0])
        check(toks == want, f"{band} page {pg + 1}: link lists in the PDF text")
    say("PDF text: the link lists on K-1 pp. 1, 3, 4 and on pp. 1-2 of grades 2-3 and 4-5 match")

    # portal boards
    for nm in ("k5", "k6", "k7"):
        pos, links, S = N.PORTAL[nm]
        txt = open(os.path.join(gen, f"portal_{nm}.tex")).read()
        nodes = {lab: (float(x) / S, float(y) / S) for x, y, lab in
                 re.findall(r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{([A-G])\};", txt)}
        check(set(nodes) == set(pos) and all(math.dist(nodes[v], pos[v]) < 2e-3 for v in pos), f"portal {nm} positions")
    txt = open(os.path.join(gen, "portal_k33.tex")).read()
    nodes = {lab: (float(x) / 7.2, float(y) / 7.2) for x, y, lab in
             re.findall(r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{([A-G])\};", txt)}
    check(all(abs(nodes[v][0] - N.TOR_K33[v][0]) < 2e-3 and abs(nodes[v][1] - N.TOR_K33[v][1]) < 0.02 for v in N.TOR_K33),
          "portal k33 positions")
    say("portal boards: the printed dot positions for network 5, network 2, 6 dots and 7 dots match")

    boards = {}
    for f in sorted(os.listdir(gen)):
        if f.startswith("game_"):
            boards[f[5:-4]] = parse_circles(os.path.join(gen, f))
    say("game boards:", ", ".join(f"{k} ({len(v)} dots)" for k, v in boards.items()))
    return boards


def check_numbers():
    """Problem numbers and their pages in the final PDFs, and the guide's headings."""
    say("== problem numbers and pages ==")
    where = {}
    for band in ("k-1", "grades-2-3", "grades-4-5"):
        pages = page_texts(band)
        found = {}
        for i, t in enumerate(pages):
            for m in re.findall(r"Problem (\d+):", t):
                found[int(m)] = i + 1
        check(sorted(found) == list(range(1, len(found) + 1)), f"{band}: problems not consecutive")
        where[band] = (found, len(pages))
        say(f"{band}: {len(pages)} pages; problem -> page {found}")
    # the guide's headings: \sub{Problem N, page P...} or \sub{Problems N and M, pages P and Q...}
    sol = open(os.path.join(HERE, "solutions.tex")).read()
    parts = re.split(r"\\head\{Grades (K--1|2--3|4--5)", sol)
    bandmap = {"K--1": "k-1", "2--3": "grades-2-3", "4--5": "grades-4-5"}
    n = 0
    for lab, body in zip(parts[1::2], parts[2::2]):
        found, npages = where[bandmap[lab]]
        seen = set()
        for probs, pgs in re.findall(r"\\sub\{Problems? ([\d, and]+?),? pages? ([\d, and–-]+?)[:\}]", body):
            ps = [int(x) for x in re.findall(r"\d+", probs)]
            gs = [int(x) for x in re.findall(r"\d+", pgs)]
            if "–" in pgs or "-" in pgs:
                gs = list(range(gs[0], gs[-1] + 1))
            for p in ps:
                check(p in found, f"guide {lab}: Problem {p} does not exist")
                check(found[p] in gs, f"guide {lab}: Problem {p} is on page {found[p]}, not {pgs}")
                seen.add(p)
                n += 1
        check(seen == set(found), f"guide {lab}: headings cover {sorted(seen)}, packet has {sorted(found)}")
    say(f"guide headings: {n} problem citations match the printed problem and page numbers; every problem has a heading")
    return where


# ====================================================================== 2. the mathematics
def check_networks():
    say("== 2. networks: type, crossings in the picture, untangled drawing, regions ==")
    for nm, (links, where) in N.PAGE_NETS.items():
        G = nx.Graph(links)
        V, Ecount = G.number_of_nodes(), G.number_of_edges()
        planar = nx.check_planarity(G)[0]
        c = len(N.crossing_pairs(N.PAGE_POS[nm], links)) if nm in N.PAGE_POS else None
        line = f"{where:28s} V={V} E={Ecount} planar={planar} crossings in picture={c}"
        if planar:
            check(Ecount <= 3 * V - 6, nm)
        if nm in N.UNTANGLED:
            pos = N.UNTANGLED[nm]
            check(set(pos) == set(G.nodes), nm)
            check(N.crossing_pairs(pos, links) == [], f"{nm}: guide drawing has a crossing")
            check(N.dot_clearance(pos, links) > 0.3, f"{nm}: guide drawing passes near a dot")
            F = N.plane_faces(pos, links)
            check(V - Ecount + F == 2, nm)
            line += f"  guide drawing: 0 crossings, {F} regions, V-E+F={V - Ecount + F}"
        say(line)
    # facts the guide states
    K5 = nx.complete_graph("ABCDE")
    K33 = nx.complete_bipartite_graph(3, 3)
    oct_ = nx.Graph(N.PAGE_NETS["n6"][0])
    check(nx.is_isomorphic(nx.Graph(N.PAGE_NETS["n2"][0]), K5), "network 2 is K5")
    check(nx.is_isomorphic(nx.Graph(N.PAGE_NETS["n5"][0]), K33), "network 5 is K3,3")
    check(set(map(frozenset, N.PAGE_NETS["n3"][0])) == set(map(frozenset, N.complete("ABCDE"))) - {frozenset("DE")},
          "network 3 is network 2 without D-E")
    check(nx.is_isomorphic(oct_, nx.octahedral_graph()), "network 6 is the octahedron")
    check(not ({frozenset(e) for e in N.PAGE_NETS["n6"][0]} & {frozenset("AF"), frozenset("BD"), frozenset("CE")}),
          "network 6 misses A-F, B-D, C-E")
    check(nx.is_isomorphic(nx.Graph(N.PAGE_NETS["n4"][0]), nx.circular_ladder_graph(3)), "network 4 is the prism")
    check(nx.is_isomorphic(nx.Graph(N.PAGE_NETS["n1"][0]), nx.Graph(N.PAGE_NETS["k_fan"][0])), "network 1 is the fan")
    check(N.PAGE_NETS["n4"][0] == N.PAGE_NETS["k_prism"][0], "network 4 has the K-1 prism's labels")
    check(nx.is_isomorphic(nx.Graph(N.PAGE_NETS["k_star"][0]), nx.cycle_graph(5)), "K-1 star is a 5-ring")
    say("types: n1 fan, n2 K5, n3 K5 without D-E, n4 prism (same labels as K-1's), n5 K3,3, n6 octahedron "
        "(missing A-F, B-D, C-E); K-1 star is a 5-ring")
    # region table for Problem 2
    table = {nm: (len(N.UNTANGLED[nm]), len(N.PAGE_NETS[nm][0]), N.plane_faces(N.UNTANGLED[nm], N.PAGE_NETS[nm][0]))
             for nm in ("n1", "n3", "n4", "n6")}
    check(table == {"n1": (5, 7, 4), "n3": (5, 9, 6), "n4": (6, 9, 5), "n6": (6, 12, 8)}, "region table")
    rect = {1: (0, 0), 2: (4, 0), 3: (4, 2.8), 4: (0, 2.8)}
    check(N.plane_faces(rect, [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]) == 3, "page example")
    say("Problem 2 table:", table, "; page example 4 dots, 5 links, 3 regions")
    # two pieces
    tri2 = {1: (0, 0), 2: (1, 0), 3: (0, 1)}
    say("two pieces: two triangles give 6 - 6 + 3 =", 6 - 6 + 3, "(1 + number of pieces)")
    # tangled pictures: regions = links - dots + 2 + crossings
    for nm in N.PAGE_POS:
        links = N.PAGE_NETS[nm][0]
        F = planarized_faces(N.PAGE_POS[nm], links)
        c = len(N.crossing_pairs(N.PAGE_POS[nm], links))
        check(F == len(links) - len(N.PAGE_POS[nm]) + 2 + c, f"tangled regions {nm}")
    say("tangled pictures: in all 13, regions = links - dots + 2 + crossings")
    # K-1 Problem 1: moving a single dot (to some grid point) removes the crossing
    for nm in ("k_bowtie", "k_kite", "k_k4"):
        pos, links = N.PAGE_POS[nm], N.PAGE_NETS[nm][0]
        movers = set()
        for v in pos:
            for x in range(-3, 9):
                for y in range(-3, 9):
                    q = dict(pos, **{v: (x, y)})
                    if min(math.dist(q[v], q[u]) for u in q if u != v) < 1:
                        continue
                    if not N.crossing_pairs(q, links) and N.dot_clearance(q, links) > 0.3:
                        movers.add(v)
        check(movers, nm)
        say(f"{nm}: one move untangles it (dots that can do it alone: {''.join(sorted(movers))})")


def planarized_faces(pos, links):
    """Faces of a drawing with crossings, each crossing made into a dot."""
    pts = dict(pos)
    on = {e: [pos[e[0]], pos[e[1]]] for e in links}
    k = 0
    for e, f in N.crossing_pairs(pos, links):
        c = N.cross_point(pos[e[0]], pos[e[1]], pos[f[0]], pos[f[1]])
        k += 1
        pts[f"x{k}"] = c
        on[e].append(c)
        on[f].append(c)
    name = {p: v for v, p in pts.items()}
    segs = []
    for e, ps in on.items():
        a = pos[e[0]]
        ps = sorted(ps, key=lambda p: math.dist(a, p))
        segs += [(name[p], name[q]) for p, q in zip(ps, ps[1:])]
    return N.plane_faces(pts, segs)


def check_impossible():
    say("== impossibility arguments ==")
    for nm, V, Ecount, tri in (("K5", 5, 10, True), ("K3,3", 6, 9, False)):
        F = Ecount - V + 2
        need = (3 if tri else 4) * F
        check(need > 2 * Ecount, nm)
        say(f"{nm}: untangled would give {F} regions needing >= {need} link-sides, but {Ecount} links have {2 * Ecount}")
    check(10 > 3 * 5 - 6 and 9 > 2 * 6 - 4, "edge bounds")
    check(nx.is_bipartite(nx.complete_bipartite_graph(3, 3)), "K3,3 has no triangles")
    # ring arguments: chords of a ring cross (if on the same side) exactly when their ends interleave
    def interleave(c1, c2, order):
        i = {v: k for k, v in enumerate(order)}
        a, b = sorted((i[c1[0]], i[c1[1]]))
        x, y = i[c2[0]], i[c2[1]]
        return (a < x < b) != (a < y < b) and not set(c1) & set(c2)
    ring = "ABCDE"
    chords = [c for c in N.complete(ring) if (ring.index(c[1]) - ring.index(c[0])) % 5 not in (1, 4)]
    best = max(len(s) for r in range(6) for s in itertools.combinations(chords, r)
               if all(not interleave(a, b, ring) for a, b in itertools.combinations(s, 2)))
    check(len(chords) == 5 and best == 2, "pentagon chords")
    say("K5 ring A-B-C-D-E: 5 other links; at most", best, "fit on one side without crossing; 5 > 2 + 2")
    hexa = "ADBECF"
    rest = [("A", "E"), ("B", "F"), ("C", "D")]
    check(all(interleave(a, b, hexa) for a, b in itertools.combinations(rest, 2)), "hexagon chords")
    say("K3,3 ring A-D-B-E-C-F: the other links A-E, B-F, C-D cross pairwise on one side; 3 links, 2 sides")
    # K4 untangled: every region has three corners, so a fifth dot reaches only three
    G4 = nx.complete_graph(4)
    ok, emb = nx.check_planarity(G4)
    faces = []
    seen = set()
    for u, v in emb.edges():
        if (u, v) not in seen:
            faces.append(len(emb.traverse_face(u, v, mark_half_edges=seen)))
    check(sorted(faces) == [3, 3, 3, 3], "K4 faces")
    check(6 == 3 * 4 - 6, "K4 has the most links possible on 4 dots, so every untangled drawing is all triangles")
    say("K4 untangled: 4 regions, each with 3 corners (true for every drawing, since 6 = 3*4 - 6)")
    for e in N.complete("ABCDE"):
        G = nx.complete_graph("ABCDE")
        G.remove_edge(*e)
        check(nx.check_planarity(G)[0], "K5 minus a link")
    for e in itertools.product("ABC", "DEF"):
        G = nx.Graph([(h, w) for h in "ABC" for w in "DEF"])
        G.remove_edge(*e)
        check(nx.check_planarity(G)[0], "K3,3 minus a link")
    say("K5 minus any one link, and K3,3 minus any one link, can be untangled")


def check_fewest():
    say("== fewest crossings ==")
    for nm, (pos, links, c) in N.FEWEST.items():
        cp = N.crossing_pairs(pos, links)
        check(len(cp) == c, nm)
        check(N.dot_clearance(pos, links) > 0.3, f"{nm} clearance")
        say(f"{nm}: guide drawing has {len(cp)} crossing(s): {cp}")
    check(N.crossing_pairs(*N.FEWEST["K5"][:2]) == [(("A", "C"), ("D", "E"))], "K5 crossing involves D-E")
    pos5 = N.FEWEST["K5"][0]
    check(all(abs(pos5[v][0] - N.UNTANGLED["n3"][v][0]) < 1e-9 for v in pos5), "K5 drawing = network 3 drawing + D-E")
    for nm, V, Ecount, cap in (("K5", 5, 10, 9), ("K3,3", 6, 9, 8), ("K6", 6, 15, 12)):
        say(f"{nm}: lower bound {Ecount} - {cap} = {Ecount - cap} (remove one link per crossing)")
    check(15 - (3 * 6 - 6) == 3, "K6 bound")
    # loophole if many links may pass through one place: all links of K6 through one point
    say("without the two-links rule, all 15 links of K6 can pass through one point: one crossing place")


def random_game_straight(pts, rnd, clear=0.3):
    n = len(pts)
    links = []
    pairs = list(itertools.combinations(range(n), 2))
    while True:
        legal = []
        for a, b in pairs:
            if (a, b) in links:
                continue
            if any(N.point_seg_dist(pts[k], pts[a], pts[b]) < clear for k in range(n) if k not in (a, b)):
                continue
            if any(not ({a, b} & {c, d}) and N.proper_cross(pts[a], pts[b], pts[c], pts[d]) for c, d in links):
                continue
            legal.append((a, b))
        if not legal:
            return len(links)
        links.append(rnd.choice(legal))


def hull_size(pts):
    pts = sorted(pts)
    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and N.orient(h[-2], h[-1], p) <= 0:
                h.pop()
            h.append(p)
        return h
    lo, up = half(pts), half(pts[::-1])
    return len(lo) + len(up) - 2


def check_game(boards):
    say("== the link game ==")
    rnd = random.Random(2026)
    for nm, pts in boards.items():
        n = len(pts)
        check(hull_size(pts) == 3, f"{nm}: three outer dots")
        counts = {random_game_straight(pts, rnd) for _ in range(300)}
        check(counts == {3 * n - 6}, f"{nm}: {counts}")
        say(f"board {nm}: {n} dots, 3 outer; 300 random straight-link games all ended with {3 * n - 6} links "
            f"-> {'second' if (3 * n - 6) % 2 == 0 else 'first'} player wins")
    # dots may move (abstract planar): random maximal planar networks
    for n in range(3, 12):
        ends = set()
        for _ in range(60):
            G = nx.empty_graph(n)
            pairs = list(itertools.combinations(range(n), 2))
            rnd.shuffle(pairs)
            changed = True
            while changed:
                changed = False
                for a, b in pairs:
                    if G.has_edge(a, b):
                        continue
                    G.add_edge(a, b)
                    if nx.check_planarity(G)[0]:
                        changed = True
                    else:
                        G.remove_edge(a, b)
            ends.add(G.number_of_edges())
        check(ends == {3 * n - 6}, f"abstract game n={n}: {ends}")
    say("bent links (abstract): random finished games on 3..11 dots always have 3n-6 links")
    for n in (10, 11):
        L = 3 * n - 6
        say(f"{n} dots: every finished game has {L} links -> {'second' if L % 2 == 0 else 'first'} player wins")
    check((3 * 10 - 6) % 2 == 0 and (3 * 11 - 6) % 2 == 1, "10 and 11")
    # straight links on other arrangements: 3n - 3 - h
    seen = set()
    for n in (6, 10, 11):
        for _ in range(12):
            pts = [(rnd.uniform(0, 10), rnd.uniform(0, 10)) for _ in range(n)]
            h = hull_size(pts)
            L = random_game_straight(pts, rnd, clear=1e-6)
            check(L == 3 * n - 3 - h, f"straight game n={n} h={h} L={L}")
            seen.add((n, h, L))
    say("straight links on random arrangements: links at the end = 3n - 3 - (outer dots), e.g.",
        sorted(seen)[:6])


def check_portal():
    say("== portal board (flat torus) ==")
    for nm in N.PORTAL:
        pos, links, S = N.PORTAL[nm]
        offs = N.portal_offsets(nm)
        check({frozenset(e) for e in offs} == {frozenset(e) for e in links}, nm)
        probs = N.torus_check(pos, offs)
        check(probs == [], f"{nm}: {probs}")
        F = N.torus_faces(pos, offs)
        V, Ecount = len(pos), len(links)
        check(V - Ecount + F == 0, f"{nm}: Euler on the torus")
        clear = min(N.torus_clearance(pos, N.cover_segment(pos, e, o), e) for e, o in offs.items())
        through = sorted("".join(e) for e, o in offs.items() if o != (0, 0))
        say(f"{nm}: crossing-free; {len(through)} of {Ecount} links use a portal ({', '.join(through)}); "
            f"{F} regions, V-E+F = {V - Ecount + F}; links clear other dots by {clear * S:.2f} cm on the printed board")
    k33 = N.portal_offsets("k33")
    say("network 5 route:", {"".join(e): o for e, o in k33.items()})
    check(28 > 3 * 8, "K8 cannot go on the torus")
    say("torus bound: links <= 3 x dots; K7 has 21 = 3 x 7; K8 has 28 > 24")


def check_launch_and_materials():
    say("== launch and materials ==")
    paw = nx.Graph(N.LAUNCH_LINKS)
    for nm, (links, where) in N.PAGE_NETS.items():
        check(not nx.is_isomorphic(paw, nx.Graph(links)), f"launch equals {nm}")
    for k in range(3, 12):
        check(paw.number_of_edges() != 3 * k - 6 or paw.number_of_nodes() != k, "launch is a finished game")
    check(len(N.crossing_pairs(N.LAUNCH_IN, N.LAUNCH_LINKS)) == 1, "launch input")
    check(N.crossing_pairs(N.LAUNCH_OUT, N.LAUNCH_LINKS) == [], "launch output")
    check(N.dot_clearance(N.LAUNCH_OUT, N.LAUNCH_LINKS) > 0.4, "launch output clearance")
    say("launch: triangle with a tail (4 dots, 4 links) is none of the page networks; input 1 crossing, output 0")
    build = [nm for nm in N.PAGE_NETS if nm != "k_k5"]
    md = max(len({v for e in N.PAGE_NETS[nm][0] for v in e}) for nm in N.PAGE_NETS)
    ml = max(len(N.PAGE_NETS[nm][0]) for nm in N.PAGE_NETS)
    deg = {nm: max(dict(nx.Graph(N.PAGE_NETS[nm][0]).degree()).values()) for nm in N.PAGE_NETS}
    say(f"materials: at most {md} dots and {ml} links in any printed network; largest number of link ends at one dot: "
        + ", ".join(f"{nm} {d}" for nm, d in deg.items() if d >= 4))


# ====================================================================== 3. revision: new figures and plan
def check_revision():
    """Checks added in the revision: the bent launch link, the K-1 key's fewest-crossing drawings,
    the numbered exits on the portal drawings (read back from the generated TikZ), and the time budget."""
    say("== revision checks ==")
    gen = os.path.join(HERE, "gen")
    # bent launch link, read back from the printed figure
    txt = open(os.path.join(gen, "launch_bend.tex")).read()
    nodes = {lab: (float(x), float(y)) for x, y, lab in re.findall(r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{([A-D])\};", txt)}
    straight = [((float(a), float(b)), (float(c), float(d))) for a, b, c, d in
                re.findall(r"\\draw\[line width=[\d.]+pt\] \(" + NUM + "," + NUM + r"\) -- \(" + NUM + "," + NUM + r"\);", txt)]
    curves = re.findall(r"\(" + NUM + "," + NUM + r"\) \.\. controls \(" + NUM + "," + NUM + r"\) and \(" + NUM + "," + NUM
                        + r"\) \.\. \(" + NUM + "," + NUM + r"\)", txt)
    check(len(curves) == 1 and len(straight) == 3, "launch_bend: one bent link and three straight ones")
    v = [float(x) for x in curves[0]]
    p0, c1, c2, p3 = (v[0], v[1]), (v[2], v[3]), (v[4], v[5]), (v[6], v[7])
    check(math.dist(p0, nodes["C"]) < 1e-6 and math.dist(p3, nodes["D"]) < 1e-6, "bent link joins C and D")
    pts = N.bezier_points(p0, c1, c2, p3, 400)
    poly = list(zip(pts, pts[1:]))
    for a, b in straight:
        check(not any(N.proper_cross(a, b, p, q) for p, q in poly), "bent link crosses a straight link")
    r = 0.17
    clear = min(N.point_seg_dist(nodes[u], p, q) for u in "AB" for p, q in poly) - r
    check(clear > 0.2, f"bent link passes {clear:.2f} cm from dot A or B")
    labels = {frozenset((min(nodes, key=lambda u: math.dist(nodes[u], a)), min(nodes, key=lambda u: math.dist(nodes[u], b))))
              for a, b in straight}
    check(labels == {frozenset(e) for e in N.E("AB BC AC")}, "launch_bend straight links")
    check(nodes["D"] == {lab: (float(x), float(y)) for x, y, lab in re.findall(
        r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{([A-D])\};", open(os.path.join(gen, "launch_in.tex")).read())}["D"],
        "D has not moved in the bent panel")
    say(f"launch: C-D bent round B joins C to D with D unmoved, crosses nothing, and clears A and B by {clear:.2f} cm")

    # K-1 key: Problems 3 and 5 use the K-1 labels
    check({frozenset(e) for e in N.FEWEST["K33"][1]} == {frozenset(e) for e in N.PAGE_NETS["k_hw33"][0]}, "K-1 P3 labels")
    check({frozenset(e) for e in N.FEWEST["K5"][1]} == {frozenset(e) for e in N.PAGE_NETS["k_k5"][0]}, "K-1 P5 labels")
    for f, links in (("key_k_hw33", N.PAGE_NETS["k_hw33"][0]), ("key_k_k5", N.PAGE_NETS["k_k5"][0])):
        t = open(os.path.join(gen, f + ".tex")).read()
        nd = {lab: (float(x), float(y)) for x, y, lab in re.findall(r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{([A-F])\};", t)}
        segs = re.findall(r"\\draw\[line width=0.9pt\] \(" + NUM + "," + NUM + r"\) -- \(" + NUM + "," + NUM + r"\);", t)
        circ = len(re.findall(r"circle \(0\.1\)", t))
        check(len(segs) == len(links) and circ == 1, f"{f}: {len(segs)} links, {circ} circled crossing")
    say("K-1 key: Problems 3 and 5 drawings have the K-1 page's links and labels, each with 1 circled crossing")

    # portal drawings: numbered exits read back from the printed figures
    for nm in N.PORTAL:
        pos, links, printed = N.PORTAL[nm]
        t = open(os.path.join(gen, f"portal_{nm}.tex")).read()
        size = float(re.search(r"rectangle \(" + NUM + "," + NUM + r"\)", t).group(1))
        labs = [(int(n), (float(x), float(y))) for x, y, n in
                re.findall(r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{(\d+)\};", t)]
        segs = [((float(a), float(b)), (float(c), float(d))) for a, b, c, d in
                re.findall(r"\\draw\[line width=0.7pt\] \(" + NUM + "," + NUM + r"\) -- \(" + NUM + "," + NUM + r"\);", t)]
        ends = [p for s in segs for p in s if min(abs(p[0]), abs(p[0] - size), abs(p[1]), abs(p[1] - size)) < 1e-3]
        nums = collections.Counter(n for n, _ in labs)
        stubs = N.portal_stubs(pos, N.portal_offsets(nm))
        check(sorted(nums) == list(range(1, len(stubs) + 1)) and set(nums.values()) == {2}, f"portal {nm}: each number twice")
        check(len(ends) == 2 * len(stubs), f"portal {nm}: {len(ends)} side points for {len(stubs)} numbers")

        def foot(p):  # the boundary point a label sits beside
            x, y = p
            return (min(max(x, 0), size), min(max(y, 0), size))
        for n in nums:
            a, b = [foot(p) for m, p in labs if m == n]
            sa, sb = N.side_of((a[0] / size, a[1] / size)), N.side_of((b[0] / size, b[1] / size))
            check({sa, sb} in ({"L", "R"}, {"T", "B"}), f"portal {nm}: number {n} not on opposite sides")
            along = (1, 1) if sa in "LR" else (0, 0)
            check(abs(a[along[0]] - b[along[1]]) < 1e-3, f"portal {nm}: number {n} at different heights")
            for q in (a, b):
                check(any(math.dist(q, e) < 1e-3 for e in ends), f"portal {nm}: number {n} is not at a link's exit")
        gap = min(math.dist(p, q) for (m, p), (k, q) in itertools.combinations(labs, 2))
        check(gap > 0.3, f"portal {nm}: two numbers only {gap:.2f} cm apart")
        through = sum(1 for e, o in N.portal_offsets(nm).items() if o != (0, 0))
        say(f"portal {nm}: {len(stubs)} numbered exits for {through} portal links; every number marks a drawn exit and its "
            f"entry on the opposite side at the same height; numbers at least {gap:.2f} cm apart; board {size:.1f} cm")

    # Grades 2-3 split: each pair's half of Problem 1 holds two networks that untangle
    for half in (("n1", "n2", "n3"), ("n4", "n5", "n6")):
        ok = [nm for nm in half if nx.check_planarity(nx.Graph(N.PAGE_NETS[nm][0]))[0]]
        check(len(ok) == 2, f"split {half}")
    say("2-3 split: networks 1-3 give two untangled networks (1, 3) and 4-6 give two (4, 6); pooled, all four rows")

    # time budget in "A first hour": each first route fits 35-40 minutes at the tables
    tex = open(os.path.join(HERE, "facilitator.tex")).read()
    para = tex[tex.index(r"\textbf{A first hour.}"):tex.index(r"\input{solutions.tex}")]
    routes = re.split(r"\n(?=K--1:|Grades 2--3:|Grades 4--5:|Close)", para)
    for r_ in routes[1:4]:
        core = r_.split("only if time allows")[0]
        lo = hi = 0
        for a, b in re.findall(r"\((\d+)(?:--(\d+))? minutes", core):
            lo += int(a)
            hi += int(b or a)
        pool = 2 if r_.startswith("Grades 2--3") else 0
        check(35 - 5 <= lo + pool and hi + pool <= 40, f"route {r_[:12]}: {lo + pool}-{hi + pool} minutes")
        say(f"time budget {r_.split(':')[0]}: {lo + pool}-{hi + pool} minutes before any 'if time' step"
            + (" (2 minutes of pooling counted)" if pool else ""))
    check(re.search(r"Close \(3 minutes\)", para) is not None, "close")


if __name__ == "__main__":
    tmp = rebuild_student_figures()
    try:
        boards = check_pages(tmp)
        check_numbers()
        check_networks()
        check_impossible()
        check_fewest()
        check_game(boards)
        check_portal()
        check_launch_and_materials()
        check_revision()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    say("ALL CHECKS PASSED")
    with open(os.path.join(HERE, "check-output.txt"), "w") as f:
        f.write("\n".join(LOG) + "\n")
