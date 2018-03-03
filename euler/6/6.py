import sys
#import math

#The sum of the squares of the first ten natural numbers is,

#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)^2 = 552 = 3025

#Hence the difference between the sum of the squares of the first
#ten natural numbers and the square of the sum is 3025 - 385 = 2640

#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.

upper = 100
lower = 1

sumofsquares = 0
sums = 0

minimum = 1
num = 0

for x in range(lower, upper+1):
    sumofsquares = sumofsquares + ( x**2 )

print(str(sumofsquares) + " is the sum of squared integers between " + str(lower) + " and " + str(upper))

for x in range(lower, upper+1):
    sums = sums + x

squareofsums = sums**2

print(str(squareofsums) + " is the square of summed integers between " + str(lower) + " and " + str(upper))

difference = squareofsums - sumofsquares

print(str(difference) + " is the difference between the sum of squares and the square of sums for integers between " + str(lower) + " and " + str(upper))

