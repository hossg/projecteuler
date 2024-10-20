# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Is this not the same as the smallest common multiple of the primes under 20?
# but we then need to allow for those numbers under 20 that require more than a single one of the preceding primes
# to form them as a composite number to make sure we have "enough" of each prime
# specifically we need 4 2's to get 16, and 2 3's to get 9


expectedAnswer = 232792560
import os
import logging
import math

logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result

def solution():
    x = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 2 * 2 * 2 * 3
    numbers = range(1, 21)
    result = lcm_multiple(numbers)
    return result


if __name__ == "__main__":
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)