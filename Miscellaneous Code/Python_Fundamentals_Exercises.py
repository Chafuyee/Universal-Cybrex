import math

#Python Fundamentals Exercises - Q1
def find_radius():
    area = float(input("Enter the area of a circle: "))
    radius = math.sqrt(area / math.pi)
    print(round(radius, 1))

#Python Fundamentals Exercises - Q2
def input_fn():
    input_str = input("Enter a sentence: ")
    print("The result is " + input_str[0] + input_str[-1])

#Python Fundamentals Exercises - Q3
def program():
    x = float(input("Enter a Number: "))
    series_sum = 1 + (1/2) + (1/3) + (1/4) + (1/x)
    print(round(series_sum, 1))

#Python Fundamentals Exercises - Q4
def get_hypotenuse(side1 = 3, side2 = 4):
    hypotenuse = math.sqrt((side1 **2) + (side2 **2))
    print(round(hypotenuse,1))
 
def is_palindrome():
    word = "radar"
    a_list = [letter for letter in word]
    a_list.reverse()
    new_str = ""
    for element in a_list:
        new_str += element
    if new_str == word:
        print("True")
    else:
        print("False")

#Python Fundamentals Exercises - Q6
def get_index_of_smallest(numbers):
    if len(numbers) <= 0:
        result = -1
        print(result)
    else:
        smallest_value = min(numbers)
        position = numbers.index(smallest_value)
        print(position)

#Python Fundamentals Exercises - Q7
def create_string_lengths_dictionary():
    fruit_list = ["avocado", "apple"]
    length_list = [len(element) for element in fruit_list]
    fruit_dict = {}
    for index in range(len(fruit_list)):
        fruit_dict[fruit_list[index]] = length_list[index]
    print(fruit_dict)

#Python Fundamentals Exercises - Q8
content = input_file.readlines()
for line in content:
    words_list = line.split(" ")
    letter_list = [word[0] for word in words_list]
    output_str = letter_list.join()
    print(output_str)














