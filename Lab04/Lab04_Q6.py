
def get_smallest_even(filename):
    try:
        input_file = open(filename, 'r')
        items_list = input_file.read().split()
        input_file.close()
        smallest = False
        for element in items_list:
            try:
                value = int(element)
                if value % 2 == 0:
                    if not smallest:
                        smallest = value
                    elif value < smallest:
                        smallest = value
            except ValueError:
                element = element
        return smallest
    except FileNotFoundError:
        file_name = "'" + str(filename) + "'"
        print("ERROR: The file " + file_name + " does not exist.")
        