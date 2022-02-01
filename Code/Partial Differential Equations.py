from manim import *
import math

class InitialConditions(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        labels = axes.get_axis_labels(y_label='u')
        
        region_top_boundary = lambda y : 4
        top = axes.plot(region_top_boundary)
        line1 = axes.get_vertical_line(axes.input_to_graph_point(0, top), color = BLUE)
        line2 = axes.get_vertical_line(axes.input_to_graph_point(1, top), color = RED)
        area = axes.get_area(top, [0, 1], color = BLUE_B, opacity=0.2)
        
        axes.set_color(WHITE)
        labels.set_color(WHITE)
        self.camera_background_color = BLACK
        
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

class Fourier(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10, 2],
            y_range=[-0.5, 1.5, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        e0 = lambda x : 0
        e1 = lambda x : 1
        pt1 = Dot(point=axes.coords_to_point(-4, 0.5))
        pt2 = Dot(point=axes.coords_to_point(6, 0.5))
        
        l1 = axes.plot(e1, x_range = [-4, 6, 1] ,color = PURPLE)
        l2 = axes.plot(e0, x_range = [-10, -4, 1], color = BLUE_D)
        l3 = axes.plot(e0, x_range = [6, 10, 1], color = BLUE_D)
        self.add(axes, l1, l2, l3, pt1, pt2)
        self.wait()

class Fourier2(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        e1 = lambda x : 1
        e2 = lambda x : math.cos(1 * math.pi * x)
        e3 = lambda x : math.cos(2 * math.pi * x)
        l1 = axes.plot(e1, color = PURPLE)
        l2 = axes.plot(e2, color = BLUE_D)
        l3 = axes.plot(e3, color = BLUE)
        self.add(axes, l1, l2, l3)
        self.wait()