class Displayer():

    def display_menu(self):
        user_input = input("Learn Geometry.\n  What do you want to do?\n  (1) Add new shape\n  (2) Show all shapes\n  (3) Show shape with the largest perimeter\n  (4) Show shape with the largest area\n  (5) Show formulas\n  (0) Exit program\n")
        return user_input

    def inform_the_selection_is_invalid(self):
        self.display("\nInvalid selection. Please select a number 0-5\n")

    def choose_shape_type_to_add(self):
        shape_type = input("What shape would you like to add? ")
        return shape_type
        
    def choose_shape_to_show_formula(self):
        shape = input("Formula of which shape would you like to see? ")
        return shape

    def print_perimeter_and_area_formula(self,shape):
        self.display(f"perimeter formula: {shape.get_perimeter_formula()}\narea formula: {shape.get_area_formula()}")

    def display(self,message):
        print(message)