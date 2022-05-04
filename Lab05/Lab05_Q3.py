def rate(n):
    primitives = 0
    i = n
    while i > 0:
        j = 0
        primitives += 2
        while j < n:
            total += j 
            j += 2
            primitives += 3
        i -= 1
        primitives += 1
    print("Number of operations:", primitives)