
def read_word_list(filename):
    input_file = open(filename, "r")
    word_list = input_file.readlines()
    for index in range(len(word_list)):
        if word_list[index][-1] == "\n":
            word_list[index] = word_list[index][:-1]
    return word_list
