#!/usr/bin/env python3
"""Enumerate a small lozenge board and check its flip graph / height functions.

Coordinates (u,v) mean (u + v/2, sqrt(3)*v/2) in unit-edge space.
Run from any directory; writes week-01-lozenge-research.json beside this file.
Only Python's standard library is needed. This is a mathematical verification
and geometry source, not a general-purpose tiling library.
"""
from collections import deque
import json
from pathlib import Path


def cross(a, b, p):
    return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])


def region(a, b, c):
    polygon = [(0,0),(a,0),(a,b),(a-c,b+c),(-c,b+c),(-c,c)]
    triangles = []
    for u in range(-c-1, a+1):
        for v in range(-1, b+c+1):
            for up, vertices in [(True,[(u,v),(u+1,v),(u,v+1)]),
                                 (False,[(u+1,v),(u+1,v+1),(u,v+1)])]:
                p = tuple(sum(q[k] for q in vertices)/3 for k in (0,1))
                if all(cross(polygon[i],polygon[(i+1)%6],p)>-1e-8 for i in range(6)):
                    triangles.append({'id':len(triangles), 'up':up, 'vertices':vertices})
    return polygon, triangles


def enumerate_board(a, b, c):
    polygon, triangles = region(a,b,c)
    vertices = sorted({v for t in triangles for v in t['vertices']})
    adjacency = {t['id']:[] for t in triangles}
    for t in triangles:
        for s in triangles:
            if len(set(t['vertices']) & set(s['vertices'])) == 2:
                adjacency[t['id']].append(s['id'])
    tilings = []
    def visit(remaining, pairs):
        if not remaining:
            tilings.append(tuple(sorted(pairs)))
            return
        t = min(remaining)
        for s in adjacency[t]:
            if s in remaining:
                visit(remaining-{t,s}, pairs+[tuple(sorted((t,s)))])
    visit(set(adjacency), [])

    edges = set()
    for t in triangles:
        vs = t['vertices']
        edges.update(tuple(sorted((vs[i],vs[(i+1)%3]))) for i in range(3))
    # Orient every edge with the up-pointing triangle on its left.
    directed = {}
    for t in triangles:
        vs = t['vertices']
        for i in range(3):
            x,y=vs[i],vs[(i+1)%3]
            if not t['up']:
                x,y=y,x
            directed[tuple(sorted((x,y)))]=(x,y)

    results = []
    for pairs in tilings:
        covered = {tuple(sorted(set(triangles[i]['vertices']) & set(triangles[j]['vertices'])))
                   for i,j in pairs}
        steps = {v:[] for v in vertices}
        for e in edges:
            x,y = directed[e]
            delta = -2 if e in covered else 1
            steps[x].append((y,delta))
            steps[y].append((x,-delta))
        heights={(0,0):0}
        queue=deque([(0,0)])
        while queue:
            x=queue.popleft()
            for y,delta in steps[x]:
                value=heights[x]+delta
                if y in heights:
                    assert heights[y]==value
                else:
                    heights[y]=value
                    queue.append(y)
        assert len(heights)==len(vertices)
        tiles=[]
        for i,j in pairs:
            vs=set(triangles[i]['vertices'])|set(triangles[j]['vertices'])
            # Hull order: an angular sort using physical coordinates.
            import math
            center=tuple(sum(v[k] for v in vs)/4 for k in (0,1))
            ordered=sorted(vs,key=lambda v:math.atan2((v[1]-center[1])*math.sqrt(3)/2,
                                                     v[0]-center[0]+(v[1]-center[1])/2))
            tiles.append({'triangles':[i,j],'vertices':ordered})
        results.append({'pairs':pairs, 'tiles':tiles, 'heights':[heights[v] for v in vertices],
                        'height_sum':sum(heights.values())})
    lowest=min(r['height_sum'] for r in results)
    for r in results:
        assert (r['height_sum']-lowest)%3==0
        r['rank']=(r['height_sum']-lowest)//3
    results.sort(key=lambda r:(r['rank'],r['pairs']))
    graph=[]
    for i,r in enumerate(results):
        r['label']=chr(65+i)
        r['neighbors']=[]
        for j,s in enumerate(results):
            different=[k for k,(x,y) in enumerate(zip(r['heights'],s['heights'])) if x!=y]
            if len(different)==1 and abs(r['heights'][different[0]]-s['heights'][different[0]])==3:
                assert len(set(r['pairs'])-set(s['pairs']))==3
                r['neighbors'].append(chr(65+j))
                if i<j:
                    graph.append({'from':chr(65+i),'to':chr(65+j),
                                  'center':vertices[different[0]]})
    # Exhaustive BFS distances must agree with the height-function formula.
    for i,r in enumerate(results):
        distances={i:0}; queue=deque([i])
        while queue:
            j=queue.popleft()
            for label in results[j]['neighbors']:
                k=ord(label)-65
                if k not in distances:
                    distances[k]=distances[j]+1;queue.append(k)
        assert len(distances)==len(results)
        r['distances']={chr(65+j):d for j,d in sorted(distances.items())}
        for j,s in enumerate(results):
            assert distances[j]*3==sum(abs(x-y) for x,y in zip(r['heights'],s['heights']))
    # The lesson board is the lattice of order ideals of a 2-by-2 grid.
    # Its normalized interior heights are binary cube-occupancy indicators.
    varying=[i for i in range(len(vertices)) if len({r['heights'][i] for r in results})>1]
    for r in results:
        r['normalized_interior_heights']=[(r['heights'][i]-results[0]['heights'][i])//3
                                          for i in varying]
        assert r['rank']==sum(r['normalized_interior_heights'])
    if (a,b,c)==(1,2,2):
        for r in results:
            edge=((0,0),(1,0))
            visited=[];path=[(0.5,0)];code=''
            while True:
                options=[]
                for k,tile in enumerate(r['tiles']):
                    vs=[tuple(v) for v in tile['vertices']]
                    horizontal=[tuple(sorted((vs[i],vs[(i+1)%4]))) for i in range(4)
                                if vs[i][1]==vs[(i+1)%4][1]]
                    if edge in horizontal and k not in visited:
                        options.append((k,horizontal))
                if not options:
                    break
                assert len(options)==1
                k,horizontal=options[0];visited.append(k)
                next_edge=next(e for e in horizontal if e!=edge)
                midpoint=tuple((next_edge[0][j]+next_edge[1][j])/2 for j in (0,1))
                delta=(midpoint[0]-path[-1][0],midpoint[1]-path[-1][1])
                assert delta in [(0,1),(-1,1)]
                code+='0' if delta==(0,1) else '1'
                path.append(midpoint);edge=next_edge
            assert len(visited)==4 and code.count('0')==code.count('1')==2
            assert edge==((-2,4),(-1,4))
            r['path_code']=code
            r['path_midpoints']=path
            r['path_tile_indices']=visited
            assert r['rank']==sum(code[i]=='1' and code[j]=='0'
                                  for i in range(4) for j in range(i+1,4))
    return {'sides':[a,b,c,a,b,c], 'coordinate_basis':'(u+v/2, sqrt(3)*v/2)',
            'polygon':polygon,'triangles':triangles,'vertices':vertices,
            'interior_vertices':[vertices[i] for i in varying],
            'tilings':results,'flips':graph}


if __name__=='__main__':
    board=enumerate_board(1,2,2)
    assert len(board['triangles'])==16
    assert len(board['tilings'])==6
    assert len(board['flips'])==6
    assert [t['rank'] for t in board['tilings']]==[0,1,2,2,3,4]
    larger=enumerate_board(2,2,2)
    assert len(larger['tilings'])==20
    output=Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(board,indent=2)+'\n')
    print(f'{output}: 6 tilings, 6 flips, diameter 4; side-2 hexagon: 20 tilings verified.')
    for t in board['tilings']:
        print(t['label'], 'rank',t['rank'],'neighbors',','.join(t['neighbors']))
