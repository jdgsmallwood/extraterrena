from manim import ThreeDScene, Axes, GREY, GREEN,  FadeOut, Angle, ORIGIN, Arrow3D, YELLOW, Arc, ThreeDAxes, BLUE, Arrow, Vector, MathTex, UP, DOWN, GREEN, DashedLine, GRAY, DEGREES, Create, GrowArrow, Write


class VectorProjection3D(ThreeDScene):
    def construct(self):
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            z_range=[-1, 4, 1],
            x_length=6,
            y_length=6,
            z_length=4,
        )

        labels = axes.get_axis_labels(
            x_label=MathTex("z"),
            y_label=MathTex("y"),
            z_label=MathTex("x")
        )
        self.set_camera_orientation(phi=60 * DEGREES, theta=-50 * DEGREES)


        
        # Define the original 3D vector
        v = [2, 2, 3]
        vector = Arrow(start=axes.c2p(0,0,0), end=axes.c2p(*v), color=BLUE)
        label_v = MathTex(r"\vec{v}*").next_to(vector.get_end(), UP)
        # Define the projection onto the yz-plane (x=0)
        proj_v = [0, v[1], v[2]]
        vector_proj = Arrow(start=axes.c2p(0,0,0), end=axes.c2p(*proj_v), color=GREEN)
        label_proj = MathTex(r"\vec{v}_{yz}").next_to(vector_proj.get_end(), DOWN)
        # Dotted line from tip of original vector down to projection
        dashed_line = DashedLine(
            start=vector.get_end(),
            end=vector_proj.get_end(),
            color=GRAY
        )

        # Set the camera orientation
        self.add_fixed_orientation_mobjects(label_v, label_proj)
        # Add objects
        self.play(Create(axes), Write(labels))
        self.play(GrowArrow(vector))
        self.add_fixed_orientation_mobjects(label_v)
        self.play(GrowArrow(vector_proj), Write(label_proj))
        self.play(Create(dashed_line))
        self.wait()


        self.play(FadeOut(vector), FadeOut(label_v), FadeOut(dashed_line) )

        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, frame_center=ORIGIN, zoom=1.5)

        self.wait(10)