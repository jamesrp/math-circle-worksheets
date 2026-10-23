# Week 75: mathematical verification

## 75. Twists on a cylinder — PASS, relative endpoints essential

Write the annulus as `(R/Z)x[0,1]`. For integer `n`, `T_n(theta,t)=(theta+n*t,t)` is a homeomorphism with inverse `T_-n`. It fixes both boundary circles **pointwise**, because adding `n` at the upper boundary is zero modulo 1. Composing maps gives `T_a T_b=T_(a+b)`.

A joining arc is proper and simple: its endpoints are on the two different rims and its interior remains in the open annulus. Fix the same endpoint on each rim for both arcs. A lift starting at `(0,0)` ends at `(a,1)` for an integer winding `a`. Isotopies keep the endpoints fixed. Reversing a twist subtracts winding; freely rotating a marked rim would change this problem.

The minimum number of **interior** intersections of arcs of winding `a,b` is `max(|a−b|−1,0)`. Upper bound: straight lifts `(a*t,t)` and `(b*t,t)` intersect after projection when `(a−b)t` is integral. For `a!=b` and `0<t<1`, this happens exactly `|a−b|−1` times. When the windings agree, move one representative a small amount sideways, vanishing at the endpoints, to make their interiors disjoint.

For the lower bound, straighten one arc to winding zero by a boundary-fixing annular homeomorphism (cut along that proper simple arc to obtain a disk/rectangle, then reglue). Its lifts are the vertical barriers at all integer horizontal coordinates. The other lifted arc joins `(0,0)` to `(d,1)`, where `d=b−a`. Its horizontal coordinate must attain every integer strictly between 0 and `d`. At each such time it crosses a lift of the first arc. Its simplicity ensures the resulting projected interior intersection points are distinct. Therefore at least `|d|−1` intersections are necessary when `|d|>=2`; the other cases have lower bound zero.

This is a minimum over representatives, not the number of crossings in an arbitrary drawing. Shared endpoints are excluded; overlapped strands are not a transverse minimal-position drawing. Changing either endpoint changes the count. The strands stay on the surface: lifting yarn into three-dimensional space to pass over another strand is outside the model. A rigid paper cylinder is a strand-routing model, not a literal deforming Dehn twist.

Independent checks enumerate straight-representative crossings for winding pairs from −8 to8 and check twist composition and boundary fixing with rational angles/heights. Davis Problem 111 supplies related torus shear imagery; the annular fixed-endpoint formula is an independently proved extension, not a quoted result there.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
