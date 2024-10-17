# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the
# sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square
# of the sum.
import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

def sumSquareDifference(n):
    sumSquares, sum = 0,0

    for i in range(n+1):
        sumSquares += pow(i,2)
        sum += i
    squareSums=pow(sum,2)

    return squareSums - sumSquares

def solution():
    ssd100 = sumSquareDifference(100)
    assert(ssd100 == 25164150)
    logger.info('solution = {}'.format(ssd100))
    return ssd100



if __name__ == "__main__":
    solution()