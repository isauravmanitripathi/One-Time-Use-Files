from manim import *

class InnovationsPricing(Scene):
    def construct(self):
        title = Text("Innovations in Pricing Derivatives", font_size=40, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Stock price random path
        path = VMobject(color=BLUE)
        points = [LEFT*5+DOWN, LEFT*4+UP*0.5, LEFT*3+DOWN*0.5, LEFT*2+UP*1.2,
                  LEFT+DOWN*0.2, ORIGIN+UP*1.5, RIGHT+UP*0.3, RIGHT*2+UP*2]
        path.set_points_smoothly(points)
        self.play(Create(path))
        self.wait(1)

        # Barrier reflection principle
        barrier = DashedLine(LEFT*5+UP*1.2, RIGHT*3+UP*1.2, color=RED)
        barrier_label = Text("Barrier c", font_size=24, color=RED).next_to(barrier, UP)
        self.play(Create(barrier), Write(barrier_label))
        self.wait(1)

        reflected = path.copy().set_color(GREEN).flip(UP)
        self.play(TransformFromCopy(path, reflected))
        self.wait(2)
        self.play(FadeOut(barrier, barrier_label, reflected, path))

        # Reflection formula minimal text
        formula = MathTex(r"P(M_t > c) = 2P(B_t > c)", font_size=36, color=BLUE)
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))

        # Option pricing idea – Gaussian averaging
        curve = FunctionGraph(lambda x: np.exp(-x**2/2)/np.sqrt(2*PI), x_range=[-3,3], color=YELLOW)
        self.play(Create(curve))
        avg_label = Text("Averaging payoffs under Gaussian curve", font_size=28, color=WHITE).next_to(curve, DOWN)
        self.play(Write(avg_label))
        self.wait(2)
        self.play(FadeOut(curve, avg_label))

        # Black-Scholes Equation
        eqn = MathTex(r"\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = rV",
                      font_size=34, color=GREEN)
        self.play(Write(eqn))
        self.wait(3)
        self.play(FadeOut(eqn))

        # Market boom animation
        market_arrow = Arrow(LEFT*3+DOWN, RIGHT*3+UP*2, buff=0.3, color=BLUE)
        trillions = Text("$600+ Trillion Market", font_size=36, color=BLUE).next_to(market_arrow, UP)
        self.play(GrowArrow(market_arrow), Write(trillions))
        self.wait(2)
        self.play(FadeOut(market_arrow, trillions))

        # Black Swan Event
        crash = SVGMobject("/usr/share/icons/Adwaita/scalable/status/dialog-error-symbolic.svg").scale(1.5).set_color(RED)
        crash_text = Text("Black Swan Crash 1987", font_size=32, color=RED).next_to(crash, DOWN)
        self.play(FadeIn(crash), Write(crash_text))
        self.wait(2)
        self.play(FadeOut(crash, crash_text))

        # Final message
        closing = Text("Profound Impacts: Finance, Math & Economy", font_size=36, color=YELLOW)
        self.play(Write(closing))
        self.wait(3)