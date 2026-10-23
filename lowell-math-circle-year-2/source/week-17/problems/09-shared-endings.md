+++
id = "w17.shared-endings"
title = "Can the same added cards separate two rows?"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "first", "4-5" = "first" }
kernel = "Two rows that leave a machine on the same circle can never be separated by a shared ending; rows separated in this way need different circles."
+++

## prompt size=17 [K-1]
For each pair, can you add the same cards in the same order after both printed rows to get \Y\ and \N? Adding no cards is allowed.

## prompt size=14.5 [2-3]
A row gets YES exactly when its red cards can be put in groups of three with none left over, including no red cards. For each pair, add the same extra cards in the same order to both rows to give one YES and one NO, or explain why this cannot be done. Adding no cards is allowed.

## prompt size=14.5 [4-5]
A row gets YES exactly when its red cards can be grouped in threes with none left over, including no red cards. For each pair, add the same extra cards in the same order to both rows to give one YES and one NO, or explain why this cannot be done. Adding no cards is allowed.

## figure [K-1]
three(2.88,True)+pairs([('','R',4.65),('R','RR',5.98),('RR','RBR',7.31),('B','RRR',8.64)],True)

## figure [2-3]
pairs([('','R',2.6),('R','RR',3.88),('RR','RRR',5.16),('RBR','RR',6.44),('B','RRR',7.72),('RB','BR',9.0)])

## figure [4-5]
pairs([('','R',2.6),('R','RR',3.9),('RR','BRR',5.2),('BBB','RRR',6.5)])
