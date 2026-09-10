# Linear Models in Animal Breeding: A Worked Approach

[![Render and Deploy](https://github.com/austin-putz/animal-models-book/actions/workflows/quarto-publish.yml/badge.svg)](https://github.com/austin-putz/animal-models-book/actions/workflows/quarto-publish.yml)

A graduate textbook on the pedigree-based mixed model, written so that every result is worked on
real numbers before it is written as a formula. Each chapter opens with a dataset small enough to
solve with a calculator, works the mixed model equations step by step, reproduces the identical
answer in R, and then scales the same model up.

Genomic selection and large-scale computation are deliberately out of scope; each is deferred to a
companion volume.

## Book URL

**Read the book online**: https://austin-putz.github.io/animal-models-book/

## About This Book

This book provides a hands-on, example-driven introduction to animal models for first-year graduate students in animal breeding and genetics. Each of the 24 chapters starts with small datasets (5-10 animals), demonstrates hand calculations, and then scales up to realistic applications using R.

### What's Covered

- **Part I**: Background (matrix algebra, linear models, mixed models, relationship matrices, data preparation)
- **Part II**: Core animal models (animal model, reduced models, random environmental effects, genetic groups, maternal effects)
- **Part III**: Advanced model structures (multivariate, random regression, social interaction)
- **Part IV**: Categorical and time-to-event traits (threshold models, survival analysis)
- **Part V**: Non-additive genetic effects (dominance, epistasis)
- **Part VI**: Multibreed and crossbred evaluation
- **Part VII**: Variance component estimation (ANOVA/Henderson, REML/AI-REML, Gibbs sampling)
- **Part VIII**: Validation and computation

Plus 9 appendices covering notation, the BLUP derivation, algorithms, R code reference, BLUPF90 guide, datasets, and solutions to exercises.

### Scope

This book covers the **pedigree-based** mixed model. Two subjects are deliberately deferred to companion volumes rather than compressed into a chapter here:

- **Genomic selection** - the genomic relationship matrix, GBLUP, single-step, and the Bayesian alphabet
- **Large-scale computation** - sparse methods, parallel solving, and software internals

Chapter 24 is the one exception on computation: it exists so readers understand why production evaluations are not solved the way the examples in this book are.

The full chapter outline, including per-chapter objectives, sections, and datasets, is in [CHAPTERS.md](CHAPTERS.md).

## Local Development

### Prerequisites

1. [Install Quarto](https://quarto.org/docs/get-started/) (version 1.4 or higher)
2. [Install R](https://www.r-project.org/) (version 4.3 or higher recommended)
3. [Install RStudio](https://posit.co/download/rstudio-desktop/) (optional but recommended)

### Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/austin-putz/animal-models-book.git
   cd animal-models-book
   ```

2. **Install required R packages**:
   ```bash
   Rscript setup.R
   ```

   Or manually in R:
   ```r
   install.packages(c(
     "tidyverse", "sommer", "pedigreemm", "nadiv",
     "Matrix", "lme4", "MCMCglmm", "coda",
     "survival", "coxme", "orthopolynom",
     "kableExtra", "gt", "patchwork", "here"
   ))
   ```

3. **Render the book locally**:
   ```bash
   quarto render
   ```

   The rendered book will be in the `_book/` directory.

4. **Preview the book**:
   ```bash
   quarto preview
   ```

   This will open a browser window with a live preview that updates as you edit.

### Working on Specific Chapters

To render a single chapter:
```bash
quarto render chapters/01-matrix-algebra.qmd
```

To preview a single chapter:
```bash
quarto preview chapters/01-matrix-algebra.qmd
```

## Project Structure

```
animal-models-book/
├── _quarto.yml              # Book configuration
├── CHAPTERS.md              # Chapter outline (source of truth for structure)
├── CLAUDE.md                # Scope, conventions, and authoring rules
├── index.qmd                # Landing page
├── references.qmd           # Bibliography page
├── references.bib           # BibTeX references
├── chapters/                # 24 main chapters
│   ├── 01-matrix-algebra.qmd
│   ├── 02-linear-models.qmd
│   └── ...
├── appendices/              # 9 appendices
│   ├── A-notation-reference.qmd
│   ├── B-blup-derivation.qmd
│   └── ...
├── data/                    # Example datasets (CSV files)
├── data-raw/                # R scripts to create datasets
├── styles/                  # Custom CSS
├── .github/workflows/       # GitHub Actions for deployment
└── setup.R                  # R package installation script
```

## Contributing

Contributions are welcome! If you find a typo, error, or have a suggestion:

1. **Report an issue**: [Open an issue](https://github.com/austin-putz/animal-models-book/issues)
2. **Submit a fix**: Fork the repository, make your changes, and submit a pull request
3. **Discuss improvements**: Start a discussion in the [Discussions tab](https://github.com/austin-putz/animal-models-book/discussions)

Please ensure your contributions maintain the book's pedagogical style:
- Start with small, hand-calculable examples
- Define all symbols and state dimensions
- Include R code in **visible** chunks — `code-fold` is off book-wide, because the code is
  material students read and retype rather than an appendix. See the "Code visible" rule in
  `CLAUDE.md` for what that requires of the code itself.
- Add practice exercises where appropriate

## Citation

If you use this book in your research or teaching, please cite as:

```
Putz, Austin (2025). Linear Models in Animal Breeding: A Worked Approach
  in Breeding and Genetics. https://austin-putz.github.io/animal-models-book/
```

BibTeX:
```bibtex
@book{putz2025animal,
  title={Linear Models in Animal Breeding: A Worked Approach},
  author={Putz, Austin},
  year={2025},
  url={https://austin-putz.github.io/animal-models-book/},
  note={Online book}
}
```

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license

## Acknowledgments

This book was developed using:
- [Quarto](https://quarto.org/) for publishing
- [R](https://www.r-project.org/) for statistical computing
- [tidyverse](https://www.tidyverse.org/) for data manipulation
- Various R packages for mixed models (sommer, pedigreemm, nadiv, lme4, MCMCglmm)

Special thanks to the open-source community and to students who provided feedback on early drafts.

## Contact

For questions about the book content, please [open an issue](https://github.com/austin-putz/animal-models-book/issues).

For other inquiries, contact Austin Putz via GitHub.
