def rate(n):
    i = n #1 operation
    total = 0 #1 operation
    while i > 0: #n+1 operations
        j = 0 #n operations
        while j < n: #n+1 operations
            total += j  #n operations
            j += 1 #n operations
        i -= 1 #n operations
    return total #1 operation

# 1 + 1 + ((n+1) + n)((n+1)  + n + n) + n + 1
# 3 + ((n^2 + n + n + 1) + n^2 + n + n^2 + n + n^2 + n + n^2 + n^2) + n + 1