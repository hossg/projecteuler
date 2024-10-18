# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import logging

expectedAnswer = 872187

def binary(n):
    return "{0:b}".format(n)

def isPalindrome(s):
    if s[::-1]==s:
        return True
    else:
        return False


def solve(max):
    palindromes=[]
    for n in range (max):
        if isPalindrome(str(n)):
            b=binary(n)
            if isPalindrome(b):
                logging.debug('{} is {} and both are palindromes.'.format(n,b))
                palindromes.append(n)
    total=0
    for i in palindromes:
        total+=i
    return total

def solution():
    return solve(1000000)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution=solve(1000000)
    assert (solution==872187)
    logging.info('Solution = {}'.format(solution))
