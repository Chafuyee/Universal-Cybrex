
def find_longest_words(word_list):
    longest_list = []
    longest_length = 0
    for index in range(len(word_list)):
        if len(word_list[index]) > longest_length:
            longest_length = len(word_list[index])
    for index in range(len(word_list)):
        if len(word_list[index]) == longest_length:
            longest_length += [index]
    return longest_list



