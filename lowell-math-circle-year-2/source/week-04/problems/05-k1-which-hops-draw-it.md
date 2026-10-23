+++
id = "w04.k1-which-hops-draw-it"
title = "Which hops draw each picture?"
grades = ["K-1"]
route = "return"
page = "new"
+++

## prompt
Find every hop from 1 to 5 that draws each picture. Write the hops under the picture.

## figure
parts(row([k1_picture_cell(5, 1), k1_picture_cell(5, 2), k1_picture_cell(6, 1)], before='0.3in'),
      row(["\\hspace{0.6in}", k1_picture_cell(6, 2), k1_picture_cell(6, 3), "\\hspace{0.6in}"], before='0.3in'),
      row([k1_trial_cell(5), k1_trial_cell(5), k1_trial_cell(6), k1_trial_cell(6)], before='0.45in'))
