
def bubble_single_pass(data, index):

    for iteration in range(index):
        if data[iteration+1] < data[iteration]:
            data[iteration], data[iteration+1] = data[iteration+1], data[iteration]
            
def my_bubble_sort(data): 
    for num_steps in range(len(data) - 1, 0, -1):
        bubble_single_pass(data, num_steps)


numbers = [76, 53, 48, 24, 12]
my_bubble_sort(numbers)
print(numbers)