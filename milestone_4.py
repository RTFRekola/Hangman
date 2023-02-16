import random

class Hangman:
    '''
    This class is used to . 
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

# Check if the approved letter is in the randomly chosen word. 
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess!", guess, "is in the word.")
    else: 
        print("Sorry,", guess, "is not in the word. Try again.")
    # end if
    return

# Ask for user input and check it is valid.
def ask_for_input():
    while True:
        # Ask user to guess one letter."
        guess = input("Please, give a single letter: ")

        # Check if the guess is indeed a letter and just one letter.
        if (guess.isalpha() and len(guess)==1):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        # end if
    # end while
    check_guess(guess)
    return

# Create a list of five fruits.
word_list = ["papaya", "mango", "watermelon", "pear", "apple"]

# Ask for user input, check validity and whether it is in the chosen word.
ask_for_input()


