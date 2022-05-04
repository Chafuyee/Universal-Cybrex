
def get_letter_counts(string):
    letter_dict = {}
    string = string.lower()
    for letter in string:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    frequency_dict = {}
    for key in letter_dict:
        if letter_dict[key] not in frequency_dict:
            frequency_dict[letter_dict[key]] = [key]
        else:
            frequency_dict[letter_dict[key]] += [key]
    for key in frequency_dict:
        frequency_dict[key] = sorted(frequency_dict[key])
    return frequency_dict

get_letter_counts("apple")

"""
def get_letter_counts(string):
    frequency_dict = {string.count(letter):letter for letter in string}
    print(frequency_dict)
        frequency_dict = {letter_dict[key]:key for key in letter_dict}


get_letter_counts("Apple")
"""