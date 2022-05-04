def rate(n):
    i = 0 #1 operations
    total = 0 #1 operations
    while i < n: #n+1 operations
        total += i #n operations
        i += 2 #n operations
    return total #1 operation

# 1 + 1 + (n/2)*3 + 1 + 1
# f(n) = (n/2)*3 + 4 time complexity = O(n)
