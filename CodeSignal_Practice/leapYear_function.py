def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))

##############################################################################
## instructions
# input n : for example 5
# output: 12345 (as a string)

###############################################################################
#array = []
#for x in range(n):
#    string = x + 1
#    array.append(string)
#print(array)

# list comprehension
#array = [x + 1 for x in range(n)]
#print(array)
#string = ''.join(str(elem) for elem in array)
#print(string)


# another option? [x + 1 for x in range(n)]
string = ''.join(str(elem) for elem in [x + 1 for x in range(n)])
print(string)

############################################################################################

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
		user_cards.remove(11) and user_cards.append(1)  
    else:
		return sum(user_cards)
print(calculate_score(user_cards))