########################################################################
# ENCODING AND DECODING STRINGS - CAESAR CIPHER
########################################################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#########################################################################
# Try to refactor with this code:
# def caesar(start_text, shift_amount, direction_type):
# 	end_text = ""
# 	for letter in start_text:
# 		position = alphabet.index(letter)
# 		if direction_type == "encode":
# 			new_position = position + shift_amount
# 		elif direction_type == "decode":
# 			new_position = position - shift_amount
# 		end_text += alphabet[new_position]
# 	print(f"The {direction_type}d text is {end_text}")

#########################################################################

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = char
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
			
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 

should_continue = True
while should_continue:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	#end_program = input("Do you want to continue? Type 'yes' to continue, type 'no' to end.")

	#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
	#Try running the program and entering a shift number of 45.
	#Hint: Think about how you can use the modulus (%).
	shift = shift % 26
	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

	result = input("Type 'yes' if you want to go again. Othrewise type 'no'\n").lower()
	if result == 'no':
		should_continue = False
		print("Godbye")