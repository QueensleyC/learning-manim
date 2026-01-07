from manim import *
import numpy as np

class ProbabilityIntegralTransform(Scene):
    def construct(self):
        
        # 1. Setup Axes (Fixed the height/width error here)
        ax_pdf = Axes(
            x_range=[0, 4, 1], 
            y_range=[0, 1.2, 0.5],
            x_length=6, 
            y_length=2.5,
            axis_config={"include_tip": False}
        ).to_edge(UP, buff=0.5)
        
        ax_uni = Axes(
            x_range=[0, 1, 0.5], 
            y_range=[0, 1.5, 0.5],
            x_length=6, 
            y_length=2.5,
            axis_config={"include_tip": False}
        ).to_edge(DOWN, buff=0.5)

        # 2. Define the Functions
        # Exponential PDF: f(x) = e^-x
        pdf_curve = ax_pdf.plot(lambda x: np.exp(-x), color=BLUE)
        pdf_label = MathTex("X \sim Exp(1)", color=BLUE).next_to(ax_pdf, RIGHT)

        # The transformation formula
        transform_text = MathTex("Y = F_X(X)", color=YELLOW).move_to(ORIGIN)

        # 3. Animations: The Transformation
        self.play(Create(ax_pdf), Create(ax_uni))
        self.play(Create(pdf_curve), Write(pdf_label))
        self.wait(1)

        # We will move "slices" of probability to show the flattening
        # Let's pick 5 points along the X axis
        x_values = [0.2, 0.5, 1.0, 1.8, 3.0]
        
        self.play(Write(transform_text))
        
        for x in x_values:
            # Create a dot on the PDF
            dot_pdf = Dot(ax_pdf.c2p(x, np.exp(-x)), color=BLUE)
            
            # Calculate the CDF value: F(x) = 1 - e^-x
            y_val = 1 - np.exp(-x)
            
            # Create the corresponding dot on the Uniform axis
            # The PIT says this y_val will be Uniformly distributed between 0 and 1
            dot_uni = Dot(ax_uni.c2p(y_val, 1), color=YELLOW)
            
            # Trace the path
            arrow = Arrow(dot_pdf.get_center(), dot_uni.get_center(), color=WHITE, stroke_width=2, tip_length=0.1)
            
            self.play(FadeIn(dot_pdf, scale=0.5))
            self.play(GrowArrow(arrow), run_time=0.5)
            self.play(FadeIn(dot_uni, scale=0.5))
            self.add(dot_uni) # Keep dots on bottom for visual "pile up"
            self.play(FadeOut(dot_pdf), FadeOut(arrow), run_time=0.3)

        # 4. Show the final Uniform "Box"
        uniform_box = ax_uni.plot(lambda x: 1, x_range=[0, 1], color=YELLOW)
        uniform_area = ax_uni.get_area(uniform_box, x_range=[0, 1], color=YELLOW, opacity=0.3)
        uni_label = MathTex("Y \sim U(0, 1)", color=YELLOW).next_to(ax_uni, RIGHT)

        self.play(Create(uniform_box), FadeIn(uniform_area))
        self.play(Write(uni_label))
        self.wait(3)

        
if __name__ == "__main__":
    from manim import config
    # This simulates the command line flags
    config.quality = "low_quality"
    config.preview = True
    
    scene = ProbabilityIntegralTransform()
    scene.render()