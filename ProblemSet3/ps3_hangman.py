# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    secret_char = list(secretWord)
    secret_in = []

    guess = True

    for i in range(len(secret_char)):
        if secret_char[i] in lettersGuessed:
            secret_in.append(True)
        else:
            secret_in.append(False)

    

    for i in range(len(secret_in)):
        if not secret_in[i]:
            guess = False

    return guess
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    secret_char = list(secretWord)
    secret_in = []

    

    for i in range(len(secret_char)):
        if secret_char[i] in lettersGuessed:
            secret_in.append(secret_char[i])
        else:
            secret_in.append('_')

    return ''.join(secret_in)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    remainGuess = list(string.ascii_lowercase)

    
                       

    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in string.ascii_lowercase:
            remainGuess.remove(lettersGuessed[i])

    


    return ''.join(remainGuess)
            
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print "==================================================="
    print "=========== Welcome to the game, Hangman =========="
    print "==================================================="

    #secretWord = chooseWord(wordlist).lower()

    

    length  = len(secretWord)

    print "Iam thinking of a word that is %s letters long" % length

    print "---------------------"

    numGuesses = 8

    lettersGuessed = []

    mistakesMade = 0

    

    

    while numGuesses >= 0:
        print "---------------------------------------------------------"

        print " You have %s guesses left" % numGuesses
        print "Available letters: % s" % getAvailableLetters(lettersGuessed)
        guess = raw_input("Please enter a guess: " ).lower()

        if  guess in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(guess)

        else:
            print "Oops! you have already guessed that letter % s" % getGuessedWord(secretWord,lettersGuessed)
        

        if not guess in secretWord:
            print "Oops! That letter is not in my word %s" % getGuessedWord(secretWord,lettersGuessed)
            
            numGuesses = numGuesses - 1
        else:
                            
            print "Good guess: %s " % getGuessedWord(secretWord,lettersGuessed)
 
        if isWordGuessed(secretWord,lettersGuessed):
            print "Good guess: %s " % secretWord
            print "Congratulations you won!"
            return

        #numGuesses = numGuesses - 1

        if numGuesses == 0:
            break



    print "You have run out of guesses"
            

        

        

    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
hangman('word')
