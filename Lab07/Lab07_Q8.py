
def binary_search_tuples(tuple_list, a_tuple):
    left_index = 0
    right_index = len(tuple_list)






my_list = [(1,5),(1,7),(2,1),(2,5),(3,1),(3,5)] 
a_tuple = (3,1)
print(binary_search_tuples(my_list, a_tuple))

"""
def binary_search_tuples(my_list, a_tuple):
    left_index = 0
    right_index = len(my_list)-1
    step_count = 0
    while right_index > left_index:
        step_count += 1
        mid_index = (right_index + left_index) // 2
        print("left: ", left_index, ", right: ", right_index, ", mid: ", mid_index, sep="")
        if my_list[mid_index] == a_tuple:
            return mid_index
        if my_list[mid_index][0] < a_tuple[0]:
            if my_list[mid_index][1] < a_tuple[1]:
                left_index = mid_index +1
        if (my_list[mid_index][0] > a_tuple[0]):
            if my_list[mid_index][1] > a_tuple[1]:
                right_index = mid_index -1
        if (right_index < left_index) or (right_index == left_index):
            return (-1, step_count)
"""

"""
def binary_search_tuples(my_list, a_tuple):
    left_index = 0
    right_index = len(my_list)-1
    step_count = 0
    while right_index > left_index:
        step_count += 1
        mid_index = (right_index + left_index) // 2
        print("left: ", left_index, ", right: ", right_index, ", mid: ", mid_index, sep="")
        if my_list[mid_index] == a_tuple:
            return mid_index
        if my_list[mid_index][0] < a_tuple[0]:
            if my_list[mid_index][1] < a_tuple[1]:
                left_index = mid_index +1
        if (my_list[mid_index][0] > a_tuple[0]):
            if my_list[mid_index][1] > a_tuple[1]:
                right_index = mid_index -1
        if (right_index < left_index) or (right_index == left_index):
            return (-1, step_count)
"""