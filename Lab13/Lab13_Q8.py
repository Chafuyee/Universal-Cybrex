

def get_sum(a_node):
    if a_node.get_data() == None:
        return 
    else:
        return a_node.get_data() + (get_sum(a_node.get_next()))