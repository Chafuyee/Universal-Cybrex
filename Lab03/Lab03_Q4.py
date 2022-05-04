"""
def position_of_shortest_word(words)

takes one input, a list of words, and it returns the index position in that list of the shortest word.  If there is more than one word with length equal to the shortest length, then the function should return the index position of the first word (i.e. the one with the smallest index position).  If the list is empty, the function should return -1. 

Several definitions of this function have been defined (one of these definitions is correct, and the other definitions contain some type of bug).

Define a set of tests such that the correct function definition passes all of your tests, and all of the incorrect function definitions fail at least one of your tests.  A test consists of a print() statement that displays the output from calling the function with some input, along with the expected output.

""" 

def position_of_shortest_words(words):
    return "test"

#Returns index of shortest word in list
#If the list is empty return -1
#If there are more than one word with shortest length then return the index of the fist word in order
#Tests
print(position_of_shortest_words([])) #-1
print(position_of_shortest_words(["apple"])) #0
print(position_of_shortest_words(["aaa", "aa", "a"])) #2
print(position_of_shortest_words(["aaa", "a", "aa", "a"])) #1

