This small repository contains a LaTeX Preamble with settings for Computer Science handins together with a full document examples of use of all the different packages loaded with the preamble.

# Preamble_xx.tex
The preamble is made in two parts, with the intent to divide the settings between the general and the localization specific stuff. This is only of value, should you write your .tex document in various languages.
- Base: Packages and most settings
- dk/en: Settings specifically for localization to danish (dk) or english (en).

When importing the preamble you only have to import the localized .tex file, since there's already a call to the base settings within both. At the start of your new .tex file you write the following based on your language

```tex
\documentclass[a4, danish]{article}
\input{preamble_dk.tex}
```

# Template.tex
template.tex is a very small and sparse document, in which already the preamble, abstract, title, bibliography and two sections are ready for use. This should get you started much faster.

# Examples.tex
example.tex document is a slowly growing document with explanations and examples of using the various packages in the preamble. They are all made with the intent to be reverse engineerable.
