from manim import *

class VectorAndMatrix(VectorScene):
    def construct(self):
        
        plane = self.add_plane(animate = True).add_coordinates()
        vector = self.add_vector([-3, -2], color=YELLOW, animate = True)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector)

        vector2 = self.add_vector([2,2])
        self.write_vector_coordinates(vector2)
        self.wait(2)
    
class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=True
        )

    def construct(self):
        matrix = [[1,2], [2,1]]
        matrix_tex = MathTex(
            r"A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}"
        ).to_edge(UL).add_background_rectangle()

        unit_square = self.get_unit_square()
        text = always_redraw(
            lambda: MathTex("Det(A)").set(width = 0.7).move_to(unit_square.get_center())
        )

        vect = self.get_vector([1,-2], color = PURPLE_B)

        rect1 = Rectangle(height=2, width=1, stroke_color=BLUE_A,
                          fill_color=BLUE_D, fill_opacity=0.6).shift(LEFT*2 + UP*2)
        
        circ1 = Circle(radius=1, stroke_color=BLUE_A,
                       fill_color=BLUE_D, fill_opacity=0.6).shift(RIGHT*1 + DOWN*2)
        
        self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        self.add_background_mobject(matrix_tex, text)
        self.apply_matrix(matrix)

        self.wait()

class Tute1(Scene):

    def construct(self):

        plane = NumberPlane(x_range=[-5,5], y_range=[-4,4],
                            x_length=10, y_length=7).add_coordinates().shift(RIGHT*2)
        
        vect1 = Line(start = plane.c2p(0,0), end = plane.c2p(3,2), stroke_color=YELLOW).add_tip()
        vect1_name = MathTex("\\vec{v}").next_to(vect1, RIGHT, buff=0.1).set_color(YELLOW)

        vect2 = Line(start = plane.c2p(0,0), end = plane.c2p(-2,1), stroke_color=RED).add_tip()
        vect2_name = MathTex("\\vec{w}").next_to(vect2, LEFT, buff=0.1).set_color(RED)

        vect3 = Line(start= plane.c2p(3,2), end= plane.c2p(1,3), stroke_color=RED).add_tip()

        vect4 = Line(start = plane.c2p(0,0), end = plane.c2p(1,3), stroke_color=GREEN).add_tip()
        vect4_name = MathTex("\\vec{v} + \\vec{w}").next_to(vect4, LEFT, buff=0.1).set_color(GREEN)

        stuff = VGroup(plane, vect1, vect1_name, vect2, vect2_name, vect3, vect4, vect4_name)

        box = RoundedRectangle(height=1.5, width = 1.5, corner_radius=0.1, stroke_color=PINK).to_edge(DL)

        self.play(DrawBorderThenFill(plane), run_time = 2)
        self.wait(1)
        self.play(GrowFromPoint(vect1, point = vect1.get_start()), Write(vect1_name), run_time=2)
        self.wait()
        self.play(GrowFromPoint(vect2, point = vect2.get_start()), Write(vect2_name), run_time=2)
        self.wait()
        self.play(Transform(vect2, vect3), vect2_name.animate.next_to(vect3, UP, buff=0.1), run_time=2)
        self.wait()
        self.play(
            LaggedStart
                (
                GrowFromPoint(vect4, point = vect4.get_start()),
                Write(vect4_name)
                ), run_time=3, lag_ratio=1
            )
        self.wait()
        self.add(box)
        self.wait()
        self.play(stuff.animate.move_to(box.get_center()).set(width=1.2), run_time=3)
        self.wait(2)
        

if __name__ == "__main__":
    from manim import config
    # This simulates the command line flags
    config.quality = "low_quality"
    config.preview = True
    
    scene = Tute1()
    scene.render()
