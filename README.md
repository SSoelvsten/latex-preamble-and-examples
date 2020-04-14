# LaTeX - Preamble and Examples
[![MIT License](https://img.shields.io/badge/license-MIT%20License-blue.svg)](LICENSE.md)
![test](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/workflows/test/badge.svg?branch=master)

This small repository contains a LaTeX Preamble with settings for Computer
Science handins together with a document with examples of use of all the
different packages in the preamble together with a template to get a new
document started quicker.

> THIS IS A MAJOR REWRITE OF THE PREAMBLE! This does include multiple breaking
> changes. Your old version most likely does not at all compile any more. You
> can find the old version at commit `782d91460e2ba6f9c1c6a1c83b255decc7fb6dcc`
> or on the branch `version/v1`.

## Preamble
The preamble is made in two parts, with the intent to divide the settings
between the general and the localisation specific settings. This is only of
value, should you write your .tex document in various languages.
- `base_p1`, `base_p2`: Packages and most settings (the second part is to be
  executed after localisation)
- `dk`/`en`: Settings specifically for localisation to danish (dk) or english (en).
  The underlying preamble

When importing the preamble you have to only import the localised .tex file,
since there's already a call to the base settings within both. How you import it
depends on where you have the preamble files located compared to your document.

### Same folder
```tex
\documentclass[a4, english]{article}
\input{preamble_en.tex}
```

### Absolute path
On Windows
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{C:/GitHub/LaTeX-Preamble_and_Examples/preamble/}{preamble_en.tex}
```

On Unix
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{/home/username/Documents/LaTeX-Preamble_and_Examples/preamble/}{preamble_en.tex}
```

### Relative path
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\subimport{../preamble/}{preamble_en.tex}
```

## Documents
In the `documents` folder you can find multiple documents: _template*.tex_,
and _example*.tex._

This repository contains multiple templates to quickly get started on your next
hand-in, report, thesis, or slideshow.

![Alt text](/img/template.png?raw=true "The template files")

Furthermore the documents folder contains example documents with explanations
and examples of using the various packages in the preamble. They are all made
with the intent to be reverse engineerable.

![Alt text](/img/example.png?raw=true "The example files")