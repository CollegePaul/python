from manim import *

class One(Scene):
    def construct(self):
        title = Tex(r"Lets have a go at addition")
        basel = Tex(r"Lets have a go at addition")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()