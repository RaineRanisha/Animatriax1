from manim import *
import numpy as np

class SquareWaveHarmonics(Scene):
    def construct(self):
        # Configuration for the plot
        x_range = [-2 * PI, 2 * PI]
        y_range = [-1.5, 1.5]
        x_length = config.frame_width - 2  # Adjust width to fit scene
        y_length = 6                     # Adjust height
        
        # Number of odd harmonics to sum (e.g., 5 means n=1, 3, 5, 7, 9)
        num_harmonics_to_show = 5 
        
        # Colors for individual harmonics, the sum, and the target square wave
        harmonic_colors = [BLUE, GREEN, YELLOW, ORANGE, PURPLE]
        sum_color = RED
        target_color = WHITE

        # 1. Create Coordinate System (Axes)
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={
                "include_numbers": False, 
                "include_ticks": False, 
                "stroke_width": 1
            },
        ).to_edge(DOWN, buff=0.7) # Position axes at the bottom part of the screen

        # Labels for the axes using Text()
        x_label = Text("Time (x)").scale(0.6).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("Amplitude").scale(0.6).next_to(axes.y_axis, LEFT, buff=0.2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # Main title for the scene
        title = Text("Building a Square Wave from Sine Harmonics").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2. Define Harmonic Functions
        # A square wave with amplitude A=1 and period 2*PI (omega=1) is given by:
        # f(x) = (4/PI) * sum_{n=1,3,5,...} (1/n) * sin(n*x)
        amplitude_scale_factor = 4 / PI

        def get_harmonic_func(n_val):
            """Returns the function for the n-th harmonic term."""
            return lambda x: amplitude_scale_factor * (1 / n_val) * np.sin(n_val * x)

        def get_sum_func(max_n_val):
            """Returns the function for the sum of harmonics up to max_n_val."""
            def func(x):
                s = 0
                # Sum only odd harmonics
                for n in range(1, max_n_val + 1, 2): 
                    s += (1 / n) * np.sin(n * x)
                return amplitude_scale_factor * s
            return func

        # 3. Define the ideal target square wave
        def get_square_wave_func(x):
            """Returns the ideal square wave function (amplitude -1 or 1)."""
            # Normalize x to [-PI, PI) for a single period
            x_mod = (x + PI) % (2 * PI) - PI 
            if x_mod >= 0:
                return 1
            else:
                return -1

        # Create the graph for the ideal square wave
        target_square_wave = axes.plot(
            get_square_wave_func, 
            color=target_color, 
            stroke_width=2
        ).set_stroke(dash_arg=[0.1, 0.1]) # Make it dashed for distinction

        # Introduce the target square wave briefly
        self.play(Create(target_square_wave))
        self.wait(1)
        self.play(FadeOut(target_square_wave)) # Hide it for now to focus on the build-up
        self.wait(0.5)

        # Initialize the graph for the accumulating sum (starts as a flat line at 0)
        current_sum_graph = axes.plot(lambda x: 0, color=sum_color, stroke_width=3)
        self.add(current_sum_graph) # Add it to the scene so it can be transformed

        # Text labels for the display area
        sum_label = Text("Current Sum: ").scale(0.6).to_corner(UL).shift(RIGHT*2).set_color(sum_color)
        self.play(Write(sum_label))
        self.wait(0.5)

        harmonic_texts_group = VGroup() # Group to hold individual harmonic labels

        # 4. Animate the sum, step-by-step
        n_values = [n for n in range(1, num_harmonics_to_show * 2, 2)] # Generates 1, 3, 5, 7, 9
        all_individual_harmonic_graphs = VGroup() # Group to hold all individual harmonic graphs

        for i, n_val in enumerate(n_values):
            color = harmonic_colors[i]

            # Create the graph for the current individual harmonic term
            new_harmonic_graph = axes.plot(get_harmonic_func(n_val), color=color, stroke_width=2)
            
            # Create the graph for the new accumulated sum
            new_sum_graph = axes.plot(get_sum_func(n_val), color=sum_color, stroke_width=3)

            # Create text for the current harmonic term
            harmonic_term_text = Text(
                f"Harmonic {n_val}: (1/{n_val})sin({n_val}x)"
            ).scale(0.5).set_color(color).next_to(sum_label, DOWN, buff=0.2).align_to(sum_label, LEFT)
            
            if i > 0:
                # If not the first harmonic, shift the new text below the previous ones
                harmonic_term_text.next_to(harmonic_texts_group[-1], DOWN, buff=0.1)
                
            harmonic_texts_group.add(harmonic_term_text)

            # Animation: Add the new harmonic and transform the sum graph
            self.play(
                Create(new_harmonic_graph),                  # Draw the new harmonic wave
                FadeIn(harmonic_term_text, shift=RIGHT),     # Show its label
                Transform(current_sum_graph, new_sum_graph), # Update the sum graph
                run_time=2
            )
            self.wait(1)
            
            # Add the individual harmonic graph to a group to manage later
            all_individual_harmonic_graphs.add(new_harmonic_graph)

        self.wait(2)

        # 5. Final comparison: The sum vs. the ideal square wave
        final_sum_label = Text(f"Sum of {num_harmonics_to_show} Harmonics").scale(0.7).to_corner(UL).shift(RIGHT*2).set_color(sum_color)
        
        self.play(
            FadeOut(title),
            FadeOut(sum_label),
            FadeOut(harmonic_texts_group), # Fade out all individual harmonic labels
            FadeIn(final_sum_label),
            FadeIn(target_square_wave)     # Bring back the ideal square wave for comparison
        )
        self.wait(2)
        
        # Optionally, fade out the individual harmonic graphs to highlight the sum and target
        self.play(FadeOut(all_individual_harmonic_graphs, shift=UP), run_time=1.5)
        self.wait(3)