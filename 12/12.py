import sys
import time
import math

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

start = time.time()
i = 0
divisors = 0
trinum = 0

while divisors < 500:
    i += 1
    trinum += i

    divisors = 1 #itself

    if trinum % 2 == 0:
        #half of itself (for speed)
        divisors +=1
    
    if trinum % 3 == 0:
        # one third of itself (for speed)
        divisors +=1
    
    if trinum % 4 == 0:
        #one fourth of itself (for speed)
        divisors +=1
    
    for j in range(1, int(trinum/5)+1):
        if trinum % j == 0:
            divisors +=1

    # for j in range(1, int(math.sqrt(trinum))):
    #     if trinum % j == 0:
    #         divisors += 2
            
    print str(trinum) + " has " + str(divisors) + " divisors"
        
#print "The first triangle number with to have over " + str(divisors) + " divisors is " + str(triangle)

end = time.time()
sys.exit("Elapsed: "+str(end - start))

# 76564125 has 96 divisors
# 76576500 has 576 divisors
# Elapsed: 7014.60624409
