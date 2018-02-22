import sys
import time
import math

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

start = time.time()

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

runningsum = 0
maxtocheck = 2000000

for i in range(0, maxtocheck):
    if isprime(i):
        runningsum += i
        
print "The sum of primes below " + str(maxtocheck) + " is " + str(runningsum)

end = time.time()
sys.exit("Elapsed: "+str(end - start))

#The sum of primes below 2000000 is 142913828922
#Elapsed: 22.0553779602
