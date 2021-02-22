###################################################
# FUNCTIONS
###################################################

## A SIMPLE FUNCTION
# def my_function():
#   Do this
#   Then do this
#   Finnaly do this
# my_function()

## FUNCTIONS WITH INPUTS
# def my_function(something):
#   Do this with something
#   Then do this
#   Finnaly do this
# my_function()

## FUNCTIONS WITH OUTPUTS
# def my_function():
#   result = 3*2
#   return result
# my_function() => output will be the 
# output = result (save this result in another variable)

## SHORT VERSION: FUNCTIONS WITH OUTPUTS
# def myfunction():
#   return 3*2
# output = my_function() ##save the output/result of the function

# leap year!!


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(enter_year, enter_month):
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
	#pseudocode:
	if month > 12 or month < 1:
		return "Ivalid month"
	if is_leap(enter_year) == True and enter_month == 2:
		return 29
	else:
		return month_days[enter_month -1]
		
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
