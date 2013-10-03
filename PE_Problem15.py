# File: PE_Problem15.py
#
# Finds the number of paths on a 20x20 grid of numbers

import math        

'''
    The number of paths on a grid is the (n choose k) where n is the total
    number of steps you must take, and k is the number of steps in one direction
'''

def FindPaths(x,y):
    numPaths = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
    return numPaths

def main():
    gridXDim = 20
    gridYDim = 20

    paths = FindPaths(gridXDim,gridYDim)
    print "Number of paths: " + str(paths)


if __name__ == "__main__":
    main()
