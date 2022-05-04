
def selection_sort(data):
    num_elements = len(data)
    num_comparisons = 0
    num_swaps = 0
    for num_iteration in range(len(data)-1, 0, -1):
        for index in range(num_iteration, 0, -1):
            if index == num_iteration:
                num_comparisons += 1
                largest_element = data[index] 
                largest_index = index
            else:
                num_comparisons += 1
                if data[index] > largest_element:
                    largest_element = data[index]
                    largest_index = index
        data[largest_index], data[num_iteration] = data[num_iteration], data[largest_index]
        num_swaps += 1
    return (num_elements, num_comparisons, num_swaps)


data = [2, 4, 7, 8, 3]
selection_sort(data)