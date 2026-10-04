from tri import *
H = region_from_poly(hexagon_poly(2,2,2))
us = sorted(c for c in H if c[0]=='U'); ds = sorted(c for c in H if c[0]=='D')
bad=[]; good=0
for u in us:
    for d in ds:
        rest = H - {u,d}
        m = max_matching(rest)
        if 2*len(m) != len(rest): bad.append((u,d))
        else: good+=1
print('1U1D tileable',good,'untileable',bad)
# boundary cells
be = boundary_edges(H)
bc = [c for c in H if any(e in be for e in edges(c))]
print('boundary cells', sorted(bc))
print('all', sorted(H))
