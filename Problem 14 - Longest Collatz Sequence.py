# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

def collatz(startingNumber):
    n=startingNumber
    while True:
        yield n
        if n==1:
            break
        if n % 2 == 0:
            n=int(n/2)
        else:
            n = 3 * n + 1

def solution():
    maxSequence=(1,1)
    for i in range(2,1000000):
        l=len([c for c in collatz(i)])
        if l > maxSequence[1]:
            maxSequence=(i,l)
        logger.debug("{} : {} terms".format(i,l))  # disabled for large runs for performance reasons

    logger.info("max sequence length: collatz({}): {} items".format(maxSequence[0],maxSequence[1]))
    assert(maxSequence[0]==837799)
    return maxSequence[0]

# TODO - need to benchmark this (and all other solutions) and compare with canonical versions available elsewhere

if __name__ == "__main__":
    solution()