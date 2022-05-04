
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

    def move(self, num_rows, num_columns):

        adjusted_row = self.row
        adjusted_column = self.column
        
        for i in range(abs(self.row_speed)):
            if self.row_speed > 0:
                adjusted_row += 1
                if adjusted_row > (num_rows-1):
                    adjusted_row = 0
            if self.row_speed < 0:
                adjusted_row -= 1
                if adjusted_row < 0:
                    adjusted_row = num_rows-1

        for i in range(abs(self.column_speed)):
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

    def __str__(self):

        output_string = ""

        for index in range(len(self.car_list)):
            list_num = index+1
            output_string += (str(list_num) + ") " + str(self.car_list[index]) + "\n")
           
        return output_string
    
    def execute(self, moves):

        for index in range(moves):
            for car in self.car_list:
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
c1 = Car('ABC123', 5, 5, 1, 1)
c2 = Car('DEF456', 3, 6, 0, 2)
c3 = Car('XYZ999', 9, 9, 0, 0)
simulation.add_car(c1)
simulation.add_car(c2)
simulation.add_car(c3)

print(simulation.get_location('DEF456'))
print(simulation.get_plates(9, 9))

br()

























