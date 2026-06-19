from manim import *
import numpy as np

class PythagoreanTheoremProof(Scene):
    def construct(self):
        title = Text("Pythagorean Theorem: Geometric Proof").scale(0.6).to_edge(UP)
        self.play(FadeIn(title))
        self.wait(0.5)
        
        # 3-4-5 Triangle vertices positioned to avoid edge clipping
        A = np.array([-1.5, -1.0, 0])  
        B = np.array([1.5, -1.0, 0])   
        C = np.array([1.5, 1.0, 0])    
        
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=4)
        self.play(Create(triangle))
        
        # Dynamic midpoint anchoring for labels
        label_a = Text("a").scale(0.5).next_to(Line(B, C).get_center(), RIGHT, buff=0.2)
        label_b = Text("b").scale(0.5).next_to(Line(A, B).get_center(), DOWN, buff=0.2)
        label_c = Text("c").scale(0.5).next_to(Line(A, C).get_center(), UL, buff=0.15)
        
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1.0) 
        
        # Outward projecting squares with exact mathematical vectors
        sq_b = Polygon(B, A, A + DOWN * 3.0, B + DOWN * 3.0, color=RED, fill_opacity=0.4)
        sq_a = Polygon(C, B, B + RIGHT * 2.0, C + RIGHT * 2.0, color=YELLOW, fill_opacity=0.4)
        
        v_AC = C - A
        perp_v = np.array([-v_AC[1], v_AC[0], 0])  
        sq_c = Polygon(A, C, C + perp_v, A + perp_v, color=ORANGE, fill_opacity=0.5)
        
        self.play(FadeIn(sq_b, run_time=1.2))
        self.wait(0.5)
        self.play(FadeIn(sq_a, run_time=1.2))
        self.wait(0.5)
        self.play(FadeIn(sq_c, run_time=1.5))
        self.wait(1.0)
        
        # Color-coded identity tracking to the bottom layout boundary
        eq_colored = VGroup(
            Text("a²", color=YELLOW), Text(" + "), 
            Text("b²", color=RED), Text(" = "), 
            Text("c²", color=ORANGE)
        ).arrange(RIGHT, buff=0.1).scale(0.7).to_edge(DOWN).shift(UP * 0.3)
        
        self.play(Write(eq_colored))
        self.wait(2.5)
