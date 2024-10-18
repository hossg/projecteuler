# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

import os
import logging
import timeit

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


def yieldNextMultipleOf3or5():
    candidate = 0
    while True:
        if candidate % 3 == 0:
            yield candidate
        elif candidate % 5 == 0:  #Avoid yielding the SAME number (a joint multiple of 3 and 5) and thus double counting
            yield candidate
        candidate += 1


def solution():
    total = 0
    for i in yieldNextMultipleOf3or5():
        #print(i)
        if i < 1000:
            total += i
        else:
            break

    assert (total == 233168)
    return total


expectedAnswer = 233168

if __name__ == "__main__":
    logger.info("Solution = {}".format(solution()))
    n = 10000
    t = timeit.timeit('solution()', number=n, globals=globals())
    logger.info("Time taken = {} ms".format(t * 1000 / n))
