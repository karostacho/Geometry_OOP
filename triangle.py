from shape import Shape
import math

class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.are_all_args_greater_than_zero([a, b, c])
        self.a = a
        self.b = b
        self.c = c
        self.is_triangle_possible()
        self.name = "triangle"
        self.perimeter_formula = "a+b+c"
        self.area_formula = "√(s(s-a)(s-b)(s-c))"

    def calculate_area(self):
        s = (self.a+self.b+ self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def calculate_perimeter(self):
        return self.a+self.b+ self.c

    def get_area_formula(self):
        return self.area_formula

    def get_perimeter_formula(self):
        return self.perimeter_formula
    
    def is_triangle_possible(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            return True
        raise ValueError("Triangle impossible. One side can't be greater than sum of two others.")
        
    def __str__(self):
        return (f"{self.name} (side lengths: a = {self.a}, b = {self.b}, c = {self.c})")
    
class EquilateralTriangle(Triangle):
    def __init__(self,a):
        super().__init__(a,a,a)
        self.perimeter_formula = "3a"
        self.area_formula = "√s(s-a)**3)"

    def __str__(self):
        return (f"{self.name} (side length: a = {self.a})")
