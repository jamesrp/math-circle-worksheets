+++
id = "w10.find-a-walk"
title = "Find a walk in each town"
grades = ["2-3", "4-5"]
route = "first"
+++

## prompt [2-3]
In each town, find a walk that picks up every counter, and write its islands in order,
like A~B~C~A.

## prompt [4-5]
In each town, find a walk that crosses every bridge exactly once, and write its islands
in order.

## figure [2-3]
figs([[town(1, house('m1a'), line=7.5), town(1, rotate(lollipop('m1b'), 90), line=7.5)]],
     [[town(1, row_doubles('m1c'), line=9.0)]], align='bottom')

## figure [4-5]
figs([[town(1, house('u1a'), line=7.5), town(1, rotate(lollipop('u1b'), 90), line=7.5)]],
     [[town(1, row_doubles('u1c'))]], align='bottom')
