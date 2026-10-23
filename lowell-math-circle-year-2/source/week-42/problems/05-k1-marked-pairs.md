+++
id = "w42.k1-marked-pairs"
title = "Count the shapes on the sixteen marked pairs"
grades = ["K-1"]
route = "first"
kernel = "Of the 16 equally likely marked pairs, 3 are RB and 3 are BR, 9 are RR and 1 is BB; only RB against BR splits evenly."
+++

## text @0 size=12
The red counters have marks R1, R2, R3. Each marked pair below has the same chance.

## prompt @1.5 size=13
Does your rule give each shape to the same number of pictures? Find every rule that does and sometimes gives each shape.

## figure
k1_marked_pairs()

## key
RR has nine marked pictures; RB and BR have three each; BB has one. The two fair rules are exactly: (i) BR square, RB circle, RR/BB no shape; (ii) BR circle, RB square, RR/BB no shape. To see completeness, a shape receiving all nine RR pictures cannot be balanced by the seven other pictures, so RR is skipped. Among the remaining classes, BB cannot be balanced without breaking a three-picture class. Thus BB is skipped and RB/BR must go to different shapes. Adult-supported matching is enough; a written exhaustion is not required.
