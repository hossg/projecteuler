# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
expectedAnswer = 104743
import os
import logging
import math

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


# Eratosthenes Sieve
def getPrimesLessThan(N):

    candidates = [2] + [c for c in range(3, N, 2)]

    for n in range(3, int(math.sqrt(N)) + 1):
        #print(candidates)   # show the reducing set of candidates
        for c in candidates:
            if c != n and c % n == 0:
                candidates.remove(c)

    return candidates


def isPrime(n):
    primes = getPrimesLessThan(n)
    return n in primes


def NthPrime(n):
    # from the Prime Number theorem
    #Nth prime is approx N.log(N) = 10, 000 * log(10, 000)
    maxPrime = int(
        n * math.log10(n)
    ) * 6  #  a very crude factor to allow for the factthat maxPrime is just an approximation, so we need to make sure we don't run out of space
    primes = getPrimesLessThan(maxPrime)
    return primes[n - 1]  # to allow for 0-based indexing in Python


def solution():
    s = NthPrime(10001)
    logger.debug('solution = {}'.format(s))
    return s


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
