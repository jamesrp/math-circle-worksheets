+++
id = "w90.undo-rules"
kind = "setup"
title = "Undoing a slide: rules and an example"
grades = ["2-5"]
route = "return"
page = "new"
+++

## text
\node[anchor=north west,inner sep=0pt,text width=186mm,font=\fontsize{11}{13.97}\selectfont] at (15,27) {To undo one whole slide, save its starting square S and exit E. Uncover E and put the ring there. Slide in the larger numbered neighbor immediately above or left, or the only one. Move the ring back to the emptied square. Stop when it reaches S; replace the ring with gray.};
\fill[white] (18,70) rectangle ++(14,14);
\draw[line width=.45pt] (18,70) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (25.0,77.0) {1};
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (18.5,70.5) {S};
\fill[white] (32,70) rectangle ++(14,14);
\draw[line width=.45pt] (32,70) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (39.0,77.0) {2};
\fill[white] (18,84) rectangle ++(14,14);
\draw[line width=.45pt] (18,84) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (25.0,91.0) {3};
\fill[black!70] (32,84) rectangle ++(14,14);
\fill[pattern=crosshatch,pattern color=black!95] (32,84) rectangle ++(14,14);
\draw[line width=.45pt] (32,84) rectangle ++(14,14);
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (32.5,84.5) {E};
\draw[-{Stealth[length=2mm]},line width=.7pt] (49,83) -- ++(13,0);
\fill[white] (66,70) rectangle ++(14,14);
\draw[line width=.45pt] (66,70) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (73.0,77.0) {1};
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (66.5,70.5) {S};
\fill[white] (80,70) rectangle ++(14,14);
\draw[line width=.45pt] (80,70) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (87.0,77.0) {2};
\fill[white] (66,84) rectangle ++(14,14);
\draw[line width=.45pt] (66,84) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (73.0,91.0) {3};
\fill[white] (80,84) rectangle ++(14,14);
\draw[line width=.45pt] (80,84) rectangle ++(14,14);
\draw[line width=1.5pt] (87.0,91.0) circle (4.34);
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (80.5,84.5) {E};
\draw[-{Stealth[length=2mm]},line width=.7pt] (97,83) -- ++(13,0);
\fill[white] (114,70) rectangle ++(14,14);
\draw[line width=.45pt] (114,70) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (121.0,77.0) {1};
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (114.5,70.5) {S};
\fill[white] (128,70) rectangle ++(14,14);
\draw[line width=.45pt] (128,70) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (135.0,77.0) {2};
\fill[white] (114,84) rectangle ++(14,14);
\draw[line width=.45pt] (114,84) rectangle ++(14,14);
\draw[line width=1.5pt] (121.0,91.0) circle (4.34);
\fill[white] (128,84) rectangle ++(14,14);
\draw[line width=.45pt] (128,84) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (135.0,91.0) {3};
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (128.5,84.5) {E};
\draw[-{Stealth[length=2mm]},line width=.7pt] (145,83) -- ++(13,0);
\fill[black!12] (162,70) rectangle ++(14,14);
\fill[pattern=north east lines,pattern color=black!40] (162,70) rectangle ++(14,14);
\draw[line width=.45pt] (162,70) rectangle ++(14,14);
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (162.5,70.5) {S};
\fill[white] (176,70) rectangle ++(14,14);
\draw[line width=.45pt] (176,70) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (183.0,77.0) {2};
\fill[white] (162,84) rectangle ++(14,14);
\draw[line width=.45pt] (162,84) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (169.0,91.0) {1};
\fill[white] (176,84) rectangle ++(14,14);
\draw[line width=.45pt] (176,84) rectangle ++(14,14);
\node[font=\fontsize{13.16}{14}\selectfont] at (183.0,91.0) {3};
\node[fill=white,inner sep=.4pt,font=\fontsize{6}{6}\selectfont,anchor=north west] at (176.5,84.5) {E};
\node[anchor=north west,inner sep=0pt,text width=42mm,font=\fontsize{9}{11.43}\selectfont] at (18,103) {Finished slide};
\node[anchor=north west,inner sep=0pt,text width=42mm,font=\fontsize{9}{11.43}\selectfont] at (66,103) {Reopen E};
\node[anchor=north west,inner sep=0pt,text width=42mm,font=\fontsize{9}{11.43}\selectfont] at (114,103) {3 slides right};
\node[anchor=north west,inner sep=0pt,text width=40mm,font=\fontsize{9}{11.43}\selectfont] at (162,103) {1 moves down;\newline stop at S};
