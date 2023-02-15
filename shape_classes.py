from shapes import Shape
import math

class Circle(Shape):
    def __init__(self, name, formula_p, formula_a, r):
        Shape.__init__(self, name, formula_p, formula_a)
        self.radius = r
        


r = float(input("what is radius?"))   
circle = Circle("circle", 2*math.pi * r, math.pi * r**2, r)
        
circle.get_area_formula()