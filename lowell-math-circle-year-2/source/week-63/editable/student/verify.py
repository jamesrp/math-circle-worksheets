#!/usr/bin/env python3
"""Independent backtracking, bijections, actual PDF records and metric geometry."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re

def orders(labels, avoid=False):
    """Build a row by its home positions, without a permutation library."""
    result = []
    def fill(row, remaining):
        if not remaining:
            result.append("".join(row))
            return
        home = labels[len(row)]
        for card in remaining:
            if avoid and card == home:
                continue
            fill(row + [card], [x for x in remaining if x != card])
    fill([], list(labels))
    return result

def destinations(labels, row):
    return dict(zip(row, labels))

def row_from_map(labels, mapping):
    inverse = {home: card for card, home in mapping.items()}
    assert len(inverse) == len(labels)
    return "".join(inverse[h] for h in labels)

def math_checks():
    results = {}
    expected = [1, 0, 1, 2, 9, 44]
    for n in range(6):
        labels = "ABCDE"[:n]
        universe = orders(labels)
        good = orders(labels, avoid=True)
        assert len(universe) == math.factorial(n)
        assert len(good) == expected[n]
        histogram = [0]*(n+1)
        for row in universe:
            matches = {h for h, c in zip(labels, row) if h == c}
            histogram[len(matches)] += 1
            # Independently enumerate every subset of this outcome's matches.
            coefficient = 0
            for mask in range(1 << len(matches)):
                coefficient += (-1)**mask.bit_count()
            assert coefficient == (1 if not matches else 0)
        intersections = {}
        for mask in range(1 << n):
            subset = [labels[i] for i in range(n) if mask >> i & 1]
            count = sum(all(row[labels.index(h)] == h for h in subset)
                        for row in universe)
            assert count == math.factorial(n-len(subset))
            intersections["".join(subset) or "none"] = count
        signed = [(-1)**k * math.comb(n, k)*math.factorial(n-k)
                  for k in range(n+1)]
        assert sum(signed) == len(good)
        branches = {}
        if n >= 2:
            distinguished = labels[-1]
            for home in labels[:-1]:
                target_rows = {r for r in good if destinations(labels, r)[distinguished] == home}
                reciprocal, longer = set(), set()
                # Forward reversible lifts from smaller derangements.
                pair_labels = labels.replace(distinguished, "").replace(home, "")
                for base in orders(pair_labels, avoid=True):
                    mapping = destinations(pair_labels, base)
                    mapping.update({distinguished: home, home: distinguished})
                    row = row_from_map(labels, mapping)
                    assert row in target_rows
                    reciprocal.add(row)
                long_labels = labels.replace(distinguished, "")
                for base in orders(long_labels, avoid=True):
                    mapping = destinations(long_labels, base)
                    incoming = next(c for c, h in mapping.items() if h == home)
                    mapping[incoming] = distinguished
                    mapping[distinguished] = home
                    row = row_from_map(labels, mapping)
                    assert row in target_rows
                    longer.add(row)
                assert not reciprocal & longer
                assert reciprocal | longer == target_rows
                # Reverse every target row and reconstruct it exactly.
                for row in target_rows:
                    mapping = destinations(labels, row)
                    if mapping[home] == distinguished:
                        del mapping[home]
                        del mapping[distinguished]
                        base = row_from_map(pair_labels, mapping)
                        assert base in orders(pair_labels, avoid=True)
                        mapping.update({distinguished: home, home: distinguished})
                    else:
                        incoming = next(c for c, h in mapping.items() if h == distinguished)
                        del mapping[distinguished]
                        mapping[incoming] = home
                        base = row_from_map(long_labels, mapping)
                        assert base in orders(long_labels, avoid=True)
                        mapping[incoming] = distinguished
                        mapping[distinguished] = home
                    assert row_from_map(labels, mapping) == row
                branches[home] = {"reciprocal": sorted(reciprocal), "longer": sorted(longer)}
                assert len(reciprocal) == expected[n-2]
                assert len(longer) == expected[n-1]
        results[str(n)] = {"all": len(universe), "home_free": good,
                            "matches_histogram": histogram, "intersections": intersections,
                            "signed_terms": signed, "branches": branches}
    assert results["3"]["home_free"] == ["BCA", "CAB"]
    assert results["4"]["home_free"] == ["BADC", "BCDA", "BDAC", "CADB", "CDAB", "CDBA", "DABC", "DCAB", "DCBA"]
    for labels, expected_partial in [("ABC", 3), ("ABCD", 14)]:
        neither = [r for r in orders(labels) if r[0] != "A" and r[1] != "B"]
        assert len(neither) == expected_partial
        results["partial_"+labels] = neither
    assert destinations("UVWX", "VUWX") == {"V":"U", "U":"V", "W":"W", "X":"X"}
    cycle = "PTS RQ".replace(" ", "")
    edges = dict(zip(cycle, cycle[1:]+cycle[:1]))
    assert edges == destinations("PQRST", "QRSTP")
    # Non-task six-letter removal illustrations, independent of task labels.
    pair = {"P":"U", "U":"P", "Q":"R", "R":"S", "S":"T", "T":"Q"}
    del pair["P"]; del pair["U"]
    assert pair == {"Q":"R", "R":"S", "S":"T", "T":"Q"}
    long_cycle = dict(zip("PQRSTU", "QRSTUP"))
    del long_cycle["U"]; long_cycle["T"] = "P"
    assert long_cycle == dict(zip("PQRST", "QRSTP"))
    results["convention_examples"] = "placement checks, arrow direction, and both removal examples verified"
    return results

def pdf_checks(folder):
    import fitz
    mm = 72/25.4
    def rectangles(page, width, height):
        found = []
        for path in page.get_drawings():
            # TikZ emits some rectangles as four explicit line segments.
            lines = [item for item in path["items"] if item[0] == "l"]
            if len(lines) == len(path["items"]) == 4:
                axis_aligned = all(abs(item[1].x-item[2].x)<0.01 or
                                   abs(item[1].y-item[2].y)<0.01 for item in lines)
                closed = math.hypot(lines[0][1].x-lines[-1][2].x,
                                    lines[0][1].y-lines[-1][2].y)<0.01
                rect = path["rect"]
                if axis_aligned and closed and abs(rect.width/mm-width)<0.02 and abs(rect.height/mm-height)<0.02:
                    found.append(rect)
            for item in path["items"]:
                if item[0] == "re":
                    rect = item[1]
                    if abs(rect.width/mm-width)<0.02 and abs(rect.height/mm-height)<0.02:
                        found.append(rect)
        return found
    docs = {stem: fitz.open(folder / f"{stem}.pdf") for stem in ("students", "materials")}
    assert len(docs["students"]) == 9 and len(docs["materials"]) == 3
    membership = docs["students"][1]
    membership_text = membership.get_text()
    assert "One outcome card is one whole placement." in membership_text
    assert "Check the same row" in membership_text
    assert "W in home W: yes" in membership_text and "X in home X: yes" in membership_text
    assert "W-home and" in membership_text and "X-home groups" in membership_text
    assert membership_text.index("VUWX") < membership_text.index("Problem 2:")
    assert len(rectangles(membership,56,27)) == 1
    assert len(rectangles(membership,48,10)) == 2
    assert "two or more distinct cards" in docs["students"][8].get_text()
    assert "any number of distinct cards" not in docs["students"][8].get_text()
    evidence = {}
    for stem, doc in docs.items():
        all_text = ""
        for i, page in enumerate(doc, 1):
            assert tuple(page.rect) == (0.0, 0.0, 612.0, 792.0)
            text = page.get_text()
            assert "Week 63 / Cards away from home /" in text
            assert "Bellingham Math Circle / Week 63 /" in text
            if stem == "students":
                band = "Grades 2–5" if i <= 2 else "Grades 3–5" if i <= 5 else "Grades 4–5"
                assert band in text
                assert re.findall(r"Problem (\d+):", text) == [str(i)]
            for span in [s for b in page.get_text("dict")["blocks"] if "lines" in b
                         for line in b["lines"] for s in line["spans"]]:
                x0,y0,x1,y1=span["bbox"]
                assert 12<=x0<=x1<=600 and 12<=y0<=y1<=780, (stem,i,span)
            all_text += text
        evidence[stem] = {"pages": len(doc), "dimensions_points": [612,792],
                          "text_sha256": hashlib.sha256(all_text.encode()).hexdigest()}
    page = docs["materials"][0]
    cards = rectangles(page,30,40)
    homes = rectangles(page,35,45)
    assert len(cards) == 10 and len(homes) == 10
    actual_card_labels = []
    actual_home_labels = []
    for rect in cards:
        words = page.get_text("words",clip=rect)
        labels = [w[4] for w in words if re.fullmatch("[A-E]",w[4])]
        assert len(labels)==1
        actual_card_labels += labels
    for rect in homes:
        words = page.get_text("words",clip=rect)
        labels = [w for w in words if re.fullmatch("[A-E]",w[4])]
        assert len(labels)==1
        # Home lettering lies above the 40 mm card placed at the cell's bottom.
        assert labels[0][3] < rect.y0+5*mm
        actual_home_labels.append(labels[0][4])
    assert sorted(actual_card_labels)==sorted(actual_home_labels)==list("AABBCCDDEE")
    # Verify actual rendered triangle paths are equilateral and diamond sides equal.
    polygons = []
    for path in page.get_drawings():
        points = []
        for item in path["items"]:
            if item[0] == "l":
                if not points: points.append(item[1])
                points.append(item[2])
        if len(points) in (3,4,5) and path["fill"] is not None:
            if points[0] == points[-1]: points.pop()
            if len(points) in (3,4):
                lengths = [math.hypot(points[(j+1)%len(points)].x-p.x,
                                     points[(j+1)%len(points)].y-p.y)
                           for j,p in enumerate(points)]
                assert max(lengths)-min(lengths)<0.02, lengths
                polygons.append({"sides":len(points), "side_lengths_mm":[x/mm for x in lengths]})
    assert sum(p["sides"]==3 for p in polygons)==2
    assert sum(p["sides"]==4 for p in polygons)==4
    # Verify square icons from actual rectangle objects separately.
    assert len(rectangles(page,12,12)) == 2
    rendered_outcomes = {}
    for index, labels in [(1,"ABC"),(2,"ABCD")]:
        p = docs["materials"][index]
        frames = rectangles(p,56,27)
        assert len(frames) == (18 if index==1 else 24)
        parsed = []
        blank = 0
        for frame in frames:
            words = p.get_text("words",clip=frame)
            homes_words, cards_words, ids = [], [], []
            for word in words:
                x0,y0,x1,y1,text,*_=word
                center=(y0+y1)/2-frame.y0
                if center<9*mm and re.fullmatch(r"[A-E]",text): homes_words.append((x0,text))
                elif center<19*mm and re.fullmatch(r"[A-E]",text): cards_words.append((x0,text))
                elif re.fullmatch(r"[A-E]{3,5}",text): ids.append(text)
            homes_string="".join(w for _,w in sorted(homes_words))
            cards_string="".join(w for _,w in sorted(cards_words))
            if not cards_string:
                assert homes_string=="ABCDE" and not ids
                blank+=1
                continue
            assert homes_string==labels
            assert len(ids)==1 and cards_string==ids[0]
            parsed.append(cards_string)
        assert len(parsed)==len(set(parsed))
        assert set(parsed)==set(orders(labels))
        assert blank==(12 if index==1 else 0)
        rendered_outcomes[labels]=parsed
    evidence["materials_geometry"]={"working_cards_30x40_mm":len(cards),
        "home_cells_35x45_mm":len(homes),"outcomes_56x27_mm":rendered_outcomes,
        "equal_sided_icon_paths":polygons,"square_icons_12x12_mm":2}
    assert len(rectangles(docs["materials"][1],34,16)) == 5
    for label in "ABCDE":
        assert f"{label} in home {label}" in docs["materials"][1].get_text()
    for d in docs.values(): d.close()
    return evidence

def compare_rebuild(original, rebuilt):
    import fitz
    comparison={}
    for stem in ("students","materials"):
        a,b=(fitz.open(folder/f"{stem}.pdf") for folder in (original,rebuilt))
        assert len(a)==len(b)
        pages=[]
        for i,(pa,pb) in enumerate(zip(a,b),1):
            assert pa.rect==pb.rect and pa.get_text()==pb.get_text()
            xa,xb=(p.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False) for p in (pa,pb))
            assert xa.width==xb.width and xa.height==xb.height and xa.samples==xb.samples
            pages.append({"page":i,"text_equal":True,"dimensions_equal":True,
                          "pixels_equal_at_144dpi":True,
                          "pixel_sha256":hashlib.sha256(xa.samples).hexdigest()})
        comparison[stem]={"pages":pages,
            "pdf_bytes_equal":(original/f"{stem}.pdf").read_bytes()==(rebuilt/f"{stem}.pdf").read_bytes()}
        a.close();b.close()
    return comparison

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pdf-dir",required=True,type=Path)
    p.add_argument("--out",required=True,type=Path)
    p.add_argument("--compare-dir",type=Path)
    args=p.parse_args()
    evidence={"independent_math":math_checks(),"actual_pdf":pdf_checks(args.pdf_dir)}
    if args.compare_dir:
        evidence["clean_rebuild"] = compare_rebuild(args.pdf_dir,args.compare_dir)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(evidence,indent=2)+"\n")
    print("All enumerations, overlap counts, reversible constructions, actual PDF outcome records, headers and geometry passed.")
    print(args.out)

if __name__=="__main__":main()
