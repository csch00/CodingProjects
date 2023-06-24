'''
Rock Paper Scissors
'''

computer_option = [1, 2, 3]
computer_option[0] = "Rock" and 1
computer_option[1] = "Paper" and 2
computer_option[2] = "Scissors" and 4

import random
computer_selection = computer_option[random.randint(0,2)]

user_selection = input("Rock, Paper, or Scissors   ")
user_selection = str(user_selection)
if user_selection == "Rock":
  user_value = 1
elif user_selection == "Paper":
  user_value = 2
else:
  user_value = 4

computer_value = ["0","Rock", "Paper", "Scissors"]
show_computer_value = computer_value[computer_selection]
score_computer = 0
score_user = 0


if computer_selection - user_value == 1:
  score_computer += 1
  scoreboard = "Computer: " + str(score_computer) + " User: " + str(score_user)
  print(show_computer_value)
  print("+1 to computer")
  print(scoreboard)
elif computer_selection - user_value == -1:
  score_user += 1
  scoreboard = "Computer: " + str(score_computer) + " User: " + str(score_user)
  print(show_computer_value)
  print("+1 to user")
  print(scoreboard)
elif computer_selection - user_value == 2:
  score_computer += 1
  scoreboard = "Computer: " + str(score_computer) + " User: " + str(score_user)
  print(show_computer_value)
  print("+1 to computer")
  print(scoreboard)
elif computer_selection - user_value == -2:
  score_user += 1
  scoreboard = "Computer: " + str(score_computer) + " User: " + str(score_user)
  print(show_computer_value)
  print("+1 to user")
  print(scoreboard)
elif computer_selection - user_value == 3:
  score_user += 1
  scoreboard = "Computer: " + str(score_computer) + " User: " + str(score_user)
  print(show_computer_value)
  print("+1 to user")
  print(scoreboard)
elif computer_selection - user_value == -3:
  score_computer += 1
  scoreboard = "Computer: " + str(score_computer) + " User: " + str(score_user)
  print(show_computer_value)
  print("+1 to computer")
  print(scoreboard)
else: 
  scoreboard = "Computer: " + str(score_computer) + " User: " + str(score_user)
  print(show_computer_value)
  print("Tie")
  print(scoreboard)
