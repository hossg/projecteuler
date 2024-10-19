# Put the problem description here, including a link to the problem on the website if available.

# Euler's totient function, Phi, [sometimes called the phi function], is defined as the number of positive integers not exceeding n which are relatively prime to n. For example, as 1,2,4,5,7,8 are all less than or equal to nine and relatively prime to nine, phi(9)=6

 # n  Relatively Prime     Phi(n) n/Phi(n)	
 # 2	1	                    1	2
 # 3	1,2	                    2	1.5
 # 4	1,3	                    2	2
 # 5	1,2,3,4	                4	1.25
 # 6	1,5	                    2	3
 # 7	1,2,3,4,5,6	            6	1.1666...
 # 8	1,3,5,7	                4	2
 # 9	1,2,4,5,7,8	            6	1.5
 # 10	1,3,7,9	                4	2.5

# It can be seen that n=6 produces a maximum n/Phi(n) for n<=10.
# Find the value of n <=1000000 for which n/Phi(n) is a maximum. 
# Ref: https://projecteuler.net/problem=69
 
# Put the expected answer here
expectedAnswer=510510

import logging, os

def compute_totients(up_to):
    # Initialize the phi array
    phi = list(range(up_to + 1))
    # Implement the sieve for Totient function
    for i in range(2, up_to + 1):
        if phi[i] == i:  # i is a prime
            for j in range(i, up_to + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i
    
    return phi[1:]

def n_over_phi(phis):
    return [n / p for n, p in zip(range(1, len(phis)), phis)]    

# This function calculates the answer and returns it
def solution():
    #implement solution to the problem here
    phis = compute_totients(1000000)
    logging.debug(f'Phi values: {phis}')
    n_p = n_over_phi(phis)
    logging.debug(f'n/phi values: {n_p}')
    max_n_p = max(n_p)
    solution=n_p.index(max_n_p)+1
    return solution

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)
    