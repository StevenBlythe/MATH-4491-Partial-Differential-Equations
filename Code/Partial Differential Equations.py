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
            "Theme": WHITE,
            "Theme_A": RED,
            "Theme_B": BLUE,
            "Theme_C": PURPLE,
            "Theme_D": GREEN
        }
        self.camera.background_color = BLACK
        
        ### Begin ###
        axes = Axes(
            x_range=(-4, 4, 2),
            y_range=(-4, 4, 2),
            x_length=12,
            y_length=12,
            x_axis_config={
                "numbers_to_include": np.arange(-4, 4.01, 2)
            },
            y_axis_config={
                "numbers_to_include": np.arange(-4, 4.01, 2)
            },
            tips=False
        ).set_color(colors["Theme"])

        x_label = axes.get_x_axis_label("x").set_color(colors["Theme"])
        y_label = axes.get_y_axis_label("y").set_color(colors["Theme"]).shift(UP*2.8)
        self.add(axes, x_label, y_label)
        

        ### Circle around 
        rounded = RoundedRectangle(corner_radius=3, height=12, width=12.0).set_color(colors["Theme_A"])
        self.play(Create(rounded))


        ### Write Omega
        omega = Tex("$\Omega$").set_color(colors["Theme"]).move_to(axes.c2p(2, 2, 0)).scale(2)
        
        self.play(FadeIn(omega))

        self.wait(2)

        self.play(FadeOut(omega))

        ### Create a point x_0
        point = Dot(color=colors["Theme"])
        x0 = Tex("$x_0$").next_to(point, UP).set_color(colors["Theme"])

        ### Move point x_0
        location = VGroup(x0, point).move_to(axes.c2p(1, 1, 0))
        self.play(FadeIn(location))
        self.wait(1)
        self.play(location.animate.shift(RIGHT*1 + UP*2))
        self.wait(1)
        self.play(location.animate.shift(LEFT*5 + DOWN*8))
        self.wait(1)
        self.play(location.animate.shift(RIGHT*6 + UP*3))
        self.wait(1)
        self.play(location.animate.move_to(axes.c2p(1, 1, 0)))

        ### Create a neighborhood around x_0

        ### Circle Size ###
        ball = Circle(radius=0.75).move_to(point).set_color(colors["Theme_B"])
        radius = Line(ball.get_center(), ball.point_at_angle(0)).set_color(colors["Theme_D"])
        self.play(Create(ball), Create(radius))

        # Eps
        eps = Tex("$\epsilon$", color=colors["Theme_C"]).next_to(radius, UP)
        self.play(FadeIn(eps))
        eps.add_updater(lambda z: z.become(Tex("$\epsilon$", color=colors["Theme_C"]).next_to(radius, UP)))

        self.add(radius)
        self.wait(1)
        circa = Circle(radius = 3).move_to(point).set_color(colors["Theme_B"])
        radiusa = Line(circa.get_center(), circa.point_at_angle(0)).set_color(colors["Theme_D"])
        self.play(Transform(ball, circa), Transform(radius, radiusa))
        self.wait(1)
        circb = Circle(radius = 1.5).move_to(point).set_color(colors["Theme_B"])
        radiusb = Line(circb.get_center(), circb.point_at_angle(0)).set_color(colors["Theme_D"])
        self.play(Transform(ball, circb), Transform(radius, radiusb))
        self.wait(2)

        self.play(FadeOut(eps))
        self.wait(2)

        # Move to the center, ball, radius, and location
        circc = Circle(radius = 6).move_to((0, 0, 0)).set_color(colors["Theme_B"])
        radiusc = Line(circc.get_center(), circc.point_at_angle(0)).set_color(colors["Theme_D"])
        self.play(location.animate.move_to((0, 0.28, 0)), Transform(ball, circc), Transform(radius, radiusc))
        self.wait(2)

        # Here, let us consider the area of the other region

        # Now, let us shrink to find our value:
        circd = Circle(radius = 3.0).move_to((0, 0, 0)).set_color(colors["Theme_B"])
        radiusd = Line(circd.get_center(), circd.point_at_angle(0)).set_color(colors["Theme_D"])
        self.play(location.animate.move_to((0, 0.28, 0)), Transform(ball, circd), Transform(radius, radiusd))
        self.wait(2)

        # Now, let us consider another area
        whole = VGroup(point, x0, ball, radius)
        self.play(whole.animate.move_to(axes.c2p(2, 2, 0)))

        self.wait(2)

        # Change the shape

        self.wait(2)

        whole = VGroup(point, x0, ball, radius)
        self.play(whole.animate.move_to(axes.c2p(-2, -2, 0)))

        # Now, let us shrink to find our value:
        circe = Circle(radius = 1.5).move_to(point).set_color(colors["Theme_B"])
        radiuse = Line(circe.get_center(), circe.point_at_angle(0)).set_color(colors["Theme_D"])
        self.play(Transform(ball, circe), Transform(radius, radiuse))
        self.wait(2)


         




class HomeworkVPi(ThreeDScene):
    def construct(self):
        # General colors 
        colors = {
            "Theme": WHITE,
            "Theme_A": BLUE,
            "Theme_B": RED,
            "Theme_C": GREEN
        }
        self.camera.background_color = BLACK

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
            return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(42, 42),
            v_range=[-3.6, 3.6],
            u_range=[-3.6, 3.6],
            )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (PURPLE, 0), (BLUE, 0.5)], axis=2)
        #surface_plane.set_fill_by_value(axes=axes, colors=[(BLACK, -0.5), (GRAY_D, 0), (GRAY, 0.5)], axis=2)

        self.add(surface_plane)

        self.wait(2)

        # Set up Surface 
        surface_a = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(42, 42),
            v_range=[-2.0, 2.0],
            u_range=[-2.0, 2.0],
            ).set_style(fill_opacity=1).set_fill_by_value(axes=axes, colors=[(RED, -0.5), (PURPLE, 0), (BLUE, 0.5)], axis=2)
        
        self.play(Transform(surface_plane, surface_a))
        
        self.wait(2)

        # Set up Surface 
        surface_b = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(42, 42),
            v_range=[0, 3.5],
            u_range=[0, 3.5],
            ).set_style(fill_opacity=1).set_fill_by_value(axes=axes, colors=[(RED, -0.5), (PURPLE, 0), (BLUE, 0.5)], axis=2)
        
        self.play(Transform(surface_plane, surface_b))

        self.wait(4)

        # Define new Surface
        
        surface_c = Surface(
            lambda u, v: axes.c2p(u, v, 0.2),
            resolution=(42, 42),
            v_range=[0, 3.5],
            u_range=[0, 3.5],
            ).set_style(fill_opacity=1).set_fill_by_value(axes=axes, colors=[(RED, -0.5), (PURPLE, 0), (BLUE, 0.5)], axis=2)
        
        self.play(Transform(surface_plane, surface_c))
        self.wait(2)

        surface_d = Surface(
            lambda u, v: axes.c2p(u, v, 0.2),
            resolution=(42, 42),
            v_range=[-4, 0],
            u_range=[-4, 0],
            ).set_style(fill_opacity=1).set_fill_by_value(axes=axes, colors=[(RED, -0.5), (PURPLE, 0), (BLUE, 0.5)], axis=2)
        
        self.play(Transform(surface_plane, surface_d))
        self.wait(2)

        surface_e = Surface(
            lambda u, v: axes.c2p(u, v, 0.2),
            resolution=(42, 42),
            v_range=[-3, -1],
            u_range=[-3, -1],
            ).set_style(fill_opacity=1).set_fill_by_value(axes=axes, colors=[(RED, -0.5), (PURPLE, 0), (BLUE, 0.5)], axis=2)
        
        self.play(Transform(surface_plane, surface_e))
        self.wait(2)

class HomeworkVPiia(Scene):
    def construct(self):
        ### Set Theme Color ###

        self.camera.background_color = WHITE

        colors = {
            "Theme": GRAY,
            "Theme_A": BLACK,
            "Theme_B": BLACK,
            "Theme_C": BLACK,
            "Theme_D": BLACK
        }

        ### Setup axes and Labels
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 0.5],
            axis_config={"color": colors["Theme"]},
            tips=False
        )

        labels = axes.get_axis_labels().set_color(colors["Theme_A"])

        self.add(axes, labels)

        ### Setup both functions ###
        def func_a(x):
            if -1 < x and x < 0:
                return -1
            elif 0 < x and x < 1:
                return 1
            else:
                return 0
        
        def func_b(x):
            v = abs(x)
            if v <= 1:
                return 1 - v
            else:
                return 0
        
        ### Create lines a and b ###
        line_a = axes.plot(
            lambda x : func_a(x),
            x_range=[-2, 2],
            discontinuities=[-1, 0, 1],
            color=colors["Theme_B"]
        )

        line_b = axes.plot(
            lambda x : func_b(x),
            x_range=[-2, 2],
            discontinuities=[-1, 0, 1],
            color=colors["Theme_D"]
        )

        self.play(Create(line_a), run_time=2, rate_function=smooth)
        self.wait()
        self.play(FadeOut(line_a))
        self.wait()
        self.play(Create(line_b), run_time=2, rate_function=smooth)
        self.wait()
        self.play(FadeOut(line_b))

class ProjectGradient(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 2, 1],
            tips=False
        )
        l1 = lambda x : 1
        l2 = lambda x : 2
        axes.plot(l1)
        axes.plot(l2)