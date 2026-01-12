from manim import *
import numpy as np

class MoveCameraTutorial(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        )

        graph = axes.plot(lambda x: x**2, x_range = [-2,2,1], color=YELLOW)
        rects = axes.get_riemann_rectangles(graph, x_range=[-2,2], dx=0.1, stroke_color = WHITE)

        graph2 = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range = [-2*PI, 2*PI],
            color = RED
            )
        
        self.add(axes, graph)
        self.wait()
        ## THE CAMERA IS AUTO SET TO PHI = 0 AND THETA = -90

        self.move_camera(phi=60*DEGREES)
        self.wait()
        self.move_camera(theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate = PI/10, about = 'theta')
        self.wait()
        self.play(Create(rects), run_time=3)
        self.play(Create(graph2))
        self.wait()
        self.stop_ambient_camera_rotation()

        self.wait()
        self.begin_ambient_camera_rotation(rate = PI/10, about = 'phi')
        self.wait(2)
        self.stop_ambient_camera_rotation()

class PresetCamera(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()

        graph = axes.plot(lambda x: x**2, x_range = [-2,2,1], color=YELLOW)

        surface = Surface(
            lambda u, v: axes.c2p(v*np.cos(u), v*np.sin(u), 0.5*(v**2)),
            u_range=[0, 2*PI],
            v_range=[0, 3],
            
            checkerboard_colors = [GREEN, RED]
        )

        three_d_stuff = VGroup(axes, graph, surface)

        self.add(axes, graph)
        self.begin_ambient_camera_rotation(rate = PI/20)
        # self.wait(10)
        self.play(Create(surface))
        # self.wait(5)
        self.play(three_d_stuff.animate.shift(LEFT*2))
        self.wait(5)

 

if __name__ == "__main__":
    from manim import config
    # This simulates the command line flags
    config.quality = "low_quality"
    config.preview = True
    
    scene = PresetCamera()
    scene.render()