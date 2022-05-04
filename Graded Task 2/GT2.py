
def br():
    print("=" * 20)

br()

class GridMap:

    def __init__(self, num_rows, num_columns):

        self.num_rows = num_rows
        self.num_columns = num_columns
        self.coord_A = []
        self.coord_Z = []
        
    def add_start(self, row_A, column_A):
        self.coord_A = [row_A, column_A]


    def add_end(self, row_Z, column_Z):
        self.coord_Z = [row_Z, column_Z]


    def __str__(self):
        str_grid = ""
        grid_list = []

        #Initialising 2D Array
        for row in range(self.num_rows):
            grid_list += [["0"] * self.num_columns]

        #Adding Start Coord
        if len(self.coord_A) != 0 and (len(self.coord_Z) == 0):
            grid_list[self.coord_A[0]][self.coord_A[1]] = "A"
            for row in range(self.num_rows):
                for column in range(len(grid_list[row])):
                    str_grid += grid_list[row][column]
                str_grid += "\n"
            return str_grid

        #Adding End Coord / Adding Path
        elif len(self.coord_Z) != 0:
            grid_list[self.coord_A[0]][self.coord_A[1]] = "A"
            grid_list[self.coord_Z[0]][self.coord_Z[1]] = "Z"
            #If they are on the same row
            if self.coord_A[0] == self.coord_Z[0]:
                #If coord A comes after coord Z
                if self.coord_A[1] > self.coord_Z[1]:
                    for index in range(self.num_columns):
                        if (index > self.coord_Z[1]) and (index < self.coord_A[1]):
                            grid_list[self.coord_A[0]][index] = "X"
                #If coord A comes before Coord Z
                elif self.coord_A[1] < self.coord_Z[1]:
                    for index in range(self.num_columns):
                        if (index > self.coord_A[1]) and (index < self.coord_Z[1]):
                            grid_list[self.coord_A[0]][index] = "X"
            else:
                for iteration in range(self.num_rows):
                    for index in range(self.num_columns):
                        if iteration == self.coord_A[0]:
                            if self.coord_A[1] < self.coord_Z[1]:
                                if (index > self.coord_A[1]) and (index <= self.coord_Z[1]):
                                    grid_list[iteration][index] = "X"
                            if self.coord_A[1] > self.coord_Z[1]:
                                if (index < self.coord_A[1]) and (index >= self.coord_Z[1]):
                                    grid_list[iteration][index] = "X"
                        elif self.coord_Z[0] < self.coord_A[0]:
                            if (iteration < self.coord_A[0]) and (iteration > self.coord_Z[0]):
                                if index == self.coord_Z[1]:
                                    grid_list[iteration][index] = "X"
                        elif self.coord_Z[0] > self.coord_A[0]:
                            if (iteration > self.coord_A[0]) and (iteration < self.coord_Z[0]):
                                if index == self.coord_Z[1]:
                                    grid_list[iteration][index] = "X"

            for row in range(self.num_rows):
                for column in range(len(grid_list[row])):
                    str_grid += grid_list[row][column]
                str_grid += "\n"
            return str_grid
        
        else:
            for row in range(self.num_rows):
                for column in range(len(grid_list[row])):
                    str_grid += grid_list[row][column]
                str_grid += "\n"
            return str_grid



m = GridMap(5, 5)
m.add_start(0, 0)
m.add_end(4, 3)
print(m)

br()
"""
        for row in range(self.num_rows):
            for element in single_row_list:
                str_grid += element
            if row != self.num_rows-1:
                str_grid += "\n"
        return str_grid
"""

"""
    def __str__(self):
        str_grid = ""

        if len(self.coord_A) != 0 and (len(self.coord_Z) == 0):
            grid_list = []
            for row in range(self.num_rows):
                if row == self.coord_A[0]:
                    grid_list += ["0" * (self.coord_A[1]) + "A" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                else:
                    grid_list += ["0" * self.num_columns]

            for row in range(self.num_rows):
                for element in grid_list[row]:
                    str_grid += element
                if row != self.num_rows-1:
                    str_grid += "\n"
            str_grid += "\n"
            return str_grid

        elif len(self.coord_Z) != 0:
            grid_list = []
            for row in range(self.num_rows):
                #If both coords on the same row
                if (row == self.coord_A[0]) and (row == self.coord_Z[0]):
                    grid_list += ["0" * (self.coord_A[1]) + "A" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                    if self.coord_Z[1] < self.coord_A[1]:
                        grid_list += ["0" * self.coord_Z[1] + "Z" + ("0" * (self.coord_A - self.coord_Z) + "A") + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                #If coord_A on row
                elif row == self.coord_A[0]:
                    grid_list += ["0" * (self.coord_A[1]) + "A" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]

                #If coord_Z on row
                elif row == self.coord_Z[0]:
                    grid_list += ["0" * (self.coord_Z[1]) + "Z" + ("0" * ((self.num_columns-1) - self.coord_Z[1]))]
                else:
                    grid_list += ["0" * self.num_columns]

            for row in range(self.num_rows):
                for element in grid_list[row]:
                    str_grid += element
                if row != self.num_rows-1:
                    str_grid += "\n"
            str_grid += "\n"
            return str_grid

        else:
            grid_list = []
            for row in range(self.num_rows):
                grid_list += ["0" * self.num_columns]

            for row in range(self.num_rows):
                for element in grid_list[row]:
                    str_grid += element
                if row != self.num_rows-1:
                    str_grid += "\n"
            str_grid += "\n"
            return str_grid

"""
"""
    def __str__(self):
        str_grid = ""

        if len(self.coord_A) != 0 and (len(self.coord_Z) == 0):
            grid_list = []
            for row in range(self.num_rows):
                if row == self.coord_A[0]:
                    grid_list += ["0" * (self.coord_A[1]) + "A" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                else:
                    grid_list += ["0" * self.num_columns]

            for row in range(self.num_rows):
                for element in grid_list[row]:
                    str_grid += element
                if row != self.num_rows-1:
                    str_grid += "\n"
            str_grid += "\n"
            return str_grid

        elif len(self.coord_Z) != 0:
            grid_list = []
            for row in range(self.num_rows):

                #If both coords on the same row
                if (row == self.coord_A[0]) and (row == self.coord_Z[0]):
                    grid_list += ["0" * (self.coord_A[1]) + "A" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                    if self.coord_Z[1] < self.coord_A[1]:
                        grid_list += ["0" * self.coord_Z[1] + "Z" + ("0" * (self.coord_A - self.coord_Z) + "A") + ("0" * ((self.num_columns-1) - self.coord_A[1]))]

                #If coord_A on row
                elif row == self.coord_A[0]:
                    if self.coord_A[1] > self.coord_Z[1]:
                        grid_list += ["0" * (self.coord_Z[1]) + "X" * (self.coord_A[1] - self.coord_Z[1]) + "A" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                    elif self.coord_A[1] < self.coord_Z[1]:
                         grid_list += ["0" * (self.coord_A[1]) + "A" + ("X" * (self.coord_Z[1] - self.coord_A[1]))+ ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                    else:
                        grid_list += ["0" * (self.coord_A[1]) + "A" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]

                #If coord_Z on row
                elif row == self.coord_Z[0]:
                    if self.coord_Z[1] > self.coord_A[1]:
                        grid_list += ["0" * (self.coord_A[1]) + "X" * (self.coord_Z[1] - self.coord_A[1]) + "Z" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                    elif self.coord_A[1] < self.coord_Z[1]:
                         grid_list += ["0" * (self.coord_Z[1]) + "Z" + ("X" * (self.coord_A[1] - self.coord_Z[1]))+ ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                    else:
                        grid_list += ["0" * (self.coord_Z[1]) + "Z" + ("0" * ((self.num_columns-1) - self.coord_Z[1]))]

                else:
                    if row > self.coord_A[0]:
                        grid_list += ["0" * self.coord_A[1] + "X" + ("0" * ((self.num_columns-1) - self.coord_A[1]))]
                    elif row > self.coord_Z[0]:
                        grid_list += [("0" * self.coord_Z[1]) + "X" + ("0" * ((self.num_columns-1) - self.coord_Z[1]))]
                    else:
                        grid_list += ["0" * self.num_columns]

            for row in range(self.num_rows):
                for element in grid_list[row]:
                    str_grid += element
                if row != self.num_rows-1:
                    str_grid += "\n"
            str_grid += "\n"
            return str_grid

        else:
            grid_list = []
            for row in range(self.num_rows):
                grid_list += ["0" * self.num_columns]

            for row in range(self.num_rows):
                for element in grid_list[row]:
                    str_grid += element
                if row != self.num_rows-1:
                    str_grid += "\n"
            str_grid += "\n"
            return str_grid
"""