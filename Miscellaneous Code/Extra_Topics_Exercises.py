#Formatting Strings 1
def string_formatting():
    name = "daniel"
    a_list = ["hello", "there", "theo"]
    print("{} is cool".format(name))
    print("{} {} {} is cool".format("I", "think", name))
    print("{} what are you doing today".format(a_list))
    print("The average is {:.2f}".format(78.235876))
    print("My name is {0} and I am {1} years old".format("john", 8))

#Formatting Strings 2
def f_strings():
    name = "John"
    age = 18
    print(f"My name is {name} and I am {age} years old!")

#String Padding & Alignment
def padding():
    print(" {:_^10}".format("test"))
    print(" {:_>10}".format("test"))
    print(" {:_<10}".format("test"))

#The Join Method
def join():
    a_list = ["A", "B", "C", "D", "E"]
    print("--".join(a_list))

#Extra Topic Exercises - Q1
def print_names_and_weights(names, weights):
    print("{:10}".format("Name") + "{:<6}".format("Weight"))
    print("-" * 16)
    for index in range(len(names)):
        print("{:10}".format(names[index]) + "{:<6}".format(weights[index]))
"""
names = ["Helen", "Bill", "Michael"]
weights = [76.27, 54.61, 67.92]
print_names_and_weights(names, weights)
""" 

#Ternary Operators
def ternary_operators():
    intelligence_input = int(input("Enter IQ: "))
    print("Zach's level of IQ" if intelligence_input > 100 else "Daniel's level of IQ")

#Extra Topic Exercises - Q2
def get_string(words):
    output_str = ".".join(words)
    return output_str   
"""
a_list = ["coderunner", "auckland", "ac", "nz"]
get_string(a_list)
"""

#Default Argument Values
def my_default_value_print(some_object = "Zach"):
    print(some_object)
"""
my_default_value_print("Hello Loser")
my_default_value_print()
my_default_value_print(7)
"""

#Rules
def info(value, spacing = 15, collapse = 1):
    print(value, spacing, collapse)
"""
info(5)
info(5, 12)
info(5, collapse = 0)
info(collapse = 2)
info(collapse = 5, 5) #Error
"""

#List Comprehension 1
def list_comprehension():
    #a_list = [expression for variable in sequence]
    number_list = [2, 3, 4, 5]
    fresh_fruit = ["   banana", "  apple  "]
    a_list = [x for x in range(0, 5)]
    a_list2 = [letter for letter in "Ann"]
    a_list3 = [fruit.strip() for fruit in fresh_fruit]
    a_list4 = [5 * num for num in number_list]
    a_list5 = [num * 2 for num in range(1, 5)]
    print(a_list)
    print(a_list2)
    print(a_list3)
    print(a_list4)
    print(a_list5)

#List Comprehension 2
def list_comprehension2():
    values = ["hello", [1,2], (3, 5)]
    values2 = [("a", 1), ("b", 2), ("c", 7)]
    a_list1 = [len(n) for n in values]
    a_list2 = [ n * 2 for (s, n) in values2]
    print(a_list1)
    print(a_list2)

#List Comprehension 3
def list_comprehension3():
    def square(a):
        return a * a

    a_list = [(6, 3), (1, 7), (5, 5)]
    result_list = [square(x) for (x, y) in a_list]
    print(result_list)

#List Comprehension 4
def list_comprehension4():
    numbers = [2, 4, 6]
    result1 = [{num: num ** 2} for num in numbers]
    result2 = [[num, num ** 2] for num in numbers]
    print(result1)
    print(result2)

#List Comprehension 5
def list_comprehension5():
    result = [num for num in range(0, 10) if num % 2 == 0]
    #[expression for variable in sequence if condition]
    print(result)
    
#Exta Topic Exercises - Q3
def modify_list(numbers, value):
    numbers.append(value)
    print(numbers)
"""
numbers = [1, 2, 3]
value = 4
modify_list(numbers, value)
"""

#Extra Topic Exercises - Q4
def get_appended_list(numbers, value):
    source_list = []
    for number in numbers:
        source_list += [number]
    target_list = numbers
    target_list += [value]
    print(source_list)
    print(target_list)
"""
numbers = [1, 2, 3]
value = 4
get_appended_list(numbers, value)
"""

#Extra Topic Exercises - Q5
def generate_odd_numbers(max_value):
    a_list = [x for x in range(1, max_value, 2)]
    print(a_list)

max_value = 10
generate_odd_numbers(max_value)


#Extra Topic Exercises - Q6
def get_vowels(word):
    vowels = "aeiouAEIOU"
    target_list = [letter for letter in word]
    return target_list


    








    
