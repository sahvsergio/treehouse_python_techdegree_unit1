"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import csv
import random
import sys
import time

# Import the random module.

# Create the start_game function.
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.


def start_game():

  # creating the header of the game

  # creating the  intro messages
  welcoming_message = """Welcome to the number guessing game"""
  instructions = 'The idea of the game is guessing  a number between 1 and 10'

  # splitting the string into  a list of words
  welcoming_words = welcoming_message.split()
  # printing 30 "*" as the top line of a box
  print(30*'*')

  # looping through the words list
  for word in welcoming_words:
    # creating the sides of the decorating box and adjusting spaces on the right based on  the length of words
    if len(word) == 2:
      print('*', ' '*10, word, ' '*(len(word)+10), '*')

    if len(word) == 3:
      print('*', ' '*10, word, ' '*(len(word)+8), '*')
    if len(word) == 4:

      print('*', ' '*10, word, ' '*(len(word)+6), '*')

    if len(word) == 7:
      print('*', ' '*10, word, ' '*len(word), '*')
    if len(word) == 8:
     print('*', ' '*10, word, ' '*(len(word)-2), '*')
    # adding delay with time so that the words show  slowly on the screen for practice
    time.sleep(1)

  # creating the lower part of the box by multiplying a string
  print(30*'*')
  # spacing out
  print()
  print()
  # print instructions
  print(instructions)
  print()
  print()

  # storing the random number as a Constant, as it remain
  RANDOM_NUMBER = random.randint(1, 10)

  # ask for a username to be used and adding unicode emoji as in the list deletion video
  user_name = input('Please enter your name for the game \u25B6:')
  # adding some
  time.sleep(3)

  # initializing rounds  variable to count how many rounds a user has played.
  total_rounds = 0

 # initial settings of total_rounds = 0 the game
  current_score = []
  initial_points = 1000
  accrued_attempts = []
  current_attempts = 0
  # every player starts with 1000 "possible points" to be won each time

  #  ask continuously for a number

  # start a while loop to continuously ask for the number
  while True:

    try:

      player_number = int(
          input(f'{user_name.title()},Please take a guess at the secret number >>:'))
      # initalizing an attempts  variable to 1, since they are already trying to guess a number

      # initalizing the score
      score = 0

      # adding some  delay for cognitive load
      time.sleep(1)

      # raise exceptions and informing the user in text and visually using unicode
      # if number is less or equal to zero
      if player_number <= 0:
        current_attempts += 1
        raise Exception('The number must be higher than 0 \N{cross mark}')

      # if number is higher than 10
      elif player_number > 10:
        current_attempts += 1
        raise Exception('Number cannot be higher than 10 \N{cross mark}')
    # handle exception of user entering floats or entering the number spelled-out, i.e Value Errors
    except ValueError:
      current_attempts += 1
      print(
          f'please enter a valid number, no letter, no decimals \N{cross mark}')
    except Exception as e:
      # printing
      print(e)
   # using the else statement to keep running the program once exceptions are raised and handled
    else:
      # if number is lower, user will see a message saying "it's lower " and an arrow prompting them to
      if player_number > RANDOM_NUMBER:

        print('It\'s lower\u23EC')
        current_attempts += 1
      # else if the number is lower
      elif player_number < RANDOM_NUMBER:
        print('It\'s higher \u23EB')
        current_attempts += 1

      else:
        # once the number is guessed properly.
        # adding it to the list of attempts
        current_attempts += 1

        # informing the player they have won and how many attempts it took them  using numbers and unicode

        print(f"\u1534 You got it,{user_name}, it took you {
              current_attempts}attempts  to discover it on this round", current_attempts*'\u2B55')
      # setting scores based on # of attempts
        if current_attempts == 1:
          # the user gets full initial possible points
          score = initial_points
        else:
          # else we multiply the  number of attempts by 10 and then substract the result from the inital points
          score = initial_points-(current_attempts*10)
          print(f'The game is over, your score for this round is {score} ')
          accrued_attempts.append(current_attempts)
          print(accrued_attempts)

        # the player is asking if they want to play again
        play_again = input('Would you like to play again? ')
        # if yes
        if play_again.lower() == 'yes' or play_again.lower() == 'y':
          # store the previous user
          user_name = user_name

          print(f'This is the total sum of attempts {
                sum(accrued_attempts)} so far in rounds{total_rounds}')
          current_attempts = 0

          current_score.append(score)
          print('this is the current score', sum(current_score))

          # prints the score for the round
          print(
              f'The round has ended , your score for this round is {(score)} ')

          total_rounds += 1
          continue

        # else
        elif play_again.lower() == 'no' or play_again.lower() == 'n':
          print(f'this is the number of total rounds:{total_rounds} by{user_name} with a total score of {sum(
              current_score)} your best round had {min(accrued_attempts)} attempts and a maximum score of {max(current_score)}')

          print(f'Hope to see you again {user_name} \N{GRINNING FACE}')

          # askk if there is any other playing
          new_user = input('Is there another person playing?')
          if new_user.lower() == 'y' or new_user.lower() == 'yes':
            start_game()
          elif new_user.lower() == 'n' or new_user.lower() == 'no':
            break

          # sys.exit()
         # continue: hops to the start of the loop Break: hops OUT of the loop to the next piece of code


start_game()
