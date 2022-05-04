
from operator import truediv
#Trimmed List Function that Creates new list
"""
def trim_list(int_list):
    #Check if all values are equal
    first_iteration = True
    is_same = True
    for number in int_list:
        if is_same == True:
            if first_iteration == True:
                checker = number
                first_iteration = False
            else:
                is_same = checker == number
    #Edit the list
    if is_same == True:
        return int_list
    else:
        max_value = max(int_list)
        max_value_list = [value for value in int_list if (value == max_value)]
        max_occurence = len(max_value_list)
        excluding_list = [value for value in int_list if (value != max_value)]
        second_max_value = max(excluding_list)
        trimmed_list = []
        for value in int_list:
            if value == max_value:
                trimmed_list += [second_max_value]
            else: 
                trimmed_list += [value]
        print(trimmed_list)
            
trim_list([6, 7, 7, 7, 7, 7])   
"""

def trim_list(int_list): 
    #Check if all values are equal
    first_iteration = True
    is_same = True
    for number in int_list:
        if is_same == True:
            if first_iteration == True:
                checker = number
                first_iteration = False
            else:
                is_same = checker == number
    #Edit the list
    if is_same == True:
        return int_list
    else:
        max_value = max(int_list)
        max_value_list = [value for value in int_list if (value == max_value)]
        max_occurence = len(max_value_list)
        excluding_list = [value for value in int_list if (value != max_value)]
        second_max_value = max(excluding_list)
        for index in range(len(int_list)):
            if int_list[index] == max_value:
                int_list[index] = second_max_value
        return int_list

"""
def trim_list(int_list):
    #Check if all values are equal
    first_iteration = True
    is_same = True
    for number in int_list:
        if is_same == True:
            if first_iteration == True:
                checker = number
                first_iteration = False
            else:
                is_same = checker == number
    #Edit the list
    if is_same == True:
        return int_list
    else:
        max_value = max(int_list)
        max_value_list = [value for value in int_list if (value == max_value)]
        max_occurence = len(max_value_list)
        excluding_list = [value for value in int_list if (value != max_value)]
        second_max_value = max(excluding_list)
        for index in range(len(int_list)):
            if int_list[index] == max_value:
                int_list[index] = second_max_value
        return int_list
"""

values = [1, 2, 3, 4, 4, 3, 2, 1]
trim_list(values)
print(values)