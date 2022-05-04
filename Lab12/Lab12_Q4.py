
def no_negatives(numbers):
    if len(numbers) == 0:
        return True
    if numbers[0] < 0:
        return False
    else:
        return no_negatives(numbers[1:])
        
print(no_negatives([2, -4]))