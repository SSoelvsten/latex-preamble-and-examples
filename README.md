This small repository contains a LaTeX Preamble with packages and settings for Computer Science handins together with examples of use.

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
The template.tex is a very small and sparse file, in which already the preamble, abstract, title, bibliography and two sections are ready for use. This should get you started much faster.

# Examples.tex
The example.tex document is a slowly growing document with explanations and examples of using the various packages in the preamble. They are all made with the intent to be reverse engineerable.
