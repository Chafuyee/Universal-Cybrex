
def print_between(start, end):
    num = start
    if num == end:
        print(num)
    else:
        print(num)
        print_between(start+1, end)

print_between(1, 5)