from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number, **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

class CountdownScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))
        self.add(number)
        self.wait()
        # Play the Count Animation to count from 5 to 0 in 5 seconds
        self.play(Count(number, 5, 0), run_time=5, rate_func=linear)
        self.wait()
