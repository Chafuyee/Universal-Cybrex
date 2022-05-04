
from curses.ascii import isalpha
from fileinput import filename

"""
def decrypt_file(filename):
    source_file = open(filename, "r")
    encrypted_list = source_file.readlines()
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #Remove the \n from each string
    for index in range(len(encrypted_list)):
        if encrypted_list[index][-1] == "\n":
            encrypted_list[index] = encrypted_list[index][:-1]
    for index in range(len(encrypted_list)):
        for iteration in range(len(encrypted_list[index])):
            if encrypted_list[index][iteration] in alphabet_list_upper:
                position = alphabet_list_upper.index(encrypted_list[index][iteration])
                encrypted_list = alphabet_list_upper[position-1]
            elif encrypted_list[index][iteration] in alphabet_list:
                position = alphabet_list.index(encrypted_list[index][iteration])
                encrypted_list[index][iteration] = alphabet_list[position-1]
    return encrypted_list
"""
"""
def decrypt_file(filename):
    source_file = open(filename, "r")
    encrypted_list = source_file.readlines()
    alphabet_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index in range(len(encrypted_list)):
        if encrypted_list[index][-1] == "\n":
            encrypted_list[index] = encrypted_list[index][:-1]
    for index in range(len(encrypted_list)):
        sentence = encrypted_list[index]
        encrypted_words = sentence.split(" ")
        for iteration in range(len(encrypted_words)):
            if encrypted_words[iteration].isalpha() == True:
                if encrypted_words[iteration] == "a":
                    encrypted_words[iteration] = "z"
                elif encrypted_words[iteration] == "A":
                    encrypted_words[iteration] = "Z"
                else:
                    position = alphabet_str.find(encrypted_words[iteration])
                    encrypted_words[iteration] = alphabet_str[position-1]
        print(encrypted_words)
"""
"""
def decrypt_file(filename):
    source_file = open(filename, "r")
    encrypted_list = source_file.readlines()
    alphabet_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output_list = []
    for index in range(len(encrypted_list)):
        if encrypted_list[index][-1] == "\n":
            encrypted_list[index] = encrypted_list[index][:-1]
    for index in range(len(encrypted_list)):
        sentence = encrypted_list[index]
        encrypted_words = sentence.split(" ")
        for iteration in range(len(encrypted_words)):
            for x in range(len(encrypted_words[iteration])):
                if encrypted_words[iteration][x].isalpha() == True:
                    temp_str = ""
                    if encrypted_words[iteration][x] == "z":
                        temp_str += "a"
                    elif encrypted_words[iteration][x] == "Z":
                        temp_str += "A"
                    else:
                        position = alphabet_str.find(encrypted_words[iteration])
                        temp_str += alphabet_str[position+1]
                print(temp_str)
""" 
        
def decrypt_file(filename):
    source_file = open(filename, "r")
    encrypted_list = source_file.readlines()
    alphabet_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index in range(len(encrypted_list)):
        if encrypted_list[index][-1] == "\n":
            encrypted_list[index] = encrypted_list[index][:-1]
    for index in range(len(encrypted_list)):
        output_list = []
        sentence = encrypted_list[index]
        words_list = sentence.split(" ")
        for word in words_list:
            temp_str = ""
            for letter in word:
                if letter == "z":
                    temp_str += "a"
                elif letter == "Z":
                    temp_str += "A"
                elif (letter.isalpha() == True):
                    position = alphabet_str.find(letter)
                    temp_str += alphabet_str[position+1]
                else:
                    temp_str += letter
            output_list += [temp_str]
        print(" ".join(output_list))



        

