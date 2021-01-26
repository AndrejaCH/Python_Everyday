###############################################################
# FUNCTIONS, INPUT, PARAMETERS AND ARGUMENTS
###############################################################

###############################################################
# CALCULATING WITH FUNCTIONS
###############################################################
# NOTES:
# passing the parameters and arguments
# paint_calc(height=test_h, width=test_w, cover=coverage)
# height = parameter
# test_h =  argument

import math

# def paint_calc(height, width, cover):
#     num_cans = (height * width) / cover
#     round_up_cans = math.ceil(num_cans)
#     print(f"You'll need {round_up_cans} cans of paint.")

def paint_calc(height, width, cover):
	cover = math.ceil((height * width) / cover)
	print(f"You'll need {cover} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#######################################################################
# PRIME NUMBERS
#######################################################################

#Write your code below this line 👇

# ONE WAY OF DOING IT:
def prime_checker(number):
	if n == 2 or n == 3 or n == 5:
		print("It's a prime number.")
	elif n == 1 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
		print("It's not a prime number.")
	else:
		print("It's a prime number.")

# FROM THE LESSON
# USING FOR LOOP
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


########################################################################
# ENCODING AND DECODING STRINGS - CAESAR CIPHER
########################################################################

