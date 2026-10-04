from tri import *
for abc in [(1,1,1),(2,1,1),(2,2,1),(2,2,2),(1,3,3),(3,1,1),(1,2,2)]:
    cells = region_from_poly(hexagon_poly(*abc))
    T = all_tilings(cells)
    print('H',abc, len(cells), counts(cells), 'tilings', len(T), 'bbox', [round(v,3) for v in bbox(cells)])
for n in range(1,7):
    cells = region_from_poly(triangle_poly(n))
    m = max_matching(cells)
    ch = chevrons(cells)
    pk = max_packing(cells, ch) if n<=5 else []
    print('T',n,len(cells),counts(cells),'max blue',len(m),'greens',len(cells)-2*len(m),'max purple',len(pk),'greens',len(cells)-4*len(pk))
