+++
id = "w18.which-keys"
title = "Which keys always let the receiver find the picture?"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "Rows that differ in all three places (000 and 111) survive one hidden change; rows that differ in one place (001, 101), or two-place rows, do not."
+++

## prompt @3.45 [K-1]
Send both pictures with this key many times. Can the changer fool the receiver?

## prompt @3.85 [2-3]
Use each key to send both pictures several times. Which keys always let the receiver tell which picture was sent?

## prompt @4.1 [4-5]
For each key, find every row the receiver might see. Mark any row that could mean either picture. Which keys always let the receiver recover the picture?

## figure [K-1]
keyed(.35,6.15,'triangle','000')+keyed(9.7,6.15,'square','111')+''.join(strip(1.1,y,'---')+strip(10.45,y,'---') for y in [10.25,14.35,18.45])

## figure [2-3]
''.join(keyed(x,6.35,'triangle',a,2,small=True)+keyed(x,9.0,'square',b,2,small=True) for x,a,b in [(.8,'000','111'),(10,'001','101')])+''.join(strip(1.8,y,'---',2)+strip(11,y,'---',2) for y in [12.2,15.8,19.4])

## figure [4-5]
''.join(keyed(.45,y,'triangle',a,.85,.95,'number')+keyed(9.7,y,'square',b,.85,.95,'number') for y,a,b in [(7,'00','11'),(12.7,'000','111'),(18.4,'0010','0100')])
