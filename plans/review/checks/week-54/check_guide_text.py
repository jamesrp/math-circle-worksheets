#!/usr/bin/env python3
"""Confirm that the delivered guide PDF (not just its TeX) prints the answer keys
that check_math.py computes, page by page, and that the student PDF prints the
problem wording I checked. Uses pdftotext.

Run: python3 check_guide_text.py > out_check_guide_text.txt
"""
import re
import subprocess

import check_math as M

REPO = M.REPO
GUIDE = REPO / "lowell-math-circle-year-2/week-54/week-54-facilitator.pdf"
STUD = REPO / "lowell-math-circle-year-2/week-54/week-54-students.pdf"


def page_text(pdf, page, layout=False):
    args = ["pdftotext"] + (["-layout"] if layout else []) + ["-f", str(page), "-l", str(page), str(pdf), "-"]
    t = subprocess.run(args,
                       capture_output=True, text=True, check=True).stdout
    return re.sub(r"\s+", " ", t)


def tup(p):
    return "(" + ", ".join(map(str, p)) + ")"


def main():
    bad = 0

    def need(page_txt, s, where):
        nonlocal bad
        ok = s in page_txt
        bad += not ok
        print(("ok   " if ok else "MISS ") + f"{where}: {s}")

    g = {i: page_text(GUIDE, i) for i in range(1, 9)}
    # Problem 1 key, guide p.3
    for n in (4, 5):
        for p in M.partitions(n):
            need(g[3], tup(p), f"guide p3 P1 total {n}")
    # Problem 2 key, guide p.4
    for n in (6, 7):
        for p in M.odd_parts(n) + M.distinct_parts(n):
            need(g[4], tup(p), f"guide p4 P2 total {n}")
    # Problem 3 key, guide p.4
    for start in [(5, 5, 3, 3, 3, 1, 1), (5, 3, 1), (1,) * 9]:
        need(g[4], tup(M.join_all(start)), f"guide p4 P3 result of {tup(start)}")
    # Problem 4 key, guide p.5
    for start in [(10, 7, 4, 2, 1), (12, 6, 3), (7, 3, 1)]:
        need(g[5], tup(M.split_all(start)), f"guide p5 P4 split of {tup(start)}")
    # Problem 5 key, guide p.5
    for p in M.odd_parts(8):
        need(g[5], tup(p), "guide p5 P5 odd side")
        need(g[5], tup(M.join_all(p)), "guide p5 P5 distinct side")
    # Problem 6 terminal, guide p.6
    need(g[6], tup(M.join_all((3, 3, 3, 3, 1, 1, 1, 1, 1, 1))), "guide p6 P6 terminal")
    # Problems 7 and 8, guide p.7
    for p in [(5, 2, 1), (4, 4), (3, 3, 1, 1)]:
        need(g[7], tup(M.conjugate(p)), f"guide p7 P7 once for {tup(p)}")
    g7rows = page_text(GUIDE, 7, layout=True)   # layout mode keeps each table row on one line
    for p in [q for q in M.partitions(8) if len(q) <= 3]:
        need(g7rows, tup(p) + " " + tup(M.conjugate(p)), "guide p7 P8 row")
    need(g[7], "ten pairs", "guide p7 P8 count")
    need(g[5], "six pairs", "guide p5 P5 count")

    # student wording that the math check relies on
    s = {i: page_text(STUD, i) for i in range(1, 10)}
    need(s[1], "Find every collection you can make with 4 units, and with 5 units.", "student p1 P1")
    need(s[2], "Choose 6 or 7 units. Find every collection of each kind below.", "student p2 P2")
    need(s[3], "Join equal-size pairs until all sizes are different.", "student p3 P3")
    need(s[4], "Does each starting collection return?", "student p4 P4")
    need(s[5], "With 8 units, find every pair of collections connected by joining and splitting.", "student p5 P5")
    need(s[6], "Can the routes end with different collections?", "student p6 P6")
    need(s[7], "What does the second exchange do?", "student p7 P7")
    need(s[8], "Find all 8-unit collections with at most 3 strips.", "student p8 P8")
    need(s[9], "are there exactly as many collections with only odd sizes as collections with all sizes different?",
         "student p9 P9")
    print("missing:", bad)


if __name__ == "__main__":
    main()
