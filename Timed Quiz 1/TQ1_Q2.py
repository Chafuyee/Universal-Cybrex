filename = input("Enter a filename: ")
input_file = open(filename, "r")
lines_str = input_file.read()
lines_list = lines_str.split("\n")
for sentence in lines_list:
    word_list = sentence.split(" ")
    temp_str = ""
    for word in word_list:
        temp_str += word[-1]
    print(temp_str)


input_file.close()


filename = input("Enter a filename: ")
input_file = open(filename, "r")
lines_str = input_file.read()
lines_list = lines_str.split("\n")
for sentence in lines_list:
    word_list = sentence.split(" ")
    temp_str = ""
    for word in word_list:
        temp_str += word[-1]
    print(temp_str)


input_file.close()

filename = input("Enter a filename: ")
input_file = open(filename, "r")
lines_str = input_file.read()
lines_list = lines_str.split("\n")
for sentence in lines_list:
    word_list = sentence.split(" ")
    temp_str = ""
    for word in word_list:
        word += " "
    for word in word_list:
        temp_str += word[(word.find(" "))-1]
    print(temp_str)
