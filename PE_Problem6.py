# File: PE_Problem6.py
#
# Finds the difference between the sum of n numbers squared, and the sum of
# those n numbers squared. I.E. (1+2+...+n)^2 - (1^2 + 2^2 + ... + n^2)

def main():
    n = 100
    values = []
    squared_values = []
    for i in range(1,n+1):
        values.append(i)
        squared_values.append(i**2)
    sum_squared = sum(values)**2
    sum_of_squares = sum(squared_values)

    difference = sum_squared - sum_of_squares
    print difference

if __name__ == "__main__":
    main()
