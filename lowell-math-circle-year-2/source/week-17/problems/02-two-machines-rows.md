+++
id = "w17.two-machines-rows"
title = "Rows that make exactly one of two machines say yes"
grades = ["2-3"]
route = "first"
page = "same"
kernel = "A four-card row has an even number of reds or ends in red, but not both, in exactly 8 of 16 rows."
+++

## prompt @1.86 size=14.5
Find every four-card row that makes exactly one of these machines say YES. Start both machines fresh for each row, and write each row once.

## figure
two('even',1.75,3.25,3.7,False,'a',labels=True)+two('lastR',5.35,6.85,3.7,False,'b')

## text @.8,4.48 w=6.9 size=11.5
Left machine, input B R: start 1 $\xrightarrow{\ B\ }$ 1 $\xrightarrow{\ R\ }$ 2; stop: NO.

## figure
''.join(line(x,y,2.6) for y in [5.2,6.03,6.86,7.69,8.52,9.35] for x in [.95,4.75])
