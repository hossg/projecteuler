# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

# put the expected answer here
expectedAnswer=26241

import logging, math, timeit, time, psutil, platform, os

def get_diagonals(square_size):
    d4=square_size**2
    diff = square_size-1
    d3=d4-diff
    d2=d3-diff
    d1=d2-diff
    return (d1,d2,d3,d4)

def get_prime_diagonals(square_size, primes_list):
    result=[]
    ds = get_diagonals(square_size)
    for d in ds:
        if primes_list[d] != 0: # change to d-2 if using python sieve implementation below
            result.append(d)
    return result


# Eratosthenes Primes algorithm
# This was too slow for practical use, hence I switched to using the external primesieve library
# Note - the sparse array this returns is 2-based rather than 0-based with the alternate implementation
# so you can't simply swap one for the other, instead you need to change the indexing/lookup in the checking
# function above to look at d-2
def sieve(upperlimit):
    # mark off all multiples of 2 so we can use 2*p as the step for the inner loop
    l = [2] + [x if x % 2 != 0 else 0 for x in range(3, upperlimit + 1)]

    for p in l:
        if p ** 2 > upperlimit:
            break
        elif p:
            for i in range(p * p, upperlimit + 1, 2 * p):
                l[i - 2] = 0

    return l    # rather than return ONLY the primes, return primes and non-primes to allow super-fast, index-based
                # lookup of primes later on



import numba
import numpy
import timeit
import datetime 

@numba.jit(nopython = True, parallel = True, fastmath = True, forceobj = False)
def sieve2(n: int) -> numpy.ndarray:
    primes = numpy.full(n, True)
    primes[0], primes[1] = False, False
    for i in numba.prange(2, int(numpy.sqrt(n) + 1)):
        if primes[i]:
            primes[i*i::i] = False
    return numpy.flatnonzero(primes)


import subprocess

def solution():
    # just a placeholder for where the solution to the problem will be stored and then returned
    solution=987654321

    max_square_size=40000 # increased this by trial and error until I generated a big enough square
    logging.debug('Preparing primes')

    # Rather than use a home-built sieve method in Python, make use of primesieve library
    # I did try to install pyprimesieve with a python/native interface but couldnt get it to install on my Mac
    # Instead just do an ugly hack and call the tool via the command line and capture the output
    # x = subprocess.run(['primesieve', '-p', str(max_square_size**2)], stdout=subprocess.PIPE).stdout.decode('utf-8')
    # y = x.split('\n')   # primesieve returns one prime per line
    # z = y[:-1]          # and an irritating additional newline at the end
    # primes = [int(n) for n in z]
    primes = sieve2(max_square_size**2)
    # now generate a sparse array to contain the primes - this massively optimises prime-lookup speed compared with
    # simply doing  if x in y list lookup
    max_prime = primes[-1]
    sparse_primes=[0]*(max_prime+1)
    for i in primes:
        sparse_primes[i]=i

    prime_diagonals=[]
    logging.debug('Looking for prime diagonals primes')
    for i in range(3,max_square_size,2):
        prime_diagonals+=(get_prime_diagonals(i,sparse_primes))
        n_diagonals = 2 * i - 1
        prime_ratio=len(prime_diagonals)/n_diagonals
        logging.debug('Square Size: {}, Prime Ratio: {}, Primes: {}'.format(i,prime_ratio,prime_diagonals))
        if prime_ratio < 0.1:
            solution = i
            break

    return solution


# Utility function for measuring the performance of solutions
processtime=0.0
walltime=0.0
def stopwatch():
    global walltime, processtime
    wt=time.time()
    ct=time.clock()
    wtElapsed=wt-walltime
    ctElapsed=ct-processtime
    walltime=wt
    processtime=ct
    return('Elapsed process time:{}s, Elapsed clock time:{}s'.format(ctElapsed,wtElapsed))

def getsysteminfo():
    p=platform.platform()+' ' +platform.processor()+' Python: '+platform.python_version()
    memory=psutil.virtual_memory()
    cpuc=psutil.cpu_count()
    cpup=psutil.cpu_count(logical=True)
    cpuf=psutil.cpu_freq()
    cput=psutil.cpu_times_percent(percpu=False)

    return 'Platform: {}, Memory: {} Physical CPUs: {}, Logical CPUs: {}, Frequency (MHz): {}, Utilisation: {}'.format\
        (p,memory,cpuc,cpup,cpuf,cput)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logging=logging.getLogger(os.path.basename(__file__))
    stopwatch() #start timing
    solution = solution()
    timetaken=stopwatch() #stop timing
    assert (solution == expectedAnswer)
    logging.info('Solution = {}'.format(solution))
    logging.info(timetaken)
    logging.info('System info: {}'.format(getsysteminfo()))

