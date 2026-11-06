+++
id = "w24.k1-a-against-b"
title = "A against B, all nine pairs"
grades = ["K-1"]
route = "first"
kernel = "Of the nine equally likely card pairs, A wins five: (2,1), (4,1), (9,1), (9,6) and (9,8)."
+++

## prompt
Circle the winner in each pair. Which deck wins more pairs?

## figure
art(kdeck('A',[2,4,9],7.9), kdeck('B',[1,6,8],6.45), shared_pairs('A',[2,4,9],'B',[1,6,8]))
