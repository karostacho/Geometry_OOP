from display import display_menu, inform_the_selection_is_invalid, choose_shape_type_to_add, show_formulas
from shape_list import ShapeList

class Program:
    def __init__(self):
        self.shape_list = ShapeList()
        
    def run(self):
        user_input = display_menu()
        if not user_input.isdigit():
            inform_the_selection_is_invalid()
            return self.run()
        user_input = int(user_input)
        if user_input not in range(6):
            inform_the_selection_is_invalid()
            return self.run() 
        if user_input == 0:
            quit()
        if user_input == 1:
            shape = choose_shape_type_to_add()
            self.shape_list.add_shape(shape)
            return self.run() 
        if user_input == 2:
            self.shape_list.show_all_shapes()
            return self.run() 
        if user_input == 3:
            self.shape_list.get_largest_shape_by_perimeter()
            return self.run() 
        if user_input == 4:
            self.shape_list.get_largest_shape_by_area()
            return self.run() 
        if user_input == 5:   
            show_formulas()
            return self.run() 
        else:
            inform_the_selection_is_invalid()
            return self.run() 

geometry_program = Program()
geometry_program.run()
