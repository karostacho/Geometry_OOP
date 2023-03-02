from shape import Shape
import math

class Circle(Shape):
    def __init__(self, r):
        Shape.check_if_args_greater_than_zero([r])
        self.name = "circle"
        self.r = r
        self.perimeter_formula = "2\u03C0r"
        self.area_formula = "\u03C0r2"

    def calculate_area(self):
        return math.pi * self.r**2

    def calculate_perimeter(self):
        return 2*math.pi * self.r

    def get_area_formula(self):
        return self.area_formula

    def get_perimeter_formula(self):
        return self.perimeter_formula

    def __str__(self):
        return (f"{self.name} (radius length: r = {self.r}) ")
