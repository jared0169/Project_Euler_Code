# File: PE_Problem14.py
#
# Finds the longest Collatz sequence less than 1 million

# FindSequence takes in the number as the parameter. Finds the Collatz sequence
# for that number and returns both the number and the length of the Collatz
# sequence

def FindSequence(number):
    sequenceLength = 1
    sequenceNumber = number
    while sequenceNumber != 1:
        if sequenceNumber % 2 == 0:
            sequenceNumber /= 2
        else:
            sequenceNumber = 3*sequenceNumber + 1
        sequenceLength += 1
    return number,sequenceLength

def main():
    longestSequence = 1
    longestNumber = 1

    for i in range(2,1000000):
        if i % 10 == 0:
            print i
        number,sequenceLength = FindSequence(i)
        if sequenceLength > longestSequence:
            longestSequence = sequenceLength
            longestNumber = number

    print longestNumber
    return


if __name__ == "__main__":
    main()
