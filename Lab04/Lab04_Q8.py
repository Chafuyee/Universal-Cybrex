
def get_valid_month():
    valid_answer = False
    valid_list = [value for value in range(1, 13)]
    while valid_answer == False:
        try:
            user_input = int(input("Enter a valid month (1-12): "))
            if user_input not in valid_list:
                raise ValueError
            else:
                valid_answer = True
        except ValueError:
            valid_answer = False
            
    return user_input

month = get_valid_month()
print('Valid input:', month)





