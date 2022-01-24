from manim import *
import math

class InitialConditions(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 6, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        labels = axes.get_axis_labels(y_label='t')
        region_top_boundary = lambda y : 6
        top = axes.plot(region_top_boundary)
        line1 = axes.get_vertical_line(axes.input_to_graph_point(2, top), color = BLUE)
        line2 = axes.get_vertical_line(axes.input_to_graph_point(3, top), color = RED)
        area = axes.get_area(top, [2, 3], color = BLUE_B, opacity=0.2)
        self.add(axes, line1, line2, area, labels)
        self.wait()


class Pipe(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        labels = axes.get_axis_labels()
        cylinder = Cylinder(radius=1, height=4, direction=[1, 0, 0])
        self.set_camera_orientation(phi=60 * DEGREES, theta=-75 * DEGREES)
        self.add(axes, cylinder, labels)
        self.wait()

class InitialCondition(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 3, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        labels = axes.get_axis_labels(y_label='u')
        e1 = lambda x : math.cos(x * 2.5) + 1.5
        l1 = axes.plot(e1, x_range=[0.25, 2.75])
        l2 = axes.get_vertical_line(axes.input_to_graph_point(2, l1), color = BLUE)
        l3 = axes.get_vertical_line(axes.input_to_graph_point(2.25, l1), color = RED)
        self.add(axes, labels, l1, l2, l3)
        t1 = Tex("$x$").scale(0.75).move_to(l2, DOWN).shift(DOWN * 0.4)
        t2 = Tex("$x + \Delta x$").scale(0.75).move_to(l3, DOWN).shift(DOWN * 0.4)
        self.add(t1, t2)
        self.wait()