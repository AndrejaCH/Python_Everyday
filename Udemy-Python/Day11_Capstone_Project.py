############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
#from replit import clear
from asciiart import blackjack_logo

def blackjack():
	print(logo)

	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	def deal_card():
		return random.choice(cards)

	#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
	# create an empty list to store the values
	user_cards = []
	computer_cards = []

	# create a range to call the function twice.
	for i in range(2):
		# store the return value of the function in a new variable
		user_cards_choice = deal_card()
		# append this stored value in a new list
		user_cards.append(user_cards_choice)

		# do the same for the computer card.
		computer_cards_choice = deal_card()
		computer_cards.append(computer_cards_choice)

	#print(user_cards)	
	#print(computer_cards)
		# sum-up the list to get the score.
		#sum_user_cards = sum(user_cards)

	#declare global variable outside the function
	# user_score = 0
	# computer_score = 0

	#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
	#and returns the score. 
	#Look up the sum() function to help you do this.
	def calculate_score(user_cards, computer_cards):

		#create a variable that you can use it before return statement.
		user_score = sum(user_cards)
		computer_score = sum(computer_cards)
		#calculate user score in the function
			
		#calculate computer score in the function
		#computer_score = sum(computer_cards)
		#return computer_score
		if computer_score == 21:
			computer_score = 0
			#print("You lose!")
			#game over
		elif user_score == 21:
			user_score = 0
			#print("You win!")
			#game over

		if user_score > 21 and 11 in user_cards:
			user_cards.remove(11), user_cards.append(1)
			# recalculate the result
			user_score = sum(user_cards)

		elif computer_score > 21 and 11 in computer_cards:
			computer_cards.remove(11), computer_cards.append(1)
			# recalculate the result
			computer_score = sum(computer_cards)

		return user_score, computer_score

	score = calculate_score(user_cards, computer_cards)
	user_score = score[0]
	computer_score = score[1]

	#print(score)

	# print players cards
	print(f"Your cards: {user_cards}, current score: {user_score}")
	#sum_computer_cards = sum(computer_cards)
	# print computer's first card.
	print(f"Computer's first card: {computer_cards[0]}  c_cards:{computer_cards} c_score:{computer_score}")

	#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

	#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

	#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
		# set the flag for the while loop
	game_on = True
	while game_on:

		again = input("Type 'y' for another card, type 'n' to hold: ")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			print("game over")
			game_on = False
		else:
			if again == 'y':
				for i in range(1):
					# store the return value of the function in a new variable
					user_cards_choice = deal_card()
					# append this stored value in a new list
					user_cards.append(user_cards_choice)
					user_score = sum(user_cards)
					calculate_score(user_cards, computer_cards)
					print(f"Your cards: {user_cards}, current score: {user_score}")
					print(f"Computer's first card: {computer_cards[0]}  c_cards:{computer_cards} c_score:{computer_score}")
			elif again == 'n':
				while computer_score < 17:
					for i in range(1):
						computer_cards_choice = deal_card()
						computer_cards.append(computer_cards_choice)
						computer_score = sum(computer_cards)
						game_on = False
				print(f"Your cards: {user_cards}, current score: {user_score}")
				print(f"Computer's first card: {computer_cards[0]}  c_cards:{computer_cards} c_score:{computer_score}")

	#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.


	#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

	#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.


	#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
	def compare(user_score, computer_score):

		if user_score == computer_score:
			print("It's a draw")
		elif computer_score == 0:
			print("Computer blackjack! \t You lose!")
		elif user_score == 0:
			print("User's blackjack! \t You win!")
		elif user_score > 21:
			print("You lose!")
		elif computer_score > 21:
			print("You win!")
		elif user_score < computer_score:
			print("You lose!")
		elif user_score > computer_score:
			print("You win!")

		print(f"Your final hand: {user_cards}, final score: {user_score}")
		print(f"Computer's first hand: {computer_cards}  final score:{computer_score}")
	#Call the function
	compare(user_score, computer_score)

	if input("Do you want to play again? 'y' or 'n'? ") == 'y':
		#clear()
		blackjack()
	else:
		game_on = False

blackjack()
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
# 	clear()
# 	blackjack()
# else: 
# 	#exit while loop?
# 	game_on = False

