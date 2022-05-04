
class Car:

    def __init__(self, colour):
        self.colour = colour
        self.velocity = 0

    def __str__(self):
        return str(self.colour) + " (" + str(self.velocity) + ")"
    
    def accelerate(self, speed_increase):
        self.velocity += speed_increase

    def brake(self):
        if self.velocity >= 10:
            self.velocity -= 10
        else:
            self.velocity -= self.velocity