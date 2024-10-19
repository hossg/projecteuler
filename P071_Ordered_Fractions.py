# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer=428570

import logging,os

import math

def find_fraction(limit):
    closest_numerator = 0
    closest_denominator = 1
    target_numerator = 3
    target_denominator = 7

    for denominator in range(2, limit + 1):
        # Find the largest numerator n such that n/d < 3/7
        numerator = (target_numerator * denominator - 1) // target_denominator

        # Check if the fraction is reduced
        if math.gcd(numerator, denominator) == 1:
            # Check if this fraction is closer to 3/7 than the current best
            if numerator * closest_denominator > closest_numerator * denominator:
                closest_numerator = numerator
                closest_denominator = denominator

    return closest_numerator, closest_denominator


# This function calculates the answer and returns it
def solution():

    limit = 1000000
    numerator, denominator = find_fraction(limit)
    logging.debug(f"The fraction just to the left of 3/7 is {numerator}/{denominator}")

    return numerator

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
    