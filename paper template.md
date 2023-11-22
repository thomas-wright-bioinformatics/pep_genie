---
title: 'The Pep Genie: swift automation of peptide array data analysis through a Django web application'
tags:
  - Python
  - peptides
  - peptide arrays
  - biochemistry
  - Django
  - web application
  - data analysis
  - image analysis
authors:
  - name: Thomas A. Wright
    orcid: 0009-0006-2920-1764
    equal-contrib: true
    affiliation: 1
affiliations:
 - name: University of Glasgow, United Kingdom
   index: 1
date: 22 November 2023
bibliography: paper.bib
---




# Summary

The Pep Genie is a Django based website application that simplifies and speeds up the data analysis of peptide arrays. 

Peptide array screening is a method for analysing peptide binding against target proteins. Peptides arrays are small peptide libraries synthesised as a grid of spots on a membrane. Binding of an overlaid target is determined by immunodetection, and results in a grid of binding spot signals. 

Peptide arrays are analysed by measuring spot intensity and slicing spot images (Figure 1). 
Done manually, this is a lengthy and painstaking process. 
The Pep Genie provides a grid drawing method for the quick measurement of peptide array binding spots and slicing of spot images, and prepares the data directly in PowerPoint presentation format, saving considerable of time and work. 
The Pep Genie is an open-source software that is freely available at the host website and the GitHub repository.

[The Pep Genie](http://pepgenie.pythonanywhere.com)
<http://pepgenie.pythonanywhere.com>

[GitHub thomas-wright-bioinformatics](https://github.com/thomas-wright-bioinformatics)
<https://github.com/thomas-wright-bioinformatics>

![Figure 1: Peptide array analysis provided by The Pep Genie. Peptide array spots are quantified and sliced into figures.](app/static/app/img/docs-overview.png)










# Statement of need

`Gala` is an Astropy-affiliated Python package for galactic dynamics. Python
enables wrapping low-level languages (e.g., C) for speed without losing
flexibility or ease-of-use in the user-interface. The API for `Gala` was
designed to provide a class-based and user-friendly interface to fast (C or
Cython-optimized) implementations of common operations such as gravitational
potential and force evaluation, orbit integration, dynamical transformations,
and chaos indicators for nonlinear dynamics. `Gala` also relies heavily on and
interfaces well with the implementations of physical units and astronomical
coordinate systems in the `Astropy` package [@astropy] (`astropy.units` and
`astropy.coordinates`).

`Gala` was designed to be used by both astronomical researchers and by
students in courses on gravitational dynamics or astronomy. It has already been
used in a number of scientific publications [@Pearson:2017] and has also been
used in graduate courses on Galactic dynamics to, e.g., provide interactive
visualizations of textbook material [@Binney:2008]. The combination of speed,
design, and support for Astropy functionality in `Gala` will enable exciting
scientific explorations of forthcoming data releases from the *Gaia* mission
[@gaia] by students and experts alike.

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References
