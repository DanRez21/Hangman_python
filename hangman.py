# Problem Set 2, hangman.py
# Name: Danylo Reznyk
# Collaborators: -
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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
    n=0
    for i in secret_word:
        if i in letters_guessed:
            n+=1
    if n==len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    new = []
    string = ""  
    for i in letters_guessed:
      if i in secret_word:
        new.append(i)
    for c in secret_word:
      if c in new:
        string += c
      else:
        string += "_ "
    
    return string



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    string = string.ascii_lowercase
    for i in letters_guessed:
        if i in string:
            string = string.replace(i,"")
    return string
    
    

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a','e','i','o','u']
    all_letter = [] #all letters, which entered by user
    true_letter = [] #letters that are correctly guessed
    letters = list(secret_word) #letters in the word
    print("You have {} warnings left.".format(warnings_remaining))
    while is_word_guessed(secret_word, true_letter) != True and guesses_remaining > 0:
        print('-' * 13)
        a=True
        while a:
          print("You have {} guess left.".format(guesses_remaining))
          print("Available letters: ", get_available_letters(all_letter))
          i = input("Please guess a letter: ").lower()
          if i in letters and i not in all_letter:
            true_letter.append(i)
            all_letter.append(i)
            print("Good guess: ", get_guessed_word(secret_word, true_letter))
          else:
            #if the letter was entered earlier
            if i in all_letter:
              if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have {} warnings left: ".format(warnings_remaining), get_guessed_word(secret_word, true_letter))
              else : 
                print("Oops! You've already guessed that letter. You have no warnings: ", get_guessed_word(secret_word, true_letter) )
                guesses_remaining -= 1
            #if the letter isn't letter and not in Latin
            elif not i.isalpha() or i not in string.ascii_lowercase:
              if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have {} warnings left: ".format(warnings_remaining), get_guessed_word(secret_word, true_letter))
              else : 
                print("Oops! That is not a valid letter. You have no warnings: ", get_guessed_word(secret_word, true_letter))
                guesses_remaining -= 1
            #if the letter wasn't entered earlier and the letter is letter and in Latin
            else:
              all_letter.append(i)
              if i in vowels :
                guesses_remaining -= 2
              else:
                guesses_remaining -= 1
              print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, true_letter))
          a = False
    if guesses_remaining > 0:
      print("Congratulations, you won! Your total score for this game is: ", guesses_remaining * len(set(true_letter)))
    else:
      print("Sorry, you ran out of guesses. The word was {}".format(secret_word))



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
    my_word_2, my_word_3, other_word_3 = "", "", ""
    for i in my_word:
      if i != " ":
        my_word_2 += i
    left, delete = [], []
    if len(my_word_2) == len(other_word):
        for i in range(len(my_word_2)):
            if my_word_2[i].isalpha():
                left.append(i)
            else:
                delete.append(i)       
    else:
        return False
    for i in left:
        for a in delete:
            if other_word[a] == other_word[i]:
                return False
            else:
                my_word_3 += my_word_2[i]
                other_word_3 += other_word[i]
    return my_word_3 == other_word_3



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    words=[]
    for i in wordlist:
      if match_with_gaps(my_word, i):
        words.append(i)
    return words



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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a','e','i','o','u']
    all_letter = [] #all letters, which entered by user
    true_letter = [] #letters that are correctly guessed
    letters = list(secret_word) #letters in the word
    print("You have {} warnings left.".format(warnings_remaining))
    while is_word_guessed(secret_word, true_letter) != True and guesses_remaining > 0:
        print('-' * 13)
        a=True
        while a:
          print("You have {} guess left.".format(guesses_remaining))
          print("Available letters: ", get_available_letters(all_letter))
          i = input("Please guess a letter: ").lower()
          if i in letters and i not in all_letter:
            true_letter.append(i)
            all_letter.append(i)
            print("Good guess: ", get_guessed_word(secret_word, true_letter))
          else:
            #if the letter was entered earlier
            if i in all_letter:
              if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have {} warnings left: ".format(warnings_remaining), get_guessed_word(secret_word, true_letter))
              else : 
                print("Oops! You've already guessed that letter. You have no warnings: ", get_guessed_word(secret_word, true_letter) )
                guesses_remaining -= 1
            elif i=='*':
              print("Possible word matches are: ", show_possible_matches(get_guessed_word(secret_word, true_letter)))
            #if the letter isn't letter and not in Latin
            elif not i.isalpha() or i not in string.ascii_lowercase:
              if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have {} warnings left: ".format(warnings_remaining), get_guessed_word(secret_word, true_letter))
              else : 
                print("Oops! That is not a valid letter. You have no warnings: ", get_guessed_word(secret_word, true_letter))
                guesses_remaining -= 1
            #if the letter wasn't entered earlier and the letter is letter and in Latin
            else:
              all_letter.append(i)
              if i in vowels :
                guesses_remaining -= 2
              else:
                guesses_remaining -= 1
              print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, true_letter))
          a = False
    if guesses_remaining > 0:
      print("Congratulations, you won! Your total score for this game is: ", guesses_remaining * len(set(true_letter)))
    else:
      print("Sorry, you ran out of guesses. The word was {}".format(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
