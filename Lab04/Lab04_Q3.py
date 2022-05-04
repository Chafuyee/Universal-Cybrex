

def get_valid_sum(value_list):
    total_sum = 0
    for element in value_list:
        try:
            total_sum += element
        except TypeError:
            total_sum += 0
    return total_sum


print(get_valid_sum([-1, '-2', -3, '4']))

