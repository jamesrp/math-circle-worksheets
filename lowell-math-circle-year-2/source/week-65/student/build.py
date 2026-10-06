#!/usr/bin/env python3
"""Build the revised Week 65 student packet (v2) with Python 3 and pdfLaTeX/TikZ.
No downloaded art, fonts, modules, or machine-specific paths are required.
"""
from pathlib import Path
from math import sqrt, pi, cos, sin, atan2, acos, acosh
from collections import Counter
import argparse, cmath, json, shutil, subprocess, tempfile

ROOT = Path(__file__).resolve().parent
R = sqrt(sqrt(2)-1)
V = [R*cmath.exp(1j*(pi/8+k*pi/4)) for k in range(8)]

def circle(p,q):
    det=p.real*q.imag-p.imag*q.real
    if abs(det)<1e-11: return None
    a=(abs(p)**2+1)/2; b=(abs(q)**2+1)/2
    c=complex((a*q.imag-p.imag*b)/det,(p.real*b-a*q.real)/det)
    return c,abs(c)**2-1

def reflect(z,p,q):
    cr=circle(p,q)
    if cr is None:
        d=q-p; return d/d.conjugate()*z.conjugate()
    c,r2=cr; return c+r2/(z-c).conjugate()

def key(z): return (round(z.real,8),round(z.imag,8))
def n(z): return f'({z.real:.9f},{z.imag:.9f})'

def path(p,q):
    cr=circle(p,q)
    if cr is None: return '-- '+n(q)
    c,r2=cr
    a=cmath.phase(p-c); b=cmath.phase(q-c)
    d=(b-a+pi)%(2*pi)-pi
    return f'arc[start angle={a*180/pi:.9f},delta angle={d*180/pi:.9f},radius={sqrt(r2):.9f}]'

def edge(p,q,style='black,line width=0.8pt'):
    return f'\\draw[{style}] {n(p)} '+path(p,q)+';\n'

def polygon(v,style):
    return f'\\path[{style}] '+n(v[0])+' '+ ' '.join(path(v[k],v[(k+1)%len(v)]) for k in range(len(v)))+' -- cycle;\n'

def full_ends(p,q):
    cr=circle(p,q)
    if cr is None:
        e=(q-p)/abs(q-p); return -e,e
    c,r2=cr; e=c/abs(c); h=sqrt(1-1/abs(c)**2)
    return e/abs(c)+1j*e*h,e/abs(c)-1j*e*h

def point(p,label=None,where='above right',style='black',rad='1.8pt'):
    out=f'\\fill[{style}] {n(p)} circle[radius={rad}];\n'
    if label: out+=f'\\node[{where},inner sep=3pt,font=\\sffamily\\bfseries\\normalsize,fill=white] at {n(p)} {{{label}}};\n'
    return out

def tangent(p,q):
    cr=circle(p,q)
    if cr is None: return (q-p)/abs(q-p)
    c,r2=cr; v=1j*(p-c); v/=abs(v)
    if (v.conjugate()*(q-p)).real<0: v=-v
    return v

# Exact isometry centered on the hyperbolic midpoint of side 7.
MIDPOINT = 2**0.25 - R
PAIR_SCALE = 3.6
SINGLE_SCALE = 3.23

def pair_view(z): return (z-MIDPOINT)/(1-MIDPOINT*z)
LEFT = [pair_view(z) for z in V]
RIGHT = [-z.conjugate() for z in LEFT]
BOUNDARY = LEFT + [RIGHT[k] for k in range(6,0,-1)]
SQUARE_BOUNDARY = [1+1j, 0+1j, 0j, 1+0j, 2+0j, 2+1j]

def extend(p,q,distance):
    """Continue beyond p, away from q, along its actual geodesic.
    distance is Euclidean arc length in disk units, for visual stub size only.
    """
    cr=circle(p,q)
    direction=-tangent(p,q)
    if cr is None: return p+distance*direction
    c,r2=cr
    turn=1 if ((1j*(p-c)).conjugate()*direction).real>0 else -1
    return c+(p-c)*cmath.exp(1j*turn*distance/sqrt(r2))

def stubs(polys,distance=.08):
    s=''; seen=set()
    for poly in polys:
        for k,p in enumerate(poly):
            q=poly[(k+1)%len(poly)]
            for a,b in ((p,q),(q,p)):
                e=extend(a,b,distance)
                ek=(key(a),key(e))
                if ek not in seen:
                    seen.add(ek)
                    s+=edge(a,e,'black!55,line width=.65pt')
    return s

def local_turns(poly,curved=True):
    angles=[]
    for k,z in enumerate(poly):
        prev,nxt=poly[(k-1)%len(poly)],poly[(k+1)%len(poly)]
        arrival=-tangent(z,prev) if curved else (z-prev)/abs(z-prev)
        departure=tangent(z,nxt) if curved else (nxt-z)/abs(nxt-z)
        angles.append(cmath.phase(departure/arrival)*180/pi)
    return angles

def min_separation(points,scale):
    return min(abs(z-w) for i,z in enumerate(points) for w in points[i+1:])*scale*25.4

def arc_length(p,q):
    cr=circle(p,q)
    if cr is None: return abs(q-p)
    c,r2=cr
    return abs(cmath.phase((q-c)/(p-c)))*sqrt(r2)

TILES=[(0j,V,0)]; INDEX={key(0j):0}; ADJ={}
for i,(center,poly,depth) in enumerate(TILES):
    ADJ.setdefault(i,set())
    if depth>=2: continue
    for k in range(8):
        p,q=poly[k],poly[(k+1)%8]
        z=reflect(center,p,q); zkey=key(z)
        if zkey not in INDEX:
            INDEX[zkey]=len(TILES)
            TILES.append((z,[reflect(w,p,q) for w in poly],depth+1))
        j=INDEX[zkey];ADJ[i].add(j);ADJ.setdefault(j,set()).add(i)

P=V[0]
def mob(z): return (z-P)/(1-P.conjugate()*z)
ROT=-cmath.exp(-1j*cmath.phase(mob(V[1])))
def corner_view(z): return ROT*mob(z)
FOUR=[i for i,(_,poly,_) in enumerate(TILES) if any(abs(z-P)<1e-7 for z in poly)]
# Determine names by actual adjacency, rather than by generation-order guesses.
HOME=0
NEIGHBORS=sorted(ADJ[HOME].intersection(FOUR))
STAR=next(i for i in FOUR if i!=0 and i not in NEIGHBORS)
# A occupies the upper-left quadrant in the recentered map; B lower-right.
A=next(i for i in NEIGHBORS if corner_view(TILES[i][0]).imag>0)
B=next(i for i in NEIGHBORS if i!=A)
NAMES={HOME:'Home', A:'A', B:'B', STAR:r'$\star$'}

def verify():
    assert Counter(d for _,_,d in TILES)=={0:1,1:8,2:48}
    incoming=Counter(j for i in ADJ[0] for j in ADJ[i] if j!=0)
    assert Counter(incoming.values())=={1:40,2:8}
    angles=[]
    for k in range(8):
        u=tangent(V[k],V[(k-1)%8]);v=tangent(V[k],V[(k+1)%8])
        deg=acos(max(-1,min(1,(u.conjugate()*v).real)))*180/pi
        assert abs(deg-90)<1e-9; angles.append(deg)
        c,r2=circle(V[k],V[(k+1)%8])
        assert abs(abs(c)**2-r2-1)<1e-10
    # Check both entire defining circles against R's defining circle.
    c3,s3=circle(V[3],V[4]); disjoint=[]
    for k in (0,7):
        c,r2=circle(V[k],V[(k+1)%8]); gap=abs(c-c3)-sqrt(r2)-sqrt(s3)
        assert gap>0; disjoint.append(gap)
    assert len(FOUR)==4 and all(len(ADJ[i].intersection(FOUR))==2 for i in FOUR)
    for i in FOUR:
        poly=[corner_view(z) for z in TILES[i][1]]
        assert len(poly)==8 and max(abs(z) for z in poly)<1
        for k in range(8):
            u=tangent(poly[k],poly[(k-1)%8]);v=tangent(poly[k],poly[(k+1)%8])
            assert abs((u.conjugate()*v).real)<1e-7
    def routes(length):
        results=[]
        def visit(route):
            if len(route)==length+1:
                if route[-1]==STAR: results.append([NAMES[x] for x in route])
                return
            for j in sorted(ADJ[route[-1]].intersection(FOUR)): visit(route+[j])
        visit([HOME]); return results
    two,four=routes(2),routes(4)
    assert len(two)==2 and len(four)==8
    # On each octagon, a repeated local left move tracks its eight sides.
    # All 8 positions are distinct; 4 moves ends at the opposite vertex.
    assert len({key(z) for z in V})==8 and abs(V[4]+V[0])<1e-10
    # Two-room geometry and physical measurements, using every pair of dots.
    assert len(BOUNDARY)==14 and len({key(z) for z in BOUNDARY})==14
    assert abs(LEFT[0]-RIGHT[0])<1e-12 and abs(LEFT[7]-RIGHT[7])<1e-12
    assert abs((LEFT[0]+LEFT[7])/2)<1e-12
    assert all(abs(z)>1e-5 for z in BOUNDARY)  # no dot at side midpoint
    for k in range(8):
        assert abs(pair_view(reflect(V[k],V[7],V[0]))-RIGHT[k])<1e-10
    pair_angles=local_turns(BOUNDARY)
    square_angles=local_turns(SQUARE_BOUNDARY,False)
    assert sum(abs(t-90)<1e-8 for t in pair_angles)==12
    assert sum(abs(t)<1e-8 for t in pair_angles)==2
    assert abs(pair_angles[0])<1e-8 and abs(pair_angles[7])<1e-8
    assert sum(abs(t-90)<1e-8 for t in square_angles)==4
    assert sum(abs(t)<1e-8 for t in square_angles)==2
    assert abs(square_angles[0])<1e-8
    metric_edges=[]
    orthogonality_errors=[]
    for poly in [V,LEFT,RIGHT]+[[corner_view(z) for z in TILES[i][1]] for i in FOUR]:
        for k,p in enumerate(poly):
            q=poly[(k+1)%8]
            metric_edges.append(acosh(1+2*abs(p-q)**2/((1-abs(p)**2)*(1-abs(q)**2))))
            u=tangent(p,poly[(k-1)%8]);v=tangent(p,q)
            assert abs((u.conjugate()*v).real)<1e-7
            cr=circle(p,q)
            if cr is not None:
                c,r2=cr;orthogonality_errors.append(abs(abs(c)**2-r2-1))
    assert max(metric_edges)-min(metric_edges)<1e-9
    pair_chords=[abs(BOUNDARY[(k+1)%14]-z)*PAIR_SCALE*25.4 for k,z in enumerate(BOUNDARY)]
    pair_arcs=[arc_length(z,BOUNDARY[(k+1)%14])*PAIR_SCALE*25.4 for k,z in enumerate(BOUNDARY)]
    minimum=min_separation(BOUNDARY,PAIR_SCALE)
    assert abs(minimum-17.850196284)<1e-8
    visual_extents=[extend(p,poly[(k+1)%len(poly)],.06) for poly in [LEFT,RIGHT] for k,p in enumerate(poly)]
    visual_extents += [extend(p,poly[(k-1)%len(poly)],.06) for poly in [LEFT,RIGHT] for k,p in enumerate(poly)]
    assert max(abs(z) for z in visual_extents)<1
    # The three-state curved visual uses these actual tangents.
    departure=tangent(V[0],V[1]);arrival=-tangent(V[1],V[0]);turned=tangent(V[1],V[2])
    assert abs(cmath.phase(turned/arrival)*180/pi-90)<1e-8
    return {'version':'W65-S-v2','student_pages':6,'problems':[1,2,3,4,5],
            'geometry':'regular hyperbolic {8,4}', 'corner_degrees':angles,
            'layer_counts':[1,8,48], 'two_step_multiplicities':{'once':40,'twice':8},
            'whole_circle_disjointness_gaps':disjoint,
            'four_room_tile_ids':FOUR, 'two_door_routes':two,'four_door_routes':four,
            'left_loop_first_return':8,'left_loop_position_after_four':'E, opposite vertex',
            'square_grid_sample_routes':{'4':'ENWS','6':'EENWWS','8':'EENNWWSS'},
            'curved_visual_headings_degrees':[cmath.phase(z)*180/pi for z in (departure,arrival,turned)],
            'two_octagons':{'midpoint':MIDPOINT,'scale_inches_per_unit':PAIR_SCALE,
                'boundary_vertices':[[z.real,z.imag] for z in BOUNDARY],
                'edge_moves':14,'left_turns':12,'straight_junctions':2,
                'local_turn_degrees':pair_angles,'start_is_straight':True,'midpoint_has_dot':False,
                'width_inches':(max(z.real for z in BOUNDARY)-min(z.real for z in BOUNDARY))*PAIR_SCALE,
                'height_inches':(max(z.imag for z in BOUNDARY)-min(z.imag for z in BOUNDARY))*PAIR_SCALE,
                'edge_arcs_mm':pair_arcs,'adjacent_junction_distances_mm':pair_chords,
                'all_pairs_min_junction_separation_mm':minimum,
                'clear_gap_for_10mm_counters_mm':minimum-10,
                'clear_gap_for_15mm_counters_mm':minimum-15,
                'context_stub_envelope_inches':[min(z.real for z in visual_extents)*PAIR_SCALE,
                    max(z.real for z in visual_extents)*PAIR_SCALE,
                    min(z.imag for z in visual_extents)*PAIR_SCALE,
                    max(z.imag for z in visual_extents)*PAIR_SCALE]},
            'two_squares':{'edge_moves':6,'left_turns':4,'straight_junctions':2,
                'local_turn_degrees':square_angles,'min_junction_separation_mm':27.94},
            'single_octagon':{'scale_inches_per_unit':SINGLE_SCALE,
                'all_pairs_min_junction_separation_mm':min_separation(V,SINGLE_SCALE),
                'vertex_label_center_clearance_mm':abs(V[0])*.22*SINGLE_SCALE*25.4},
            'grid_min_junction_separation_mm':.76*25.4,
            'room_record_sheet':{'two_crossing_lines':3,'four_crossing_lines':10,
                'line_width_inches':6.9,'four_crossing_line_pitch_inches':.55},
            'all_room_hyperbolic_edge_length_range':[min(metric_edges),max(metric_edges)],
            'orthogonality_max_error':max(orthogonality_errors),
            'status':'Digitally verified revised packet; not physically rehearsed or classroom piloted.'}


PRE=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc}
\usepackage{amssymb}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''

def page_start(number):
    return r'\noindent\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]'+ '\n'+r'\begin{scope}[shift={(current page.south west)}]'+ '\n'+r'\node[anchor=west,font=\sffamily\fontsize{10.8}{13}\selectfont] at (0.62,10.52) {Week 65 / Hyperbolic octagon streets / Grades 3--5};'+ '\n'+f'\\node[anchor=west,font=\\sffamily\\fontsize{{9}}{{11}}\\selectfont] at (0.62,0.42) {{Bellingham Math Circle / Week 65 / W65-S-v2}};\n'+f'\\node[anchor=east,font=\\sffamily\\small] at (7.88,0.42) {{{number}}};\n'

def text(x,y,width,body,size=12.5,leading=16):
    return f'\\node[anchor=north west,inner sep=0pt,text width={width}in,align=left,font=\\sffamily\\fontsize{{{size}}}{{{leading}}}\\selectfont] at ({x},{y}) {{{body}}};\n'

def end(): return '\\end{scope}\n\\end{tikzpicture}\\null\\newpage\n'

def scope(x,y,scale): return f'\\begin{{scope}}[shift={{({x},{y})}},x={scale}in,y={scale}in]\n'

def square_grid(size=4,step=.5):
    s=''
    for k in range(-size,size+1):
        s+=f'\\draw[black!65,line width=0.6pt] ({k*step},{-size*step}) -- ({k*step},{size*step});\n'
        s+=f'\\draw[black!65,line width=0.6pt] ({-size*step},{k*step}) -- ({size*step},{k*step});\n'
    for k in range(-size,size+1):
        for l in range(-size,size+1): s+=f'\\fill[black] ({k*step},{l*step}) circle[radius=1.25pt];\n'
    return s

def arrow(p,q,style='black,line width=1.2pt'):
    return f'\\draw[{style},-{{Latex[length=3mm,width=2.2mm]}}] {n(p)} -- {n(q)};\n'

def packet():
    out=PRE
    # Page 1. A single procedure example, then a roomy square-grid investigation.
    out+=page_start(1)
    out+=text(.65,10.13,7.1,r'Use a slim 10 mm paper arrow. One move follows an edge to the next dot. Then turn left, turn right, or go straight. The arrow shows which way you face. One partner moves; the other checks. Swap roles.')
    for j,(label,pos,heading) in enumerate([('Start',0j,1),('Move one edge',1+0j,1),('Turn left',1+0j,1j)]):
        out+=scope(1.62+j*2.55,8.72,.4)
        for k in range(-1,3):
            out+=f'\\draw[black!35,line width=.55pt] ({k},-1) -- ({k},1);\n'
        for k in range(-1,2): out+=f'\\draw[black!35,line width=.55pt] (-1,{k}) -- (2,{k});\n'
        out+=point(0j,rad='1.5pt')+point(1+0j,rad='1.5pt')
        if j: out+='\\draw[black,line width=1.6pt] (0,0)--(1,0);\n'
        out+=arrow(pos-heading*.17,pos+heading*.43)
        out+='\\end{scope}\n'
        out+=text(.99+j*2.55,8.19,2.1,label,10.5,13)
    out+=text(.65,7.66,7.1,r'\textbf{Problem 1:} Start at A, facing along the arrow. Find routes of 4, 6, and 8 moves that return to A facing the same way. Never turn around.')
    out+=scope(4.25,3.96,1)
    out+=square_grid(3,.76)
    out+=point(0j,rad='2.2pt')
    out+='\\node[font=\\sffamily\\bfseries\\normalsize,fill=white,inner sep=2pt] at (-.26,-.26) {A};\n'
    out+=arrow(.07+0j,.49+0j)
    out+='\\end{scope}\n'
    out+=end()
    # Page 2. Preserve the large working octagon; context is only crossing stubs.
    out+=page_start(2)
    out+=text(.65,10.13,7.1,r'Each octagon has eight right-angle corners. The rooms are all the same size in this geometry. The map makes straight streets look curved.')
    out+=text(.65,9.47,7.1,r'Keep the arrow along the road as it bends. Turn left or right from the arrival direction.')
    for j,label in enumerate(['Start along the road','Arrive along the road','Turn left']):
        out+=scope(1.25+j*2.5,7.91,1.20)
        out+=edge(V[0],V[1],'black!55,line width=.8pt')
        out+=edge(V[1],V[2],'black!55,line width=.8pt')
        out+=point(V[0],rad='1.7pt')+point(V[1],rad='1.7pt')
        pos=V[0] if j==0 else V[1]
        direction=tangent(V[0],V[1]) if j==0 else (-tangent(V[1],V[0]) if j==1 else tangent(V[1],V[2]))
        out+=arrow(pos-direction*.14,pos+direction*.19,'black,line width=1.35pt,preaction={draw=white,line width=3.8pt}')
        out+='\\end{scope}\n'
        out+=text(.80+j*2.5,7.97,2.35,label,10.5,13)
    out+=text(.65,7.49,7.1,r'\textbf{Problem 2:} Start at A, facing along the road toward B. Move one edge and turn left, over and over. Mark where you are after 4 moves. How many moves make the first return to your starting place and heading? Start toward H and try only right turns.')
    out+=scope(4.25,3.69,SINGLE_SCALE)
    out+=stubs([V],.10)
    for k in range(8): out+=edge(V[k],V[(k+1)%8],'black,line width=1.05pt')
    for k,z in enumerate(V):
        out+=point(z,rad='2.4pt')
        out+=f'\\node[font=\\sffamily\\bfseries\\large,fill=white,inner sep=2pt] at {n(z*.78)} {{{chr(65+k)}}};\n'
    start=V[0];t=tangent(V[0],V[1]);out+=arrow(start+t*.025,start+t*.147)
    out+='\\end{scope}\n'
    out+=text(.65,1.08,7.1,r'Left turns: \rule{0.72in}{0.35pt} moves \hspace{0.5in} Right turns: \rule{0.72in}{0.35pt} moves',12,15)
    out+=end()
    # Page 3. The actual midpoint-centered pair, at 3.6 inches per disk unit.
    out+=page_start(3)
    out+=text(.65,10.13,7.1,r'\textbf{Problem 3:} Walk once around the outside of both rooms, starting at A along the arrow. Keep both rooms on your left. Count only the turns at dots. Mark dots where you go straight. Compare the two octagons with the two squares.')
    out+=scope(4.25,6.88,PAIR_SCALE)
    out+=stubs([LEFT,RIGHT],.06)
    out+=edge(LEFT[7],LEFT[0],'black!65,line width=.85pt')
    for k,z in enumerate(BOUNDARY):
        out+=edge(z,BOUNDARY[(k+1)%14],'black,line width=1.15pt')
        out+=point(z,rad='2.3pt')
    # Only endpoints of the shared side are tiling junctions. Never dot its midpoint.
    start=LEFT[0];t=tangent(start,LEFT[1])
    out+=arrow(start+t*.025,start+t*.135)
    out+=f'\\node[font=\\sffamily\\bfseries\\large,inner sep=2pt,fill=white] at {n(start+.12+.06j)} {{A}};\n'
    out+='\\end{scope}\n'
    out+=text(1.05,4.63,6.4,r'Around two octagons: \rule{1.0in}{0.35pt} left turns',12.5,16)
    out+=scope(3.15,2.48,1.1)
    for z in SQUARE_BOUNDARY:
        for direction in (1,-1,1j,-1j):
            out+=f'\\draw[black!55,line width=.65pt] {n(z)} -- {n(z+.18*direction)};\n'
    for k,z in enumerate(SQUARE_BOUNDARY):
        q=SQUARE_BOUNDARY[(k+1)%6]
        out+=f'\\draw[black,line width=1.15pt] {n(z)} -- {n(q)};\n'
        out+=point(z,rad='2.3pt')
    out+='\\draw[black!65,line width=.85pt] (1,0)--(1,1);\n'
    out+=arrow(.94+1j,.582+1j)
    out+='\\node[font=\\sffamily\\bfseries\\large,inner sep=2pt,fill=white] at (1.22,1.24) {A};\n'
    out+='\\end{scope}\n'
    out+=text(1.05,1.78,6.4,r'Around two squares: \rule{1.0in}{0.35pt} left turns',12.5,16)
    out+=end()
    # Page 4. Complete actual geodesics, never a finite-crop inference.
    out+=page_start(4)
    out+=text(.65,10.13,7.1,r'A complete street goes straight through every crossing, taking the opposite branch. Streets continue forever. The dotted circle is the edge of the map; no number of moves reaches it. Only some streets are drawn.')
    out+=text(.65,8.99,7.1,r'\textbf{Problem 4:} Trace every drawn complete street through P in both directions. How many miss the heavy dashed street R? Can two distinct ordinary straight lines through one point both miss a third line? The ordinary lines also continue forever in both directions. Draw or explain below.')
    out+=scope(4.25,5.20,2.92)
    out+='\\draw[black!45,densely dotted,line width=.75pt] (0,0) circle[radius=1];\n'
    for k in range(8):
        a,b=full_ends(V[k],V[(k+1)%8])
        out+=edge(a,b,'black,line width=.78pt')
    a,b=full_ends(V[3],V[4]);out+=edge(a,b,'black,line width=2.3pt,dash pattern=on 5pt off 2.8pt')
    out+=f'\\node[font=\\sffamily\\bfseries\\large,fill=white,inner sep=3pt] at (-0.77,0.08) {{R}};\n'
    out+=point(P,rad='2.8pt')
    out+=f'\\node[font=\\sffamily\\bfseries\\large,inner sep=0pt] at {n(P-.10-.045j)} {{P}};\n'
    out+='\\end{scope}\n'
    out+=end()
    # Page 5. A recentered isometry makes all four local rooms usable.
    out+=page_start(5)
    out+=text(.65,10.13,7.1,r'For room routes, put a coin inside a room. A door crossing moves it across one shared side into the next room. Crossing a corner is not allowed. Write the rooms in the order you visit them.')
    out+=scope(1.32,8.70,.52)
    for k,lab in enumerate('CDE'):
        out+=f'\\draw[line width=.75pt] ({k},0) rectangle ({k+1},1);\n'
        out+=f'\\node[font=\\sffamily\\normalsize] at ({k+.5},.65) {{{lab}}};\n'
    out+='\\draw[-{Latex[length=2mm]},line width=1pt] (.35,.25)--(2.65,.25);\n'
    out+='\\end{scope}\n'
    out+=text(3.30,9.05,4.10,r'$C\ \rightarrow\ D\ \rightarrow\ E$\\[5pt]Two door crossings',11.5,14)
    out+=text(.65,8.29,7.1,r'\textbf{Problem 5:} This is another view of the same geometry, showing four rooms around one corner. Find every room route from Home to $\star$ using exactly 2 door crossings. Then find every route using exactly 4 door crossings. Stay in these four rooms. You may visit a room or use a door more than once.')
    out+=scope(4.25,3.72,2.82)
    # Lightly differentiated printable fills support the four readable regions.
    for i in FOUR:
        poly=[corner_view(z) for z in TILES[i][1]]
        out+=polygon(poly, 'fill=black!'+('5' if i==0 else '0')+',draw=none')
    seen=set()
    for i in FOUR:
        poly=[corner_view(z) for z in TILES[i][1]]
        for k in range(8):
            p,q=poly[k],poly[(k+1)%8];ek=tuple(sorted((key(p),key(q))))
            if ek in seen:continue
            seen.add(ek);out+=edge(p,q,'black,line width=.9pt')
        c=corner_view(TILES[i][0])*.88
        out+=f'\\node[font=\\sffamily\\bfseries\\Large,inner sep=3pt] at {n(c)} {{{NAMES[i]}}};\n'
    out+=point(0j,rad='2pt')
    out+='\\end{scope}\n'
    out+=text(.65,.92,7.1,r'Keep the route sheet beside this board.',10.5,13)
    out+=end()
    # Page 6 stays beside page 5 so the route catalog and coin state coexist.
    out+=page_start(6)
    out+=text(.65,10.13,7.1,r'Extra workspace for Problem 5. Keep the board beside this sheet.')
    out+=text(.80,9.47,7.0,r'2 door crossings',12.5,16)
    for y in (8.85,8.25,7.65):
        out+=f'\\draw[black!55,line width=.4pt] (.80,{y}) -- (7.70,{y});\n'
    out+=text(.80,7.06,7.0,r'4 door crossings',12.5,16)
    for j in range(10):
        y=6.45-j*.55
        out+=f'\\draw[black!55,line width=.4pt] (.80,{y:.2f}) -- (7.70,{y:.2f});\n'
    out+=end()
    out+=r'\end{document}'+'\n'
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT.parent/'students.pdf')
    parser.add_argument('--verify-only',action='store_true')
    args=parser.parse_args()
    checks=verify()
    (ROOT/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    (ROOT/'students.tex').write_text(packet())
    if args.verify_only:
        print(json.dumps(checks,indent=2));return
    if not shutil.which('pdflatex'): raise SystemExit('Install a TeX distribution providing pdflatex, TikZ and amssymb.')
    output=args.output.resolve();output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='week65-build-') as tmp:
        dest=Path(tmp)
        shutil.copy(ROOT/'students.tex',dest/'students.tex')
        for _ in range(2):
            run=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','students.tex'],cwd=dest,capture_output=True,text=True)
            if run.returncode:
                print(run.stdout);raise SystemExit(run.returncode)
        shutil.copy(dest/'students.pdf',output)
        (ROOT/'build.log').write_text((dest/'students.log').read_text())
    print(f'Built {output} (six student pages, v2). Geometry and route checks passed.')

if __name__=='__main__':main()
