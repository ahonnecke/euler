import sys
import math

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#numprime = 6
numprime = 10001

def isprime( number ):
    "is number a prime number"
    if(number < 2):
        return False;

    if(number < 4):
        return True;

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

primesfound = 1
i = 0

while(primesfound <= numprime):
    i += 1
    if (isprime(i)):
        primesfound += 1
        print str(i) + " is the " + str(primesfound-1) + "th prime"
