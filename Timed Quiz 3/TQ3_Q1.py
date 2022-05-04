
def bubble_sort_portion(data, left_index, right_index):
    passes = right_index - left_index
    for iteration in range(passes):
        for index in range(passes):
            start_pos = left_index + index
            if data[start_pos] > data[start_pos+1]:
                data[start_pos], data[start_pos+1] = data[start_pos+1], data[start_pos]
        print(data)


 	
"""
values = [3, 1, 2]
bubble_sort_portion(values, 0, 2)
"""
values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort_portion(values, 2, 4)
