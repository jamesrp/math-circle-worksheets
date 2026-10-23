+++
id = "w88.equal-ring"
title = "Biggest ring of 40 mm disks around a 40 mm disk"
grades = ["K-5"]
route = "first"
kernel = "Six equal disks fit around an equal middle disk, each touching it; a seventh never fits."
+++

## prompt
Use the 40 mm disks. How many can touch one middle disk at once? Make the biggest ring you can.

## text
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
\path[use as bounding box] (-75,-67) rectangle (75,67);
\draw[thick,fill=black!6] (0,0) circle (20);
\fill (0,0) circle (.6);

\end{tikzpicture}
\end{center}
\vfill
Most outside disks in our ring: \rule{25mm}{.3pt}
