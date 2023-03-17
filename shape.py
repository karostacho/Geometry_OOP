from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def get_area_formula(self):
        pass

    @abstractmethod
    def get_perimeter_formula(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @staticmethod
    def are_all_args_greater_than_zero(args):
        if all(arg > 0 for arg in args):
            return True
        else:
            raise ValueError("Argument can't be less or equal to 0")
