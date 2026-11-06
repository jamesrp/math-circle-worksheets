+++
id = "w16.rows"
title = "Doors along a row of dots"
grades = ["2-3", "4-5"]
route = "return"
page = "new"
kernel = "A row from R to B has an odd number of doors and a row from R to R an even number, whatever its length."
+++

## prompt [2-3]
Write R or B on every empty dot and mark the doors. Can any row have an even number of doors? Explain why or why not.

## prompt [4-5]
Write R or B on every empty dot and mark the doors. Which numbers of doors can each row have? Explain your answer for rows of any length.

## figure [2-3]
chains(['RB']*5,[2,3,4,5,6])

## figure [4-5]
chains(['RB','RR','RB','RR','RB'],[3,4,5,6,7])
