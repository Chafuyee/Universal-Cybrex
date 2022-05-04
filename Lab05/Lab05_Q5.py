def rate(n):
    i = 1 #1 operation
    total = 0 #1 operation
    while i < n: #n+1 operations
        total += i #n operators
        i *= 2 # log(n)
    return total #1 operation

#1 + 1 + 3*log(n) + 1 + 1
#3*log(n) + 4 