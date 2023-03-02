from shape import Shape

class ShapeList():
    def __init__(self):
        self.shapes = [] 

    def add_shape(self,shape):
        if isinstance (shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError("The object is not a shape")
        
    def show_all_shapes(self):
        for shape in self.shapes:
            print(shape)
    
    def get_shape_at(self, shape_index):
        shape = self.shapes[shape_index]
        return shape

    def get_largest_shape_by_perimeter(self):
        shapes_perimeters = []
        for shape in self.shapes:
            perimeter = shape.calculate_perimeter()
            shapes_perimeters.append(perimeter)
        index_of_largest_shape = shapes_perimeters.index(max(shapes_perimeters))
        largest_shape = self.shapes[index_of_largest_shape]
        print (largest_shape)

    def get_largest_shape_by_area(self):
        shapes_areas = []
        for shape in self.shapes:
            area = shape.calculate_area()
            shapes_areas.append(area)
        index_of_largest_shape = shapes_areas.index(max(shapes_areas))
        largest_shape = self.shapes[index_of_largest_shape]
        print (largest_shape)

    def __str__(self):
        return f"{self.shapes}"
