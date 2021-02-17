# replit wont work in VScode
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from asciiart import logo
print(logo)

bidders_data = {}
winner = 0

to_continue = True
while to_continue:

	name = input("What is your name? ")
	bid = int(input("What is your bid? $"))
	bidders_data[name] = bid
	#print(bidders_data)

	other_bidders = input("Are there any other bidders? Type 'yes or no'.\n")
	clear()

  # using lambda function
	if other_bidders == 'no':
		to_continue = False
		for key in bidders_data:
			winner = max(bidders_data.items(), key=lambda x : x[1])
		
		print(f"The winner is {winner[0]} with a bid of ${winner[1]}.")

  # using for loop
  	if other_bidders == 'no':
		to_continue = False
		for key in bidders_data:
			winner_name = max(bidders_data, key=bidders_data.get)
			winner_bid = bidders_data[winner_name]
			
		
		print(f"The winner is {winner_name} with a bid of ${winner_bid}.")

