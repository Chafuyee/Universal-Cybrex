"""
A valid time (in 24-hour notation) can be expressed where the hours are between 0 and 23 (inclusive) and the minutes are between 0 and 59 (inclusive).

The valid_time() function takes two integers as input.  The first integer represents the hours, and the second integer represents the minutes.  The function should return True if those values represent a valid time, and False otherwise.

Several definitions of this function have been defined (one of these definitions is correct, and the other definitions contain some type of bug).  Define a set of tests such that the correct function definition passes all of your tests, and all of the incorrect function definitions fail at least one of your tests.  A test consists of a print() statement that displays the output from calling the function with some input, along with the expected output. 

"""

def valid_time():
    return "test"

#Hours must be between 0 and 23 inclusive
#Minutes must be between 0 and 59 inclusive
#Tests
print(valid_time(11, 11)) #True
print(valid_time(0, 0)) #True
print(valid_time(23, 59)) #True
print(valid_time(24, 59)) #False
print(valid_time(23, 60)) #False
print(valid_time(24, 60)) #False
print(valid_time(-1, -10)) #False