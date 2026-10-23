+++
id = "w24.k1-b-against-c"
title = "B against C, all nine pairs"
grades = ["K-1"]
route = "first"
kernel = "Of the nine card pairs, B wins five: (6,3), (6,5), (8,3), (8,5) and (8,7)."
+++

## prompt
Circle the winner in each pair. Which deck wins more pairs?

## figure
art(kdeck('B',[1,6,8],7.9), kdeck('C',[3,5,7],6.45), shared_pairs('B',[1,6,8],'C',[3,5,7]))
