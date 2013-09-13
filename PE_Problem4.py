# File: PE_Problem4.py
#
# Finds the largest palindrome that results from the multiplication
# of two three digit numbers.

import string

def main():
    i = 100
    j = 101
    largest_palindrome = 0
    for i in range(100,999):
        for j in range(100,999):
##            print "Forwards: " + str(i*j)
##            print "Backwards: " + str(i*j)[::-1]
##            break
            if str(i*j) == str(i*j)[::-1] and i*j > largest_palindrome:
                largest_palindrome = i * j

    print largest_palindrome

if __name__ == "__main__":
    main()
