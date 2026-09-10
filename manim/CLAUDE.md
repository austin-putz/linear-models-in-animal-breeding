# Manim clips — project conventions

Animated explainers for the book, rendered with Manim Community and embedded in
the Quarto chapters. **Manim never runs inside `quarto render`.** This is a
build pass of its own, exactly parallel to `data-raw/` → `data/`: source of
truth here in `manim/`, generated artefact committed in `assets/video/`.

```bash
python manim/build.py            # re-render only what is out of date
python manim/build.py ch01       # one chapter
python manim/build.py --force    # ignore mtimes
```

The renderer is found automatically: `manim/venv/bin/manim` if it exists, else
`~/Claude/manim_test/venv/bin/manim`, else whatever `manim` is on PATH.

| File | What it is |
|---|---|
| `ambook/style.py` | Palette, `GridMatrix`, chrome helpers, and the animation grammars. The single source of truth for how every clip looks |
| `ch01_matrix_algebra.py` | Chapter 1 scenes |
| `build.py` | The manifest and the render/copy pass |

## Naming — the asset stem is the identifier

One stem threads through four places, and the `MANIFEST` in `build.py` is the
single registry of every clip in the book:

| Where | Form | Example |
|---|---|---|
| Scene class | `ChNNPascalCase` | `Ch01MatMul` |
| Module | `chNN_topic.py` | `ch01_matrix_algebra.py` |
| Assets | `assets/video/<stem>.{mp4,png}` | `ch01-matmul.mp4` + `.png` |
| Chapter call | `{{< animation <stem> caption="…" >}}` | `{{< animation ch01-matmul … >}}` |

A duplicate stem is a duplicate manifest key and `build.py` refuses to run. A
clip reused in a later chapter **keeps its original chapter's prefix** —
`ch01-kronecker` is embedded again in Chapter 11, not renamed.

## The colour system

**One rule: colour encodes the role a quantity plays in the model, and nothing
else.** A student who learns "blue is fixed structure" in Chapter 1 must still
be able to rely on it in Chapter 17. Never reuse a role colour for decoration,
emphasis, or a heading. The full rationale, the hue table, and the rules for
adding a colour live in `plans/manim_visual_standards.md`, which is
authoritative; `ambook/style.py` is its implementation.

### Theme — no semantic meaning

| Name | Hex | Used for |
|---|---|---|
| `BG` | `#101826` | Background, set globally on import |
| `TITLE` | `#f5efe4` | Headings, title cards, punchlines, the active-state stroke |
| `BODY` | `#dfe5ee` | Prose, operators, role-less brackets and cells |
| `SUBTEXT` | `#7f8da4` | Captions, dimension tags, table heads |

Headings and captions are **never** a role colour.

### Roles — the model's moving parts

| Name | Hex | Role |
|---|---|---|
| `DATA` | `#e8b64c` amber | Given data: `y`, phenotypes, `X'y`, `Z'y`, the whole RHS |
| `FIXED` | `#5aa9e6` blue | Fixed-effect structure: `X`, `X'`, `X'X` |
| `RANDOM` | `#3fd0b0` teal | Random-effect structure: `Z`, `Z'Z`, `Z'Z + A⁻¹α` |
| `LINK` | `#a8c0d8` steel | The fixed × random cross blocks: `X'Z`, `Z'X` |
| `SOLVE` | `#f0879f` rose | The unknowns: `b̂`, `û`, the solution vector |
| `RESID` | `#9a9a94` grey | Residual: `e` |
| `VAR` | `#b98cf0` violet | Variance / relationship structure: `α`, `A⁻¹`, `C`, PEV, accuracy |
| `POS` / `NEG` | `#5fbf7f` / `#e2685f` | Sign or valence only, never a model role |

**Chapter 1 is mostly pre-semantic.** A matrix there has no model role yet, so
cells are `BODY` and the *grammar* carries the teaching. From `ch01-xtx-counts`
onward `X` takes `FIXED` and `y` takes `DATA`, so a student arriving at
Chapter 6 already reads the palette. Say so in one caption the first time.

## Production conventions

- **Every clip states its learning objective in its docstring**, as a
  `# Ch N, objective N` line keyed to `CHAPTERS.md`. `build.py` warns when one
  is missing. A clip that cannot name its objective is a clip we do not need,
  and this is what keeps the clip count honest.
- **One idea, five new symbols, 75 seconds.** Past any of those it is two
  clips. Inline clips run 20–75 s; `build.py` warns above 90 s.
- **No reveal without a hold.** Before a result appears the question is on
  screen and the frame holds. `ambook.style.HOLD` (1.75 s) is the standard beat.
- **The final frame is the poster.** `build.py` renders it separately with
  `-s` and it is what every PDF reader sees, so a scene must end on exactly the
  static figure a print reader needs — not on a fade-out.
- **A clip is never load-bearing.** Everything in it is also in the text.
- **Spatial layout is fixed book-wide**: heading `to_edge(UP, buff=0.45)`,
  caption `to_edge(DOWN, buff=0.5)` and under ~80 characters. The MME on screen
  is arranged exactly as the MME on the page.
- **No audio, ever.** Captions carry the narration; the clip must work muted.
- Use `GridMatrix`, never manim's `Matrix`. Manim's sizes itself to its
  content, so two separately-built matrices do not line up. `GridMatrix` puts
  every cell on a fixed pitch, which is what lets blocks drop into a larger
  matrix with rows still registering.
- Verify layout by rendering `-ql --disable_caching` and extracting frames at
  `self.wait()` points with `ffmpeg -ss <t> -frames:v 1`. **Frames sampled
  mid-animation give false alarms.**

## Grammars

The same operation must look the same in Chapter 1 and Chapter 17.
`row_times_column()` in `ambook/style.py` is the row-by-column sequence — the
most reused choreography in the book — and it takes the hold as a parameter.
Add a new grammar to `plans/manim_visual_standards.md` first, then implement it
here; never the other way round.
