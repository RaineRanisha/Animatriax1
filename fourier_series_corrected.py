from manim import *
import numpy as np

class FourierSquareWaveCorrected(Scene):
    def construct(self):
        title = Text("Fourier Series: Square Wave Decomposition").scale(0.6).to_edge(UP)
        self.play(FadeIn(title))
        
        # Setup Axes for the wave plotting
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE}
        ).shift(DOWN * 0.5)
        
        self.play(Create(axes))
        
        # Define clean mathematical harmonic components using fundamental math blocks
        # No system-dependent MathTex or external compilation strings are called
        colors = [RED, ORANGE, YELLOW, GREEN, PURPLE]
        
        def harmonic_wave(x, n):
            # Fourier component formula: (4/pi) * (sin(n * x) / n)
            return (4.0 / np.pi) * (np.sin(n * np.pi * x) / n)
            
        # Cumulative harmonic wave plotter
        def structural_fourier_sum(x, terms_count):
            total = 0.0
            for i in range(terms_count):
                n = 2 * i + 1  # Odd harmonics only
                total += harmonic_wave(x, n)
            return total

        previous_plot = None
        
        # Iteratively add 5 harmonic levels step-by-step with proper label matching
        for i in range(5):
            terms_count = i + 1
            current_harmonic_order = 2 * i + 1
            
            # Label track tracking structural addition
            label = Text(f"Harmonics up to n = {current_harmonic_order}").scale(0.5).to_corner(UL).shift(DOWN * 0.5)
            
            # Safe text drawing replacing crashing LaTeX components
            current_plot = axes.plot(
                lambda x: structural_fourier_sum(x, terms_count),
                color=colors[i],
                x_range=[-3, 3]
            )
            
            if i == 0:
                self.play(Create(current_plot), Write(label), run_time=1.5)
            else:
                self.play(
                    Transform(previous_plot, current_plot),
                    FadeOut(previous_label),
                    Write(label),
                    run_time=1.5
                )
                
            previous_label = label
            if i > 0:
                # Retain the accurate updated pointer frame reference
                pass
            else:
                previous_plot = current_plot
                
            self.wait(0.5)
            
        self.wait(2)
