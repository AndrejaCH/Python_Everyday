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

################################################
# Nested list
#################################################
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
# What will get printed?

######################################################
# financal roullete
#########################################################

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")



#print(f"{random.choice(names)} will pay the bill")
