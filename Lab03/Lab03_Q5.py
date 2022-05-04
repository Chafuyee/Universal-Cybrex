"""
def is_taller(person1, person2)

takes the heights of two people as input: both heights are expressed as tuples as defined above.  The function should return a boolean: True if Person 1 is taller than Person 2 and False otherwise.

Several definitions of this function have been defined (one of these definitions is correct, and the other definitions contain some type of bug).

Define a set of tests such that the correct function definition passes all of your tests, and all of the incorrect function definitions fail at least one of your tests.  A test consists of a print() statement that displays the output from calling the function with some input, along with the expected output.  

"""

def is_taller(person1, person2):
    return "test"

#Should return True if person 1 is taller than person 2
#Tests
print(is_taller((6, 3), (4, 2))) #True
print(is_taller((6, 3), (6, 3))) #False
print(is_taller((6, 3), (6, 4))) #False
print(is_taller((5, 4), (7, 2))) #False


