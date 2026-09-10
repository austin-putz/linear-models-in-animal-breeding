# Manim visual standards

Extends `~/Claude/manim_test/CLAUDE.md`. Nothing in that file is overturned; this adds the axes
and grammars needed to cover the whole book rather than one BLUP explainer.

**When `manim/` is created in this repo, this file becomes `manim/CLAUDE.md`.**

---

## 1. One meaning per channel

The original rule — *colour encodes the role a quantity plays in the model, and nothing else* — is
right, and it breaks the moment a chapter has two random effects. The fix is not more hues. It is
to say what each **visual channel** is allowed to mean, and to never overload one.

| Channel | Encodes | Values |
|---|---|---|
| **Hue** | What *kind* of quantity this is | 8 roles, §2 |
| **Tint** | *Which one* of that kind — direct vs maternal, trait 1 vs 2, herd 1 vs 2 | 2 (rarely 3) per hue, §3 |
| **Fill state** | Observed vs latent; pending vs active vs settled | §4, §5 |
| **Emphasis** | Sign or valence only | `POS` / `NEG`, unchanged |

A student who has learned "teal is random structure" must never have to also learn "bright teal
means something else." **Attention is not a hue.** The cell currently being computed is marked by
stroke and scale, never by a colour change (§5) — otherwise every step-by-step calculation
animation collides with the role system on its first frame.

There are ~8 hues a viewer can hold apart on a dark background. The book has ~40 distinct
objects. Hues are the scarce resource; spend them only where §2 says.

---

## 2. Hue roles

Unchanged from the original, with one addition.

| Name | Hex | Role |
|---|---|---|
| `DATA` | `#e8b64c` amber | Given data, or a pure re-organisation of it — `y`, phenotypes, `X'y`, `Z'y`, the RHS |
| `FIXED` | `#5aa9e6` blue | Fixed-effect structure you build — `X`, `X'X`, herd/breed/group panels |
| `RANDOM` | `#3fd0b0` teal | **Genetic** random-effect structure — `Z`, `Z'Z`, `Z'Z + A⁻¹α` |
| `ENVR` | `#5cb2ab` drained teal | **Non-genetic** random-effect structure — permanent environment, common litter environment | 
| `LINK` | `#a8c0d8` steel | Fixed × random cross blocks — `X'Z`, `Z'X` |
| `SOLVE` | `#f0879f` rose | The unknowns — `b`, `u`, `b̂`, `û`, the solution vector, predictions |
| `RESID` | `#9a9a94` grey | Residual — `e`, and the residual of a linear system in Ch 24 |
| `VAR` | `#b98cf0` violet | Variance / relationship structure — `A`, `A⁻¹`, `D`, `G₀`, `λ`, `h²`, `C`, PEV, accuracy |

**Why `ENVR` is the one new hue.** Chapter 8's entire teaching point is that a second random
effect has appeared and *it is not genetic*. If permanent environment shares teal with the
breeding value, the chapter's thesis is invisible. It is deliberately teal with the colour drained
out — same family (random structure you build), visibly less alive. It is not a new *kind* of
object, so it is not a new *hue*; it is teal, demoted.

Theme colours (`BG` `#101826`, `TITLE` `#f5efe4`, `BODY` `#dfe5ee`, `SUBTEXT` `#7f8da4`) and
emphasis (`POS` `#5fbf7f`, `NEG` `#e2685f`) are unchanged. Headings and captions are never a role
colour.

### Every object in the book, and where it lands

Nothing below needs a new hue. Work down this table before inventing anything.

| Ch | Object | Colour | Note |
|---|---|---|---|
| 1 | any matrix with no model role yet | `BODY` | Ch 1 is pre-semantic; brackets and cells are neutral, the *grammar* (§7) does the teaching |
| 2 | `X`, `X'X` / non-full-rank column | `FIXED` / `FIXED` + `NEG` outline | the offending column is a warning, not a role |
| 3 | `Z`, `Z'Z` / `û` | `RANDOM` / `SOLVE` | |
| 4 | `A`, `A⁻¹` / pedigree node / unknown parent | `VAR` / `BODY` / latent (§4) | |
| 5 | contemporary group panel / disconnected block | `FIXED` / `NEG` outline | |
| 6 | the four LHS blocks / `α` / `C`, PEV, accuracy | `FIXED` `LINK` `RANDOM` / `VAR` / `VAR` | as already built |
| 6 | animal with no record | latent `DATA` (§4) | the same rule as liability and censoring |
| 6 | PA, YD, PC | `SOLVE` tints 0/1/2 | three parts of one EBV — tints, not hues |
| 7 | animal → sire → sire–MGS `Z` | `RANDOM`, dimming as data is discarded | |
| 8 | `pe`, `c²` structure / their solutions | `ENVR` / `SOLVE` tint 1 | |
| 9 | `Q` / `ĝ` | `FIXED` tint 1 / `SOLVE` tint 1 | groups are structure; their effects are unknowns |
| 10 | `Z_d`, `Z_m` / `â`, `m̂` / `G₀` 2×2 | `RANDOM` tints 0,1 / `SOLVE` tints 0,1 / `VAR` | |
| 11 | `G₀ ⊗ A` / trait 1, trait 2 | `VAR` / tint index = trait | |
| 12 | Legendre basis `Φ` / regression coefficients / fitted curve | `RANDOM` / `SOLVE` / `SOLVE` | time axis is `SUBTEXT` |
| 13 | direct, indirect `Z` / `â_D`, `â_S` | `RANDOM` tints 0,1 / `SOLVE` tints 0,1 | same shape as maternal, deliberately |
| 14 | observed category / **liability** / thresholds | `DATA` / latent `DATA` / `VAR` | |
| 15 | event / **censored** record / time | `DATA` / latent `DATA` / `SUBTEXT` | |
| 16–17 | `D`, `A#A`, `A#D` | `VAR` tints 1, 2 | all the same *kind* of object — that is the lesson |
| 18–19 | breed panel / purebred vs crossbred record / **unobserved crossbred performance** | `FIXED` tints / `DATA` tints 0,1 / latent `DATA` | |
| 20–22 | `σ²a`, `σ²e`, posterior, likelihood surface | `VAR` | a *variance of* something takes `VAR`, not that thing's hue |
| 22 | chain history | `VAR` at 25%, current draw at 100% | state, not hue (§5) |
| 23 | realized vs predicted | `DATA` vs `SOLVE` | the whole chapter in two colours already in the system |
| 24 | iterate `k` / system residual | `SOLVE` at rising opacity / `RESID` | |

---

## 3. Tint — *which one*

`tint(base, i)`: `i=0` the base hue; `i=1` mixed 34% toward `TITLE`; `i=2` mixed 30% toward `BG`.
The existing `HERD_CL = ["#8ecbf5", "#4f9edb"]` is this idea already — two tints of `FIXED`,
because a herd *is* a fixed effect.

| Role | i=0 | i=1 | i=2 |
|---|---|---|---|
| `DATA` | `#e8b64c` | `#ecc980` | `#a78741` |
| `FIXED` | `#5aa9e6` | `#8fc1e5` | `#447eac` |
| `RANDOM` | `#3fd0b0` | `#7ddbc2` | `#319987` |
| `SOLVE` | `#f0879f` | `#f2aab6` | `#ad667b` |
| `VAR` | `#b98cf0` | `#cdaeec` | `#8669b3` |

Rules:

- **Two tints. Three only when the model genuinely has three** (a 3-trait `G₀`, the PA/YD/PC
  decomposition). Four is not distinguishable at phone size; use position or labels instead.
- **The tint index is announced on screen the first time it appears** and holds for the whole
  clip: "teal = direct, pale teal = maternal", top-left, `SUBTEXT`.
- **Index order is fixed by convention:** 0 = the effect on the animal itself (direct, trait 1,
  purebred, additive); 1 = the second-order or partner effect (maternal, social, trait 2,
  crossbred, dominance). A student who sees pale-teal in Ch 10 and again in Ch 13 should feel the
  parallel, because it is a real one.
- Tint index means different things in different chapters (trait in Ch 11, direct/maternal in
  Ch 10). That is fine and unavoidable — it is always scoped to the clip and always announced.

---

## 4. Latent — the same colour, dashed

**Anything real but unobserved is drawn in its own role colour, dashed, at 45% opacity.**

One rule, six chapters:

| Chapter | What is latent |
|---|---|
| 4, 9 | an unknown parent |
| 6 | an animal with no record of its own (but an EBV all the same) |
| 14 | the liability scale under an observed 0/1 |
| 15 | a censored record — the event that has not happened yet |
| 19 | the crossbred performance of a purebred selection candidate |
| 21–22 | the true parameter a chain is estimating |

This teaches the relationship instead of inventing a colour for it: **liability is amber because
it is the phenotype we would have measured if we could.** When a latent quantity is later
predicted or realised, the dashes close and the opacity comes up to 100% — a single animation that
*is* the statistical point.

---

## 5. State — attention without hue

Three states, applied to cells, blocks, or whole matrices:

| State | Fill | Stroke | Scale |
|---|---|---|---|
| **Pending** — not yet computed | role colour, 35% | none | 1.00 |
| **Active** — being computed now | role colour, 100% | `TITLE` 2 px | 1.06 |
| **Settled** — done | role colour, 100% | none | 1.00 |

The active marker is a **cream stroke and a 6% scale pulse** — no hue anywhere in it, so it
composes with every role colour and never lies about what kind of object it is. This is the
channel that makes step-by-step calculation work, so it must stay clean.

Sources feeding an active cell are joined to it by a thin `SUBTEXT` line while it is active, and
the line goes when the cell settles.

---

## 6. Colour is never the only channel

The book ships a PDF whose figures are the poster stills, some readers are colour-blind, and
`DATA` amber, `POS` green, and `NEG` red converge badly under deuteranopia and protanopia.

- **Every role-coloured object carries its symbol or a `SUBTEXT` label** — `X`, `Z`, `A⁻¹`, `û`.
  Colour is *redundant* encoding that makes the structure fast to read; it never carries meaning
  alone.
- `POS`/`NEG` never appear next to `DATA` without an explicit `+` / `−` glyph.
- Every matrix gets its dimension tag on first appearance — `4 × 2` in `SUBTEXT` beneath the
  bracket. This is CLAUDE.md's "state the dimensions of every matrix," enforced visually.
- A frame must still be readable in greyscale. If it is not, position or labelling is doing too
  little work.

---

## 7. Grammars — how each kind of calculation is animated

The same operation must look the same in Chapter 1 and in Chapter 17. A student learns the visual
grammar once and then reads every later clip fluently.

| Calculation | Choreography |
|---|---|
| **Element-wise** (add, subtract, Hadamard) | Operands hold position. Corresponding cells pulse **together**, result cell appears in a third matrix below. Nothing travels — the point is that position is preserved. |
| **Row × column** (matmul, `X'X`, `X'y`) | Row *i* goes active; column *j* goes active; both copies detach and rotate to meet above the target cell; the products appear in a row; they collapse to a sum; the sum drops into cell (*i*,*j*). The inner dimensions visibly cancel in the dimension tags. **This is the single most reused sequence in the book — build it once as a helper.** |
| **Transpose** | Rotation about the main diagonal, with diagonal cells held fixed as the anchor. Never a fade-and-replace. |
| **Assembly** (blocks → a larger matrix) | Each block keeps its own role colour and *slides* to its position; off-diagonal `LINK` blocks settle at 80% so the eye lands on the diagonal first. Row and column registration must be visibly exact — this is what `GridMatrix` exists for. |
| **Inversion** | Never animate the arithmetic of an inverse; it teaches nothing. Animate the *check*: `A A⁻¹` sweeping to `I`, ones landing on the diagonal, zeros elsewhere. |
| **Solving** | Substitution: the solution vector's values travel back into the equation and both sides settle to the same number. |
| **Recursion / accumulation** (tabular `A`, the `A⁻¹` rules) | A cursor walks cells in fixed order. Settled cells lock (§5). The active cell shows its source cells linked by `SUBTEXT` lines. The walk order *is* the algorithm — never fill cells all at once. |
| **Shrinkage** | A value slides along a number line toward an anchor line (the mean, the parent average). `α` or `λ` shown as the thing controlling the distance. Used in Ch 3, 6, 7. |
| **Distribution / latent scale** | Density curve with the observed data as amber ticks beneath; thresholds are `VAR` vertical rules; area under the curve fills to show a probability. |
| **Iteration / convergence** | The *path* is the subject. History at 25% opacity, current state at 100%. **Build in R with `gganimate`**, not manim — the numbers come from the chapter's own chunk. |

---

## 8. Where things live on screen

Consistent placement across the book is a memory aid: a student should recognise the LHS by
where it is before reading it.

- Heading: `to_edge(UP, buff=0.45)`, `TITLE`. Caption: `to_edge(DOWN, buff=0.5)`, `SUBTEXT`,
  under 80 characters.
- Object-level labels attach to the object, not to the caption line. A cell's value is explained
  next to the cell — never four inches away at the bottom of the frame.
- The model equation reads left-to-right in its book order: `y = Xb + Zu + e`. Anything derived
  from a term appears **below** that term, never on the other side of the frame.
- In an MME frame: LHS left, RHS right, solution vector to the right of the equals — the same
  arrangement as the printed equation in the chapter, so the video and the page are the same
  picture.

---

## 9. Timing, and the hold

An animation a student watches passively teaches less than a static figure they had to read.
Every clip is built to force one prediction.

- **No reveal without a hold.** Before a result appears, the question is on screen and the frame
  holds for **1.5–2.0 s**. `self.wait(1.75)` is the standard beat.
- One idea per clip. **No more than five new symbols in a single clip** — if there are more, it
  is two clips.
- Inline clips 20–75 s; `build.py` warns above 90 s. Chapter features 2–4 min.
- **The first frame shows the object in the notation the chapter uses**, so a student scrubbing
  the timeline knows instantly what they are looking at. No cold opens.
- No audio, ever. Captions carry the narration; the clip must work muted, in a library, and as a
  still in print.
- **A clip is never load-bearing.** Everything in it is also in the text — PDF readers and
  screen-reader users get the poster frame only. The clip makes a hard thing fast; it is never
  the only place the thing is said.

---

## 10. Acceptance test

`manim/ambook/swatches.py` defines `StyleSwatches`, a single scene rendering every role, every
tint, the three states, and a latent example. It is the palette's regression test and the first
thing to re-render after any change here.

Before a new colour or grammar is added to this file, the swatch card must pass:

1. Readable at 320 px wide (phone, video at half screen).
2. Adjacent roles remain distinct under a deuteranopia simulation.
3. Readable converted to greyscale.
4. Every role still has a text label, so failing 1–3 degrades gracefully rather than silently.

## 11. Adding to this standard

In order of preference: **use an existing hue** → **use a tint** → **use the latent or state
axis** → **use position or a label**. A new hue is the last resort, needs a genuinely new *kind*
of quantity, must sit ≥30° from every existing role on the wheel, and must be added here with its
rationale and to `StyleSwatches` in the same commit.
