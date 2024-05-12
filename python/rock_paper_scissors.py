#!/usr/bin/env python3

import random

valid_choices = ['ROCK','PAPER','SCISSORS']

while True:
   print('welcome to rock, paper, scissors!')
   player_choice = input('Please type your choice: ')
   player = player_choice.upper()

   if player not in valid_choices.lower():
      print('that is not a valid option')
      
   robot = random.choice(valid_choices)

# ROCK
   if player == valid_choices[0]:
      print('Player:\t\t',player)
      print('Robot:\t\t',robot)

      if robot == player:
         print('you tied!')
      elif robot == valid_choices[1]:
         print('you lose!')
      elif robot == valid_choices[2]:
         print('you win!')

# PAPER
   if player == valid_choices[1]:
      print('Player:\t\t',player)
      print('Robot:\t\t',robot)

      if robot == player:
         print('you tied!')
      elif robot == valid_choices[0]:
         print('you win!')
      elif robot == valid_choices[2]
         print('you lose!')

# SCISSORS
   if player == valid_choices[2]:
      print('Player:\t\t',player)
      print('Robot:\t\t', )

      if robot == player:
         print('you tied!')
      elif robot == valid_choices[0]:
         print('you lose!')
      elif robot == valid_choices[1]:
         print('you win!')

