

def print_sum_between(num_list, index_start, index_end):
    sum_value = 0
    temp_list = []
    for index in range(index_start, index_end+1):
        try:
            sum_value += num_list[index]
        except IndexError:
            print(str(index) + " is an invalid index")
    print("Sum =", sum_value)