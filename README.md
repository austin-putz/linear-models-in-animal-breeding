# Animal Models: A Graduate Introduction

[![Render and Deploy](https://github.com/austinputz/animal-models-book/actions/workflows/quarto-publish.yml/badge.svg)](https://github.com/austinputz/animal-models-book/actions/workflows/quarto-publish.yml)

A comprehensive Quarto book on mixed model equations for animal breeding and genetics, designed for graduate students.

## Book URL

**Read the book online**: https://austinputz.github.io/animal-models-book/

## About This Book

This book provides a hands-on, example-driven introduction to animal models for first-year graduate students in animal breeding and genetics. Each of the 20 chapters starts with small datasets (5-10 animals), demonstrates hand calculations, and then scales up to realistic applications using R.

### What's Covered

- **Part I**: Foundations (introduction, MME basics, relationship matrices)
- **Part II**: Core animal models (sire model, animal model, repeatability, maternal effects)
- **Part III**: Multi-trait and longitudinal models (correlated traits, test-day, random regression, reaction norms)
- **Part IV**: Categorical traits (threshold models, survival analysis)
- **Part V**: Genomic prediction (G matrix, GBLUP, ssGBLUP, Bayesian alphabet)
- **Part VI**: Variance estimation and computing (ANOVA, REML, AI-REML, Bayesian methods, computational strategies)

Plus 6 comprehensive appendices covering notation, matrix operations, R code reference, BLUPF90 guide, datasets, and solutions to exercises.

## Local Development

### Prerequisites

1. [Install Quarto](https://quarto.org/docs/get-started/) (version 1.4 or higher)
2. [Install R](https://www.r-project.org/) (version 4.3 or higher recommended)
3. [Install RStudio](https://posit.co/download/rstudio-desktop/) (optional but recommended)

### Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/austinputz/animal-models-book.git
   cd animal-models-book
   ```

2. **Install required R packages**:
   ```bash
   Rscript setup.R
   ```

   Or manually in R:
   ```r
   install.packages(c(
     "tidyverse", "sommer", "pedigreemm", "BGLR",
     "Matrix", "nadiv", "kableExtra", "gt",
     "patchwork", "here", "lme4", "MCMCglmm"
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
quarto render chapters/01-introduction.qmd
```

To preview a single chapter:
```bash
quarto preview chapters/01-introduction.qmd
```

## Project Structure

```
animal-models-book/
├── _quarto.yml              # Book configuration
├── index.qmd                # Landing page
├── references.qmd           # Bibliography page
├── references.bib           # BibTeX references
├── chapters/                # 20 main chapters
│   ├── 01-introduction.qmd
│   ├── 02-mme-primer.qmd
│   └── ...
├── appendices/              # 6 appendices
│   ├── A-notation-reference.qmd
│   ├── B-matrix-operations.qmd
│   └── ...
├── data/                    # Example datasets (CSV files)
├── data-raw/                # R scripts to create datasets
├── styles/                  # Custom CSS
├── .github/workflows/       # GitHub Actions for deployment
└── setup.R                  # R package installation script
```

## Contributing

Contributions are welcome! If you find a typo, error, or have a suggestion:

1. **Report an issue**: [Open an issue](https://github.com/austinputz/animal-models-book/issues)
2. **Submit a fix**: Fork the repository, make your changes, and submit a pull request
3. **Discuss improvements**: Start a discussion in the [Discussions tab](https://github.com/austinputz/animal-models-book/discussions)

Please ensure your contributions maintain the book's pedagogical style:
- Start with small, hand-calculable examples
- Define all symbols and state dimensions
- Include R code in folded chunks (code-fold: true)
- Add practice exercises where appropriate

## Citation

If you use this book in your research or teaching, please cite as:

```
Putz, Austin (2025). Animal Models: A Graduate Introduction to Mixed Model Equations
  in Breeding and Genetics. https://austinputz.github.io/animal-models-book/
```

BibTeX:
```bibtex
@book{putz2025animal,
  title={Animal Models: A Graduate Introduction to Mixed Model Equations in Breeding and Genetics},
  author={Putz, Austin},
  year={2025},
  url={https://austinputz.github.io/animal-models-book/},
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
- Various R packages for mixed models (sommer, pedigreemm, BGLR, lme4, MCMCglmm)

Special thanks to the open-source community and to students who provided feedback on early drafts.

## Contact

For questions about the book content, please [open an issue](https://github.com/austinputz/animal-models-book/issues).

For other inquiries, contact Austin Putz via GitHub.
