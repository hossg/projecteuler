# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000

import os
import logging

expectedAnswer = 1366

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


def solution():
    x = pow(2, 1000)
    s = str(x)
    digitSum = 0
    for d in s:
        digitSum += int(d)
    assert (digitSum == 1366)
    logger.info('solution = {}'.format(digitSum))
    return digitSum


if __name__ == "__main__":
    solution()
