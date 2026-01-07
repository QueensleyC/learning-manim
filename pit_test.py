from manim import *
import numpy as np

class PIT_Workflow(Scene):
    def construct(self):
        # 1. Setup Three Axes (Stacked)
        axes_config = {"x_range": [0, 4], "y_range": [0, 1.1], "x_length": 5, "y_length": 2, "axis_config": {"include_tip": False}}
        
        ax_pdf = Axes(**axes_config).to_edge(UP, buff=0.2)
        ax_cdf = Axes(**axes_config).move_to(ORIGIN)
        ax_uni = Axes(x_range=[0, 1], y_range=[0, 1.1], x_length=5, y_length=2, axis_config={"include_tip": False}).to_edge(DOWN, buff=0.2)

        # 2. Labels
        pdf_lab = Text("1. PDF (Input)", font_size=24).next_to(ax_pdf, LEFT)
        cdf_lab = Text("2. CDF (Function)", font_size=24).next_to(ax_cdf, LEFT)
        uni_lab = Text("3. Uniform (Output)", font_size=24).next_to(ax_uni, LEFT)

        # 3. Curves
        pdf_curve = ax_pdf.plot(lambda x: np.exp(-x), color=BLUE)
        cdf_curve = ax_cdf.plot(lambda x: 1 - np.exp(-x), color=GREEN)
        uni_line = ax_uni.plot(lambda x: 1, x_range=[0, 1], color=YELLOW)

        self.add(ax_pdf, ax_cdf, ax_uni, pdf_lab, cdf_lab, uni_lab)
        self.play(Create(pdf_curve), Create(cdf_curve))

        # 4. The Plugging-In Animation
        # We'll pick a sample value x = 1.2
        sample_x = 1.2
        cdf_val = 1 - np.exp(-sample_x) # This is the output y

        # Vertical line on PDF
        v_line_pdf = ax_pdf.get_vertical_line(ax_pdf.c2p(sample_x, np.exp(-sample_x)), color=WHITE)
        dot_pdf = Dot(ax_pdf.c2p(sample_x, np.exp(-sample_x)), color=BLUE)

        # Path through CDF
        dot_cdf = Dot(ax_cdf.c2p(sample_x, cdf_val), color=GREEN)
        h_line_cdf = Line(ax_cdf.c2p(0, cdf_val), ax_cdf.c2p(sample_x, cdf_val), color=YELLOW)
        
        # Final dot on Uniform
        dot_uni = Dot(ax_uni.c2p(cdf_val, 1), color=YELLOW)
        v_line_uni = Line(ax_cdf.c2p(0, cdf_val), ax_uni.c2p(cdf_val, 1), color=WHITE, stroke_opacity=0.5)

        # 5. EXECUTE STEPS
        # Step A: Pick from PDF
        self.play(Create(v_line_pdf), FadeIn(dot_pdf))
        self.wait(0.5)

        # Step B: Plug into CDF (Vertical move from PDF to CDF)
        connector_1 = Line(dot_pdf.get_center(), dot_cdf.get_center(), color=WHITE, stroke_width=2)
        self.play(Create(connector_1))
        self.play(FadeIn(dot_cdf))
        
        # Step C: Show the Y-value on CDF axis
        self.play(Create(h_line_cdf))
        self.wait(0.5)

        # Step D: Place on Uniform graph (Mapping the Y-value to the X-axis of the result)
        self.play(
            ReplacementTransform(h_line_cdf.copy(), dot_uni),
            Create(v_line_uni),
            run_time=1.5
        )
        self.play(Create(uni_line), FadeIn(ax_uni.get_area(uni_line, x_range=[0, 1], opacity=0.2)))
        
        self.wait(2)

if __name__ == "__main__":
    scene = PIT_Workflow()
    scene.render()