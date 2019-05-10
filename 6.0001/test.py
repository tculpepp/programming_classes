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
    my_word_stripped = my_word.replace(' ', '')
    index = 0
    match = False
    used_letters = ''
    if len(my_word_stripped) == len(other_word):
      for char in my_word_stripped:
          if char == other_word[index]:
            match = True
            used_letters += char
            index += 1
          elif char == "_" and other_word.find(char) == -1 and char not in used_letters:
            match = True
            index += 1
          else: 
            match = False
            break
    return match

print (match_with_gaps("a_ _ le", "apple"))