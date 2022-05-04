"""
Fix the faulty function below named increment(numbers) which takes a list of numbers as a parameter. The function should increment (i.e. increase) every element in the list by 1, so that if the list is printed after calling the function, all elements should be displayed as one larger than their original values. You can assume that the list is not empty and that each element is a valid number. 

"""
def increment(numbers):
    for number in numbers:
        number += 1

numbers = [1, 2]
increment(numbers)
print(numbers)














