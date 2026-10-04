#!/usr/bin/env python3
from pathlib import Path
import importlib.util,subprocess,sys
spec=importlib.util.spec_from_file_location('gc',Path(__file__).with_name('guide_content.py'));mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
ROOT=Path(__file__).resolve().parents[2]
PREAMBLE=r'''\documentclass[11pt]{article}
\usepackage[letterpaper,margin=.68in,headheight=16pt,headsep=.18in,footskip=.28in]{geometry}
\usepackage{amsmath,array,enumitem,fancyhdr,hyperref}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{.3pt}
\fancyhead[L]{\small Bellingham Math Circle / Week WEEK / Return visits}
\fancyhead[R]{\small Adult guide}
\fancyfoot[L]{\small RV-WEEK-FAC-v1 / Draft and unpiloted}\fancyfoot[R]{\small\thepage}
\setlength{\emergencystretch}{2em}
\setlength{\parindent}{0pt}\setlength{\parskip}{7pt}
\setlist[itemize]{leftmargin=1.3em,itemsep=3pt,topsep=4pt}
\hypersetup{hidelinks,pdftitle={Week WEEK return-visit facilitator guide}}
\begin{document}
'''
for n in [int(x)for x in sys.argv[1:]] or range(11,18):
 g=mod.GUIDES[n];dest=ROOT/f'tmp/encore-11-17/guide-drafts/week-{n:02}'
 dest.mkdir(parents=True,exist_ok=True)
 text=PREAMBLE.replace('WEEK',str(n))
 text+=r'{\Large\bfseries Mathematical overview}\par\medskip'+'\n'+g['overview']
 text+='\n'+r'\newpage {\Large\bfseries Prepare a return visit}\par\medskip'+'\n'
 text+=r'\textbf{Status and use.} Three investigations extend one familiar theme. These companions are separate from the base packets and may support several visits. All pages are new and unpiloted. Printed labels describe prerequisites, not age restrictions. Offer one investigation’s pages at a time; completing every page is not the goal.'+'\n\n'
 text+=r'\textbf{Materials and preparation.} '+g['materials']+'\n\n'
 text+=r'\textbf{Staffing.} Current context: eleven children, fixed KK11 / 3333 / 445 tables, one adult anchored to each table. Use pairs; the upper third child rotates as reader or checker. Routine adult reading, arrow drawing or recording can leave the mathematical decisions with children. If adults must choose every move, use the earlier entry rather than run the investigation for them.'+'\n\n'
 text+=r'\textbf{Short common launch.} '+g['launch']+'\n\n'
 text+=r'\textbf{Suggested first route.} '+g['route']+'\n\n'
 text+=r'\textbf{Flexible timing.} Allow 3--5 minutes of material play and 2--4 minutes for the common demonstration, then 15--25 minutes for one investigation and 5 minutes to share. A longer second visit can spend 30--45 minutes on the same investigation, including unfinished examples or its explanation. These are planning estimates, not observed timings. Do not require all three within one hour.'+'\n\n'
 text+=r"\textbf{Questions and hints.} Start with ``What can you try?'' and ``What would count as success?'' Check the actual rule before giving a strategy. Optional questions and hints are keyed below; use them only after a real attempt. A counter argument or drawing may be a complete explanation."+'\n\n'
 text+=r'\textbf{Source and pilot record.} Mathematical examples and arguments here are original local follow-ups to the current base theme. Consulted teaching source: \emph{Math Circle by the Bay}, Preface pp. vii--x (local PDF pp. 8--11), on interaction, manipulatives, hints, explanations and themes spanning multiple years. Our exact launch, entry route and timing are design inferences. Year-1 \emph{Handouts 6}, Problems 6.2--6.6, provided a local example of connecting representations. Record actual problem, starting route, examples tried, what needed adult rescue, and what children want to resume. Distinguish observations from hypotheses. Counter fit, materials stock, procedures and classroom response have not been physically tested.'
 for i,solution in enumerate(g['solutions'],1):text+='\n'+r'\newpage'+'\n'+solution
 text+='\n'+r'\end{document}'+'\n'
 (dest/'facilitator.tex').write_text(text)
 build=dest/'build';build.mkdir(exist_ok=True)
 p=subprocess.run(['/Library/TeX/texbin/pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(build),'facilitator.tex'],cwd=dest,capture_output=True,text=True)
 (dest/'compile.txt').write_text(p.stdout+p.stderr)
 if p.returncode:raise SystemExit(p.stdout[-3000:])
 print(n,build/'facilitator.pdf')
