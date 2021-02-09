print(Welcome to Treasure Island.)
print(Your mission is to find the treasure.) 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#first_stop = input(You come to the 1st crossrad.\n Where do you want to go?\n Type 'L' for left and 'R' for right: )
#second_stop = input(You came to the 2nd stop. Do you want to swim 'S' or walt 'W'? )
#third_stop = input(You came to the 3nd stop. Which door will you choose? Red, Blue or Yellow? )

first_stop = input(You come to the 1st crossrad.\n Where do you want to go?\n Type 'Left' for left and 'Right' for right: ).lower()
if first_stop == 'left':
	second_stop = input(You came to the 2nd stop. Do you want to swim 'Swim' or walt 'Walt'? ).lower()
	print(second_stop)

	if second_stop == 'wait':
		third_stop = input(You came to the 3nd stop. Which door will you choose? Red, Blue or Green ).lower()
		print(third_stop)

		if third_stop == 'blue':
			print(You win!)
		elif third_stop == 'red':
			print(Fire! Game Over!)
		elif third_stop == 'green':
			print(Room full of beasts. Game Over.)
		else:
			print('Game over! Type the valid colour!')

	elif second_stop == 'swim':
		print(Attecked by trout. Game Over.)
	else:
		print(Type the valid command!)

elif first_stop == 'right':
	print(Fall into a hole. Game Over.)
else:
	print(Type the valid command!)
