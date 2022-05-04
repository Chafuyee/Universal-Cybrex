

def get_valid_sum(value_list):
    try:
        sum_value = 0
        for number in value_list:
            sum_value += number
        return sum_value
    except TypeError:
        return sum_value


print(get_valid_sum([1, 2, 3.5, 4]))