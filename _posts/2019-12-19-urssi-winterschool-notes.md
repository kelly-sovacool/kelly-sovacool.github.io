---
title: "URSSI Winter School"
date: 2019-12-19
permalink: /posts/2019/12/urssi-winterschool-notes
tags:
  - Research Software Engineering
  - Open Source Software
  - Reproducibility
  - Software Development
---
# My notes from the URSSI Winter School

All slides & other resources are available on GitHub: [si2-urssi/winterschool](https://github.com/si2-urssi/winterschool)

**Contents**:
<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Day 1](#day-1)
	- [Intro to Software Design (Jeffrey Carver)](#intro-to-software-design-jeffrey-carver)
	- [Think like a programmer (Andy Loftus)](#think-like-a-programmer-andy-loftus)
	- [Intro to design patterns (Jeffrey Carver)](#intro-to-design-patterns-jeffrey-carver)
	- [Basics of packaging Python programs (Kyle Niemeyer)](#basics-of-packaging-python-programs-kyle-niemeyer)
- [Day 2](#day-2)
	- [Collaboration with Git & GitHub (Karthik Ram)](#collaboration-with-git-github-karthik-ram)
	- [Git Exercises (James Howison)](#git-exercises-james-howison)
	- [Software testing & continuous integration (Kyle Niemeyer)](#software-testing-continuous-integration-kyle-niemeyer)
	- [Git Exercises ctd (James Howison)](#git-exercises-ctd-james-howison)
- [Day 3](#day-3)
	- [Code Review (Jeffrey Carver)](#code-review-jeffrey-carver)
	- [Open Science & Software Citation (Kyle Niemeyer)](#open-science-software-citation-kyle-niemeyer)
	- [Reproducibility](#reproducibility)
	- [Documentation (Kyle Niemeyer)](#documentation-kyle-niemeyer)

<!-- /TOC -->

## Day 1

### Intro to Software Design (Jeffrey Carver)

* Whether you know it or not, you’re doing software design. Make those decisions with intent & purpose.
* Characteristics of good design
    * Firmness: hard to write bugs accidentally
    * Suitable for intended purpose
    * Interesting & useful to users
* Principles of design:
    * Traceability - easy to understand what the software is supposed to do.
    * Minimize intellectual distance - as close to the real-world as possible
    * Don’t reinvent the wheel. Re-use good design if it’s already a solved problem.
    * Accommodate change.
    * Fail gracefully.

### Think like a programmer (Andy Loftus)

* Solve easy problems; defer hard ones until they are easy.
    * Zen of Python (`import this`) excerpt: “If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea."
* Think about code before you write it
    1. Identify use cases
    2. Define goals from use cases
    3. Split into small, easy pieces
    4. Define one piece at a time
* Thinking about use-cases before the goal helps you focus on the small, easy-to-solve pieces (exact problem at hand, limit the scope of the problem) without getting bogged down in any grandiose, big-picture ideas.
* Encapsulation
    * Isolate unrelated concerns.
    * Hide changing things.
    * Python details:
        * Use the `@property` & `@var.setter` decorators for getters & setters.
        * `@classmethod` decorator for different constructors & other methods that work on the class but not instances of the class.
* Environment variables
    * `collections.ChainMap`: use it to prioritize program options.
        * `os.environ` to access shell environment variables.
        * Defaults = some dict
        * `combined = ChainMap(cmdline_args, os.environ, defaults)`
            * Equivalent of stringing together `dictionary.update` but in reverse
* Structuring code for readability: Trey Hunner blog post: craft your python like poetry.
* Low barrier to entry. Make your code usable & accessible to lots of people.
    * Make a runnable sample
        * Keep it short; one command if possible.
            * slick example: `curl URL/quickstart.sh | bash` (see slides for contents of `quickstart.sh`)
        * Clean up after running
        * Run it multiple times in a row & it does the exact same thing every time

### Intro to design patterns (Jeffrey Carver)

* Chain of responsibility
    * Common interface to handle requests, but user doesn’t need to know which specific method handles the request.
* Creational pattern: Builder
    * Create various representations of the same object. Abstract construction steps with different implementations of methods for different object variants.
* Structural pattern: Proxy
    * Only load something when you actually need it if it takes a long time to load or is expensive to create. e.g. when loading webpage, it’ll display the text before images have finished loading, with blank placeholder where image will load.
* More resources
    * “Gang of four” original book on design patterns
    * toptal.com python design patterns book

### Basics of packaging Python programs (Kyle Niemeyer)

* Module: any python file that contains definitions & statements.
* Package: a collection of modules in the same directory.
    * Must contain the `__init__.py` file. (Except for namespace packages...)
        * Often this file is empty.
        * Python executes this file before anything else when imported.
    * Can contain subdirectories with “submodules” containing more Python files and another `__init__.py` file.
    * Tests subdirectory for test files (more on pytest later).
* Lots of different ways to import modules.
    * Kyle’s preferred way: explicit relative imports
        * Uses dot notation (`.` for current path, `..` for one level up)
* DON’T REINVENT THE WHEEL
    * Rely on the standard library, numpy, scipy, etc.
* main() & `__main__` (Bryan Weber, writes for RealPython)
    * Can use a module both as a module AND a script.
    * main() is the entry point to the program.
    * Import guard example: realpython.com/python-main-function
    * `__main__.py`: special use case to execute your package as a script. e.g. pip.
* Package management
    * pip to install packages on PyPI or from source.
        * `-e` flag for development version.
    * The `setup.py` file (at same level as source directory) tells pip how to install your package.
        * See slides for example use.
    * See Kyle’s "better example” slide for cool use of `path.abspath` & `path.join` with `here` variable (kinda like R’s `here` pkg)
    * [Keep a Changelog](https://keepachangelog.com)
    * [Semantic versioning](https://semver.org) (PEP 440)
        * `MAJOR.MINOR.PATCH`
    * Problem with `setup.py`: could have malicious code.
        * PyPA has come up with `pyproject.toml` & `flit` to get around that. Also easier than using `setup.py`.
        * Also look into `cookiecutter` templates.
* Think about this at the very beginning so you don’t have to re-organize everything later.

## Day 2

### Collaboration with Git and GitHub (Karthik Ram)

* Workflows
    * Centralized workflow
        * Only works for really small projects
        * Everyone just commits to master 😬
    * Feature branching workflow
        * Also work in a feature branch.
        * Start a pull request before merging to master.
        * Delete branches after they’re merged.
    * Forking workflow
        * Only reason to fork is if you don’t have write access to someone else’s project / when you’re not a core contributor.
        * Create a PR when ready to merge.
* Alias `git` to [`hub`](https://hub.github.com/)
    * Extensions to interface with GitHub from the command line.
    * Create a GitHub repo from a local git repo: `git create username/reponame`
    * Open up the repo in your browser: `git browse`
    * Open a new PR: `git pull-request`
    * Compare 2 branches: `git compare master..feature-branch`
    * If you clone a repo but realize you wanted to fork it: `git fork`
* On branches:
    * A branch is just a pointer to a commit. Commits are linked nodes.
* Use pull requests as much as possible.
    * Fosters code review.
    * Facilitates discussion.
    * Can use continuous integration to run tests automatically.
    * Someone else should merge your code into master so two sets of eyeballs review each feature.
        * Pick one or two people to do a technical review & an end-user review.
    * Instead of creating a merge commit, could use rebase to squash all the commits from that branch into one.
    * NEVER SEND A PULL REQUEST FROM MASTER.
        * Master branches will become incompatible.
        * GitHub now warns you if you attempt to do this.
    * Never send a large pull request without notice.
        * Read the contributing doc.
        * Common practice is to ask whether the maintainers want the feature before you work on it.
        * Pull requests should be small, digestible changes.
            * Make each unit of code simple enough for someone to review & accept.
* Tips:
    * Always `git pull` before you start new work.
    * Keep branch names descriptive.
    * Generously use branches, but delete them when you’re done.
    * Use the `hub` extension to make your life easier.

### Git Exercises (James Howison)

* Pull requests are communication; make them digestible.
* Note: any time you edit files, that’s a feature, so you should always do that in a branch.
* Maintainer as developer AND champion of the community.
    * Create a welcoming & active environment.
    * How long ago was the last commit is really important. Is the project active?
    * “Turn the music on — make it feel like a party!"
    * Even when you’re working with people face-to-face, you should document discussions on GitHub.
* How to split pull requests.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">We’re learning so many useful tips &amp; tricks for research software sustainability at <a href="https://twitter.com/hashtag/urssi_winterschool?src=hash&amp;ref_src=twsrc%5Etfw">#urssi_winterschool</a> <br>...and having fun along the way! <a href="https://t.co/FMApXXj9wL">pic.twitter.com/FMApXXj9wL</a></p>&mdash; Kelly Sovacool (@kelly_sovacool) <a href="https://twitter.com/kelly_sovacool/status/1207708578561179648?ref_src=twsrc%5Etfw">December 19, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### Software testing & continuous integration (Kyle Niemeyer)

* How do you know your code gives the right answers? …what about after you make changes to the code?
* When: ALWAYS
* Where: external test suite
    * e.g. inside `tests/` subdir in package repo.
    * Some tests are better than no tests. But a rigorous test suite is best!
* Why: make sure our results are trustworthy.
    * It’s really easy to make subtle mistakes.
    * Helps us know that a PR won’t break anything.
    * Unit tests are good examples of how a package works.
* What and how
    * Tests compare expected vs observed outputs for known inputs.
    * You don’t have to have a function written in order to write a test.
    * Use assertions (e.g. `assert exp == obs`).
    * Use `math.isclose()` or `np.allclose()` to get around floating point precision.
    * Use `pytest` package.
        * `-s` to keep standard output.
        * `-k` to run tests matching a substring.
        * `-q` run specific test file & test function.
* What cases to test
    * Interior: precise values don’t matter (just test one of these).
    * Edge: beginning or end of range of inputs (test all of these).
    * Corner cases: 2 or more edge cases that intersect.
* Pytest test generators
    * Decorator to feed lots of inputs to one test function: `@pytest.mark.parametrize`
* Types of tests
    * Unit test: test individual functions & methods.
        * Have to break up your code into small functions.
    * Integration test: verify that multiple pieces of the code work together.
    * Regression test: confirm that new results match prior results (which are assumed correct).
* Test-driven development (TDD): write your tests before you implement the functions.
* More tips
    * Test for consistency with PEP8.
        * e.g. `flake8`: linter & style-checker. `black` auto-formatter (not mentioned by Kyle).
        * Plugins for your favorite IDE to run it continuously.
    * Test that exceptions are raised: `pytest.raises(ExceptionClass)`
    * Mocking
        * Replace parts of the system with precisely controllable code to specify return values & throw exceptions.
* Test coverage
    * Percentage of code (in number of lines) that are touched by tests.
    * 100% test coverage doesn’t guarantee that you catch all potential errors; it means every line of code is run by at least one test.
    * `pytest-cov` creates a coverage report.
    * codecov.io integrates with GitHub.
* Continuous integration
    * Ensure all changes to your project pass tests through automated test & build process.
    * Services: GitHub Actions, travis, CircleCI, AppVeyor, Jenkins (used by mothur)
    * Add the CI badge to your readme: it signals that your tool is being actively maintained.
    * See PyTeCK repo as an example of useful badges.
* Tests in the wild: PyTeCK

### Git Exercises ctd (James Howison)

* The "split a pull request" activity (see urssi repo).
* [LearnGitBranching](https://learngitbranching.js.org/?NODEMO) visualizer.
* Note: `git cherry-pick` keeps the original author information. 😄
* `git rebase` re-writes history to move the branch point. Obviates merge commits, instead makes them fast-forwards.
* `git rebase -i` in interactive mode is a good idea. Allows you to squash commits and clean things up.

## Day 3

### Code Review (Jeffrey Carver)

* Code review augments testing, but doesn’t replace testing.
    * Efficiency, readability, etc. can’t be tested for.
* The purpose is to make the code better. Everyone makes mistakes. There’s no expectation that you’ll do it exactly right the first time.
* By doing code review, you save time down the road.
* Goals:
    * Team cohesion.
        * Gain shared understanding of the project.
        * Get to know teammates skills’ better.
    * Code quality.
        * Find problems early.
        * Get different perspectives.
        * Consistency & readability.
        * Makes code easier to maintain.
    * Personal learning.
        * Reading other people’s code & having your code reviewed.
* Mindset:
    * Developer:
        * Recognize that a code critique is not a personal attack. You are not your code.
        * Be ready & willing to learn new things.
        * Expect that there will be changes. Remove the fear of making mistakes.
        * Be humble.
    * Reviewer:
        * Don’t assume that your way is the best.
        * Make positive comments, not only negative ones.
        * Understand why the developer asked you to review the code.
        * Focus on the code, not on the author.
        * Pick your battles.
* Techniques
    * Prioritize things that humans can spot that automated testing can't.
        * Readability
        * Algorithms
* How we communicate matters (applies in all types of feedback-giving)
    * Ask questions where possible.
        * e.g. “Have you considered…” -- Maybe they have and there's a good reason for it.
    * No personal attacks. It's about the code, not the person!
    * Be as specific as possible about how the code could be improved instead of making general statements.
    * Put yourself in others' shoes.
        * If you wouldn't want to get the comment, you probably shouldn't give it to someone else.
    * Explain _why_ you're making the suggestion.
* Checklist
    * Before you ask someone to review your code:
        * Write tests.
        * Make sure the code runs & passes the tests.
        * Write comments & other documentation.
            * Document any weird edge cases & work-arounds
        * Follow the style guide.
    * When you review someone else's code:
        * Comments are understandable & appropriate.
        * DRY up repetitive code.
        * Code runs & passes tests.
        * Exceptions are handled appropriately.
* Best practices
    * Communicate goals of code review.
    * Do it early & often.
    * Review a small amount of code.
        * If it takes longer than 60 minutes to review, that's too much.
    * Establish a process for what to do after reviews.
        * Is it a hard gate that you have to make the reviewer happy, or are they just suggestions you could choose not to follow?
* Issues you might identify in code review
    * Inconsistent style
    * Inefficiency
    * Unvalidated inputs
    * Lack of exception handling
* Why is code review important for research software specifically?
    * Just like peer-reviewing publications, we want to make sure the code underlying the science is sound.
    * Science depends on the correctness of your code.
    * Help spread best-practices & high-level understanding in the scientific community.
    * Results may not always be known. There's not always "ground truth" (e.g. in simulations).
* GitHub-specific tips: using Pull Requests for code review (examples: [pr-omethe-us/PyKED](https://github.com/pr-omethe-us/PyKED) & [astropy](https://github.com/astropy/astropy)) (Kyle Niemeyer)
    * Use pull request templates.
        * Could enforce check boxes like which issue(s) it resolves, that test cases were added, etc.
    * Easily view file diffs & add comments right alongside the code. Facilitates conversation.
        * You can leave comments at multiple lines.
        * Make suggestions for small, easy changes. There's an "insert suggestion" button! (Don't do this for design changes.)
    * Under settings > branches, you can protect branches
        * e.g. require that a PR has to be reviewed before merging into master.
        * More on code owners in [github docs](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners)
    * Tool: [octobox.io](https://octobox.io) for managing GitHub notifications.

### Open Science and Software Citation (Kyle Niemeyer)

* TLDR: if you make your code public, pick a license and put a `LICENSE` file in your repo.
* Copyright
    * Facts & ideas are **not** copyrightable.
    * _Expressions_ of ideas **are** copyrightable.
    * Right of first publication: goes to the first creator even if not explicitly specified.
    * You should include a license with all publicly available software code so people know how they can (or can't) use it.
        * Or, you can explicitly put work into the public domain, then it's free for anyone & everyone to use & modify.
* Software Licenses
    * Types:
        * Proprietary
        * Free/open source (FOSS, FLOSS, OSS)
            * Permissive: BSD 3-clause, MIT
            * Copyleft: GPL (the license is "viral")
    * Pick an existing license; don't make your own!
    * [choosealicense.com](https://choosealicense.com)
    * Open Source Initiative (OSI) Licenses
        * To call your work "open-source", you have to release it under one of the OSI licenses.
* Non-software: Creative Commons
    * Codes:
        * BY: Attribution (similar to permissive)
        * SA: ShareAlike (similar to copyleft)
        * ND: NoDerivatives
        * NC: NonCommercial
    * e.g. CC BY, CC BY-SA
    * CC0: like the public domain version of creative commons.
* More concepts
    * Patents: cover ideas & concepts (which copyright doesn't).
    * Trademarks: symbols that represent a business or organization.
    * Export control: gov't may forbid transfer of code/data/ideas to another country or foreign national.
    * HIPAA: cannot share human patient data.
* Archiving & Citing Software
    * Services: Zenodo, figshare, something within your University's library (UMich has one)
        * Archives your stuff forever and makes it citable with a DOI.
        * figshare: company, for-profit...
        * Zenodo: run by CERN. Will be around as long as the EU exists.
            * Free! Good file size limits.
            * Connects with GitHub! When you turn on Zenodo for your repo, it creates a new DOI when you cut a new release.
    * Without proper citations, your work is not reproducible.
    * Academia relies on citations for credit.
    * Paper: [Software Citation Principles](https://peerj.com/articles/cs-86/)
        * Software should be "first-class" citations just like other publications.
        * How? name, author(s), DOI or other persistent identifier.
            * A GitHub link is **not** a persistent identifier, but it's better than nothing.
        * If there's a paper describing it, cite both the paper & the code DOI.
    * How can we make our software easily citable?
        * Create a DOI (e.g. via Zenodo)
        * Include a `CITATION` file in your GitHub repo.
    * Tool in development: [cite as](https://citeas.org) (James Howison)
        * Web scraper to find the right citation given a package name or website.

### Reproducibility

* repro-packs (Kyle Niemeyer)
    * Lorena Barbra: "reproducibility packages (repro-pack)" -- packages associated with papers shared under CC-BY.
    * Produce a single repro-pack for an entire paper
        * containing:
            * Code, results, input data (if small enough)
            * Figures (vector format)
            * Config file, etc
        * Upload to FigShare/Zenodo under CC-BY license.
        * Cite using the resulting DOI in the associated papers.
    * Benefits
        * Improve reproducibility & impact of your work.
        * Reviewers love it.
        * Lets you reuse your figures without violating a journal copyright.
            * When published, the journal (one that isn't open access) owns the paper & everything in it that isn't licensed from somewhere else.
    * Can include an appendix with statement about the availability of material. Or put it in the methods section.
    * [Research compendium](https://github.com/ropensci/rrrpkg): make your paper like a package so it's easily-installable. Uses lightweight packaging structure.
* rOpenSci (Karthik Ram)
    * rOpenSci: Scientific software for R. Helping researchers write sustainable software tools.
    * [software-review](https://github.com/ropensci/software-review): rOpenSci Software Peer Review of community-contributed packages
    * JOSS got started when rOpenSci realized the need extends beyond R packages.
    * rOpenSci's [dev-guide](https://devguide.ropensci.org/)
    * PyOpenSci recently got started as the Python version of ROpenSci. ([David Nicholson](https://twitter.com/nicholdav))
* JOSS: Journal of Open Source Software (Kyle Niemeyer)
    * Open, no fees.
    * If you've already licensed your code & have good documentation, it should take under an hour to submit to JOSS.
    * Very short paper to describe the software.
    * All the conversation happens on GitHub. Uses same structure as JOSE (Journal of Open Source Education).
    * Questions from the audience: when to submit as a package (e.g. to JOSS) versus in a repro-pack (to your society journal)?
        * If anyone else would ever use it, it should probably be a package.
        * If the code is only used for creating a paper, it should just be in the repro-pack.
        * If your goal is to write a methods paper, it probably wouldn't go to JOSS.
        * **If you have the option to submit to a domain journal, do that first instead of JOSS.** (Karthik's take)
            * JOSS is meant to fill in the gap for people who don't have a place to publish their software.
    * This is for getting research credit. _But_ you still need to cite the specific version you used (e.g. from Zotero) for reproducibility purposes.

* Sidney Bell at the Chan Zuckerberg Initiative.
    * CZI started funding scientific software.
        * foundational packages (e.g. scikit-learn, matplotlib, pandas).
        * biology domain-specific packages.
    * First cycle of funding awarded. Second round closes in Feb.
    * Funding awarded to organizations (e.g. NumFocus, Universities), not people.

### Documentation (Kyle Niemeyer)

* Value of documentation.
    * The value & extent of your work if it's understandable by your colleagues.
    * Provides provenance for your scientific process.
    * Demonstrates your skill & professionalism.
    * "A love-letter that you write to your future self."
* It's easier than you think!
* Types:
    * user & developer guides
        * `README` file accompanied by `LICENSE`, `CITATION`, `CHANGELOG`, etc.
    * code comments
        * docstring
            * for functions & classes
            * available within Python via `help()` & easy to parse by Sphinx.
        * in-line
            * bad: polluting the code with unnecessary information that's already evident from reading the code.
            * good: use sparingly to explain reasons behind choices & complicated sections
    * self-documenting code
        * intelligently name things that tells you why it exists, what it does, and how it's used.
        * write really simple functions that do only one thing.
            * "A `function` should have _a function_, not _multiple functions_."
        * follow consistent style.
    * generated API documentation
* Tools
    * Sphinx: automatically generate documentation
        * Set it up with CI to automatically build your documentation website when you make changes.
        * Writing docstrings that are compatible with Sphinx:
            * Styles: NumPy, Google, reStructuredText...
            * Specify parameters, returns, & include a short description
        * Easy to get started quickly. See slides for more details.
            ```
            # at top-level of repo, same level as package dir
            mkdir docs/
            cd docs/
            sphinx-quickstart
            make html
            ```
    * `doctr`: auto-deploy docs to GitHub pages using TravisCI.
    * [Read the Docs](https://readthedocs.org) to host your documentation.
        * Simple example: [Kyle's MechE course](https://github.com/kyleniemeyer/ME373)
        * More complex example: [astropy](https://github.com/astropy/astropy)
