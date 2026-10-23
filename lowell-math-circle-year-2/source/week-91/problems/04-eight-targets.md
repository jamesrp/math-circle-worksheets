+++
id = "w91.eight-targets"
title = "Eight-exit tree: which orders?"
grades = ["2-5"]
route = "return"
kernel = "Every switch alternates, so AECGBFDH (all L) and HDFBGCEA (all R) can be made but AEBFCGDH cannot: the left subtree gets A, B first."
+++

## figure
head('Grades 4--5')

## prompt @15,31
Use the eight-exit tree. Choose starting arrows to make each order. Which orders can the machine make?

## figure
eight_targets(['A E C G B F D H','H D F B G C E A','A E B F C G D H'], label_dy=10)
