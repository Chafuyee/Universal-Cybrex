"""
Fix the faulty function below named remove_all_evens(numbers) which takes a list of numbers as a parameter. The function should remove all even numbers in the list, so that if the list is printed after calling the function, no even values should be displayed.  Note that the function makes changes in place (i.e. it changes the list that is passed to the function rather than creating a new list).  As a reminder, the pop() function removes and returns the item at the specified index in the list.

"""

def remove_all_evens(numbers):
    for index in range(len(numbers)-1, 0, -1):
        num = numbers[index]
        if (num % 2 == 0):
            numbers.pop(index)
    if len(numbers) == 1:
        if numbers[0] == 0:
            numbers.pop(0)


 	

numbers = [0, 2, 0]
remove_all_evens(numbers)
print(numbers)















