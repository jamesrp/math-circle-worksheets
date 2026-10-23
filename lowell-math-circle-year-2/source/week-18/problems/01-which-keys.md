+++
id = "w18.which-keys"
title = "Which keys always let the receiver find the picture?"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "Rows that differ in all three places (000 and 111) survive one hidden change; rows that differ in one place (001, 101), or two-place rows, do not."
+++

## prompt [K-1]
Send both pictures with this key many times. Can the changer fool the receiver?

## prompt [2-3]
Use each key to send both pictures several times. Which keys always let the receiver tell which picture was sent?

## prompt [4-5]
For each key, find every row the receiver might see. Mark any row that could mean either picture. Which keys always let the receiver recover the picture?

## figure [K-1]
keyed(.35,3.15,'triangle','000')+keyed(9.7,3.15,'square','111')+''.join(strip(1.1,y,'---')+strip(10.45,y,'---') for y in [7.25,11.35,15.45])

## figure [2-3]
''.join(keyed(x,2.95,'triangle',a,2,small=True)+keyed(x,5.6,'square',b,2,small=True) for x,a,b in [(.8,'000','111'),(10,'001','101')])+''.join(strip(1.8,y,'---',2)+strip(11,y,'---',2) for y in [8.8,12.4,16.0])

## figure [4-5]
''.join(keyed(.45,y,'triangle',a,.85,.95,'number')+keyed(9.7,y,'square',b,.85,.95,'number') for y,a,b in [(3.35,'00','11'),(9.05,'000','111'),(14.75,'0010','0100')])
