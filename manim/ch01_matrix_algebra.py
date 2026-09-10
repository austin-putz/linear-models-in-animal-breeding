"""Chapter 1 — Matrix Algebra for Animal Breeders.

Eight clips are planned (see plans/chapter_01_linear_algebra.md section 7).
Ch01MatMul is built first: it carries the row-by-column grammar that the rest
of the book reuses.

Colour note: sections 1.1-1.4 are pre-semantic. A matrix has no model role yet,
so cells are BODY and the *grammar* carries the teaching. From Ch01XtXCounts
onward, X takes FIXED blue and y takes DATA amber, so a student arriving at
Chapter 6 already reads the palette.
"""

from manim import *
from ambook.style import (
    BODY, SUBTEXT, TITLE, HOLD,
    GridMatrix, caption, dim_tag, heading, row_times_column,
)

# Example A: four lambs, two flocks. Sheep yearling weight, kg.
WEIGHTS = [48, 52, 41, 45]
FLOCK_A = [1, 1, 0, 0]
FLOCK_B = [0, 0, 1, 1]


class Ch01MatMul(Scene):
    """Row times column, one lamb at a time; the inner dimensions cancel.

    # Ch 1, objective 1 — perform matrix multiplication by hand and verify it.
    """

    def construct(self):
        head = heading("Two flock totals")
        self.play(FadeIn(head, shift=DOWN * 0.2), run_time=0.6)

        # --- the bookkeeping table, in the notation the chapter uses ---------
        # Wide cells so the column headers fit without colliding.
        wt = GridMatrix([[a, b] for a, b in zip(FLOCK_A, FLOCK_B)],
                        color=BODY, font_size=30, cell_w=1.35)
        yv = GridMatrix([[w] for w in WEIGHTS], color=BODY, font_size=30)

        wt.move_to(LEFT * 1.6 + DOWN * 0.35)
        yv.next_to(wt, RIGHT, buff=2.0)

        col_hdr = VGroup(*[
            Text(name, font_size=19, color=SUBTEXT)
            for name in ("flock A", "flock B")
        ])
        for k, h in enumerate(col_hdr):
            h.move_to([wt.cell(0, k).get_center()[0], 0, 0])
            h.next_to(wt, UP, buff=0.24)
            h.set_x(wt.cell(0, k).get_center()[0])

        # The matrix labels sit clear above the headers, not on top of them.
        w_lab = MathTex(r"\mathbf{W}", font_size=36, color=BODY)
        w_lab.next_to(col_hdr, UP, buff=0.22).set_x(wt.get_center()[0])
        y_lab = MathTex(r"\mathbf{y}", font_size=36, color=BODY)
        y_lab.next_to(yv, UP, buff=0.24).set_y(w_lab.get_center()[1])

        # Anchored to the matrix's left edge, not to its first column, so the
        # bracket never runs through the labels.
        lamb_lbl = VGroup(*[
            Text(f"lamb {k + 1}", font_size=18, color=SUBTEXT)
            .next_to(wt, LEFT, buff=0.28)
            .set_y(wt.cell(k, 0).get_center()[1])
            for k in range(4)
        ])

        cap = caption("Each column marks which lambs belong to that flock.")
        self.play(FadeIn(wt), FadeIn(col_hdr), FadeIn(lamb_lbl), run_time=1.0)
        self.play(FadeIn(w_lab), run_time=0.4)
        self.play(FadeIn(yv), FadeIn(y_lab), FadeIn(cap), run_time=0.8)
        self.wait(2.2)

        # --- stand the table on its side ------------------------------------
        cap2 = caption("Stand it on its side so its columns become rows.")
        self.play(FadeOut(cap), FadeIn(cap2), run_time=0.5)

        wtt = GridMatrix([FLOCK_A, FLOCK_B], color=BODY, font_size=30)
        wtt.move_to(LEFT * 2.5 + UP * 0.9)
        wt_lab = MathTex(r"\mathbf{W}'", font_size=36, color=BODY)
        wt_lab.next_to(wtt, LEFT, buff=0.32)

        self.wait(0.8)
        self.play(FadeOut(col_hdr), FadeOut(lamb_lbl), run_time=0.5)
        self.play(
            ReplacementTransform(wt, wtt),
            ReplacementTransform(w_lab, wt_lab),
            run_time=1.1,
        )

        yv2 = GridMatrix([[w] for w in WEIGHTS], color=BODY, font_size=30)
        yv2.next_to(wtt, RIGHT, buff=0.55)
        y_lab2 = MathTex(r"\mathbf{y}", font_size=32, color=BODY)
        y_lab2.next_to(yv2, UP, buff=0.22)
        self.play(ReplacementTransform(yv, yv2),
                  ReplacementTransform(y_lab, y_lab2), run_time=0.8)

        # --- the result, still empty, and the dimension tags ----------------
        eq = MathTex("=", font_size=38, color=BODY).next_to(yv2, RIGHT, buff=0.45)
        res = GridMatrix([["?"], ["?"]], color=BODY, font_size=30)
        res.next_to(eq, RIGHT, buff=0.45)
        for r in range(2):
            res.cell(r, 0).set_opacity(0.35)

        d1 = dim_tag(wtt, 2, 4)
        d2 = dim_tag(yv2, 4, 1)
        d3 = dim_tag(res, 2, 1)
        self.play(FadeIn(eq), FadeIn(res), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.6)
        self.wait(1.2)

        # The inner dimensions meet in the middle and cancel.
        cap3 = caption("The inner dimensions must match. They cancel.")
        self.play(FadeOut(cap2), FadeIn(cap3), run_time=0.5)
        strike = VGroup(*[
            Line(m.get_corner(DL) + LEFT * 0.04, m.get_corner(UR) + RIGHT * 0.04,
                 stroke_width=2.4, color=TITLE)
            for m in (d1[0][2:], d2[0][:1])
        ])
        self.play(Create(strike), run_time=0.8)
        self.wait(1.6)
        self.play(FadeIn(d3), run_time=0.6)
        self.wait(1.6)
        self.play(FadeOut(strike), run_time=0.5)

        # --- row 1: flock A's total ----------------------------------------
        stage = DOWN * 1.9
        cap4 = caption("Pair the row with the weights, one lamb at a time.")
        self.play(FadeOut(cap3), FadeIn(cap4), run_time=0.5)
        row_times_column(self, wtt, yv2, res, 0, 0, stage_at=stage, hold=HOLD + 0.5)
        self.wait(1.4)

        # --- row 2: flock B's total, with a longer hold ---------------------
        cap5 = caption("Same walk, second row. What comes out?")
        self.play(FadeOut(cap4), FadeIn(cap5), run_time=0.5)
        self.wait(1.0)
        row_times_column(self, wtt, yv2, res, 1, 0, stage_at=stage, hold=HOLD + 1.2)

        # --- the final frame is the poster still for the PDF ----------------
        cap6 = caption("Two columns in, two totals out. That walk is matrix multiplication.")
        self.play(FadeOut(cap5), FadeIn(cap6), run_time=0.6)
        box = SurroundingRectangle(res, color=TITLE, buff=0.16,
                                   stroke_width=2.0)
        self.play(Create(box), run_time=0.7)
        self.wait(3.4)
