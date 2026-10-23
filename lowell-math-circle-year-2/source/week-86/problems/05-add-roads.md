+++
id = "w86.add-roads"
title = "Fewest added roads so C wins"
grades = ["4-5"]
route = "return"
kernel = "One diagonal makes the square cop-win; the pentagon needs two chords, and one chord still leaves R a square to run on."
+++

## prompt
Add as few roads as possible to each ring so C can always catch R. A road joins two existing dots. A crossing is not a new dot. Show a winning cop plan for each changed map.

## figure
graph(*cycle(4, 36), 96, 82, label='E4') + graph(*cycle(5, 36), 96, 185, label='E5') + lines(238, 1)

## key
The square needs exactly one diagonal. With none, the previous escape strategy works; either diagonal makes its endpoint adjacent to every dot, so C starts there and catches on move one.

The pentagon needs two chords. Chords a--c and a--d make a adjacent to every other dot, so two suffice. Zero fails by the ring strategy. To show one fails, any one-chord pentagon can be relabeled with chord a--c. Keep R on the square a--c--d--e--a. Project a cop at b to a, leaving other cop positions unchanged. Every actual cop move projects to a legal square move or stay, since b's neighbors a,c both map next to a. R uses its square escape strategy against that projected cop. Actual capture would imply projected capture, which never occurs. This is a graph-map proof, not just the report of several games. Children may test all five single-chord choices together before an adult offers this explanation.

A different pair of chords is acceptable if its claimed strategy is valid; the question asks a minimum, not every minimum pair. Two chords work only if they share an endpoint. Two crossing chords such as a--c and b--d still lose: b and c then reach the same places, and folding b leaves the square a--c--d--e. Adding roads can help a cop by removing hiding places, or help an escapee by creating a way around a former barrier. The number of roads alone does not decide the outcome.
