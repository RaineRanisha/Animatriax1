from manim import *

class PythagoreanTheoremProof(Scene):
    def construct(self):
        # Using MathTex will intentionally trigger a missing LaTeX system exception
        title = MathTex(r"a^2 + b^2 = c^2")
        self.play(Write(title))
