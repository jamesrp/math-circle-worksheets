+++
id = "w18.rules"
kind = "setup"
title = "The folder game and a practice row"
grades = ["K-1", "2-3", "4-5"]
route = ["first", "return"]
+++

## text @0,.45 w=18.4 size=14 [K-1]
Keep the arrow at the left. The sender hides a picture and its row. The changer turns over zero or one counter in secret. Only the final row crosses the folder; the receiver uses the key to find the picture.

## text @0,.45 w=18.4 size=14 [2-3]
Keep the arrow at the left. A key gives each picture a different row, all the same length. The sender hides the picture and its row. A changer secretly turns over zero or one counter. Only the final row crosses the folder. The receiver knows the key.

## text @0,.45 w=18.4 size=14 [4-5]
Use 0 for an empty circle and 1 for a filled circle. A key gives a different row to each picture, all the same length. The sender hides the picture and its row. A changer changes zero or one entry, without saying where or whether a change occurred. The receiver gets only the final row and knows the key. Keep the arrow at the left.

## figure [K-1, 2-3]
say(.5,3.4,18,'Example: a practice row',15,19)+example('circle')+say(11.9,14.2,6.7,'The receiver sees only this row.',14,18)

## figure [4-5]
say(.5,3.4,18,'Example: a practice row',15,19)+example('number')+say(11.9,14.2,6.7,'The receiver sees only this row.',14,18)

## text @.5,17.2 w=17.5 size=14
In the game, the start row and the changed position stay hidden behind the folder.

## figure
say(.5,19.6,17.5,'The changer may also leave the row as it is.',14,18)
