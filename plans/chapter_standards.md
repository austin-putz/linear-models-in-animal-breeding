# Chapter standards — structure, callouts, and math tiers

The visual and structural contract every chapter honours. A student who has read Chapter 1 should
be able to navigate Chapter 17 without relearning where anything is.

Companion documents: [`pedagogical_order.md`](pedagogical_order.md) (**the order everything is
presented in — read it before this one**), [`manim_videos.md`](manim_videos.md) (where clips go),
[`manim_visual_standards.md`](manim_visual_standards.md) (colour inside the math).

This document says *what* is in a chapter and what it looks like. `pedagogical_order.md` says what
order it comes in, and where the two touch — the placement of Tier 1 boxes, the skeleton in §3 —
it governs.

---

## 1. The three math tiers

This is the answer to *"how does a student tell the derivation of BLUP from the MME they actually
need?"* Every displayed equation in the book is one of three tiers, and the tier is visible before
the equation is read.

| Tier | Looks like | The student must be able to | Budget |
|---|---|---|---|
| **1 — Key Equation** | Boxed, named, numbered `{#eq-...}` | Write it from memory and say what every symbol is | **1–3 per chapter** |
| **2 — Working math** | Ordinary display math in the flow | Follow it, and reproduce it with the book open | unlimited |
| **3 — Derivation** | Collapsed grey callout, closed by default | Know it exists and that the result is earned, not asserted | 0–3 per chapter |

**The mechanical signal: if an equation carries a `{#eq-...}` label, it is Tier 1.** Nothing else
gets a label. A reader flipping through sees the boxes and knows exactly what the chapter is
asking them to own.

### The placement rule

Tier 1 and Tier 3 are ordered by `pedagogical_order.md`, and the order is **instance, then box,
then derivation**:

```markdown
[ the worked instance — X, Z and A⁻¹ as literal numbers for six pigs, solved ]

[ the Pattern paragraph — what depended on the numbers, what on the shape,
  what would have been identical for any dataset ]

::: {.callout-important .key-equation}
## Key Equation — The Mixed Model Equations {#eq-mme}
...
:::

::: {.callout-note .derivation collapse="true"}
## Derivation — Henderson's mixed model equations (optional)

Skip this on a first read. You already have the result above; this shows it holds for
every dataset and not only the one you just solved.

[ the joint density, the differentiation, the algebra ]
:::
```

**The hard rule: a Key Equation box is never the reader's first sight of its own content.** If a
symbol appears inside a box before it has appeared attached to a number, the section is written
backwards. This is the first thing to check in review, and it is mechanically checkable.

The old property still holds and is strengthened: a student who never opens the grey box has now
met the MME *twice* — once solved, once boxed — instead of once. The derivation's job has changed
rather than shrunk. It no longer earns the result (the worked instance did that); it answers the
narrower question of why the result generalises.

Corollary: **never let a chapter's headline result appear only at the end of a derivation.** If it
does, the derivation is being asked to do a job that belongs to a box.

### What each tier looks like in Chapter 6

- **Tier 2 comes first** — building `X`, `Z`, `A⁻¹` for six named pigs; forming each block; the
  arithmetic of the solve. All of it in literal numbers.
- **Tier 1 second** — the MME itself; the EBV decomposition `EBV = PA + YD + PC`; accuracy from
  the diagonal of `C`. Three boxes, and that is the chapter's whole memorisation load. Each one
  names something the reader has already computed.
- **Tier 3 last, collapsed** — deriving the MME from the joint density of `y` and `u`; showing
  BLUP is the selection index with `b̂` estimated simultaneously.

Note that this inverts the usual textbook order of the tiers, which is the point. The reader
solves an 8 × 8 system for six pigs *before* the MME is written in general form.

A long Tier 3 derivation (more than roughly a page) moves to an appendix and the collapsed box
holds a four-line sketch plus the cross-reference. Appendix B already exists for the BLUP
derivation — that is exactly this pattern.

---

## 2. Callout taxonomy

Ten boxes. Each has one purpose, one fixed title prefix, and a budget. **Fixed titles are the
point** — students learn to recognise "Common Mistake" the way they recognise a road sign.

| Box | Markdown | Title form | Purpose | Per chapter |
|---|---|---|---|---|
| **Learning Objectives** | `.callout-note icon=false` | `Learning Objectives` | What you will be able to do | **1, required** |
| **Definition** | `.callout-note .definition` | `Definition — <term>` | A term the reader must be able to look up (§2b) | 0–8, **outside the cap** |

A chapter whose job is to establish the book's vocabulary may exceed the Definition budget, but
records it as an exception in its chapter plan. Chapter 1 is the only expected case.
| **Key Equation** | `.callout-important .key-equation` | `Key Equation — <name>` | Tier 1 math (§1) | 1–3 |
| **Derivation** | `.callout-note .derivation collapse="true"` | `Derivation — <what> (optional)` | Tier 3 math (§1) | 0–3 |
| **Check Yourself** | `.callout-caution .check collapse="true"` | `Check Yourself` | Predict before you read on | 2–3 |
| **Common Mistake** | `.callout-warning` | `Common Mistake — <what>` | The error students actually make | 0–3 |
| **In R** | `.callout-tip` | `In R — <what>` | An R-specific trap or idiom | 0–4 |
| **Notation Watch** | `.callout-note .notation` | `Notation Watch — <symbol>` | Where the literature disagrees | 0–2 |
| **In Practice** | `.callout-note .practice` | `In Practice — <where>` | What national evaluations really do | 0–2 |
| **Beyond This Book** | `.callout-note .beyond` | `Beyond This Book — <topic>` | Scope boundary + forward pointer | 0–2 |

**Hard cap: 15 boxes per chapter**, counting every box *except* Definition (§2b). Past that they
stop being signals and become wallpaper — the reader starts skipping every coloured rectangle,
including the Key Equations.

### Notes on the less obvious ones

**Check Yourself** is the page's version of the animation hold rule: the question is visible, the
answer is collapsed. It sits at the moment the reader is about to be told something they could
have predicted — *"α is 1.2 here. Before reading on: will animal 4's EBV shrink more or less than
animal 2's, and why?"* This is distinct from end-of-chapter exercises, which are graded work;
Check Yourself is a five-second self-test that costs nothing to fail.

**At least one sits immediately before the generalisation beat** (§3, beat 8) — after the worked
instance and before the general form. That is the one point in a chapter where a prediction is
both possible and not yet spoiled: *"you solved this for six pigs and got an 8 × 8 system. For 600
pigs in 12 contemporary groups, how large is the system, and which block grew?"*

Check Yourself is also where the reader does the work rather than watching it. Give them the steps
that stand alone — building `X` and `Z` from a table, transposing, forming `P = G + R` — and work
the steps whose pieces are meaningless separately (assembling the MME blocks, Henderson's rules,
an AI-REML update) in front of them. `pedagogical_order.md` §6 has the full split and the evidence
for it.

**Notation Watch** is only for genuine conflicts in the literature — `α` vs `λ` for the variance
ratio, `u` vs `a` for the breeding value, EBV vs EPD vs ETA. Defining a symbol on first use is
prose, not a box (CLAUDE.md already requires it). Every Notation Watch points at Appendix A, which
stays authoritative.

**Beyond This Book** is how CLAUDE.md's scope rule is enforced visually. Genomic successors and
large-scale computation get one or two sentences and a pointer to the companion volume, inside a
box that is visibly a signpost rather than content. This makes it obvious in review when a section
has started teaching something out of scope.

**In Practice** is what keeps this from being a maths book. One or two per chapter, naming a real
evaluation — what the US dairy evaluation actually does with unknown parent groups, why a swine
company runs weekly rather than daily.

### 2b. Definition boxes

**A key term gets a box, not bold text.** When a chapter introduces a word the student will be
expected to use for the rest of the book — *singular*, *rank*, *estimable*, *positive definite*,
*conformable*, *linear combination* — bolding it inside a paragraph is not enough. A definition
buried in prose cannot be found again three chapters later, which is exactly when it is needed.

Each box holds three things, in this order and nothing else:

1. **The term**, in the header: `Definition — Singular matrix`
2. **What it is**, in one or two sentences. Plain language first; the formal condition second if
   the two differ.
3. **Why it matters here**, in one or two sentences, under a bold `**Why it matters.**` lead. This
   is the half that stops the box being a glossary entry — it says what goes wrong if you do not
   know the term, and names the chapter where it returns.

**They sit outside the 15-box cap.** The cap exists so that *teaching signals* — the boxes asking
you to memorise, predict, or beware — do not become wallpaper. A Definition box is not competing
for that attention; it is reference furniture the reader scans past until the moment they need it,
like a glossary printed in the margin. Eight in a vocabulary-heavy chapter is fine; eight Common
Mistakes would not be.

**Where they go.** Immediately after the term is first used in context, never before. The rule
from `pedagogical_order.md` still binds: the reader meets a singular matrix — sees a column that
is the sum of two others, watches the determinant come out zero — and *then* gets the box that
names it. A Definition box that arrives before its own instance is the same error as a Key
Equation that does.

**What does not get one.** A symbol defined on first use is prose, not a box (`CLAUDE.md`
already requires that). A word used once and never again is prose. A term whose meaning is
obvious from the surrounding sentence is prose. Reserve the box for vocabulary the reader will be
held to.

### Provenance notes are prose, not callouts

A note on where a result came from — who proved it, when, and what it superseded — is ordinary
text with `[@key]` citations in it, or a `### Where this material comes from` subsection. It is
**not** a *Beyond This Book* box: that box marks a **scope boundary**, something this book
deliberately does not teach. Using it for history inflates the callout count and blunts the one
signal that is supposed to mean "we stop here."

### Callout colours are deliberately not the animation palette

The manim palette encodes *what a quantity is in the model*. Callout colours encode *what the
reader should do with this box*. They are different alphabets on different surfaces, and making
them rhyme would imply a relationship that does not exist. Do not unify them.

---

## 2a. R code is visible

`code-fold` is **off** book-wide. Beats 10 and 11 of the skeleton below, and every interleaved
chunk in a reference chapter, render with their source shown.

This is a pedagogical decision, not a formatting one, and it binds on how the code is written:
a chunk a student cannot read straight down and retype has failed even if it produces the right
number. `CLAUDE.md`'s **Code visible** rule is authoritative and lists what that requires — one
idea per chunk, book notation for object names, printed results that match the hand answer,
comments on the modelling step rather than the syntax, and the explicit form before the
idiomatic one.

Two consequences for this document. **In R** callouts carry the idiomatic shortcut *after* the
explicit form has appeared in a visible chunk, so the box is an upgrade rather than the reader's
first contact. And a chunk long enough to bury the section it belongs to is a sign the section is
doing too much — split the chunk before reaching for `code-fold`, which is reserved for
incidental code that teaches nothing.

---

## 3. Chapter skeleton

Required beats, in order. Chapter-specific sections from `CHAPTERS.md` slot into steps 4–7; the
opening and closing beats are fixed.

| # | Beat | Contents |
|---|---|---|
| 1 | **Title** | `NN-slug.qmd`, numbered by `_quarto.yml` |
| 2 | **Learning Objectives** | The box. 3–5 numbered items, verb first, matching `CHAPTERS.md` |
| 3 | **Prerequisites** | One italic line: *Assumes Ch 2 (**X**), Ch 4 (**A⁻¹**).* |
| 4 | **Why this chapter** | The problem, in breeding terms, before any algebra. Chapter-opener clip goes here |
| 5 | **The toy dataset** | 5–10 animals, shown as a table, species named. Not inlined — read from `data/` |
| 6 | **The matrices for *these* animals** | Literal integer arrays for this dataset. **No general dimensions, no Tier 1 boxes.** A symbol is introduced as a name for an array already printed, never as a placeholder for one to come |
| 7 | **Solve by hand** | Tier 2 arithmetic, every step. Board-work clips and the Common Mistake box live here |
| 8 | **The general form** | The Pattern paragraph (three questions, `pedagogical_order.md` §3), then every Tier 1 box, then any Tier 3 derivation, collapsed. A Check Yourself sits immediately before this beat |
| 9 | **Interpret the answer** | What the numbers mean to a breeder. **Never skip this** — the beat most often dropped and the one students most need |
| 10 | **The same model in R** | Explicit matrix code first, then the one-line package call. Both must reproduce the hand answer exactly |
| 11 | **Scale up** | The larger dataset, same trait, same model |
| 12 | **Further reading** | 3–6 sources, each one line on *what it is for* and *when to reach for it*. Written as advice, not a list. Every entry verified through the scite tool and present in `references.bib` with a DOI (CLAUDE.md, *Citations and references*) |
| 13 | **Key equations** | Recap listing this chapter's Tier 1 boxes by `@eq-` reference |
| 14 | **Exercises** | Count per `CHAPTERS.md`; solutions to Appendix H |

**Beats 8 and 9 are the two to defend in review**, and they fail in opposite directions. A chapter
that stops after beat 7 has taught arithmetic on six pigs and left the reader unable to recognise
the same model anywhere else. A chapter that stops after beat 8 has taught algebra, not breeding.
Both are dropped under deadline; neither is optional.

A reference chapter with many small results (Chapter 1) runs beats 6–8 once per section rather
than once per chapter. Record that as a documented exception in the chapter plan.

**Appendix A gains a key-equation index** — every Tier 1 box in the book, one line each, with its
`@eq-` cross-reference. That single page is what a student revises from.

---

## 4. Writing the objectives

They are a contract, and they are what the exercises are written against.

- 3–5 per chapter, numbered, **verb first**: *Build*, *Solve*, *Interpret*, *Explain*, *Diagnose*.
  Never *Understand* or *Be familiar with* — neither can be assessed, so neither can be a promise.
- Bold the verb and the object, as in the linear models book; the bolding is what makes the list
  scannable at a glance.
- Every objective is testable by at least one exercise in that chapter. If nothing tests it, either
  write the exercise or cut the objective.
- They are copied verbatim from `CHAPTERS.md`, which stays the source of truth. If a chapter
  drifts, fix `CHAPTERS.md` first.
- Manim scene docstrings cite these by number (`# Ch 6, objective 3`), so the numbering is a real
  interface — do not renumber casually.

---

## 5. Files

- `templates/chapter-template.qmd` — the skeleton, with every box shown once, filled with
  instructional placeholder text. Copy it to start a chapter.
- `styles/custom.css` — carries `.key-equation`, `.derivation`, `.check`, `.notation`,
  `.practice`, `.beyond`, in both light and dark themes.

**Known issue to fix before the first chapter ships:** the existing `styles/custom.css` hardcodes
light backgrounds (`#f2f2f2` table striping, `#d1ecf1` callouts) with no dark-theme override, and
`_quarto.yml` ships `darkly` as the dark theme. Every table and callout will be unreadable in dark
mode. The new classes added for this standard are theme-aware; the pre-existing rules are not.

---

## 6. Pedagogical order

The order of presentation is governed by [`pedagogical_order.md`](pedagogical_order.md), not by
this document. In one line: **numbers before symbols** — every result is presented as
Instance → Pattern → Statement, and no general form precedes the worked instance that earns it.

Three of that standard's rules bind directly on this one and are reproduced above so they cannot
be missed: the placement rule (§1), the Check Yourself position (§2), and beats 6–8 of the
skeleton (§3).
