from manim import *

class UpdaterAnimations(Scene):
    def construct(self):

        r = ValueTracker(0.5) # Tracks the value of the radius

        circle = always_redraw(lambda: 
                               Circle(radius=r.get_value(), stroke_color=BLUE, stroke_width = 5))
        
        line_radius = always_redraw(lambda:
                                    Line(start=circle.get_center(), end = circle.get_bottom(), stroke_color=YELLOW, stroke_width = 10))
        
        line_circumference = always_redraw(lambda:
                                           Line(stroke_color = YELLOW, stroke_width = 5)
                                           .set_length(2 * 3.14 * r.get_value())
                                           .next_to(circle, DOWN, buff=0.2))
        
        triangle = always_redraw(lambda:
                                 Polygon(circle.get_top(), circle.get_right(), circle.get_left(), stroke_color=GREEN, stroke_width=5))
        

        self.play(LaggedStart(
            Create(circle),
            DrawBorderThenFill(line_radius),
            DrawBorderThenFill(triangle),
            run_time = 4,
            lag_ratio= 0.75
        ))

        self.play(ReplacementTransform(circle.copy(), line_circumference), run_time=2)
        self.play(r.animate.set_value(2), run_time=5)

if __name__ == "__main__":
    from manim import config
    # This simulates the command line flags
    config.quality = "low_quality"
    config.preview = True
    
    scene = UpdaterAnimations()
    scene.render()