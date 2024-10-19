# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer=8319823

import logging,os
import P069_Totient_Maximum


# This function calculates the answer and returns it
def solution():
    logging.debug('Generating totients upto 10^7')
    totients = P069_Totient_Maximum.compute_totients(10000000)
    # logging.debug(totients)
    # for n in range(87100,87119):
    #     logging.debug(f't({n})={totients[n-1]}')
    min_ratio = 100000000000
    min_n = 1
    for n,t in enumerate(totients,start=1):

        n_s = sorted(str(n))
        t_s = sorted(str(t))
        if n_s == t_s:
            logging.debug(f'phi({n})={t} n/t = {n/t}')
            if n>1 and n/t < min_ratio:
                min_ratio = n/t
                min_n = n
                logging.debug(f'New lowest ratio found for n={n}')

    return min_n

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
    