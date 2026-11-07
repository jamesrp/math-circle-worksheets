+++
id = "w24.k1-three-games"
title = "Play A against B, B against C and C against A"
grades = ["K-1"]
route = "first"
page = "same"
kernel = "Each game is a short random experiment: in each matchup the deck with five of nine winning pairs wins a round with chance 5/9, so six rounds often, but not always, favour it, and no deck is ahead in both of its games."
+++

## prompt @7.72
With a partner, play three games: A against B, B against C, and C against A. Play six rounds in each game, and put a counter in the winning deck's row each round. Is one deck better than both of the others?

## figure
art(kdecks_row(8.0), ktracks([('A','B'),('B','C'),('C','A')],6.4,1.95,.72))
