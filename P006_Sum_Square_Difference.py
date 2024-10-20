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
expectedAnswer = 25164150
import os
import logging



def sumSquareDifference(n):
    sumSquares, sum = 0, 0

    for i in range(n + 1):
        sumSquares += pow(i, 2)
        sum += i
    squareSums = pow(sum, 2)

    return squareSums - sumSquares


def solution():
    ssd100 = sumSquareDifference(100)
    return ssd100


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
