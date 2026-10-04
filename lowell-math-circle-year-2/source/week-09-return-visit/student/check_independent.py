#!/usr/bin/env python3
"""Revision-stage checks using unfolded tiles, folded states and actual PDF vectors.

This checker does not import or call check_math.py or check_pdf.py.
PyMuPDF is optional QA tooling; ordinary builds need only the standard library.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import lcm
from pathlib import Path
import argparse
import json
import pymupdf


def unfolded_words(finish, w=4, h=4):
    """Enumerate target tiles; order exact boundary-line crossing times."""
    results = {}
    for i, j in product(range(-2, 3), repeat=2):
        image = (i*w+(finish[0] if i%2 == 0 else w-finish[0]),
                 j*h+(finish[1] if j%2 == 0 else h-finish[1]))
        events = []
        for start, end, side, names in ((1,image[0],w,('L','R')),
                                       (1,image[1],h,('B','T'))):
            if end == start:
                continue
            for k in range(-3, 4):
                t = Q(k*side-start, end-start)
                if 0 < t < 1:
                    events.append((t, names[k%2]))
        events.sort()
        if len(events) != 2 or events[0][0] == events[1][0]:
            continue
        word = ''.join(name for _, name in events)
        assert word not in results
        results[word] = {'tile':[i,j], 'times':[str(t) for t,_ in events],
                         'squared_length':(image[0]-1)**2+(image[1]-1)**2}
    return results


def fold(value, side):
    phase = value % (2*side)
    return min(phase,2*side-phase), (1 if phase < side else -1)


def classify(start, w=6, h=4):
    """Read physical state directly from the straight unfolded NE ray."""
    earlier_returns = []
    for n in range(1, 2*lcm(w,h)+1):
        x,dx = fold(start[0]+n,w)
        y,dy = fold(start[1]+n,h)
        if x in (0,w) and y in (0,h):
            return {'kind':'corner','steps':n,'end':[x,y],
                    'earlier_point_returns':earlier_returns}
        if (x,y) == start:
            if (dx,dy) == (1,1):
                return {'kind':'loop','steps':n,
                        'earlier_point_returns':earlier_returns}
            earlier_returns.append([n,dx,dy])
    raise AssertionError(start)


def crossing_points(w,h):
    """Fold only wall-time vertices, intersect maximal rays exactly."""
    finish = lcm(w,h)
    times = sorted(set(range(0,finish+1,w)) | set(range(0,finish+1,h)))
    vertices = [(fold(t,w)[0],fold(t,h)[0]) for t in times]
    segments = list(zip(vertices,vertices[1:]))
    found = set()
    for (a,b),(c,d) in combinations(segments,2):
        ax,ay = b[0]-a[0],b[1]-a[1]
        bx,by = d[0]-c[0],d[1]-c[1]
        determinant = ax*by-ay*bx
        if not determinant:
            continue
        cx,cy = c[0]-a[0],c[1]-a[1]
        t = Q(cx*by-cy*bx,determinant)
        u = Q(cx*ay-cy*ax,determinant)
        if 0 < t < 1 and 0 < u < 1:
            x,y = a[0]+t*ax,a[1]+t*ay
            if 0 < x < w and 0 < y < h:
                found.add((x,y))
    return {'count':len(found),'points':[[str(x),str(y)] for x,y in sorted(found)],
            'steps':finish,'end':list(vertices[-1])}


def center(drawing):
    r = drawing['rect']
    return ((r.x0+r.x1)/2,(r.y0+r.y1)/2)


def local(point,rect,w,h):
    return ((point[0]-rect.x0)*w/rect.width,(rect.y1-point[1])*h/rect.height)


def close(a,b,tolerance=0.003):
    assert max(abs(x-y) for x,y in zip(a,b)) < tolerance,(a,b)


def inspect_pdf(pdf):
    doc = pymupdf.open(pdf)
    assert len(doc) == 7
    specifications = [
        [(4,4,12.5)]*4,[(4,4,12.5)]*6,[(4,4,12.5)]*6,
        [(3,3,7)]*3+[(6,4,22)],[(6,4,18)]*2,
        [(2,3,12.5),(3,4,12.5),(4,5,12.5),(4,6,12.5)],[(12,12,12.5)]]
    bands = [2,2,2,4,4,2,2]
    reports = []
    for index,page in enumerate(doc):
        text = page.get_text().replace('\n',' ')
        assert f'Grades {bands[index]}–5' in text
        assert 'Bellingham Math Circle / Week 9 / F09-RV-v1' in text
        close((page.rect.width,page.rect.height),(612,792),0.01)
        drawings = page.get_drawings()
        def blue(drawing):
            return drawing.get('color') is not None and max(
                abs(a-b) for a,b in zip(drawing['color'],(32/255,69/255,115/255))) < 0.001
        if index == 0:
            frames = [s for s in drawings if s.get('color') is not None
                      and all(abs(c-0.75)<0.001 for c in s['color']) and len(s['items'])==4]
            assert len(frames) == 3
            frame = frames[-1]['rect']
            completed = [s for s in drawings if blue(s) and len(s['items'])==2
                         and all(item[0]=='l' for item in s['items'])
                         and frame.contains(s['rect'])]
            assert len(completed) == 1
            rays = completed[0]['items']
            expected = [((1,1),(4,2)),((4,2),(1,3))]
            for line,(a,b) in zip(rays,expected):
                close(local(line[1],frame,4,4),a)
                close(local(line[2],frame,4,4),b)
            # Actual incoming and outgoing vectors are (3,1) and (-3,1),
            # hence their angles with the vertical reflecting wall agree.
        if index == 5:
            circled = [s for s in drawings if s.get('color') == (0,0,0)
                       and len(s['items'])==4 and all(item[0]=='c' for item in s['items'])]
            assert len(circled) == 1
            point = center(circled[0])
            completed = [s for s in drawings if blue(s) and len(s['items'])==2
                         and all(item[0]=='l' for item in s['items'])
                         and s['rect'].contains(pymupdf.Point(*point))]
            assert len(completed) == 1
            slopes = []
            for _,a,b in completed[0]['items']:
                close(((a.x+b.x)/2,(a.y+b.y)/2),point)
                slopes.append((b.y-a.y)/(b.x-a.x))
            close(tuple(sorted(slopes)),(-1,1))
            # Both transverse rays have the same midpoint: one X location.
        grids = [s for s in drawings if s.get('color') is not None
                 and all(abs(c-0.75) < 0.001 for c in s['color'])
                 and len(s['items']) > 4]
        assert len(grids) == len(specifications[index]),(index+1,len(grids))
        page_boards = []
        for board_index,(grid,(w,h,mm)) in enumerate(zip(grids,specifications[index])):
            rect = grid['rect']
            horizontal = [line for line in grid['items'] if line[0]=='l' and abs(line[1].y-line[2].y)<0.001]
            vertical = [line for line in grid['items'] if line[0]=='l' and abs(line[1].x-line[2].x)<0.001]
            assert len(horizontal) == h+1 and len(vertical) == w+1
            close((rect.width/w*25.4/72,rect.height/h*25.4/72),(mm,mm),0.01)
            outlined = index != 6
            if outlined:
                outlines = [s for s in drawings if s.get('color') == (0,0,0)
                            and len(s['items'])==4 and all(k[0]=='l' for k in s['items'])
                            and max(abs(a-b) for a,b in zip(s['rect'],rect))<0.015]
                assert len(outlines) == 1
                for line in outlines[0]['items']:
                    assert (abs(line[1].x-line[2].x)<0.001) != (abs(line[1].y-line[2].y)<0.001)
            circles = [s for s in drawings if len(s['items']) == 4
                       and all(item[0]=='c' for item in s['items'])
                       and rect.x0-0.01 <= center(s)[0] <= rect.x1+0.01
                       and rect.y0-0.01 <= center(s)[1] <= rect.y1+0.01]
            if index <= 2:
                black = [s for s in circles if s.get('fill') == (0,0,0)]
                white = [s for s in circles if s.get('fill') == (1,1,1)]
                assert len(black) == len(white) == 1
                close(local(center(black[0]),rect,w,h),(1,1))
                close(local(center(white[0]),rect,w,h),(2 if board_index%2==0 else 3,3))
            if index == 3:
                dots = [s for s in circles if s.get('fill') == (0,0,0)]
                if board_index < 3:
                    assert len(dots) == 1
                    position = [(2,1),(3,2),(2,3)][board_index]
                    close(local(center(dots[0]),rect,w,h),position)
                    outgoing = []
                    for drawing in drawings:
                        if not blue(drawing):
                            continue
                        for item in drawing['items']:
                            if item[0]=='l' and max(abs(a-b) for a,b in zip(
                                local(item[1],rect,w,h),position)) < 0.003:
                                end=local(item[2],rect,w,h)
                                if abs(end[0]-position[0]) > 0.1:
                                    outgoing.append((end[0]-position[0],end[1]-position[1]))
                    assert len(outgoing) == 1
                    dx,dy=outgoing[0]
                    assert ((dx>0)-(dx<0),(dy>0)-(dy<0)) == [(1,1),(-1,1),(-1,-1)][board_index]
                    assert abs(abs(dx)-abs(dy)) < 0.003
                else:
                    assert len(dots) == 15
                    for dot,(y,x) in zip(dots,product((3,2,1),range(1,6))):
                        close(local(center(dot),rect,w,h),(x,y))
                    letters = [word for word in page.get_text('words')
                               if word[4] in 'ABCDEFGHIJKLMNO' and len(word[4])==1
                               and rect.x0 < word[0] < rect.x1 and rect.y0 < word[1] < rect.y1]
                    assert len(letters) == 15
                    for label,dot in zip(letters,dots):
                        x,y=center(dot)
                        assert 0 < label[0]-x < 5 and -2 < label[1]-y < 5
                    assert ''.join(word[4] for word in letters) == 'ABCDEFGHIJKLMNO'
            if index in (5,6):
                black = [s for s in circles if s.get('fill') == (0,0,0)]
                assert len(black) == 1
                close(local(center(black[0]),rect,w,h),(0,0))
            page_boards.append({'width':w,'height':h,'cell_mm':mm,
                                'horizontal_lines':len(horizontal),'vertical_lines':len(vertical),
                                'outline_sides':4 if outlined else None})
        reports.append({'page':index+1,'band':f'Grades {bands[index]}-5','grids':page_boards})
    assert sum(page.get_text().count('Problem 1:') for page in doc) == 1
    assert sum(page.get_text().count('Problem 2:') for page in doc) == 1
    assert sum(page.get_text().count('Problem 3:') for page in doc) == 1
    assert 'one square across and one square up or down each step.' in doc[5].get_text().replace('\n',' ')
    return reports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    words = {name:unfolded_words(finish) for name,finish in [('A',(2,3)),('B',(3,3))]}
    assert set(words['A']) == {'LR','LT','RL','RT','BL','BR','BT','TB'}
    assert set(words['B']) == {'LR','LT','RL','BR','BT','TB'}
    assert {word:r['squared_length'] for word,r in words['A'].items()} == {
        'LR':53,'RL':85,'BT':37,'TB':101,'LT':25,'BL':25,'RT':41,'BR':41}
    loops = {chr(65+i):classify((x,y)) for i,(y,x) in enumerate(product((3,2,1),range(1,6)))}
    assert {letter for letter,r in loops.items() if r['kind']=='corner'} == set('ACEGIKMO')
    assert {r['steps'] for r in loops.values() if r['kind']=='loop'} == {24}
    assert loops['H']['earlier_point_returns'] == [[12,1,-1]]
    assert {letter:r['steps'] for letter,r in loops.items() if r['kind']=='corner'} == {
        'A':5,'C':9,'E':1,'G':10,'I':2,'K':11,'M':3,'O':7}
    crossings = {f'{w}x{h}':crossing_points(w,h) for w,h in [(2,3),(3,4),(4,5),(4,6),(5,6),(10,12)]}
    assert [r['count'] for r in crossings.values()] == [1,3,6,1,10,10]
    inventions = [(w,h) for w,h in product(range(1,13),repeat=2) if crossing_points(w,h)['count']==10]
    assert inventions == [(3,11),(5,6),(6,5),(10,12),(11,3),(12,10)]
    report = {'checks':'passed','method':'independent unfolded tiles/folded states/maximal-ray intersections',
              'two_bounce':words,'interior_starts':loops,'crossings':crossings,
              'ten_crossing_integer_rectangles_up_to_12':inventions,
              'actual_pdf_vectors':inspect_pdf(args.pdf),
              'convention_examples':'one-bounce angles; NE/NW/SW states; single circled X verified'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print('Independent checks passed: all examples, 144 invention cases, all 7 actual PDF page bands and grids.')

if __name__ == '__main__':
    main()
