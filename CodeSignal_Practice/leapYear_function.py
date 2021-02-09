def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))

##############################################################################
## instructions
# input n : for example 5
# output: 12345 (as a string)

###############################################################################
#array = []
#for x in range(n):
#    string = x + 1
#    array.append(string)
#print(array)

# list comprehension
#array = [x + 1 for x in range(n)]
#print(array)
#string = ''.join(str(elem) for elem in array)
#print(string)


# another option? [x + 1 for x in range(n)]
string = ''.join(str(elem) for elem in [x + 1 for x in range(n)])
print(string)

############################################################################################