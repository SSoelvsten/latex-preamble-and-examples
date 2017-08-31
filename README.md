This small repository contains a LaTeX Preamble with settings for Computer Science handins together with a document with examples of use of all the different packages in the preamble together with a template to get a new document started quicker.

# Preamble
The preamble is made in two parts, with the intent to divide the settings between the general and the localization specific settings. This is only of value, should you write your .tex document in various languages.
- base: Packages and most settings
- dk/en: Settings specifically for localization to danish (dk) or english (en).

When importing the preamble you have to only import the localized .tex file, since there's already a call to the base settings within both. How you import it depends on where you have the preamble files located compared to your document.

## Same folder
```tex
\documentclass[a4, english]{article}
\input{preamble_en.tex}
```

## Absolute path
On Windows
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{C:/GitHub/LaTeX_Preamble_and_Examples/preamble/}{preamble_en.tex}
```

On Unix
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{/home/username/Documents/LaTeX_Preamble_and_Examples/preamble/}{preamble_en.tex}
```

## Relative path
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\subimport{../preamble/}{preamble_en.tex}
```

# Documents
This repository contains two documents, _template.tex_ and _example.tex._
## template.tex
A very small and sparse document, in which already the preamble, abstract, title, bibliography and two sections are ready for use. This should get you started much faster.
![Alt text](/img/template.png?raw=true "The template file")

## examples.tex
A slowly growing document with explanations and examples of using the various packages in the preamble. They are all made with the intent to be reverse engineerable.
![Alt text](/img/example.png?raw=true "The template file")

# Python Template Generator
In the folder Python you can find a Python Template Generator, created by Kristian 'Yurippe' Gausel. *prepare.py* is the file that creates *latexgen.py* and packs the template and the *preamble_en*, *preamble_dk* and *preamble_base* into *latexgen.py* to create a standalone script to generate a template from

This is especially useful for ShareLatTeX since you can add a --zip argument to zip the template into a ShareLaTeX compatible format for easy upload.

The *latexgen.py* file can be found under [Releases](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/releases)
