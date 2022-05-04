def br():
    print("=" * 20)

br()

class Car:

    def __init__(self, licence_plate, row, column, row_speed, column_speed):

        self.licence_plate = licence_plate
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
        return str(self.licence_plate) + "_" + str(self.row) + "_" + str(self.column)

c1 = Car('ABC123', 5, 5, 1, 1)
c2 = Car('DEF456', 0, 0, 0, 2)
c3 = Car('XYZ999', 9, 9, 0, 0)
c1.move(10, 10)
c2.move(10, 10)
c3.move(10, 10)

print(c1)
print(c2)
print(c3)

c1.move(10, 10)
c2.move(10, 10)

print(c1)
print(c2)

c1.move(10, 10)
c1.move(10, 10)

print(c1)

c1.move(10, 10)

print(c1)

"""
c1 = Car('ABC123', 4, 2, -1, 0)
c2 = Car('DEF456', 1, 4, 0, -2)

print(c1)
print(c2)

c1.move(5, 5)
c2.move(5, 5)

print(c1)
print(c2)

c1.move(5, 5)
c2.move(5, 5)

print(c1)
print(c2)

c1.move(5, 5)
c2.move(5, 5)

print(c1)
print(c2)
"""

br()

