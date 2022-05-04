
def linear_search_sorted(baby_names, target_name):
    num_elements = len(baby_names)
    num_comparisons = 0
    for index in range(len(baby_names)):
        num_comparisons += 1
        if baby_names[index] == target_name:
            return (True, num_elements, num_comparisons)
        if (baby_names[index][0] == target_name[0]) and (baby_names[index+1][0] != target_name[0]):
            return (False, num_elements, num_comparisons)

    return (False, num_elements, num_comparisons)


result = linear_search_sorted(['Abby', 'Bella', 'Charlotte', 'Daisy', 'Ella', 'Faith', 'Grace', 'Hannah', 'Isabella', 'Jade', 'Kate', 'Lily', 'Maddison', 'Natalie', 'Olivia', 'Phoebe', 'Queen', 'Rebecca', 'Samantha'], 'Ethan')
print('Found: {} Length: {} Comparisons: {}'.format(result[0], result[1], result[2]))