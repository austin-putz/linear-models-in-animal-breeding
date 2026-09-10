# Pedagogical order — numbers before symbols

The book's answer to *"why does every statistics text state the theorem and then condescend to an
example?"*

Companion documents: [`chapter_standards.md`](chapter_standards.md) (structure, callouts, math
tiers) · [`manim_visual_standards.md`](manim_visual_standards.md) · `CLAUDE.md` (scope, traits,
datasets).

**Status:** adopted 2026-09-04. The edits in §9 have been applied to `chapter_standards.md`,
`templates/chapter-template.qmd`, `CLAUDE.md`, `chapter_01_linear_algebra.md` and
`manim_videos.md`. No chapters were drafted at the time of adoption, so nothing needed rewriting.

---

## 1. The claim, and the part of it that needs qualifying

The claim: mathematics is conventionally taught **deductively** — general statement first,
instance second — and for a reader meeting the material for the first time that order is
backwards. Show two matrices being multiplied, then say what multiplication is.

This is right, and the evidence is not thin (§2). But two qualifications change how it must be
implemented, and skipping them turns a good instinct into a worse book than the one it replaces.

**Qualification 1 — the generalisation step is mandatory, not optional.** A reader given only the
instance memorises the instance. Kaminski, Sloutsky & Heckler (2008) found that learners trained
on a *generic* symbolic version of a rule transferred it to a new domain better than learners
trained on a rich concrete instantiation, who stayed stuck to the surface story. The resolution in
the later literature is not "abstract wins" but *fading*: the concrete instance is the entry, and
it must be deliberately stripped down to the symbols rather than left standing. In this book the
risk is specific and severe — livestock context is extremely concrete, and a reader who meets the
MME only as "the eight equations for those six pigs" will not recognise it in Chapter 12.
**Reversing the order without adding a compulsory generalisation beat makes the book worse, not
better.**

**Qualification 2 — it is not students-versus-professors, it is first-reading-versus-return.** The
relevant variable is prior knowledge *in the specific topic*, not seniority (this is the expertise
reversal effect; Sweller, van Merriënboer & Paas 2019). A dairy geneticist of twenty years' standing
opening Chapter 12 for the first time is a novice in random regression and is helped by the
instance exactly as much as a first-year is. Conversely, a first-year *returning* to Chapter 4 to
look up Henderson's rules wants the statement immediately and is insulted by four paragraphs of
narrative.

So the rule is not "reverse the order for students." It is:

> **The first pass through any result is instance-first. Statement-first access is provided
> separately, as an index, for the reader who already has the result and wants it back.**

The book already has the mechanism for the second half: the Tier 1 Key Equation boxes and the
key-equation index in Appendix A. That index stops being a revision aid and becomes load-bearing —
it is the deductive door into a book that is otherwise inductive throughout.

---

## 2. The evidence

Every reference below was retrieved and verified against the publisher record — none is
reconstructed from memory, and none carried a retraction, correction, or editorial concern when
checked (2026-09-04). Full APA entries are in the References section; DOI links are repeated here so each claim is
one click from its source. **OA** marks an openly readable version; the rest need the Iowa State
library proxy.

| Finding | Source | Link |
|---|---|---|
| Inductive methods (case-first, problem-first, inquiry) are consistently **at least equal to and generally more effective than** deductive instruction across a broad range of outcomes, reviewed specifically for engineering education | Prince & Felder (2006), *J. Eng. Educ.* 95(2):123–138 | [10.1002/j.2168-9830.2006.tb00884.x](https://doi.org/10.1002/j.2168-9830.2006.tb00884.x) |
| **Concreteness fading** — concrete → representational → symbolic — reviewed across mathematics and science instruction | Fyfe, McNeil & Son (2014), *Educ. Psychol. Rev.* 26(1):9–25 | [10.1007/s10648-014-9249-3](https://doi.org/10.1007/s10648-014-9249-3) |
| Fading concrete material to symbols **promotes transfer**, more than concrete-only or abstract-only instruction | McNeil & Fyfe (2012), *Learn. Instr.* 22(6):440–448 | [10.1016/j.learninstruc.2012.05.001](https://doi.org/10.1016/j.learninstruc.2012.05.001) |
| The **direction matters**: concrete→abstract beats abstract→concrete, and the benefit holds at both low and high prior knowledge | Fyfe, McNeil & Borjas (2015), *Learn. Instr.* 35:104–120 | [10.1016/j.learninstruc.2014.10.004](https://doi.org/10.1016/j.learninstruc.2014.10.004) |
| The counterpoint: generic/abstract training transferred better than concrete instantiations | Kaminski, Sloutsky & Heckler (2008), *Science* 320:454–455 | [10.1126/science.1154659](https://doi.org/10.1126/science.1154659) |
| Novices learn more from **studying a worked solution** than from solving; the advantage reverses as expertise grows | Sweller, van Merriënboer & Paas (2019), *Educ. Psychol. Rev.* 31(2):261–292 | **OA** [10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5) |
| Worked examples win for **high element interactivity**; generating the answer yourself wins for **low element interactivity** | Chen, Kalyuga & Sweller (2015), *J. Educ. Psychol.* 107(3):689–704 | **OA** [10.1037/edu0000018](https://doi.org/10.1037/edu0000018) |

The last row is the most practically useful and is developed in §6. It is what stops "show
everything worked" from becoming "the reader never does anything." Conveniently, the two openly
readable papers are also the two worth reading first: Sweller et al. (2019) summarises the whole
cognitive-load programme, and Chen et al. (2015) is the one that gives §6 its rule.

Note what the evidence does *not* say. It does not support discovery learning, in which the reader
is handed a dataset and left to invent BLUP. Every result in this book is fully worked in front of
the reader. What changes is only the **order of presentation**: the worked instance comes before
the general statement rather than after it.

---

## 3. The rule: Instance → Pattern → Statement

Every result in the book is presented in three moves, in this order. A fourth is optional.

| Move | What it is | Length |
|---|---|---|
| **1. Instance** | One specific case, with actual numbers, worked completely. No general symbols yet, or symbols only as labels for numbers already on the page. | Whatever it takes |
| **2. Pattern** | What stayed the same and what would change. The reader is invited to generalise before being told. | 3–8 lines |
| **3. Statement** | The general form. **This is the Tier 1 Key Equation box.** | The box |
| **4. Proof** *(optional)* | Why it is true in general. **Tier 3, collapsed, and now placed *after* the box, not before.** | Collapsed |

Slogan for the margin of every draft: **numbers before symbols.**

### The Pattern move, mechanically

This is the move that does not exist in the current standards and the one that will get dropped in
drafting unless it is specified. It answers three questions, in this order, in a few lines:

1. **What in that calculation depended on the particular numbers?** (the values — 118 kg, α = 1.2)
2. **What depended on the shape of the data?** (the dimensions — 6 animals, 1 contemporary group,
   so an 8 × 8 system)
3. **What would have been identical for any dataset at all?** (the structure — and *that* is the
   equation)

Question 3's answer, written out, *is* the Statement. The Tier 1 box is then not a new object
dropped on the reader; it is the third answer, set in a box because it is the one worth
memorising.

### The inverted pairing rule

`chapter_standards.md` §1 formerly required **derivation → Key Equation box**, so a reader who
skips the grey box still lands on the result. That property is preserved and strengthened by the
reversal, because the box now has *two* things leading into it:

```
[ worked instance, with numbers ]        ← new: the box is never the reader's first contact
        ↓
[ Pattern: what would change, what would not ]
        ↓
::: {.callout-important .key-equation}
## Key Equation — The Mixed Model Equations {#eq-mme}
:::
        ↓
::: {.callout-note .derivation collapse="true"}
## Derivation — the MME from the joint density (optional)
:::
```

**New hard rule: a Key Equation box is never the first appearance of its own content.** If a
reader meets `X'X` for the first time inside a box, the section is written backwards. This is
mechanically checkable in review and should be the first thing a reviewer looks for.

The derivation moves *after* the box because its job has changed. Under the old order it earned
the result. Under the new order the worked instance has already convinced the reader the result is
true; the derivation now only shows *why it holds for every dataset and not just this one*. That
is a different question, it is genuinely optional, and it belongs after the answer it justifies.

### Symbols enter attached to numbers

Corollary for `CLAUDE.md`'s "define every symbol on first use." Strengthen it to:

> A symbol's first appearance is a **name given to something already on the page**, never a
> placeholder for something to come.

```
Bad:   Let X be the n × p incidence matrix of fixed effects. For our six pigs, X is …
Good:  Every pig is in the same contemporary group and each is either a barrow or a gilt, so
       each record needs two indicators:

           1  0        pig 1, barrow
           1  0        pig 2, barrow
           1  1        pig 3, gilt
           ...

       Six rows, one per record; two columns, one per thing being estimated. Call this X.
```

---

## 4. Worked demonstration — the reader's own example

Matrix multiplication, `chapters/01-matrix-algebra.qmd` §1.4.

**Conventional (deductive).** *If **A** is m × n and **B** is n × p, then **C** = **AB** is m × p
with elements c_ij = Σ_k a_ik b_kj. For example, …*

Two things are wrong with this. The reader must hold three index variables in working memory
before anything has happened, and the summation notation — the hardest object on the page — is
carrying the *definition*, so there is nothing to check it against.

**Instance-first.**

> Flock A's two lambs weigh 48 and 52 kg; flock B's weigh 41 and 45. We want each flock's total.
>
> Here are the records, and here is a bookkeeping table marking which flock each lamb is in:
>
> ```
>       flock A  flock B                y
> lamb1    1        0                  48
> lamb2    1        0                  52
> lamb3    0        1                  41
> lamb4    0        1                  45
> ```
>
> Flock A's total is `1(48) + 1(52) + 0(41) + 0(45) = 100`. Multiply the flock A column by the
> weights, one lamb at a time, and add. Flock B's is `0(48) + 0(52) + 1(41) + 1(45) = 86`.
>
> Two totals, from two columns, against one list of weights. Write them as a pair:
>
> ```
> [100]
> [ 86]
> ```

**Pattern.**

> The numbers 48 and 52 were the lambs' weights — change the weights and the totals change.
> The number of columns we walked through was the number of flocks, and it fixed how many
> totals came out. But *the walk itself* — take a column, pair it term by term with the list,
> multiply, add — never changed, and it would not change for 4 lambs or 4 million, for 2 flocks
> or 200.

**Statement.** Only now:

> That walk is matrix multiplication. Standing the bookkeeping table on its side so its columns
> become rows, `X′y` is the vector whose *i*th element pairs row *i* of `X′` with `y` term by term
> and sums:
>
> (X′y)_i = Σ_k (X′)_ik y_k
>
> The condition for it to work is exactly the one we relied on without saying so: the thing being
> walked along and the thing being walked against must have the same length.

The summation now describes an operation the reader has already performed twice by hand. It is a
notation for a known thing, which is the only circumstance under which notation is easy.

Note what came for free. `X′y` **is a table of sums** — not a fact stated about the object later,
but the reason the object was constructed. The `X′X`-as-counts idea in the Chapter 1 plan lands
the same way and no longer needs a callout to point at it.

---

## 5. Before and after, in the book's own structure

`chapter_standards.md` §3 *formerly* ordered the beats like this (kept here as the "before", since
the file itself has now been changed):

```
6. The model and its matrices   ← "Tier 1 boxes appear here"
7. Solve by hand
8. Interpret the answer
```

That is statement-first. Chapter 6 as specified would present the MME in a box and *then* put
numbers in it. The revised skeleton:

| # | Beat | Change |
|---|---|---|
| 1 | Title | — |
| 2 | Learning Objectives | — |
| 3 | Prerequisites | — |
| 4 | Why this chapter | — |
| 5 | The toy dataset | — |
| 6 | **The matrices for *these* animals** | **renamed and rescoped.** Literal integer arrays for this dataset. No general dimensions, no Tier 1 boxes. Symbols named after the arrays they label |
| 7 | **Solve by hand** | unchanged in content; now the reader's *second* beat of arithmetic rather than their first |
| 8 | **The general form** | **new beat.** The Pattern move, then every Tier 1 box in the chapter, then any Tier 3 derivation, collapsed |
| 9 | Interpret the answer | — |
| 10 | The same model in R | — |
| 11 | Scale up | — |
| 12 | Key equations | recap table, unchanged |
| 13 | Exercises | — |

Beat 8 is the one that will be dropped under deadline, exactly as beat 9 ("Interpret") is the one
the current standard flags as most often dropped. Both are worth defending in review, and for the
same reason: a chapter that stops after beat 7 has taught arithmetic on six pigs.

**Check Yourself boxes acquire a fixed home.** The most valuable position is immediately *before*
beat 8 — the reader has the worked instance and has not yet been given the general form, which is
the one moment in the chapter when a prediction is both possible and not yet spoiled:

> *You solved this for six pigs and got an 8 × 8 system. Before you read on: for 600 pigs in 12
> contemporary groups, how large is the system, and which block grew?*

At least one of a chapter's 2–3 Check Yourself boxes sits here.

---

## 6. What to work for the reader, and what to make them do

From Chen, Kalyuga & Sweller (2015): worked examples beat self-generation when the material has
**high element interactivity** (many pieces that only make sense together); generating the answer
yourself beats being shown when interactivity is **low** (steps that can be understood one at a
time). Instance-first does not mean everything is pre-chewed.

| Element interactivity | Examples in this book | Treatment |
|---|---|---|
| **Low** — one step, understandable alone | Building `X` and `Z` from a data table; transposing; forming `P = G + R`; reading `h²` off `G` and `P`; counting a pedigree's generations | **Make the reader generate it.** Check Yourself box, or an exercise. Give the answer immediately after |
| **High** — the pieces are meaningless separately | Assembling the four MME blocks; Henderson's `A⁻¹` rules; the Kronecker expansion; a Gibbs full conditional; the AI-REML update | **Fully worked in front of the reader**, every step, no gaps |

This is also the honest reason `X` and `Z` construction is a Check Yourself rather than a worked
page: not to save space, but because it is the kind of step people learn better by doing.

---

## 7. Fading across the book, and what the clips are actually for

Concreteness fading is a three-stage progression, and the middle stage is the one everyone skips.
The book already has homes for all three.

| Stage | Where it lives |
|---|---|
| **Concrete** | The toy dataset, and the **board-work clips** — real numbers, moved one step at a time |
| **Representational** | The **structural clips** — matrices as labelled blocks with dimensions, `Z G Z'` closing into `V` |
| **Symbolic** | The Tier 1 Key Equation box |

### The two kinds of clip

The clips are not one thing, and the distinction decides which are worth building.

| | **Board work** | **Structural** |
|---|---|---|
| Shows | A specific calculation, with actual numbers, one step at a time | Shape, assembly, relationship — no arithmetic |
| Is the… | **Instance** move | **Pattern** move |
| Answers | *How is this done?* | *What is this thing?* |
| Examples | `ch01-matmul`, `ch01-inverse-2x2`, `ch01-cholesky`, Jacobi iterating | `ch01-kronecker`, `ch01-var-linear`, the MME's four blocks |

**The criterion: prose is bad at sequence.**

A paragraph that says *"take row i, pair it term by term with column j, multiply, sum, and that is
element c_ij"* asks the reader to run a process in working memory while reading about it. That is
the single thing writing cannot do and a whiteboard does effortlessly — which is why every teacher
who is any good walks to the board for matrix multiplication instead of describing it. Prose is
good at statements *about* an object; it is bad at a sequence of moves *on* one.

So:

> **A clip earns board-work treatment when the difficulty is a sequence of steps. If the
> difficulty is the shape of an object, a static figure is as good and costs a fraction as much.**

Two corollaries, and they cut in opposite directions:

- **Don't animate easy mechanics.** A transpose, or `P = G + R` element by element, is a sequence
  — but a two-second one that a static before-and-after conveys completely. Animating it spends
  budget and teaches the reader that clips are decoration, so they stop watching the ones that
  matter.
- **Don't leave a hard sequence in prose because it's "just algebra."** The Cholesky recursion,
  Henderson's `A⁻¹` contributions accumulating over a pedigree, and a Gibbs sweep are all
  sequences the page genuinely cannot carry.

Where a board-work clip exists, **it is the Instance move** and the prose beneath it is the
Pattern and Statement. The prose does not re-narrate the steps; it says what stayed the same.

### Length of the instance, by Part

The *order* never changes — no statement precedes its instance anywhere in the book. What changes
is how long the instance runs, because by Part VII the reader is no longer a novice in matrix
notation and a full six-animal solve to motivate a likelihood is padding.

| Part | Instance length |
|---|---|
| **I–II** (Ch 1–10) | Full. Every array printed, every arithmetic step shown |
| **III–VI** (Ch 11–19) | Compressed. Show one animal's rows, one block, one pen — enough for the pattern; refer back for the rest |
| **VII–VIII** (Ch 20–24) | Minimal. Often a single numeric evaluation (three points on a likelihood curve; three Jacobi iterations in a table) before the general form |

---

## 8. Where the reversal does **not** apply

Stated explicitly, because a rule applied without exception becomes a mannerism and the writing
turns coy — narrating toward a definition the reader would rather just be handed.

**Reverse results. Declare conventions.**

| Do not reverse | Why | Example |
|---|---|---|
| **Notation and conventions** | Nothing to discover. `A′` means transpose because we say so | §1.2's symbol table; the notation appendix |
| **Model statements** | `y = Xb + Zu + e` is an assumption, not a derived result. It is declared, then justified by what it buys. (Even here, Ch 1 §1.1's four scalar equations stacking into matrix form is the right treatment) | Ch 3 §3.2, Ch 6 §6.1 |
| **Distributional assumptions** | `u ~ N(0, Aσ²a)` is a modelling choice | Ch 6 §6.2, Ch 14 §14.2 |
| **Definitions of terms** | Repeatability, censoring, estimability — a definition is a naming, and a reader hunting for the name should find it | Ch 8 §8.3, Ch 15 §15.2 |
| **Chapter 1's reference sections** | Entered mid-way, out of order, by a reader who wants the rule. Each section still opens with its instance, but stays short enough that the rule is visible on the same screen | §1.2–1.11 |
| **Appendix A** | Statement-first by design. It is the deductive index into an inductive book (§1) | — |

**Sanity check when unsure:** if a reader could in principle have predicted the general form from
the worked instance, reverse it. If they could only have guessed, declare it.

---

## 9. Edits this requires

**All applied 2026-09-04.** None of the drafted content changed, because no chapters are drafted
— this landed before the first chapter shipped, which is why it was worth doing now rather than as
a revision pass. A fifth file, `manim_videos.md` §6, gained the sequence-versus-shape criterion
from §7.

1. **`plans/chapter_standards.md`**
   - §1, the pairing rule: invert to instance → Pattern → box → collapsed derivation. Add the hard
     rule that a Key Equation box is never the first appearance of its content.
   - §1, "What each tier looks like in Chapter 6": Tier 3 now *follows* Tier 1.
   - §2, Check Yourself: add the fixed position immediately before the generalisation beat.
   - §3, the skeleton: replace beats 6–8 with the seven-row block in §5 above.
   - New §6 cross-referencing this document.

2. **`templates/chapter-template.qmd`**
   - Reorder to match: `## The matrices for these animals` (literal arrays) → `## Solving by hand`
     → `## The general form` (Pattern paragraph, then Key Equation box, then collapsed Derivation)
     → `## What the answer means`.
   - Add the Pattern placeholder with its three questions as an HTML comment, so a drafter cannot
     skip it without deleting something.

3. **`CLAUDE.md`**
   - Under *Pedagogical rules*, replace "**Show every step.** Define every symbol on first use"
     with the strengthened symbol rule from §3 and a one-line statement of Instance → Pattern →
     Statement, pointing here.

4. **`plans/chapter_01_linear_algebra.md`**
   - §1.3 and §1.6 currently place Key Equations 1 and 2 (`(AB)′ = B′A′`, the 2 × 2 inverse) at
     the head of their sections. Move both after the worked instance. §1.4's `X′X`-as-counts and
     §1.12's `Var(Ay)` are already instance-first and need no change.

---

## 10. Per-chapter application

The concrete thing that opens each chapter's central result, and the statement it earns. One row
per chapter; fill these into the chapter plans as they are written.

### Part I — Background

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 1 | Four lambs' weights written as four scalar equations, then stacked. Each operation on 2 × 2 numbers before its rule | The operation rules; `(AB)′ = B′A′`; the 2 × 2 inverse; `Var(Ay) = A Var(y) A′` |
| 2 | Print the literal 9 × 4 array of 0s and 1s for nine pigs. Form `X′X` **by counting records**, not by multiplying | The normal equations; estimability |
| 3 | Solve the pen model twice by hand — once treating pens as fixed, once with α = 5 — and set the two sets of pen solutions side by side | The MME with `G = Iσ²`; the shrinkage factor, which the reader has already watched happen |
| 4 | Build `A` for four animals cell by cell. Then invert a 3 × 3 `A` **numerically** and point at the ±1, ±½, ¼ pattern sitting in the result | Henderson's rules for `A⁻¹` — read off a pattern the reader has already seen, instead of asserted as a recipe |
| 5 | One EBV ranking from 25 records; drop the singleton contemporary group; the second ranking beside the first | The editing principles, and why they are not clerical |

### Part II — Core animal models

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 6 | Six pigs. Print `X`, `Z`, `A⁻¹`, α = 1.2 as literal arrays; assemble and solve the 8 × 8 system by hand | **The MME.** The book's headline Tier 1 box, and under this standard it appears *after* the reader has solved one |
| 7 | Refit the Chapter 6 animals as a sire model; two EBV columns, same six pigs, in one table | The equivalence statement; what a reduced model discards |
| 8 | One sow, three parities. Compute her EBV with, then without, a permanent environmental term | The repeatability model; r as the bound on h² |
| 9 | Run the same ten beef animals with one base population, then with two era groups. Plot both genetic trends | The MME with `Q`; what UPG assume |
| 10 | Take one calf's 220 kg apart by hand into direct and maternal contributions, using its dam's own record | The maternal MME with the direct–maternal covariance block |

### Part III — Advanced model structures

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 11 | Write out the 4 × 4 covariance of two traits on two sheep, cell by cell, asking of each cell "whose, which trait, what relationship?" — **before the symbol `⊗` is used at all** | `G₀ ⊗ A`, named as the thing just constructed; the multivariate MME |
| 12 | One cow, five test-days. Fit a straight line to her deviations by hand; plot it. Her "random effect" is visibly an intercept and a slope | The random regression model; `Φ`; why the effects are coefficients (the chapter's hardest idea, already seen before it is named) |
| 13 | One pen of three hens. Write the three rows of `Z_d` and `Z_s` by hand and notice each hen appears in her pen-mates' rows | `TBV = a_d + (n − 1)a_s` |

### Part IV — Categorical and time-to-event

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 14 | Fit an ordinary linear model to ten 0/1 stillbirth records and get a predicted probability outside [0, 1]. Then one iteration of the threshold model, by hand | Liability; the threshold model |
| 15 | Compute mean days-to-removal for ten cows two ways — censored records treated as complete, then as removals — and get two wrong answers | Censoring; the hazard formulation |

### Part V — Non-additive effects

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 16 | One full-sib pair. Enumerate the grandparental paths and arrive at ¼ by counting | The dominance relationship matrix `D`; the additive + dominance MME |
| 17 | Form `A#A` on the Chapter 16 pedigree and scatter its off-diagonals against `A`'s. The near-line is the chapter | Why epistatic variance is not estimable, and what that justifies about the rest of the book |

### Part VI — Multibreed and crossbred

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 18 | One F1 animal, evaluated under a single additive variance and then under breed-specific ones. Two numbers | Breed-specific covariance; segregation variance; `Γ` |
| 19 | Rank five boars on purebred slaughter weight, then on crossbred. Show the rank order swap | The two-trait formulation; `r_pc` and its consequences |

### Part VII — Variance components

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 20 | Five sires × four progeny. Compute the mean squares by hand and get σ²s. Then drop one sire and **watch the estimate go negative** | The expected-mean-square equations; why they had to be replaced |
| 21 | Evaluate the REML log-likelihood at three values of σ²a and plot the three points. On balanced data the peak sits where ANOVA landed | The REML likelihood; the AI update, as an efficient way to climb a curve the reader has now seen |
| 22 | Draw five samples by hand from the full conditionals, fixed seed, tabulated. Five rows of numbers | The Gibbs sampler; posterior summaries |

### Part VIII — Validation and computation

| Ch | Opening instance | Statement it earns |
|---|---|---|
| 23 | Two EBV columns — partial data and whole data — for animals born after a cutoff. Regress one on the other; the slope is 0.78, not 1 | The LR method statistics; accuracy vs bias vs dispersion as three separate failures |
| 24 | Time `solve()` on systems of growing size and tabulate. Then three Jacobi iterations on a 5-equation system, iteration by iteration | The cost of direct inversion; iterative solving; iteration on data |

---

## 11. Review checklist

Run against every drafted chapter. Five questions, all mechanically checkable.

1. Does any **Tier 1 box** contain a symbol or object the reader has not already seen carrying a
   number? *(If yes, the section is backwards.)*
2. Is there a **Pattern** paragraph between the hand solve and the first Key Equation box, and does
   it answer all three questions in §3? *(This is the beat that gets dropped.)*
3. Does every **Tier 3 derivation** sit *after* the box holding its result?
4. Is at least one **Check Yourself** placed immediately before the generalisation beat?
5. Are the **low-interactivity steps** (§6) given to the reader to do rather than worked for them?

---

## 12. Open questions

- **Chapter 1's section length.** §8 exempts Chapter 1's reference sections from a long instance,
  but "short enough that the rule is visible on the same screen" is a judgement, not a rule. Worth
  fixing a concrete budget — perhaps: instance ≤ 10 lines, rule within one screen — once §1.3 is
  drafted and we can see what it costs.
- **Does the reversal change the exercises?** Under the old order, exercises apply a stated rule.
  Under the new one, an exercise could plausibly *be* an instance the next section generalises.
  That is attractive but risks a chapter that cannot be read without doing the homework. Current
  recommendation: leave exercises as assessment, and put the generative work in Check Yourself
  boxes (§6), which are self-contained.
- **Do the manim clips need re-specifying?** §7 splits them into board work and structural and
  gives a criterion (does the difficulty lie in a *sequence* or in a *shape*?). Applied to
  Chapter 1 this already demotes four clips to static figures and promotes two — see
  `chapter_01_linear_algebra.md` §7. The other chapters' clip lists in `manim_videos.md` have not
  been re-read against it yet, and should be before any clip past Chapter 1 is built.

---

## References

Chen, O., Kalyuga, S., & Sweller, J. (2015). The worked example effect, the generation effect, and
element interactivity. *Journal of Educational Psychology*, 107(3), 689–704.
https://doi.org/10.1037/edu0000018

Fyfe, E. R., McNeil, N. M., & Borjas, S. (2015). Benefits of "concreteness fading" for children's
mathematics understanding. *Learning and Instruction*, 35, 104–120.
https://doi.org/10.1016/j.learninstruc.2014.10.004

Fyfe, E. R., McNeil, N. M., & Son, J. Y. (2014). Concreteness fading in mathematics and science
instruction: A systematic review. *Educational Psychology Review*, 26(1), 9–25.
https://doi.org/10.1007/s10648-014-9249-3

Kaminski, J. A., Sloutsky, V. M., & Heckler, A. F. (2008). The advantage of abstract examples in
learning math. *Science*, 320(5875), 454–455. https://doi.org/10.1126/science.1154659

McNeil, N. M., & Fyfe, E. R. (2012). "Concreteness fading" promotes transfer of mathematical
knowledge. *Learning and Instruction*, 22(6), 440–448.
https://doi.org/10.1016/j.learninstruc.2012.05.001

Prince, M. J., & Felder, R. M. (2006). Inductive teaching and learning methods: Definitions,
comparisons, and research bases. *Journal of Engineering Education*, 95(2), 123–138.
https://doi.org/10.1002/j.2168-9830.2006.tb00884.x

Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional
design: 20 years later. *Educational Psychology Review*, 31(2), 261–292.
https://doi.org/10.1007/s10648-019-09465-5
