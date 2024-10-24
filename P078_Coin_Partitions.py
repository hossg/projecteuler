# Let p(n)
#  represent the number of different ways in which
#  coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7
# .
#
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n
#  for which p(n)
#  is divisible by one million.

# A bit of a naive approach perhaps. Wiki shows some interesting approaches using pentagonal numbers, but
# the proof of that is beyond me, so simply implementing an algorithm I don't understand seems pointless.

# Put the expected answer here
expectedAnswer=55374

import logging,os
import itertools



# This function calculates the answer and returns it
def solution():
    # Define the target number
    target = 100000

    # Create a list to store the number of ways to partition each number
    partitions = [0] * (target + 1)
    partitions[0] = 1  # Base case: only one way to partition 0

    # Dynamic programming to calculate partitions
    for i in range(1, target + 1):
        for j in range(i, target + 1):
            partitions[j] += partitions[j - i]

    # The answer is the number of ways to partition 100 minus 1 (excluding the partition [100])

    for i in range (len(partitions)):
        if partitions[i] % 1000000 == 0:
            return i





if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    sol = solution()
    logging.info('Solution = {}'.format(sol))
    assert (sol == expectedAnswer)
    