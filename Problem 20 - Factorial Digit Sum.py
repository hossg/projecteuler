# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

import math

def solution():
    n = math.factorial(100)
    s=str(n)
    sum = 0
    for c in s:
        sum += int(c)
    assert(sum==648)
    logger.info('solution = {}'.format(sum))
    return sum

if __name__ == "__main__":
    solution()