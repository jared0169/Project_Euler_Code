# File: PE_Problem13.py
#
# Determines the first 10 digits of the sum of 100 50-digit numbers

def getNumbers():
    f = open("PE_13_File.txt",'r')
    numbersList = []
    for line in f:
        numbersList.append(int(line))
    return numbersList

def main():
    numbersList = getNumbers()

    sumOfNumbers = sum(numbersList)

    sumString = str(sumOfNumbers)

    print sumString[0:10]
    
    return


if __name__ == "__main__":
    main()
