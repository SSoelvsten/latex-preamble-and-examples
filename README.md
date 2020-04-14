# LaTeX - Preamble and Examples
[![version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/tree/master)
![test](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/workflows/test/badge.svg?branch=master)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/graphs/commit-activity)
[![MIT License](https://img.shields.io/badge/license-MIT%20License-blue.svg)](LICENSE.md)

This small repository contains a LaTeX Preamble with settings for Computer
Science handins together with a document with examples of use of all the
different packages in the preamble together with a template to get a new
document started quicker.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [LaTeX - Preamble and Examples](#latex---preamble-and-examples)
    - [Example and Template Documents](#example-and-template-documents)
        - [Templates](#templates)
        - [Examples](#examples)
    - [How to use the preamble in your project](#how-to-use-the-preamble-in-your-project)
        - [Step 1: Installation](#step-1-installation)
            - [Local Machine](#local-machine)
            - [Git Project](#git-project)
            - [Overleaf / ShareLaTeX](#overleaf--sharelatex)
        - [Step 2: Linking your document with the preamble](#step-2-linking-your-document-with-the-preamble)

<!-- markdown-toc end -->

> DISCLAIMER: To compile your old documents prior to the rewrite in early 2020
> you most likely need to use the old version. This one can be found on the
> [`version/v1`](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/tree/version/v1)
> branch.

## Example and Template Documents
In the `documents` folder you can find multiple documents of the form
`template_*.tex` and `example_*.tex.`. The compiled version of all files are
also immediately provided, such that you can cross-compare the code and the
output without having to compile yourself.

### Templates

| File                        | Purpose                                        |
|-----------------------------|------------------------------------------------|
| `template_blank.tex`        | Smallest template provided, useful for handins |
| `template_dissertation.tex` | Template for your dissertations                |
| `template_report.tex`       | Template for longer reports and papers         |

### Examples
The examples provide explanations and examples of how to use the various
packages in the preamble. They are all made with the intent to be reverse
engineerable.

| File                  | Purpose                                                  |
|-----------------------|----------------------------------------------------------|
| `example_article.tex` | Example document for handins, reports, and dissertations |
| `example_beamer.tex`  | Example document for slideshows                          |

## How to use the preamble in your project
The purpose of a preamble is to have a single source of all your LaTeX settings.
This can work elegantly when the document source is on your machine.

### Step 1: Installation
Before you can include the preamble in your project you first need a copy of the
preamble.

#### Local Machine
For a simple project on your local machine you can simply _clone_ this
repository somewhere on your machine.
```bash
git clone git@github.com:SSoelvsten/LaTeX-Preamble_and_Examples.git
```
If you don't need the examples document, you can choose to only clone the
`preamble-only` branch.
```bash
git clone -b preamble-only git@github.com:SSoelvsten/LaTeX-Preamble_and_Examples.git
```

#### Git Project
In a Git repository you may want to directly include this as a subrepository
such that everyone has the same version and the relative path is always the
same. To keep the footprint small, you only need to clone the `preamble-only`
branch which contains the newest version of all the files in the _preamble/_
folder.

To do this run the following commands
```bash
git submodule add -b preamble-only git@github.com:SSoelvsten/LaTeX-Preamble_and_Examples.git preamble
git commit -m "Add preamble submodule"
```
This registers the subrepository in your project as a submodule and places the
preamble files in the _preamble/_ folder.

When you then clone your Git project, then either clone it with the
`--recursive` option or run the following two commands in an already cloned repository.
```bash
git submodules init
git submodules update
```

#### Overleaf / ShareLaTeX
In the
[Releases](https://github.com/SSoelvsten/LaTeX-Preamble_and_Examples/releases)
section you can find _.zip_ files that you can directly drag and drop into your
project and have everything set up. This way you can directly skip _Step 2_.

### Step 2: Linking your document with the preamble
The preamble is made in two parts, with the intent to divide the settings
between the general and the localisation specific settings. This is only of
value, should you write your .tex document in various languages.
- `base_p1`, `base_p2`: Packages and most settings (the second part is to be
  executed after localisation)
- `dk`/`en`: Settings specifically for localisation to danish (dk) or english (en**.
  The underlying preamble

When importing the preamble you have to only import the localised .tex file,
since there's already a call to the base settings within both. How you import it
depends on where you have the preamble files located compared to your document.

**Case: Same folder**
```tex
\documentclass[a4, english]{article}
\input{preamble_en.tex}
```

**Case: Relative path**
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\subimport{../preamble/}{preamble_en.tex}
```

**Case: Absolute path**
> **On Windows**
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{C:/GitHub/LaTeX-Preamble_and_Examples/preamble/}{preamble_en.tex}
```

> **On Unix**
```tex
\documentclass[a4, english]{article}
\usepackage{import}
\import{/home/username/Documents/LaTeX-Preamble_and_Examples/preamble/}{preamble_en.tex}
```

Notice, that the paths above is a bit different if you choose to only clone the
`preamble-only` branch.
