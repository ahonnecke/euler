import sys
import time
import math

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# a b c
# d e f
# h i j

starttime = time.time()

Matrix = {
    "a" : [ "b", "d" ],
    "b" : [ "e", "c" ],
    "c" : [ "f"],
    "d" : [ "e", "h" ],
    "e" : [ "f", "i" ],
    "f" : [ "j" ],
    "h" : [ "i" ],
    "i" : [ "j" ],        
    "j" : [ ],        
}

def find_all_paths(matrix, start, end, paths=[]):
    mypaths = paths + [start]
    if start == end:
        paths.append("j")
        print(paths)
    else:
        for node in matrix[start]:
            #print(node)
            find_all_paths(matrix, node, end, mypaths)

find_all_paths(Matrix, "a", "j")
        
endtime = time.time()
sys.exit("Elapsed: " + str(endtime - starttime))
