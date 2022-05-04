
def br():
    print("=" * 20)

br()

class Car:

    def __init__(self, license_plate, row, column, row_speed, column_speed):

        self.license_plate = license_plate
        self.row = row
        self.column = column
        self.row_speed = row_speed
        self.column_speed = column_speed
        self.has_collided = False

    def collides(self, other_car):

        if (self.row == other_car.row) and (self.column == other_car.column):
            other_car.has_collided = True
            self.has_collided = True
            return True
        else:
            return False

    def move(self, num_rows, num_columns):

        adjusted_row = self.row
        adjusted_column = self.column

        if self.has_collided != True:
            for index in range(abs(self.row_speed)):
                if self.row_speed > 0:
                    adjusted_row += 1
                    if adjusted_row > (num_rows-1):
                        adjusted_row = 0
                if self.row_speed < 0:
                    adjusted_row -= 1
                    if adjusted_row < 0:
                        adjusted_row = num_rows-1

            for index in range(abs(self.column_speed)):
                if self.column_speed > 0:
                    adjusted_column += 1
                    if adjusted_column > (num_columns-1):
                        adjusted_column = 0
                if self.column_speed < 0:
                    adjusted_column -= 1
                    if adjusted_column < 0:
                        adjusted_column = num_columns-1

            
        self.row = adjusted_row
        self.column = adjusted_column


    def __str__(self):
        return str(self.license_plate) + "_" + str(self.row) + "_" + str(self.column)


class Traffic():

    def __init__(self, num_rows, num_columns):
        
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.car_list = []

    def add_car(self, car):

        if (car.row > (self.num_rows-1)) or (car.row < 0):
            raise ValueError("Invalid position")
        if (car.column > (self.num_columns-1)) or (car.column < 0):
            raise ValueError("Invalid position")

        if len(self.car_list) > 0:
            for list_car in self.car_list:
                if list_car.license_plate == car.license_plate:
                    raise ValueError("Car in use")
                if (list_car.row == car.row) and (list_car.column == car.column):
                    raise ValueError("Position in use")

        self.car_list += [car]

    def get_collisions(self):
        
        collision_list = []
        for iteration in range(len(self.car_list)-1):
            compare_car = self.car_list[iteration]
            for index in range(len(self.car_list)):
                if index != iteration:
                    if (self.car_list[index].row, self.car_list[index].column) not in collision_list:
                        if compare_car.collides(self.car_list[index]):
                            collision_list += [(compare_car.row, compare_car.column)]
        
        collision_list.sort()
        return collision_list
    def __str__(self):

        output_string = ""

        for index in range(len(self.car_list)):
            list_num = index+1
            output_string += (str(list_num) + ") " + str(self.car_list[index]) + "\n")
           
        return output_string
    
    def execute(self, moves):

        for index in range(moves):
            collision_list = self.get_collisions()
            for car in self.car_list:
                if (car.row, car.column) not in collision_list:
                    car.move(self.num_rows, self.num_columns)
        
    def get_plates(self, row, column):

        license_list = []
        for car in self.car_list:
            if (car.row == row) and (car.column == column):
                license_list += [car.license_plate]
        return sorted(license_list)

    def get_location(self, license_plate):

        for car in self.car_list:
            if car.license_plate == license_plate:
                return (car.row, car.column)

simulation = Traffic(10, 10)
c1 = Car('ABC123', 0, 0, 2, 2)
c2 = Car('DEF456', 2, 8, -1, 0)
c3 = Car('GHI789', 1, 6, -3, 1)
c4 = Car('JKL123', 3, 3, 1, 1)
c5 = Car('MNO456', 7, 9, 0, 3)
c6 = Car('PQR789', 2, 4, 1, 0)
c7 = Car('STU123', 4, 0, -2, -1)
c8 = Car('VWX456', 6, 7, 0, 1)
c9 = Car('YZZ789', 9, 2, 1, -1)
c10 = Car('AAA111', 5, 5, 4, 3)
c11 = Car('ZZZ999', 5, 7, 0, 0)
c12 = Car('WWW777', 7, 7, 1, 1)
simulation.add_car(c1)
simulation.add_car(c2)
simulation.add_car(c3)
simulation.add_car(c4)
simulation.add_car(c5)
simulation.add_car(c6)
simulation.add_car(c7)
simulation.add_car(c8)
simulation.add_car(c9)
simulation.add_car(c10)
simulation.add_car(c11)
simulation.add_car(c12)

simulation.execute(35)

print(simulation.get_collisions())
print(simulation.get_plates(4, 4))
print(simulation.get_location('VWX456'))
print(simulation.get_location('YZZ789'))

br()






"""
        collision_list = []
        for num_iterations in range(len(self.car_list)-1):
            compare_car = self.car_list[num_iterations]
            for index in range(len(self.car_list)):
                if index != num_iterations:
                    if self.car_list[index] not in collision_list:
                        if (compare_car.row == self.car_list[index].row) and (compare_car.column == self.car_list[index].column):
                            collision_list += [(compare_car.row, compare_car.column)]
"""

















