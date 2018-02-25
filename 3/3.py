import sys
import math

lower = 1
upper = 600851475143
#upper = 13195
maxfac = 0
num = int(math.sqrt(upper))

def isprime( number ):
    "is number a prime number"
    if(number < 3):
        return False;

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

while (num > 1):
    if(upper % num == 0):
        if (isprime(num)):
            print(str(num) + " is the largest prime factor of " + str(upper))
            num = 1
            break
    num = num - 1;
