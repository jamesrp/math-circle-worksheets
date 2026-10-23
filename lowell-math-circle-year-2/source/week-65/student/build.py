#!/usr/bin/env python3
"""Check the Week 65 geometry and compile the student packet (v4) with pdfLaTeX/TikZ.

students.tex is written from the problem files by regenerate.py, which this script runs
first unless --no-regenerate is given (the package's root build.py regenerates in place,
then builds a copy). The pages are drawn by ../figures.py from the construction in
geometry.py; verify() checks that construction. The old builder, which also wrote the
LaTeX, is archived in ../archive-before-problem-files-2026-10-23/build.py.
"""
from pathlib import Path
from math import sqrt, pi, cos, sin, atan2, acos, acosh
from collections import Counter
import argparse, cmath, json, shutil, subprocess, sys, tempfile

from geometry import *  # noqa: F401,F403  (V, circle, tangent, TILES, FOUR, NAMES, ...)

ROOT = Path(__file__).resolve().parent

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
    # Problem 6 (v3): rooms first reached in exactly 2 door crossings.
    # Octagon floor: the 48 rooms of layer 2 (56 rooms within 2 crossings, minus Home and 8).
    # Square floor: the cells at grid distance exactly 2 from Home, 12 - 4 = 8.
    squares2=sum(1 for x in range(-3,4) for y in range(-3,4) if abs(x)+abs(y)==2)
    assert squares2==8 and Counter(d for _,_,d in TILES)[2]==48
    # Problem 6's map (v4): Home, its 8 side neighbours and its 8 corner rooms. Each neighbour's
    # 8 doors lead to Home, 2 corner rooms and 5 rooms off the map; each corner room is next to
    # exactly 2 neighbours; the 8 x 5 rooms off the map are all different. So 40 + 8 = 48.
    neighbours=sorted(ADJ[HOME]); drawn={HOME,*ROOMS_AROUND_HOME}
    assert len(neighbours)==8 and len(CORNER_ROOMS)==8 and ROOMS_AROUND_HOME==neighbours+CORNER_ROOMS
    assert all(len(ADJ[c].intersection(neighbours))==2 and HOME not in ADJ[c] for c in CORNER_ROOMS)
    assert all(len(ADJ[i])==8 and len(ADJ[i].intersection(CORNER_ROOMS))==2 for i in neighbours)
    outward=[j for i in neighbours for j in ADJ[i] if j not in drawn]
    assert len(outward)==40 and len(set(outward))==40
    assert set(outward)|set(CORNER_ROOMS)=={i for i,(_,_,d) in enumerate(TILES) if d==2}
    return {'version':'W65-S-v4','student_pages':7,'problems':[1,2,3,4,5,6],
            'two_crossing_rooms':{'octagon_floor':48,'square_floor':squares2},
            'problem_6_map':{'rooms_drawn':1+len(ROOMS_AROUND_HOME),'side_neighbours':8,'corner_rooms':8,
                'neighbour_doors':{'home':1,'corner_rooms':2,'off_map':5},'off_map_rooms_distinct':40},
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



def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT.parent/'students.pdf')
    parser.add_argument('--verify-only',action='store_true')
    parser.add_argument('--no-regenerate',action='store_true',help='compile students.tex as it is')
    args=parser.parse_args()
    checks=verify()
    (ROOT/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    if args.verify_only:
        print(json.dumps(checks,indent=2));return
    if not args.no_regenerate:
        subprocess.run([sys.executable,str(ROOT/'regenerate.py')],check=True)
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
    print(f'Built {output} (seven student pages, v4). Geometry and route checks passed.')

if __name__=='__main__':main()
