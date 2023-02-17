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
            self.num_lives = self.num_lives - 1
            print(f'You have {self.num_lives} lives left.')
        # end if
        self.list_of_guesses.append(guess)

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
                break
            # end if
        # end while

# Create a list of five fruits.
word_list = ["papaya", "mango", "watermelon", "pear", "apple"]

def play_game(word_list):
    '''
    This function allows the actual game play.
    '''
    num_lives = 1
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives==0:
            print("You lost!")
            break
        if game.num_letters>0:
            game.ask_for_input()
        if not num_lives==0 and not game.num_letters>0:
            print("Congratulations. You won the game!")
            break
    # end while

play_game(word_list)
