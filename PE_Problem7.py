# File: PE_Problem7.py
#
# Determine what the 10001 prime number is

import scipy

def find_primes(n):
    # Finds a list of primes up to the nth prime number
    primes_list = [2,3]
    i = 5
    while (len(primes_list) != n):
        #print i
        isPrime = True;
        j = 1
        while isPrime and i / primes_list[j] >= primes_list[j]:
            #print "In second While Loop"
            if ( i % primes_list[j] == 0):
                isPrime = False;
            j += 1
        if isPrime:
            primes_list.append(i)
        i+=2
    #print primes_list
    print primes_list[-1]
        

def main():
    n = 10001
    find_primes(n)

if __name__ == "__main__":
    main()
