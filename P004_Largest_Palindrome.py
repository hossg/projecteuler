# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import os
import logging
logger=logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')


def isPalindrome(N):
    S=str(N)
    R=S[::-1]
    if R==S:
        return True
    else:
        return False


def getPalindromes():
    palindromes = []
    for x in range(999,100,-1):
        for y in range(999,100,-1):
            if isPalindrome(x * y):
                palindromes.append(x * y)
    return palindromes


def solution():
    m=max(getPalindromes())
    logger.info("solution = {}".format(m))
    assert (m == 906609)
    return m

if __name__ == "__main__":
    solution()