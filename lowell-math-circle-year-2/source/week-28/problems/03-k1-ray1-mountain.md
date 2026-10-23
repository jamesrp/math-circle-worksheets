+++
id = "w28.k1-ray1-mountain"
title = "Every fold with ray 1 a mountain"
grades = ["K-1"]
route = "return"
kernel = "Fixing one label splits the eight right-angle folds into cases: ray 1 is the odd one out, or one of the other rays is."
+++

## prompt
Ray 1 must be a mountain. Find every flat fold with that label.

## figure
k1_ray1_mountain()

## key
\textbf{All four answers:} MMMV, MMVM, MVMM, MVVV. If M is the majority, its single V can occupy ray 2,3 or 4. If M is the minority, ray 1 is the only M. Those cases exhaust the catalog while keeping ray 1 fixed.
