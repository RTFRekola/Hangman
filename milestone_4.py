import random

class Hangman:
    '''
    This class is used to process Hangman input. 
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
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i]==guess:
                    self.word_guessed[i] = guess
                # end if
            # end for
            self.num_letters = self.num_letters - 1
        else: 
            print(f"Sorry, {guess} is not in the word.")
            # First attempt:
            print(f'You have {self.num_lives} lives left.')
            # Second attempt: 
            # num_lives = self.num_lives
            # print(f'You have {num_lives} lives left.')
            # Third attempt: 
            # print('You have', self.num_lives, 'lives left.')
        # end if

    def ask_for_input(self):
        '''
        This method asks for user input and checks that it is valid.
        '''
        while True:
            # Ask user to guess one letter.
            guess = input('Please, give a single letter: ')
            
            # Check if the guess is indeed a letter and just one letter.
            if not guess.isalpha() or len(guess)!=1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
            # end if
        # end while

# Create a list of five fruits.
word_list = ["papaya", "mango", "watermelon", "pear", "apple"]

# Ask for user input, check validity and whether it is in the chosen word.
h = Hangman(word_list)
h.ask_for_input()


