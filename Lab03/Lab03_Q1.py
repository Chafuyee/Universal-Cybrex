"""
A valid exam score is a score that is between 0 and 100 inclusive.  The following function:

def valid_score(score)

takes one input, an exam score, and it returns a boolean: True if the score is valid and False otherwise. 

Several definitions of this function have been defined (one of these definitions is correct, and the other definitions contain some type of bug).

Define a set of tests such that the correct function definition passes all of your tests, and all of the incorrect function definitions fail at least one of your tests.  A test consists of a print() statement that displays the output from calling the function with some input, along with the expected output. 

"""
def valid_score(num):
    return 10

#Input must be greater than or equal to 0 and less then or equal to 100
#Tests
print(valid_score(20)) #True
print(valid_score(15.6)) #True
print(valid_score(-10)) #False
print(valid_score(120)) #False
print(valid_score(0)) #True
print(valid_score(100)) #True

