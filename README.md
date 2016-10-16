This small repository contains a LaTeX Preamble with settings for Computer Science handins together with a full document examples of use of all the different packages loaded with the preamble.

# Preamble
The preamble is made in two parts, with the intent to divide the settings between the general and the localization specific stuff. This is only of value, should you write your .tex document in various languages.
- base: Packages and most settings
- dk/en: Settings specifically for localization to danish (dk) or english (en).

When importing the preamble you have to only import the localized .tex file, since there's already a call to the base settings within both. How you import it depends on where you have the preamble files located compared to your document.

## Same folder
```tex
\documentclass[a4, english]{article}
\input{preamble_en.tex}
```

## Absolute path
```tex
\documentclass[a4, english]{article}
%\usepackage{import}
%\import{C:/GitHub/LaTeX_Preamble_and_Examples/preamble/}{preamble_en.tex}
```

## Relative path
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\subimport{../preamble/}{preamble_en.tex}
```

# Documents
This repository contains two documents _template.tex_ and _example.tex._
## template.tex
A very small and sparse document, in which already the preamble, abstract, title, bibliography and two sections are ready for use. This should get you started much faster.
![Alt text](/img/template.png?raw=true "The template file")

## examples.tex
A slowly growing document with explanations and examples of using the various packages in the preamble. They are all made with the intent to be reverse engineerable.
![Alt text](/img/example.png?raw=true "The template file")
