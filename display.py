from shape_list import ShapeList
from shape import Shape
from triangle import Triangle, EquilateralTriangle
from rectangle import Rectangle, Square
from circle import Circle
from regular_pentagon import RegularPentagon

shape_list = ShapeList()
def display_menu():
    user_input = int(input("Learn Geometry.\n  What do you want to do?\n  (1) Add new shape\n  (2) Show all shapes\n  (3) Show shape with the largest perimeter\n  (4) Show shape with the largest area\n  (5) Show formulas\n  (0) Exit program\n"))
    if user_input == 0:
        quit()
    if user_input == 1:
        add_new_shape()
    if user_input == 2:
        print(shape_list)
    if user_input == 3:
        shape_list.get_largest_shape_by_perimeter()
    if user_input == 4:
        shape_list.get_largest_shape_by_area()
    if user_input == 5:   
        show_formula()

def add_new_shape():
    shape_type = input("What shape would you like to add? ")
    if shape_type == "circle":
        r = float(input("Please enter the radius of the circle: "))
        shape = Circle(r)

    if shape_type == "triangle":
        a = float(input("Please enter the length of side a: "))
        b = float(input("Please enter the length of side b: "))
        c = float(input("Please enter the length of side c: "))
        shape = Triangle(a, b, c)

    if shape_type == "equilateral triangle":
        a = float(input("Please enter the side length of the triangle: "))
        shape = EquilateralTriangle(a)

    if shape_type == "rectangle":
        a = float(input("Please enter the width of the rectangle: "))
        b = float(input("Please enter the height of the rectangle: "))
        shape = Rectangle(a)

    if shape_type == "square":
        side = float(input("Please enter the side length of the square: "))
        shape = Square(side)
    
    if shape_type == "regular pentagon":
        side = float(input("Please enter the side length of the pentagon: "))
        shape = RegularPentagon(side)
    shape_list.add_shape(shape)
    print(f"{shape} has been added to the list")


def show_formula():
    shape_type = input("Formula of which shape you would like to see? ")
    if shape_type == "circle":
        print (Circle.get_perimeter_formula())

    if shape_type == "triangle":
        print (Triangle.get_perimeter_formula())

    if shape_type == "equilateral triangle":
        print (EquilateralTriangle.get_perimeter_formula())

    if shape_type == "rectangle":
        print (Rectangle.get_perimeter_formula())
    
    if shape_type == "square":
        print (Square.get_perimeter_formula())

    if shape_type == "regular pentagon":
        print (RegularPentagon.get_perimeter_formula())
    

display_menu()