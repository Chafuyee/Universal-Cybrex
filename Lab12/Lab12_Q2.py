


def get_sum_squares(numbers):
    if len(numbers) == 1:
        return numbers[0] ** 2
    elif len(numbers) == 0:
        return 0
    else:
        return (numbers[0] ** 2) + get_sum_squares(numbers[1:])

numbers = []
print(get_sum_squares(numbers))