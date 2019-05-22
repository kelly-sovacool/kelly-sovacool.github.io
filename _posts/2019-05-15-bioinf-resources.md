---
title: 'Bioinformatics Resources'
date: 2019-05-15
permalink: /posts/2019/05/bioinf-resources
tags:
  - Bioinformatics
  - Software Development
  - Data Analysis
  - Reproducibility
---

# Resources for Bioinformatics Software Development & Data Analysis

I found myself sending some of the same links over and over again to people who asked questions related to bioinformatics. So it was time to compile all the links in one convenient place!

All of the resources linked below are free unless otherwise noted. This isn't intended to be an exhaustive list of all the resources available, just some of the ones I have come across and have found useful.

*Last updated: 2019-05-15*

**Table of Contents:**
<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Programming](#programming)
	- [Python](#python)
	- [R](#r)
- [Reproducibility](#reproducibility)
	- [Project organization](#project-organization)
	- [Literate programming](#literate-programming)
		- [R Markdown](#r-markdown)
		- [Jupyter](#jupyter)
	- [Documentation](#documentation)
- [Misc. Tools](#misc-tools)
	- [For git](#for-git)
	- [Editors](#editors)
	- [etc.](#etc)

<!-- /TOC -->


## Programming
- [Software Carpentry](https://software-carpentry.org/lessons/): Intro lessons on the Unix shell, git, R, & Python.
- [Langmead Lab teaching materials](http://www.langmead-lab.org/teaching-materials/): cover classic bioinformatics algorithms.
- [Advent of Code](https://adventofcode.com/): small programming puzzles.
- [Stepik Bioinformatics Contest](https://bioinf.me/en/contest).

### Python
- [Project Rosalind](http://rosalind.info/problems/locations/): learn Python & practice solving bioinformatics problems.
- [GWC Code demos](https://github.com/GWC-DCMB/codeDemos): introductory Python demos - [Girls Who Code @ UM-DCMB](http://umich.edu/~girlswc/)
- [GWC Challenge Questions](https://github.com/GWC-DCMB/challengeQuestions): practice solving problems - [Girls Who Code @ UM-DCMB](http://umich.edu/~girlswc/)
- [Python For Everybody](https://www.coursera.org/specializations/python) course on Coursera (free for UMich students) - Charles Severance
- Books:
    - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - Al Sweigart
    - [Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/thinkpython/html/index.html) - Allen Downey
    - [Dive Into Python 3](https://www.cmi.ac.in/~madhavan/courses/prog2-2012/docs/diveintopython3/index.html) - Mark Pilgrim
    - [Object-Oriented Programming in Python](https://python-textbok.readthedocs.io) - 
- Videos:
    - [Office Hours for BIOINF 529: Bioinformatic Concepts & Algorithms](https://www.youtube.com/channel/UCewko4qgzTUZFmydW2shcEg) - [Marcus Sherman](https://www.betteridiot.tech/)
    - [Transforming Code into Beautiful, Idiomatic Python](https://pyvideo.org/pycon-us-2013/transforming-code-into-beautiful-idiomatic-pytho.html) - Raymond Hettinger
    - [Beyond PEP 8 -- Best practices for beautiful intelligible code](https://youtu.be/wf-BqAjZb8M) - Raymond Hettinger

### R
- [Riffomonas minimalR](http://www.riffomonas.org/minimalR/): Intro to R tutorial with applications in microbiology - Pat Schloss
- [What they forgot to teach you about R](https://whattheyforgot.org/) - Jenny Bryan & Jim Hester
- [Happy Git and GitHub for the useR](https://happygitwithr.com/) - Jenny Bryan & Jim Hester
- Books:
    - [R for Data Science](https://r4ds.had.co.nz/) - Hadley Wickham
    - [Mastering Software Development in R](https://bookdown.org/rdpeng/RProgDA/) - Roger Peng, Sean Kross, & Brooke Anderson
    - [Advanced R](https://adv-r.hadley.nz/) - Hadley Wickham
    - [R Packages](http://r-pkgs.had.co.nz/) - Hadley Wickham


## Reproducibility
- [Riffomonas reproducible research tutorial](http://www.riffomonas.org/reproducible_research/) - Pat Schloss
- [Snakemake](https://snakemake.readthedocs.io/en/stable/): Python-based workflow management system.
- [conda](https://conda.io/en/latest/): package, dependency, & environment manager.
- [git](https://git-scm.com/doc): version control system.
    - Also take a look at the [Software Carpentry lesson on git](http://swcarpentry.github.io/git-novice/).

### Project organization
- Noble WS. **A quick guide to organizing computational biology projects**. PLoS Comput Biol. 2009 Jul;5(7):e1000424. doi: [10.1371/journal.pcbi.1000424](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424).
- [Scientific project template](https://github.com/SchlossLab/new_project).
- [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) project templating tool.

### Literate programming

#### R Markdown
- [How I use R Markdown to document my bioinformatics analyses](https://rachaellappan.github.io/rmarkdown/) - Rachael Lappan
- [RMarkdown for writing reproducible scientific papers](https://libscie.github.io/rmarkdown-workshop/handout.html) - Mike Frank & Chris Hartgerink
- [R Markdown: The Definitive Guide](https://bookdown.org/yihui/rmarkdown/) - Yihui Xie, J. J. Allaire, Garrett Grolemund

#### Jupyter
- [Jupyter Notebooks for Performing and Sharing Bioinformatics Analyses](https://github.com/ljdursi/glbio-jupyter-workshop) - Jonathan Dursi
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/en/stable/)

### Documentation
- Lee BD (2018) **Ten simple rules for documenting scientific software**. PLoS Comput Biol 14(12): e1006561. doi: [10.1371/journal.pcbi.1006561](https://doi.org/10.1371/journal.pcbi.1006561).
- [Sphinx](http://www.sphinx-doc.org/en/master/) for creating documentation.
- [Read the Docs](https://docs.readthedocs.io/en/stable/) for hosting documentation.
- [Writing R package documentation](https://support.rstudio.com/hc/en-us/articles/200532317-Writing-Package-Documentation).
- [pkgdown](https://pkgdown.r-lib.org/): build a website for your R package.


## Misc. Tools

### For git
- Link your university email to [GitHub](https://education.github.com/benefits) to get pro/education features.
    - All users (Pro or free) get free unlimited private repositories on GitHub.
- [GitKraken](https://www.gitkraken.com/invite/xin2e3HK) has a nice GUI for interacting with git, GitHub, GitLab, etc. (Note that this is a referral link to be entered to win a Nintendo Switch.)

### Editors
- [Atom](https://atom.io/): text editor. Additional pacakges for atom:
    - [Autosave on change](https://atom.io/packages/autosave-onchange)
    - [Markdown Preview](https://atom.io/packages/markdown-preview-plus)
    - [Markdown TOC](https://atom.io/packages/markdown-toc)
    - [Language LaTeX](https://atom.io/packages/language-latex)
- [PyCharm](https://www.jetbrains.com/pycharm/): IDE for Python.
    - The community edition is free, or link your university email to get the pro version for free.
    - Supports Snakemake syntax highlighting & Jupyter notebooks.
- [RStudio](https://www.rstudio.com/): IDE for R.
- [Kite](https://kite.com/): AI autocomplete for Python. Works in Atom, PyCharm, Vim, & more.

### etc.
- [docopt](http://docopt.org/): easily create & parse command-line interfaces. Available for Python, R, C++, & more.
- [csvkit](https://csvkit.readthedocs.io/en/1.0.3/index.html): command-line tool for working with and converting to CSV format from Excel, JSON, etc.
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) Python testing module.
