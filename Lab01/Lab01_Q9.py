
def create_surnames_dictionary(string_list):
    surname_dict = {}
    for name in string_list:
        centre_position = name.find(" ")
        surname_letter = name[centre_position+1]
        first_name = name[:centre_position]
        if surname_letter not in surname_dict:
            surname_dict[surname_letter] = [name]
        else:
            surname_dict[surname_letter] += [name]
    return surname_dict
