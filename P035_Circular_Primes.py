# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are
# themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import math, itertools, logging

expectedAnswer = 55

# Eratosthenes Primes algorithm
def sieve(upperlimit):
    # mark off all multiples of 2 so we can use 2*p as the step for the inner loop
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    return l    # rather than return ONLY the primes, return primes and non-primes to allow super-fast, index-based
                # lookup of primes later on

    # filter out non primes from the list, not really that important i could work with a list full of zeros as well
    # return [x for x in l if x]

# Produce a list with all circular rotations of an integer
def rotate(s):
    l=str(s)
    x = [int(l[n:] + l[:n]) for n in range(len(l))]
    return x

def solve(upto):
    primes = sieve(upto)
    circularPrimes=[]

    for p in [x for x in primes if x!=0]:           # For each prime...
        isCircularPrime = True                      # assume it's one of a circular group.
        for n in rotate(p):                         # For each of it's rotated partners...
            if primes[n-2]==0:                      # check to see if THAT is prime
                isCircularPrime = False             # and if not, invalidate our assumption.
                break
        if isCircularPrime == True:                 # If every one of the circular group is prime, then
            circularPrimes.append(p)                # we've found a group of circular primes

                                                    # We could optimise this further by pre-checking to see if
                                                    # a prime is already in the circular primes list, since that
                                                    # list will be very much smaller than the list of all primes

    logging.debug('Circular Primes: {}'.format(circularPrimes))
    return len(circularPrimes)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution = solve (1000000)
    assert (solution==55)
    logging.info('Solution = {}'.format(solution))

def solution():
    return solve(1000000)

