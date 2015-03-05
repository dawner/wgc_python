# Hangman sample program for Wellington Girls College 2015

import random

words_file = open("words.txt", 'r') # Open a file
file_contents = words_file.read() # Read the file
word_array = file_contents.split("\n") # Break it up into a list

computer_word = random.choice(word_array) # Pick a random word from the list

past_guesses = []
guesses_left = 8

while True: #Loop forever
  for letter in computer_word:
    if letter in past_guesses:
      print(letter, end=" ") # 'end=" "' puts a space at the end instead of a newline character, \n
    else:
      print("_", end=" ")

  print("\n\nYou have", guesses_left, "guesses left.")

  player_guess = input("Guess a letter: ") # Ask user to input a letter
  while len(player_guess) != 1 or not player_guess.isalpha():
    # Print error if input is not a single character or a non-alphabetic character
    print("Guess must be a single letter! Try again.\n")
    player_guess = input("Guess a letter: ")

  player_guess = player_guess.lower() # Make guess lowercase for comparison

  if player_guess in past_guesses:
    print("\nYou already guessed '%s'. Try again." % player_guess)
    continue
  else:
    past_guesses.append(player_guess)

  if player_guess in computer_word:
    solved_word = True

    for letter in computer_word:
      if letter not in past_guesses:
        solved_word =  False # Haven't guessed the full word yet

    if solved_word:
      print("Congratulations! You guess the word:", computer_word, "! \(^.^)/")
      break
  else:
    guesses_left = guesses_left - 1

    if guesses_left == 0:
      print("Sorry, but you've run out of guesses. (~_~) ")
      print("The word was", computer_word)
      break