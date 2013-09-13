# File: PE_Problem8.py
#
# Find the greatest product of 5 consecutive digits in the 1000 digit number

import urllib
import string
import re

def source_Processing(inputString):
    # Processes the source code for the project euler problem 8 web
    # page to grab the field of numbers. Mainly to see if I could, but
    # partially because I'm too lazy and didn't want to deal with the
    # copy and paste and making sure it was correct
    
    s1 = ""
    targetString = inputString[inputString.find("r;'>")+4:]
    targetString = targetString[:targetString.find("</p>")]
    while targetString.find("<br />") != -1:
        s1 = s1 + targetString[:targetString.find("<br />")]
        targetString = targetString[targetString.find("<br />")+7:]
    return s1

def get_product(s1):
    product = 1
    for i in s1:
        product *= int(i)
    return product

def find_largest_product(inpString):
    largest_product = 0
    i = 0
    for i in range(len(inpString)-4):
        test_string = inpString[i:i+5]
        product = get_product(test_string)
        if product > largest_product:
            largest_product = product
    return largest_product

def main():
    page = urllib.urlopen("http://projecteuler.net/problem=8")
    source = page.read()

    target_string = source_Processing(source)
##    print len(target_string)
##    print target_string

    target_string = target_string[1:]
    #print len(target_string)
    largest_product = find_largest_product(target_string)
    print largest_product
    



if __name__ == "__main__":
    main()
