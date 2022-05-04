
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


one_letter_difference("hello", "world")
