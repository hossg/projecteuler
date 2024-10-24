# Put the problem description here, including a link to the problem on the website if available.

# Put the expected answer here
expectedAnswer=71

import logging,os



def sieve_of_eratosthenes(limit):
    """ Returns a list of primes up to the limit using the Sieve of Eratosthenes. """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]


def count_prime_sums(target, primes):
    """ Count the ways to express integers as sums of primes. """
    ways = [0] * (target + 1)
    ways[0] = 1  # Base case: one way to make zero

    for prime in primes:
        for j in range(prime, target + 1):
            ways[j] += ways[j - prime]

    return ways


def find_min_integer(target_ways):
    """ Find the smallest integer that can be expressed as the sum of primes in more than target_ways ways. """
    limit = 100  # Initial limit for primes
    primes = sieve_of_eratosthenes(limit)

    while True:
        ways = count_prime_sums(limit, primes)

        for i in range(len(ways)):
            if ways[i] > target_ways:
                return i,ways[i]

        # A bit inefficient, but if we didn't start with a big enough number of primes, then start again with double the amount!
        limit *= 2
        primes = sieve_of_eratosthenes(limit)





# This function calculates the answer and returns it
def solution():
    # Set the target number of ways
    target_ways = 5000
    result = find_min_integer(target_ways)
    return result[0]

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    sol = solution()
    logging.info('Solution = {}'.format(sol))
    assert (sol == expectedAnswer)
    