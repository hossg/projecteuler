# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer = 190569291

import logging, os


# This function calculates the answer and returns it
def solution():
    # Define the target number
    target = 100

    # Create a list to store the number of ways to partition each number
    partitions = [0] * (target + 1)
    partitions[0] = 1  # Base case: only one way to partition 0

    # Dynamic programming to calculate partitions
    for i in range(1, target + 1):
        for j in range(i, target + 1):
            partitions[j] += partitions[j - i]

    # The answer is the number of ways to partition 100 minus 1 (excluding the partition [100])
    return partitions[target] - 1


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging = logging.getLogger(os.path.basename(__file__))
    s = solution()
    logging.info('Solution = {}'.format(s))
    assert (s == expectedAnswer)
