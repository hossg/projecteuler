# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')


import timeit


fib = __import__('Problem 2 - Fibonacci')

def getFirstNDigitFibonacci(N):
    count = 1                               # seeding this at 1 because this implementation of Fibonacci starts 1,2,3
                                            # so we're essentially skipping the first element of the conventional series
    for n in fib.yieldFibonacci():
        count+=1
        s=str(n)
        if len(s)==N:
            return count,n


def solution():
    solution = getFirstNDigitFibonacci(1000)
    assert(solution[0]==4782)
    logger.info("solution = {}".format(solution[0]))
    return(solution[0])

def time():
    i=100
    t=timeit.timeit('problem25()', globals=globals(), number = 100)
    m="{} iterations completed in {:0.2f}s".format(i,t)
    logger.info(m)

if __name__ == "__main__":
    solution()
    time()