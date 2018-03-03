import sys
import time
import math
from pprint import pprint
from collections import defaultdict

# Starting in the top left corner of a 2x2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# a b c
# d e f
# h i j

# Matrix = {
#     "a" : [ "b", "d" ],
#     "b" : [ "e", "c" ],
#     "c" : [ "f"],
#     "d" : [ "e", "h" ],
#     "e" : [ "f", "i" ],
#     "f" : [ "j" ],
#     "h" : [ "i" ],
#     "i" : [ "j" ],        
#     "j" : [ ],        
# }

# 1 2 3
# 4 5 6
# 7 8 9

# Matrix = {
#     "1" : [ "2", "4" ],
#     "2" : [ "5", "3" ],
#     "3" : [ "6"],
#     "4" : [ "5", "7" ],
#     "5" : [ "6", "8" ],
#     "6" : [ "9" ],
#     "7" : [ "8" ],
#     "8" : [ "9" ],
#     "9" : [ ],        
# }

starttime = time.time()
limit = 21
total = limit**2
Matrix = {}
visited = {}
for i in range(1, total):
    visited[i] = False
    arcs = []
    if i+1 <= total and i % limit != 0:
        arcs.append(i+1)
        
    if  i+limit <= total:
        arcs.append(i+limit)
    Matrix[i] = arcs
Matrix[total] = []
visited[total] = False

print("Finished building input matrix")
print("Finished building visited")

def count_all_paths(matrix, start, end, visited=[]):
    """
    :rtype: int
    """    
    count = 0
    if start == end:
        return 1
    for node in matrix[start]:
        if not visited[node]:
            visited[node] = count_all_paths(matrix, node, end, visited)
        count += visited[node]
    return count

print("Finished construcing path array")
allpaths = count_all_paths(Matrix, 1, total, visited)


print(str(allpaths) + " total paths for a " + str(limit-1) + " x " + str(limit-1) + " grid")

endtime = time.time()
sys.exit("Time elapsed: " + str(endtime - starttime))
