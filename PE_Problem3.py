# File: PE_Problem3.py
#
#   Finds the largest prime factor of a number
#
import scipy
import sys

def find_primes(n):
    # Finds all the primes up to the number n using a Sieve of Erastosthenes
    # Algorithm.
    #print "In find_primes"
    prime_factors = []
    divisor = 2
    '''
        This loop runs first through with divisor = 2. Each time through the
        inner while loop, n is divided by 2. By the time the inner loop reaches
        the point where it is no longer evenly divisible by 2, all even
        factors are removed. The divisor is increased by one to 3, and the
        process is repeated until it is no longer divisible by 3. Next number
        would be 5 since n would not be divisible by 4, since it isn't by 2.
        Etc...

    '''
    while n > 1:
        while n % divisor == 0:
            if divisor not in prime_factors:
                prime_factors.append(divisor)
            n = n / d
        divisor += 1
##        if d*d > n:
##            if n > 1:
##                prime_factors.append(n)
##                break
    return prime_factors

def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        print 'Error -- Usage: ' + str(sys.argv[0]) + ' <number to factor>'
        exit(0)
    primes_list = find_primes(n)
    print "\n"
    print primes_list[-1]

if __name__ == "__main__":
    main()
