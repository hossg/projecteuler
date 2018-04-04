

# put the expected answer here
expectedAnswer=123456789

import logging, math

def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321

    #implement solution to the problem here

    return solution


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution = solution()
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))