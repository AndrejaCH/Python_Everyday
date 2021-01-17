
##############################################################################
# ### Write a program that switches the values stored in the variables a and b
##############################################################################
# # 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# c = a
# a = b
# b = c

# #Write your code above this line 👆
# ####################################

# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)

##################################################################################
## Band name genarator
##################################################################################
print("Welcome to the Band Name Generator.")
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)

###################################################################################
## Life in weeks
###################################################################################
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


####################################################################################
# EVEN OR ODD NUMBER. CONDITIONALS, MODULO
####################################################################################
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
	print("This is even number.")
else:
	print("This is an odd number.")


#######################################################################################
# NESTED IF STATEMENT: BMI CALCULATOR
#######################################################################################
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2

if bmi < 18.5:
	print(f"Your BMI is {bmi:.2f}, you are underweight.") 
elif bmi >= 18.5 and bmi < 25:
	print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
	print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")
elif bmi >= 30:
	print(f"Your BMI is {bmi:.2f}, you are clinically obese.")

## ANOTHER VERSION: note the version above migh not be the best one.

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

###############################################################
## LEAP YEAR
################################################################
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
	if year % 100 != 0:
		print("Leap year.")
	else:
		if year % 400 == 0:
			print("Leap year.")
		else:
			print("Leap year.")
else:
	print("Not leap year.")


# Another soulution
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


#####################################################
# MULTIPLE CONDITIONAL STATEMENT: ORDERING PIZZA
# ###################################################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

#############################################################
# buzzfizz love calculator
#############################################################
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_word = 'true'
second_word = 'love'

both_names = name1.lower() + name2.lower()

letter_t = both_names.lower().count('t')
letter_r = both_names.lower().count('r')
letter_u = both_names.lower().count('u')
letter_e = both_names.lower().count('e')
true_score = letter_t + letter_r + letter_u + letter_e
print(f"Score for TRUE is: {true_score }")

letter_l = both_names.lower().count('l')
letter_o = both_names.lower().count('o')
letter_v = both_names.lower().count('v')
letter_ee = both_names.lower().count('e')
love_score = letter_l + letter_o + letter_v + letter_ee

print(f"Score for TRUE is: {love_score}")
total_score = str(true_score) + str(love_score)
print(total_score)

if int(total_score) < 10 or int(total_score) > 90:
	print(f"Your score is {total_score}, you go together like coke and mentos.")
elif int(total_score) > 40 and int(total_score) < 50:
	print(f"Your score is {total_score}, you are alright together.")
else:
	print(f"Your score is {total_score}.")


