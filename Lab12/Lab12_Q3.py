
def sum_evens_between(start, end):
    if start == end:
        if start%2 == 0:
            return start
        else:
            return 0
    else:
        if start%2 != 0:
            value = 0 
        else: 
            value = start
        return value + sum_evens_between(start+1, end)
        
print(sum_evens_between(1, 3))