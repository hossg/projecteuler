# put the expected answer here
expectedAnswer=1322

import logging, math, timeit, time, psutil, platform, os

def continued_fraction_sqrt(N):
    # Initial integer part of the square root
    a0 = int(N**0.5)

    # If N is a perfect square, return the single integer as its continued fraction representation
    if a0 * a0 == N:
        return a0, []

    # Initialize variables
    m = [0]
    d = [1]
    a = [a0]

    # Limit iterations to avoid infinite loops in our code
    for _ in range(1000):
        # Calculate the next terms
        m_next = d[-1] * a[-1] - m[-1]
        d_next = (N - m_next**2)

        # Check if division by zero might occur
        if d_next == 0:
            break  # Exit the loop since we cannot continue

        d_next //= d[-1]  # Perform integer division
        a_next = (a0 + m_next) // d_next

        # Append new values
        m.append(m_next)
        d.append(d_next)
        a.append(a_next)

        # Check if the sequence starts to repeat
        if a[-1] == 2 * a0:
            break

    return a0, a[1:]

def solution():
    count_odd_periods=0
    for n in range(2,10001):
        a=continued_fraction_sqrt(n)[1]  
        if len(a)%2==1:
            count_odd_periods+=1
    return count_odd_periods

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
 