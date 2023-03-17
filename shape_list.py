from shape import Shape
from triangle import Triangle, EquilateralTriangle
from rectangle import Rectangle, Square
from circle import Circle
from regular_pentagon import RegularPentagon
from rhombus import Rhombus
from display import Displayer

class ShapeList():
    def __init__(self):
        self.shapes = []
        self.displayer =  Displayer()

    def add_shape(self,shape):
        if isinstance (shape, Shape):
            self.shapes.append(shape)
            self.displayer.display(f"{shape} has been added to the list")
        else:
            raise TypeError("The object is not a shape")
        
    def show_all_shapes(self):
        if not self.shapes:
            raise ValueError("Shape List is empty")
        for shape in self.shapes:
            self.displayer.display(shape)
        
    def get_shape_at(self, shape_index):
        shape = self.shapes[shape_index]
        return shape

    def get_largest_shape_by_perimeter(self):
        shapes_perimeters = []
        if not self.shapes:
            raise ValueError("Shape List is empty")
        else:
            for shape in self.shapes:
                    perimeter = shape.calculate_perimeter()
                    shapes_perimeters.append(perimeter)
            index_of_largest_perimeter_shape = shapes_perimeters.index(max(shapes_perimeters))
            largest_shape = self.get_shape_at(index_of_largest_perimeter_shape)
            self.displayer.display(largest_shape)

    def get_largest_shape_by_area(self):
        shapes_areas = []
        if not self.shapes:
            raise ValueError("Shape List is empty")
        else:
            for shape in self.shapes:
                area = shape.calculate_area()
                shapes_areas.append(area)
            index_of_largest_area_shape = shapes_areas.index(max(shapes_areas))
            largest_shape = self.get_shape_at(index_of_largest_area_shape)
            self.displayer.display(largest_shape)

    def create_shape(self):
        shape_type = self.displayer.choose_shape_type_to_add()
        if shape_type == "circle":
            r = float(input("Please enter the radius of the circle: "))
            shape = Circle(r)
            return shape

        elif shape_type == "triangle":
            a = float(input("Please enter the length of side a: "))
            b = float(input("Please enter the length of side b: "))
            c = float(input("Please enter the length of side c: "))
            shape = Triangle(a, b, c)
            return shape

        elif shape_type == "equilateral triangle":
            a = float(input("Please enter the side length of the triangle: "))
            shape = EquilateralTriangle(a)
            return shape

        elif shape_type == "rectangle":
            a = float(input("Please enter the width of the rectangle: "))
            b = float(input("Please enter the height of the rectangle: "))
            shape = Rectangle(a,b)
            return shape

        elif shape_type == "square":
            a = float(input("Please enter the side length of the square: "))
            shape = Square(a)
            return shape
        
        elif shape_type == "regular pentagon":
            a = float(input("Please enter the side length of the pentagon: "))
            shape = RegularPentagon(a)
            return shape

        elif shape_type == "rhombus":
            a = float(input("Please enter the side length of the rhombus: "))
            d1 = float(input("Please enter the first diagonal length: "))
            d2 = float(input("Please enter the second diagonal length: "))
            shape = Rhombus(a,d1,d2)
            return shape

        else:
            self.displayer.display("Invalid shape name")
            return self.create_shape(self)
        
    def show_shape_formulas(self):
        shape = self.displayer.choose_shape_to_show_formula()
        if shape == "circle":
            circle = Circle(1)
            self.displayer.print_perimeter_and_area_formula(circle)

        elif shape == "triangle":
            triangle = Triangle(1,2,3)
            self.displayer.print_perimeter_and_area_formula(triangle)

        elif shape == "equilateral triangle":
            equilateral_triangle = EquilateralTriangle(1)
            self.displayer.print_perimeter_and_area_formula(equilateral_triangle)

        elif shape == "rectangle":
            rectangle = Rectangle(1,2)
            self.displayer.print_perimeter_and_area_formula(rectangle)

        elif shape == "square":
            square = Square(1)
            self.displayer.print_perimeter_and_area_formula(square)

        elif shape == "regular pentagon":
            regular_pentagon = RegularPentagon(1)
            self.displayer.print_perimeter_and_area_formula(regular_pentagon)

        elif shape == "rhombus":
            rhombus = Rhombus(1,2,3)
            self.displayer.print_perimeter_and_area_formula(rhombus)

        else:
            self.displayer.display("Invalid shape name")
            return self.show_shape_formulas()
        
    def __str__(self):
        return f"{self.shapes}"
        