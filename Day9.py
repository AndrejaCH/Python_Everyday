###################################################
# DICTIONARIES
####################################################

programming_dictionary = {
	Bug: An error in a program that prevents the program from running as expected., 
	Function: A piece of code that you can easily call over and over again.,
	}

# Retrieving items form dictionary.
print(programming_dictionary[Bug])

#Adding nwe items to dictionary.
programming_dictionary[Loop] = The action of doings something over and over again

#print(programming_dictionary)

#Empty dictionary
empty_dictionary = {}

#Wipe and existing dictionary
#programming_dictionary = {}
print(programming_dictionary)

# Edit/modifying an item in a dictionary
programming_dictionary[Bug] = A moth in your computer

print(programming_dictionary)

#############################################################
# LOOPING THROUGH DICTIONARY
# Retrieving keys and values
###############################################################

# Loop throught a dictionary
for key in programming_dictionary:
	print(key)
	# Retrival code to get the values!!
	print(programming_dictionary[key])


######################################################################
# STUDENTS GRADES CHALLENGE
######################################################################
student_scores = {
  Harry: 81,
  Ron: 78,
  Hermione: 99, 
  Draco: 74,
  Neville: 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# ONE WAY OF DOING IT!
# for student in student_scores:
# 	score = student_scores[student]
# 	if score > 90:
# 		student_grades[student] = Outstanding


# ANOTHER WAY OF DOING IT 
# CAREFUL WHEN USIN == OR =!! THAT CAUSED A PROBLEM!
for key in student_scores:
	if student_scores[key] >= 91:
		student_grades[key] = Outstanding
	elif student_scores[key] >= 81:
		student_grades[key] = Exceeds Expectations
	elif student_scores[key] >= 71:
		student_grades[key] = Acceptable
	elif student_scores[key] <= 70:
		student_grades[key] = Fail


# 🚨 Don't change the code below 👇
print(student_grades)


###########################################################
# NESTING
###########################################################
#######################################

#Nesting 
capitals = {
  France: Paris,
  Germany: Berlin,
}

#Nesting a List in a Dictionary

travel_log = {
  France: [Paris, Lille, Dijon],
  Germany: [Berlin, Hamburg, Stuttgart],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  France: {cities_visited: [Paris, Lille, Dijon], total_visits: 12},
  Germany: {cities_visited: [Berlin, Hamburg, Stuttgart], total_visits: 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  country: France, 
  cities_visited: [Paris, Lille, Dijon], 
  total_visits: 12,
},
{
  country: Germany,
  cities_visited: [Berlin, Hamburg, Stuttgart],
  total_visits: 5,
},
]


#############################################################################
# TRAVEL LOG
###############################################################################
# NOTES:
# - see the structure of the data
travel_log = [
{
  country: France,
  visits: 12,
  cities: [Paris, Lille, Dijon]
},
{
  country: Germany,
  visits: 5,
  cities: [Berlin, Hamburg, Stuttgart]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_name, num_of_visits, cities_visited):
	# Create a new dictionary first. Because the data in travel_log are separate dictionaries.
	# and you want to insert all the data that way.
	new_country = {}
	# now just add the all the values to corresponding keys
	new_country[country] = country_name
	new_country[visits] = num_of_visits
	new_country[cities] = cities_visited
	# now add to the travel log list!! You should call the treavel log to add!
	travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country(Russia, 2, [Moscow, Saint Petersburg])
print(travel_log)