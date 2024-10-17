# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Approach:
#
# Loop n from 2 to N
# if N % n == 0 then n is a factor, so record this fact
# we can then proceed again from a new starting point - the quotient of that trial division
# and we can continue from the SAME n (since it may divide again), but anything smaller cannot be a factor
# as we've already tried it for the larger composite number
#
# We don't need to test for primality since by repeating the process we will decompose all
# numbers into their prime factors

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

def isFactor(N,n):
    if N % n ==0:
        return True
    else:
        return False

def factorize(N, startFrom = 2):
    logger.debug("factoring {}, starting from {}".format(N,startFrom))
    factors=[]
    i = startFrom

    while i <= N:
        if isFactor(N,i):
            factors.append(i)
            factors += factorize(int(N/i),i)
            break
        i += 1
    return factors

def solution():
    factors = factorize(600851475143)
    m = max(factors)
    logger.info("solution = {}".format(m))
    assert(m==6857)
    return m

if __name__ == "__main__":
    solution()