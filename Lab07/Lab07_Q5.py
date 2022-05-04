
def linear_search(baby_names, target_name):
    found = False
    num_elements = len(baby_names)
    num_comparisons = 0
    for name in baby_names:
        num_comparisons += 1
        if name == target_name:
            return (True, num_elements, num_comparisons)
    return (False, num_elements, num_comparisons)