
def censor_sentence(sentence, banned_list):
    sentence_list = sentence.split(" ")
    sentence_censored = ""
    for index in range(len(sentence_list)):
        if sentence_list[index] in banned_list:
            word_length = len(sentence_list[index])
            censor_count = "*" * word_length
            word = censor_count + " "
            sentence_censored += word
            print(sentence_censored)
        else:
            word = sentence_list[index] + " "
            sentence_censored += word
            print(sentence_censored)
    return sentence_censored

sentence = "the quick brown fox jumps over the lazy dog"
censored = censor_sentence(sentence, ["jumps", "dog"])
print(censored)