# File: PE_Problem1.py

def multiples(n):
    multiples_list = []
    for i in range(1,n):
        if i % 3 == 0 and i not in multiples_list:
            multiples_list.append(i)
        elif i % 5 == 0 and i not in multiples_list:
            multiples_list.append(i)
    #print multiples_list
    return sum(multiples_list)

def main():
    n = 1000

    sum_of_multiples = multiples(n)
    print sum_of_multiples


if __name__ == "__main__":
    main()
