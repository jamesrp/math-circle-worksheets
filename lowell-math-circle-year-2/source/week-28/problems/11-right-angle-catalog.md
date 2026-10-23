+++
id = "w28.right-angle-catalog"
title = "Every flat labeling of the four-right-angle disk"
grades = ["K-1", "2-3", "4-5"]
route = "return"
kernel = "The four-right-angle disk has exactly eight flat labelings: one exceptional ray in any of four positions, labelled M or V."
+++

## prompt [K-1]
Find every flat fold of the four-ray disk. Keep ray 1 at the top and mark every ray M or V.

## prompt [2-3]
Find every mountain/valley labeling of the four-right-angle disk that can close flat. Keep ray 1 at the top and make each fold on your disk.

## prompt [4-5]
Find as many mountain/valley labelings of the four-right-angle disk that can close flat as you can.

## figure [4-5]
labelings_45()

## figure
ten_small_disks()

## key
\textbf{Full possible list:} MMMV, MMVM, MVMM, VMMM, MVVV, VMVV, VVMV, VVVM.

## key [K-1]
Organize them by the exceptional ray and by whether its label is M or V: four positions times two types. The necessity proof is on page 6 and the construction is on page 3.

## key [2-3]
Keep ray 1 at the top; rotations count as new only when the numbered-ray labels change. A full justification has two parts: all listed words work by construction, and all others are ruled out by page 6.

## key [4-5]
The page asks for as many as children can find; each fold is its own witness. It does not yet require them to know the list is complete. For each state, use the two-book-fold construction, rotate the exceptional ray, and if needed reverse all folds.
