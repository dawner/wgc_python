# Hangman sample program for Wellington Girls College 2015

import random

words_file = open("words.txt", 'r').read() # Open a file and read it
word_array = words_file.split("\n") # Break it up into a list
computer_word = random.choice(word_array) # Pick a random word from the list

past_guesses = []
guesses_left = 8

while True: #Loop forever
  for letter in computer_word:
    if letter in past_guesses:
      print(letter, end=" ") # 'end=" "' puts a space instead of a newline character, \n
    else:
      print("_", end=" ")

  print("\n\nYou have", guesses_left, "guesses left.")
  guest_letter = input("Guess a letter: ") # Ask user to input a letter

  past_guesses.append(guest_letter)

  if guest_letter in computer_word:
    solved_word = True

    for letter in computer_word:
      if letter not in past_guesses: solved_word =  False #Havn't guessed the full word yet

    if solved_word:
      print("\n", computer_word)
      print("Congratulations, you guessed the word! \(^.^)/")
      break
  else:
    guesses_left = guesses_left - 1

    if guesses_left == 0:
      print("Sorry, but you've run out of guesses. (~_~) ")
      print("The word was %s." % computer_word)
      break