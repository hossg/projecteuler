# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are
# themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import math, itertools, logging

knownPrimes=[]

def isPrime(n):
    if n<2:
        return False

    if n==2:
        return True

    if (n%2 == 0):
        return False

    if n in knownPrimes:
        return True

    for p in knownPrimes:
        if (p<n and n%p == 0):
            return False

    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False

    knownPrimes.append(n)
    return True



def solution():

    circularPrimes=[]
    for x in range (1000000):
        if isPrime(x):
            logging.debug('{} is prime'.format(x))
            isCircularPrime=True
            for n in itertools.permutations(str(x)):
                c=int(''.join(n))
                if(c in knownPrimes):
                    logging.debug('{} is prime'.format(c))
                elif (isPrime(c) == False):
                    isCircularPrime=False
                    logging.debug('{} is NOT prime'.format(c))
                else:
                    logging.debug('{} is prime'.format(c))
                    knownPrimes.append(c)

            if isCircularPrime:
                circularPrimes.append(x)
                logging.debug('{} is CIRCULAR prime'.format(x))

    logging.info('Circular Primes: {}'.format(circularPrimes))
    return len(circularPrimes)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging.info('Solution = {}'.format(solution()))