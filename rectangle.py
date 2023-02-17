from shape import Shape

class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        Shape.check_if_args_greater_than_zero([self.a,self.b])
        self.name = "rectangle"
        self.perimeter_formula = "2a +2b"
        self.area_formula = "ab"

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return self.a*self.b

    def get_area_formula(self):
        return self.area_formula

    def get_perimeter_formula(self):
        return self.perimeter_formula

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)
        self.perimeter_formula = "4a"
        self.area_formula = "a2"