+++
id = "w24.k1-a-against-b"
title = "A against B, all nine pairs"
grades = ["K-1"]
route = "first"
page = "same"
kernel = "Of the nine equally likely card pairs, A wins five: (2,1), (4,1), (9,1), (9,6) and (9,8)."
+++

## prompt @9.02
For each of Problems 1--3, split the pairs among you and circle all nine winners on one shared page. Which deck wins more pairs?

## figure
art(kdeck('A',[2,4,9],7.3), kdeck('B',[1,6,8],5.85), shared_pairs('A',[2,4,9],'B',[1,6,8]))
