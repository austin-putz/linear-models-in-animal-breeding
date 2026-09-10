# Plan — Manim animations for the book

**Status:** vertical slice built and proven end to end (2026-09-09). `manim/`,
`_extensions/animation/` and `assets/video/` exist; `ch01-matmul` is rendered and embedded in
Chapter 1, verified in both HTML and PDF. The remaining 7 Chapter 1 clips and all later chapters
are still to build.
**Date:** 2026-09-03, updated 2026-09-09

Animated explainers rendered with [Manim Community](https://www.manim.community/), embedded in
the Quarto chapters, degrading to a still figure in the PDF.

---

## 1. What already exists

`~/Claude/manim_test/` is a working Manim project with two finished BLUP explainers. It is not a
prototype — it already has the hard part solved:

| File | Scene | Length | Covers |
|---|---|---|---|
| `blup_demo.py` | `BLUPExplainer` | ~1.5 min | Why BLUP exists: herds confound raw performance |
| `blup_construction.py` | `BLUPConstruction` | ~2.8 min | Every matrix, the MME, the inverse, accuracy |
| `blup_common.py` | — | — | Palette, worked data, `GridMatrix`, cow/card mobjects |

Its `CLAUDE.md` documents a **colour-role system** (colour encodes the role a quantity plays in
the model — `FIXED` blue, `RANDOM` teal, `DATA` amber, `SOLVE` rose, `VAR` violet, …) and a
`GridMatrix` mobject that puts every cell on a fixed pitch so separately-built matrices register
when they drop into the assembled MME. That is a real asset and this plan is built on top of it,
not beside it.

**Environment (verified 2026-09-03):** manim 0.21.0, Python 3.13.2 in `manim_test/venv`;
MacTeX / TeX Live 2020 with `latex` + `dvisvgm`; cairo, pango, pkgconf via Homebrew; ffmpeg at
`/usr/local/bin/ffmpeg`. `media/Tex/` is full of successfully rendered `.svg`, so the `MathTex`
pipeline works end to end. Nothing needs installing.

---

## 2. Decisions

Each decision states what we do. Where a reasonable alternative exists it is recorded as **Not
now** so we do not re-litigate it later.

### D1 — Embed with our own Quarto shortcode

Write a small Lua shortcode in `_extensions/animation/`, used as one line in a `.qmd`:

```markdown
{{< animation ch06-assemble-mme caption="The four blocks drop into the LHS" >}}
```

It resolves `assets/video/ch06-assemble-mme.{mp4,png}` and emits format-appropriate output
(§5). ~40 lines of Lua, written once, used everywhere.

**Why not the built-in `{{< video >}}` shortcode.** Tested here on Quarto 1.9.37: in HTML it
works and wraps the file in video.js; in **PDF it degrades to the literal text `t.mp4`** — not a
link, not a figure. Unusable for a book that ships a PDF.

> **Not now:** hand-written `::: {.content-visible when-format="html"}` / `when-format="pdf"`
> div pairs at every call site. Works, no infrastructure, but it is ~8 lines of boilerplate
> repeated 40+ times and every one is a chance to get the fallback wrong. Reconsider only if the
> Lua extension turns out to fight Quarto's figure numbering.

### D2 — Render as a separate pass; commit the mp4s

Manim never runs inside `quarto render`. It is a build pass of its own, exactly parallel to the
existing `data-raw/` → `data/` convention: source of truth in `manim/`, generated artefact
committed in `assets/video/`.

```bash
python manim/build.py          # re-render only scenes whose source is newer than its mp4
python manim/build.py ch06     # one chapter
```

Committed mp4s mean the **GitHub Actions workflow needs no changes at all** — no manim, no
cairo, no second LaTeX install in CI. Videos are just files in `assets/`. At 1080p30 a 45-second
clip is roughly 0.5–2 MB; 40 clips lands near 30–60 MB, which plain git handles.

> **Not now:** rendering in CI. Adds a heavy toolchain to every build for no reader-visible gain.
> **Not now:** Git LFS. Revisit if `assets/video/` passes ~150 MB.
> **Never:** a knitr chunk that shells out to manim during render. It would fight `freeze: auto`
> and make a full rebuild take an hour.

### D3 — Promote `manim_test` into this repo as a package

Move `blup_common.py` in as `manim/ambook/style.py` (palette, `GridMatrix`, mobject helpers) and
its colour-role documentation into `manim/CLAUDE.md`. Scene files become per-chapter modules.
The existing two scenes come along as the first Chapter 6 assets (§7).

> **Not now:** keeping `manim_test` a separate repo and copying rendered mp4s over. Cheap today,
> but the style module and the book's worked examples must stay in lockstep (D5), and two repos
> guarantees they will not.

### D4 — Dark background only, for now

`blup_common` sets `config.background_color = "#101826"` and the whole role palette was chosen
for contrast against it. The book ships cosmo (light) + darkly (dark), so a dark video sits
oddly on a light page — accept that for the first pass.

> **Not now:** rendering every scene twice (light/dark) and toggling with `body.quarto-dark` CSS.
> This is *not* just a background swap — amber `#e8b64c` and cream `#f5efe4` fail contrast on
> white, so a light mode needs a parallel palette with the same role names at ~20% lower
> lightness. Design `style.py` so the palette is selected by an env var from day one, then the
> light set is an afternoon's work whenever we want it, and `build.py` gains one loop.

### D5 — One source of truth for the numbers

CLAUDE.md already requires the hand answer and the R answer to match. A video is a *third* copy
of those numbers and it will drift. For chapters where a full worked example appears in the
video, the toy dataset lives in `data/` and is read by both the `.qmd` and the scene module.
For Chapter 1's throwaway 2×2s, hardcoding in the scene is fine.

**Live conflict to resolve first:** `blup_construction.py` uses 305-day milk on four cows,
h² = 0.25, λ = 3. `CHAPTERS.md` Ch 6 specifies **pigs, ultrasound backfat, ~6 animals,
h² ≈ 0.45, α ≈ 1.2**, with documented reasons (measured once, on the animal, no maternal
component; α ≈ 1.2 keeps EBVs visibly separated). Recommendation: **re-cut the construction scene
onto the book's backfat dataset** and keep the milk version as a standalone lecture video. The
integer-clean arithmetic will need re-engineering for the new α, which is the main cost.

### D6 — Two kinds of video, not one

| | **Inline clip** | **Chapter feature** |
|---|---|---|
| Length | 20–75 s | 2–4 min |
| Placement | mid-section, at the step it illustrates | chapter opener or closer |
| Count | 2–5 per chapter where warranted | 0–1 per chapter, ~8 in the book |
| Autoplay | no; poster + `preload="none"` | no |
| Also useful as | — | standalone lecture / YouTube |

The existing `BLUPConstruction` is a chapter feature. Its `construct()` is already split into
methods (`build_y`, `build_fixed`, `lhs_blocks`, `assemble`, `invert`, `accuracy`), so carving
standalone inline clips out of it is close to mechanical.

---

## 3. Layout

```
manim/
  CLAUDE.md                 # colour-role system + production conventions (from manim_test)
  requirements.txt
  ambook/
    __init__.py
    style.py                # palette (dark now, light later), GridMatrix, helpers
    data.py                 # loads data/ CSVs so scenes and .qmd share numbers
  ch01_matrix_algebra.py    # Ch01MatMul, Ch01Transpose, Ch01Inverse2x2, ...
  ch04_relationships.py
  ch06_animal_model.py
  build.py
assets/video/
  ch06-assemble-mme.mp4
  ch06-assemble-mme.png     # poster = last frame, for the PDF
_extensions/animation/
  _extension.yml
  animation.lua
```

Naming: scene class `Ch06AssembleMME` in `ch06_animal_model.py` → asset `ch06-assemble-mme`.
The asset stem is the only thing a chapter author types.

## 4. `build.py` contract

1. Read a manifest (a list of `(module, SceneClass, stem)` at the top of `build.py` — a
   separate YAML is not worth it at this scale).
2. Skip any scene whose `.mp4` is newer than both its module and `ambook/`.
3. Render `manim -qh --format=mp4` for the clip and `manim -qh -s` for the poster still — the
   final frame of a well-built scene is exactly the static figure a print reader should see.
4. Copy both out of manim's nested `media/videos/<module>/<res>/` into `assets/video/<stem>.*`.
5. Warn on any inline clip over 90 s and any scene missing an objective line in its docstring
   (§8) — cheap guards that keep the series disciplined.
6. `--force` to ignore mtimes; a bare chapter prefix argument to filter.

## 4a. What the vertical slice changed (2026-09-09)

Three things in D1/section 5 did not survive contact and are corrected here.

1. **The PDF branch must be raw LaTeX, not a pandoc `Figure`.** Returning either a
   `pandoc.Figure` or a bare `pandoc.Para` from a shortcode fails inside Quarto's own filter with
   `object has no __toinline metamethod`. A pandoc `Image` also makes pandoc emit
   `\includegraphics[alt={...}]`, and the LaTeX `alt` key is undefined in the book class, which
   fails the build outright. The shortcode now emits a `\begin{figure}[htbp]` float directly.
   LaTeX numbers it, so print readers still get a numbered figure.
2. **Poster stills need a project `resources` entry.** Quarto discovers the mp4 from the
   `<source src>` tag but not the poster from the `poster=` attribute, and
   `quarto.doc.add_resource()` does not reach the book's resource collection from inside a
   shortcode. `_quarto.yml` now carries `resources: [assets/video/**]`. Without it the video
   opens on a black frame in the deployed book.
3. **Raw HTML paths are not rewritten by Quarto.** A chapter one directory down must reach the
   project root itself; the shortcode uses `quarto.project.offset` to build the prefix.

Confirmed working as designed: the mtime skip, the manifest duplicate-stem check, the objective
line warning, and the `-s` poster render landing on exactly the final frame.

---

## 5. Shortcode behaviour

**HTML**

```html
<figure class="animation">
  <video controls muted playsinline preload="none"
         poster="assets/video/STEM.png" width="100%">
    <source src="assets/video/STEM.mp4" type="video/mp4">
  </video>
  <figcaption>CAPTION</figcaption>
</figure>
```

`preload="none"` matters: a chapter with five clips would otherwise pull tens of MB before the
reader scrolls past the first heading.

**PDF** — the poster still as a normal numbered figure, caption suffixed with a short URL to the
HTML book so a print reader can find the animation.

**Gotcha found in testing:** a raw `<video>` tag written directly inside a `:::` fenced div
swallows the closing `:::` unless a blank line separates them — pandoc reads the two lines as one
raw HTML block and the div silently never closes. Another reason to hide this inside Lua (D1).

---

## 6. When does a video earn its place?

Animations are underused in this material, but "more videos" is not the goal — the goal is a
video wherever motion carries information a static figure cannot. Use this test.

### The governing criterion: prose is bad at sequence

A paragraph that says *"take row i, pair it term by term with column j, multiply, sum, and that is
element c_ij"* asks the reader to run a process in working memory while reading about it. That is
the one thing writing cannot do, and it is why every good teacher walks to the board for matrix
multiplication rather than describing it. A paragraph saying *"X'X is symmetric"* is a statement
about an object, and prose handles that perfectly.

> **A clip earns its place when the difficulty is a sequence of steps. When the difficulty is the
> shape of an object, a static figure is as good and costs a fraction as much.**

This splits the clips into two kinds, which should not be budgeted as if they were one
(`pedagogical_order.md` §7):

| | **Board work** | **Structural** |
|---|---|---|
| Shows | A specific calculation, real numbers, one step at a time | Shape, assembly, relationship — no arithmetic |
| Answers | *How is this done?* | *What is this thing?* |
| Is the… | **Instance** move | **Pattern** move |
| Examples | `ch01-matmul`, `ch01-cholesky`, Jacobi iterating, a Gibbs sweep | `ch01-kronecker`, `ch01-var-linear`, the MME's four blocks dropping in |

Where a board-work clip exists **it is the instance**, and the prose beneath it stops narrating
the steps and picks up at the Pattern.

Two corollaries, cutting in opposite directions:

- **Do not animate easy mechanics.** A transpose, or `P = G + R` element by element, is a
  sequence — but a two-second one that a labelled before-and-after conveys completely. Animating
  it spends budget and teaches the reader that clips are decoration, so they stop watching the
  ones that matter. Chapter 1 demotes four clips to static figures on exactly this ground.
- **Do not leave a hard sequence in prose because it is "just algebra."** The Cholesky recursion,
  Henderson's `A⁻¹` contributions accumulating over a pedigree, and a Gibbs sweep are all
  sequences the page genuinely cannot carry.

### The older test, still good

**A video earns its place if at least one is true:**

1. **Something assembles or moves.** Blocks dropping into the LHS, `A` filling cell by cell,
   `G₀ ⊗ A` expanding, a matrix flipping about its diagonal. A static figure can only show
   before and after; the transition *is* the lesson.
2. **Three or more objects must be held in mind at once** and then combined — the reason the MME
   is hard is not any one matrix, it is four of them at the same time.
3. **A geometric intuition exists that the algebra hides** — shrinkage as pulling toward the
   mean, the liability scale under a threshold, eigenvectors as the axes of a covariance ellipse.
4. **It converges.** An iterative process where the *path* matters (a Gibbs chain, PCG
   iterations). **But** these are data animations: build them in R with `gganimate` from the same
   chunk that produced the numbers, write the mp4/gif into `assets/video/`, and embed with the
   same shortcode. Manim for how the algebra moves; R for how the numbers converge.

**It does not earn its place if:**

- it is a static equation with a fade-in — that is a slide, not an animation;
- it re-narrates R output or walks a results table;
- the same insight fits in one well-labelled figure (then draw the figure).

**Three roles, decided per chapter:**

- **Opener** — motivates the chapter's *problem*. Only worth it where the problem is
  non-obvious ("why can't we just fit sire as a fixed effect?", "why isn't a phenotype an EBV?").
  A tool chapter does not need one.
- **Step-through** — the workhorse, and where most of the budget goes. Sits inline at the worked
  example, one clip per genuinely hard step.
- **Summary** — assembles the chapter's object once more, at speed, and places it in the book.
  Earns its keep in capstone chapters, becomes filler everywhere else.

**Budget:** roughly 40–55 clips total across the book. Cap inline clips at five per chapter; if
a chapter seems to want more, the chapter is doing too much.

**Re-read the per-chapter lists in §7 against the sequence-versus-shape criterion before building
anything past Chapter 1.** Chapter 1's list has been reworked already
(`chapter_01_linear_algebra.md` §7): same count of eight, but two clips promoted, four demoted to
static figures, and the board-work clips given priority because they are the ones carrying the
teaching rather than illustrating it.

---

## 7. Per-chapter plan

Priority: **P1** build first · **P2** build once P1 ships · **P3** only if the book is otherwise done.

| Ch | Opener | Step-through clips | Summary | Pri |
|---|---|---|---|---|
| 1 Matrix algebra | — | transpose (flip about diagonal); addition & why dimensions must match; **multiplication** (row–column sweep, inner dimension cancelling); 2×2 inverse via adjugate → `AA⁻¹ = I` collapsing; singularity (dependent rows, determinant → 0) | — | **P1** |
| 2 Linear models | — | building `X` row by row from the data frame; non-full-rank `X'X` — the column that is the sum of the others | — | P2 |
| 3 Mixed models (G = I) | why a mean isn't an effect | `Z` from animal IDs; shrinkage as α grows (the geometric intuition) | — | P2 |
| 4 Relationships | — | **tabular method filling `A` cell by cell** as the pedigree is walked; the three `A⁻¹` contribution rules applied to one trio | `A` and `A⁻¹` side by side, sparsity visible | **P1** |
| 5 Data preparation | why analyses fail before they start | contemporary groups forming; a disconnected data structure | — | P3 |
| 6 **Animal model** | ✔ *(existing `BLUPExplainer`, re-cut)* | swapping `I` for `A⁻¹`; **the four blocks dropping into the LHS**; the solve; EBV = PA + YD + PC decomposing | ✔ *(existing `BLUPConstruction`, re-cut)* | **P1** |
| 7 Reduced models | — | the same data collapsing from animal → sire → sire–MGS | — | P2 |
| 8 Random environmental | — | records nesting under a permanent-environment effect | — | P3 |
| 9 Genetic groups | where unknown parents send their genes | `Q` and the group rows joining the MME | — | P3 |
| 10 Maternal effects | one phenotype, two genetic effects | the doubled `Z`; the 2×2 `G₀` block entering | ✔ | P2 |
| 11 Multivariate | — | **`G₀ ⊗ A` expanding a 2×2 into a block matrix**; trait ordering vs animal ordering | ✔ | **P1** |
| 12 Random regression | a trajectory, not a point | Legendre polynomials summing into one animal's curve | — | P2 |
| 13 Social interaction | your neighbour's genes in your phenotype | direct + indirect `Z` for one pen | — | P3 |
| 14 Threshold models | **the liability scale under an observed 0/1** | thresholds cutting the underlying distribution | — | P2 |
| 15 Survival analysis | what censoring does to a mean | — | — | P3 |
| 16 Dominance | breeding value vs genotypic value | `D` alongside `A` for the same pedigree | — | P3 |
| 17 Epistasis | — | Hadamard products building `A#A`, `A#D` | ✔ why it's all additive in practice | P3 |
| 18 Multibreed | — | breed composition entering the covariance | — | P3 |
| 19 CCPS | — | purebred and crossbred as two correlated traits | — | P3 |
| 20 ANOVA / Henderson | — | sums of squares partitioning; a negative variance estimate appearing | — | P3 |
| 21 REML | — | the likelihood surface and one AI step climbing it | — | P2 |
| 22 Gibbs sampling | — | **the chain wandering, burn-in, the posterior filling in** — *R/gganimate, not manim* | ✔ three routes, same components | P2 |
| 23 Validation | — | forward prediction: cutting the data at a date | — | P3 |
| 24 Solving at scale | why direct inversion dies | **iterations converging on the solution** — *R/gganimate* | — | P2 |

P1 is 13 clips across four chapters and covers the book's two hardest ideas (`A⁻¹` and the MME
assembly). Within P1, ship Chapter 6's **opener** early even though Chapter 6 is written late:
`BLUPExplainer` already exists, and motivation-before-mechanism is worth more to a student in
week one than another mechanism clip. Everything else is judged after we see how P1 lands.

---

## 8. Production conventions

**The visual standard lives in [`manim_visual_standards.md`](manim_visual_standards.md)** —
the colour-role system extended to cover every object in the book, the tint / latent / state
axes, and the animation grammar for each kind of calculation. It becomes `manim/CLAUDE.md` when
`manim/` is created. Read it before writing a scene.

Design rules that shape the *plan* rather than the pixels:

- **Every clip states its learning objective in one sentence**, in the scene docstring, keyed to
  the numbered objective in `CHAPTERS.md` it serves (`# Ch 6, objective 3`). A clip that cannot
  name its objective is a clip we do not need. This is also what keeps clip count honest.
- **No reveal without a hold.** Every clip poses its next step and holds ~1.75 s before showing
  the answer. Animation watched passively teaches less than a figure the student had to read;
  the hold is what makes it active.
- **One idea, five new symbols, 75 seconds.** Past any of those it is two clips.
- **A clip is never load-bearing.** Everything in it is also in the prose — PDF readers and
  screen-reader users get the poster still and nothing else. The clip makes a hard thing fast;
  it is never the only place the thing is said.
- **The first frame shows the object in the chapter's own notation**, so a student scrubbing the
  timeline knows what they are looking at. No cold opens, no title cards on inline clips.
- **Spatial layout is fixed book-wide** — the MME on screen is arranged exactly as the MME on the
  page, so the video and the printed equation are the same picture.
- No audio, in either clip class. Captions carry the narration.

## 9. Order of work

1. **Vertical slice.** One scene (`Ch01MatMul`) → `build.py` → the Lua shortcode → `quarto render`
   to both HTML and PDF, confirming the poster fallback reads as a real book figure. ~1 hour,
   de-risks everything downstream.
2. Move `manim_test` in as `manim/ambook/` (D3); port its `CLAUDE.md` and merge
   `manim_visual_standards.md` into it. Build `StyleSwatches` and run its four checks — the
   palette is easiest to fix before 13 clips depend on it.
3. Finish Chapter 1's five clips — they are self-contained and need no book dataset.
4. Resolve the Ch 6 dataset conflict (D5), build the Ch 6 toy dataset in `data-raw/`, re-cut the
   two existing scenes onto it.
5. Chapters 4 and 11.
6. Review with students before starting P2.

## 10. Open questions

- **Ch 6 example: milk or backfat?** (D5) Blocks re-cutting the existing scenes.
- **Do the chapter features also go on YouTube?** If yes, they need a title card, an end card,
  and a resolution/aspect decision made before, not after, 8 videos are rendered.
- **Captions/subtitles for accessibility?** Manim can emit `.srt`; adding it later means
  revisiting every scene, so decide before P1 ships.
