# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import os
import logging
expectedAnswer = 31626

logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

divisors = __import__("P012_Highly_Divisible_Triangular_Number")

def sumDivisors(N):
    d=divisors.divisors(N)
    d=[n for n in d if n!=N] # need to remove N itself form the this implementation, i.e. "proper divisors" only
    return sum(d)

def getSumOfDivisorsInRange(N):
    sumsOfDivisors=[]
    for n in range(N+1):
        sumsOfDivisors.append(sumDivisors(n))
    return sumsOfDivisors

def areAmicable(a,b, lookup):
    dA = lookup[a]
    dB = lookup[b]
    if dA ==b and dB == a:
        return True
    else:
        return False

def solution():
    searchRange=10000+1
    divisorsSummed10000=getSumOfDivisorsInRange(searchRange)
    amicableNumbers=[]
    for a in range(2,searchRange):          #1 is not considered an amicable number
        for b in range(2,searchRange):
            if a!=b:
                if areAmicable(a,b, divisorsSummed10000):
                    logger.debug("Amicable number: {},{}".format(a,b))
                    amicableNumbers.append(a)
                    amicableNumbers.append(b)

    setOfAmicableNumbers=set(amicableNumbers) # to remove the duplicates, i.e. the "reverse pairs"
    s = sum(setOfAmicableNumbers)
    logger.debug(setOfAmicableNumbers)

    return s

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)