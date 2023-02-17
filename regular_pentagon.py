from shape import Shape
import math

class RegularPentagon(Shape):
    def __init__(self, a):
        self.a = a
        Shape.check_if_args_greater_than_zero([self.a])
        self.name = "regular pentagon"
        self.perimeter_formula = "5a"
        self.area_formula = "1/4(√5(5+2√5)s2)"

    def calculate_area(self):
        return self.a * 5

    def calculate_perimeter(self):
        return (math.sqrt(5*(5+2*math.sqrt(5)))*self.a**2)/4

    def get_area_formula(self):
        return self.area_formula 

    def get_perimeter_formula(self):
        return self.perimeter_formula
