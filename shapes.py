class Shape:
    def __init__(self, name, formula_p, formula_a):
        self.name = name
        self.formula_p = formula_p
        self.formula_a = formula_a
        #self.attributes = []
        #self.attributes = attributes 
        
    def get_name(self):
        self.name = input("What shape would you like to add?")

    def calculate_area(self, area):
        return float(area)
    
    def calculate_perimeter(self):
        return float(self.formula_p)
    
    def get_area_formula(self):
        print(str(self.formula_a))

    def get_perimeter_formula(self):
        return (f"{self.formula_p}")

    def __str__(self):
        perimeter = Shape.calculate_perimeter(self)
        return (f"{self.name} (perimeter: {perimeter})")

    @staticmethod
    def check_if_args_greater_than_zero(args):
        if any(arg > 0 for arg in args):
            return True
        if any(arg <= 0 for arg in args):
            raise ValueError("Argument can't be less or equal to 0")
