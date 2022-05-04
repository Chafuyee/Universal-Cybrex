"""
def get_palindromes(word_list):
    palindrome_list = []
    for word in word_list:
        a_list = [letter for letter in word]
        a_list.reverse()
        new_str = ""
        for element in a_list:
            new_str += element
        if new_str == word:
            palindrome_list += (word, len(word))
    return palindrome_list
"""

def get_palindromes(word_list):
    palindrome_list = [(word, len(word)) for word in word_list if (word[::-1] == word)]
    return palindrome_list

words = ["noon", "bob", "ann"]
result = get_palindromes(words)
print(result)