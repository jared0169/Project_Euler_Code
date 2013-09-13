# File: PE_Problem11.py
#
# Finds the product of 4 adjacent integers in a grid.

import re

def main():
    grid = []
    f = open('PE_11_File.txt','r')
    for line in f:
        grid.append(re.findall("[0-9]{2}",line))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = int(grid[i][j])

    print grid
    #print str(len(grid)) + "x" + str(len(grid[0]))


if __name__ == "__main__":
    main()
