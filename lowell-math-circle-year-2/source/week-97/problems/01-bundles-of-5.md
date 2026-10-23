+++
id = "w97.bundles-of-5"
title = "Bundles of 5: which inputs share an output?"
grades = ["3-5"]
route = "first"
kernel = "For bundles of 5, inputs 1 and 4 share output 1 and inputs 2 and 3 share output 4; outputs 2 and 3 never occur."
+++

## prompt
Build squares with inputs 0, 1, 2, 3 and 4. Use bundles of 5. Find every pair of different inputs that leaves the same output. Which outputs from 0 to 4 cannot occur?

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\foreach \n in {0,1,2,3,4}{
\pgfmathsetmacro{\left}{3.55*\n}
\draw[gray!50,rounded corners=3pt] (\left,0) rectangle +(3.15,2.8);
\node at(\left+1.575,2.4){\small Input \n};
\ifnum\n=0 \node at(\left+1.575,1.1){\small 0 counters};\else
\foreach \x in {1,...,\n}\foreach \y in {1,...,\n}{\dotat{\left+1.575+(\x-(\n+1)/2)*0.4}{1.1+(\y-(\n+1)/2)*0.4}}\fi
}
\end{tikzpicture}
\end{center}
\blank{6.0}
