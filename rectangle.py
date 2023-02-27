from shape import Shape

class Rectangle(Shape):
    def __init__(self, a, b):
        Shape.check_if_args_greater_than_zero([a, b])
        self.a = a
        self.b = b
        self.name = "rectangle"
        self.perimeter_formula = "2a +2b"
        self.area_formula = "ab"

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return self.a * self.b

    def get_area_formula(self):
        return self.area_formula

    def get_perimeter_formula(self):
        return self.perimeter_formula
    
    def __str__(self):
        return (f"{self.name} (side lengths: a = {self.a}, b = {self.b}")

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        self.name = "square"
        self.perimeter_formula = "4a"
        self.area_formula = "a2"

    def __str__(self):
        return (f"{self.name} (side length: a = {self.a})")
