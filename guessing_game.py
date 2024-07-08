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
  #empty print statements for spacing 
  print()
  print()

  # storing the random number as a Constant, as it remain
  random_number = random.randint(1, 10)
  #rint(RANDOM_NUMBER)

  # ask for a username to be used and adding unicode emoji of an arrow  as in the list deletion class for fajitas
  user_name = input('Please enter your name for the game \u25B6:')
  # adding some delay
  time.sleep(3)
  print()
  print()

  # initializing  total rounds  variable to  keep track of how many times a single player plays the game 
  #
  total_rounds = 0

 # initial settings of current score with a list
  current_score = []
  # every player starts with 1000 "possible points" to be won each time
  initial_points = 1000
  #Attempts  variables
  #list of  total attempts to keep log of overall attempts from turn to turn
  accrued_attempts = []

  #how many attempts per one turn?
  current_attempts = 0
  
  #  ask continuously for a number

  # start a while loop to continuously ask for the number
  while True:
    
    try:
      #prompting the user for a number
      
      player_number = int(input(f'{user_name.title()},Please take a guess at the secret number >>:'))
      print()
      print()
     

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
      if player_number > random_number:

        print('It\'s lower\u23EC')
        current_attempts += 1
      # else if the number is lower
      elif player_number < random_number:
        print('It\'s higher \u23EB')
        current_attempts += 1

      else:
        # once the number is guessed properly.
        # adding it to the list of attempts
        current_attempts += 1

        # informing the player they have won and how many attempts it took them  using numbers and unicode

        print(f"\u1534 You got it,{user_name}, it took you {current_attempts} attempts  to discover it on this round", current_attempts*'\u2B55')
      # setting scores based on # of attempts
        if current_attempts == 1:
          # the user gets full initial possible points
          score = initial_points
        else:
          # else we multiply the  number of attempts by 10 and then substract the result from the inital points
          score = initial_points-(current_attempts*10)
          print(f'The game is over, your score for this round is {score} ')
          accrued_attempts.append(current_attempts)
          sum_attempts = sum(accrued_attempts)
          
          print(sum_attempts)
          total_rounds += 1
          

        # the player is asking if they want to play again
        play_again = input('Would you like to play again? ')
        # if yes
        if play_again.lower() == 'yes' or play_again.lower() == 'y':
          # store the previous user
          user_name = user_name
          random_number = random.randint(1, 10)
          current_attempts = 0

          current_score.append(score)
          print(50*'*')
          print(f'|Your score for the previous  round was: {(score)}',' '*7 )
          print(50*'_')
          print('|Your current total score for all rounds is:', sum(current_score),-1*'|')
          print(50*'_')
          sum_of_scores=sum(current_score)
         
          max_scores=max(current_score)
          print('|','This is the total of  rounds played: ',total_rounds,' '*6,'|' )
          print(50*'_')
          print('|','This is the total attempts in all rounds:',sum_attempts,''*4,'|')
          print(50*'*')

          # prints the score for the round
                   
          continue

        # else
        elif play_again.lower() == 'no' or play_again.lower() == 'n':
          
          print(f'this is the number of total rounds:{total_rounds} by {user_name}')
        
          print('total score of',sum(current_score))
          print(f'your best round had {min(accrued_attempts)} attempts and a maximum score of {max(current_score)}')

          print(f'Hope to see you again {user_name} \N{GRINNING FACE}')

          # askk if there is any other playing
          new_user = input('Is there another person playing?')
          if new_user.lower() == 'y' or new_user.lower() == 'yes':
            start_game()
          elif new_user.lower() == 'n' or new_user.lower() == 'no':
            print('Good Bye, Players. Until we meet again!')
            break

          # sys.exit()
         # continue: hops to the start of the loop Break: hops OUT of the loop to the next piece of code


start_game()
