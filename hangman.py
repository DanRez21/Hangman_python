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
    return n==len(secret_word)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    string = ""  
    for c in secret_word:
      if c in letters_guessed:
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
    import string
    string = string.ascii_lowercase
    for i in letters_guessed:
        if i in string:
            string = string.replace(i, "")
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
    all_letter = [] #all letters, which entered by user
    print("You have {} warnings left.".format(warnings_remaining))
    while is_word_guessed(secret_word, all_letter) != True and guesses_remaining > 0:
        print('-' * 13)
        a=True
        while a:
          print("You have {} guess left.".format(guesses_remaining))
          print("Available letters: ", get_available_letters(all_letter))
          i = input("Please guess a letter: ").lower()
          if i in secret_word and i not in all_letter and i!='':
            all_letter.append(i)
            print("Good guess: ", get_guessed_word(secret_word, all_letter))
          else:
            #if the letter was entered earlier
            if i in all_letter or not i.isalpha() or i not in string.ascii_lowercase or len(i)!=1:
              if i in all_letter:
                msg="You've already guessed that letter."
              else:
                msg="That is not a valid letter."
              if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! ",msg, " You have {} warnings left: ".format(warnings_remaining), get_guessed_word(secret_word, all_letter))
              else : 
                print("Oops! ",msg, " You have no warnings: ", get_guessed_word(secret_word, all_letter))
                guesses_remaining -= 1
            #if the letter wasn't entered earlier
            else:
              all_letter.append(i)
              if i in 'aeiou' :
                guesses_remaining -= 2
              else:
                guesses_remaining -= 1
              print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, all_letter))
          a = False
    print('-' * 13)
    if guesses_remaining > 0:
      print("Congratulations, you won! Your total score for this game is: ", guesses_remaining * len(set(secret_word)))
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
    left=[]
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
      return False
    for i in my_word:
      if i.isalpha():
        left.append(i)
    for n, i in enumerate(my_word):
      if i.isalpha():
        if i!=other_word[n]:
          return False
      else:
        if other_word[n] in left:
          return False
    return True

          

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    words = []
    for i in wordlist:
      if match_with_gaps(my_word, i):
        words.append(i)
    if len(words)==0:
      print("No matches found")
    else:
      print(words)


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
    all_letter = [] #all letters, which entered by user
    print("You have {} warnings left.".format(warnings_remaining))
    while is_word_guessed(secret_word, all_letter) != True and guesses_remaining > 0:
        print('-' * 13)
        a=True
        while a:
          print("You have {} guesses left.".format(guesses_remaining))
          print("Available letters: ", get_available_letters(all_letter))
          i = input("Please guess a letter: ").lower()
          if i in secret_word and i not in all_letter and i!='' and len(i)==1:
            all_letter.append(i)
            print("Good guess: ", get_guessed_word(secret_word, all_letter))
          else:
            if i=='*':
              print("Possible word matches are: ")
              show_possible_matches(get_guessed_word(secret_word, all_letter))
            #if the letter was entered earlier
            elif i in all_letter or not i.isalpha() or i not in string.ascii_lowercase or len(i)!=1:
              if i in all_letter:
                msg="You've already guessed that letter."
              else:
                msg="That is not a valid letter."
              if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! ",msg, " You have {} warnings left: ".format(warnings_remaining), get_guessed_word(secret_word, all_letter))
              else : 
                print("Oops! ",msg, " You have no warnings: ", get_guessed_word(secret_word, all_letter))
                guesses_remaining -= 1
            #if the letter wasn't entered earlier
            else:
              all_letter.append(i)
              if i in 'aeiou' :
                guesses_remaining -= 2
              else:
                guesses_remaining -= 1
              print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, all_letter))
          a = False
    print('-' * 13)
    if guesses_remaining > 0:
      print("Congratulations, you won! Your total score for this game is: ", guesses_remaining * len(set(secret_word)))
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