#Find a century
# Find a century in a year
def centuryFromYear(year):
    return(year - 1) // 100 + 1

print(centuryFromYear(2022))

# Reverse string & Palindrome
def checkPalindrome(inputString):
    if inputString.lower() == inputString.lower()[::-1]:
        return True
    else:
        return False


# Given an array of integers, 
# find the pair of adjacent elements that has the largest product and return that product. 
# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.
# 7 and 3 produce the largest product.

def adjacentElementsProduct(inputArray):
    
    lenght = len(inputArray)
    result = []
    for n in range(lenght-1):
        result.append(inputArray[n] * inputArray[n+1])
    return max(result)

# Finding shape area
def shapeArea(n):
if n == 1:
    return 1
return n**2 + (n-1)**2

# Find consecutive statues
# https://babywalnut.tistory.com/3
def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1