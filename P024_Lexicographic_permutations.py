# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2,
# 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

import itertools

def solution():
    s='0123456789'
    m=(next(itertools.islice(itertools.permutations(s, 10),999999,1000000))) # items are zero-based, so we want item 999999
    ms=''.join(m)
    logger.info('solution = {}'.format(ms))
    assert(ms=='2783915460')
    return ms


if __name__ == "__main__":
    solution()