import math

#Question One
def find_radius():
    area = float(input("Enter the area of a circle: "))
    radius = math.sqrt(area / math.pi)
    print(round(radius, 1))

#Question Two
def last_letter():
    input_source = input("Enter a sentence: ")
    output_str = input_source[0] + input_source[-1]
    print("The result is ", output_str, ".", sep="")

#Question Three 
def series_program():
    input_value = int(input("Enter an integer: "))
    starting_x = 1
    for index in range(2, input_value+1):
        starting_x += (1/index)
    output_value = starting_x
    print("The sum is", round(output_value, 1))

#Question Four
def get_hypotenuse(side1, side2):
    hypotenuse = math.sqrt((side1 **2) + (side2 **2))
    hypotenuse = round(hypotenuse, 1)
    return hypotenuse
    
#Question Five
def is_palindrome(word):
    a_list = [letter for letter in word]
    a_list.reverse()
    new_str = ""
    for element in a_list:
        new_str += element
    if new_str != word:
        return False
    else:
        return True

#Question Six
def get_index_of_smallest(numbers):
    if len(numbers) <= 0:
        result = -1
        return (result)
    else:
        smallest_value = min(numbers)
        position = numbers.index(smallest_value)
        return (position)

#Question Seven
def create_string_lengths_dictionary(fruit_list):
    length_list = [len(element) for element in fruit_list]
    fruit_dict = {}
    for index in range(len(fruit_list)):
        fruit_dict[fruit_list[index]] = length_list[index]
    return fruit_dict