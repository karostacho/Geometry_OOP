from shape import Shape

class Rhombus(Shape):
    def __init__(self, a, d1, d2):
        Shape.are_all_args_greater_than_zero([a, d1, d2])
        self.a = a
        self.d1 = d1
        self.d2 = d2
        self.name = "rhombus"
        self.perimeter_formula = "4a"
        self.area_formula = "(d1 x d2)/2"

    def calculate_area(self):
        return (self.d1 * self.d2)/2

    def calculate_perimeter(self):
        return 4*self.a

    def get_area_formula(self):
        return self.area_formula 

    def get_perimeter_formula(self):
        return self.perimeter_formula
    
    def __str__(self):
        return (f"{self.name} (side length: a = {self.a}), first diagonal length: d1 = {self.d1}, second diagonal length: d2 = {self.d2}")