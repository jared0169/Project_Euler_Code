# File: PE_Problem11.py
#
# Finds the product of 4 adjacent integers in a grid.

import re

def Right(i,j,grid,k):
    product = 1
    if j <= (len(grid[i]) - k):
        for m in range(k):
            product *= grid[i][j+m]
        return product
    return product

def Down(i,j,grid,k):
    product = 1
    if i <= (len(grid) - k):
        for m in range(k):
            product *= grid[i+m][j]
        return product
    return product

def diagDownLeft(i,j,grid,k):
    product = 1
    if i <= (len(grid) - k) and j >= (k-1):
        for m in range(k):
            product *= grid[i+m][j-m]
        return product
    return product

def diagDownRight(i,j,grid,k):
    product = 1
    if i <= (len(grid) - k) and j <= (len(grid[i]) - k):
        for m in range(k):
            product *= grid[i+m][j+m]
    return

def getLargestProduct(i,j,largest_product,grid,k):
    directions = [Right,Down,diagDownLeft,diagDownRight]

    for direction in directions:
        product = direction(i,j,grid,k)
        if product > largest_product:
            largest_product = product
    return largest_product

def main():
    grid = []
    f = open('PE_11_File.txt','r')
    for line in f:
        grid.append(re.findall("[0-9]{2}",line))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = int(grid[i][j])

    k = 4
    largest_product = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            largest_product = getLargestProduct(i,j,largest_product,grid,k)

    print largest_product
    #diagUpLeft(1,3,grid,3,coordDictionary)
    #print grid
    #print str(len(grid)) + "x" + str(len(grid[0]))


if __name__ == "__main__":
    main()
