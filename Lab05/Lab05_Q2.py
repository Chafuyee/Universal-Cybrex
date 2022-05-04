def rate(n):
    primitives = 4
    i = n
    while i > 1:
        j = 0
        i //= 2
        primitives += 3
    print ("Number of operations:", primitives)