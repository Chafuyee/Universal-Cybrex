import random

def bubble_sort_fast(a_list): 
    comp=0
    swap=0
    for pass_num in range(len(a_list)-1, 0, -1):
        swaps=False
        for i in range(0, pass_num):
            comp+=1
            if a_list[i] > a_list[i+1]:
                swap+=1
                swaps=True
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        if swaps==False:
            output_tuple = (len(a_list), comp, swap)
            break
        output_tuple = (len(a_list), comp, swap)            
    return output_tuple


#Normal Bubble Sort: Length: 26 Comparisons: 325 Swaps: 169
d2 = [54, 91, 11, 63, 19, 69, 40, 56, 77, 97, 54, 69, 52, 81, 53, 97, 42, 1, 5, 82, 56, 66, 67, 62, 22, 43, 58, 11, 52, 44, 70, 17, 14, 43, 44, 83, 99, 29, 30, 57, 92]
result2 = bubble_sort_fast(d2)
print('Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result2[0], result2[1], result2[2]))

"""
random.seed(30)
numbers = [random.randint(1, 50) for index in range(50)]
#Normal Bubble Sort: Length: 50 Comparisons: 1225 Swaps: 567
d2 = numbers.copy()
result2 = bubble_sort_fast(d2)
print('Fast Bubble Sort: Length: {} Comparisons: {} Swaps: {}'.format(result2[0], result2[1], result2[2]))
""" 
"""
def bubble_sort_fast(data):
    num_elements = len(data)
    num_comparisons = 0
    num_swaps = 0
    temp_length = len(data)-1
    for iteration in range(len(data)-1):
        num_comparisons += temp_length
        inner_swaps = 0
        for index in range(len(data)-1, 0, -1):
            if data[index] < data[index-1]:
                data[index-1], data[index] = data[index], data[index-1]
                num_swaps +=1
                inner_swaps +=1
        temp_length -= 1

        if inner_swaps == 0:
            return (num_elements, num_comparisons, num_swaps)
    return (num_elements, num_comparisons, num_swaps)
"""

""""
def bubble_sort_fast(data):
    num_elements = len(data)
    num_comparisons = 0
    num_swaps = 0
    for num_iterations in range(num_elements-1):
        times_in_order = 0
        for index in range(num_elements-1, num_iterations, -1):
            num_comparisons +=1
            if data[index] < data[index-1]:
                times_in_order = 0
                data[index-1], data[index] = data[index], data[index-1]
                num_swaps +=1
            else:
                times_in_order += 1
        
            if times_in_order == num_elements - num_iterations:
                return (num_elements, num_comparisons, num_swaps)
    return (num_elements, num_comparisons, num_swaps)
"""
"""
def bubble_sort_fast(data):
    num_elements = len(data)
    num_comparisons = 0
    num_swaps = 0
    temp_length = len(data)-1
    inner_swaps = 0
    for num_iterations in range(len(data)-1):
        inner_comparisons = temp_length - inner_swaps
        num_comparisons += inner_comparisons
        inner_swaps = 0
        inner_comparisons = 0
        for index in range(len(data)-1, num_iterations, -1):
            if data[index] < data[index-1]:
                data[index-1], data[index] = data[index], data[index-1]
                num_swaps +=1
                inner_swaps +=1
        temp_length -= 1

        if inner_swaps == 0:
            return (num_elements, num_comparisons, num_swaps)
    return (num_elements, num_comparisons, num_swaps)
"""