+++
id = "w92.fill-the-track"
title = "Moves until a band fills the track"
grades = ["shared"]
route = "first"
kernel = '$[1,2]$ and the wider $[7,9]$ both first fill the whole track on move 4: location matters as well as width.'
+++

## figure
band('Grades 2--3')

## prompt @0
Start with each band below. Move the whole band until every place on the track is possible. How many moves does each need?

## figure
r'''\track{-24}{Start}\range{-24}{1}{2}
\track{-38}{After 1 move}\track{-52}{After 2 moves}\track{-66}{After 3 moves}\track{-80}{After 4 moves}\track{-94}{After 5 moves}\track{-108}{After 6 moves}
\track{-128}{Start}\range{-128}{7}{9}
\track{-142}{After 1 move}\track{-156}{After 2 moves}\track{-170}{After 3 moves}\track{-184}{After 4 moves}\track{-198}{After 5 moves}\track{-212}{After 6 moves}'''
