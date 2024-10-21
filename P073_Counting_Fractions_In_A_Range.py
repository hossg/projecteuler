# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer = 7295372

import logging, os
from math import gcd

# This function calculates the answer and returns it


def count_fractions(limit):
    count = 0
    for d in range(2, limit + 1):
        # Calculate the lower and upper bounds for the numerators
        lower_bound = d // 3 + 1  # We need the smallest n such that n/d > 1/3
        upper_bound = (d - 1) // 2  # We need the largest n such that n/d < 1/2
        for n in range(lower_bound, upper_bound + 1):
            if gcd(n, d) == 1:  # Check if fraction is reduced (coprime)
                count += 1
    return count


def solution():
    limit = 12000
    result = count_fractions(limit)
    logging.debug(
        f"The number of reduced proper fractions between 1/3 and 1/2 for d ≤ {limit} is {result}."
    )
    return result


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging = logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
