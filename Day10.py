# Functions with Outputs

# def format_name(first_name, last_name):
# 	formated_f_name = first_name.title()
# 	formated_l_name = last_name.title()
# 	#full_name = first_name.title() + " " + last_name.title()
# 	return f"{formated_f_name} {formated_l_name}"

# ## MANY WAYS OF DOING IT
# #formated_string = format_name('CAMERON', 'ho')
# #print(formated_string)
# print(format_name('andreja', 'ho'))


#####################################################
# RETURN
#####################################################
# !!!!!!! IMPORTANT !!!!!! The return keyword will exit the function and prevent the rest of the code from being executed. !!!!!!
# Notes: "return" statement is the last thing in the function.
# Function will stop afterwards.
# see the example of print statement after the return.

# def format_name(first_name, last_name):
# 	formated_f_name = first_name.title()
# 	formated_l_name = last_name.title()
# 	#full_name = first_name.title() + " " + last_name.title()
# 	return f"{formated_f_name} {formated_l_name}"
#     # gives an error
#     print("This will not be printed on the console")

# print(format_name('andreja', 'ho'))

#################################################################################
# MULTIPLE RETURN STATEMENTS
#################################################################################
def format_name(first_name, last_name):
    if first_name == "" or last_name =="":
        return "This is not a valid input."
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()
    #full_name = first_name.title() + " " + last_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What's your first name? "), (input("What's your last name? "))))


#####################################################
# LEAP YEAR
#####################################################
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

def days_in_month(year_input, month_input):
    '''Takes in year and month and calculates the day in the months.'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year):
        if month == 2:
			return (month_days[month - 1]) + 1 
		else:
			return month_days[month - 1]
	else:
		return month_days[month - 1]

## ANOTHER SOLUTION FOR THE FUNCTION
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month > 12 or month < 1:
#     return "Invalid month entered."
#   if month == 2 and is_leap(year):
#     return 29
#   return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year_input=year, month_input=month)
print(days)
