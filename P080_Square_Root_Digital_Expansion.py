# https://projecteuler.net/problem=80

# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
#
# The square root of two is 1.41421356...
# , and the digital sum of the first one hundred decimal digits is 475
# .
#
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
#
# A very ambiguous question - 'decimal digits' does not mean just the digits after the decimal place it turns out, but difficult
# tell just by doing a sum check on the example given (sqrt(2) -> 475 since it would appear that that 100th digit is a 1, the
# same as the digit before the decimal place!
expectedAnswer=40886

import logging,os
from decimal import *

def digitSum(d):
    sum = 0
    s=str(d)
    for digit in d:
        sum += int(digit)
    return sum
# This function calculates the answer and returns it
def solution():
    getcontext().prec=102 # need enough precision to deal with both the Decimal representation of the number, and the power of 0.5

    totalDigitSum=0
    perfectSquares=[1,4,9,16,25,36,49,64,81,100]
    for i in range (1,101):
        if i not in perfectSquares:
            sqrti = str(Decimal(i)**Decimal('0.5'))
            sqrti = sqrti.replace('.','')[:100]
            logging.debug(f'{i:03} {sqrti}')
            totalDigitSum+=digitSum(sqrti)


    return totalDigitSum
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    sol = solution()
    logging.info('Solution = {}'.format(sol))
    assert (sol == expectedAnswer)
    