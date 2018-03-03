import sys
import time
import math
from pprint import pprint

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
for i in range(1, total):
    arcs = []
    if i+1 <= total and i % limit != 0:
        arcs.append(i+1)
        
    if  i+limit <= total:
        arcs.append(i+limit)
    print("i:" + str(i))
    pprint(arcs)
    Matrix[i] = arcs
Matrix[total] = []


# def find_a_path(matrix, start, end, paths=[]):
#     mypaths = paths + [start]
#     if start == end:
#         return(mypaths)
#     else:
#         for node in matrix[start]:
#             if node not in mypaths:
#                 return(find_a_path(matrix, node, end, mypaths))

# print(find_a_path(Matrix, "a", "j"))

print("Finished building input matrix")

# def find_all_paths(matrix, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         print('.', end='')
#         return([path])
#     paths = []
#     for node in matrix[start]:
#         if node not in paths:
#             for newpath in find_all_paths(matrix, node, end, path):
#                 paths.append(newpath)
#                 count += 1
#     return paths

# print("Finished construcing path array")
# allpaths = find_all_paths(Matrix, 1, total)

def count_all_paths(matrix, start, end, path=[]):
    path = path + [start]
    if start == end:
        return 1
    count = 0
    for node in matrix[start]:
        count += count_all_paths(matrix, node, end, path)
        if count > 50:
            print(str(node) + ": " + str(count))
    return count

print("Finished construcing path array")
allpaths = count_all_paths(Matrix, 1, total)

print(str(allpaths) + " total paths for a " + str(limit-1) + " x " + str(limit-1) + " grid")

        
endtime = time.time()
sys.exit("Time elapsed: " + str(endtime - starttime))
