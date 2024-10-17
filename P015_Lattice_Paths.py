# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?


# Solution:
# To get to the bottom right of an N*N grid, we have to take N steps to the right and N steps down, i.e. 2N steps
# in total, and in any order, for example RDRD, RRDD, RDDR, DRRD, DRDR, DDRR for a 2x2 grid
#
# Recognizing that we need the 2N-step process to have N R's and N D's we see that we need the number of combinations
# D's and R's.  On first glance this appears as if it would be (2N)! but given that each of the D's are
# indistinguishable, and so are each of the R's, we need to reduce the final combination-count by the appropriate
# amount, giving: (2N)!/(N!*N!)

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

import math

def routes(gridSize):
    r = math.factorial(gridSize*2)/(math.factorial(gridSize)*math.factorial(gridSize))
    return int(r)

def multiSolution():
    for i in range(1,21):
        logger.info("Gridsize: {}, routes: {}".format(i,routes(i)))

def solution():
    s=routes(20)
    assert(s==137846528820)
    logger.info('solution = {}'.format(s))
    return s


if __name__ == "__main__":
    solution()