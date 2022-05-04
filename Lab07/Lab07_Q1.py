

def bubble_sort(data):
    length = len(data)
    comparisons = 0
    swaps = 0
    for num_iterations in range(len(data) - 1, 0, -1):
        for i in range(0, num_iterations):
            comparisons += 1
            if data[i] > data[i+1]:
                swaps += 1
                data[i], data[i+1] = data[i+1], data[i]
    return (length, comparisons, swaps)


numbers = [12, 78, 81, 99, 91]
result = bubble_sort(numbers)
print('Length: {} Comparisons: {} Swaps: {}'.format(result[0], result[1], result[2]))