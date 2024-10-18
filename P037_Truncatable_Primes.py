# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import logging
expectedAnswer=748317

def truncateLeft(n):
    s=str(n)
    s=s[1:]
    return int(s)

def truncateRight(n):
    return int(n/10)

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


def isLeftTruncateable(candidatePrimes,n):
    if(candidatePrimes[n-2]==0):
        return False
    if(n in invalidSingleDigitPrimes):
        return True
    m=truncateLeft(n)
    t= isLeftTruncateable(candidatePrimes,m)
    if t==False:
        candidatePrimes[m-2]=0
    return t

def isRightTruncateable(candidatePrimes,n):
    if(candidatePrimes[n-2]==0):
        return False
    if(n in invalidSingleDigitPrimes):
        return True
    m=truncateRight(n)
    t= isRightTruncateable(candidatePrimes,m)
    if t==False:
        candidatePrimes[m-2]=0
    return t

def solution():

    # We are told that there are 11 solutions to this problem, so by experiment we increase the total search space
    # to 1,000,000 until we confirm that we have 11 solutions.

    # Find all primes that are Right Truncatable
    candidatePrimes=sieve(1000000)
    for i in candidatePrimes:
        if not isRightTruncateable(candidatePrimes,i):
            candidatePrimes[i-2] = 0
    rtp = [x for x in candidatePrimes if x!=0]


    # Find all primes that are Left Truncatable
    candidatePrimes=sieve(1000000)
    for i in candidatePrimes:
        if not isLeftTruncateable(candidatePrimes,i):
            candidatePrimes[i-2] = 0
    ltp = [x for x in candidatePrimes if x!=0]


    # Find all primes that are in both sets
    truncateablePrimes=[x for x in ltp if x in rtp]
    for i in invalidSingleDigitPrimes:
        truncateablePrimes.remove(i)
    logging.debug('After left truncating primes: {}'.format(truncateablePrimes))
    logging.debug('{} truncatable primes found.'.format(len(truncateablePrimes)))
    total = 0
    for i in truncateablePrimes:
        total += i
    return total

invalidSingleDigitPrimes=[2,3,5,7]
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution=solution()
    assert (solution==748317)
    logging.info('Solution = {}'.format(solution))









