# Week 73: mathematical verification

## 73. The gentlest stretch — PASS under named-side constraint

Let `R=[0,4]x[0,1]` and `Q=[0,2]x[0,2]` with Euclidean distance. The permitted maps are homeomorphisms carrying each named side to the corresponding named side. Choose points `(x,0),(x,1)` on the two horizontal boundaries. They are distance 1 apart. Their images are on opposite horizontal square boundaries, so are at least distance 2 apart. Every legal map therefore has worst pairwise stretch at least 2. A non-Lipschitz map has infinite worst stretch and does not evade the bound.

The map `F(x,y)=(x/2,2y)` is a legal homeomorphism. For every displacement `(u,v)`, its squared image length is `u^2/4+4v^2 <= 4(u^2+v^2)`. Thus its worst stretch is at most 2; vertical pairs attain 2. The optimum is exactly 2.

Pin or ruler tests over finitely many pairs establish only a lower bound on a chosen map's all-pairs maximum. A general proposed map needs a whole-sheet rule before an upper bound can be proved. This is a one-sided Lipschitz optimization; do not call the number 2 a Teichmüller distance or confuse it with a logarithmic or quasiconformal normalization. Side correspondence is an essential hypothesis.

Independent checks verify the squared bound on 351 exact sampled pairs. The universal proof is the inequality and boundary argument above. The particular elementary optimization is authored here, not attributed to the 2005 talk.


### Exact fan-map extension in the Week 73 draft

The old center is `(2,1/2)` in the 4-by-1 rectangle; its new location is `O'=(u,v)` strictly inside the 2-by-2 square. Map each center-to-side triangle affinely to its corresponding triangle. The four maps agree along shared edges. Both sets of four nondegenerate triangles partition their rectangles, so the glued map is a side-preserving homeomorphism. Putting O on the boundary would invalidate this argument; the draft now explicitly excludes edges.

All ten original five-pin pairs have stretch at most2, whatever the interior location of O'. The old vertical corner pairs attain2. Each old center-to-corner distance is `sqrt(17)/2`, while any new center-to-corner distance is at most `sqrt(8)`, giving ratio less than2. Horizontal and diagonal corner pairs also give smaller ratios. Thus the initial five-pin score is exactly2 everywhere, and genuinely cannot distinguish the good map from bad ones.

Let M,N be the midpoints of the bottom and top sides. Their old distances to O are both1/2, and their images are `(1,0),(1,2)`. Passing the two additional O–M and O–N tests requires `|(u,v)−(1,0)|<=1` and `|(u,v)−(1,2)|<=1`. The two closed unit disks are tangent only at `(1,1)`, so every off-center fan fails one of these tests. Equivalently, adding the two squared inequalities yields `(u−1)^2+(v−1)^2<=0`. The centered fan is the globally optimal linear map already proved above.

For a general target rectangle of width W and height H, the same opposite-side argument gives lower bound `max(W/4,H)`; the diagonal linear map attains it. Thus the draft's 6-by-2 and2-by-3 targets have optimum2 and3. Exactly1.5 is attained when positive W,H satisfy `W<=6`, `H<=1.5`, and at least one equality holds. For instance6-by-1 and3-by-1.5 work.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
