##########################################
# Day 4: 
#########################################
# random
import random
#import my_module

random_int = random.randint(1,4)
#print(random_int)

#print(my_module.pi)
random_float = random.random()
#print(random_float)

print(random_int * random_float)


# Toss the coin
import random

print(input("Press enter to toss the coin."))

random_integer = random.randint(0, 1)
if random_integer == 1:
  print("Heads")
else:
	print("Tails")


# Treasure
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position[0])
row = int(position[1])

map[row -1][column -1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")