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
        self.add(axes, labels)
        self.play(Create(line1), Create(line2), Create(area))
        self.wait(10)


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

class Fourier2(Scene):
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

class Fourier(Scene):
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
        self.add(Dot())

class LaplacesEquation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        labels = axes.get_axis_labels()
        
        region_top_boundary = lambda y : 3
        top = axes.plot(region_top_boundary)
        line1 = axes.get_vertical_line(axes.input_to_graph_point(0, top), color = BLUE)
        line2 = axes.get_vertical_line(axes.input_to_graph_point(1, top), color = RED)
        area = axes.get_area(top, [0, 1], color = BLUE_B, opacity=0.2)
        
        axes.set_color(WHITE)
        labels.set_color(WHITE)
        self.camera_background_color = BLACK
        
        self.add(axes, line1, line2, area, labels)
        self.wait()

class HeatEquation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        arrowx1 = Arrow3D(start=np.array([-2, 1, 1]), end=np.array([0, 1, 1]), color=RED)
        arrowx2 = Arrow3D(start=np.array([2, 1, 1]), end=np.array([4, 1, 1]), color=RED)
        arrowy1 = Arrow3D(start=np.array([1, -2, 1]), end=np.array([1, 0, 1]), color=PURPLE_E)
        arrowy2 = Arrow3D(start=np.array([1, 2, 1]), end=np.array([1, 4, 1]), color=PURPLE_E)
        heat = Cube(
            side_length = 2,
            fill_opacity = 0.75
        ).shift([1, 1, 1])
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.add(axes, heat)
        self.add(arrowx1, arrowx2, arrowy1, arrowy2)
        self.wait()

class HomeworkiiProblemia(Scene):
    def construct(self):
        # Camera background
        self.camera.background_color = WHITE
        # Create the base graph
        axes = Axes(
            x_range=[-3 * PI - 0.0001, 3 * PI + 0.0001, PI],
            y_range=[-4, 4, 1],
            tips=False
        ).set_color(BLACK)
        labels = axes.get_axis_labels().set_color(BLACK)
        self.add(axes, labels)

        # Create the x-labels
        x_labels = [
            MathTex("-3 \pi"), MathTex("-2 \pi"), MathTex("-\pi"), MathTex(""), MathTex("\pi"), MathTex("2 \pi"), MathTex("3 \pi")
        ]
        for i in range(len(x_labels)):
            x_labels[i].move_to(axes.c2p(-3 * PI + i * PI)).shift(DOWN*0.4).set_color(BLACK)
            self.add(x_labels[i])
        
        discont = [0]

        #for i in range(1, math.floor(len(x_labels)/2) + 1):
            #discont.append(i * PI)
            #discont.append(i * -PI)
        l1 = axes.plot(self.fourier, color=BLACK, discontinuities=[0])
        self.add(l1)
        # Dots at Discontinuities
        dots = [
            Dot(axes.c2p(0, 2, 0), color=BLACK)
        ]
        for dot in dots:
            self.add(dot)
        
        self.wait()


    def fourier(self, x):
        if x == 0:
            return 2
        else: return 1

class HomeworkVPib(Scene):
    def construct(self):
        colors = {
            "Theme": BLACK
        }
        self.camera.background_color = WHITE

        ### Begin ###
        axes = Axes(
            x_range=(-4, 4, 2),
            y_range=(-4, 4, 2),
            x_length=12,
            y_length=12
        ).set_color(colors["Theme"])

        self.add(axes)

        ### Circle around 
        graphp = ImplicitFunction(
            lambda x, y: x**2/9 + y**2/9 * y - 1,
            color=BLACK,
            x_range=[-3.01, 3.01],
            y_range=[-3.01, 3.01]
        )
        graphn = ImplicitFunction(
            lambda x, y: -(x**2/9 + y**2/9 * y - 1),
            color=BLACK,
            x_range=[-3.01, 3.01],
            y_range=[-3.01, 3.01]
        )
        self.add(graphn)

class HomeworkVPi(ThreeDScene):
    def construct(self):
        # General colors 
        colors = {
            "Theme": BLACK
        }
        self.camera.background_color = WHITE

        ### Begin ###
        # Rotate Camera
        self.set_camera_orientation(phi = 75 * DEGREES, theta = -30 * DEGREES)

        # Setup Axes
        axes = ThreeDAxes(
            x_range=(-4, 4, 2), 
            y_range=(-4, 4, 2), 
            z_range=(-1, 1, 0.5)
        ).set_color(colors["Theme"])

        self.add(axes)

        # Set up Surface
        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.cos(y)
            if z < 1:
                return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(42, 42),
            v_range=[-3.5, 3.5],
            u_range=[-3.5, 3.5],
            )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (PURPLE, 0), (BLUE, 0.5)], axis=2)

        self.add(surface_plane)

        # Set up 2-D Surface


        self.wait()


class HomeworkVPia(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        axes = ThreeDAxes(
            x_range=(-4, 4, 2), 
            y_range=(-4, 4, 2), 
            z_range=(-1, 1, 0.5))


