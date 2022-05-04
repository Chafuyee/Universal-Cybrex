
def bubble_single_pass(data, index):

    for iteration in range(index):
        if data[iteration+1] < data[iteration]:
            data[iteration], data[iteration+1] = data[iteration+1], data[iteration]
            