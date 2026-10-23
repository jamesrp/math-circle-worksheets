+++
id = "w27.k1-fill-one-strip"
title = "Fill the empty strip"
grades = ["K-1"]
route = "return"
kernel = "Top: Y must rank A first for both pairings to stay. Bottom: impossible, because B and X block AX / BY whatever Y says."
+++

## prompt @0.91
Fill each empty strip so both drawn pairings can stay. If it cannot be done, cross out the empty strip.

## figure
kcase(2.0,get('k_two_stable')[0],{**get('k_two_stable')[1],'Y':['','']})+ln(.6,5.99,7.9,5.99)
+ kcase(6.3,{'A':['X','Y'],'B':['X','Y']},{'X':['B','A'],'Y':['','']})
