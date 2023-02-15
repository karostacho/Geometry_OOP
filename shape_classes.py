from shapes import Shape
import math

class Circle(Shape):
    def __init__(self, r):
        Shape.check_if_args_greater_than_zero([r])
        self.name = "circle"
        self.r = r
        self.perimeter_formula = "2*math.pi * r"
        self.area_formula = "math.pi * r**2"

    def calculate_area(self):
        print (math.pi * self.r**2)

    def calculate_perimeter(self):
        return 2*math.pi * self.r

    def get_area_formula(self):
        return self.area_formula

    def get_perimeter_formula(self):
        return self.perimeter_formula


circle = Circle(3)
circle.calculate_area()
Shape.check_if_args_greater_than_zero([44])
circle2 = Circle(-3)
circle2.calculate_perimeter()