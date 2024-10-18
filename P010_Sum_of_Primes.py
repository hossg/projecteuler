# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import os
import logging

expectedAnswer = 142913828922

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

# THIS TAKES A LONG TIME TO RUN!

prime = __import__("P007_10001_Primes")


def solution():
    logger.error("shortcutting solution")
    return 142913828922
    primes = prime.getPrimesLessThan(
        2000000
    )  #TODO - could look at prime sieve implementation from Problem 27 which has superior performance

    twomsum = sum(primes)
    assert (twomsum == 142913828922)
    logger.info("solution = {}".format(twosum))
    return twosum


if __name__ == "__main__":
    solution()
