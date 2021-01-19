############################################################
## ROCK SCISSORS, PAPER
###########################################################
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
	print(game_images[user_choice])

	computer_choice = random.randint(0, 2)
	print("Computer chose:")
	print(game_images[computer_choice])


	if user_choice == 0 and computer_choice == 2:
		print("You win!")
	elif computer_choice == 0 and user_choice == 2:
		print("You lose")
	elif computer_choice > user_choice:
		print("You lose")
	elif user_choice > computer_choice:
		print("You win!")
	elif computer_choice == user_choice:
		print("It's a draw")


#######################################################
# Working solution, but could use some more work
#######################################################
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
my_choice = int(input(("Type 0 for Rock, 1 for Paper or 2 for Scissors. ")))
computer_choice = random.randint(0, 2)

#print(type(my_choice))
#print(type(my_choice)
#print(computer_choice)

if computer_choice == 0 and my_choice == 1:
	print(f"You chose:\n{paper}\nComputer chose:\n{rock}\n You win")
elif computer_choice == 0 and my_choice == 2:
 		print(f"You chose:\n{scissors}\nComputer chose:\n{rock}\n You lose")
elif computer_choice == 1 and my_choice == 0:
		print(f"You chose:\n{rock}\nComputer chose:\n{paper}\n You lose")
elif computer_choice == 1 and my_choice == 2:
		print(f"You chose:\n{scissors}\nComputer chose:\n{paper}\n You win")
elif computer_choice == 2 and my_choice == 0:
		print(f"You chose:\n{rock}\nComputer chose:\n{scissors}\n You win")
elif computer_choice == 2 and my_choice == 1:
		print(f"You chose:\n{paper}\nComputer chose:\n{scissors}\n You lose")
elif computer_choice == my_choice:
	print("It's a draw")
else:
 	print('Type the right number')
