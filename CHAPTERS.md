# Chapter Outline

Working outline for *Animal Models: A Graduate Introduction to Mixed Model Equations in Breeding
and Genetics*. This file is the single source of truth for the chapter list; `_quarto.yml` is kept
in sync with it.

Scope decisions (genomics and large-scale computation deferred to companion volumes, trait
reservation rules, dataset conventions) are recorded in `CLAUDE.md`.

Datasets are described **generically** here — species, trait, approximate size, required
structure. Actual values are built later: generating script in `data-raw/`, CSV output in `data/`.

**Status:** structure agreed; no chapters drafted.

---

# Part I — Background

## Chapter 1 — Matrix Algebra for Animal Breeders

**Purpose:** Only the linear algebra used later in this book, with a map of what is needed where.

**Prerequisites:** none

**Objectives**
1. Perform transpose, addition, multiplication, and inversion by hand on matrices up to 4×4, and
   verify each result in R
2. Diagnose a singular matrix, explain why breeding models routinely produce one, and use a
   generalized inverse
3. Apply the Kronecker and Hadamard products and name the chapter where each is used
4. Decompose a covariance matrix by Cholesky and by eigenvalues, and state what each
   decomposition is for
5. Derive the variance of a linear combination, Var(**Ay**) = **A**Var(**y**)**A**′, and use it to
   assemble **V** = **ZGZ**′ + **R**

**Sections**
```
1.1   Why linear algebra?
1.2   Matrices, vectors, and scalars
1.3   Transpose
1.4   Addition, subtraction, and scalar multiplication
1.5   Matrix multiplication
1.6   Special matrices
1.7   Why matrices: one model, many animals
1.8   Rank, singularity, and the determinant
1.9   Inversion, solving, and partitioned matrices
1.10  Generalized inverses
1.11  Kronecker product, Hadamard product, and direct sum
1.12  Cholesky decomposition
1.13  Eigenvalues and eigenvectors
1.14  Quadratic forms, traces, and matrix derivatives
1.15  Variances of linear combinations: building V
1.16  Which section do you need for which chapter?
1.17  Key equations
1.18  Exercises
```

**Toy dataset:** none — worked matrices no larger than 4×4 throughout. Three running examples
carry the chapter: four lambs in two flocks (sheep yearling weight); a two-trait G/R/P set; and a
decomposable 2×2 covariance matrix.
**Scale-up:** none.
**Packages:** base, Matrix (plus `MASS::ginv`, which ships with R)
**Exercises:** 6
**Notes:** §1.14 exists to serve Ch 21 (REML derivatives); say so explicitly. Mention SVD in one
paragraph in §1.13 and point to the computational volume — do not develop it. §1.16 is a table
mapping sections to the chapters that need them, so readers can skip intelligently.

§1.1 is background: what linear algebra *is*, why a breeder needs it inside and outside this book
(selection index, general linear models, multivariate analysis, genomics), and the core vocabulary
— matrix, vector, scalar, linear combination — introduced on a plain 4 × 2 table of measurements
that carries no model. The linear model `y = Xb + e` is deliberately **not** the chapter's opening
example: it arrives in §1.7, after the reader has met matrices, the transpose, addition and
multiplication — because `X'X` cannot be explained before multiplication exists.

**The section order is a dependency order.** §1.2–§1.5 must be read in sequence: the transpose
needs only a matrix, addition needs only position, multiplication needs the transpose, and the
reversal rule `(AB)' = B'A'` needs multiplication — which is why it sits in §1.5 and not with the
transpose. Special matrices come *after* the operations (§1.6) because most of them are defined by
how they behave under those operations, not by how they look. **No operation is used in the text
or in an R chunk before the section that teaches it**; the single deliberate exception is
`try(solve())` in §1.8, used to show what R does when asked to invert a singular matrix, and
flagged as a preview in the chunk.

Two changes from the original outline, made per `plans/chapter_01_linear_algebra.md` §9: the old
§1.3 is **split** into transpose/addition (§1.3) and multiplication (§1.4), because multiplication
is the hardest operation in the chapter and `X′X`-as-counts deserves its own heading; and §1.12,
**variances of linear combinations**, is **new** — `Var(Ay) = A Var(y) A′` is used in almost every
later chapter and was taught in none of them. Objectives were revised to match: the spec's old
objectives 4 and 5 are merged into objective 4, freeing a slot for the variance rule.

**Documented exceptions** for this chapter, all recorded in the chapter plan:
1. **8 manim clips rather than 5** — one per section, because this is a reference chapter entered
   at any point rather than read straight through.
2. **Three skeleton beats absent** (`plans/chapter_standards.md` §3): the toy dataset (Example A
   serves the role; matrices are inline, no CSV), "the same model in R" as a standalone beat (R is
   interleaved section by section instead), and scale-up (the one exception is a timing
   comparison in §1.6).
3. **Instance → Pattern → Statement runs once per section, not once per chapter** — eleven small
   results rather than one large one.
4. **Short-instance allowance for a reference chapter** (`plans/pedagogical_order.md` §8): each
   section still opens with its instance, but stays short enough that the rule is visible on the
   same screen as the numbers that earned it.
5. **9 Definition callouts rather than the 0–8 budget** (`plans/chapter_standards.md` §2b). This
   chapter establishes the vocabulary the rest of the book is held to — matrix/vector/scalar,
   linear combination, conformable, linear dependence and rank, singular, inverse, generalized
   inverse, estimable, positive definite. Definition boxes sit outside the 15-box callout cap,
   which this chapter meets exactly.

---

## Chapter 2 — Linear Models

**Purpose:** Fixed effects only. Build **X**, solve the normal equations, confront non-full-rank.

**Prerequisites:** Ch 1

**Objectives**
1. Write a linear model in matrix form and build **X** for a given design
2. Compare parameterizations and show they give identical fitted values
3. Solve (X'X)⁻X'y by hand and reproduce it with `lm()`
4. Explain estimability and why individual solutions need not be unique
5. Interpret residuals and estimate σ²e

**Sections**
```
2.1  The general linear model in matrix form
2.2  Building X: covariates, factors, interactions
2.3  Parameterizations (cell means, reference level, sum-to-zero)
2.4  The normal equations and the non-full-rank problem
2.5  Generalized inverse solutions and estimable functions
2.6  Solving by hand
2.7  The same fit with lm()
2.8  Residuals and the residual variance
2.9  Exercises
```

**Toy dataset:** ~9 pigs, live weight at a fixed age, 3 diet groups. No pedigree, no random
effects. Hand-solvable.
**Scale-up:** ~500 records, diet × sex.
**Packages:** base, Matrix
**Exercises:** 4
**Notes:** §2.3 is the payoff — students must see that different solution vectors give the same
predictions. This is where the generalized inverse stops being abstract.

---

## Chapter 3 — Mixed Models Without Relationships

**Purpose:** Introduce **Z** and random effects with no genetics attached. **G = I**.

**Prerequisites:** Ch 2

**Objectives**
1. Distinguish fixed from random effects and state when each is appropriate
2. Build **Z** for a random classification effect
3. Assemble and solve the MME with a variance ratio α
4. Contrast BLUE of fixed effects with BLUP of random effects, and explain shrinkage
5. Reproduce the hand solution with `lmer()`

**Sections**
```
3.1  When should an effect be random?
3.2  The mixed model y = Xb + Zu + e
3.3  Building Z for a pen effect
3.4  Variance structure: G = Iσ²pen, R = Iσ²e
3.5  The mixed model equations
3.6  Solving by hand
3.7  Shrinkage: why BLUP pulls toward the mean
3.8  The same model with lmer()
3.9  Exercises
```

**Toy dataset:** ~12 pigs, live weight, 4 pens, one fixed effect (sex). **G = I** — deliberately
no relationships.
**Scale-up:** ~800 pigs across ~40 pens.
**Packages:** Matrix, lme4
**Exercises:** 4
**Notes:** A pen effect is used rather than a sire effect so that "random effect" and "relationship
matrix" stay decoupled until Ch 4 joins them. Forward-reference Ch 13: here the pen is a nuisance;
there the pen-mates carry genetics.

---

## Chapter 4 — Pedigrees and Relationship Matrices

**Purpose:** **A** and **A⁻¹** — the object that makes the animal model work.

**Prerequisites:** Ch 1

**Objectives**
1. Store, sort, and renumber a pedigree correctly
2. Build **A** by the tabular method by hand
3. Compute inbreeding coefficients and interpret the diagonal of **A**
4. Build **A⁻¹** directly by Henderson's rules, with and without inbreeding
5. Reproduce both in R

**Sections**
```
4.1   Pedigree structure, storage, and common errors
4.2   Sorting: parents before progeny
4.3   Renumbering
4.4   Identity by descent vs identity by state
4.5   Building A by the tabular method
4.6   Inbreeding and the diagonal of A
4.7   Henderson's rules for A⁻¹ ignoring inbreeding
4.8   A⁻¹ accounting for inbreeding
4.9   In R: pedigreemm and nadiv
4.10  Exercises
```

**Toy dataset:** 10-animal pedigree, 3 generations, containing at least one inbred animal and one
animal with a single unknown parent. No trait.
**Scale-up:** ~5,000-animal pedigree; check sorting and examine the inbreeding distribution.
**Packages:** pedigreemm, nadiv, Matrix
**Exercises:** 5
**Notes:** The direct A⁻¹ rules are the single most surprising result in the book for most students
— that you never need to form and invert **A**. Give that its own emphasis.

---

## Chapter 5 — Data Preparation, Contemporary Groups, and Connectedness

**Purpose:** What goes wrong before a model is ever fitted. This is where real analyses fail.

**Prerequisites:** Ch 2, Ch 4

**Objectives**
1. Define contemporary groups and justify a definition for a given trait
2. Diagnose and handle small and singleton contemporary groups
3. Assess genetic connectedness and explain the consequences of disconnection
4. Detect and resolve pedigree errors
5. Apply an editing pipeline and document its decisions reproducibly

**Sections**
```
5.1  Why editing decisions change EBVs
5.2  Defining contemporary groups: herd, year, season, management
5.3  Minimum group size; fixed vs random contemporary group
5.4  Connectedness: what it is, how to measure it, what disconnection does
5.5  Pedigree errors: cycles, sex inconsistencies, impossible birth dates
5.6  Outliers and biologically impossible records
5.7  Building a reproducible editing script
5.8  Exercises
```

**Toy dataset:** ~25 beef records across 4 herds, deliberately containing a singleton contemporary
group, one disconnected herd, and one pedigree error.
**Scale-up:** ~20,000 multi-herd records run through a full editing pipeline.
**Packages:** tidyverse, pedigreemm
**Exercises:** 4
**Notes:** Not in Mrode. Justify its place: the modelling chapters all assume clean data, and no
student has ever been handed clean data.

---

# Part II — Core Animal Models

## Chapter 6 — The Animal Model

**Purpose:** The central chapter. Solve the full MME with **A⁻¹**, then interpret what came out.

**Prerequisites:** Ch 2 (X), Ch 3 (Z), Ch 4 (A⁻¹)

**Objectives**
1. Build and solve the animal-model MME by hand for a small pedigree
2. Explain the role of α = σ²e/σ²a and what happens as it grows
3. Obtain PEV, accuracy, and reliability from the inverse of the LHS
4. Decompose an EBV into parent average, yield deviation, and progeny contribution
5. Explain BLUP as a selection index with simultaneously estimated fixed effects

**Sections**
```
6.1  From Ch 3 to the animal model: swapping I for A
6.2  Setting up the MME (X, Z, A⁻¹, α)
6.3  Solving by hand
6.4  Interpreting solutions; the base population
6.5  PEV, accuracy, and reliability
6.6  Decomposing the EBV: PA + YD + PC
6.7  The same model in R (matrix code, then pedigreemm/sommer)
6.8  BLUP and the selection index
6.9  Exercises
```

**Toy dataset:** pigs, ultrasound backfat depth at off-test. ~6 animals, 2 sires, 1 contemporary
group. Must include at least one animal with both a record and recorded progeny (so §6.6 has a PC
term) and one animal with no record of its own.
**Scale-up:** same trait, ~2,000 animals across several contemporary groups.
**Packages:** Matrix, pedigreemm, sommer
**Exercises:** 4 (one adds an animal with no record; one varies α)
**Notes:** Backfat is chosen because it is measured once, on the animal, by ultrasound — no
maternal component at off-test age, not repeated, not competitive. At h² ≈ 0.45, α ≈ 1.2, so the
hand arithmetic stays clean and the EBVs separate visibly. Add a short sidebar in §6.2 on where
the variance ratio comes from, pointing to Part VII, so readers are not left wondering for fifteen
chapters.

---

## Chapter 7 — Equivalent and Reduced Models

**Purpose:** Sire, sire–MGS, and reduced animal models, framed as data reduction and model
equivalence rather than as a step backward.

**Prerequisites:** Ch 6

**Objectives**
1. Derive the sire model and state the assumptions that make it an approximation
2. Relate sire EBVs to animal-model EBVs computed on the same data
3. Build the sire–maternal grandsire relationship matrix and its inverse
4. Set up a reduced animal model and back-solve for non-parents
5. Judge when a reduced model is worth the information it discards

**Sections**
```
7.1  Why reduce? Historical and computational motives
7.2  The sire model
7.3  Comparing sire and animal model solutions on the same data
7.4  The sire–maternal grandsire model
7.5  A⁻¹ rules for sire and sire–MGS matrices
7.6  The reduced animal model
7.7  Back-solving for non-parent animals
7.8  Equivalent models: a general statement
7.9  Exercises
```

**Toy dataset:** the Ch 6 backfat data, reanalyzed. The comparison is the lesson.
**Scale-up:** the Ch 6 scale-up file.
**Packages:** Matrix, pedigreemm
**Exercises:** 4
**Notes:** Deliberate data reuse — students see the same animals ranked by three models and can
attribute every difference to the model rather than the data.

---

## Chapter 8 — Random Environmental Effects

**Purpose:** Repeatability and common environmental effects — a second random effect that is not
genetic.

**Prerequisites:** Ch 6

**Objectives**
1. Distinguish permanent from temporary environmental effects
2. Define repeatability and state its relationship to heritability
3. Set up and solve a repeatability model with multiple records per animal
4. Model a common environmental (litter) effect and explain its confounding with relationship
5. Interpret variance ratios when several random effects compete for the same variance

**Sections**
```
8.1  Repeated records: what changes
8.2  Permanent environmental effects
8.3  Repeatability and its bound on heritability
8.4  The repeatability model MME
8.5  Solving by hand
8.6  Common environmental effects: the litter
8.7  Why c² and a² are hard to separate among full sibs
8.8  In R
8.9  Exercises
```

**Toy dataset:** two small sets — (a) ~5 sows with 2–3 parities each, litter size; (b) ~12 piglets
in 4 litters, birth weight.
**Scale-up:** ~3,000 sow-parity records; ~4,000 piglets in ~500 litters.
**Packages:** Matrix, sommer, lme4
**Exercises:** 5
**Notes:** §8.7 matters more than it looks — it is the first time students meet a confounding that
no amount of data resolves, and it sets up Ch 16 and Ch 17.

---

## Chapter 9 — Genetic Groups

**Purpose:** Unknown parent groups, and an honest statement of what they get wrong.

**Prerequisites:** Ch 4, Ch 6

**Objectives**
1. Explain what the base population assumption means and when it fails
2. Decide how to form unknown parent groups for a given population
3. Set up and solve an animal model with groups
4. Interpret group solutions and their effect on estimated genetic trend
5. State the limitations of UPG and what metafounders change

**Sections**
```
9.1  The base population assumption
9.2  When unknown parents are not exchangeable: imports, era, selection path
9.3  Forming groups: how many, on what criteria
9.4  The MME with groups
9.5  Solving by hand
9.6  Group solutions and genetic trend
9.7  Too many groups: what goes wrong
9.8  What UPG assume, and how metafounders relax it
9.9  Exercises
```

**Toy dataset:** ~10 beef animals, yearling weight, unknown dams split across 2 eras.
**Scale-up:** ~10,000 animals with era- and origin-based groups.
**Packages:** Matrix, nadiv
**Exercises:** 4
**Notes:** §9.8 is short and conceptual — state that UPG assume base groups are unrelated and
non-inbred, that metafounders relax this, and that estimating Γ requires marker data. Develop
metafounders properly in Ch 18; forward-reference it here.

---

## Chapter 10 — Maternal Effects Models

**Purpose:** Two correlated genetic effects on one phenotype.

**Prerequisites:** Ch 6, Ch 8

**Objectives**
1. Separate direct and maternal genetic contributions to a phenotype
2. Build the MME with correlated direct and maternal genetic effects
3. Include a maternal permanent environmental effect and justify it
4. Interpret the direct–maternal genetic correlation and the controversy surrounding it
5. Compute total maternal and total genetic merit for selection

**Sections**
```
10.1  Traits where the dam's genes affect the offspring's phenotype
10.2  The maternal effects model
10.3  Covariance structure with a direct–maternal covariance
10.4  Maternal permanent environment
10.5  Setting up and solving by hand
10.6  The negative direct–maternal correlation: real, or artifact?
10.7  Total maternal value and combined selection criteria
10.8  In R
10.9  Exercises
```

**Toy dataset:** ~8 beef calves, weaning weight, with dams having their own records where possible.
**Scale-up:** ~5,000 weaning weight records with full dam pedigree.
**Packages:** Matrix, sommer
**Exercises:** 5
**Notes:** Weaning weight is reserved for this chapter and must not appear earlier (see
`CLAUDE.md`). §10.6 should be genuinely two-sided — the negative estimate is partly real and partly
a data-structure artifact, and students should see both arguments.

---

# Part III — Advanced Model Structures

## Chapter 11 — Multivariate Models

**Purpose:** Several traits at once; the Kronecker product earns its keep.

**Prerequisites:** Ch 6, Ch 1 (§1.7)

**Objectives**
1. Write the multivariate MME using the Kronecker product
2. Solve a two-trait model by hand with equal design matrices
3. Handle missing records and unequal design matrices
4. Explain how genetic correlation moves information between traits
5. Describe how dimension reduction makes many-trait models tractable

**Sections**
```
11.1   Why analyze traits jointly
11.2   The multivariate model and G₀ ⊗ A
11.3   Equal design matrices, no missing records
11.4   Solving a two-trait model by hand
11.5   Missing records
11.6   Unequal design matrices
11.7   Where the gain comes from: correlation and differential recording
11.8   Dimension reduction: canonical, Cholesky, factor analytic, reduced-rank PC
11.9   In R
11.10  Exercises
```

**Toy dataset:** ~6 sheep, yearling weight and fleece weight, with one animal missing fleece.
**Scale-up:** ~3,000 sheep, 3 traits (yearling weight, fleece weight, fiber diameter).
**Packages:** Matrix, sommer
**Exercises:** 5
**Notes:** Sheep are used to avoid brushing against dairy milk yield, which Ch 12 owns, and to get
a third species into the book. §11.8 is a survey with references, not derivations — the algorithms
belong to the computational volume.

---

## Chapter 12 — Longitudinal Data and Random Regression

**Purpose:** Traits measured along a trajectory.

**Prerequisites:** Ch 8, Ch 11

**Objectives**
1. Distinguish fixed from random regression and state what each can model
2. Build a covariate matrix of Legendre polynomials
3. Set up and solve a random regression model
4. Recover the covariance function and per-time-point variances from RR coefficients
5. Fit and interpret a reaction norm as a special case

**Sections**
```
12.1   Repeated records along a trajectory
12.2   Fixed regression models
12.3   Legendre polynomials as covariates
12.4   The random regression model
12.5   Solving a small RR model
12.6   From RR coefficients to variances and EBVs at any point
12.7   Covariance functions and their equivalence to RR
12.8   Splines as an alternative basis
12.9   Reaction norms: environment as the trajectory
12.10  Choosing an order of fit
12.11  In R
12.12  Exercises
```

**Toy dataset:** ~4 cows with 4–5 test-day milk records each.
**Scale-up:** ~2,000 cows with monthly test days across a lactation.
**Packages:** Matrix, sommer, orthopolynom
**Exercises:** 5
**Notes:** The hard part for students is that the random effects are now *coefficients*, not
breeding values — §12.6 is where that clicks and deserves the most space.

---

## Chapter 13 — Social Interaction Models

**Purpose:** An animal's phenotype depends on its group-mates' genes.

**Prerequisites:** Ch 3, Ch 6, Ch 11

**Objectives**
1. Explain how a group-mate's genes become part of an animal's phenotype
2. Build the direct and indirect genetic effect design matrices
3. Define the total breeding value and show why it, not the direct effect, is the selection criterion
4. Explain how group size and composition affect identifiability
5. Recognize when indirect genetic effects and a random group effect are confounded

**Sections**
```
13.1   Competition and cooperation as heritable effects
13.2   The model with direct and indirect genetic effects
13.3   Building Z for group-mates
13.4   Covariance structure and the direct–indirect correlation
13.5   Solving a small example by hand
13.6   Total breeding value
13.7   Group composition and identifiability
13.8   Group effect vs indirect effect: the confounding problem
13.9   In R
13.10  Exercises
```

**Toy dataset:** ~12 laying hens in 4 pens of 3, egg number.
**Scale-up:** ~2,000 hens in group cages.
**Packages:** Matrix, sommer
**Exercises:** 4
**Notes:** Egg number rather than mortality — the canonical poultry IGE literature is on
cannibalism and feather pecking, but a mortality trait would collide with Ch 15 and would be a
survival trait analyzed with a non-survival model. Describe feather pecking as the *mechanism*
while keeping the trait a clean count. Cross-reference Ch 3 explicitly: the pen was a nuisance
effect there, and the pen-mates carry genetics here. Verify the layer IGE citations when drafting.

---

# Part IV — Categorical and Time-to-Event Traits

## Chapter 14 — Threshold Models for Categorical Traits

**Purpose:** Binary and ordered categorical traits in one chapter — same model, more thresholds.

**Prerequisites:** Ch 6, Ch 11

**Objectives**
1. Explain the liability concept and the threshold model
2. Set up a threshold model for a binary trait and solve it iteratively
3. Extend to more than two ordered categories with multiple thresholds
4. Convert heritability between the observed and underlying scales
5. Fit a joint model for a categorical and a continuous trait

**Sections**
```
14.1   Why a linear model on a 0/1 trait misbehaves
14.2   Liability and the threshold concept
14.3   The binary threshold model
14.4   Iterative solution
14.5   More than two categories: multiple thresholds
14.6   Heritability on the observed vs underlying scale
14.7   Extreme category proportions and non-convergence
14.8   Joint analysis of a categorical and a continuous trait
14.9   In R
14.10  Exercises
```

**Toy dataset:** ~10 beef calving records — stillbirth (0/1) for the binary case and calving ease
(1–4) for the ordinal case, from the same animals.
**Scale-up:** ~8,000 calving records with contemporary group and calf sex.
**Packages:** Matrix, MCMCglmm, sommer
**Exercises:** 5
**Notes:** §14.7 is the practical section — extreme incidence and small contemporary groups are why
these models fail in practice, and students should see it before they meet it.

---

## Chapter 15 — Survival Analysis

**Purpose:** Time-to-event data and censoring.

**Prerequisites:** Ch 6, Ch 14

**Objectives**
1. Define censoring and explain why it breaks a standard linear model
2. Distinguish true from functional longevity
3. Contrast a binary stayability model with a true time-to-event analysis
4. Fit a proportional hazards model containing a genetic effect
5. Interpret survival EBVs and relate them to economic merit

**Sections**
```
15.1   Time-to-event data in livestock
15.2   Censoring: right, left, interval
15.3   True vs functional longevity
15.4   Stayability as a binary threshold trait, and what it discards
15.5   Non-parametric estimation: Kaplan–Meier
15.6   Proportional hazards with a genetic effect
15.7   Linear and random regression approximations
15.8   Interpreting survival EBVs
15.9   In R
15.10  Exercises
```

**Toy dataset:** ~10 beef cows, days from first calving to removal, with several still in the herd
(censored).
**Scale-up:** ~6,000 beef cows with removal dates and a censoring indicator.
**Packages:** survival, coxme, Matrix
**Exercises:** 4
**Notes:** §15.4 is the deliberate link back to Ch 14 — stayability to six years is normally run as
a binary threshold trait, so opening with "here is what that throws away" motivates the whole
chapter. Beef rather than swine both for economic weight and for species balance.

---

# Part V — Non-additive Genetic Effects

## Chapter 16 — Dominance Models

**Purpose:** Genotypic value, not just breeding value — and the one place non-additive effects
change a decision.

**Prerequisites:** Ch 4, Ch 6

**Objectives**
1. Distinguish breeding value from genotypic value
2. Build the dominance relationship matrix **D** from a pedigree
3. Set up and solve an animal model with additive and dominance effects
4. Explain why dominance and common environment confound
5. Use predicted dominance for mate allocation

**Sections**
```
16.1   Breeding value vs total genetic merit
16.2   Dominance deviations
16.3   The dominance relationship matrix from pedigree
16.4   The additive + dominance MME
16.5   Solving by hand
16.6   Confounding with common environment and full-sib structure
16.7   Data requirements: why full sibs are essential
16.8   Mate allocation using predicted dominance
16.9   In R
16.10  Exercises
```

**Toy dataset:** ~12 broilers in a full-sib / half-sib design, body weight.
**Scale-up:** ~4,000 broilers with substantial full-sib structure.
**Packages:** Matrix, nadiv
**Exercises:** 4
**Notes:** §16.8 is what keeps this chapter practical rather than theoretical — without mate
allocation, dominance is an academic exercise. Flag that **D** from pedigree assumes non-inbred
animals; that assumption leads directly into Ch 17.

---

## Chapter 17 — Epistasis Models

**Purpose:** Capstone to Part V, answering the question the whole book raises: why is everything
else additive?

**Prerequisites:** Ch 1 (§1.7), Ch 16

**Objectives**
1. Define additive×additive, additive×dominance, and dominance×dominance variance
2. Build epistatic relationship matrices as Hadamard products of **A** and **D**
3. Set up a model containing an epistatic term
4. Explain why epistatic variance is nearly unidentifiable from pedigree data
5. Justify the additive model used throughout the rest of the book

**Sections**
```
17.1  Interaction at the level of genes vs at the level of variance
17.2  Epistatic relationship matrices: A#A, A#D, D#D
17.3  The non-inbred assumption and where it fails
17.4  Setting up the model
17.5  A worked A#A on a small pedigree
17.6  Why it cannot be estimated
17.7  The evidence: mainly additive variance in practice
17.8  What this justifies about the rest of the book
17.9  Exercises
```

**Toy dataset:** reuse the Ch 16 broiler pedigree; build **A#A** on the same animals.
**Scale-up:** none — the point of §17.6 is that scale does not rescue it.
**Packages:** Matrix, nadiv
**Exercises:** 3
**Notes:** Deliberately short. §17.6 covers three distinct problems: near-collinearity of **A#A**
with **A**, confounding with c², and sampling variance. Anchor citations, already verified —
Henderson (1985) for the Hadamard construction; Hill, Goddard & Visscher (2008) and Hivert et al.
(2021) for the empirical case that epistatic variance is not estimable at realistic sample sizes.
Under inbreeding the theory needs Jacquard's condensed identity coefficients; state this and stop.
If this chapter still reads thin when drafted, collapse it into a closing section of Ch 16.

---

# Part VI — Multibreed and Crossbred Evaluation

## Chapter 18 — Multibreed Models

**Purpose:** More than one breed in a single evaluation.

**Prerequisites:** Ch 9, Ch 11

**Objectives**
1. Explain why one **A** and one variance are wrong across breeds
2. Model breed composition and heterosis as covariates
3. Define segregation variance and state when it matters
4. Build a breed-specific covariance structure
5. Explain metafounders as a generalization of unknown parent groups

**Sections**
```
18.1  Why multibreed is not "add breed as a fixed effect"
18.2  Breed proportion and heterosis coefficients
18.3  Breed-specific additive variance
18.4  Segregation variance
18.5  Splitting breeding values by breed of origin
18.6  Metafounders: the base populations are related
18.7  Γ and its interpretation
18.8  In R
18.9  Exercises
```

**Toy dataset:** ~10 animals — Angus, Simmental, and F1 — yearling weight.
**Scale-up:** ~8,000 multibreed beef records.
**Packages:** Matrix, nadiv
**Exercises:** 4
**Notes:** This is where metafounders get developed properly (Ch 9 only introduces them), because
Γ has a concrete breed-level interpretation here. Be explicit in §18.7 that estimating Γ requires
marker data, and point to the genomics volume rather than teaching it. Yearling weight is used
because maternal effects have largely dissipated by that age.

---

## Chapter 19 — Crossbred Evaluation and CCPS

**Purpose:** Selecting purebreds for crossbred performance.

**Prerequisites:** Ch 11, Ch 18

**Objectives**
1. Explain why purebred performance predicts crossbred performance imperfectly
2. Define the purebred–crossbred genetic correlation r_pc and its consequences
3. Set up purebred and crossbred performance as two correlated traits
4. Judge when crossbred data is worth collecting
5. Describe how genomic breed-origin methods extend this

**Sections**
```
19.1   The crossbred performance problem
19.2   Why r_pc < 1: G×E, dominance, differing allele frequencies
19.3   The two-trait formulation
19.4   Setting up the MME
19.5   Solving a small example
19.6   Response under CCPS vs purebred selection
19.7   Practical design: how much crossbred data, and on whom
19.8   Genomic breed-origin-of-alleles methods
19.9   In R
19.10  Exercises
```

**Toy dataset:** ~10 pigs, purebred and crossbred slaughter weight treated as two traits.
**Scale-up:** ~5,000 purebred and ~5,000 crossbred slaughter weight records.
**Packages:** Matrix, sommer
**Exercises:** 4
**Notes:** The classical CCPS formulation is entirely pedigree-based — it is a correlated-trait
problem, and the chapter works without any genomic content. §19.8 is a one-page forward reference
to the genomics volume, not a section that teaches breed origin of alleles.

---

# Part VII — Variance Component Estimation

## Chapter 20 — ANOVA and Henderson's Methods

**Purpose:** Where variance components came from before REML, and why they had to be replaced.

**Prerequisites:** Ch 3, Ch 7

**Objectives**
1. Estimate variance components from a balanced half-sib design by ANOVA
2. Compute heritability and its standard error by hand
3. Describe Henderson's Methods I, II, and III and their scopes
4. Show how unbalanced data breaks the ANOVA approach
5. Explain why these methods were superseded

**Sections**
```
20.1   Variance components from expected mean squares
20.2   The balanced half-sib design
20.3   Estimating h² and its standard error by hand
20.4   Henderson's Method I
20.5   Henderson's Method II
20.6   Henderson's Method III
20.7   Unbalanced data, selection, and negative estimates
20.8   Why REML replaced these methods
20.9   In R
20.10  Exercises
```

**Toy dataset:** **the shared variance-component dataset** — a balanced half-sib design, 5 sires ×
4 progeny, live weight. Reused unchanged in Ch 21 and Ch 22.
**Scale-up:** the same design at ~100 sires, plus a deliberately unbalanced version.
**Packages:** base, lme4
**Exercises:** 4
**Notes:** Keep this chapter historical and brisk. §20.7 sets up the whole of Ch 21 — students must
see ANOVA produce a negative variance estimate with their own hands.

---

## Chapter 21 — REML

**Purpose:** The workhorse.

**Prerequisites:** Ch 20

**Objectives**
1. State the difference between ML and REML and why REML is preferred
2. Describe the EM, Newton–Raphson, and average information algorithms
3. Run AI-REML and interpret its output
4. Obtain standard errors of variance components and of heritability
5. Diagnose convergence failure in multi-trait analyses

**Sections**
```
21.1   The likelihood for a mixed model
21.2   ML bias and the REML correction
21.3   The EM algorithm
21.4   Newton–Raphson and Fisher scoring
21.5   The average information algorithm
21.6   Sampling variance and standard errors of estimates
21.7   Multi-trait convergence, the parameter space, and bending
21.8   The Chapter 20 data, by REML
21.9   In R
21.10  Exercises
```

**Toy dataset:** the Ch 20 half-sib data — compared directly against the ANOVA answer.
**Scale-up:** the unbalanced version, where ANOVA failed.
**Packages:** Matrix, sommer, lme4
**Exercises:** 4
**Notes:** §1.10 supplies the matrix derivatives. §21.5 should explain *why* averaging the observed
and expected information works so well, not just state the formula.

---

## Chapter 22 — Bayesian Estimation via Gibbs Sampling

**Purpose:** The third route to the same variance components, and the one that gives full
distributions.

**Prerequisites:** Ch 21

**Objectives**
1. State the Bayesian formulation of the animal model and its priors
2. Derive the full conditional distributions
3. Implement a Gibbs sampler for a single-trait animal model
4. Assess convergence and mixing
5. Summarize posteriors and compare them to REML point estimates

**Sections**
```
22.1   The Bayesian view of a mixed model
22.2   Priors for location and dispersion parameters
22.3   Full conditional distributions
22.4   The Gibbs sampler, step by step
22.5   Implementing it in R from scratch
22.6   Burn-in, thinning, and convergence diagnostics
22.7   Posterior summaries; credible vs confidence intervals
22.8   Extension to the multivariate model
22.9   Comparison with the Chapter 20 and 21 results
22.10  In R with MCMCglmm
22.11  Exercises
```

**Toy dataset:** the Ch 20 half-sib data once more — third method, same numbers.
**Scale-up:** the unbalanced version.
**Packages:** MCMCglmm, coda, Matrix
**Exercises:** 4
**Notes:** §22.5 — writing the sampler from scratch in ~30 lines is the point of the chapter; the
package call in §22.10 is the afterthought. §22.9 closes Part VII by putting all three methods'
estimates in one table.

---

# Part VIII — Validation and Computation

## Chapter 23 — Validating Genetic Evaluations

**Purpose:** How do you know the evaluation works?

**Prerequisites:** Ch 6, Ch 21

**Objectives**
1. Distinguish accuracy, bias, and dispersion as separate failure modes
2. Design a forward (time-split) validation
3. Apply the LR method and interpret its statistics
4. Perform cross-validation appropriately for related individuals
5. Diagnose the cause of a failed validation

**Sections**
```
23.1  What "does the evaluation work" actually means
23.2  Accuracy, bias, and dispersion
23.3  Forward validation on a birth-year cutoff
23.4  Cross-validation and relatedness between folds
23.5  The LR method
23.6  Interpreting a regression slope that is not 1
23.7  Common causes: wrong variance ratios, missing CG, selection, pedigree errors
23.8  In R
23.9  Exercises
```

**Toy dataset:** a subset small enough that the split is visible by eye — reuse the Ch 6 backfat
scale-up data with a birth-year cutoff.
**Scale-up:** the same data at full size.
**Packages:** tidyverse, Matrix, sommer
**Exercises:** 4
**Notes:** Not in Mrode, and the most current material in the book. §23.2 is the key distinction —
students conflate "accurate" with "unbiased," and the LR method exists precisely because they are
different questions.

---

## Chapter 24 — Solving the Mixed Model Equations at Scale

**Purpose:** Expose students to what production software actually does. Deliberately thin.

**Prerequisites:** Ch 6

**Objectives**
1. Explain why direct inversion is infeasible for a national evaluation
2. Describe the sparsity of the MME and of **A⁻¹**
3. Implement Jacobi and Gauss–Seidel iteration on a small system
4. Describe PCG and iteration on data conceptually
5. Explain how reliabilities are approximated when the LHS cannot be inverted

**Sections**
```
24.1   How large is a national evaluation, really?
24.2   The cost of direct inversion
24.3   Sparsity of the MME and of A⁻¹
24.4   Absorption
24.5   Jacobi iteration
24.6   Gauss–Seidel iteration
24.7   Preconditioned conjugate gradient
24.8   Iteration on data: never forming the LHS
24.9   Approximating reliabilities at scale
24.10  What this book does not cover
24.11  Exercises
```

**Toy dataset:** a 5-equation system solved by Jacobi and by Gauss–Seidel, shown iteration by
iteration.
**Scale-up:** a large simulated pedigree, used only for a timing comparison.
**Packages:** Matrix
**Exercises:** 3
**Notes:** Thin by design. The goal is that a student never again believes `solve()` is how
evaluations are run. §24.9 holds the approximate reliability methods deliberately moved out of Ch
6. §24.10 points explicitly to the computational volume.

---

# Appendices

| | Title | Contents |
|---|---|---|
| A | Notation reference | Authoritative symbol list; check before introducing any new symbol |
| B | Derivation of BLUP and the MME | Henderson's derivation; proof that b̂ is GLS and â is BLUP |
| C | Fast inbreeding computation | Meuwissen & Luo algorithm, worked |
| D | Legendre polynomials | Constructing Φ at given ages or time points |
| E | Deregression of breeding values | Procedure and worked example |
| F | R code reference | Common operations, indexed by task |
| G | Datasets | Every dataset used, with structure and provenance |
| H | Solutions to exercises | All chapters |
| I | BLUPF90 guide | Parameter files, running, reading output |

**Note:** the matrix operations appendix from the original plan is gone — that material is now
Chapter 1.

---

# Cross-cutting notes

**Trait allocation.** Reserved traits are listed in `CLAUDE.md`. In summary: weaning weight belongs
to Ch 10, litter size and litter effects to Ch 8, test-day milk to Ch 12, group-housed layers to
Ch 13, calving ease and stillbirth to Ch 14, beef longevity to Ch 15, purebred-vs-crossbred to
Ch 19.

**Deliberate dataset reuse.** Ch 7 reuses Ch 6; Ch 17 reuses Ch 16; Ch 21 and Ch 22 reuse Ch 20;
Ch 23 reuses the Ch 6 scale-up. In each case the comparison across methods is the lesson.

**Species balance.** Swine: Ch 2, 3, 6, 7, 8, 19. Beef: Ch 5, 9, 10, 14, 15, 18. Poultry: Ch 13
(layers), 16 (broilers). Sheep: Ch 11. Dairy: Ch 12.

**Open questions.**
- Ch 13: confirm egg number vs. hen body weight as the IGE trait, and gather layer IGE citations.
- Ch 20: fix the exact half-sib design once, since Ch 21 and Ch 22 both depend on it.
- Appendix I: decide whether BLUPF90 coverage belongs here or in the computational volume.
