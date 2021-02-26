import random
#from replit import clear

play_a_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# if play_a_game == 'n':
# 	#exit_game = True
# else:
# 	#call a function to play a game.
 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
	return random.choice(cards)

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

for i in range(2):
	user_cards_choice = deal_card()
	user_cards.append(user_cards_choice)
	computer_cards_choice = deal_card()
	computer_cards.append(computer_cards_choice)
	sum_user_cards = sum(user_cards)
print(f"Your cards: {user_cards}, current score: {sum_user_cards}")
sum_computer_cards = sum(computer_cards)
print(f"Computer's first card: {computer_cards[0]}")