# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

def getC(a,b):
    return 1000 - a - b

def solution():
    for a in range(1,1000):
        for b in range (1,1000-a):
            c = getC(a,b)
            a2 = pow(a,2)
            b2 = pow(b,2)
            c2 = pow(c,2)
            if (a2+b2)==c2:
                s=a*b*c
                assert((s)==31875000)
                logger.info('solution = {}'.format(s))
                return s


if __name__ == "__main__":
    solution()
