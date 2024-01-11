# Project Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation Instructions

When preparing to run this code for the first time, do the following:

- create a directory for the code; e.g. in Linux terminal <b>mkdir hangman</b>
- copy files milestone_2.py, milestone_3.py, milestone_4.py and milestone_5.py into the directory you just created

## Usage Instructions

- go to the directory where you installed the code
- run the file milestone_5.py; e.g. in Linux terminal <b>python3 milestone_5.py</b>

## License Information

Copyright 2023, Rami Rekola

Copying and distribution of these files, with or without modification, are permitted in any medium without royalty, provided the copyright notice and this notice are preserved. These files are offered as-is, without any warranty.

## Project History

### Create the Variables for the Game

This consists of setting up a word list (as a list), choosing a word from the list (using random.choice), and asking a user to select a letter (with input). Once the user has selected a letter, it is tested (in a if statement) for validity (i.e. that it is an alphabetical letter and just one character). The input is tested with isalpha() method and len. 

### Check If the Guessed Character Is in the Word

Initially the user is asked for input and then this is checked to be a single alphabetical letter. This is repeated until the condition is valid. 
Next we check that the approved letter is in the word randomly chosed from a list of five fruits. 
Finally we move these two operations into two separate functions. The function for asking input does not take any arguments, nor return anything, but does internally ask for user's guess of a letter and checks that it is a single letter. Then it calls for the other function, which takes in as an argument the letter the user guessed, checks whether this letter is in the randomly chosen word and tells the user whether it is or not. Thus the first function is called from the main programme without arguments and after the second function the process returns to the main programme without any return value. 

### Create the Game Class

The Hangman class takes in two arguments, the list of words created in the main programme and the number of lives, which is initiated in the main programme. The number of lives is assigned a value of 5 just in case the initiation fails to include it. Besides these two variables, four other attributes are defined. One attribute chooses randomly a word from the word list and another one is set to be a list with as many underscore values as the length of the chosen word. A third attribute is the number of letters in the chosen word, although this variable is later on decreased by one each time the user makes a correct guess. Finally the list of guesses contains all letters that the user has already correctly guessed. This is needed so that we can tell the user if he makes the same guess more than once. 

Besides the attributes, the class has two methods, besides the standard init. The check_guess function checks if the validated letter exists in the randomly chosen word. If it does, the number of remaining letters is reduced by one. If it does not, the player loses one game life. The function ask_for_input asks for user input and checks that it is valid. If the input is not valid, the user is asked to provide a proper letter. Otherwise the function calls check_guess for the next step. 

### Putting It All Together

Finally the main programme is put together. First we set up the word list, then call for a function that creates an instance of the Hangman class and maintains the game statistics. Essentially, if the players number of game lives goes to zero, the game ends and the player loses. Otherwise, if the number of letters is higher than zero, the game continues and the ask_for_input is called in the Hangman class. If the number of letters, however, is zero, and the player has any game lives left, he is declared a winner and the game ends. 
