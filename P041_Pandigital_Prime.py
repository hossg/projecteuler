#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
# 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?



# Eratosthenes Primes algorithm
import logging

expectedAnswer = 7652413

def sieve(upperlimit):
    # mark off all multiples of 2 so we can use 2*p as the step for the inner loop
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    # return l    # rather than return ONLY the primes, return primes and non-primes to allow super-fast, index-based
                # lookup of primes later on

    # filter out non primes from the list, not really that important i could work with a list full of zeros as well
    return [x for x in l if x]

def isPandigital(s):
    st=sorted(s)
    if ''.join(st) == "123456789"[:len(s)]:
        return True
    else:
        return False



def solution():
    # sum of digits 1-9 is 45 which is divisble by 9 and 3, so any n=9 pandigital cannot be a prime
    # sum of digits 1-8 is 26 which is divisible by 3, so any n=8 pandigital cannot be a prime
    # this allows us to hugely reduce the search space of primes we need to generate
    logging.debug('Preparing primes')
    primes=sieve(7654321)
    logging.debug('Scanning primes')
    for i in range(len(primes)):
        p = primes.pop()
        if isPandigital(str(p)):
            logging.debug('Found largest pandigital prime: {}'.format(p))
            return p
        else:
            logging.debug('{} is not pandigital'.format(p))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    solution = solution()
    assert (solution == 7652413)
    logging.info('Solution = {}'.format(solution))