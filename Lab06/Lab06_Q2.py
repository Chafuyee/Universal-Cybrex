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


def selection_single_pass(data, index):
    largest_element_index = get_position_of_largest(data, index)
    data[largest_element_index], data[index] = data[index], data[largest_element_index]


numbers = [12, 24, 48, 53, 76]
selection_single_pass(numbers, 3)
print(numbers)