import sys

#2520 is the smallest number that can be divided by each of the numbers
#              from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all
#              of the numbers from 1 to 20?

upper = 20
lower = 1

minimum = 1
num = 0

def isDivisible(lower, upper, divisor):
    "is divisor evenly divisible by all numbers betwen lower and upper"
    for x in range(lower, upper):
        if(divisor % x != 0):
            return False
    return True

done = False
while(False == done):
    num = num+1;
    if(isDivisible(lower, upper, num)):
        done = True
    else:
        continue

print str(num) + " is the lowest number that is evenly divisible by all numbers between " + str(lower) + " and " + str(upper)
