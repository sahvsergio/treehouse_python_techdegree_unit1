"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

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
high_score=1000000000

def start_game():
  
  global high_score
  
  # creating the header of the game

  # creating the  intro messages
  welcoming_message = """Welcome to the number guessing game"""
  
  instructions = 'The idea of the game is guessing  a number between 1 and 10'

  # splitting the string into  a list of words
  welcoming_words = welcoming_message.split()
  # printing 30 "*" as the top line of a box
  print(171*' ',30*'*')
  #looping to create box  in order to 
  for word in welcoming_words:
     if len(word) == 2:
       print(' '*171, '*', word, ' '*(len(word)+21), '*')
     if len(word) == 3:
       print(' '*171, '*', word, ' '*(len(word)+19), '*')
     if len(word) == 4:
       print(' '*171, '*', word, ' '*(len(word)+17), '*')
     if len(word) == 7:
       print(' '*171, '*', word, ' '*(len(word)+11), '*')
     if len(word) == 8:
       print(' '*171, '*', word, ' '*(len(word)+9), '*')

      
     time.sleep(1)

     
     
  print()
  print()
  #creating the lower part of the box by multiplying a string
  #printing the highscore at the top
  print(f'Current HighScore: {high_score}'.center(127))
  time.sleep(3)
  print(171*' ',30*'*')
  
  #spacing out 
  print()
  print()
  # spacing out
  instructions="""
              The idea behind the game is
              to guess the randomly generated number which is i the range of 1-10. 
              Feedback will be provided in the form of 
              a message saying: it is higher or it is lower,
              prompting you for a new guess
              or telling you if there is an invalid input, such as letters,
              decimals, negative numbers or number out of the range""".center(180)
  print(instructions)
  #print(instructions.center(127))
  #empty print statements for spacing 
  print()
  print()

  # storing the random number as a Constant, as it remain
  random_number = random.randint(1, 10)
  

  # ask for a username to be used and adding unicode emoji of an arrow  as in the list deletion class for fajitas
  user_name = input('Please enter your name for the game \u25B6:'.center(70))
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
  initial_points = 1000000
  #Attempts  variables
  #list of  total attempts to keep log of overall attempts from turn to turn
  accrued_attempts = []

  #how many attempts per one turn?
  
  current_attempts = 0
  
  #  

  # start a while loop to continuously ask for the number continuously  
  while True:
    
        
    try:
      #prompting the user for a number anc centering the print statement with .center()
      
      player_number = int(input(f'{user_name.title()},Please take a guess at the secret number >>:'.center(80)))
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
        raise Exception('The number must be higher than 0 \N{cross mark}'.center(127))

      # if number is higher than 10
      elif player_number > 10:
        current_attempts += 1
        raise Exception('Number cannot be higher than 10 \N{cross mark}'.center(127))
      
    # handle exception of user entering floats or entering the number spelled-out, i.e Value Errors
    
    except ValueError:
      current_attempts += 1
      print(
          f'please enter a valid number, no letter, no decimals \N{cross mark}'.center(127))
    except Exception as e:
      # printing
      print(e)
   # using the else statement to keep running the program once exceptions are raised and handled
    else:
      # if number is lower, user will see a message saying "it's lower " and an arrow prompting them to
      if player_number > random_number:

        print('It\'s lower\u23EC'.center(127))
        current_attempts += 1
      # else if the number is lower
      elif player_number < random_number:
        print('It\'s higher \u23EB'.center(127))
        current_attempts += 1

      else:
        # once the number is guessed properly.
        # adding it to the list of attempts
        current_attempts += 1

        # informing the player they have won and how many attempts it took them  using numbers and unicode
        print(100*'*')
        print(f" You got it,{user_name.title()}, it took you {current_attempts} attempts  to discover it on this round", current_attempts*'\u2B55')
      # setting scores based on # of attempts
      # added the current value of current attempts to the accrued(accummulated) attempts for all rounds
        accrued_attempts.append(current_attempts)
        # we add all the elements fo the accreed_attempts to get the complete attempts in all turns
        sum_attempts = sum(accrued_attempts)
        if current_attempts == 1:
          # the user gets full initial possible points
          score = initial_points
          
        else:
          # else  attempts are more than 1 , we multiply the  number of attempts by 10 and then substract the result from the inital points
          score = initial_points-(current_attempts*10)
          print(f'The game is over, your score for this round is {score} ')
          

          #increase the total turns or rounds in 1 after it 
        total_rounds += 1
        current_score.append(score)
          

        # the player is asked if they want to play again
        play_again = input('Would you like to play again? ')
        sum_of_scores = sum(current_score)
        # if yes
        #turn whatever input into lower case for better comparison and provide 2 options  yes or y
        if play_again.lower() == 'yes' or play_again.lower() == 'y':
          # store the previous user
          user_name = user_name
          #make sure that the new random number 
          random_number = random.randint(1, 10)
          #reinitating  attempt variables for each turn
          current_attempts = 0
          

          
          #a summary of their performace is printed
          print(50*'*')
          print(f'|Your score for the previous  round was: {(score)}',' '*7 )
          print(50*'_')
          print('|Your current total score for all rounds is:', sum(current_score),-1*'|')
          print('The hi-score for the game is ',high_score)
          print(50*'_')
          #sum_of_scores=sum(current_score)
         
          max_scores=max(current_score)
          print('|','This is the total of  rounds played: ',total_rounds,' '*6,'|' )
          print(50*'_')
          print('|','This is the total attempts in all rounds:',sum_attempts,''*4,'|')
          print(50*'*')
          print()
          if sum_of_scores>high_score:
            high_score=max_scores
            print(f'New hi-score achieved by {user_name}:{high_score}')
            # prints the score for the round
            continue
          else:
            print(f'Hi-Score is {high_score}'.center(127))
            print()
            print()

        
        #if the player does not want to play again

        # we turn the input into lowercase for comparison and have 2 options 'no' or n 
        else:
          #play_again.lower() == 'no' or play_again.lower() == 'n':
          #prnting 
          user_name=''
          print()
          print()
          print(50*'*')   
          print(f'this is the number of total rounds:{total_rounds} by {user_name}')
          
          print(50*'*')
               
          
          print('total score of',sum(current_score))
          
          
        
          
          print(50*'*')
          print(f'your best round had {min(accrued_attempts)} attempts and a maximum score of {max(current_score)}')
          if sum_of_scores>high_score:
            high_score=max(current_score)
            print()
            print()
            print(f'New Hi-Score achieved by {user_name}: {high_score}'.center(127)) 
          
          print(50*'*')

          

          print(50*'*')

          print()
          print()
          

          print(f'Hope to see you again {user_name} \N{GRINNING FACE}')
          print('Please remember our hi-score: ',high_score)
          print(50*'*')
          print()
          print()

          # offer to have someone else playing-perhaps a friend sitting next to them taking turns
          new_user = input('Is there another person playing?')
          #compare the response
          #if yes
          if new_user.lower() == 'y' or new_user.lower() == 'yes':
            #start the game fresh
            start_game()
          #if not
          else:
            #new_user.lower() == 'n' or new_user.lower() == 'no':
            print()
            print()
            #print the good bye message and break the game
            print('Good Bye, Players. Until we meet again!')
            print('Remember our hi-score : ',high_score)
            sys.exit()

          # sys.exit()
         # continue: hops to the start of the loop Break: hops OUT of the loop to the next piece of code


start_game()
