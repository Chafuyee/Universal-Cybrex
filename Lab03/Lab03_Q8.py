"""
Fix the faulty function below named average_positives(values) that takes a list of values as a parameter and returns the average of the values in the list that are greater than 0.  If the list contains no numbers greater than 0, then the function should return -1.

A faulty solution has been provided below (note, although this function could be written more simply, your goal is to identify and fix the bug that exists in the current definition). Identify the fault and submit a corrected version of this code.
"""

def average_positives(values):
    positives = []
    total = 0
    for value in values:
        if value > 0:
            total = total + value
            positives = positives.append(value)
    if len(positives) == 0:
        return -1
    return total / len(positives) 

print(average_positives([1, 2, 3, 4, 5]))



