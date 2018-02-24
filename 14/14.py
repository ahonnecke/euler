import sys
import time
import math

# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

starttime = time.time()

limit = 1000000
maxterms = 0

for i in range(1, limit):
    steps = 1
    start = i
    #print "Doing " + str(i)
    while(start != 1):
        steps += 1
        if start % 2 == 0:
            start = start / 2
        else:
            start = start * 3 + 1
        #print "  Step " + str(start)

    if steps > maxterms:
        maxterms = steps
        print "A seed of '" + str(i) + "' generates " + str(steps) + " terms"

end = time.time()
sys.exit("Elapsed: " + str(end - starttime))

# A seed of '626331' generates 509 terms
# A seed of '837799' generates 525 terms
# Elapsed: 30.5476250648
