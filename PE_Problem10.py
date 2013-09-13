# File: PE_Problem10.py
#
# Finds all the primes below n and finds their sum

import scipy

def find_primes(n):
    prime_markers = scipy.zeros(n+1)
    primes_list = []
    prime_markers[0] = 1
    prime_markers[1] = 1

    for i in range(2,n+1):
        j = i
        while (i*j) <= n:
            prime_markers[i*j] = 1
            j += 1

    for i in range(2,n):
        if prime_markers[i] == 0:
            primes_list.append(i)

    return sum(primes_list)

def main():
    n = 2000000

    prime_sum = find_primes(n)
    print prime_sum

if __name__ == "__main__":
    main()
