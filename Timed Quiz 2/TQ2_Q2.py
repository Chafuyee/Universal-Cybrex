

def get_leaves_eaten(branch_length, distance_between_rests, distance_between_leaves):
    branch_list = [value for value in range(branch_length+1)]
    rest_list = [value for value in range(0, branch_length+1, distance_between_rests)]
    leaf_list = [value for value in range(0, branch_length+1, distance_between_leaves)]
    leaves_eaten_list = [leaf for leaf in leaf_list if (leaf in rest_list)]
    return len(leaves_eaten_list)

print('Leaves eaten =', get_leaves_eaten(12, 6, 4))