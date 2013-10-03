# File: PE_Problem16.py
#
# Finds the sum of the digits of 2^1000

def main():
    n = 2**1000
    nSum = 0
    for i in str(n):
        nSum += int(i)
    return nSum

if __name__ == "__main__":
    print main()
