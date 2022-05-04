

def read_word_list(filename):
    input_file = open(filename, "r")
    word_list = input_file.readlines()
    for index in range(len(word_list)):
        if word_list[index][-1] == "\n":
            word_list[index] = word_list[index][:-1]
    return word_list


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


def get_all_valid_responses(current_word, unused_list):
    valid_list = []
    for word in unused_list:
        valid_condition = one_letter_difference(current_word, word)
        if valid_condition == True:
            valid_list += [word]
    return valid_list


def get_computer_word(current_word, unused_list):
    valid_list = get_all_valid_responses(current_word, unused_list)
    computer_output = valid_list[0]
    return computer_output


def get_user_word(current_word, word_list):
    valid_response = False
    while valid_response == False:
        player_input = input("Enter word: ")
        if current_word == None:
            if player_input in word_list:
                valid_response = True
            elif player_input == "?":
                valid_response = False
        else:
            valid_list = get_all_valid_responses(current_word, word_list)
            if player_input in valid_list:
                valid_response = True
            elif player_input == "?":
                valid_response = True

    return player_input


def initialise_game(filename):
    full_list = read_word_list(filename)
    first_turn = True
    if first_turn == True:
        user_input = get_user_word(None, full_list)
        full_list.remove(user_input)
        return (user_input, full_list)


def play_one_turn(current_word, full_list, computer_turn):
    turn_list = get_all_valid_responses(current_word, full_list)
    if len(turn_list) == 0:
        if computer_turn == True:
            print("Game over! You win!")
        else:
            print("Game over! You lose!")
        return None
    else:
        if computer_turn == True:
            selected_word = get_computer_word(current_word, turn_list)
            print("Computer: " + selected_word)
            full_list.remove(selected_word)
            return selected_word
        else:
            loop_condition = True
            while loop_condition == True:
                user_input = get_user_word(current_word, turn_list)
                if user_input == "?":
                    print(turn_list)
                elif user_input in turn_list:
                    full_list.remove(user_input)
                    return user_input


def main(filename):
    computer_turn = True
    word, words = initialise_game(filename)
    
    while word is not None:
        word = play_one_turn(word, words, computer_turn)
        computer_turn = not computer_turn

    print('Thanks for playing!')

