+++
id = "w43.six-shuffles"
title = "Must six shuffles show all six rows?"
grades = ["2-3"]
route = "return"
page = "same"
kernel = 'Equal chances do not make a short run representative: six fair shuffles show all six rows with probability $6!/6^6 = 5/324$, about 1.5\%.'
+++

## prompt @16.2
Shuffle six times with the two-swap rule. A friend says six shuffles must show all six rows once. Is the friend right?

## figure
six_shuffle_records()

## key
No. Six shuffles have $6^6 = 46{,}656$ equally likely lists of ticket stories, and only $6! = 720$ of them show all six rows once, about 1 run in 65. Six repeats of (1,2), giving ABC six times, is one legal run. Uniform probability does not force a perfectly representative batch of six results.
