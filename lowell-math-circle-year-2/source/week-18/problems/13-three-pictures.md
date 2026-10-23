+++
id = "w18.three-pictures"
title = "Can three pictures share a short key?"
grades = ["K-1", "4-5"]
route = "return"
kernel = "Three pictures fit neither three counters nor four: three rows cannot differ pairwise in three places when each position adds at most two to the three distances."
+++

## prompt [K-1]
Can three pictures share a three-counter key that always works? Make one, or show why it cannot be done.

## prompt [4-5]
Can three pictures have a key that always works with four entries in each row? Find one, or explain why every choice fails.

## figure [K-1]
''.join(keyed(x,y,s,'---') for x in [.35,9.7] for y,s in zip([4,8.2,12.4],['triangle','square','star']))

## figure [4-5]
''.join(keyed(1.5,y,s,'----',1.3,1.1,'number') for y,s in zip([3.4,5.9,8.4],['triangle','square','star']))
