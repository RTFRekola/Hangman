# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1: Set up the environment

This consists of getting the Git and GitHub going. 

## Milestone 2: Create the variables for the game

This consists of setting up a word list (as a list), choosing a word from the list (using random.choice), and asking a user to select a letter (with input). Once the user has selected a letter, it is tested (in a if statement) for validity (i.e. that it is an alphabetical letter and just one character). The input is tested with isalpha() method and len. 

## Milestone 3: Check if the guessed character is in the word

Initially the user is asked for input and then this is checked to be a single alphabetical letter. This is repeated until the condition is valid. 
Next we check that the approved letter is in the word randomly chosed from a list of five fruits. 
