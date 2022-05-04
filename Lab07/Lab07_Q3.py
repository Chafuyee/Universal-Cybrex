
def bubble_sort_descending(data):

    for iteration in range(len(data)-1):
        inner_swaps = 0
        for index in range(len(data)-1, 0, -1):
            if data[index] > data[index-1]:
                data[index-1], data[index] = data[index], data[index-1]
                inner_swaps +=1
        if inner_swaps == 0:
            return data
            



d = [2, 16, 7, 11, 1]
bubble_sort_descending(d)
print(d)