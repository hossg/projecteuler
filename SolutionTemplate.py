# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer=123456789

import logging,os

# This function calculates the answer and returns it
def solution():

    return 123456789

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    sol = solution()
    logging.info('Solution = {}'.format(sol))
    assert (sol == expectedAnswer)
    