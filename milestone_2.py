import random

# Create a list of five fruits.
word_list = ["papaya", "mango", "watermelon", "pear", "apple"]
print(word_list)

# Choose randomly one of the fruits.
word = random.choice(word_list)
print(word)

# Ask user to guess one letter."
guess = input("Please, give a single letter: ")

# Check if the guess is indeed a letter and just one letter.
if (guess.isalpha() and len(guess)==1):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
# end if
