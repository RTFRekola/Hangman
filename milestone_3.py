import random

# Create a list of five fruits.
word_list = ["papaya", "mango", "watermelon", "pear", "apple"]

# Choose randomly one of the fruits.
word = random.choice(word_list)

# Ask for user input and check it is valid.
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

# Check if the approved letter is in the randomly chosen word.
if (guess in word):
    print("Good guess!", guess, "is in the word.")
else: 
    print("Sorry,", guess, "is not in the word. Try again.")
# end if 
