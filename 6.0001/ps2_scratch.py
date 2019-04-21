# secret_word = "apple"
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# #letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'l']
# correct_guesses = 0
# for guess in letters_guessed:
#     letter_occurance = secret_word.count(guess)
#     if letter_occurance >= 1:
#         print ("letter", guess, "found", letter_occurance, "times")
#         correct_guesses += letter_occurance
# if len(secret_word) <= correct_guesses:
#     print ("True")
# else: print ("False")

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 'l']
# guessed_word = ""
# for char in secret_word:
#     if char in letters_guessed:
#         guessed_word += char
#     else:
#         guessed_word += '_ '
# #return guessed_word
# #print (guessed_word)
# #print(get_guessed_word(secret_word, letters_guessed))

letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 'l']
import string
letters_available = ""
for char in string.ascii_lowercase:
    if char not in letters_guessed:
        letters_available += char
return letters_available
print (letters_available)
#print(get_guessed_word(secret_word, letters_guessed))