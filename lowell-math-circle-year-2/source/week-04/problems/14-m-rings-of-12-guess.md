+++
id = "w04.m-rings-of-12-guess"
title = "Guess, then draw: rings of 12"
grades = ["2-3"]
route = "first"
page = "new"
+++

## prompt
Before you draw each hop on these rings of 12 dots, guess how many times you will start and write your guess. Then draw it and write how many times you did start.

## figure
grid([ring_cell(12, 1.0, [f"hop {k}", "guess~\\bx\\quad started~\\bx"], 2.42) for k in range(2, 7)], 3, 2.42, before='0.3in', between='0.45in')
