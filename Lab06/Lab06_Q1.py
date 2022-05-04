
def get_position_of_largest(data, index):
    element_index = 0
    for iteration in range(index+1):
        if iteration == 0:
            largest_element = data[iteration]
        else:
            if data[iteration] > largest_element:
                largest_element = data[iteration]
                element_index = iteration

    return element_index
 	
numbers = [20, 27, 69, 10, 76, 41]
print(get_position_of_largest(numbers, 2))

	

