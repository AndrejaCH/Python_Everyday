
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
else:
	print(f"Your BMI is {bmi:.2f}, you are clinically obese.")