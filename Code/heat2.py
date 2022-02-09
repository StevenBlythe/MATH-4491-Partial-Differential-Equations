from manim import *
from manim.utils.rate_functions import ease_in_out_cubic

#config.background_color = WHITE
# config.VMobject.set_default(color=BLACK)
# config.MathTex.set_default(color=BLACK)

class heatSinWaves(ThreeDScene):
    def f1surf(self, u, v):
            return np.array([u, v, np.sin(u)*np.exp(-v)])
    def f2surf(self, u, v):
            return np.array([u, v, 0.5*np.cos(2*u)*np.exp(-4*v)])
    def f3surf(self, u, v):
            return np.array([u, v, 0.7*np.sin(2*u)*np.exp(-4*v)])
    def f4surf(self, u, v):
            return np.array([u, v, (np.sin(u)*np.exp(-v) + 0.5*np.cos(2*u)*np.exp(-4*v) + 0.7*np.sin(2*u)*np.exp(-4*v))])

    def construct(self):
        # VMobject.set_default(color=BLACK)
        # MathTex.set_default(color=BLACK)
        # self.camera.background_color=WHITE
        timeStartValue = 0
        timeEndValue = 2
        k1 = ValueTracker(timeStartValue)
        k2 = ValueTracker(timeStartValue)

        # COORDINATE SYSTEM ###
        axes1 = ThreeDAxes(
            axis_config={
                "tip_length": 0.2,
                "include_ticks": False
            },
            x_range=[-1, 2*PI+1,1],
            y_range=[-0.1, timeEndValue,0.1],
            z_range=[-1,1.5,1],
            x_length=7,
            y_length=5,
            z_length=4
        )
        y_axis = axes1.submobjects[1]\
            .set_opacity(0)

        # AXIS LABELS ###
        x_label = axes1.get_x_axis_label(Tex("$x$"))\
            .rotate(PI/2,axis=RIGHT)\
            .shift(0.25*RIGHT)
        y_label = axes1.get_y_axis_label(Tex("$t$"))\
            .rotate(PI/2,axis=RIGHT)\
            .set_opacity(0)
        z_label = axes1.get_z_axis_label(Tex("$u$"))\
            .shift(0.1*OUT,0.25*RIGHT)
        axes_labels1 = VGroup(x_label,y_label,z_label)
        system1 = VGroup(axes1, axes_labels1)

        # UPDATER FUNCTIONS ###
        def axisAndLabel_FadeIn_updater(mob,alpha): # 0 ≤ alpha ≤ 1
            mob.set_opacity(alpha)

        def surface_FadeIn_updater(mob,alpha):
            dx = interpolate(0,0.1,alpha)
            mob.set_stroke(opacity=dx)
            mob.set_fill(opacity=dx)
        
        def surface_FadeOut_updater(mob,alpha):
            dx = interpolate(0,0.1,alpha)
            mob.set_stroke(opacity=0.1-dx)
            mob.set_fill(opacity=0.1-dx)

        # COLOR GRADIENT FUNCTION ###
        def interpolate_color_range(color1, color2, color3, alpha):
            if alpha < 0.5:
                return interpolate_color(color1, color2, alpha/0.5)
            if alpha > 0.5:
                return interpolate_color(color2, color3, (alpha-0.5)/0.5)

        def colorGradient(graph, axes, color1, color2, color3):
            subPaths = CurvesAsSubmobjects(graph)
            y_Min = -1.78 # axes.y_range[0]
            y_Max = 1.42 # axes.y_range[1]

            y_Range = y_Max - y_Min
            for sP in subPaths:
                camera_coordinate = sP.get_center()
                axes_coordinate = axes.p2c(camera_coordinate)
                d_coordinate = abs(y_Min - axes_coordinate[2])
                dy = d_coordinate / y_Range

                color = interpolate_color_range(color1, color2, color3, dy) # 0 (color1) <= dy <= 1 (color3)
                sP.set_color(color)
            return subPaths

        #WAVE FUNCTION 1 ###
        def f1(x, y):
            return np.sin(x)*np.exp(-y)   
        f1graph = axes1.plot_parametric_curve(
            lambda t : np.array([
                t,
                0,
                f1(t, 0)
            ]),
            t_range = [0, 2*np.pi]
        )
        f1graph = colorGradient(f1graph,axes1,BLUE,GREEN,RED)

        #FADING CURVE 1 ###
        fadingCurve1 = always_redraw(
            lambda : colorGradient(
                axes1.plot_parametric_curve(
                    lambda t : np.array([
                        t,
                        k1.get_value(),
                        f1(t, k1.get_value())
                    ]),
                    t_range = [0, 2*np.pi],
                    stroke_opacity = (timeEndValue-k1.get_value())/(timeEndValue-timeStartValue)
                ), axes1, BLUE, GREEN, RED
            )
        )

        #SURFACE 1 ###
        surface1 = Surface(
            lambda u, v: axes1.c2p(*self.f1surf(u, v)),
            u_range = [0,2*PI],
            v_range = [0,timeEndValue],
            checkerboard_colors = [LIGHT_GRAY],
            fill_opacity = 0,
            stroke_opacity = 0,
            stroke_width = 0.5
        )

        all1 = VGroup(system1, f1graph, fadingCurve1, surface1)\
            .rotate(90*DEGREES,LEFT)
        #self.add_fixed_orientation_mobjects(all1)

        # START ###############################
        #STEP 1: AXES1
        self.add(system1)
        self.wait()
        self.play(
            Create(f1graph),
            Create(fadingCurve1),
            rate_func=smooth
        )
        self.add(surface1)
        self.play(all1.animate
            .rotate(10*DEGREES,RIGHT)
            .rotate(30*DEGREES,DOWN)
            .rotate(7*DEGREES,IN),
            run_time=2,
            rate_func = ease_in_out_cubic
        )
        self.play(
            UpdateFromAlphaFunc(y_axis, axisAndLabel_FadeIn_updater),
            UpdateFromAlphaFunc(y_label, axisAndLabel_FadeIn_updater),
            UpdateFromAlphaFunc(surface1, surface_FadeIn_updater),
            k1.animate.set_value(timeEndValue),
            run_time=5,
            rate_func = smooth
        )

        # #STEP 2: AXES2 AND AXES3 AND PLOTS
        self.play(all1.animate
            .rotate(0.9*DEGREES,IN)
            .scale(0.5)
            .to_edge(LEFT),
            buff=0.5,
            run_time=2,
            rate_func = smooth
        )
        plusSign1 = Tex("+")\
            .next_to(all1, buff=0.2)
        
        #AXES 2
        axes2 = axes1.copy()
        axes_labels2 = axes_labels1.copy()
        system2 = VGroup(axes2, axes_labels2)

        #WAVE FUNCTION 2 ###
        def f2(x, y):
            return 0.5*np.cos(2*x)*np.exp(-4*y)
        f2graph = axes2.plot_parametric_curve(
                lambda t : np.array([
                    t,
                    0,
                    f2(t, 0)
                ]),
                t_range = [0, 2*np.pi]
        )
        f2graph = colorGradient(f2graph,axes2,BLUE,GREEN,RED)

        #FADING CURVE 2 ###
        fadingCurve2 = always_redraw(
            lambda : colorGradient(
                axes2.plot_parametric_curve(
                    lambda t : np.array([
                        t,
                        k2.get_value(),
                        f2(t, k2.get_value())
                    ]),
                    t_range = [0, 2*np.pi],
                    stroke_opacity = (timeEndValue-k2.get_value())/(timeEndValue-timeStartValue)
                ),axes1,BLUE,GREEN,RED
            )
        )
        #SURFACE 2 ###
        surface2 = Surface(
            lambda u, v: axes2.c2p(*self.f2surf(u, v)),
            u_range = [0,2*PI],
            v_range = [0,timeEndValue],
            checkerboard_colors = [LIGHT_GRAY],
            fill_opacity = 0,
            stroke_opacity = 0,
            stroke_width = 0.5
        )
        all2 = VGroup(axes2, axes_labels2, f2graph, fadingCurve2, surface2)\
            .next_to(plusSign1, buff=0.3)\
            .rotate(0*DEGREES,LEFT)\
            .rotate(7*DEGREES,DOWN)\
            .rotate(1*DEGREES,OUT)

        plusSign2 = Tex("+").next_to(all2,buff=0.2)

        #AXES 3
        axes3 = axes2.copy()
        axes_labels3 = axes_labels2.copy()
        system3 = VGroup(axes3, axes_labels3)\
            .next_to(plusSign2, buff=0.3)\
            .rotate(15*DEGREES,DOWN)\
            .rotate(0.5*DEGREES,IN)

        #WAVE FUNCTION 3 ###
        def f3(x, y):
            return 0.7*np.sin(2*x)*np.exp(-4*y)   
        f3graph = axes3.plot_parametric_curve(
            lambda t : np.array([
                t,
                0,
                f3(t, 0)
            ]),
            t_range = [0, 2*np.pi]
        )
        f3graph = colorGradient(f3graph,axes3,BLUE,GREEN,RED)

        #FADING CURVE 3 ###
        fadingCurve3 = always_redraw(
            lambda : colorGradient(
                axes3.plot_parametric_curve(
                    lambda t : np.array([
                        t,
                        k2.get_value(),
                        f3(t, k2.get_value())
                    ]),
                    t_range = [0, 2*np.pi],
                    stroke_opacity = (timeEndValue-k2.get_value())/(timeEndValue-timeStartValue)
                ), axes1, BLUE, GREEN, RED
            )
        )
        #SURFACE 3 ###
        surface3 = Surface(
            lambda u, v: axes3.c2p(*self.f3surf(u, v)),
            u_range = [0,2*PI],
            v_range = [0,timeEndValue],
            checkerboard_colors = [LIGHT_GRAY],
            fill_opacity = 0,
            stroke_opacity = 0,
            stroke_width = 0.5
        )
        ####################
        self.play(
            FadeIn(system2),
            FadeIn(system3),
            FadeIn(plusSign1),
            FadeIn(plusSign2),
            run_time = 2
        )
        self.play(
            Create(f2graph),
            Create(fadingCurve2),
            Create(f3graph),
            Create(fadingCurve3),
            rate_func = smooth
        )
        self.add(
            surface2,
            surface3
        )
        self.wait()
        self.play(
            UpdateFromAlphaFunc(surface2, surface_FadeIn_updater),
            UpdateFromAlphaFunc(surface3, surface_FadeIn_updater),
            k2.animate.set_value(timeEndValue),
            run_time=3,
            rate_func = smooth
        )
        #self.wait()

        # STEP 3: TRANSFORM TO NEW WAVE FUNCTION
        #WAVE FUNCTION 4 ###
        def f4(x, y):
            return (np.sin(x)*np.exp(-y) + 0.5*np.cos(2*x)*np.exp(-4*y) + 0.7*np.sin(2*x)*np.exp(-4*y))
        f4graph = axes2.plot_parametric_curve(
                lambda t : np.array([
                    t,
                    0,
                    f4(t, 0)
                ]),
                t_range = [0, 2*np.pi]
            )
        f4graph = colorGradient(f4graph,axes2,BLUE,GREEN,RED)

        #SURFACE 4 ###
        surface4 = Surface(
            lambda u, v: axes2.c2p(*self.f4surf(u, v)),
            u_range = [0,2*PI],
            v_range = [0,timeEndValue],
            checkerboard_colors = [LIGHT_GRAY],
            fill_opacity = 0.1,
            stroke_opacity = 0.1,
            stroke_width = 0.5
            )
        all4 = VGroup(system2, f4graph, surface4)

        self.play(
            f1graph.animate
                .move_to(f2graph)
                .set_opacity(0),
            surface1.animate
                .move_to(surface2)
                .set_opacity(0),
            f3graph.animate
                .move_to(f2graph)
                .set_opacity(0),
            surface3.animate
                .move_to(surface2)
                .set_opacity(0),
            FadeOut(plusSign1),
            FadeOut(plusSign2),
            FadeOut(system1),
            FadeOut(system3),
            ReplacementTransform(f2graph,f4graph),
            ReplacementTransform(surface2,surface4),
            UpdateFromAlphaFunc(surface1, surface_FadeOut_updater),
            UpdateFromAlphaFunc(surface3, surface_FadeOut_updater),
            rate_func = smooth
        )

        self.wait()
        self.play(all4.animate
            .scale(1.7)
        )
        self.wait()