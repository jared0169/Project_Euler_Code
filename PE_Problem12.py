# File: PE_Problem12.py
#
# Finds the first triangle number with 500+ divisors.

def FindFactors(number):
    # Finds the factors of a number passed to the function.
    # Returns a list of the factors
    factorList = []

    placeHolder = number
    i = 1
    while i not in factorList:
        if placeHolder == 1:
            factorList.append(i)
            break
        if number % i == 0:
            factorList.append(i)
            factorList.append(number/i)
            placeHolder = number / i
        i += 1
    return factorList

def main():
    i = 1
    triangleNum = (i*(i+1))/2
    factors = FindFactors(triangleNum)
    print len(factors)
    factors.sort()
    #print factors
    while (True):
        triangleNum = (i*(i+1))/2
        #factors = FindFactors(triangleNum)
        print i
        if len(FindFactors(triangleNum)) >= 500:
            print "Answer = " + str(triangleNum)
            return
        i += 1
    #print FindFactors(i)
    return



if __name__ == "__main__":
    main()
