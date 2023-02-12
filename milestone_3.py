# Ask for user input and check it is valid.
while(True):
    # Ask user to guess one letter."
    guess = input("Please, give a single letter: ")

    # Check if the guess is indeed a letter and just one letter.
    if (guess.isalpha() and len(guess)==1):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    # end if
# end while
