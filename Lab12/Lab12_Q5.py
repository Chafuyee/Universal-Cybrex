


def choose(n, m):

    if m == 0:
        return 1
    elif m == n:
        return 1
    else:
        return choose(n-1, m-1) + choose(n-1, m)

print(choose(4, 2))

"""
def choose(n, m):
    
    def calculate_fact(num):
        if num <= 0:
            return 1
        else: 
             return num * calculate_fact(num-1)

    n_fact = calculate_fact(n)
    m_fact = calculate_fact(m)
    nm_fact = calculate_fact(n-m)

    combinations = n_fact / (m_fact * nm_fact)
    return int(combinations)
"""