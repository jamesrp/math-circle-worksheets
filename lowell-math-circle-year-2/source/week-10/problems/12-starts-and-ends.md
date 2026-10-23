+++
id = "w10.starts-and-ends"
title = "Where walks start and end"
grades = ["2-3", "4-5"]
route = "first"
+++

## prompt [2-3]
In each town, find every island where a walk that picks up every counter can start,
and where such a walk can end. If a town has no such walk, write ``none''.

## prompt [4-5]
In each town, find every island where a walk that crosses every bridge exactly once can
start, and where such a walk can end. If a town has no such walk, write ``none''.

## figure [2-3]
figs([[town(2, fan('m2a', with_cd=False))]], [[town(2, fan('m2b'))]],
     [[town(2, m_ladder('m2c'))]], [[town(2, flower('m2d'))]])

## figure [4-5]
figs([[town(2, fan('u2a', with_cd=False))]], [[town(2, fan('u2b'))]],
     [[town(2, m_ladder('u2c'))]], [[town(2, flower('u2d'))]])
