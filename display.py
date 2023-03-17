from triangle import Triangle, EquilateralTriangle
from rectangle import Rectangle, Square
from circle import Circle
from regular_pentagon import RegularPentagon
from rhombus import Rhombus

class Displayer():

    def display_menu(self):
        user_input = input("Learn Geometry.\n  What do you want to do?\n  (1) Add new shape\n  (2) Show all shapes\n  (3) Show shape with the largest perimeter\n  (4) Show shape with the largest area\n  (5) Show formulas\n  (0) Exit program\n")
        return user_input

    def inform_the_selection_is_invalid(self):
        print("\nInvalid selection. Please select a number 0-5\n")

    def choose_shape_type_to_add(self):
        shape_type = input("What shape would you like to add? ")
        if shape_type == "circle":
            r = float(input("Please enter the radius of the circle: "))
            shape = Circle(r)

        elif shape_type == "triangle":
            a = float(input("Please enter the length of side a: "))
            b = float(input("Please enter the length of side b: "))
            c = float(input("Please enter the length of side c: "))
            shape = Triangle(a, b, c)

        elif shape_type == "equilateral triangle":
            a = float(input("Please enter the side length of the triangle: "))
            shape = EquilateralTriangle(a)

        elif shape_type == "rectangle":
            a = float(input("Please enter the width of the rectangle: "))
            b = float(input("Please enter the height of the rectangle: "))
            shape = Rectangle(a,b)

        elif shape_type == "square":
            a = float(input("Please enter the side length of the square: "))
            shape = Square(a)
        
        elif shape_type == "regular pentagon":
            a = float(input("Please enter the side length of the pentagon: "))
            shape = RegularPentagon(a)

        elif shape_type == "rhombus":
            a = float(input("Please enter the side length of the rhombus: "))
            d1 = float(input("Please enter the first diagonal length: "))
            d2 = float(input("Please enter the second diagonal length: "))
            shape = Rhombus(a,d1,d2)

        else:
            print("Invalid shape name")
            return self.choose_shape_type_to_add()
        print(f"{shape} has been added to the list")
        return shape
        
    
    def show_formulas(self):
        shape = input("Formula of which shape would you like to see? ")
        if shape == "circle":
            circle = Circle(1)
            self.print_perimeter_and_area_formula(circle)

        elif shape == "triangle":
            triangle = Triangle(1,2,3)
            self.print_perimeter_and_area_formula(triangle)

        elif shape == "equilateral triangle":
            equilateral_triangle = EquilateralTriangle(1)
            self.print_perimeter_and_area_formula(equilateral_triangle)

        elif shape == "rectangle":
            rectangle = Rectangle(1,2)
            self.print_perimeter_and_area_formula(rectangle)

        elif shape == "square":
            square = Square(1)
            self.print_perimeter_and_area_formula(square)

        elif shape == "regular pentagon":
            regular_pentagon = RegularPentagon(1)
            self.print_perimeter_and_area_formula(regular_pentagon)

        elif shape == "rhombus":
            rhombus = Rhombus(1,2,3)
            self.print_perimeter_and_area_formula(rhombus)

        else:
            print("Invalid shape name")
            return self.show_formulas()

    def print_perimeter_and_area_formula(self,shape):
        print ((f"perimeter formula: {shape.get_perimeter_formula()}\narea formula: {shape.get_area_formula()}"))