import math

class Circle:

    def __init__(self, radius = 1):
        self.radius = radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius
    