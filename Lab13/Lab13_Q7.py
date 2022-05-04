

def reverse_chain_of_nodes(a_node):
    current = a_node
    node_str = ""
    while current != None:
        word = current.get_data()
        new_word = word[-1::-1]
        current.set_data(new_word)
        current = current.get_next()