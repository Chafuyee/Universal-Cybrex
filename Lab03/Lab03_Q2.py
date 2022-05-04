"""
A person is eligible for a discount if they are a child (between 0 and 12 years of age, inclusive) or if they have a membership card.  The following function:

def gets_discount(age, card)

takes two inputs: a person's age and a boolean indicating if they have a membership card.  It should return a boolean: True if they are eligible for a discount, and False otherwise.  If the value of age is less than zero, then the data about the person must be invalid and the function should return False.

Several definitions of this function have been defined (one of these definitions is correct, and the other definitions contain some type of bug).

Define a set of tests such that the correct function definition passes all of your tests, and all of the incorrect function definitions fail at least one of your tests.  A test consists of a print() statement that displays the output from calling the function with some input, along with the expected output.
  
"""

def gets_discount(age, card):
    return "test"

#Age variable must be greater than zero; members are only eligible for discounts if they are betweeen 0 and 12 (inclusive) or they have a membership card
#Tests
print(gets_discount(0, False)) #True
print(gets_discount(6, False)) #True
print(gets_discount(12, False)) #True
print(gets_discount(-1, True)) #False
print(gets_discount(55, True)) #True
print(gets_discount(35, False)) #False