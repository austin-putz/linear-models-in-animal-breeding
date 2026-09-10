"""Palette, matrix mobjects, and the reusable animation grammars.

Single source of truth for how every clip in the book looks. Ported from
``~/Claude/manim_test/blup_common.py``; see ``manim/CLAUDE.md`` for the colour
rationale and ``plans/manim_visual_standards.md`` for the grammars.

Nothing in here knows about a particular chapter. Chapter modules import from
here and supply their own numbers.
"""

from manim import *  # noqa: F401,F403
import numpy as np

# ---------------------------------------------------------------- palette
# Colour encodes the role a quantity plays in the model, and nothing else.

# --- theme: carries no semantic meaning
BG = "#101826"        # background
TITLE = "#f5efe4"     # headings, title cards, punchlines
BODY = "#dfe5ee"      # prose, operators, role-less brackets and cells
SUBTEXT = "#7f8da4"   # captions, dimension tags, table heads

# --- roles: the moving parts of y = Xb + Zu + e
DATA = "#e8b64c"      # given data          y, phenotypes, X'y, Z'y, RHS
FIXED = "#5aa9e6"     # fixed structure     X, X', X'X
RANDOM = "#3fd0b0"    # random structure    Z, Z', Z'Z
LINK = "#a8c0d8"      # fixed x random      X'Z, Z'X
SOLVE = "#f0879f"     # the unknowns        b, u, b-hat, u-hat
RESID = "#9a9a94"     # residual            e
VAR = "#b98cf0"       # variance structure  lambda, A^-1, C, PEV, accuracy

# --- emphasis: sign / valence only, never a model role
POS = "#5fbf7f"
NEG = "#e2685f"

config.background_color = BG

# States (visual standards section 5). Attention is carried by a cream stroke
# and a scale pulse, never by hue, so it composes with every role colour.
PENDING_OPACITY = 0.35
ACTIVE_STROKE = 2.0
ACTIVE_SCALE = 1.06

HOLD = 1.75           # the standard beat before any reveal


# --------------------------------------------------------------- matrices
class GridMatrix(VGroup):
    """A matrix laid out on an explicit, fixed cell grid.

    Manim's built-in ``Matrix`` sizes itself around its content, so two
    matrices with different entries do not line up. Here every cell sits on a
    grid of known pitch, which is what lets separately-built blocks drop into
    a larger matrix with their rows and columns still registering.
    """

    def __init__(self, rows, cell_w=0.66, cell_h=0.58, font_size=32,
                 color=BODY, brackets=True, dim_zeros=False,
                 bracket_color=None, **kwargs):
        super().__init__(**kwargs)
        self.rows_src = [list(r) for r in rows]
        self.nr, self.nc = len(self.rows_src), len(self.rows_src[0])
        self.cell_w, self.cell_h = cell_w, cell_h

        self.cells, self.body = [], VGroup()
        for r, row in enumerate(self.rows_src):
            out = []
            for c, v in enumerate(row):
                col = color
                t = MathTex(str(v), font_size=font_size, color=col)
                if dim_zeros and str(v) == "0":
                    t.set_color(SUBTEXT).set_opacity(0.45)
                t.move_to([(c - (self.nc - 1) / 2) * cell_w,
                           -(r - (self.nr - 1) / 2) * cell_h, 0])
                out.append(t)
                self.body.add(t)
            self.cells.append(out)
        self.add(self.body)

        self.brk = VGroup()
        if brackets:
            self.brk = self.make_brackets(bracket_color or color)
            self.add(self.brk)

    def make_brackets(self, color=BODY, pad=0.10, arm=0.17, sw=2.6):
        w = self.nc * self.cell_w / 2 + pad
        h = self.nr * self.cell_h / 2
        out = VGroup()
        for sign, x in ((1, -w), (-1, w)):
            b = VMobject(stroke_color=color, stroke_width=sw)
            b.set_points_as_corners([
                [x + sign * arm, h, 0], [x, h, 0],
                [x, -h, 0], [x + sign * arm, -h, 0],
            ])
            out.add(b)
        return out

    def cell(self, r, c):
        return self.cells[r][c]

    def block(self, r0, r1, c0, c1):
        """The cells in rows r0..r1, cols c0..c1 inclusive."""
        return VGroup(*[self.cells[r][c]
                        for r in range(r0, r1 + 1)
                        for c in range(c0, c1 + 1)])

    def row(self, r):
        return self.block(r, r, 0, self.nc - 1)

    def col(self, c):
        return self.block(0, self.nr - 1, c, c)

    def block_rect(self, r0, r1, c0, c1, color, pad=0.06, opacity=0.14):
        return Rectangle(
            width=(c1 - c0 + 1) * self.cell_w + pad,
            height=(r1 - r0 + 1) * self.cell_h + pad,
            stroke_color=color, stroke_width=1.8,
            fill_color=color, fill_opacity=opacity,
        ).move_to(self.block(r0, r1, c0, c1))

    def row_rect(self, r, color, **kw):
        return self.block_rect(r, r, 0, self.nc - 1, color, **kw)

    def col_rect(self, c, color, **kw):
        return self.block_rect(0, self.nr - 1, c, c, color, **kw)


def block_offset(r0, c0, nr, nc, tot_r, tot_c, cell_w, cell_h):
    """Where a block's centre must sit inside a larger matrix."""
    cx = ((c0 + (nc - 1) / 2) - (tot_c - 1) / 2) * cell_w
    cy = -((r0 + (nr - 1) / 2) - (tot_r - 1) / 2) * cell_h
    return np.array([cx, cy, 0.0])


# ----------------------------------------------------------------- chrome
def heading(text, color=TITLE, font_size=34):
    """A clip heading, always in the same place (visual standards section 8)."""
    return Text(text, font_size=font_size, color=color).to_edge(UP, buff=0.45)


def caption(text, color=SUBTEXT, font_size=24):
    """A caption under the action. Keep it under ~80 characters."""
    return Text(text, font_size=font_size, color=color).to_edge(DOWN, buff=0.5)


def dim_tag(mob, nr, nc, color=SUBTEXT, font_size=22, buff=0.18):
    """The dimension tag every matrix carries on first appearance.

    CLAUDE.md's "state the dimensions of every matrix", enforced visually.
    """
    t = MathTex(rf"{nr} \times {nc}", font_size=font_size, color=color)
    t.next_to(mob, DOWN, buff=buff)
    return t


def labelled(mat, tex, buff=0.32, font_size=38, color=BODY):
    """Put ``tex =`` immediately left of a matrix, returning the group."""
    lab = MathTex(tex + " =", font_size=font_size, color=color)
    lab.next_to(mat, LEFT, buff=buff)
    g = VGroup(lab, mat)
    g.lab, g.mat = lab, mat
    return g


def set_pending(mob):
    """Mark a cell or block as not yet computed."""
    return mob.set_opacity(PENDING_OPACITY)


def activate(scene, *mobs, run_time=0.4):
    """Cream stroke plus a scale pulse — the active marker, no hue."""
    return scene.play(*[
        m.animate.scale(ACTIVE_SCALE).set_stroke(TITLE, ACTIVE_STROKE)
        for m in mobs
    ], run_time=run_time)


def settle(scene, *mobs, run_time=0.35):
    """Return an active cell or block to its settled state."""
    return scene.play(*[
        m.animate.scale(1 / ACTIVE_SCALE).set_stroke(width=0)
        for m in mobs
    ], run_time=run_time)


# -------------------------------------------------------------- grammars
def row_times_column(scene, left, right, target, i, j, stage_at,
                     hold=HOLD, product_font=30, link_color=SUBTEXT):
    """The row-by-column sequence — the most reused grammar in the book.

    Row *i* of ``left`` goes active, column *j* of ``right`` goes active, the
    pairs are written out as products at ``stage_at``, the products collapse to
    a sum, and the sum drops into cell (i, j) of ``target``.

    ``left``, ``right`` and ``target`` are ``GridMatrix`` instances; the frame
    holds for ``hold`` seconds before the sum is revealed, so the viewer has to
    predict it (visual standards section 9).

    Returns the mobjects it created so the caller can clean them up.
    """
    row_vals = left.rows_src[i]
    col_vals = [right.rows_src[k][j] for k in range(right.nr)]
    assert len(row_vals) == len(col_vals), "inner dimensions must match"

    rrect = left.row_rect(i, TITLE, opacity=0.10)
    crect = right.col_rect(j, TITLE, opacity=0.10)
    scene.play(Create(rrect), Create(crect), run_time=0.5)

    # Thin lines joining the sources to the cell being computed, per section 5.
    links = VGroup(
        Line(rrect.get_right(), target.cell(i, j).get_center(),
             stroke_width=1.2, color=link_color).set_opacity(0.5),
        Line(crect.get_bottom(), target.cell(i, j).get_center(),
             stroke_width=1.2, color=link_color).set_opacity(0.5),
    )
    scene.play(Create(links), run_time=0.4)

    terms = " + ".join(rf"{a}({b})" for a, b in zip(row_vals, col_vals))
    expr = MathTex(terms, font_size=product_font, color=BODY).move_to(stage_at)
    scene.play(Write(expr), run_time=1.1)

    # The hold: the question is on screen and the answer is not.
    scene.wait(hold)

    total = sum(int(a) * int(b) for a, b in zip(row_vals, col_vals))
    result = MathTex(str(total), font_size=product_font + 4, color=BODY)
    result.move_to(stage_at)
    scene.play(TransformMatchingShapes(expr, result), run_time=0.9)

    # Drop the sum into cell (i, j), replacing the placeholder that was
    # sitting there. The placeholder must actually go: leaving it in place is
    # how you end up with a "?" still on screen after the answer has landed.
    placeholder = target.cell(i, j)
    landed = result.copy().move_to(placeholder).scale(0.92)
    scene.play(
        ReplacementTransform(result, landed),
        FadeOut(placeholder),
        FadeOut(links), run_time=0.9,
    )

    # Re-register the cell so later highlights and blocks address the value,
    # not the discarded placeholder.
    target.body.remove(placeholder)
    target.cells[i][j] = landed
    target.body.add(landed)
    target.add(landed)

    scene.play(
        landed.animate.scale(ACTIVE_SCALE).set_stroke(TITLE, ACTIVE_STROKE),
        run_time=0.3,
    )
    scene.play(
        landed.animate.scale(1 / ACTIVE_SCALE).set_stroke(width=0),
        FadeOut(rrect), FadeOut(crect), run_time=0.4,
    )
    scene.wait(0.6)
    return landed
