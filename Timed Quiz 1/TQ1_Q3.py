
def get_last_letter_dictionary(sentence):
    lower_sentence = sentence.lower()
    word_list = lower_sentence.split(" ")
    unique_list = []
    unique_dict = {}
    for word in word_list:
        if word not in unique_list:
            unique_list += [word]
    for word in unique_list:
            if word[-1] not in unique_dict:
                unique_dict[word[-1]] = [word]
            else:
                unique_dict[word[-1]] += [word]
  
    return unique_dict


sentence = "Hello Hello World"
abc_dictionary = get_last_letter_dictionary(sentence)
for key in sorted(abc_dictionary.keys()):
	print(key, ' '.join(sorted(abc_dictionary[key])))
