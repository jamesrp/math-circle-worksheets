+++
id = "w92.fill-the-track"
title = "Moves until a band fills the track"
grades = ["shared"]
route = "first"
kernel = '$[1,2]$ and the wider $[7,9]$ both first fill the whole track on move 4: location matters as well as width.'
+++

## prompt @0
Start with each band below. Move the whole band until every place on the track is possible. How many moves does each need?

## figure
r'''\track{-32}{Start}\range{-32}{1}{2}
\track{-51}{After 1 move}\track{-70}{After 2 moves}\track{-89}{After 3 moves}\track{-108}{After 4 moves}
\track{-139}{Start}\range{-139}{7}{9}
\track{-158}{After 1 move}\track{-177}{After 2 moves}\track{-196}{After 3 moves}\track{-215}{After 4 moves}'''
