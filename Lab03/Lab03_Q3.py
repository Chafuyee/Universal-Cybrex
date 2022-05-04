"""
def get_max_odd(numbers)

returns the largest odd number in the input list, numbers.  If there are no odd numbers in the list, or if the list is empty, then the function should return 0.

Several definitions of this function have been defined (one of these definitions is correct, and the other definitions contain some type of bug).

Define a set of tests such that the correct function definition passes all of your tests, and all of the incorrect function definitions fail at least one of your tests.  A test consists of a print() statement that displays the output from calling the function with some input, along with the expected output.  

"""

def get_max_odd(numbers):
    return "test"

#Returns 0 when there are no odd numbers in list or list is empty
#Tests
print(get_max_odd([1, 2, 3, 4])) #3
print(get_max_odd([])) #0
print(get_max_odd([2, 4, 6, 8])) #0
print(get_max_odd([-1, -2, -3, -4])) #-3
print(get_max_odd([1.6, 10.3, 20.5])) #0
print(get_max_odd([3])) #3

