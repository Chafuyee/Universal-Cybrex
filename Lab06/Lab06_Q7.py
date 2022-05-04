def shifting(data, index):
    value_to_insert = data[index]
    for iteration in range(index, 0, -1):
        if value_to_insert < data[iteration-1]:
            data[iteration] = data[iteration-1]

def insertion_single_pass(data, index):
    value_to_insert = data[index]
    shifting(data, index)
    inserted = False
    for iteration in range(index):
        if value_to_insert < data[iteration]:
            if inserted == False:
                data[iteration] = value_to_insert
                inserted = True


numbers = [20, 27, 69, 10, 15, 41]
insertion_single_pass(numbers, 3)
print(numbers)