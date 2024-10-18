# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math, logging
expectedAnswer = 40730
def sumOfDigitFactorial(n):
    s=str(n)
    total = 0
    for d in s:
        total += math.factorial(int(d))
    return total




def solution():
    results=[]
    for n in range(3,math.factorial(10)):
        s=sumOfDigitFactorial(n)
        logging.debug('sumOfDigitFactorials({})={}'.format(n,s))
        if n==s:
            results.append(n)
    logging.debug('answers: {}'.format(results))
    total=0
    for n in results:
        total+=n
    assert (total==40730)
    return total

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.info('solution={}'.format(solution()))