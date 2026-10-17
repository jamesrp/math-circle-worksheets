"""Concrete draft checks independent of author programs."""
from itertools import permutations
from pathlib import Path
import json
import math

from independent_check import cells, corners, difference_table, frozen, rectifications, slide, standard_fillings, valid

OUT = Path(__file__).resolve().parent

def cascade(inputs, stages=2, starts=None):
    state = list(starts or [0]*stages)
    result = [list(state)]
    for value in inputs:
        new = list(state)
        new[0] += value
        for i in range(1, stages):
            new[i] += new[i-1]
        state = new
        result.append(list(state))
    return result

def disk_check(central_radius, neighbors):
    for x,y,r in neighbors:
        assert math.isclose(math.hypot(x,y), central_radius+r)
    separations = []
    for i,(x,y,r) in enumerate(neighbors):
        for X,Y,R in neighbors[i+1:]:
            distance = math.hypot(x-X,y-Y)
            assert distance >= r+R-1e-9
            separations.append([distance,r+R])
    return separations

def traces(outer, inner, labels, chosen_corners):
    result = []
    for corner in chosen_corners:
        o,i,t,path = slide(outer,inner,labels,corner)
        result.append({'start':corner,'path':[corner]+[tuple(m['from']) for m in path],'labels':sorted(t.items()),'outer':sorted(o),'inner':sorted(i)})
        outer,inner,labels = o,i,t
    assert not inner
    return result

def reverse_one(labels, exit, start):
    labels = dict(labels)
    hole = exit
    moved = []
    while hole != start:
        r,c = hole
        neighbors = [p for p in ((r-1,c),(r,c-1)) if p in labels]
        assert neighbors
        source = max(neighbors,key=labels.get)
        value = labels.pop(source)
        labels[hole] = value
        moved.append(value)
        hole = source
    return labels,moved

def larger_slide(labels,start):
    labels = dict(labels)
    hole = start
    while True:
        r,c = hole
        neighbors = [p for p in ((r+1,c),(r,c+1)) if p in labels]
        if not neighbors:
            return labels,hole
        source = max(neighbors,key=labels.get)
        labels[hole] = labels.pop(source)
        hole = source

def main():
    checked = {}
    centers = [(x,y) for y in (20,20+40*math.sqrt(3)) for x in (20,60,100,140)] + [(x,20+20*math.sqrt(3)) for x in (40,80,120)]
    assert all(math.dist(a,b)>=40-1e-9 for i,a in enumerate(centers) for b in centers[i+1:])
    assert all(20<=x<=140 and 20<=y<=90 for x,y in centers)
    checked['88'] = {'P2_11_centers':centers,'P6_row_height':40+40*math.sqrt(3), 'P7_first_mixed_separations':disk_check(20,[(60,0,40),(0,60,40),(-60,0,40),(0,-40,20)])}
    second_mixed = [(80,0,40)] + [(60*math.cos(k*math.pi/3),60*math.sin(k*math.pi/3),20) for k in range(1,6)]
    checked['88']['P7_second_mixed_separations'] = disk_check(40,second_mixed)
    mixed_eight = [(80,0,40)] + [(60*math.cos(math.radians(a)),60*math.sin(math.radians(a)),20) for a in (50,90,130,170,210,250,290)]
    mixed_five = [(60,0,40)] + [(40*math.cos(math.radians(a)),40*math.sin(math.radians(a)),20) for a in (80,140,200,260)]
    mixed_angle_large_center = 2*math.asin(math.sqrt(20*40/(60*80)))
    small_angle_large_center = 2*math.asin(20/60)
    mixed_angle_small_center = 2*math.asin(math.sqrt(20*40/(40*60)))
    small_angle_small_center = math.pi/3
    assert 2*mixed_angle_large_center+7*small_angle_large_center>2*math.pi
    assert 2*mixed_angle_small_center+4*small_angle_small_center>2*math.pi
    checked['88']['optional_P7_exact_mixed_maxima'] = {'large_center_maximum':8,'eight_disk_separations':disk_check(40,mixed_eight),'nine_disk_lower_bound_total_angle_deg':math.degrees(2*mixed_angle_large_center+7*small_angle_large_center),'small_center_maximum':5,'five_disk_separations':disk_check(20,mixed_five),'six_disk_lower_bound_total_angle_deg':math.degrees(2*mixed_angle_small_center+4*small_angle_small_center)}
    sample = cascade([2,0,1,0,2])
    assert sample == [[0,0],[2,2],[2,4],[3,7],[3,10],[5,15]]
    orders = sorted(set(permutations([2,0,1,0,2])))
    outputs = [(order,cascade(order)[-1][-1]) for order in orders]
    assert len(outputs)==30
    assert min(v for _,v in outputs)==9
    assert max(v for _,v in outputs)==21
    assert cascade([2,2,1,0,0])[-1][-1]==21
    assert cascade([0,0,1,2,2])[-1][-1]==9
    assert cascade([1,0,2])==[[0,0],[1,1],[1,2],[3,5]]
    assert cascade([2,0,1,0,2],stages=1,starts=[4])==[[4],[6],[6],[7],[7],[9]]
    three_stage = cascade([1,1,1,1],stages=3)
    assert three_stage == [[0,0,0],[1,1,1],[2,3,4],[3,6,10],[4,10,20]]
    tetra_counts = [sum(i+j+k<=n-1 for i in range(n) for j in range(n) for k in range(n)) for n in range(5)]
    assert tetra_counts == [0,1,4,10,20]
    checked['89'] = {'P1_square_totals':[n*n for n in range(7)],'P2_staircase':[n*(n+1)//2 for n in range(6)],'P2_rectangle':[n*(n+1) for n in range(6)],'P3_plus4_odd':[4+n*n for n in range(1,6)],'P3_plus4_even':[4+n*(n+1) for n in range(1,6)],'P4_examples':[[1,2,3,4],[5,0,5,0]],'P5_visual':cascade([1,0,2]),'P5_sample':sample,'P5_all_30_orders':outputs,'P6_start4':cascade([2,0,1,0,2],stages=1,starts=[4]),'P7_square_fifth':25,'P7_square_tail_fifth':26,'P8_shells':[n**3-(n-1)**3 for n in range(1,5)],'P9_three_stage':three_stage,'P9_tetrahedral_counts':tetra_counts}
    for n in range(1,5):
        assert n*n+n*(n-1)+(n-1)**2==n**3-(n-1)**3
    one_outer, one_inner = cells((3,2)), cells((1,))
    four_positions = [(1,2),(1,3),(2,1),(2,2)]
    A = dict(zip(four_positions,[1,4,2,3]))
    B = dict(zip(four_positions,[2,3,1,4]))
    C = dict(zip(four_positions,[1,2,3,4]))
    example_outputs = []
    for labels in (A,B,C):
        o,i,t,path = slide(one_outer,one_inner,labels,(1,1))
        recovered,moved = reverse_one(t,tuple(path[-1]['from']),(1,1))
        assert recovered == labels
        example_outputs.append({'initial':sorted(labels.items()),'final':sorted(t.items()),'path':[(1,1)]+[m['from'] for m in path],'reverse_labels':moved})
    assert [x['path'] for x in example_outputs] == [[(1,1),(1,2),(2,2)],[(1,1),(2,1),(2,2)],[(1,1),(1,2),(1,3)]]
    assert [x['reverse_labels'] for x in example_outputs] == [[3,1],[4,1],[2,1]]
    all_four = []
    for labels in standard_fillings(one_outer-one_inner):
        o,i,t,path = slide(one_outer,one_inner,labels,(1,1))
        all_four.append({'position_order':[labels[p] for p in four_positions],'final':sorted(t.items())})
    assert len(all_four) == 5
    five_outer,five_inner = cells((3,3,2)),cells((2,1))
    five_positions = [(1,3),(2,2),(2,3),(3,1),(3,2)]
    D = dict(zip(five_positions,[2,1,4,3,5]))
    east = [(1,2),(2,1),(1,1)]
    south = [(2,1),(1,2),(1,1)]
    east_trace = traces(five_outer,five_inner,D,east)
    south_trace = traces(five_outer,five_inner,D,south)
    assert east_trace[-1]['labels']==south_trace[-1]['labels']
    assert [x['path'] for x in east_trace]==[[(1,2),(2,2),(2,3)],[(2,1),(3,1),(3,2)],[(1,1),(1,2),(1,3)]]
    assert [x['path'] for x in south_trace]==[[(2,1),(2,2),(2,3)],[(1,2),(1,3)],[(1,1),(2,1),(3,1),(3,2)]]
    p4_witnesses = []
    expected_outputs = [dict(zip([(1,1),(1,2),(1,3),(2,1),(2,2)],[1,2,5,3,4])),dict(zip([(1,1),(1,2),(1,3),(2,1),(3,1)],[1,4,5,2,3])),dict(zip([(1,1),(1,2),(2,1),(2,2),(3,1)],[1,3,2,5,4]))]
    for values,expected in zip(([2,1,5,3,4],[1,2,5,3,4],[1,2,3,4,5]),expected_outputs):
        labels = dict(zip(five_positions,values))
        valid(five_outer,five_inner,labels)
        outputs = rectifications(frozen(five_outer,five_inner,labels))
        assert outputs==frozenset((tuple(sorted(expected.items())),))
        p4_witnesses.append({'initial':sorted(labels.items()),'final':sorted(expected.items())})
    all_five = list(standard_fillings(five_outer-five_inner))
    assert len(all_five)==16
    five_catalog = []
    for labels in all_five:
        outputs = rectifications(frozen(five_outer,five_inner,labels))
        assert len(outputs)==1
        five_catalog.append({'initial':sorted(labels.items()),'final':list(next(iter(outputs)))})
    diagonal_outer = cells((3,2,1))
    diagonal_positions = [(1,3),(2,2),(3,1)]
    diagonal_catalog = []
    for triple in permutations([1,2,3]):
        labels = dict(zip(diagonal_positions,triple))
        valid(diagonal_outer,five_inner,labels)
        outputs = rectifications(frozen(diagonal_outer,five_inner,labels))
        assert len(outputs)==1
        diagonal_catalog.append({'triple':triple,'final':list(next(iter(outputs)))})
    expected_diagonal = [ {(1,1):1,(2,1):2,(3,1):3},{(1,1):1,(1,2):3,(2,1):2},{(1,1):1,(1,2):2,(2,1):3},{(1,1):1,(1,2):2,(2,1):3},{(1,1):1,(1,2):3,(2,1):2},{(1,1):1,(1,2):2,(1,3):3} ]
    assert [dict((tuple(p),v) for p,v in d['final']) for d in diagonal_catalog] == expected_diagonal
    visual_initial = {(1,2):2,(2,1):1,(2,2):3}
    _,_,visual_final,visual_path = slide(cells((2,2)),cells((1,)),visual_initial,(1,1))
    assert visual_final=={(1,1):1,(1,2):2,(2,1):3}
    restored,reverse_values=reverse_one(visual_final,(2,2),(1,1))
    assert restored==visual_initial and reverse_values==[3,1]
    badA,exitA=larger_slide(A,(1,1))
    badB,exitB=larger_slide(B,(1,1))
    assert badA == {(1,1):2,(1,2):1,(1,3):4,(2,1):3}
    assert badB == {(1,1):2,(1,2):4,(1,3):3,(2,1):1}
    mask_initial={(1,3):2,(2,2):1,(2,3):3}
    mask_o,mask_i,mask_t,mask_path = slide(cells((3,3)),cells((2,1)),mask_initial,(1,2))
    assert mask_o == cells((3,2)) and mask_i == cells((1,1))
    assert mask_t=={(1,2):1,(1,3):2,(2,2):3}
    assert corners(mask_i)==((2,1),)
    checked['90'] = {'non_task_visual':{'initial':sorted(visual_initial.items()),'final':sorted(visual_final.items()),'reverse_values':reverse_values},'P3_revised_mask_bridge':{'initial':sorted(mask_initial.items()),'final':sorted(mask_t.items()),'hole_path':[(1,2)]+[m['from'] for m in mask_path],'next_corner':corners(mask_i)},'P1_outputs_P7_reverse':example_outputs,'P2_all_five':all_four,'P3_east_first':east_trace,'P3_south_first':south_trace,'P4_witnesses':p4_witnesses,'P4_all_16':five_catalog,'P5_all_six':diagonal_catalog,'P6_bad_larger_A':sorted(badA.items()),'P6_bad_larger_B':sorted(badB.items())}
    (OUT/'draft-specific-results.json').write_text(json.dumps(checked,indent=2)+'\n')
    print('Weeks 88–90 all concrete checks passed; 30 cascade orders and all 5/16/6 tableau starts independently enumerated.')

if __name__ == '__main__':
    main()
