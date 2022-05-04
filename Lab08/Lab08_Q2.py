import math

class Circle:
    
    def __init__(self, radius = 1):
        self.radius = radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius
    
    def get_diameter(self):
        return (self.radius * 2)

    def get_perimeter(self):
        perimeter = 2 * (self.radius * math.pi)
        return perimeter

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area