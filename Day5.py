#########################################
# FOR LOOPS
#########################################

## Calculate the average without sum() and len() function

# 🚨 Don't change the code below 👇
student_heights = input(Input a list of student heights ).split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height_count = 0
number_of_items = 0
for height in student_heights:
	height_count += height
	number_of_items	+= 1

result = (height_count/number_of_items)
print(fThe average heigh of students is: {result:.0f}cm)

#print(round(height_count/number_of_items))
#print(height_count/number_of_items)

######################################################################
## Calculate max and min with the for loop
######################################################################
# 🚨 Don't change the code below 👇
student_scores = input(Input a list of student scores ).split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = student_scores[0]
# or this will work too: highest_score = 0
for score in student_scores:
	#highest_score = student_scores[0] - this was the trial, when moved in the line 10 it worked! Think why!
	if score > highest_score:
		highest_score = score
		#print(highest_score) - no need for this anymore, but gives you a clue how the numbers are selected and compared to each other!


#print(highest_score)

print(fThe highest score in the class is: {highest_score})
# for min just channge the > to <!

#############################################################
## count all even numbers from 1 to 100
#############################################################
total = 0
for number in range(2, 101, 2):
	total += number
print(total)

# even_sum = 0
# for number in range(2, 101, 2):
#   # print(number)
#   even_sum += number
# print(even_sum)
  
# #or

# alternative_sum = 0
# for number in range(1, 101):
#   if number % 2 == 0:
#     # print(number)
#     alternative_sum += number
# print(alternative_sum)

############################################################
## FizzBuzz
############################################################
for number in range(1, 101):
	if number % 15 == 0:
    #if number % 3 == 0 and number % 5 == 0:
		print(FizzBuzz)		
	elif number % 5 == 0:
		print(Buzz)
	elif number % 3 == 0:
		print(Fizz)
	else:
		print(number)