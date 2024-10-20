# Consider the fraction n/d where n and d  are positive integers. If n<d and HCF(n,d)=1 , it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d<=8 in ascending order of size we see that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions for d <= 1000000

# Each reduced proper fraction has n and d that are coprime, so this question is equivalent to calculating Euler's
# totient function for each number up to 1000000 and adding these all together.

# Put the expected answer here
expectedAnswer=303963552391

import logging,os

import math
import P069_Totient_Maximum as t

# This function calculates the answer and returns it
def solution():
    totients = t.compute_totients(1000000)
    # logging.debug(totients)
    return sum(totients)-1 # subtract one since we're ignoring the fraction 1/1

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
    