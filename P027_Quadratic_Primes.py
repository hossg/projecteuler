# Euler discovered the remarkable quadratic formula:  n^2+n+41
#
# It turns out that the formula will produce 40
# primes for the consecutive integer values 0≤n≤39.
#
# However, when n=40, 40^2+40+41=40(40+1)+41 n = 40 ,
# is divisible by 41, and certainly when n=41,41^2+41+41
# is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive
# values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:  n^2+an+b , where |a|<1000 and |b|≤1000
# where |n| is the modulus/absolute value of n n  e.g. |11|=11  and |−4|=4
#
# Find the product of the coefficients, a and  b , for the quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n=0.0


# Approach/notable constraints on the ranges of the various parameters:
#
# First, we need consecutive primes from n=0, so as soon as we get a non-prime, we can move onto the next value of a,b
# and we don't need to look for more strings of primes at higher values of n for the same a,b.
#
# Second, because n=0 must yield a prime (the first prime) in our search for prime sequences, b must itself be a
# positive prime
#
# Third because the function itself must evaluate to a prime (for values of interest to us), which is positive
# n^2 + an + b > 0 so b > -(n^2+an) -> b > -n(n+a), so when a is negative, b > |a| is a further constraint
#

import logging, os, math

expectedAnswer = -59231

def getPrimesLessThan(N):


    candidates =  [2] + [c for c in range(3,N,2)]


    for n in range(3,int(math.sqrt(N))+1):
        #print(candidates)   # show the reducing set of candidates
        for c in candidates:
            if c != n and c % n == 0:
                candidates.remove(c)

    return candidates


# Not efficient from a memory perspective, (this algo returns an array of N booleans indicating whether the integer at that
# index is prime or not), but it does allow for fast lookups for primality, hence in situations with recursive or other
# large numbers of lookups this can improve performance compared with seeing if a number is in a sequence or other set
# of primes
def getBooleanPrimesLessThan(stop):
    primes = [True] * stop
    primes[0], primes[1] = [False] * 2
    L = []
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)
            L.append(ind)
    return primes



def solution():

    maxA = 999
    minA = -maxA
    maxB = 1000
    minB = 2  # Follows from constraint 2, b must be a positive prime

    m = f(maxA,maxB,500)

    logging.debug("Max possible prime is below {}".format(m))
    logging.debug("Finding all possible primes below {}".format(m))
    primes = getBooleanPrimesLessThan(m)   # all the primes we need to test against

    logging.debug("Initializing counters")
    maxPrimeSequence=0
    currentMaxPrimeSequence=0
    maxPrimeN=0
    maxPrimeA=0
    maxPrimeB=0

    logging.debug("Scanning from (a,b)=({},{}) to (a,b)]({},{})".format(minA,minB,maxA,maxB))


    for a in range(minA,maxA+1):
        startB = minB
        if a<0:
            startB = -a # see constraint 2
        for b in range(startB,maxB+1):
            if primes[b] == False:
                continue
            logging.debug("Checking {},{}".format(a,b))

            limit = b
            for n in range (limit):
                c=f(a,b,n)

                if(c>0):
                    if primes[c] == True:
                        logging.debug("Found prime ({},{}),{}: ".format(a,b,n))
                        currentMaxPrimeSequence += 1
                        if currentMaxPrimeSequence > maxPrimeSequence:
                            maxPrimeSequence=currentMaxPrimeSequence
                            maxPrimeN=n
                            maxPrimeA=a
                            maxPrimeB=b
                            logging.debug("New longest sequence of primes: n={}, {} long sequemce".format(n,maxPrimeSequence))
                    else:
                        currentMaxPrimeSequence=0
                        break   # Follows from constraint 1 - as soon as we hit a non-prime, we can move to the next a,b
            currentMaxPrimeSequence=0

    logging.info("Result: n={} produces {} consecutive primes at (a,b)=({},{})".format(maxPrimeN,maxPrimeSequence, maxPrimeA, maxPrimeB))

    result = maxPrimeA*maxPrimeB


    return result

def f(a, b, n):
    return ((pow(n, 2) + a*n) + b)




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    solution = solution()
    logging.info('Solution = {}'.format(solution))
    assert (solution == expectedAnswer)