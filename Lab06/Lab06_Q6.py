
def shifting(data, index):
    value_to_insert = data[index]
    for iteration in range(index, 0, -1):
        if value_to_insert < data[iteration-1]:
            data[iteration] = data[iteration-1]

numbers = [20, 27, 69, 25, 15, 41]
shifting(numbers, 3)
print(numbers)