
def get_word_list(filename, length):
    input_file = open(filename, "r")
    input_str = input_file.read()
    sentence_list = input_str.split("\n")
    words_list = []
    exclusive_list = []
    for sentence in sentence_list:
        words_list += sentence.split(" ")
    for word in words_list:
        if ((word != '') and (word not in exclusive_list)):
            if len(word) == length:
                exclusive_list += [word]

    for index in range(len(exclusive_list)):
        exclusive_list[index] = exclusive_list[index].lower()
    exclusive_list = sorted(exclusive_list)

    return exclusive_list

        
