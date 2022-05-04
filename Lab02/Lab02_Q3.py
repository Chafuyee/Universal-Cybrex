def read_word_list(filename):
    input_file = open(filename, "r")
    word_list = input_file.readlines()
    for index in range(len(word_list)):
        if word_list[index][-1] == "\n":
            word_list[index] = word_list[index][:-1]
    return word_list


def one_letter_difference(word1, word2):
    similarity_count = 0
    same_sum = len(word1)
    for index in range(len(word1)):
        if word1[index] == word2[index]:
            similarity_count += 1
    if (similarity_count == (same_sum -1)):
        return True
    else:
        return False


def get_all_valid_responses(current_word, unused_list):
    valid_words = []
    for word in unused_list:
        valid_condition = one_letter_difference(current_word, word)
        if valid_condition == True:
            valid_words += [word]
    return valid_words

