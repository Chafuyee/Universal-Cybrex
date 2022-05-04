
input_sentence = input("Enter a sentence: ")
vowel_count = 0
consonant_count = 0
vowel_str = "aeiouAEIOU"
consonant_str= "bcdfghjklmnpqrstvwxyzBCDFGHIJKLMNPQRSTVWXYZ"
for letter in input_sentence:
    if letter in vowel_str:
        vowel_count += 1
    elif letter in consonant_str:
        consonant_count += 1
print("The number of vowel letters = " + str(vowel_count))
print("The number of consonant letters = " + str(consonant_count))
