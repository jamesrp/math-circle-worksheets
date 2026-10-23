+++
id = "w32.g45-most-sizes"
title = "The most different square sizes"
grades = ["4-5"]
route = "return"
kernel = "Each new square size is one division step, so consecutive Fibonacci numbers give the most: 13 by 8 has five sizes, more than any other choice."
+++

## prompt @0
Choose a longer side from 9 through 15 and a shorter side from 2 through 8. Which rectangle produces the most different square sizes under the biggest-square rule? Does any other rectangle tie with it? How do you know?

## figure
workgrid(1,3.5,15,8)+workgrid(1,14.5,15,8)
