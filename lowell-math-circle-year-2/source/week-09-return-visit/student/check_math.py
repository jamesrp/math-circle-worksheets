#!/usr/bin/env python3
"""Exact checks for the represented two-bounce words, loops, and crossings."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import argparse


def reflect(p, wall, w=4, h=4):
    x, y = p
    return {"L": (-x, y), "R": (2*w-x, y),
            "B": (x, -y), "T": (x, 2*h-y)}[wall]


def next_wall(p, d, w, h):
    x, y = p
    dx, dy = d
    events = []
    if dx:
        wall, edge = ("R", w) if dx > 0 else ("L", 0)
        events.append((Q(edge-x, dx), wall))
    if dy:
        wall, edge = ("T", h) if dy > 0 else ("B", 0)
        events.append((Q(edge-y, dy), wall))
    time = min(t for t, _ in events if t > 0)
    hits = [wall for t, wall in events if t == time]
    return time, hits, (x+time*dx, y+time*dy)


def two_bounce(word, finish):
    start = (Q(1), Q(1))
    image = reflect(reflect(finish, word[1]), word[0])
    direction = (Q(image[0])-1, Q(image[1])-1)
    length_squared = direction[0]**2 + direction[1]**2
    p, d, vertices = start, direction, [start]
    for expected in word:
        _, hits, p = next_wall(p, d, 4, 4)
        vertices.append(p)
        if len(hits) != 1:
            return {"legal": False, "reason": "corner"}
        if hits[0] != expected:
            return {"legal": False, "reason": "wrong wall order"}
        dx, dy = d
        d = (-dx, dy) if expected in "LR" else (dx, -dy)
    delta = (Q(finish[0])-p[0], Q(finish[1])-p[1])
    time = delta[0]/d[0] if d[0] else delta[1]/d[1]
    wall_time, _, _ = next_wall(p, d, 4, 4)
    legal = (time > 0 and time < wall_time and
             p[0]+time*d[0] == finish[0] and
             p[1]+time*d[1] == finish[1])
    if not legal:
        return {"legal": False, "reason": "extra wall before finish"}
    vertices.append(tuple(map(Q, finish)))
    return {"legal": True, "length_squared": int(length_squared),
            "vertices": [[str(x), str(y)] for x, y in vertices]}


def walk(w, h, start, direction=(1, 1)):
    x, y = start
    dx, dy = direction
    initial = (x, y, dx, dy)
    seen = {initial}
    states = [initial]
    for step in range(1, 10000):
        x, y = x+dx, y+dy
        if x in (0, w) and y in (0, h):
            states.append((x, y, dx, dy))
            return {"kind": "corner", "steps": step, "states": states}
        if x in (0, w):
            dx = -dx
        if y in (0, h):
            dy = -dy
        state = (x, y, dx, dy)
        states.append(state)
        if state == initial:
            return {"kind": "loop", "steps": step, "states": states}
        assert state not in seen, (w, h, start, state)
        seen.add(state)
    raise AssertionError("walk did not terminate")


def determinant(a, b):
    return a[0]*b[1] - a[1]*b[0]


def crossings(w, h):
    states = walk(w, h, (0, 0))["states"]
    points = [s[:2] for s in states]
    found = set()
    for i, (a, b) in enumerate(zip(points, points[1:])):
        ab = (b[0]-a[0], b[1]-a[1])
        for c, d in zip(points[i+2:], points[i+3:]):
            cd = (d[0]-c[0], d[1]-c[1])
            den = determinant(ab, cd)
            if not den:
                continue
            ac = (c[0]-a[0], c[1]-a[1])
            t, u = Q(determinant(ac, cd), den), Q(determinant(ac, ab), den)
            if 0 <= t <= 1 and 0 <= u <= 1:
                p = (Q(a[0])+t*ab[0], Q(a[1])+t*ab[1])
                if 0 < p[0] < w and 0 < p[1] < h:
                    found.add(p)
    return {"count": len(found), "points": [list(map(str, p)) for p in sorted(found)],
            "steps": len(states)-1}


def main():
    words = [a+b for a, b in product("LRBT", repeat=2)]
    cases = {name: {word: two_bounce(word, f) for word in words}
             for name, f in [("finish-A", (2, 3)), ("finish-B", (3, 3))]}
    expected = {"finish-A": {"LR", "LT", "RL", "RT", "BL", "BR", "BT", "TB"},
                "finish-B": {"LR", "LT", "RL", "BR", "BT", "TB"}}
    for name, word_results in cases.items():
        legal = {word for word, data in word_results.items() if data["legal"]}
        assert legal == expected[name], (name, legal)
        assert all(not word_results[w]["legal"] for w in ("LL", "RR", "BB", "TT"))
    expected_sq = {"LR": 53, "RL": 85, "BT": 37, "TB": 101,
                   "LT": 25, "BL": 25, "RT": 41, "BR": 41}
    assert {w: d["length_squared"] for w, d in cases["finish-A"].items() if d["legal"]} == expected_sq

    letters = {}
    for index, (y, x) in enumerate(product((3, 2, 1), range(1, 6))):
        data = walk(6, 4, (x, y))
        assert (data["kind"] == "corner") == ((x-y) % 2 == 0)
        if data["kind"] == "loop":
            assert data["steps"] == 24
        letters[chr(65+index)] = {"start": [x, y], "kind": data["kind"],
                                  "steps": data["steps"]}
    assert sum(d["kind"] == "corner" for d in letters.values()) == 8
    assert sum(d["kind"] == "loop" for d in letters.values()) == 7
    middle = walk(6, 4, (3, 2))
    assert middle["states"][12] == (3, 2, 1, -1)
    assert middle["states"][24] == (3, 2, 1, 1)

    crossing_cases = {f"{w}x{h}": crossings(w, h)
                      for w, h in ((2, 3), (3, 4), (4, 5), (4, 6), (5, 6), (10, 12))}
    assert [crossing_cases[k]["count"] for k in ("2x3", "3x4", "4x5", "4x6", "5x6", "10x12")] == [1, 3, 6, 1, 10, 10]
    report = {"two_bounce": cases, "interior_starts": letters,
              "crossings": crossing_cases, "checks": "passed"}
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print("Exact checks passed: wall words 8/6; interior starts 8 corners/7 loops; crossing counts 1/3/6/1.")


if __name__ == "__main__":
    main()
