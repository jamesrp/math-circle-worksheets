+++
id = "w24.k1-c-against-a"
title = "C against A, and the cycle"
grades = ["K-1"]
route = "first"
kernel = "C wins five of nine pairs against A, so A beats B, B beats C and C beats A: no deck beats both others."
+++

## prompt
Does any of A, B, and C win more pairs than both other decks?

## figure
art(kdeck('C',[3,5,7],7.9), kdeck('A',[2,4,9],6.45), shared_pairs('C',[3,5,7],'A',[2,4,9]))
