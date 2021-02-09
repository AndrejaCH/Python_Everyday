#########################################################################################################
# BLIND BIND : MY VERSION
#########################################################################################################
# Notes:
# Creating empty list and appending dicitionaries!
# Important what goes inside or outside the loop
# Important how you set up the while loop (what is before true or false)


#from replit import clear
from art_bid import logo
print(logo)

all_candidates = []
another_bid = True

while another_bid:
	bid_candidates = {}
	candidate_name = input('What is your name? ')
	bid_value = int(input('What is your bid? $ '))

	bid_candidates['name'] = candidate_name
	bid_candidates['bid'] = bid_value
	all_candidates.append(bid_candidates)

	another_bid = input('Are there any other bidders? Type yes or no: ')

	if another_bid == 'yes':
		print(all_candidates)
		#clear() #- replit doesn't work in the VS code
	elif another_bid == 'no':
		another_bid = False
		print(all_candidates)

# Print the winner after exiting the loop
# renew lambda functions 
# winner = dictionary
winner = max(all_candidates, key=lambda x:x['bid'])
print(fThe winner is {winner['name']} with a bid of ${winner['bid']})
##########################################################################################################

#Notes
#dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
# for dic in all_candidates:
#     for val in dic.values():
#         print(val)

# lst = [{'price': 99, 'barcode': '2342355'}, {'price': 88, 'barcode': '2345566'}]

# maxPricedItem = max(lst, key=lambda x:x['price'])
# minPricedItem = min(lst, key=lambda x:x['price'])

#############################################################################################################
# BLIND BID: LESSON VARIATION
#############################################################################################################
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = 
  # bidding_record = {Angela: 123, James: 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(fThe winner is {winner} with a bid of ${highest_bid})

while not bidding_finished:
  name = input(What is your name?: )
  price = int(input(What is your bid?: $))
  bids[name] = price
  should_continue = input(Are there any other bidders? Type 'yes or 'no'.\n)
  if should_continue == no:
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == yes:
    clear()
