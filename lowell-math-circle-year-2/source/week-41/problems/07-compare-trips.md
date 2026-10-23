+++
id = "w41.compare-trips"
title = "Same place, same copy?"
grades = ["2-3"]
route = "return"
kernel = "RRRUUU and RURURU finish at H in the same copy, (1,1)."
+++

## prompt @27
Compare these two trips from H. Do they finish at the same place on the portal map and in the same copy on the repeated map?

## figure
arrtrip(20,64,81,'RRRUUU',13)+arrtrip(116,64,81,'RURURU',13)+tiled(20,88,25)+tiled(116,88,25)+blank(16,185,180,69)

## key
Both RRRUUU and RURURU finish at H on the portal map and in copy (1,1) on the repeated map. Their drawn paths differ, but both have three right and three up steps. This question asks for endpoint comparison, not yet a full deformation proof.
