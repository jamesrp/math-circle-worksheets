"""Week 14 boards and page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py). The October 23, 2026 card
fixes added the light-gray starts in K-1 P5's copies (START_GRAY), the arrows from the
three starts to the target in grades 4-5 P4 and a higher copy grid in grades 2-3 P6.

Coordinates are inches with y pointing down, measured from the page's top-left corner,
as the old builder drew them. Each page is one overlay picture: page_open(page) draws
the header, page_close(page) the footer and page number after the page's drawings, so
the rebuilt LaTeX is the old builder's byte for byte. Problem files call the figure
functions below by name; the rule, prompt and caption wording lives in the problem files.
The enumeration that names the printed fillings is here too; the checks that use it are
in editable/src/student_checks.py.
"""
import itertools
import math
from collections import deque


# ---------------------------------------------------------------- fillings, by noncrossing diagonal sets

def diagonals(n):
    return [(a,b) for a in range(n) for b in range(a+1,n) if b-a>1 and (a,b)!=(0,n-1)]
def cross(e,f):
    a,b=e; c,d=f
    return (a<c<b<d) or (c<a<d<b)
def fillings(n):
    return [frozenset(t) for t in itertools.combinations(diagonals(n),n-3)
            if all(not cross(a,b) for a,b in itertools.combinations(t,2))]
def graph(ts):
    return {t:[s for s in ts if len(t^s)==2] for t in ts}
def dist(g,s,t):
    q=deque([(s,0)]); seen={s}
    while q:
        u,d=q.popleft()
        if u==t: return d
        for v in g[u]:
            if v not in seen: seen.add(v); q.append((v,d+1))
def fan(n,v):
    return frozenset(e for e in diagonals(n) if v in e)
def es(*pairs): return frozenset((min(a,b)-1,max(a,b)-1) for a,b in pairs)

G5=graph(fillings(5))          # the pentagon map, for map_drawings' cycle-order check
hex_fan_b=fan(6,1)
hex_center=es((1,3),(3,5),(1,5))
hex_fan_d=fan(6,3)
oct_start=es((1,3),(1,4),(4,6),(4,7),(4,8))
oct_end=es((2,4),(2,5),(5,7),(5,8),(1,5))


# ---------------------------------------------------------------- drawing

# All coordinates are in inches from the page's top left.
# Thick outlines and vertex dots remain legible on a monochrome copier.
def text(x,y,w,s,size=14,bold=False):
    style='\\bfseries ' if bold else ''
    return (rf'\node[anchor=north west,inner sep=0pt,text width={w}in,align=left,'
            rf'font=\sffamily\fontsize{{{size}}}{{{size*1.25:.2f}}}\selectfont] at ({x},{y}) '
            '{'+style+s+'};\n')

def polygon(n,cx,cy,w,h,edges=(),labels='numbers',small=False,regular=True,edge_color=None):
    # Use one physical scale for every regular board, fitted inside its layout box.
    # The small flip examples explicitly opt out to preserve general quadrilaterals.
    raw=[(math.cos(math.pi/2-2*math.pi*i/n),-math.sin(math.pi/2-2*math.pi*i/n)) for i in range(n)]
    xmin=min(x for x,y in raw); xmax=max(x for x,y in raw)
    ymin=min(y for x,y in raw); ymax=max(y for x,y in raw)
    sx=w/(xmax-xmin); sy=h/(ymax-ymin)
    if regular: sx=sy=min(sx,sy)
    pts=[(cx+(x-(xmin+xmax)/2)*sx,cy+(y-(ymin+ymax)/2)*sy) for x,y in raw]
    p='\\begin{scope}\n' + f'% polygon: {"regular" if regular else "general-convex"} n={n}\n'
    for i,(x,y) in enumerate(pts): p+=rf'\coordinate (v{i}) at ({x:.4f},{y:.4f});'+'\n'
    p+=r'\draw[line width=0.95pt,line join=round] '+' -- '.join(f'(v{i})' for i in range(n))+r' -- cycle;'+'\n'
    colour=f',{edge_color}' if edge_color else ''   # K-1 P5's copies print the start in light gray
    for a,b in sorted(edges): p+=rf'\draw[line width=0.85pt{colour}] (v{a}) -- (v{b});'+'\n'
    for i,(x,y) in enumerate(pts):
        p+=rf'\fill (v{i}) circle[radius={0.014 if small else 0.022}in];'+'\n'
        # Outward label offsets in physical units, independent of polygon aspect ratio.
        dx=x-cx; dy=y-cy; norm=math.hypot(dx,dy)
        off=0.12 if small else 0.19
        lx=x+off*dx/norm; ly=y+off*dy/norm
        lab=str(i+1) if labels=='numbers' else chr(65+i)
        p+=rf'\node[inner sep=0pt,font=\sffamily\fontsize{{{8 if small else 13}}}{{14}}\selectfont] at ({lx:.4f},{ly:.4f}) {{{lab}}};'+'\n'
    return p+'\\end{scope}\n'

# Small polygons are recording copies; investigations retain a larger working polygon.
def copies(n,rows,cols,starty,labels='numbers',rowgap=1.30,w=1.35,h=.87):
    xs=[.95+i*(6.60/(cols-1)) for i in range(cols)] if cols>1 else [4.25]
    # Center copies in a narrower horizontal range when only three columns are used.
    if cols==3: xs=[1.45,4.25,7.05]
    if cols==4: xs=[1.35,3.28,5.22,7.15]
    return ''.join(polygon(n,x,starty+r*rowgap,w,h,labels=labels,small=True) for r in range(rows) for x in xs)
def large_plus_copies(n,edges=(),labels='numbers',topcy=4.25,copyy=7.45):
    if n==6:
        return polygon(n,4.25,topcy,4.8,4.40,edges,labels)+copies(n,2,4,7.55,labels,rowgap=1.78,w=1.30,h=1.30)
    return polygon(n,4.25,topcy,4.8,3.35,edges,labels)+copies(n,2,4,copyy,labels,rowgap=1.50,w=1.30,h=.92)

def flip_example():
    """The AC-to-BD example before the map; its caption is a text section in the problem file."""
    example=polygon(4,1.35,2.47,.95,.60,es((1,3)),'letters',True,regular=False)+polygon(4,3.20,2.47,.95,.60,es((2,4)),'letters',True,regular=False)
    example+=r'\draw[rounded corners=2pt,black!55] (.65,1.94) rectangle (2.05,3.00); \draw[rounded corners=2pt,black!55] (2.50,1.94) rectangle (3.90,3.00); \draw[line width=.8pt] (2.05,2.47)--(2.50,2.47);'+'\n'
    return example
def pentagon_map():
    """The five pentagon fans in cycle order around the page."""
    positions=[(2.00,4.05),(6.25,4.25),(6.65,6.90),(4.25,9.00),(1.55,6.65)]
    order=[0,2,4,1,3]
    assert all(fan(5,order[(i+1)%5]) in G5[fan(5,order[i])] for i in range(5))
    return ''.join(polygon(5,x,y,1.9,1.40,fan(5,j),'letters') for (x,y),j in zip(positions,order))

def first_page_pair(n1,n2,labels='numbers'):
    drawings=''
    for n,y in [(n1,4.20),(n2,8.05)]:
        if n==7 and n1==6: y=8.25
        if n==6:
            if n==n1: y=4.35
            drawings+=polygon(n,3.00,y,4.20,3.50,labels=labels)
            for dy in [-.97,.97]:
                drawings+=polygon(n,6.70,y+dy,1.50,1.35,labels=labels,small=True)
        else:
            drawings+=polygon(n,3.00,y,4.20,2.80,labels=labels)
            for dy in [-.80,.80]:
                drawings+=polygon(n,6.70,y+dy,1.50,1.05,labels=labels,small=True)
    return drawings

START_GRAY='black!35'   # light enough to read as a start to change, dark enough to photocopy

def two_cases_with_records(n1,n2,e1=(),e2=(),labels='numbers',keep_edges=False,gray_edges=False):
    drawings=''
    for n,y,edges in [(n1,3.05,e1),(n2,7.10,e2)]:
        if n==6:
            cy=3.75 if y<5 else 8.00
            drawings+=polygon(n,2.35,cy,4.80,3.45,edges,labels)
            for x in [5.25,7.15]:
                for dy in [-.90,.90]:
                    if gray_edges:
                        drawings+=polygon(n,x,cy+dy,1.30,1.30,edges,labels,small=True,edge_color=START_GRAY)
                    else:
                        drawings+=polygon(n,x,cy+dy,1.30,1.30,edges if keep_edges else (),labels,small=True)
        else:
            drawings+=polygon(n,4.25,y,4.80,2.30,edges,labels)
            for x in [1.35,3.28,5.22,7.15]:
                drawings+=polygon(n,x,y+2.00,1.30,.80,edges if keep_edges else (),labels,small=True)
    return drawings

THREE_STARTS_Y=2.40; TARGET_Y=4.58   # card fix: room for arrows from each start to the target
def three_routes():
    drawings=''
    for x,edges in zip([1.65,4.25,6.85],[hex_fan_b,hex_center,hex_fan_d]):
        drawings+=polygon(6,x,THREE_STARTS_Y,1.75,1.50,edges,'letters',True)
    drawings+=polygon(6,4.25,TARGET_Y,1.75,1.50,fan(6,0),'letters',True)
    for start,end in [((2.25,3.12),(3.42,3.90)),((4.25,3.37),(4.25,3.61)),((6.25,3.12),(5.08,3.90))]:
        drawings+=rf'\draw[-stealth,line width=.8pt] {start} -- {end};'+'\n'
    drawings+=polygon(6,2.35,7.70,4.80,4.00,labels='letters')
    for x in [5.25,7.15]:
        for y in [5.70,7.05,8.40,9.75]:
            drawings+=polygon(6,x,y,1.30,.95,labels='letters',small=True)
    return drawings

def hexagon_route_23():
    """Grades 2-3: the B fan, an arrow, the A fan, a working hexagon and eight copies."""
    return (polygon(6,2.05,2.85,2.15,1.85,hex_fan_b,'letters')+polygon(6,6.35,2.85,2.15,1.85,fan(6,0),'letters')
            +r'\draw[-stealth,line width=.8pt] (3.45,2.85) -- (4.95,2.85);'+'\n'+polygon(6,4.25,5.90,4.8,3.80,labels='letters')
            +copies(6,2,4,8.25,'letters',rowgap=1.40,w=1.30,h=.96))   # card fix: bottom row clear of the footer (was 8.38)

def octagon_route_45():
    """Grades 4-5: the two printed octagon fillings, an arrow and a working octagon."""
    return (polygon(8,2.05,3.0,2.15,1.65,oct_start,'letters')+polygon(8,6.35,3.0,2.15,1.65,oct_end,'letters')
            +r'\draw[-stealth,line width=.8pt] (3.45,3.0) -- (4.95,3.0);'+'\n'+polygon(8,4.25,6.10,4.8,3.0,labels='letters'))


# ---------------------------------------------------------------- page template

def page_preamble(week, topic, header, footer):
    return r'''\documentclass[letterpaper]{article}
\usepackage[margin=0in]{geometry}
\pdfmapfile{+cm.map}
\usepackage{type1cm}
\usepackage{tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''


def page_open(page):
    """The old Packet.page() up to the rules: the overlay picture and the header."""
    s='\\begin{tikzpicture}[remember picture,overlay,x=1in,y=-1in]\n'
    s+='\\begin{scope}[shift={(current page.north west)}]\n'
    s+=text(.55,.36,7.4,rf'Week {page.week} / {page.topic} / {page.header}',10.8,True)
    return s


def page_close(page):
    """The old Packet.page() after the drawings: footer, page number, end of picture.
    The composer adds the \\newpage between pages."""
    s=text(.55,10.48,6.9,rf'Bellingham Math Circle / Week {page.week} / {page.footer}',9)
    s+=text(7.56,10.48,.36,str(page.number),9)
    return s+'\\end{scope}\n\\end{tikzpicture}\n\\null\n'


def page_prompt(n, body, x, y, size):
    """The old problem statement: below the rules on page 1 (@1.78), else at 0.91 in."""
    return text(.65,.91 if y is None else y,7.2,rf'\textbf{{Problem {n}:}} '+body,size)


def page_text(x, y, body, w, size):
    return text(x,y,w,body,size)
