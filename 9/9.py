import sys
import time

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

start = time.time()
total = 1000

def istriplet( a, b, c ):
    "are numbers a pythagorean triplet"
    
    if(b >= c):
        return False

    if(a >= b):
        return False

    if (a ** 2 + b ** 2) == c ** 2:
        return True
    else:
        return False

a = 0
b = 0
c = 0

for c in range(0, total):
    for b in range(0, total):
        for a in range(0, total):
            if istriplet(a, b, c):
                if(a + b + c == total):
                    print "****** "+str(a) + " " + str(b) + " " + str(c)
                    print str(a * b * c)
                    end = time.time()
                    sys.exit("Elapsed: "+str(end - start))
                else:
                    print str(a) + " " + str(b) + " " + str(c)


#255 340 425
#****** 200 375 425
#31875000
#Elapsed: 76.9551150799
