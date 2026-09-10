# Chapter 1 — Matrix Algebra for Animal Breeders

Working plan for `chapters/01-matrix-algebra.qmd`.

Governed by: [`pedagogical_order.md`](pedagogical_order.md) (numbers before symbols) ·
[`chapter_standards.md`](chapter_standards.md) (structure, callouts, math tiers) ·
[`manim_videos.md`](manim_videos.md) (clip placement) ·
[`manim_visual_standards.md`](manim_visual_standards.md) (colour and grammar) ·
`CHAPTERS.md` (the spec this refines).

**Spec:** no dataset, worked matrices no larger than 4×4, packages `base` + `Matrix`, 6 exercises.

---

## 1. What this chapter is for

Only the linear algebra used later in this book, taught on breeding quantities wherever a
breeding quantity makes the point better than an abstract one. A student finishing this chapter
should be able to open Chapter 6, see the mixed model equations, and recognise every operation in
them.

Three rules shape every section:

- **Numbers before symbols** (`pedagogical_order.md`). Every section runs Instance → Pattern →
  Statement: the operation is performed on actual numbers first, then a few lines say what would
  and would not change on other data, and only then is the general rule written down. **No rule in
  this chapter appears before the reader has seen it happen.** This chapter is where the standard
  is set, because it is where the reader learns what to expect from every chapter after it.
- **Hand first, then R, in the same section.** Each operation is worked by hand on numbers small
  enough to check mentally, then immediately re-run in R in a **visible** chunk that prints the
  same answer. The R is not an appendix to the maths; it sits directly beneath it, and the reader
  should be able to retype it without expanding anything.
- **Breeding examples where they teach, abstract ones where they don't.** Matrix multiplication
  mechanics do not need livestock. `X'X`, `G + R`, `G₀ ⊗ A` and `A # A` absolutely do — each one
  is a real object the student will meet again, and seeing it here means the later chapter is
  recognition rather than first contact.

The three interact. The hand calculation *is* the Instance, so "hand first, then R" and "numbers
before symbols" are the same discipline applied to two different things — and the R chunk, which
reproduces a number the reader has already got, is a third confirmation rather than a fourth
teaching. Where a section has a board-work clip (§7), the clip is the Instance and the prose
beneath it does not re-narrate the steps.

### Learning objectives (final wording)

By the end of this chapter, you will be able to:

1. **Perform** transpose, addition, multiplication, and inversion by hand on matrices up to 4×4,
   and **verify** each result in R
2. **Diagnose** a singular matrix, **explain** why breeding models routinely produce one, and
   **use** a generalized inverse
3. **Apply** the Kronecker and Hadamard products and **name** the chapter where each is used
4. **Decompose** a covariance matrix by Cholesky and by eigenvalues, and **state** what each
   decomposition is for
5. **Derive** the variance of a linear combination, Var(**Ay**) = **A**Var(**y**)**A**′, and
   **use** it to assemble **V** = **ZGZ**′ + **R**

> These differ from `CHAPTERS.md` — see §9. Objectives 4 and 5 in the spec are merged here into
> objective 4, freeing a slot for the variance rule, which is the most-used result in the book and
> is currently missing from the outline.

---

## 2. The running examples

Three small examples carry the whole chapter. Reusing them is deliberate: a student who has met
`X` in §1.7 should not have to parse a new dataset in §1.10.

### Example A — four lambs, two flocks (§1.7–1.7, §1.14)

Sheep yearling weight, kg. Flock A = lambs 1–2, flock B = lambs 3–4.

| Lamb | Flock | Yearling wt |
|---|---|---|
| 1 | A | 48 |
| 2 | A | 52 |
| 3 | B | 41 |
| 4 | B | 45 |

Chosen so every intermediate is a whole number: flock means 50 and 43, `Σy = 186`, `ΣyA = 100`.
With the reference-level parameterisation `X = [1, flockA]`:

`X'X = [[4,2],[2,2]]`, `det = 4`, `(X'X)⁻¹ = [[0.5,−0.5],[−0.5,1]]`, `X'y = [186,100]`,
`b̂ = [43, 7]` — the flock B mean and the flock A advantage. Residuals `(−2, 2, −2, 2)`,
`e'e = 16`, `df = 2`, `σ̂²e = 8`.

Sheep, not pigs: Chapter 6's headline example is pig ultrasound backfat, and it should land there
fresh rather than as a rerun.

### Example B — two traits, one covariance structure (§1.3, §1.9, §1.11)

Sheep yearling weight (kg) and loin muscle depth (mm).

```
G = [[36, 12],      R = [[64,  4],      P = G + R = [[100, 16],
     [12,  9]]           [ 4, 16]]                   [ 16, 25]]
```

Everything a breeder reads off `P` comes out round: `σP = 10 kg` and `5 mm`, `h² = 0.36` for both
traits, `rg = 0.667`, `re = 0.125`, `rp = 0.32`. Realistic values, chosen so the arithmetic never
obscures the point.

### Example C — a decomposable covariance matrix (§1.11, §1.12)

```
M = [[100, 60],
     [ 60, 100]]
```

Cholesky `L = [[10, 0], [6, 8]]` — every entry an integer. Eigenvalues **160** and **40**,
eigenvectors `(1,1)/√2` and `(1,−1)/√2` — the "both traits together" axis and the "contrast"
axis, which is the interpretation that matters and the one Chapter 12 reuses.

Its singular sibling `[[100,100],[100,100]]` (eigenvalues 200 and 0) is the `rg = 1` matrix used
to show what a non-positive-definite **G** looks like.

### Relationship matrices used throughout

`A = [[1, 0.5], [0.5, 1]]` for two full sibs. Then `A # A = [[1, 0.25], [0.25, 1]]` for
additive × additive epistasis, and `G₀ ⊗ A` for the two-trait case.

---

## 3. Section outline

**The order is a dependency order, and that is the point.** §1.2–§1.5 must be read in sequence:
transpose needs only a matrix; addition needs only position; multiplication needs the transpose;
and the reversal rule `(AB)' = B'A'` needs multiplication, which is why it lives in §1.5 rather
than beside the transpose. Special matrices come *after* the operations (§1.6), because most are
defined by how they behave under them. `y = Xb + e` arrives in §1.7, once `X'X` can actually be
formed. No operation appears in prose or in an R chunk before the section that teaches it.

Section numbers below reflect two proposed changes to `CHAPTERS.md` (§9).

### 1.1 Why linear algebra?  [NEW]

Background before any operation: what linear algebra *is* (the mathematics of many quantities at
once, and the restriction the word *linear* imposes), the core vocabulary as **Definition**
callouts — matrix, vector, scalar, then **linear combination** as the one idea the chapter is
built from — and why a breeder needs it beyond this book: selection index, the general linear
model, multivariate analysis, principal components, genomic prediction, and diagnosing an
evaluation that has gone wrong.

The example is a plain 4 × 2 table of measurements (four lambs, yearling weight and loin depth).
**It carries no model.** That is the point: the reader meets a matrix as organised data before
meeting it as a statistical object, so `y = Xb + e` in §1.7 lands on vocabulary that already
exists.

*R:* build the matrix, read its dimensions and one element, take a column as a vector, and form
one linear combination by hand — the operation §1.5 later automates.

### 1.7 Why matrices: one model, many animals

Write Example A as four scalar equations, then stack them into `y = Xb + e`. The point is that
the matrix form is not a compression trick — it is the only form in which the same model can be
written for 4 animals or 4 million.

*R:* build `y` and `X` from a data frame with `model.matrix()`; show the object is the same one
written on the page.
*Clip:* `ch01-stacking` — board work, P1 (§7).

### 1.6 Notation, dimensions, and special matrices

Vectors and matrices, rows × columns, conformability, subscript conventions. Then the special
matrices, each introduced by the place it appears in this book, not as a list:

| Matrix | Where it shows up |
|---|---|
| Identity **I** | the residual structure `R = Iσ²e`; the "no relationships" model of Ch 3 |
| Null **0** | the off-diagonal blocks of an unrelated pedigree |
| **J** (all ones) | the mean model; `J/n` as the averaging operator |
| Diagonal | weights, unequal residual variances, `D` in `A = TDT'` |
| Symmetric | every covariance matrix; `X'X`; the whole MME left-hand side |
| Triangular | `L` from Cholesky, `T` from the pedigree |
| Incidence (0/1) | **X** and **Z** — almost entirely zeros, which is why Ch 24 exists |
| Block / partitioned | the MME itself |
| Positive definite | a valid covariance matrix — forward reference to §1.13 |

*R:* `diag()`, `matrix()`, `dim()`, `nrow()`, `Matrix::Matrix()` showing the sparse
representation of a real **Z**.
*Callout:* **Beyond This Book** — sparse storage and why a national evaluation never forms **Z**
densely; points to the computational volume.

### 1.3 Transpose, addition, and scalar multiplication

Transpose first (it is the easiest and it sets up `X'X`). Write Example A's `X` and its
transpose side by side and read off `(A')' = A` and `(A+B)' = A'+B'` from the page — these are
observations, not rules to be announced.

The reversal that matters is `(AB)' = B'A'`, **Key Equation 1**. Do not state it. Take a 2×2 `A`
and a 2×2 `B` with no symmetry and no shared structure, form `AB` by hand, transpose the result,
then form `A'B'` and `B'A'` and compare all three. One of the two matches and the other does not.
*Then* box the rule.

The Pattern line: the entries did not matter and the sizes did not matter — what mattered is that
transposing swaps which index runs along which side, so the factors must swap too. This is the
mistake students make in every chapter that follows (`X'Z` versus `Z'X`), and having produced the
wrong answer once by hand is worth more than having read the rule three times.

Addition on Example B: **P = G + R**. This is the whole reason a first-year student should care
about matrix addition — element by element, position preserved, and the result is the phenotypic
covariance matrix they will quote heritabilities from. Subtraction is `R = P − G`. Non-conformable
addition is shown failing.

Scalar multiplication: `G = Aσ²a`, and `α = σ²e/σ²a`.

*R:* `t()`, `+`, `-`, `*`; compute `h²`, `rg`, `rp` from `P` and `G` and check they are the round
numbers promised.
*Figures, not clips:* transpose as a labelled before-and-after; `P = G + R` side by side (§7).

### 1.5 Matrix multiplication — and what X′X and X′y actually count

Split out from the spec's §1.3 because it is the hardest operation and because of the second half
of the title. **This is the section the whole standard was written for**, and
`pedagogical_order.md` §4 contains it drafted end to end — follow that text.

The shape of it:

- **Instance.** Not a 2×3 by 3×2 in the abstract. Example A's flock indicator columns against the
  four weights, computing each flock's total *by hand, one lamb at a time* — arithmetic the reader
  would have done anyway without knowing it was matrix multiplication. The `ch01-matmul` clip
  carries this; the prose does not repeat the walk.
- **Pattern.** The weights were the lambs' — change them and the totals change. The number of
  columns walked through fixed how many totals came out. The walk itself would not change for four
  lambs or four million.
- **Statement.** *That walk is matrix multiplication*, with `c_ij = Σ_k a_ik b_kj` given as a
  notation for something the reader has now done twice, and conformability stated as the condition
  they already relied on without naming it.

Then the payoff on Example A:

- **X′X is a table of counts.** Its diagonal counts records per level; its off-diagonals count
  records sharing two levels. `[[4,2],[2,2]]` says "4 records, 2 of them in flock A."
- **X′y is a table of sums.** `[186, 100]` is the grand total and the flock A total.

A student who owns this reads every left-hand side in the book without effort. Also covered:
`Xb` as fitted values, `AB ≠ BA`, and `Zu` as "hand each animal its own breeding value."

*R:* `%*%`, and `crossprod(X)` / `crossprod(X, y)` as the idiomatic and faster forms.
*Callouts:* **In R** — `%*%` vs `*`; **Common Mistake** — non-conformable products, and assuming
commutativity.
*Clips:* `ch01-matmul`, `ch01-xtx-counts` — both board work, P1. `ch01-matmul` carries the
Instance for this section; the prose picks up at the Pattern.

### 1.8 Rank, singularity, and the determinant

Linear dependence shown on the overparameterised `X = [1, flockA, flockB]`, whose third column is
the first minus the second. Rank, full rank versus rank deficient, and why breeding models are
*routinely* rank deficient rather than exceptionally so.

The determinant gets a breeding meaning rather than a formula: `det = 0` means a column is
redundant; for a covariance matrix, `det(G) = 0` means `rg = ±1` and one trait carries no
information the other lacks. Example C's singular sibling makes this concrete.

*R:* `qr(X)$rank`, `det()`, and the singular `G` failing to invert.
*Clip:* `ch01-singular` — structural, P2.

### 1.9 Inversion, solving, and partitioned matrices

The inverse is defined by `AA⁻¹ = I`, and that definition is enough to *find* one without a
formula. Take `X'X = [[4,2],[2,2]]` from Example A, write the unknown inverse as four letters, and
demand the product be `I`. Four equations, four unknowns, all small: the reader solves them and
gets `[[0.5,−0.5],[−0.5,1]]`. Multiply back to confirm.

Only then, the Pattern: every entry came out over 4, which is `det = 4`; the diagonal entries
traded places and the off-diagonals changed sign. **Key Equation 2** — `A⁻¹ = adj(A)/det(A)`, with
the 2×2 case written out — is the box that names what just happened. A reader who has solved for
an inverse once will never again read the adjugate formula as an arbitrary arrangement of symbols,
and the `det = 0` case of §1.8 acquires an obvious meaning in hindsight: nothing to divide by.

Then the inverse of a diagonal matrix (reciprocals), `(AB)⁻¹ = B⁻¹A⁻¹` — which the reader should
be asked to predict from Key Equation 1 before being told — and the inverse of a covariance matrix
as a precision matrix, the first hint of why **A⁻¹**, not **A**, appears in the MME.

Solving: `X'X b = X'y`. The rule stated plainly — **do not invert to solve** — with `solve(A, b)`
against `solve(A) %*% b`, and a forward pointer to Ch 24.

Partitioned inversion (Schur complement) is set up here because the MME is a 2×2 block system and
because Chapter 7's reduced animal model and absorption are the same algebra.

*R:* `solve()` both ways; `chol2inv()` mentioned; timing comparison on a 500×500 matrix.
*Callouts:* **Derivation** — the block inverse via the Schur complement (collapsed);
**In R** — `solve(A, b)` versus `solve(A) %*% b`.
*Clip:* `ch01-inverse-2x2` — board work, P1, subject to the resolution in §7.

### 1.10 Generalized inverses

Why they are needed: the overparameterised model of §1.8 has no unique solution. Definition
`AA⁻A = A`. Two different g-inverses of the same `X'X` give two different solution vectors —
`(0, 50, 43)` and `(43, 7, 0)` — but identical fitted values and an identical flock difference of
7. Estimable functions introduced here in one paragraph and handed to Chapter 2.

*R:* `MASS::ginv()`, plus the "drop a level" g-inverse that `lm()` uses implicitly.
*Callout:* **Check Yourself** — two solutions, same answer: which quantities can you trust?
*Figure, not a clip:* two solution vectors and the contrast they agree on, as a table (§7).

### 1.11 Kronecker product, Hadamard product, and direct sum

- **Kronecker `⊗`** — `G₀ ⊗ A` expanded from a 2×2 and a 2×2 into the 4×4 covariance of two
  traits on two full sibs. Both orderings shown (trait within animal, animal within trait),
  because mixing them is the classic multi-trait error. Mixed-product rule
  `(A⊗B)(C⊗D) = AC ⊗ BD` stated; it is what makes multi-trait MME tractable. → Ch 11.
- **Hadamard `#`** — element-wise. `A # A` for additive × additive epistasis, `A # D` for
  additive × dominance. → Ch 17.
- **Direct sum `⊕`** — block diagonal, one block per contemporary group. → Ch 5, Ch 24.

*R:* `kronecker()` / `%x%`, `*`, `Matrix::bdiag()`.
*Callout:* **Common Mistake** — trait-within-animal vs animal-within-trait ordering.
*Clip:* `ch01-kronecker` — structural, P2; rendered once, embedded again in Ch 11.

### 1.12 Cholesky decomposition

`M = LL'` on Example C, computed by hand entry by entry (`L = [[10,0],[6,8]]`) — a recursion,
so a board-work clip (§7) rather than prose: each entry of `L` uses the entries already found, and
that dependency is the whole idea. Every number is an integer, so nothing is hidden. The general
recursion is stated after the reader has run it once, and it stays Tier 2. Then three uses, each
named with its chapter:

1. **Solving** — the numerically sound route to `X'X b = X'y` (Ch 24)
2. **Simulating correlated breeding values** — `a = Lz` with `z ~ N(0, I)`; this is how every
   simulation in the book generates a two-trait animal (Ch 11, Ch 22)
3. **Log-determinants in REML** — `log|M| = 2Σ log Lᵢᵢ` (Ch 21)
4. Mention that `A = TDT'` from the pedigree is a Cholesky-like factorisation, and that its
   triangular factor has a direct genetic reading (Ch 4)

*R:* `chol()` (note it returns the **upper** factor `R` with `M = R'R`, a genuine trap),
`L %*% t(L)`, and a simulation of 10,000 correlated breeding values whose realised covariance
recovers `M`.
*Callout:* **In R** — `chol()` returns upper-triangular.
*Clip:* `ch01-cholesky` — board work, promoted to P1: the recursion is exactly the kind of
sequence prose cannot carry.

### 1.13 Eigenvalues and eigenvectors

`Mv = λv` on Example C: eigenvalues 160 and 40, eigenvectors the sum and contrast axes. The
covariance ellipse drawn with its axes, so the decomposition is seen rather than computed.

Then the three facts a breeder needs:

- All eigenvalues > 0 ⟺ **positive definite** ⟺ a valid covariance matrix
- A zero eigenvalue means a perfect genetic correlation and a **G** that REML cannot handle
  (Ch 21) — the practical face of §1.8's singularity
- Eigenvectors are the principal components of the genetic covariance matrix, which is what
  reduced-rank and factor-analytic random regression models exploit (Ch 12)

One paragraph on SVD, pointing to the computational volume. Do not develop it (`CHAPTERS.md`).

*R:* `eigen()`, a positive-definiteness check, and a plot of the covariance ellipse with its axes.
*Callout:* **Derivation** — why a symmetric matrix has real eigenvalues and orthogonal
eigenvectors (collapsed).
*Figure, not a clip:* the covariance ellipse with its axes drawn and labelled (§7).

### 1.14 Quadratic forms, traces, and matrix derivatives

The section that exists to serve Chapter 21, and says so in its first line.

- **Quadratic forms** `x'Ax`: `e'e = 16` as the residual sum of squares from Example A;
  `y'y`, `b'X'y`, and the sums-of-squares partition previewing Ch 20
- **Trace**: sum of the diagonal, equals the sum of the eigenvalues; `tr(AB) = tr(BA)`;
  and the result worth memorising — the trace of the projection matrix `X(X'X)⁻X'` equals the
  rank, which is where degrees of freedom come from. Example A: `tr(H) = 2`, `df = 4 − 2 = 2`
- **Matrix derivatives**: `∂(a'x)/∂x = a` and `∂(x'Ax)/∂x = 2Ax` for symmetric `A`. Applied
  immediately: differentiating `(y − Xb)'(y − Xb)` gives `−2X'y + 2X'Xb = 0`, the normal
  equations. Chapter 2 then opens with the result already derived.

*R:* `crossprod()`, `sum(diag())`, and the hat matrix with its trace.
*Callout:* **Derivation** — `∂(x'Ax)/∂x = 2Ax` (collapsed).

### 1.15 Variances of linear combinations: building V  [NEW]

Not in the current spec, and the most-used result in the book.

`Var(Ay) = A Var(y) A'` (**Key Equation 3**), built up from the scalar case
`Var(ax) = a²Var(x)`. Then three applications in sequence, which is the whole argument of the
mixed model in one page:

1. `Var(Zu) = Z G Z'` — relationships propagate from animals to records
2. `Var(y) = ZGZ' + R` — the marginal variance **V**, assembled in front of the reader
3. `Var(k'b̂)` — the standard error of a contrast, and the seed of accuracy and PEV in Ch 6

*R:* simulate `u`, form `Zu`, and show the empirical covariance of the records converging on
`ZGZ'`. The simulation is the proof a student actually believes.
*Clip:* `ch01-var-linear` — structural, promoted to P2: `Z`, `G`, `Z'` closing in on `V`.

### 1.16 Which section do you need for which chapter?

A table mapping each section to the chapters that consume it, so readers can skip intelligently
and return. Required by `CHAPTERS.md`. It is also the chapter's honest admission that nobody
reads a matrix algebra chapter straight through.

### 1.17 Exercises

Six, one per objective plus two on the core operations. Solutions to Appendix H.

1. Form `X'X` and `X'y` by hand for a five-record, two-group design; state in words what every
   element counts or sums. *(obj 1)*
2. Given `G` and `R` for two traits, form `P`; compute both heritabilities, `rg`, and `rp`.
   *(obj 1)*
3. Invert a 2×2 `X'X` by hand, solve for `b̂`, and verify with `solve()`. *(obj 1)*
4. Show a given `X` is rank deficient; find its rank; produce two different g-inverse solutions
   and one estimable function on which they agree. *(obj 2)*
5. Compute `G₀ ⊗ A` for two traits on three animals; identify which element is
   `cov(a₁ trait 1, a₃ trait 2)` under each of the two orderings. *(obj 3)*
6. Cholesky-factor a 2×2 `G`; use `L` to simulate 10,000 pairs of correlated breeding values in R
   and confirm the realised covariance matrix. *(obj 4)*

An exercise for objective 5 is folded into exercise 6's second part (report `Var(Zu)` for a small
`Z`) rather than adding a seventh, keeping the spec's count of 6.

---

## 4. Key equations (Tier 1 — three, per the standard)

Each box is preceded by the instance that earns it, per `pedagogical_order.md` §3. **None of the
three may be the reader's first sight of its own content** — that is the check to run on the
draft.

| # | Equation | The instance that earns it | Why it is Tier 1 |
|---|---|---|---|
| 1 | `(AB)' = B'A'` and `(AB)⁻¹ = B⁻¹A⁻¹` — the reversal rules | §1.3: form `(AB)'`, `A'B'` and `B'A'` on two 2×2s and find which one matches | Used in every chapter; the source of the `X'Z` / `Z'X` confusion |
| 2 | `A⁻¹ = adj(A)/det(A)`, with the 2×2 case written out | §1.9: solve `AA⁻¹ = I` for four unknowns on `X'X`, then notice everything came out over `det` | The only inverse a student will ever compute by hand |
| 3 | `Var(Ay) = A Var(y) A'` | §1.15: the scalar `Var(ax) = a²Var(x)`, then `Var(Zu)` simulated until the realised covariance is `ZGZ'` | Everything from `V = ZGZ' + R` to PEV descends from it |

Everything else in the chapter is Tier 2. Three Tier 3 derivations, all collapsed and **all placed
after the box or result they justify**, not before: the block inverse via Schur complement (§1.9),
symmetric-matrix eigen properties (§1.13), and `∂(x'Ax)/∂x = 2Ax` (§1.14).

## 5. Callout budget — 15 teaching boxes at the cap, plus 9 Definitions outside it

| Box | n | Where |
|---|---|---|
| Learning Objectives | 1 | top |
| Definition | 9 | §1.1 ×2, §1.6, §1.8 ×2, §1.9, §1.10 ×2, §1.13 — **outside the cap** |
| Key Equation | 3 | §1.3, §1.9, §1.15 |
| Derivation | 3 | §1.9, §1.13, §1.14 |
| Check Yourself | 3 | §1.5, §1.10, §1.13 |
| Common Mistake | 2 | §1.5 (conformability, commutativity), §1.11 (trait ordering) |
| In R | 2 | §1.5 (`%*%` vs `*`), §1.12 (`chol()` returns upper) |
| Beyond This Book | 1 | §1.6 (sparse storage → computational volume) |

**Check Yourself placement.** All three sit at the Pattern moment — after the reader has worked
the instance and before the general rule is given, which is the one point in a section where a
prediction is both possible and not yet spoiled. §1.5: *"you multiplied a 4×2 by a 2×1 and got a
2×1 — what comes out of a 4×2 against a 4×1, and why can't you?"* §1.10: two solutions, same answer,
which quantities can you trust? §1.13: given the eigenvalues of `M`, predict the sign of the
determinant before computing it.

`(AB)⁻¹ = B⁻¹A⁻¹` in §1.9 is also a prediction the reader can make from Key Equation 1, but it
has no box left under the cap — ask it in the body text.

No **Notation Watch** and no **In Practice** in this chapter: the notation is being established
here rather than reconciled, and there is no evaluation to describe yet. Both return in Chapter 4.

Note the third **In R** box that §1.9 wants (`solve(A, b)` vs `solve(A) %*% b`) does not fit under
the cap. It moves into the body text as a bolded rule, which is the right call — it is a rule, not
an aside.

## 6. R policy for this chapter

R is not a separate section; it appears in every section, **visible**, immediately under the hand
calculation it reproduces. Each chunk **prints the hand result** so the two can be compared on
screen without expanding or scrolling.

`code-fold` is off book-wide (`CLAUDE.md`, "Code visible"). A student following Chapter 1 with an
R session open should be able to read straight down the page and retype every line. That governs
the code's shape as much as its visibility: one idea per chunk, objects named after the book's
notation (`X`, `y`, `XtX`, `b_hat`), comments on the modelling step rather than the syntax, and
the explicit form before the idiomatic one. `crossprod` and `solve(A, b)` are introduced as
deliberate improvements in **In R** callouts, *after* `t(X) %*% X` and `solve(A) %*% b` have been
shown — not silently as the first thing the reader sees.

The one chunk that may fold is the covariance-ellipse plot in §1.13: its `par`/`arrows`/`bquote`
cosmetics teach nothing about the algebra, and folding them keeps the eigen-decomposition itself
in view.

Functions introduced, in order: `matrix`, `dim`, `nrow`, `t`, `+`/`-`/`*`, `%*%`, `crossprod`,
`tcrossprod`, `diag`, `model.matrix`, `qr()$rank`, `det`, `solve`, `chol2inv`, `MASS::ginv`,
`kronecker` / `%x%`, `Matrix::bdiag`, `chol`, `eigen`, `sum(diag())`, and `Matrix::Matrix` for the
sparse view of **Z**. This list feeds Appendix F.

## 7. Manim clips

Chapter 1 is granted an exception to the five-clip cap: **8 clips**, distributed one per section
rather than concentrated in one flow, because this is a reference chapter a reader enters at any
point.

The roster below is **reordered from the original plan** under `pedagogical_order.md` §7. The
count is unchanged; which eight get built is not.

### Board work versus structure

The clips do two different jobs and should not be budgeted as if they did one.

- **Board work** — a specific calculation, real numbers, one step at a time. This is what a
  teacher walks to the whiteboard for. It is the **Instance** move, and where one exists the prose
  beneath it stops narrating the steps and goes straight to the Pattern.
- **Structural** — shape, assembly, relationship, no arithmetic. The **Pattern** move: what the
  object *is*, not how it is computed.

**The criterion for building one at all: prose is bad at sequence, fine at statements.** A
paragraph asking the reader to run "take row *i*, pair it with column *j*, multiply, sum" in
working memory while reading about it is doing the one thing writing cannot do. A paragraph saying
"`X'X` is symmetric" is doing something writing does perfectly well.

Applied here, that demotes four clips and promotes two.

### The eight

| # | Stem | s | Kind | Teaches | Grammar | Pri |
|---|---|---|---|---|---|---|
| 1 | `ch01-stacking` | 35 | **board** | Four scalar equations stacking into `y = Xb + e` | Assembly | P1 — §1.7, and the book's first Instance→Statement move |
| 2 | `ch01-matmul` | 60 | **board** | Row × column, one lamb at a time; inner dimensions cancel | Row × column — **build this helper first, it is reused book-wide** | P1 |
| 3 | `ch01-xtx-counts` | 45 | **board** | `X'X` counts, `X'y` sums | Row × column, landing on an annotated result | P1 |
| 4 | `ch01-inverse-2x2` | 45 | **board** | `AA⁻¹ = I` set up as four unknowns; the `det` pattern emerging | Inversion — see the note below | P1 |
| 5 | `ch01-cholesky` | 50 | **board** | `M = LL'` entry by entry, each using the last; then `a = Lz` | Recursion / accumulation | P1 — promoted from P2 |
| 6 | `ch01-singular` | 40 | structural | Dependent column, `det → 0`, `rg = 1` | Element-wise + collapse | P2 |
| 7 | `ch01-kronecker` | 45 | structural | `G₀ ⊗ A` expanding 2×2 → 4×4 | Assembly | P2 — also embedded in Ch 11 |
| 8 | `ch01-var-linear` | 40 | structural | `Z G Z'` closing into `V` | Assembly | P2 — promoted from P3 |

### Demoted to a static figure

Not dropped — each still appears, as a labelled before-and-after or a plot. They are cut as
*clips* because the sequence in each is one step long, and animating a one-step sequence teaches
the reader that clips are decoration, which costs the attention the other eight need.

| Was | Why a figure suffices |
|---|---|
| `ch01-transpose` | A before-and-after with one arrow shows the flip completely |
| `ch01-add-covariance` | `P = G + R` element by element is a side-by-side, not a process |
| `ch01-eigen` | An ellipse with its axes drawn is a picture. Nothing moves |
| `ch01-ginverse` | Two solution vectors and one matching contrast is a three-column table |

### One conflict to resolve

`manim_visual_standards.md` specifies inversion as *"animate the check, never the arithmetic."*
The board-work principle points the other way for §1.9, where the arithmetic is the teaching.

Proposed resolution, for confirmation: **animate the setup and the pattern, not the solve.** The
clip poses `AA⁻¹ = I` as four equations in four unknowns and then reveals the finished inverse with
`det = 4` highlighted under every entry and the sign flips called out; the actual solving of the
four equations stays on the page where the reader can work it at their own pace. That keeps the
visual standard's intent — never animate tedium — while still letting the clip carry why the
adjugate formula looks the way it does.

Colour note: §1.7–1.7 are pre-semantic — a matrix has no model role yet, so cells are `BODY` and
the *grammar* carries the teaching. From `ch01-xtx-counts` onward, `X` takes `FIXED` blue and
`y` takes `DATA` amber, so a student arriving at Chapter 6 already reads the palette. Say this in
one caption the first time it happens.

## 8. Chapter beats mapped to the standard skeleton

Chapter 1 has no dataset and no scale-up, so three beats of the standard skeleton are absent by
design. That is an exception to record, not a gap to fill.

| Beat | In this chapter |
|---|---|
| Learning Objectives | ✔ |
| Prerequisites | *None — this is the entry point.* |
| Why this chapter | §1.7 |
| The toy dataset | **absent** — Example A serves the role; no CSV, matrices inline (spec) |
| The matrices for these animals | §1.6, and then re-entered at the head of every section — each one opens on its own numbers |
| Solve by hand | §1.3–1.12, section by section |
| **The general form** | **runs once per section, not once per chapter.** Each operation gets its own Pattern lines and, for the three Tier 1 results, its own box |
| Interpret the answer | folded into each section rather than standing alone |
| The same model in R | **absent as a beat** — R is interleaved throughout instead (§6) |
| Scale up | **absent** — the one exception is the timing comparison in §1.9 |
| Key equations | §1.16 precedes it; recap table before the exercises |
| Exercises | §1.17 |

The per-section repetition of Instance → Pattern → Statement is the fourth documented exception
for this chapter. Everywhere else in the book the cycle runs once, around the chapter's central
result. Here it runs eleven times, because a reference chapter has eleven small results rather
than one large one — which is also why §8 of `pedagogical_order.md` caps each instance at roughly
ten lines so the rule stays on the same screen as the numbers that earned it.

## 9. Proposed changes to `CHAPTERS.md`

`CHAPTERS.md` is the source of truth and `_quarto.yml` is kept in sync with it, so these need to
be made there before the chapter is drafted:

1. **Split the spec's §1.3** into transpose/addition (§1.3) and multiplication (§1.5). Reason:
   multiplication is the hardest operation in the chapter, and the `X'X`-as-counts idea deserves
   its own heading rather than being buried.
2. **Add §1.15, "Variances of linear combinations"**, and revise the objectives as in §1 above
   (merge the spec's objectives 4 and 5, add the variance rule). Reason: `Var(Ay) = A Var(y) A'`
   is used in almost every subsequent chapter and currently appears in none of them as a taught
   result.
3. Record the four documented exceptions: 8 manim clips rather than 5, the three absent skeleton
   beats (§8), the per-section rather than per-chapter Instance → Pattern → Statement cycle (§8),
   and the short-instance allowance for a reference chapter (`pedagogical_order.md` §8).

Everything else follows the spec unchanged: no dataset, nothing larger than 4×4, `base` and
`Matrix` only, 6 exercises.

## 10. Open questions

- **Are the four clip demotions right?** §7 cuts `ch01-transpose`, `ch01-add-covariance`,
  `ch01-eigen` and `ch01-ginverse` to static figures on the grounds that a one-step sequence does
  not need animating. The count stays at 8 either way, so this is a question of *which* eight, not
  of budget. `ch01-eigen` is the arguable one — a rotating ellipse is genuinely appealing — but it
  illustrates rather than teaches, and the axes are the whole content.
- **Does the inversion clip animate the arithmetic?** §7 proposes a resolution to the conflict
  with `manim_visual_standards.md`; it needs a decision before `ch01-inverse-2x2` is storyboarded.
- **Does §1.14 go this deep on matrix derivatives?** It exists only to serve Chapter 21. The
  alternative is two lines here and the full treatment in Chapter 21 where the reader has a
  reason to care. Current plan keeps it here because Chapter 2's normal equations need it three
  pages later.
- **Ellipse plot in §1.13 — ggplot or base?** Everything else in the chapter is base R. Suggest
  base, to keep Chapter 1 dependency-free beyond `Matrix`.
- **Should `ch01-kronecker` live in Ch 1 or Ch 11?** It is rendered once either way; the question
  is which chapter's caption it is written for. Suggest writing it for Ch 1 (mechanics) and
  letting Ch 11 re-embed it with a different caption.
