
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
	return random.choice(cards)

print(deal_card())

user_cards = []
computer_cards = []

for i in range(3):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


print(user_cards)
print(computer_cards)


def calculate_score(user_cards):
	if user_cards == [10, 11] or user_cards == [11, 10]:
		return 0
	elif 11 in user_cards and sum(user_cards) > 21:
		user_cards.remove(11)
    else:



