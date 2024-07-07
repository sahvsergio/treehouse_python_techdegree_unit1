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

  ## creating the  intro messages
  welcoming_message = """Welcome to the number guessing game"""
  instructions = 'The idea of the game is guessing  a number between 1 and 10'

  ## splitting the string into  a list of words
  welcoming_words = welcoming_message.split()
  # printing 30 "*" as the top line of a box
  print(30*'*')

  ### looping through the words list
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

  ### creating the lower part of the box
  print(30*'*')
  #spacing out 
  print()
  print()
  ###  print instructions
  print(instructions)
  print()
  print()

  # storing the random number as a Constant, as it remain
  RANDOM_NUMBER = random.randint(1, 10)
  #list of players
  players = []
  # ask for a username to be used 
  user_name = input('Please enter your name for the game >>:')
  #adding some 
  time.sleep(3)
  #appending player's name to the players list
  players.append(user_name)
  #initializing rounds  variable to count how many rounds a user has played.
  total_rounds = 0
  #empty
 
  attempts = 0

  initial_points = 1000
  score = 0
  total_score = 0
  previous_score = 0

  # while RANDOM_NUMBER:
  while True:
    try:
      # ask continuously for a number
      player_number = int(
          input(f'{user_name.title()},Please take a guess at the secret number >>:'))
      print(players)
      print(total_score)
      time.sleep(1)
      # raise exceptions
      # if number is less or equal to zero
      if player_number <= 0:
        attempts+=1
        raise Exception('The number must be higher than 0 \N{cross mark}')
  
      # if number is higher than 10
      elif player_number > 10:
        attempts+=1
        raise Exception('Number cannot be higher than 10 \N{cross mark}')
    # handle exception of user entering floats or entering the number spelled-out
    except ValueError:
      attempts+=1
      print(
          f'please enter a valid number, no letter, no decimals \N{cross mark}')
    except Exception as e:
      # printing
      print(e)
      # player_number=
    else:
      if player_number > RANDOM_NUMBER:
        print('It\'s lower\u23EB')
        attempts += 1
      elif player_number < RANDOM_NUMBER:
        print('It\'s higher \u23EC')
        attempts += 1
      else:
        print(f"\u1534 You got it,{user_name}, it took you {
              attempts} attempts to discover it")

        if attempts == 1:
          score = initial_points
        else:
          score = initial_points-(attempts*10)
        print(f'The game is over, your score for this round is {score} ')
        play_again = input('Would you like to play again? ')

        if play_again.lower() == 'yes' or play_again.lower() == 'y':
          # store the previous user
          user_name = user_name
          score += score
          total_rounds += 1
          print(f'This is the number of total rounds so far:{total_rounds-1}')
          # start_game()
          continue

        elif play_again.lower() == 'no' or play_again.lower() == 'n':
          print(f'this is the number of total rounds:{
                total_rounds} by{user_name}')

          print(f'Hope to see you again {user_name} \N{GRINNING FACE}')
          new_user = input('Is there another person playing?')
          if new_user.lower() == 'y' or new_user.lower() == 'yes':
            start_game()
          elif new_user.lower() == 'n' or new_user.lower() == 'no':
            break

          # sys.exit()
         # continue: hops to the start of the loop Break: hops OUT of the loop to the next piece of code


start_game()
