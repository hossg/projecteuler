# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import os
import logging

expectedAnswer = 142913828922

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

import P027_Quadratic_Primes as prime2

def solution():
    primes2 = prime2.getBooleanPrimesLessThan(2000000)
    runningsum = 0
    for i in range(len(primes2)):
        if primes2[i]: runningsum += i

    logging.debug(f'boolean approach: {runningsum}')
    return runningsum


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
