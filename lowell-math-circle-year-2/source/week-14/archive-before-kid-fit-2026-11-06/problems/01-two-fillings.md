+++
id = "w14.two-fillings"
title = "Two fillings of each polygon"
grades = ["K-1", "2-3"]
route = "first"
page = "same"
kernel = "Every filling of a convex polygon with $n$ corners has $n-2$ triangles, however the lines are chosen."
+++

## prompt @1.78 [K-1]
Fill each shape with triangles in two different ways.

## prompt @1.78 [2-3]
Fill each polygon in two different ways. Can the two fillings of one polygon have different numbers of triangles?

## figure [K-1]
first_page_pair(5,6)

## figure [2-3]
first_page_pair(6,7,labels='letters')

## key [K-1]
Any two distinct legal fillings of each printed polygon suffice. For the pentagon, use $\{13,14\}$ and $\{24,25\}$. For the hexagon, use $\{13,14,15\}$ and $\{24,25,26\}$. Each pentagon has 3 triangles; each hexagon has 4.

## key [2-3]
Any two distinct legal fillings suffice. Hexagon examples: $\{AC,AD,AE\}$ and $\{BD,BE,BF\}$. Heptagon examples: $\{AC,AD,AE,AF\}$ and $\{BD,BE,BF,BG\}$. The counts cannot differ: every hexagon filling has 4 triangles and every heptagon filling has 5. Use page 3's splitting argument if children seek an explanation.

## hints [K-1]
If a child repeats the same picture, compare the endpoints of every line. A tracing turned around without changing corner names is still the same filling.

## hints [2-3]
Ask whether a thin or large triangle should still count as one. The task uses all triangles, regardless of size or shape.
