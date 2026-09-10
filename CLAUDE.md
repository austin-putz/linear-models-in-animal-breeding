# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this book is

**Linear Models in Animal Breeding: A Worked Approach** — a
Quarto book for first-year graduate students in animal breeding and genetics.

The book teaches the **pedigree-based** mixed model. Every chapter starts with a dataset small
enough to solve by hand (5–10 animals), works the mixed model equations step by step, then scales
the same model up in R.

Author: Austin Putz. Rendered with Quarto to HTML and PDF; deployed to GitHub Pages.

## Scope

### In scope

- Matrix algebra, fixed linear models, and mixed models as background
- Pedigrees, the numerator relationship matrix **A**, and **A⁻¹**
- The animal model and its equivalent/reduced forms (sire, sire–MGS, reduced animal)
- Random environmental effects, genetic groups, maternal effects
- Multivariate, longitudinal/random regression, and social interaction models
- Threshold models for categorical traits, and survival analysis
- Non-additive (dominance, epistasis) models built from pedigree relationships
- Multibreed and crossbred (CCPS) evaluation
- Variance component estimation: ANOVA/Henderson, REML/AI-REML, Gibbs sampling
- Validating genetic evaluations

### Out of scope — deferred to companion volumes

These are **deliberately excluded**. Do not add them to chapters, and do not expand a passing
mention into a section. Reference the companion volume instead.

1. **Genomic selection** — SNP data, the genomic relationship matrix **G**, GBLUP, SNP-BLUP,
   single-step (ssGBLUP), APY, the Bayesian alphabet, genomic dominance, and breed origin of
   alleles. A separate genomics book will cover these. Where a pedigree-based topic has a genomic
   successor (metafounder estimation, genomic CCPS), state that it exists in one or two sentences
   and point forward — do not teach it.

2. **Large-scale computation** — sparse matrix storage and factorization, parallel and GPU
   solving, and software internals. A separate computational book will cover these. The single
   exception is one chapter in this book that exposes students to *why* direct inversion fails at
   scale and what solvers actually do (Jacobi, Gauss–Seidel, PCG, iteration on data). That chapter
   stays conceptual with one small worked example.

3. **Selection index theory and breeding program design** — response to selection, economic
   indices, mating plans, optimal contributions. The one exception is the equivalence of the
   selection index and BLUP, which belongs as a section in the animal model chapter because it
   explains why BLUP works.

## Pedagogical rules

Chapters must follow this pattern. It is the reason the book exists.

- **Numbers before symbols.** Every result is presented as **Instance → Pattern → Statement**:
  the operation is performed on actual numbers, then a few lines say what would and would not
  change on other data, and only then is the general form written down. **No general form
  precedes the worked instance that earns it**, and a Key Equation box is never the reader's first
  sight of its own content. `plans/pedagogical_order.md` is the standard, including the cases that
  are exempt — conventions, model statements, and distributional assumptions are *declared*, not
  discovered.
- **Start small.** Open with a toy dataset the reader can solve with a calculator. Show the
  actual numbers in **X**, **Z**, **A⁻¹**, and the MME.
- **Show every step.** Every symbol's first appearance is a **name given to something already on
  the page**, never a placeholder for something to come. State the dimensions of every matrix.
  No step is "obvious."
- **Hand first, then R.** Solve by hand, then reproduce the identical answer in R with explicit
  matrix code, then show the package call (`lme4`, `sommer`, `pedigreemm`, `nadiv`, `MCMCglmm`)
  that does it in one line. The hand answer and the package answer must match.
- **Code visible.** R chunks are **shown by default** — `code-fold` is off book-wide. The code is
  teaching material a student reads, retypes, and runs, not an appendix to the maths. This is one
  of the core reasons the book exists, and a chapter whose R a first-year student cannot follow
  line by line has failed regardless of how correct it is. What that requires:
  - **One idea per chunk.** A chunk that builds `X`, solves, and plots is three chunks. Put the
    prose that explains a step *above* the chunk that performs it, not after.
  - **Name objects after the book's notation.** `X`, `y`, `XtX`, `b_hat`, `Ainv`, `alpha` — never
    `m1`, `tmp`, `res2`, `df`. A student should be able to point at a line of R and at a symbol in
    the equation above it and see the same thing.
  - **Every chunk prints the number the hand calculation produced**, so the two can be compared on
    screen without scrolling. That comparison is the point of the chunk.
  - **Comment the modelling step, not the R syntax.** `# X'X is the table of counts` earns its
    place; `# multiply the two matrices` does not.
  - **Prefer the explicit form over the clever one.** Write the three separate lines a student
    would write. No dense one-liners, no nested calls three deep, no pipe chains that hide a step
    the chapter is teaching. Idiomatic shortcuts (`crossprod`, `solve(A, b)`) are taught
    deliberately, in an **In R** callout, after the explicit form has been shown.
  - **Base R and the chapter's named packages only.** Introducing a dependency to save two lines
    costs a student more than it saves.
  - `code-fold: true` on an individual chunk is allowed **only** for incidental code that teaches
    nothing — the cosmetic details of a figure, say — and carries a one-line comment saying why.
- **Key terms get a box, not bold text.** Any word the reader will be held to later — *singular*,
  *rank*, *estimable*, *positive definite*, *conformable*, *linear combination* — is introduced in
  a **Definition** callout, placed immediately *after* the term has been met in context. Each box
  says what the term is and, under a bold `**Why it matters.**` lead, what goes wrong without it
  and which chapter it returns in. A term bolded mid-paragraph cannot be found again three
  chapters later, which is exactly when a student needs it. Definition boxes sit outside the
  15-box callout cap; `plans/chapter_standards.md` §2b is the standard.
- **Exercises.** End each chapter with practice problems; solutions go in the solutions appendix.
- **Species variety.** Draw examples from dairy, beef, swine, sheep, and poultry rather than
  defaulting to dairy for everything.

## Choosing example traits — read before writing any example

A trait carries a model with it. If a chapter demonstrates a trait with a well-known extra
component, students learn a model they must later unlearn. **Weaning weight in a basic BLUP
chapter is wrong** — it belongs to maternal effects, and using it earlier teaches an
underspecified model for the book's own headline maternal example.

Before writing an example, check that the trait is not reserved by a later chapter, and that it
carries no structure the current chapter has not yet taught:

| Trait | Reserved by |
|---|---|
| Beef weaning weight | Maternal effects |
| Sow litter size (repeated parities) | Repeatability |
| Piglet birth/weaning weight in a litter | Common environmental effects |
| Dairy test-day milk yield | Longitudinal / random regression |
| Group-housed laying hens | Social interaction / IGE |
| Calving ease, stillbirth | Threshold models |
| Beef cow longevity, stayability | Survival analysis |
| Purebred vs. crossbred performance | Crossbred evaluation / CCPS |

**Prefer a weight over a rate.** Use slaughter weight, live weight at a fixed age, or yearling
weight rather than average daily gain. A student learning the model should be able to picture the
number: 118 kg is concrete, 0.87 kg/d is a ratio they must decode before they can judge whether an
EBV is sensible. Reserve rates and ratios for chapters where the rate itself is the subject.

For a chapter teaching the plain additive model, choose a trait that is measured once per animal,
on the animal itself, with no maternal or competitive component at the age recorded — for example
ultrasound backfat or loin depth in pigs. Prefer a moderately-to-highly heritable trait for hand
calculations: at h² = 0.45, α ≈ 1.2 and the EBVs separate visibly, whereas at h² = 0.10, α = 9 and
every solution shrinks to near zero, which makes a worked example look broken.

**Reuse a dataset across chapters when the comparison is the lesson** — the same records analyzed
as an animal model and then a sire model, or by ANOVA then REML then Gibbs, teach more than three
unrelated datasets would.

## Chapter structure and callouts

Two standards, and they cover different things. `plans/pedagogical_order.md` is the **order** —
Instance → Pattern → Statement, and it governs wherever the two overlap.
`plans/chapter_standards.md` is the **structure**: the required chapter beats, the nine teaching
callouts with their fixed titles and per-chapter budgets, and the **three math tiers**. Start a
chapter by copying `templates/chapter-template.qmd`, whose section order already encodes both.

The math tiers matter most. Every displayed equation is Tier 1 (**Key Equation** — boxed, named,
labelled `{#eq-...}`, 1-3 per chapter, memorise it), Tier 2 (ordinary display math in the flow,
follow it), or Tier 3 (**Derivation** — collapsed grey callout, optional). **An equation label
means Tier 1 and nothing else carries one.**

The tiers appear in the order **2 → 1 → 3**: the reader works the arithmetic in literal numbers,
then meets the boxed general form that names what they just did, then may open a collapsed
derivation showing it holds for every dataset. A reader who skips the derivation of BLUP has
still met the MME twice — once solved, once boxed.

Callout colours encode what the reader should do with a box. They are deliberately not the manim
role palette (`plans/manim_visual_standards.md`), which encodes what a quantity is inside the
math. Do not unify them.

## Datasets

Chapter specs in `CHAPTERS.md` describe datasets **generically** (species, trait, approximate
size, structure) — no actual values. Datasets are built later as a separate pass: the generating
script goes in `data-raw/`, its CSV output in `data/`. Do not inline a dataset into a `.qmd`.

## Structure

`CHAPTERS.md` is the working outline and the single source of truth for the chapter list —
objectives, section headings, datasets, and R packages per chapter. `_quarto.yml` must be kept in
sync with it.

Content lives in `chapters/` and `appendices/` as `.qmd`. Datasets go in `data/` as CSV, with the
script that generated each one in `data-raw/`.

## Working in this repo

```bash
quarto render                              # build the whole book to _book/
quarto preview                             # live preview
quarto render chapters/01-matrix-algebra.qmd   # single chapter
Rscript setup.R                            # install R dependencies
```

`execute: freeze: auto` is set, so a chapter is only re-executed when it changes. Deletions in
`_freeze/` force a re-run.

## Conventions

- Notation follows Mrode where it is standard (**y**, **X**, **b**, **Z**, **a**, **e**, **A**,
  **G₀**, **R**). The notation appendix is authoritative; check it before introducing a new symbol.
- Cite with `[@key]` against `references.bib`. Do not invent citations — verify a reference exists
  before adding it.
- Chapter files are numbered `NN-slug.qmd`, appendices `X-slug.qmd`.



