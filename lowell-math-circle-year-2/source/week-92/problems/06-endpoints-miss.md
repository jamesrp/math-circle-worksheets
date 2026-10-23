+++
id = "w92.endpoints-miss"
title = "Moving only the ends"
grades = ["shared"]
route = "first"
page = "same"
kernel = 'Endpoint images miss the turn at 8: $[6,10]$ goes to $[12,16]$, not to 12 alone.'
+++

## prompt @-13
A child moves just the ends of the band from 6 to 10. Both ends land at 12. Is 12 the only possible next place? Shade the whole output band. Find two more starting bands for which shading only between the two endpoint outputs misses possible places.

## figure
r'''\track{-51}{Start}\range{-51}{6}{10}\track{-70}{After one move}
\track{-94}{Start}\track{-113}{After one move}
\track{-137}{Start}\track{-156}{After one move}'''
