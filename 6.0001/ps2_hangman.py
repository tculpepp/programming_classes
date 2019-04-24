# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2_hangman_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    correct_guesses = 0
    for guess in letters_guessed:
      letter_occurance = secret_word.count(guess)
      if letter_occurance >= 1:
        correct_guesses += letter_occurance
    if len(secret_word) <= correct_guesses:
      return True
    else: return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for char in secret_word:
      if char in letters_guessed:
        guessed_word += char
      else:
        guessed_word += '_ '
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    letters_available = ""
    for char in string.ascii_lowercase:
      if char not in letters_guessed:
        letters_available += char
    return letters_available
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    number_guesses = 6
    letters_guessed = []
    warnings_remaing = 3
    guessed_word = ("_ " * len(secret_word))
    vowels = "aeiou"
    
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is", len(secret_word), "letters long.")
    print ("You have", warnings_remaing, "warnings left.")
    while number_guesses > 0:
        no_warnings = "You have no warnings left so you lose one guess:"
        used_letter_message = "Oops! You've already guessed that letter. "
        not_alpha_message = "Oops! That is not a valid letter. "
        warnings_left = "You now have " + str(warnings_remaing - 1) + " warnings left:"
        available_letters = get_available_letters(letters_guessed)
        print ("-------------")
        print ("You have", number_guesses, "guesses left.")
        print ("Available letters:", available_letters)
        new_guess = str.lower(input("Please guess a letter: "))
        if str.isalpha(new_guess) == True and new_guess in available_letters:
            letters_guessed.extend ([new_guess])
            if new_guess in secret_word:   
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                print ("Good guess:", guessed_word)
                if is_word_guessed(secret_word, letters_guessed) == True:
                    won = True
                    break
            else:
              if new_guess in vowels:
                number_guesses -= 2
              else:
                number_guesses -= 1
              print ("Oops! That letter is not in my word:", guessed_word)
        elif str.isalpha(new_guess) == False:
            warnings_remaing -= 1
            if warnings_remaing >= 0:
                print (not_alpha_message, warnings_left, guessed_word)
            else:
                number_guesses -= 1
                number_warnings = 3
                print (not_alpha_message, no_warnings, guessed_word)
        elif new_guess not in available_letters:
            warnings_remaing -= 1
            if warnings_remaing >= 0:
                print (used_letter_message, warnings_left, guessed_word)
            else:
                number_guesses -= 1
                warnings_remaing = 3
                print (used_letter_message, no_warnings, guessed_word)
    print ("-------------")
    if number_guesses <= 0:
        print("Sorry, you ran out of guesses. The word was", secret_word)
        print("")
    elif won == True:
        secret_word_chars = ""
        for char in secret_word:
          if char not in secret_word_chars:
            secret_word_chars += char
        score = number_guesses * len(secret_word_chars)
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
        print("")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #secret_word = "apple"
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
