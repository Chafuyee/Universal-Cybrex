

def get_total_word_scores(node_chain):
    count = 0
    node_str = ""
    current = node_chain
    while current != None:
        node_str += current.get_data()
        current = current.get_next()
    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in node_str:
        if letter in alpha_list:
            value = alpha_list.index(letter)
            count += value
    return count
