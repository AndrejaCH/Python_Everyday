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


    