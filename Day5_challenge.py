#####################################################
## PASSWORD GENERATOR
#####################################################
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(Welcome to the PyPassword Generator!)
nr_letters= int(input(How many letters would you like in your password?\n)) 
nr_symbols = int(input(fHow many symbols would you like?\n))
nr_numbers = int(input(fHow many numbers would you like?\n))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = 
# random_sample_letters = random.sample(letters, nr_letters)
# for letter in random_sample_letters:
# 	password += letter

# random_sample_nr = random.sample(numbers, nr_numbers)
# for number in random_sample_nr:
# 	password += number

# random_sample_symbols = random.sample(symbols, nr_symbols)
# for symbol in random_sample_symbols:
# 	password += symbol

# print(fHere is your password: {password})

##################################################################
# Another way
#####################################################################

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Random letters
password_generator = []

random_sample_letters = random.sample(letters, nr_letters)
for letter in random_sample_letters:
	password_generator.append(letter)

# Random numbers
random_sample_nr = random.sample(numbers, nr_numbers)
for number in random_sample_nr:
	password_generator.append(number)

# Random symbols
random_sample_symbols = random.sample(symbols, nr_symbols)
for symbol in random_sample_symbols:
	password_generator.append(symbol)

print(password_generator)

random.shuffle(password_generator)
print(password_generator)

new_password = 
for element in password_generator:
	new_password += element

print(fHere is your password: {new_password})

###################################################################
## FROM THE CHALLENGE 
####################################################################
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(Welcome to the PyPassword Generator!)
nr_letters = int(input(How many letters would you like in your password?\n)) 
nr_symbols = int(input(fHow many symbols would you like?\n))
nr_numbers = int(input(fHow many numbers would you like?\n))

#Eazy Level
# password = 

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = 
for char in password_list:
  password += char

print(fYour password is: {password})

