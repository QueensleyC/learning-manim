
"""
THINGS TO KNOW BEFORE RUNNING:
1. Ensure the 'seeingstats' conda environment is active.
2. This script requires Manim Community Edition.
"""

from manim import *
import numpy as np

class GraphingMovement(Scene):

    def construct(self):
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        ).add_coordinates()
        axes.to_edge(UL)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        formula = MathTex("y = 0.5^x")
        formula.to_edge(UP)

        graph = axes.plot(lambda x: 0.5 ** x, x_range= [0,4], color=GREEN)

        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Write(formula),Create(graph))
        self.play(graphing_stuff.animate.shift(DOWN * 3))
        self.play(axes.animate.center())
        self.wait(1)

class Graphing(Scene):

    def construct(self):

        my_plane = NumberPlane(x_range=[-6, 6], y_range=[-7, 7],
                               x_length=5, y_length=5)
        my_plane.add_coordinates()
        my_plane.shift(RIGHT*3)

        my_function = my_plane.plot(lambda x: 0.1*(x-5)*x*(x+5),
                                         x_range=[-6, 6],
                                         color=GREEN_B)
        
        area = my_plane.get_area(graph=my_function, x_range=[-5, 5], color=[BLUE_D, YELLOW_C], opacity=1)

        label = MathTex("f(x) = 0.1x(x-5)(x+5)").next_to(my_plane, UP, buff = 0.2)

        horiz_line = Line(start=my_plane.c2p(0, my_function.underlying_function(-2)),
                                end=my_plane.c2p(-2, my_function.underlying_function(-2)), 
                                stroke_color=YELLOW, stroke_width=3)


        self.play(DrawBorderThenFill(my_plane))
        self.play(Create(my_function), Write(label))
        self.play(FadeIn(area))
        self.play(Create(horiz_line))
        self.wait(2)


class CoordinateSystem(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-4,4], y_range=[-2,3],
                            x_length=4, y_length=4).add_coordinates()
        plane.shift(LEFT*3+DOWN*1.5)
        plane_graph = plane.plot(lambda x: -x**3, x_range=[-4,4], color=GREEN)
        area = plane.get_riemann_rectangles(graph=plane_graph, x_range=[-2,2], dx=0.05)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2,1],
            x_length=4,
            y_length=4,
        ).add_coordinates()
        axes.shift(RIGHT*3+DOWN*1.5)
        axes_graph = axes.plot(lambda x: 1/(1+np.exp(-x)), x_range=[-4,4], color=YELLOW)
        v_lines = axes.get_vertical_lines_to_graph(
            graph = axes_graph, x_range=[-3, 3], num_lines=12
        )

        formula_plane = MathTex("y = -x^3").next_to(plane, UP, buff=0.2)
        formula_axes = MathTex("y = 1/(1+e^{-x})").next_to(axes, UP, buff=0.2)

        self.play(LaggedStart(
            Write(formula_plane), Write(plane),
            Write(formula_axes), Create(axes),
            lag_ratio=0.75
        ))
        
        self.play(Create(plane_graph), Create(axes_graph), run_time = 2)
        self.add(area, v_lines)
        self.wait(1)


class PolarPlaneClass(Scene):
    def construct(self):
        
        e = ValueTracker(0.01)

        # ==============================================================
        # SECTION 1: POLAR COORDINATE SYSTEM (LEFT SIDE)
        # ==============================================================
        # 1. Create the plane
        plane = PolarPlane(
            radius_max=3,          # The outer boundary
            size=6,                # Total diameter on screen
            # azimuth_units="PI_RADIANS", # Label angles as 0, pi/2, pi, etc.
            # azimuth_step=8,        # Divide the circle into 8 slices
        ).add_coordinates()        
        
        plane.shift(LEFT*2)
        graph1 = always_redraw(lambda:
            ParametricFunction(lambda t: plane.polar_to_point( 2 * np.sin(3 * t),t),
                               t_range=[0,e.get_value()], color=GREEN)
        )
        dot1 = always_redraw(lambda:
            Dot(fill_color = GREEN, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end())
        ) 

        # ==============================================================
        # SECTION 2: CARTESIAN COORDINATE SYSTEM (RIGHT SIDE)
        # ==============================================================
        axes = Axes(
            x_range=[0, 4],
            y_range=[-3, 3, 1],
            x_length=3,
            y_length=3,
        ).add_coordinates()
        axes.shift(RIGHT*4)

        graph2 = always_redraw(lambda:
            axes.plot(lambda x: 2 * np.sin(3 * x), x_range=[0, e.get_value()], color=GREEN)
        )

        dot2 = always_redraw(lambda:
            Dot(fill_color = GREEN, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end())
        )

        axes_formula = MathTex(r"f(\theta) = 2 \sin(3\theta)", color= GREEN).next_to(axes, UP, buff=0.2)

        # ==============================================================
        # STEP 3: ANIMATION SEQUENCE
        # ==============================================================
        self.add(plane)
        self.play(LaggedStart(
            Write(axes), 
            Write(axes_formula),
            run_time = 3,
            lag_ratio=0.5
            )
        )
        self.add( graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(np.pi), run_time=10, rate_func=linear)
        self.wait(1)


if __name__ == "__main__":
    from manim import config
    # This simulates the command line flags
    config.quality = "low_quality"
    config.preview = True
    
    scene = PolarPlaneClass()
    scene.render()


        
