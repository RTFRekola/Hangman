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

    def check_guess(self, guess):
        '''
        This method checks if the approved letter is in the randomly chosen word. 
        '''
        guess = guess.lower()
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
        #else: 
        #    print("Sorry,", guess, "is not in the word. Try again.")
        # end if
        return

    def ask_for_input(self):
        '''
        This method asks for user input and checks that it is valid.
        '''
        while True:
            # Ask user to guess one letter."
            guess = input("Please, give a single letter: ")
            
            # Check if the guess is indeed a letter and just one letter.
            if not (guess.isalpha() and len(guess)==1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                #h = Hangman(word_list)
                #h.check_guess(guess)
                Hangman.check_guess(guess)
            # end if
        # end while
        return

# Create a list of five fruits.
word_list = ["papaya", "mango", "watermelon", "pear", "apple"]

# Ask for user input, check validity and whether it is in the chosen word.
h = Hangman(word_list)
h.ask_for_input()


