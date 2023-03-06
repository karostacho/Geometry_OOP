from shape_list import ShapeList
from triangle import Triangle, EquilateralTriangle
from rectangle import Rectangle, Square
from circle import Circle
from regular_pentagon import RegularPentagon

def display_menu():
    user_input = input("Learn Geometry.\n  What do you want to do?\n  (1) Add new shape\n  (2) Show all shapes\n  (3) Show shape with the largest perimeter\n  (4) Show shape with the largest area\n  (5) Show formulas\n  (0) Exit program\n")
    return user_input

def inform_the_selection_is_invalid():
    print("\nInvalid selection. Please select a number 0-5\n")

def choose_shape_type_to_add():
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
    else:
        print("Invalid shape name")
        return choose_shape_type_to_add()
    print(f"{shape} has been added to the list")
    return shape
    
 
def show_formulas():
    shape = input("Formula of which shape would you like to see? ")
    if shape == "circle":
        circle = Circle(1)
        print(f"perimeter formula: {circle.get_perimeter_formula()}\narea formula: {circle.get_area_formula()}")

    elif shape == "triangle":
        triangle = Triangle(1,2,3)
        print(f"perimeter formula: {triangle.get_perimeter_formula()}\narea formula: {triangle.get_area_formula()}")

    elif shape == "equilateral triangle":
        equilateral_triangle = EquilateralTriangle(1)
        print(f"perimeter formula: {equilateral_triangle.get_perimeter_formula()}\narea formula: {equilateral_triangle.get_area_formula()}")

    elif shape == "rectangle":
        rectangle = Rectangle(1,2)
        print(f"perimeter formula: {rectangle.get_perimeter_formula()}\narea formula: {rectangle.get_area_formula()}")

    elif shape == "square":
        square = Square(1)
        print(f"perimeter formula: {square.get_perimeter_formula()}\narea formula: {square.get_area_formula()}")

    elif shape == "regular pentagon":
        regular_pentagon = RegularPentagon(1)
        print(f"perimeter formula: {regular_pentagon.get_perimeter_formula()}\narea formula: {regular_pentagon.get_area_formula()}")

    else:
        print("Invalid shape name")
        return show_formulas()
