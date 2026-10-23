+++
id = "w04.m-more-rings-guess"
title = "Guess, then draw: four more rings"
grades = ["2-3"]
route = "return"
page = "new"
+++

## prompt
Before you draw each of these, guess how many times you will start and write your guess. Then draw it and write how many times you did start.

## figure
grid([ring_cell(n, 1.25, [f"{n} dots, hop {k}", "guess~\\bx\\quad started~\\bx"], 3.6) for n, k in [(9, 2), (15, 5), (16, 6), (12, 8)]], 2, 3.6, before='0.3in', between='0.45in')
