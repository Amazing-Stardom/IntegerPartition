from manim import *
import math

class PartitionGraph(Scene):
    def construct(self):
        # 1. Setup the Graph Axes
        # We will plot N from 0 to 12 (since p(12) = 77, which fits on screen)
        axes = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 90, 10],
            axis_config={"color": WHITE},
            x_length=10,
            y_length=6,
            tips=False,
        ).add_coordinates()

        # Labels
        x_label = axes.get_x_axis_label("n (Target)")
        y_label = axes.get_y_axis_label("p(n)")

        # 2. Define the math functions
        def get_exact_p(n):
            # Standard DP solution
            n = int(n)
            if n < 0: return 0
            if n == 0: return 1
            partitions = [0] * (n + 1)
            partitions[0] = 1
            for i in range(1, n + 1):
                for j in range(i, n + 1):
                    partitions[j] += partitions[j - i]
            return partitions[n]

        def get_approx_p(x):
            # Hardy-Ramanujan Formula
            if x < 1: return 1 # Avoid division by zero near 0
            constant = 1 / (4 * x * math.sqrt(3))
            exponent = math.pi * math.sqrt((2 * x) / 3)
            return constant * math.exp(exponent)

        # 3. Create the Visuals
        
        # The Smooth Approximation Curve (Yellow)
        approx_graph = axes.plot(
            lambda x: get_approx_p(x), 
            x_range=[0.5, 12.5], 
            color=YELLOW
        )
        approx_label = MathTex(r"p(n) \approx \frac{1}{4n\sqrt{3}}e^{\pi\sqrt{2n/3}}")
        approx_label.set_color(YELLOW).scale(0.7).to_corner(UR)

        # The Exact Integer Points (Green Dots)
        dots = VGroup()
        for n in range(1, 13):
            value = get_exact_p(n)
            dot = Dot(axes.c2p(n, value), color=GREEN)
            dots.add(dot)

        exact_label = Text("Exact Integer Count", color=GREEN, font_size=24)
        exact_label.next_to(approx_label, DOWN)

        # 4. The Animation Script
        
        # Draw Axes
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Draw the Approximation Curve
        self.play(Create(approx_graph), run_time=2)
        self.play(Write(approx_label))
        
        # Pop the Exact Dots onto the line
        self.play(LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots], lag_ratio=0.1))
        self.play(Write(exact_label))
        
        self.wait(2)