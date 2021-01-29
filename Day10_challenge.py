# Import logo
from art import logo_calc
print(logo_calc)


#Add 
def add(n1, n2):
	return n1 + n2

#Substract 
def substract(n1, n2):
	return n1 - n2

#Multiply
def multiply(n1, n2):
	return n1 * n2

#Divide 
def divide(n1, n2):
	return n1 / n2

# Create a dictionary named operations
operations = {
'+': add,
'-': substract, 
'*': multiply,
'/': divide,
}


def calculator():
	num1 = float(input("What's the first number?: "))
	for key in operations:
		print(key)

	# setting a flag
	should_continue = True
	while should_continue:

		opretation_symbol = input("Pick an operation: ")
		num2 = float(input("What's the next number?: "))
		calculation_function = operations[opretation_symbol]
		answer = calculation_function(num1, num2)
		print(f"{num1} {opretation_symbol} {num2} = {answer}")
		if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
			num1 = answer
		else:
			should_continue = False
			calculator()

calculator()