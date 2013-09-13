# File: PE_Problem5.py
#
# Finds the smallest number evenly divisible by all positive integers less
# than or equal to 20


def prime_factorization(number,factors_dict):
    # Finds the prime factorization of a number
    n = number
    factors_list = []
    n_dict = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors_list.append(divisor)
            n /= divisor
        divisor += 1
        if divisor**2 > n and n > 1:
            factors_list.append(n)
            break
    while factors_list != []:
        if str(factors_list[0]) in n_dict:
            n_dict[str(factors_list[0])] += 1
        else:
            n_dict[str(factors_list[0])] = 1
        factors_list.pop(0)
    factors_dict[str(number)] = n_dict
    

def main():
    n = 20
    factors_dict = {}
    largestPower = {}
    final_number = 1
    for i in range(2,n+1):
        prime_factorization(i,factors_dict)
        if i == 16:
            print factors_dict[str(i)]
    #print factors_dict
    for number in factors_dict:
        for factor in factors_dict[number]:
            if factor in largestPower:
                if factors_dict[number][factor] > largestPower[factor]:
                    largestPower[factor] = factors_dict[number][factor]
            else:
                largestPower[factor] = factors_dict[number][factor]
    #print largestPower
    for val in largestPower:
        final_number *= int(val)**largestPower[val]

    print final_number
   

if __name__ == "__main__":
    main()
