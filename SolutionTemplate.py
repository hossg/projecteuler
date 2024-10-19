# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer=123456789

import logging,os

# This function calculates the answer and returns it
def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321

    #implement solution to the problem here
    time.sleep(1)

    return solution

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
    