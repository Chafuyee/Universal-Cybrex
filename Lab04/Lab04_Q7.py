
def generate_initials(string):
    middle_space = string.find(" ")
    if middle_space == -1:
        raise ValueError("ERROR: Invalid name!")
    else:
        word_list = string.split(" ")
        initials = ""
        for word in word_list:
            initials += word[0]
        return initials

print(generate_initials('Apple Banana Cherry'))