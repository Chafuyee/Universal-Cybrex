"""
Fix the faulty function below named get_index_of_largest(numbers) that takes a list of integers as a parameter and returns the index position of the largest element in the list.  If more than one element is equal largest, the function should return the index of the first occurrence of the value (i.e. the smallest index).  The function should return -1 if the list is an empty list.

A faulty solution has been provided below. Identify the faults and submit a corrected version of this code.

"""

def get_index_of_largest(numbers):
    if len(numbers) == 0:
        return -1
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i
    return max_index
#The Greater than sign made it include equal numbers 

print(get_index_of_largest([1, 4, 16, 15, 16]))





