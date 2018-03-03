import sys

upper = 999
lower = 99

numone = upper
numtwo = upper

maximum = 0

def ispalindrome( number ):
    "is number a palidrome"
    possible = str(number)
    #print "Checking " + possible

    if(possible[0] != possible[-1]):
        return False;

    if(len(possible) == 1):
        return True

    if(len(possible) == 2):
        return (possible[0] == possible[-1])

    fixed = possible[1:]
    return ispalindrome(fixed[:-1])

while (numone > lower):
    while (numtwo > lower):
        num = numone * numtwo
        if(ispalindrome(num)):
            print(str(numone) +  " * " + str(numtwo) + " = "+ str(num) + " is a palidrome")
            if(num > maximum):
                maximum = num

        numtwo = numtwo - 1;
    numone = numone - 1;
    numtwo = upper

print(str(maximum) + " is the largest palidromic number")
