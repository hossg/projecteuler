# A perfect number is a number for which the sum of its proper divisors is exactly equal
# to the number. For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it
# is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that
# can be written as the sum of two abundant numbers is 24. By mathematical analysis, it
# can be shown that all integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of
# two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two
# abundant numbers.

import os
import logging
expectedAnswer = 4179871

logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

import math

divisors = __import__("P012_Highly_Divisible_Triangular_Number")

def isAbundant(N):
    d = divisors.divisors(N)
    d = [n for n in d if n != N]  # need to remove N itself form the this implementation, i.e. "proper divisors" only

    if sum(d) > N:
        return True
    else:
        return False

def solution():
    # build the list of abundants
    limit=28123
    abundants=[]
    for i in range (1,limit):
        if isAbundant(i):
            abundants.append(i)

    # now build the list of all sums of abundants in this range
    abundantComposites=[]
    for n in abundants:
        for j in abundants:
            abundantComposites.append(n+j)
    abundantComposites=sorted(set(abundantComposites))  #remove the duplicates

    # now build a list that doesn't include those abundant composites
    nonAbundantComposites=[c for c in range(1,limit) if c not in abundantComposites]
    sumOfNonAbundantComposites = sum(nonAbundantComposites)
    logger.info('solution = {}'.format(sumOfNonAbundantComposites))
    assert(sumOfNonAbundantComposites==4179871)
    return sumOfNonAbundantComposites

if __name__ == "__main__":
    solution()