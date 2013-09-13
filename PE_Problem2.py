#File PE_Problem2.py

import timeit

fibDict = {'0':0,'1':1}

def fib(n):
    #print fibDict
    if fibDict.has_key(str(n)):    
        return fibDict[str(n)]
    else:
        fibDict[str(n)] = fib(n-1) + fib(n-2)
        return fibDict[str(n)]


def main():
    i = 0
    sumFib = 0
    fib_list = []
    while fib(i) < 4000000:
        if fib(i) % 2 == 0:
            fib_list.append(fib(i))
        i += 1

    #print fib_list
##    for i in range(len(fib_list)):
##        if fib_list[i] % 2 == 0:
##            sumFib += fib_list[i]

    return sum(fib_list)
    
